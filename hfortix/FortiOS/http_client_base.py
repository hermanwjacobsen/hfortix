"""
Base HTTP Client - Shared Logic for Sync and Async Clients

This module contains BaseHTTPClient with shared validation, retry logic,
circuit breaker, statistics, and utilities used by both HTTPClient and AsyncHTTPClient.
"""

from __future__ import annotations

import fnmatch
import logging
import time
from collections import deque
from typing import Any, Optional, TypeAlias, Union
from urllib.parse import quote

import httpx

logger = logging.getLogger("hfortix.http.base")

# Type alias for API responses
HTTPResponse: TypeAlias = dict[str, Any]

__all__ = ["BaseHTTPClient", "HTTPResponse"]


class BaseHTTPClient:
    """
    Base class for HTTP clients with shared logic.

    Provides:
    - Parameter validation
    - URL building
    - Retry statistics
    - Circuit breaker state management
    - Endpoint timeout configuration
    - Path normalization and encoding
    - Data sanitization
    """

    def __init__(
        self,
        url: str,
        verify: bool = True,
        vdom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        adaptive_retry: bool = False,
    ) -> None:
        """Initialize base HTTP client with shared configuration

        Args:
            adaptive_retry: Enable adaptive retry with backpressure detection (default: False)
                          When enabled, monitors response times and adjusts retry delays
                          based on FortiGate health signals.
        """
        # Validate parameters
        if not url:
            raise ValueError("URL is required")
        if max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        if max_retries > 100:
            raise ValueError("max_retries must be <= 100")
        if connect_timeout <= 0:
            raise ValueError("connect_timeout must be > 0")
        if read_timeout <= 0:
            raise ValueError("read_timeout must be > 0")
        if circuit_breaker_threshold <= 0:
            raise ValueError("circuit_breaker_threshold must be > 0")
        if circuit_breaker_timeout <= 0:
            raise ValueError("circuit_breaker_timeout must be > 0")
        if max_connections <= 0:
            raise ValueError("max_connections must be > 0")
        if max_keepalive_connections < 0:
            raise ValueError("max_keepalive_connections must be >= 0")

        # Auto-adjust keepalive connections if needed (don't error)
        # httpx and other libraries allow these to be independent, but we'll adjust
        # to be safe while not blocking legitimate configurations
        if max_keepalive_connections > max_connections:
            logger.warning(
                f"max_keepalive_connections ({max_keepalive_connections}) > "
                f"max_connections ({max_connections}). "
                f"Adjusting max_keepalive_connections to {max_connections}."
            )
            max_keepalive_connections = max_connections

        # Store configuration
        self._url = url.rstrip("/")
        self._verify = verify
        self._vdom = vdom
        self._max_retries = max_retries
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout

        # Initialize retry statistics
        self._retry_stats = {
            "total_retries": 0,
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "retry_by_reason": {},
            "retry_by_endpoint": {},
            "last_retry_time": None,
        }

        # Initialize circuit breaker state
        self._circuit_breaker = {
            "consecutive_failures": 0,
            "last_failure_time": None,
            "state": "closed",  # closed, open, half_open
            "failure_threshold": circuit_breaker_threshold,
            "timeout": circuit_breaker_timeout,
        }

        # Initialize per-endpoint timeout configuration
        self._endpoint_timeouts: dict[str, httpx.Timeout] = {}

        # Adaptive retry configuration
        self._adaptive_retry = adaptive_retry
        self._response_times: dict[str, deque] = {}  # endpoint -> deque of response times
        self._baseline_response_time = 0.5  # 500ms baseline
        self._slowdown_multiplier = 3.0  # Endpoint is slow if 3x baseline

    # ========================================================================
    # Shared Utility Methods
    # ========================================================================

    @staticmethod
    def _sanitize_data(data: Optional[dict[str, Any]]) -> dict[str, Any]:
        """
        Remove sensitive fields from data before logging (recursive)

        Recursively sanitizes nested dictionaries and lists to prevent
        logging sensitive information like passwords, tokens, keys, VDOMs, etc.

        Args:
            data: Data to sanitize (can be dict, list, or any value)

        Returns:
            Sanitized copy of data with sensitive values redacted

        Examples:
            >>> _sanitize_data({'password': 'secret123', 'name': 'test'})
            {'password': '***REDACTED***', 'name': 'test'}
            >>> _sanitize_data({'users': [{'name': 'admin', 'key': 'abc'}]})
            {'users': [{'name': 'admin', 'key': '***REDACTED***'}]}
        """
        if not data:
            return {}

        sensitive_keys = [
            "password",
            "passwd",
            "secret",
            "token",
            "key",
            "private-key",
            "passphrase",
            "psk",
            "api_key",
            "api-key",
            "apikey",
            "auth",
            "authorization",
            "vdom",  # Virtual domain names can reveal customer/tenant info
        ]

        def sanitize_recursive(obj: Any) -> Any:
            """Recursively sanitize nested structures"""
            if isinstance(obj, dict):
                result = {}
                for k, v in obj.items():
                    if any(s in k.lower() for s in sensitive_keys):
                        result[k] = "***REDACTED***"
                    else:
                        result[k] = sanitize_recursive(v)
                return result
            elif isinstance(obj, list):
                return [sanitize_recursive(item) for item in obj]
            else:
                return obj

        return sanitize_recursive(data)

    @staticmethod
    def _normalize_path(path: str) -> str:
        """Normalize API path by removing leading slashes"""
        if isinstance(path, str):
            return path.lstrip("/")
        return path

    def _build_url(self, api_type: str, path: str) -> str:
        """Build complete API URL from components"""
        path = self._normalize_path(path)
        encoded_path = quote(str(path), safe="/%")
        return f"{self._url}/api/v2/{api_type}/{encoded_path}"

    # ========================================================================
    # Statistics Methods
    # ========================================================================

    def get_retry_stats(self) -> dict[str, Any]:
        """Get retry statistics"""
        return self._retry_stats.copy()

    def get_circuit_breaker_state(self) -> dict[str, Any]:
        """Get current circuit breaker state"""
        return self._circuit_breaker.copy()

    def _record_retry(self, reason: str, endpoint: str) -> None:
        """Record retry attempt in statistics"""
        self._retry_stats["total_retries"] += 1
        self._retry_stats["last_retry_time"] = time.time()

        # Track by reason
        if reason not in self._retry_stats["retry_by_reason"]:
            self._retry_stats["retry_by_reason"][reason] = 0
        self._retry_stats["retry_by_reason"][reason] += 1

        # Track by endpoint
        if endpoint not in self._retry_stats["retry_by_endpoint"]:
            self._retry_stats["retry_by_endpoint"][endpoint] = 0
        self._retry_stats["retry_by_endpoint"][endpoint] += 1

    # ========================================================================
    # Endpoint Timeout Configuration
    # ========================================================================

    def configure_endpoint_timeout(
        self,
        endpoint_pattern: str,
        connect_timeout: Optional[float] = None,
        read_timeout: Optional[float] = None,
    ) -> None:
        """Configure custom timeout for specific endpoints"""
        timeout = httpx.Timeout(
            connect=connect_timeout or self._connect_timeout,
            read=read_timeout or self._read_timeout,
            write=30.0,
            pool=10.0,
        )
        self._endpoint_timeouts[endpoint_pattern] = timeout
        logger.info(
            "Configured custom timeout for endpoint pattern '%s': connect=%.1fs, read=%.1fs",
            endpoint_pattern,
            timeout.connect,
            timeout.read,
        )

    def _get_endpoint_timeout(self, endpoint: str) -> Optional[httpx.Timeout]:
        """Get custom timeout for specific endpoint if configured"""
        for pattern, timeout in self._endpoint_timeouts.items():
            if fnmatch.fnmatch(endpoint, pattern):
                return timeout
        return None

    # ========================================================================
    # Circuit Breaker Methods
    # ========================================================================

    def _check_circuit_breaker(self, endpoint: str) -> None:
        """Check circuit breaker state before making request"""
        if self._circuit_breaker["state"] == "open":
            elapsed = time.time() - (self._circuit_breaker["last_failure_time"] or 0)
            if elapsed < self._circuit_breaker["timeout"]:
                remaining = self._circuit_breaker["timeout"] - elapsed
                logger.error(
                    "Circuit breaker is OPEN - service unavailable (retry in %.1fs)",
                    remaining,
                )
                from .exceptions import CircuitBreakerOpenError

                raise CircuitBreakerOpenError(
                    f"Circuit breaker is OPEN for {endpoint}. "
                    f"Service appears to be down. Retry in {remaining:.1f}s"
                )
            else:
                self._circuit_breaker["state"] = "half_open"
                logger.info("Circuit breaker transitioning to HALF_OPEN state")

    def _record_circuit_breaker_success(self) -> None:
        """Record successful request in circuit breaker"""
        if self._circuit_breaker["state"] == "half_open":
            self._circuit_breaker["state"] = "closed"
            self._circuit_breaker["consecutive_failures"] = 0
            logger.info("Circuit breaker CLOSED after successful request")
        elif self._circuit_breaker["state"] == "closed":
            self._circuit_breaker["consecutive_failures"] = 0

    def _record_circuit_breaker_failure(self, endpoint: str) -> None:
        """Record failed request in circuit breaker"""
        self._circuit_breaker["consecutive_failures"] += 1
        self._circuit_breaker["last_failure_time"] = time.time()

        failures = self._circuit_breaker["consecutive_failures"]
        threshold = self._circuit_breaker["failure_threshold"]

        if failures >= threshold and self._circuit_breaker["state"] != "open":
            self._circuit_breaker["state"] = "open"
            logger.error(
                "Circuit breaker OPENED after %d consecutive failures for endpoint %s",
                failures,
                endpoint,
            )

    def reset_circuit_breaker(self) -> None:
        """Reset circuit breaker to closed state"""
        self._circuit_breaker["state"] = "closed"
        self._circuit_breaker["consecutive_failures"] = 0
        self._circuit_breaker["last_failure_time"] = None
        logger.info("Circuit breaker manually reset to CLOSED state")

    # ========================================================================
    # Retry Logic
    # ========================================================================

    def _should_retry(self, error: Exception, attempt: int, endpoint: str = "") -> bool:
        """Determine if a request should be retried"""
        if attempt >= self._max_retries:
            return False

        # Retry on connection errors and timeouts
        if isinstance(error, (httpx.ConnectError, httpx.NetworkError)):
            self._record_retry("connection_error", endpoint)
            logger.warning(
                "Connection error on attempt %d/%d for %s: %s",
                attempt + 1,
                self._max_retries,
                endpoint,
                error,
            )
            return True

        if isinstance(error, (httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout)):
            self._record_retry("timeout", endpoint)
            logger.warning(
                "Timeout on attempt %d/%d for %s: %s",
                attempt + 1,
                self._max_retries,
                endpoint,
                error,
            )
            return True

        # Retry on HTTP status errors (429, 500-504)
        if isinstance(error, httpx.HTTPStatusError):
            status = error.response.status_code
            if status == 429:  # Rate limit
                self._record_retry("rate_limit", endpoint)
                logger.warning(
                    "Rate limit hit on attempt %d/%d for %s",
                    attempt + 1,
                    self._max_retries,
                    endpoint,
                )
                return True
            elif 500 <= status <= 504:  # Server errors
                self._record_retry("server_error", endpoint)
                logger.warning(
                    "Server error %d on attempt %d/%d for %s",
                    status,
                    attempt + 1,
                    self._max_retries,
                    endpoint,
                )
                return True

        return False

    def _get_retry_delay(
        self,
        attempt: int,
        response: Optional[httpx.Response] = None,
        endpoint: Optional[str] = None,
    ) -> float:
        """
        Calculate retry delay with optional adaptive backpressure

        Args:
            attempt: Current retry attempt number (0-indexed)
            response: HTTP response object (if available)
            endpoint: Endpoint being retried (for adaptive logic)

        Returns:
            Delay in seconds before next retry
        """
        # Check for Retry-After header (FortiGate explicitly telling us when to retry)
        if response and "Retry-After" in response.headers:
            try:
                return float(response.headers["Retry-After"])
            except ValueError:
                pass

        # Start with exponential backoff: 1s, 2s, 4s, 8s, max 30s
        delay = min(2**attempt, 30)

        # Apply adaptive backpressure if enabled
        if self._adaptive_retry and endpoint:
            delay = self._apply_adaptive_backpressure(delay, response, endpoint)

        return delay

    def _apply_adaptive_backpressure(
        self,
        base_delay: float,
        response: Optional[httpx.Response],
        endpoint: str,
    ) -> float:
        """
        Apply adaptive backpressure based on FortiGate health signals

        Args:
            base_delay: Base exponential backoff delay
            response: HTTP response (if available)
            endpoint: Endpoint being retried

        Returns:
            Adjusted delay with backpressure multiplier applied
        """
        multiplier = 1.0

        # Signal 1: Explicit 503 Service Unavailable (FortiGate overloaded)
        if response and response.status_code == 503:
            multiplier = 3.0
            logger.warning(
                "FortiGate returned 503 (overloaded), applying 3x backpressure multiplier"
            )

        # Signal 2: Endpoint showing slow response times (early warning)
        elif self._is_endpoint_slow(endpoint):
            multiplier = 2.0
            avg_time = self._get_avg_response_time(endpoint)
            logger.warning(
                "Endpoint %s showing backpressure (avg response: %.2fs, baseline: %.2fs), applying 2x multiplier",
                endpoint,
                avg_time,
                self._baseline_response_time,
            )

        adjusted_delay = base_delay * multiplier

        # Cap maximum delay at 2 minutes
        return min(adjusted_delay, 120.0)

    def _record_response_time(self, endpoint: str, duration: float) -> None:
        """
        Record response time for adaptive backpressure detection

        Args:
            endpoint: API endpoint (e.g., 'cmdb/firewall/address')
            duration: Response time in seconds
        """
        if not self._adaptive_retry:
            return  # Zero overhead when disabled

        if endpoint not in self._response_times:
            # Keep last 100 response times per endpoint
            self._response_times[endpoint] = deque(maxlen=100)

        self._response_times[endpoint].append(duration)

    def _get_avg_response_time(self, endpoint: str) -> float:
        """
        Get average response time for endpoint

        Args:
            endpoint: API endpoint

        Returns:
            Average response time in seconds, or 0.0 if no data
        """
        times = self._response_times.get(endpoint, [])
        if not times:
            return 0.0
        return sum(times) / len(times)

    def _is_endpoint_slow(self, endpoint: str) -> bool:
        """
        Detect if endpoint is responding slowly (backpressure signal)

        Args:
            endpoint: API endpoint to check

        Returns:
            True if endpoint average response time exceeds baseline threshold
        """
        avg_time = self._get_avg_response_time(endpoint)

        # No data yet, assume healthy
        if avg_time == 0.0:
            return False

        # Slow if average > baseline * multiplier
        threshold = self._baseline_response_time * self._slowdown_multiplier
        return avg_time > threshold

    def get_health_metrics(self) -> dict[str, Any]:
        """
        Get comprehensive health metrics including adaptive retry stats

        Returns:
            Dictionary with health score, response times, circuit state, etc.
        """
        metrics = {
            "circuit_breaker": {
                "state": self._circuit_breaker["state"],
                "consecutive_failures": self._circuit_breaker["consecutive_failures"],
                "threshold": self._circuit_breaker["failure_threshold"],
            },
            "retry_stats": self._retry_stats.copy(),
            "adaptive_retry_enabled": self._adaptive_retry,
        }

        # Add response time metrics if adaptive retry is enabled
        if self._adaptive_retry and self._response_times:
            metrics["response_times"] = {}
            for endpoint, times in self._response_times.items():
                if times:
                    sorted_times = sorted(times)
                    count = len(sorted_times)
                    metrics["response_times"][endpoint] = {
                        "count": count,
                        "avg_ms": round(sum(sorted_times) / count * 1000, 2),
                        "min_ms": round(min(sorted_times) * 1000, 2),
                        "max_ms": round(max(sorted_times) * 1000, 2),
                        "p50_ms": round(sorted_times[count // 2] * 1000, 2),
                        "p95_ms": (
                            round(sorted_times[int(count * 0.95)] * 1000, 2) if count > 20 else None
                        ),
                        "is_slow": self._is_endpoint_slow(endpoint),
                    }

        return metrics

    # ========================================================================
    # Validation Helper Methods
    # ========================================================================

    @staticmethod
    def _validate_api_type(api_type: str) -> None:
        """Validate API type parameter"""
        valid_types = {"cmdb", "monitor", "log", "service"}
        if api_type not in valid_types:
            raise ValueError(
                f"Invalid api_type '{api_type}'. Must be one of: {', '.join(sorted(valid_types))}"
            )

    @staticmethod
    def _validate_path(path: str) -> None:
        """Validate path parameter"""
        if not path or not isinstance(path, str):
            raise ValueError("path must be a non-empty string")

    @staticmethod
    def _validate_data(data: Any) -> None:
        """Validate data parameter for POST/PUT"""
        if not isinstance(data, dict):
            raise TypeError(f"data must be a dictionary, got {type(data).__name__}")

    @staticmethod
    def _validate_vdom(vdom: Optional[Union[str, bool]]) -> None:
        """Validate vdom parameter"""
        if vdom is not None and not isinstance(vdom, (str, bool)):
            raise TypeError(f"vdom must be str, bool, or None, got {type(vdom).__name__}")

    @staticmethod
    def _validate_params(params: Optional[dict[str, Any]]) -> None:
        """Validate params parameter"""
        if params is not None and not isinstance(params, dict):
            raise TypeError(f"params must be a dictionary or None, got {type(params).__name__}")

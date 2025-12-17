"""
Internal HTTP Client for FortiOS API

This module contains the HTTPClient class which handles all HTTP communication
with FortiGate devices. It is an internal implementation detail and not part
of the public API.

Now powered by httpx for better performance, HTTP/2 support, and modern async capabilities.
"""

from __future__ import annotations

import fnmatch
import logging
import time
import uuid
from typing import Any, Optional, TypeAlias, Union
from urllib.parse import quote

import httpx

logger = logging.getLogger("hfortix.http")

# Type alias for API responses
HTTPResponse: TypeAlias = dict[str, Any]

__all__ = ["HTTPClient", "HTTPResponse", "encode_path_component"]


def encode_path_component(component: str) -> str:
    """
    Encode a single path component for use in URLs.

    This encodes special characters including forward slashes, which are
    commonly used in FortiOS object names (e.g., IP addresses with CIDR notation).

    Args:
        component: Path component to encode (e.g., object name)

    Returns:
        URL-encoded string safe for use in URL paths

    Examples:
        >>> encode_path_component("Test_NET_192.0.2.0/24")
        'Test_NET_192.0.2.0%2F24'
        >>> encode_path_component("test@example.com")
        'test%40example.com'
    """
    return quote(component, safe="")


class HTTPClient:
    """
    Internal HTTP client for FortiOS API requests

    Handles all HTTP communication with FortiGate devices including:
    - Session management
    - Authentication headers
    - SSL verification
    - Request/response handling
    - Error handling
    - Automatic retry with exponential backoff
    - Context manager support (use with 'with' statement)

    Query Parameter Encoding:
        The requests library automatically handles query parameter encoding:
        - Lists: Encoded as repeated parameters (e.g., ['a', 'b'] → ?key=a&key=b)
        - Booleans: Converted to lowercase strings ('true'/'false')
        - None values: Should be filtered out before passing to params
        - Special characters: URL-encoded automatically
        
    Path Encoding:
        Paths are URL-encoded with / and % as safe characters to prevent
        double-encoding of already-encoded components.

    This class is internal and not exposed to users.
    """

    def __init__(
        self,
        url: str,
        verify: bool = True,
        token: Optional[str] = None,
        vdom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
    ) -> None:
        """
        Initialize HTTP client

        Args:
            url: Base URL for API (e.g., "https://192.0.2.10")
            verify: Verify SSL certificates
            token: API authentication token
            vdom: Default virtual domain
            max_retries: Maximum number of retry attempts on transient failures (default: 3)
            connect_timeout: Timeout for establishing connection in seconds (default: 10.0)
            read_timeout: Timeout for reading response in seconds (default: 300.0)
            user_agent: Custom User-Agent header for identifying application in FortiGate logs.
                       If None, defaults to 'hfortix/{version}'. Useful for multi-team environments
                       and troubleshooting in production.
            circuit_breaker_threshold: Number of consecutive failures before opening circuit (default: 5)
            circuit_breaker_timeout: Seconds to wait before transitioning to half-open (default: 60.0)
            max_connections: Maximum number of connections in the pool (default: 100)
            max_keepalive_connections: Maximum number of keepalive connections (default: 20)
        
        Raises:
            ValueError: If parameters are invalid
        """
        # Validate parameters
        if not url:
            raise ValueError("URL is required and cannot be empty")
        if max_retries < 0:
            raise ValueError(f"max_retries must be >= 0, got {max_retries}")
        if max_retries > 100:
            logger.warning("max_retries=%d is very high, consider reducing", max_retries)
        if connect_timeout <= 0:
            raise ValueError(f"connect_timeout must be > 0, got {connect_timeout}")
        if read_timeout <= 0:
            raise ValueError(f"read_timeout must be > 0, got {read_timeout}")
        if circuit_breaker_threshold <= 0:
            raise ValueError(f"circuit_breaker_threshold must be > 0, got {circuit_breaker_threshold}")
        if circuit_breaker_timeout <= 0:
            raise ValueError(f"circuit_breaker_timeout must be > 0, got {circuit_breaker_timeout}")
        if max_connections <= 0:
            raise ValueError(f"max_connections must be > 0, got {max_connections}")
        if max_keepalive_connections < 0:
            raise ValueError(f"max_keepalive_connections must be >= 0, got {max_keepalive_connections}")
        if max_keepalive_connections > max_connections:
            raise ValueError(
                f"max_keepalive_connections ({max_keepalive_connections}) cannot exceed "
                f"max_connections ({max_connections})"
            )
        
        # Normalize URL: remove trailing slashes to prevent double-slash issues
        self._url = url.rstrip('/')
        self._verify = verify
        self._vdom = vdom
        self._max_retries = max_retries
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout
        
        # Set default User-Agent if not provided
        if user_agent is None:
            # Import here to avoid circular dependency
            from . import __version__
            user_agent = f'hfortix/{__version__}'
        
        # Initialize httpx client with proper timeout configuration
        self._client = httpx.Client(
            headers={'User-Agent': user_agent},
            timeout=httpx.Timeout(
                connect=connect_timeout,
                read=read_timeout,
                write=30.0,  # Default write timeout
                pool=10.0    # Default pool timeout
            ),
            verify=verify,
            http2=True,  # Enable HTTP/2 support
            limits=httpx.Limits(
                max_connections=max_connections,
                max_keepalive_connections=max_keepalive_connections
            )
        )

        # Initialize retry statistics
        self._retry_stats = {
            'total_retries': 0,
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'retry_by_reason': {},
            'retry_by_endpoint': {},
            'last_retry_time': None,
        }

        # Initialize circuit breaker state
        self._circuit_breaker = {
            'consecutive_failures': 0,
            'last_failure_time': None,
            'state': 'closed',  # closed, open, half_open
            'failure_threshold': circuit_breaker_threshold,
            'timeout': circuit_breaker_timeout,
        }

        # Initialize per-endpoint timeout configuration
        self._endpoint_timeouts: dict[str, httpx.Timeout] = {}

        # Set token if provided
        if token:
            self._client.headers["Authorization"] = f"Bearer {token}"

        logger.debug(
            "HTTP client initialized for %s (max_retries=%d, connect_timeout=%.1fs, read_timeout=%.1fs, "
            "http2=enabled, user_agent='%s', circuit_breaker_threshold=%d, max_connections=%d)",
            self._url,
            max_retries,
            connect_timeout,
            read_timeout,
            user_agent,
            circuit_breaker_threshold,
            max_connections,
        )

    @staticmethod
    def _sanitize_data(data: Optional[dict[str, Any]]) -> dict[str, Any]:
        """
        Remove sensitive fields from data before logging (recursive)
        
        Recursively sanitizes nested dictionaries and lists to prevent
        logging sensitive information like passwords, tokens, keys, etc.
        
        Args:
            data: Data to sanitize (can be dict, list, or any value)
            
        Returns:
            Sanitized copy of data with sensitive values redacted
            
        Examples:
            >>> client._sanitize_data({'password': 'secret123', 'name': 'test'})
            {'password': '***REDACTED***', 'name': 'test'}
            >>> client._sanitize_data({'users': [{'name': 'admin', 'key': 'abc'}]})
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
        """
        Normalize API path by removing leading slashes
        
        Args:
            path: Path to normalize
            
        Returns:
            Normalized path without leading slashes
            
        Examples:
            >>> HTTPClient._normalize_path('/firewall/address')
            'firewall/address'
            >>> HTTPClient._normalize_path('firewall/address')
            'firewall/address'
        """
        return path.lstrip('/') if isinstance(path, str) else path

    def _build_url(self, api_type: str, path: str) -> str:
        """
        Build complete API URL from components
        
        Centralizes URL construction logic with proper encoding.
        
        Args:
            api_type: API type (cmdb, monitor, log, service)
            path: Endpoint path
            
        Returns:
            Complete URL string
        """
        # Normalize path: remove leading slash
        path = self._normalize_path(path)
        
        # URL encode the path, treating / and % as safe characters
        encoded_path = quote(str(path), safe='/%') if isinstance(path, str) else path
        
        return f"{self._url}/api/v2/{api_type}/{encoded_path}"

    def get_retry_stats(self) -> dict[str, Any]:
        """
        Get retry statistics
        
        Returns:
            dict: Retry statistics including:
                - total_retries: Total number of retries across all requests
                - total_requests: Total number of requests made
                - successful_requests: Number of successful requests
                - failed_requests: Number of failed requests
                - retry_by_reason: Count of retries grouped by reason
                - retry_by_endpoint: Count of retries grouped by endpoint
                - last_retry_time: Timestamp of last retry (None if no retries)
                - success_rate: Percentage of successful requests (0-100)
        
        Example:
            >>> stats = client.get_retry_stats()
            >>> print(f"Total retries: {stats['total_retries']}")
            >>> print(f"Success rate: {stats['success_rate']:.1f}%")
            >>> print(f"Timeout retries: {stats['retry_by_reason'].get('Timeout', 0)}")
        """
        total = self._retry_stats['total_requests']
        successful = self._retry_stats['successful_requests']
        success_rate = (successful / total * 100) if total > 0 else 0.0
        
        return {
            'total_retries': self._retry_stats['total_retries'],
            'total_requests': total,
            'successful_requests': successful,
            'failed_requests': self._retry_stats['failed_requests'],
            'retry_by_reason': self._retry_stats['retry_by_reason'].copy(),
            'retry_by_endpoint': self._retry_stats['retry_by_endpoint'].copy(),
            'last_retry_time': self._retry_stats['last_retry_time'],
            'success_rate': success_rate,
        }

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get HTTP connection pool statistics
        
        Returns:
            dict: Connection statistics including:
                - http2_enabled: Whether HTTP/2 is enabled
                - max_connections: Maximum number of connections allowed
                - max_keepalive_connections: Maximum keepalive connections
                - circuit_breaker_state: Current circuit breaker state
                - consecutive_failures: Number of consecutive failures
        
        Example:
            >>> stats = client.get_connection_stats()
            >>> print(f"Circuit breaker: {stats['circuit_breaker_state']}")
        """
        return {
            'http2_enabled': True,
            'max_connections': 100,
            'max_keepalive_connections': 20,
            'circuit_breaker_state': self._circuit_breaker['state'],
            'consecutive_failures': self._circuit_breaker['consecutive_failures'],
            'last_failure_time': self._circuit_breaker['last_failure_time'],
        }

    def get_circuit_breaker_state(self) -> dict[str, Any]:
        """
        Get circuit breaker state and statistics
        
        Returns:
            dict: Circuit breaker information including:
                - state: Current state (closed/open/half_open)
                - consecutive_failures: Number of consecutive failures
                - failure_threshold: Threshold to open circuit
                - last_failure_time: Timestamp of last failure
                - timeout: Wait time before half-open (seconds)
        
        Example:
            >>> state = client.get_circuit_breaker_state()
            >>> if state['state'] == 'open':
            >>>     print("Circuit breaker is OPEN - service unavailable")
        """
        return self._circuit_breaker.copy()

    def reset_circuit_breaker(self) -> None:
        """
        Manually reset circuit breaker to closed state
        
        Useful for testing or when you know the service has recovered.
        
        Example:
            >>> client.reset_circuit_breaker()
            >>> # Circuit is now closed and will accept requests
        """
        self._circuit_breaker['consecutive_failures'] = 0
        self._circuit_breaker['last_failure_time'] = None
        self._circuit_breaker['state'] = 'closed'
        logger.info("Circuit breaker manually reset to closed state")

    def configure_endpoint_timeout(
        self,
        endpoint_pattern: str,
        connect: Optional[float] = None,
        read: Optional[float] = None,
        write: Optional[float] = None,
        pool: Optional[float] = None,
    ) -> None:
        """
        Configure custom timeout for specific endpoint patterns
        
        Args:
            endpoint_pattern: Endpoint pattern (e.g., 'monitor/system/status', 'cmdb/firewall/*')
            connect: Connection timeout in seconds
            read: Read timeout in seconds
            write: Write timeout in seconds
            pool: Pool timeout in seconds
        
        Example:
            >>> # Fast endpoint - short timeout
            >>> client.configure_endpoint_timeout('monitor/system/status', read=5.0)
            >>> 
            >>> # Slow endpoint - longer timeout
            >>> client.configure_endpoint_timeout('cmdb/firewall/policy', read=600.0)
            >>> 
            >>> # Wildcard pattern
            >>> client.configure_endpoint_timeout('monitor/*', read=10.0)
        """
        timeout = httpx.Timeout(
            connect=connect if connect is not None else self._connect_timeout,
            read=read if read is not None else self._read_timeout,
            write=write if write is not None else 30.0,
            pool=pool if pool is not None else 10.0,
        )
        self._endpoint_timeouts[endpoint_pattern] = timeout
        logger.debug("Configured timeout for endpoint pattern '%s': %s", endpoint_pattern, timeout)

    def _get_endpoint_timeout(self, endpoint: str) -> Optional[httpx.Timeout]:
        """
        Get configured timeout for endpoint (checks patterns)
        
        Supports shell-style wildcard patterns:
        - `monitor/*` - matches all monitor endpoints
        - `*/status` - matches any endpoint ending in /status
        - `monitor/*/interface` - matches monitor/{anything}/interface
        
        Args:
            endpoint: Full endpoint path (e.g., 'monitor/system/status')
        
        Returns:
            Configured timeout or None to use default
            
        Examples:
            >>> client.configure_endpoint_timeout('monitor/*', read=10.0)
            >>> client._get_endpoint_timeout('monitor/system/status')  # Matches
            >>> client._get_endpoint_timeout('cmdb/firewall/policy')   # No match
        """
        # Check exact match first (highest priority)
        if endpoint in self._endpoint_timeouts:
            return self._endpoint_timeouts[endpoint]
        
        # Check wildcard patterns using fnmatch
        for pattern, timeout in self._endpoint_timeouts.items():
            if '*' in pattern or '?' in pattern or '[' in pattern:
                if fnmatch.fnmatch(endpoint, pattern):
                    return timeout
        
        return None


    def _record_retry(self, reason: str, endpoint: str) -> None:
        """
        Record retry statistics
        
        Args:
            reason: Reason for retry (e.g., 'ConnectionError', 'Timeout', 'HTTP 429')
            endpoint: Endpoint being retried
        """
        self._retry_stats['total_retries'] += 1
        self._retry_stats['last_retry_time'] = time.time()
        
        # Track by reason
        if reason not in self._retry_stats['retry_by_reason']:
            self._retry_stats['retry_by_reason'][reason] = 0
        self._retry_stats['retry_by_reason'][reason] += 1
        
        # Track by endpoint
        if endpoint not in self._retry_stats['retry_by_endpoint']:
            self._retry_stats['retry_by_endpoint'][endpoint] = 0
        self._retry_stats['retry_by_endpoint'][endpoint] += 1

    def _check_circuit_breaker(self, endpoint: str) -> None:
        """
        Check circuit breaker state before making request
        
        Args:
            endpoint: Endpoint being accessed
        
        Raises:
            CircuitBreakerOpenError: If circuit breaker is open
        """
        state = self._circuit_breaker['state']
        
        if state == 'open':
            # Check if timeout has elapsed to transition to half-open
            if self._circuit_breaker['last_failure_time']:
                elapsed = time.time() - self._circuit_breaker['last_failure_time']
                if elapsed >= self._circuit_breaker['timeout']:
                    self._circuit_breaker['state'] = 'half_open'
                    logger.info("Circuit breaker transitioning to half-open state")
                else:
                    remaining = self._circuit_breaker['timeout'] - elapsed
                    logger.error(
                        "Circuit breaker is OPEN - service unavailable (retry in %.1fs)",
                        remaining
                    )
                    from .exceptions import CircuitBreakerOpenError
                    raise CircuitBreakerOpenError(
                        f"Circuit breaker is OPEN for {endpoint}. "
                        f"Service appears to be down. Retry in {remaining:.1f}s"
                    )

    def _record_circuit_breaker_success(self) -> None:
        """Record successful request - reset circuit breaker"""
        if self._circuit_breaker['consecutive_failures'] > 0:
            logger.info(
                "Circuit breaker: Service recovered after %d failures",
                self._circuit_breaker['consecutive_failures']
            )
        self._circuit_breaker['consecutive_failures'] = 0
        self._circuit_breaker['last_failure_time'] = None
        self._circuit_breaker['state'] = 'closed'

    def _record_circuit_breaker_failure(self, endpoint: str) -> None:
        """
        Record failed request - update circuit breaker state
        
        Args:
            endpoint: Endpoint that failed
        """
        self._circuit_breaker['consecutive_failures'] += 1
        self._circuit_breaker['last_failure_time'] = time.time()
        
        failures = self._circuit_breaker['consecutive_failures']
        threshold = self._circuit_breaker['failure_threshold']
        
        if failures >= threshold and self._circuit_breaker['state'] != 'open':
            self._circuit_breaker['state'] = 'open'
            logger.error(
                "Circuit breaker OPENED after %d consecutive failures for %s",
                failures,
                endpoint
            )
        elif failures < threshold:
            logger.warning(
                "Circuit breaker: %d/%d consecutive failures for %s",
                failures,
                threshold,
                endpoint
            )


    def _handle_response_errors(self, response: httpx.Response) -> None:
        """
        Handle HTTP response errors consistently using FortiOS error handling

        Args:
            response: httpx.Response object

        Raises:
            DuplicateEntryError: If entry already exists (-5, -15, -100)
            EntryInUseError: If entry is in use (-23, -94, -95, -96)
            PermissionDeniedError: If permission denied (-14, -37)
            InvalidValueError: If invalid value provided (-1, -50, -651)
            ResourceNotFoundError: If resource not found (-3, HTTP 404)
            BadRequestError: If bad request (HTTP 400)
            AuthenticationError: If authentication failed (HTTP 401)
            AuthorizationError: If authorization failed (HTTP 403)
            MethodNotAllowedError: If method not allowed (HTTP 405)
            RateLimitError: If rate limit exceeded (HTTP 429)
            ServerError: If server error (HTTP 500)
            APIError: For other API errors
        """
        if not response.is_success:
            try:
                from .exceptions_forti import (get_error_description,
                                               raise_for_status)

                # Try to parse JSON response (most FortiOS errors are JSON)
                json_response = response.json()

                # Add error description if error code present
                error_code = json_response.get("error")
                if error_code and "error_description" not in json_response:
                    json_response["error_description"] = get_error_description(error_code)

                # Log the error with details
                status = json_response.get("status")
                http_status = json_response.get("http_status", response.status_code)
                error_desc = json_response.get("error_description", "Unknown error")

                logger.error(
                    "Request failed: HTTP %d, status=%s, error=%s, description='%s'",
                    http_status,
                    status,
                    error_code,
                    error_desc,
                )

                # Use FortiOS-specific error handling
                raise_for_status(json_response)

            except ValueError:
                # Response is not JSON (could be binary or HTML error page)
                # This can happen with binary endpoints or proxy/firewall errors
                logger.error(
                    "Request failed: HTTP %d (non-JSON response, %d bytes)",
                    response.status_code,
                    len(response.content),
                )
                response.raise_for_status()

    def _should_retry(self, error: Exception, attempt: int, endpoint: str = "") -> bool:
        """
        Determine if a request should be retried based on error type and attempt number

        Args:
            error: The exception that occurred
            attempt: Current attempt number (0-indexed)
            endpoint: Endpoint being accessed (for statistics)

        Returns:
            True if request should be retried, False otherwise
        """
        if attempt >= self._max_retries:
            return False

        # Retry on connection errors and timeouts
        if isinstance(error, (httpx.ConnectError, httpx.NetworkError)):
            reason = type(error).__name__
            logger.warning(
                "Retryable connection error on attempt %d/%d: %s",
                attempt + 1,
                self._max_retries + 1,
                str(error),
            )
            self._record_retry(reason, endpoint)
            return True
        
        if isinstance(error, (httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout)):
            # Differentiate timeout types
            if isinstance(error, httpx.ConnectTimeout):
                reason = f"Timeout (connect, {self._connect_timeout}s)"
                logger.warning(
                    "Connection timeout after %ds on attempt %d/%d",
                    self._connect_timeout,
                    attempt + 1,
                    self._max_retries + 1,
                )
            elif isinstance(error, httpx.ReadTimeout):
                reason = f"Timeout (read, {self._read_timeout}s)"
                logger.warning(
                    "Read timeout after %ds on attempt %d/%d",
                    self._read_timeout,
                    attempt + 1,
                    self._max_retries + 1,
                )
            elif isinstance(error, httpx.WriteTimeout):
                reason = "Timeout (write)"
                logger.warning(
                    "Write timeout on attempt %d/%d",
                    attempt + 1,
                    self._max_retries + 1,
                )
            else:
                reason = f"Timeout ({type(error).__name__})"
                logger.warning(
                    "Timeout on attempt %d/%d: %s",
                    attempt + 1,
                    self._max_retries + 1,
                    type(error).__name__,
                )
            self._record_retry(reason, endpoint)
            return True

        # Retry on rate limit errors (429) and server errors (500, 502, 503, 504)
        if isinstance(error, httpx.HTTPStatusError):
            http_error: httpx.HTTPStatusError = error
            response = http_error.response
            if response is not None:
                status_code = response.status_code
                if status_code in (429, 500, 502, 503, 504):
                    reason = f"HTTP {status_code}"
                    logger.warning(
                        "Retryable HTTP %d on attempt %d/%d",
                        status_code,
                        attempt + 1,
                        self._max_retries + 1,
                    )
                    self._record_retry(reason, endpoint)
                    return True

        return False

    def _get_retry_delay(self, attempt: int, response: Optional[httpx.Response] = None) -> float:
        """
        Calculate retry delay with exponential backoff

        Args:
            attempt: Current attempt number (0-indexed)
            response: Optional response object (to check Retry-After header)

        Returns:
            Delay in seconds before next retry
        """
        # Check for Retry-After header (for 429 rate limits)
        if response is not None:
            # Log rate limit status if available
            rate_limit_remaining = response.headers.get('X-RateLimit-Remaining')
            if rate_limit_remaining:
                logger.debug("Rate limit remaining: %s", rate_limit_remaining)
            
            if "Retry-After" in response.headers:
                try:
                    retry_after = int(response.headers["Retry-After"])
                    logger.debug("Using Retry-After header: %d seconds", retry_after)
                    return float(retry_after)
                except (ValueError, TypeError):
                    pass

        # Exponential backoff: 1s, 2s, 4s, 8s, ...
        # Cap at 30 seconds to avoid excessive delays
        delay = min(2 ** attempt, 30.0)
        logger.debug("Exponential backoff delay: %.1f seconds", delay)
        return delay

    def request(
        self,
        method: str,
        api_type: str,
        path: str,
        data: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        request_id: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        Generic request method for all API calls

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            api_type: API type (cmdb, monitor, log, service)
            path: API endpoint path (e.g., 'firewall/address', 'system/status')
            data: Request body data (for POST/PUT)
            params: Query parameters dict
            vdom: Virtual domain (None=use default, or specify vdom name)
            raw_json: If False (default), return only 'results' field. If True, return full response
            request_id: Optional correlation ID for tracking requests across logs

        Returns:
            dict: If raw_json=False, returns response['results'] (or full response if no 'results' key)
                  If raw_json=True, returns complete API response with status, http_status, etc.
        """
        # Generate request ID if not provided
        if request_id is None:
            request_id = str(uuid.uuid4())[:8]  # Short UUID for readability

        # Normalize path: remove any leading slash so callers may pass
        # either 'firewall/acl' or '/firewall/acl' without causing a double-slash
        # in the constructed URL. Keep internal separators intact.
        path = self._normalize_path(path)

        # URL encode the path, treating / as safe (path separator)
        # Individual path components may already be encoded by endpoint files using
        # encode_path_component(), so quote() with safe='/' won't double-encode
        # already-encoded %XX sequences (e.g., %2F stays as %2F)
        encoded_path = quote(str(path), safe='/%') if isinstance(path, str) else path
        url = f"{self._url}/api/v2/{api_type}/{encoded_path}"
        params = params or {}

        # Only add vdom parameter if explicitly specified
        if vdom is not None:
            params["vdom"] = vdom
        elif self._vdom is not None and "vdom" not in params:
            params["vdom"] = self._vdom

        # Build full API path for logging and circuit breaker
        full_path = f"/api/v2/{api_type}/{path}"
        endpoint_key = f"{api_type}/{path}"

        # Check circuit breaker before making request
        try:
            self._check_circuit_breaker(endpoint_key)
        except RuntimeError as e:
            # Structured log for circuit breaker open
            logger.error(
                "Circuit breaker blocked request",
                extra={
                    'request_id': request_id,
                    'method': method,
                    'endpoint': full_path,
                    'circuit_state': self._circuit_breaker['state'],
                    'consecutive_failures': self._circuit_breaker['consecutive_failures'],
                }
            )
            raise

        # Get endpoint-specific timeout if configured
        endpoint_timeout = self._get_endpoint_timeout(endpoint_key)
        if endpoint_timeout:
            # Temporarily set custom timeout for this request
            original_timeout = self._client.timeout
            self._client.timeout = endpoint_timeout

        # Structured log for request start
        logger.debug(
            "Request started",
            extra={
                'request_id': request_id,
                'method': method.upper(),
                'endpoint': full_path,
                'has_data': bool(data),
                'has_params': bool(params),
            }
        )
        if params:
            logger.debug(
                "Request parameters", 
                extra={'request_id': request_id, 'params': self._sanitize_data(params)}
            )
        if data:
            logger.debug(
                "Request data", 
                extra={'request_id': request_id, 'data': self._sanitize_data(data)}
            )

        # Track timing
        start_time = time.time()
        
        # Track total requests
        self._retry_stats['total_requests'] += 1

        # Retry loop with exponential backoff
        last_error = None
        for attempt in range(self._max_retries + 1):
            try:
                # Make request with httpx client
                res = self._client.request(
                    method=method,
                    url=url,
                    json=data if data else None,
                    params=params if params else None,
                )

                # Calculate duration
                duration = time.time() - start_time

                # Handle errors (will raise exception if error response)
                self._handle_response_errors(res)

                # Record success in circuit breaker
                self._record_circuit_breaker_success()
                
                # Record successful request
                self._retry_stats['successful_requests'] += 1

                # Structured log for successful response
                logger.info(
                    "Request completed successfully",
                    extra={
                        'request_id': request_id,
                        'method': method.upper(),
                        'endpoint': full_path,
                        'status_code': res.status_code,
                        'duration_seconds': round(duration, 3),
                        'attempts': attempt + 1,
                    }
                )

                # Warn about slow requests
                if duration > 2.0:
                    logger.warning(
                        "Slow request detected",
                        extra={
                            'request_id': request_id,
                            'method': method.upper(),
                            'endpoint': full_path,
                            'duration_seconds': round(duration, 3),
                        }
                    )

                # Parse JSON response
                json_response = res.json()

                # Restore original timeout if we changed it
                if endpoint_timeout:
                    self._client.timeout = original_timeout

                # Return full response if raw_json=True, otherwise extract results
                if raw_json:
                    return json_response
                else:
                    # Return 'results' field if present, otherwise full response
                    return json_response.get("results", json_response)

            except Exception as e:
                last_error = e
                
                # Record failure in circuit breaker
                self._record_circuit_breaker_failure(endpoint_key)

                # Check if we should retry
                if self._should_retry(e, attempt, endpoint_key):
                    # Calculate delay
                    response_obj = getattr(e, 'response', None) if isinstance(e, httpx.HTTPStatusError) else None
                    delay = self._get_retry_delay(attempt, response_obj)

                    # Structured log for retry
                    logger.info(
                        "Retrying request after delay",
                        extra={
                            'request_id': request_id,
                            'method': method.upper(),
                            'endpoint': full_path,
                            'error_type': type(e).__name__,
                            'attempt': attempt + 1,
                            'max_attempts': self._max_retries + 1,
                            'delay_seconds': delay,
                        }
                    )

                    # Wait before retry
                    time.sleep(delay)
                    continue
                else:
                    # Don't retry, restore timeout and raise the error
                    if endpoint_timeout:
                        self._client.timeout = original_timeout
                    raise

        # If we've exhausted all retries, restore timeout and raise the last error
        if endpoint_timeout:
            self._client.timeout = original_timeout
            
        if last_error:
            # Record failed request
            self._retry_stats['failed_requests'] += 1
            
            logger.error(
                "Request failed after all retries",
                extra={
                    'request_id': request_id,
                    'method': method.upper(),
                    'endpoint': full_path,
                    'total_attempts': self._max_retries + 1,
                    'error_type': type(last_error).__name__,
                }
            )
            raise last_error

        # This should never be reached, but satisfies type checker
        raise RuntimeError("Request loop completed without success or error")

    def get(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """GET request"""
        return self.request("GET", api_type, path, params=params, vdom=vdom, raw_json=raw_json)

    def get_binary(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
    ) -> bytes:
        """
        GET request returning binary data (for file downloads)

        Args:
            api_type: API type
            path: Endpoint path
            params: Query parameters
            vdom: Virtual domain

        Returns:
            Raw binary response data
        """
        path = path.lstrip('/') if isinstance(path, str) else path
        url = f"{self._url}/api/v2/{api_type}/{path}"
        params = params or {}

        # Add vdom if applicable
        if vdom is not None:
            params["vdom"] = vdom
        elif self._vdom is not None and "vdom" not in params:
            params["vdom"] = self._vdom

        # Make request
        res = self._client.get(url, params=params if params else None)

        # Handle errors
        self._handle_response_errors(res)

        return res.content

    def post(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """POST request - Create new object"""
        return self.request(
            "POST", api_type, path, data=data, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """PUT request - Update existing object"""
        return self.request(
            "PUT", api_type, path, data=data, params=params, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """DELETE request - Delete object"""
        return self.request("DELETE", api_type, path, params=params, vdom=vdom, raw_json=raw_json)

    # ========================================================================
    # Validation Helper Methods
    # ========================================================================

    @staticmethod
    def validate_mkey(mkey: Any, parameter_name: str = "mkey") -> str:
        """
        Validate and convert mkey to string

        Args:
            mkey: The management key value to validate
            parameter_name: Name of the parameter (for error messages)

        Returns:
            String representation of mkey

        Raises:
            ValueError: If mkey is None, empty, or invalid

        Example:
            >>> mkey = HTTPClient.validate_mkey(user_id, 'user_id')
        """
        if mkey is None:
            raise ValueError(f"{parameter_name} is required and cannot be None")

        mkey_str = str(mkey).strip()
        if not mkey_str:
            raise ValueError(f"{parameter_name} cannot be empty")

        return mkey_str

    @staticmethod
    def validate_required_params(params: dict[str, Any], required: list[str]) -> None:
        """
        Validate that required parameters are present in params dict

        Args:
            params: Dictionary of parameters to validate
            required: List of required parameter names

        Raises:
            ValueError: If any required parameters are missing

        Example:
            >>> HTTPClient.validate_required_params(data, ['name', 'type'])
        """
        if not params:
            if required:
                raise ValueError(f"Missing required parameters: {', '.join(required)}")
            return

        missing = [param for param in required if param not in params or params[param] is None]
        if missing:
            raise ValueError(f"Missing required parameters: {', '.join(missing)}")

    @staticmethod
    def validate_range(
        value: Union[int, float],
        min_val: Union[int, float],
        max_val: Union[int, float],
        parameter_name: str = "value",
    ) -> None:
        """
        Validate that a numeric value is within a specified range

        Args:
            value: The value to validate
            min_val: Minimum allowed value (inclusive)
            max_val: Maximum allowed value (inclusive)
            parameter_name: Name of the parameter (for error messages)

        Raises:
            ValueError: If value is outside the specified range

        Example:
            >>> HTTPClient.validate_range(port, 1, 65535, 'port')
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{parameter_name} must be a number")

        if not (min_val <= value <= max_val):
            raise ValueError(
                f"{parameter_name} must be between {min_val} and {max_val}, got {value}"
            )

    @staticmethod
    def validate_choice(value: Any, choices: list[Any], parameter_name: str = "value") -> None:
        """
        Validate that a value is one of the allowed choices

        Args:
            value: The value to validate
            choices: List of allowed values
            parameter_name: Name of the parameter (for error messages)

        Raises:
            ValueError: If value is not in the allowed choices

        Example:
            >>> HTTPClient.validate_choice(protocol, ['tcp', 'udp'], 'protocol')
        """
        if value not in choices:
            raise ValueError(f"{parameter_name} must be one of {choices}, got '{value}'")

    @staticmethod
    def build_params(**kwargs: Any) -> dict[str, Any]:
        """
        Build parameters dict, filtering out None values

        Args:
            **kwargs: Keyword arguments to build params from

        Returns:
            Dictionary with None values removed

        Example:
            >>> params = HTTPClient.build_params(format=['name'], datasource=True, other=None)
            >>> # Returns: {'format': ['name'], 'datasource': True}
        """
        return {k: v for k, v in kwargs.items() if v is not None}

    def __enter__(self) -> "HTTPClient":
        """Enter context manager - returns self for use in 'with' statements"""
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any]
    ) -> None:
        """Exit context manager - ensures session is closed"""
        self.close()

    def close(self) -> None:
        """Close the HTTP session and release resources"""
        if self._client:
            self._client.close()
            logger.debug("HTTP client session closed")

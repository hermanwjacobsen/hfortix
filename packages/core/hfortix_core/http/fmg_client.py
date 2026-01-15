"""
FortiManager HTTP Client

HTTP client for FortiManager JSON-RPC API with session-based authentication.
Shares retry logic, circuit breaker, and connection pooling with HTTPClient.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Literal, Optional

import httpx

from .base import BaseHTTPClient

logger = logging.getLogger("hfortix.http.fmg")

__all__ = ["HTTPClientFMG"]


class HTTPClientFMG(BaseHTTPClient):
    """
    HTTP client for FortiManager JSON-RPC API.
    
    Provides session-based authentication and JSON-RPC request handling
    while reusing the retry logic, circuit breaker, connection pooling,
    and statistics from BaseHTTPClient.
    
    FortiManager uses a different authentication model than FortiOS:
    - FortiOS: REST API with Bearer token in headers
    - FortiManager: JSON-RPC API with session token in request body
    
    Example:
        >>> client = HTTPClientFMG(
        ...     url="https://fmg.example.com",
        ...     username="admin",
        ...     password="password",
        ... )
        >>> client.login()
        >>> response = client.execute("get", [{"url": "/dvmdb/device"}])
        >>> client.logout()
    """
    
    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        verify: bool = True,
        adom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
    ) -> None:
        """
        Initialize FortiManager HTTP client.
        
        Args:
            url: Base URL for FMG (e.g., "https://fmg.example.com")
            username: Admin username
            password: Admin password
            verify: Verify SSL certificates (default: True)
            adom: Default ADOM for operations
            max_retries: Maximum retry attempts on transient failures
            connect_timeout: Connection timeout in seconds
            read_timeout: Read timeout in seconds
            circuit_breaker_threshold: Failures before opening circuit
            circuit_breaker_timeout: Seconds before retrying after circuit opens
            max_connections: Maximum connection pool size
            max_keepalive_connections: Maximum keepalive connections
            adaptive_retry: Enable adaptive retry with backpressure detection
            retry_strategy: 'exponential' or 'linear' backoff
            retry_jitter: Add random jitter to retry delays
        """
        super().__init__(
            url=url,
            verify=verify,
            vdom=None,  # FMG uses ADOM, not VDOM
            max_retries=max_retries,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            circuit_breaker_threshold=circuit_breaker_threshold,
            circuit_breaker_timeout=circuit_breaker_timeout,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            adaptive_retry=adaptive_retry,
            retry_strategy=retry_strategy,
            retry_jitter=retry_jitter,
        )
        
        self._username = username
        self._password = password
        self._adom = adom  # For logging context
        
        self._session_token: str | None = None
        self._request_id: int = 0
        
        # HTTP client with connection pooling
        self._http_client: httpx.Client | None = None
        self._max_connections = max_connections
        self._max_keepalive = max_keepalive_connections
    
    @property
    def jsonrpc_url(self) -> str:
        """JSON-RPC endpoint URL."""
        return f"{self._url}/jsonrpc"
    
    @property
    def is_authenticated(self) -> bool:
        """Check if we have a valid session."""
        return self._session_token is not None
    
    @property
    def adom(self) -> str | None:
        """Default ADOM."""
        return self._adom
    
    def _get_http_client(self) -> httpx.Client:
        """Get or create HTTP client with connection pooling."""
        if self._http_client is None:
            limits = httpx.Limits(
                max_connections=self._max_connections,
                max_keepalive_connections=self._max_keepalive,
            )
            timeout = httpx.Timeout(
                connect=self._connect_timeout,
                read=self._read_timeout,
                write=30.0,
                pool=10.0,
            )
            self._http_client = httpx.Client(
                verify=self._verify,
                limits=limits,
                timeout=timeout,
            )
        return self._http_client
    
    def _next_id(self) -> int:
        """Get next request ID."""
        self._request_id += 1
        return self._request_id
    
    def login(self) -> None:
        """
        Authenticate with FortiManager.
        
        Raises:
            RuntimeError: If authentication fails
        """
        if self._session_token:
            return  # Already logged in
        
        request = {
            "id": self._next_id(),
            "method": "exec",
            "params": [
                {
                    "url": "/sys/login/user",
                    "data": {
                        "user": self._username,
                        "passwd": self._password,
                    }
                }
            ],
        }
        
        logger.debug("Logging in to FortiManager at %s", self._url)
        
        client = self._get_http_client()
        response = client.post(self.jsonrpc_url, json=request)
        response.raise_for_status()
        
        data = response.json()
        
        # Check for successful login
        result = data.get("result", [{}])[0]
        status = result.get("status", {})
        
        if status.get("code") != 0:
            error_msg = status.get("message", "Unknown error")
            logger.error("FMG login failed: %s", error_msg)
            raise RuntimeError(f"FMG login failed: {error_msg}")
        
        self._session_token = data.get("session")
        if not self._session_token:
            raise RuntimeError("FMG login succeeded but no session token received")
        
        logger.info("Successfully logged in to FortiManager")
    
    def logout(self) -> None:
        """End FortiManager session."""
        if not self._session_token:
            return
        
        try:
            request = {
                "id": self._next_id(),
                "method": "exec",
                "params": [{"url": "/sys/logout"}],
                "session": self._session_token,
            }
            
            client = self._get_http_client()
            client.post(self.jsonrpc_url, json=request)
            logger.debug("Logged out from FortiManager")
        except Exception as e:
            logger.debug("Logout error (ignored): %s", e)
        finally:
            self._session_token = None
    
    def execute(
        self,
        method: Literal["exec", "get", "set", "add", "update", "delete"],
        params: list[dict[str, Any]],
        verbose: int = 1,
    ) -> dict[str, Any]:
        """
        Execute a FortiManager JSON-RPC request.
        
        Args:
            method: JSON-RPC method
            params: Request parameters
            verbose: Verbosity level (0 or 1)
            
        Returns:
            FMG response dict
            
        Raises:
            RuntimeError: If not authenticated or request fails
        """
        if not self._session_token:
            self.login()
        
        endpoint = params[0].get("url", "/unknown") if params else "/unknown"
        
        # Check circuit breaker
        self._check_circuit_breaker(endpoint)
        
        request = {
            "id": self._next_id(),
            "method": method,
            "params": params,
            "session": self._session_token,
            "verbose": verbose,
        }
        
        start_time = time.perf_counter()
        attempt = 0
        last_error: Exception | None = None
        
        while attempt <= self._max_retries:
            try:
                client = self._get_http_client()
                response = client.post(self.jsonrpc_url, json=request)
                response.raise_for_status()
                
                data = response.json()
                
                # Check for FMG-level errors
                result = data.get("result", [{}])[0] if data.get("result") else {}
                status = result.get("status", {})
                
                if status.get("code") != 0:
                    error_msg = status.get("message", "Unknown error")
                    # Session expired - try to re-login
                    if "session" in error_msg.lower() or status.get("code") == -11:
                        self._session_token = None
                        self.login()
                        request["session"] = self._session_token
                        continue
                    
                    raise RuntimeError(f"FMG request failed: {error_msg}")
                
                # Success
                duration = time.perf_counter() - start_time
                self._record_circuit_breaker_success()
                self._retry_stats["successful_requests"] += 1
                self._retry_stats["total_requests"] += 1
                
                logger.debug(
                    "FMG request completed in %.3fs",
                    duration,
                    extra=self._log_context(endpoint=endpoint, duration_seconds=duration),
                )
                
                return data
                
            except httpx.TimeoutException as e:
                last_error = e
                if self._should_retry(e, attempt, endpoint):
                    attempt += 1
                    self._record_retry("timeout", endpoint)
                    delay = self._calculate_retry_delay(attempt)
                    logger.warning(
                        "Request timeout, retrying in %.1fs (attempt %d/%d)",
                        delay, attempt, self._max_retries + 1,
                    )
                    time.sleep(delay)
                    continue
                raise
                
            except httpx.HTTPStatusError as e:
                last_error = e
                if e.response.status_code >= 500 and self._should_retry(e, attempt, endpoint):
                    attempt += 1
                    self._record_retry("server_error", endpoint)
                    delay = self._calculate_retry_delay(attempt)
                    logger.warning(
                        "Server error %d, retrying in %.1fs (attempt %d/%d)",
                        e.response.status_code, delay, attempt, self._max_retries + 1,
                    )
                    time.sleep(delay)
                    continue
                raise
                
            except Exception as e:
                last_error = e
                self._record_circuit_breaker_failure(endpoint)
                raise
        
        # All retries exhausted
        self._retry_stats["failed_requests"] += 1
        self._retry_stats["total_requests"] += 1
        self._record_circuit_breaker_failure(endpoint)
        
        if last_error:
            raise last_error
        raise RuntimeError("Request failed after all retries")
    
    def _calculate_retry_delay(self, attempt: int) -> float:
        """Calculate retry delay based on strategy."""
        if self._retry_strategy == "exponential":
            delay = min(2 ** (attempt - 1), 30.0)  # Max 30 seconds
        else:  # linear
            delay = min(attempt, 5.0)  # Max 5 seconds
        
        if self._retry_jitter:
            import random
            jitter = random.uniform(0, delay * 0.25)
            delay += jitter
        
        return delay
    
    def proxy_request(
        self,
        action: Literal["get", "post", "put", "delete"],
        resource: str,
        targets: list[str],
        payload: dict[str, Any] | None = None,
        timeout: int = 60,
    ) -> dict[str, Any]:
        """
        Execute a FortiOS API call through the FMG proxy endpoint.
        
        This is the core method for routing FortiOS REST API calls
        through FortiManager to managed devices.
        
        Args:
            action: HTTP method (get, post, put, delete)
            resource: FortiOS API resource path (e.g., "/api/v2/cmdb/firewall/address")
            targets: List of target devices/groups (e.g., ["adom/root/device/fw-01"])
            payload: Request body for POST/PUT
            timeout: Request timeout in seconds
            
        Returns:
            FMG response dict containing results from each target device
        """
        data: dict[str, Any] = {
            "action": action,
            "resource": resource,
            "target": targets,
            "timeout": timeout,
        }
        
        if payload:
            data["payload"] = payload
        
        params = [
            {
                "url": "/sys/proxy/json",
                "data": data,
            }
        ]
        
        return self.execute("exec", params)
    
    def close(self) -> None:
        """Close the session and HTTP client."""
        self.logout()
        if self._http_client:
            self._http_client.close()
            self._http_client = None
    
    def __enter__(self) -> "HTTPClientFMG":
        """Context manager entry."""
        self.login()
        return self
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()
    
    # ========================================================================
    # Statistics and Health Methods (from BaseHTTPClient)
    # ========================================================================
    
    def get_health_metrics(self) -> dict[str, Any]:
        """Get health metrics for monitoring."""
        return {
            "authenticated": self.is_authenticated,
            "circuit_breaker": self.get_circuit_breaker_state(),
            "retry_stats": self.get_retry_stats(),
            "adom": self._adom,
        }
    
    def get_connection_stats(self) -> dict[str, Any]:
        """Get connection pool statistics."""
        stats: dict[str, Any] = {
            "max_connections": self._max_connections,
            "max_keepalive": self._max_keepalive,
        }
        
        if self._http_client:
            # httpx doesn't expose detailed pool stats, but we can track
            stats["client_active"] = True
        else:
            stats["client_active"] = False
        
        return stats

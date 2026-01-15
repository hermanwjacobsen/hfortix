"""
Internal HTTP Client for FortiOS API

This module contains the HTTPClient class which handles all HTTP communication
with FortiGate devices. It is an internal implementation detail and not part
of the public API.

Now powered by httpx for better performance, HTTP/2 support, and modern async
capabilities.
"""

from __future__ import annotations

import logging
import time
import uuid
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeAlias, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

from urllib.parse import quote, urlencode

import httpx
from hfortix_core.http.base import BaseHTTPClient

logger = logging.getLogger("hfortix.http")

# Type alias for API responses
HTTPResponse: TypeAlias = dict[str, Any]

__all__ = ["HTTPClient", "HTTPResponse", "encode_path_component"]


def encode_path_component(component: str | int) -> str:
    """
    Encode a single path component for use in URLs.

    This encodes special characters including forward slashes, which are
    commonly used in FortiOS object names (e.g., IP addresses with CIDR
    notation).

    Args:
        component: Path component to encode (e.g., object name or ID)

    Returns:
        URL-encoded string safe for use in URL paths

    Examples:
        >>> encode_path_component("Test_NET_192.0.2.0/24")
        'Test_NET_192.0.2.0%2F24'
        >>> encode_path_component("test@example.com")
        'test%40example.com'
        >>> encode_path_component(123)
        '123'
    """
    return quote(str(component), safe="")


class HTTPClient(BaseHTTPClient):
    """
    Internal HTTP client for FortiOS API requests (Sync Implementation)

    Implements the IHTTPClient protocol for synchronous HTTP operations.

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
        - Lists: Encoded as repeated parameters (e.g., ['a', 'b'] →
        ?key=a&key=b)
        - Booleans: Converted to lowercase strings ('true'/'false')
        - None values: Should be filtered out before passing to params
        - Special characters: URL-encoded automatically

    Path Encoding:
        Paths are URL-encoded with / and % as safe characters to prevent
        double-encoding of already-encoded components.

    Protocol Implementation:
        This class implements the IHTTPClient protocol, allowing it to be used
        interchangeably with other HTTP client implementations (e.g.,
        AsyncHTTPClient,
        custom user-provided clients).

    This class is internal and not exposed to users directly, but users can
    provide
    their own IHTTPClient implementations to FortiOS.__init__().
    """

    def __init__(
        self,
        url: str,
        verify: bool = True,
        token: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        vdom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        session_idle_timeout: Union[int, float, None] = 300,
        read_only: bool = False,
        track_operations: bool = False,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
        audit_handler: Optional[Any] = None,
        audit_callback: Optional[Any] = None,
        user_context: Optional[dict[str, Any]] = None,
    ) -> None:
        """
        Initialize HTTP client

        Args:
            url: Base URL for API (e.g., "https://192.0.2.10")
            verify: Verify SSL certificates
            token: API authentication token (if using token auth)
            username: Username for authentication (if using username/password
            auth)
            password: Password for authentication (if using username/password
            auth)
            vdom: Default virtual domain
            max_retries: Maximum number of retry attempts on transient failures
            (default: 3)
            connect_timeout: Timeout for establishing connection in seconds
            (default: 10.0)
            read_timeout: Timeout for reading response in seconds (default:
            300.0)
            user_agent: Custom User-Agent header for identifying application in
            FortiGate logs.
                       If None, defaults to 'hfortix/{version}'. Useful for
                       multi-team environments
                       and troubleshooting in production.
            circuit_breaker_threshold: Number of consecutive failures before
            opening circuit (default: 10)
            circuit_breaker_timeout: Seconds to wait before transitioning to
            half-open (default: 30.0)
            circuit_breaker_auto_retry: Enable automatic retry when circuit
            breaker opens (default: False).
                       When enabled, waits circuit_breaker_retry_delay seconds
                       between retries instead of
                       immediately raising exception. Useful for long-running
                       automation scripts.
                       NOT recommended for tests or interactive use.
            circuit_breaker_max_retries: Maximum retry attempts when
            circuit_breaker_auto_retry=True (default: 3)
            circuit_breaker_retry_delay: Delay in seconds between retry
            attempts when auto-retry enabled (default: 5.0).
                       This is separate from circuit_breaker_timeout, which
                       controls when the circuit
                       transitions from open to half-open.
            max_connections: Maximum number of connections in the pool
            (default: 100)
            max_keepalive_connections: Maximum number of keepalive connections
            (default: 20)
            session_idle_timeout: For username/password auth only. Idle timeout
            in seconds before
                       proactively re-authenticating (default: 300 = 5
                       minutes). This should match
                       your FortiGate's 'config system global' ->
                       'remoteauthtimeout' setting.
                       Set to None to disable proactive re-authentication.
                       Note: API token authentication is stateless and doesn't
                       use sessions.
            read_only: Enable read-only mode - simulate write operations
            without executing (default: False)
            track_operations: Enable operation tracking - maintain audit log of
            all API calls (default: False)
            adaptive_retry: Enable adaptive retry with backpressure detection
            (default: False).
                          When enabled, monitors response times and adjusts
                          retry delays based on
                          FortiGate health signals (slow responses, 503
                          errors). Increases retry
                          delays when FortiGate is overloaded to prevent
                          cascading failures.
            retry_strategy: Retry backoff strategy - 'exponential' (default)
                          or 'linear'. Exponential: 1s, 2s, 4s, 8s, 16s, 30s.
                          Linear: 1s, 2s, 3s, 4s, 5s. Use exponential for
                          transient failures, linear for rate limiting.
            retry_jitter: Add random jitter (0-25% of delay) to retry delays
                         to prevent thundering herd problem when multiple
                         clients retry simultaneously (default: False).
            audit_handler: Handler for audit logging (implements AuditHandler
            protocol).
                          Use built-in handlers: SyslogHandler, FileHandler,
                          StreamHandler,
                          CompositeHandler. Essential for compliance (SOC 2,
                          HIPAA, PCI-DSS).
                          Example: SyslogHandler("siem.company.com:514")
            audit_callback: Custom callback function for audit logging.
                           Alternative to audit_handler. Receives operation
                           dict as parameter.
                           Example: lambda op: send_to_kafka(op)
            user_context: Optional dict with user/application context to
            include in audit logs.
                         Example: {"username": "admin", "app": "automation",
                         "ticket": "CHG-12345"}

        Raises:
            ValueError: If parameters are invalid or both token and
            username/password provided
        """
        # Validate authentication parameters
        if token and (username or password):
            raise ValueError(
                "Cannot specify both token and username/password authentication"  # noqa: E501
            )
        if (username and not password) or (password and not username):
            raise ValueError(
                "Both username and password must be provided together"
            )

        # Call parent class constructor (handles validation and common
        # initialization)
        super().__init__(
            url=url,
            verify=verify,
            vdom=vdom,
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

        # Store circuit breaker auto-retry settings
        self._circuit_breaker_auto_retry = circuit_breaker_auto_retry
        self._circuit_breaker_max_retries = circuit_breaker_max_retries
        self._circuit_breaker_retry_delay = circuit_breaker_retry_delay

        # Store connection pool settings for monitoring
        self._max_connections = max_connections
        self._max_keepalive_connections = max_keepalive_connections

        # Set default User-Agent if not provided
        if user_agent is None:
            # Import here to avoid circular dependency
            from hfortix_core import __version__

            user_agent = f"hfortix/{__version__}"

        # Initialize httpx client with proper timeout configuration
        self._client = httpx.Client(
            headers={"User-Agent": user_agent},
            timeout=httpx.Timeout(
                connect=connect_timeout,
                read=read_timeout,
                write=30.0,  # Default write timeout
                pool=10.0,  # Default pool timeout
            ),
            verify=verify,
            http2=True,  # Enable HTTP/2 support
            limits=httpx.Limits(
                max_connections=max_connections,
                max_keepalive_connections=max_keepalive_connections,
            ),
        )

        # Store authentication credentials
        self._token = token
        self._username = username
        self._password = password
        # For username/password auth
        self._session_token: Optional[str] = None
        # Track when session was created
        self._session_created_at: Optional[float] = None
        # Track last request time
        self._session_last_activity: Optional[float] = None
        self._using_token_auth = token is not None

        # Session timeout settings (in seconds) - only for username/password
        # auth
        # If session_idle_timeout is None or False, disable proactive
        # re-authentication
        if session_idle_timeout:
            self._session_idle_timeout: float | None = float(
                session_idle_timeout
            )
            # Re-authenticate at 80% of idle timeout to avoid session
            # expiration
            self._session_proactive_refresh: float | None = (
                self._session_idle_timeout * 0.8
            )
        else:
            # Disable proactive re-authentication
            self._session_idle_timeout = None
            self._session_proactive_refresh = None

        # Read-only mode and operation tracking
        self._read_only = read_only
        self._track_operations = track_operations
        self._operations: list[dict[str, Any]] = [] if track_operations else []

        # Audit logging
        self._audit_handler = audit_handler
        self._audit_callback = audit_callback
        self._user_context = user_context or {}

        # Connection pool monitoring
        self._active_requests = 0
        self._total_requests = 0
        self._pool_exhaustion_count = 0
        self._pool_exhaustion_timestamps: list[float] = []

        # Request inspection for debugging
        self._last_request: Optional[dict[str, Any]] = None
        self._last_response: Optional[dict[str, Any]] = None
        self._last_response_time: Optional[float] = None

        # Set token if provided
        if token:
            self._client.headers["Authorization"] = f"Bearer {token}"

        # If using username/password, login automatically
        if username and password:
            self.login()

        logger.debug(
            "HTTP client initialized for %s (max_retries=%d, connect_timeout=%.1fs, read_timeout=%.1fs, "  # noqa: E501
            "http2=enabled, user_agent='%s', circuit_breaker_threshold=%d, max_connections=%d, "  # noqa: E501
            "read_only=%s, track_operations=%s)",
            self._url,
            max_retries,
            connect_timeout,
            read_timeout,
            user_agent,
            circuit_breaker_threshold,
            max_connections,
            read_only,
            track_operations,
        )

    def login(self) -> None:
        """
        Authenticate using username/password and obtain session token

        This method is called automatically if username/password are provided
        during initialization. Can also be called manually to re-authenticate.

        Raises:
            ValueError: If username/password not configured
            AuthenticationError: If login fails
        """
        if not self._username or not self._password:
            raise ValueError("Username and password required for login")

        logger.debug("Authenticating with username/password for %s", self._url)

        try:
            # FortiOS login endpoint - note: parameter name is "secretkey" not
            # "password"
            login_url = f"{self._url}/logincheck"

            # URL-encode the form data (FortiOS expects
            # application/x-www-form-urlencoded)
            login_data = urlencode(
                [("username", self._username), ("secretkey", self._password)]
            )

            # Make login request with proper content type
            # Note: FortiOS may redirect after login, so we follow redirects
            response = self._client.post(
                login_url,
                content=login_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                follow_redirects=True,  # Changed to True to handle FortiOS redirects  # noqa: E501
            )

            # Debug: Log response details
            logger.debug(f"Login response status: {response.status_code}")
            logger.debug(f"Login response headers: {dict(response.headers)}")
            logger.debug(f"Login response cookies: {dict(response.cookies)}")
            logger.debug(f"Login response history: {response.history}")
            logger.debug(
                f"Login response text (first 500 chars): {response.text[:500]}"
            )

            # Check for successful login (FortiOS returns 200 with CSRF token
            # in cookies)
            response.raise_for_status()

            # Extract CSRF token from cookies (may be in the client's cookie
            # jar after redirects)
            csrf_token = None

            # Check response cookies first
            for cookie_name, cookie_value in response.cookies.items():
                logger.debug(
                    f"Response cookie: {cookie_name} = {cookie_value}"
                )
                if "ccsrftoken" in cookie_name.lower():
                    csrf_token = cookie_value
                    break

            # If not found, check the client's cookie jar
            if not csrf_token:
                for cookie_name, cookie_value in self._client.cookies.items():
                    logger.debug(
                        f"Client cookie: {cookie_name} = {cookie_value}"
                    )
                    if "ccsrftoken" in cookie_name.lower():
                        csrf_token = cookie_value
                        break

            if csrf_token:
                self._session_token = csrf_token
                self._client.headers["X-CSRFTOKEN"] = csrf_token
                # Track session creation time
                self._session_created_at = time.time()
                self._session_last_activity = time.time()
                logger.info("Successfully authenticated via username/password")
            else:
                # If still HTML in response, authentication likely failed
                if (
                    "<!doctype html>" in response.text.lower()
                    or "<html" in response.text.lower()
                ):
                    raise ValueError(
                        "Login failed: FortiGate returned login page. "
                        "Please verify username and password are correct."
                    )
                raise ValueError(
                    "Login succeeded but no CSRF token found in response"
                )

        except httpx.HTTPError as e:
            logger.error("Login failed: %s", str(e))
            raise ValueError(f"Login failed: {str(e)}") from e

    def _should_refresh_session(self) -> bool:
        """
        Check if the session should be proactively refreshed

        Returns:
            True if session needs refresh (approaching idle timeout), False
            otherwise
        """
        # Only applicable for username/password auth with idle timeout enabled
        if (
            self._using_token_auth
            or not self._session_last_activity
            or self._session_proactive_refresh is None
        ):
            return False

        # Check if we're approaching the idle timeout threshold
        time_since_last_activity = time.time() - self._session_last_activity
        return time_since_last_activity >= self._session_proactive_refresh

    def logout(self) -> None:
        """
        Logout and invalidate session token

        This method is called automatically when using context manager (with
        statement).
        Can also be called manually to explicitly logout.

        Note:
            Only applicable when using username/password authentication.
            Token-based authentication doesn't require logout.
        """
        if not self._session_token:
            logger.debug(
                "No active session to logout (using token auth or not logged in)"  # noqa: E501
            )
            return

        logger.debug("Logging out from %s", self._url)

        try:
            logout_url = f"{self._url}/logout"
            response = self._client.post(logout_url)

            if response.status_code == 200:
                logger.info("Successfully logged out")
            else:
                logger.warning(
                    "Logout returned status code %d", response.status_code
                )

        except httpx.HTTPError as e:
            logger.warning("Logout failed: %s", str(e))
        finally:
            # Clear session token, timestamps, and header regardless of logout
            # result
            self._session_token = None
            self._session_created_at = None
            self._session_last_activity = None
            if "X-CSRFTOKEN" in self._client.headers:
                del self._client.headers["X-CSRFTOKEN"]

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get HTTP connection pool statistics

        Returns:
            dict: Connection statistics including:
                - http2_enabled: Whether HTTP/2 is enabled
                - max_connections: Maximum number of connections allowed
                - max_keepalive_connections: Maximum keepalive connections
                - active_requests: Current number of active requests
                - total_requests: Total requests made since initialization
                - pool_exhaustion_count: Times pool reached capacity
                - circuit_breaker_state: Current circuit breaker state
                - consecutive_failures: Number of consecutive failures

        Example:
            >>> stats = client.get_connection_stats()
            >>> print(f"Circuit breaker: {stats['circuit_breaker_state']}")
            >>> print(f"Active requests: {stats['active_requests']}")
        """
        return {
            "http2_enabled": True,
            "max_connections": self._max_connections,
            "max_keepalive_connections": self._max_keepalive_connections,
            "active_requests": self._active_requests,
            "total_requests": self._total_requests,
            "pool_exhaustion_count": self._pool_exhaustion_count,
            "circuit_breaker_state": self._circuit_breaker["state"],
            "consecutive_failures": self._circuit_breaker[
                "consecutive_failures"
            ],
            "last_failure_time": self._circuit_breaker["last_failure_time"],
        }

    def inspect_last_request(self) -> dict[str, Any]:
        """
        Get details of last API request for debugging

        Returns:
            dict: Request information including:
                - method: HTTP method used
                - endpoint: API endpoint path
                - params: Query parameters
                - response_time_ms: Response time in milliseconds
                - status_code: HTTP status code
                - error: Error message if no requests made

        Example:
            >>> client.get("/api/v2/cmdb/firewall/address")
            >>> info = client.inspect_last_request()
            >>> print(f"Last request took {info['response_time_ms']:.2f}ms")
        """
        if not self._last_request:
            return {"error": "No requests have been made yet"}

        result: dict[str, Any] = {
            "method": self._last_request.get("method"),
            "endpoint": self._last_request.get("endpoint"),
            "params": self._last_request.get("params"),
            "response_time_ms": (
                round(self._last_response_time * 1000, 2)
                if self._last_response_time
                else None
            ),
        }

        if self._last_response:
            result["status_code"] = self._last_response.get("status_code")

        return result

    def _check_circuit_breaker(self, endpoint: str) -> None:
        """
        Override base class circuit breaker check with optional auto-retry

        Args:
            endpoint: API endpoint being checked

        Raises:
            CircuitBreakerOpenError: If circuit breaker is open and auto-retry
                is disabled or max retries exceeded
        """
        if not self._circuit_breaker_auto_retry:
            # Use default fail-fast behavior
            super()._check_circuit_breaker(endpoint)
            return

        # Auto-retry enabled - wait and retry when circuit breaker opens
        retry_count = 0
        while retry_count < self._circuit_breaker_max_retries:
            if self._circuit_breaker["state"] == "open":
                retry_count += 1
                logger.info(
                    "Circuit breaker OPEN - auto-retry %d/%d after "
                    "%.1fs delay",
                    retry_count,
                    self._circuit_breaker_max_retries,
                    self._circuit_breaker_retry_delay,
                )
                time.sleep(self._circuit_breaker_retry_delay)

                # Check if enough time has elapsed for circuit to transition
                elapsed = time.time() - (
                    self._circuit_breaker["last_failure_time"] or 0
                )
                if elapsed >= self._circuit_breaker["timeout"]:
                    # Timeout elapsed, transition to half_open
                    self._circuit_breaker["state"] = "half_open"
                    logger.info(
                        "Circuit breaker transitioning to HALF_OPEN " "state"
                    )
                # If timeout not elapsed, circuit stays open but we
                # retry anyway (the request will fail-fast again if
                # service still down)
                return
            else:
                # Circuit breaker is closed or half_open, proceed
                return

        # Max retries exceeded, raise error
        from hfortix_core.exceptions import CircuitBreakerOpenError

        raise CircuitBreakerOpenError(
            f"Circuit breaker is OPEN for {endpoint}. "
            f"Max retries ({self._circuit_breaker_max_retries}) exceeded. "
            "Service appears to be down."
        )

    def _handle_response_errors(
        self,
        response: httpx.Response,
        endpoint: Optional[str] = None,
        method: Optional[str] = None,
        params: Optional[dict[str, Any]] = None,
        silent: bool = False,
    ) -> None:
        """
        Handle HTTP response errors consistently using FortiOS error handling

        Args:
            response: httpx.Response object
            endpoint: API endpoint path for better error context
            method: HTTP method (GET, POST, PUT, DELETE)
            params: Request parameters (will be sanitized in error messages)
            silent: If True, skip logging (for expected errors like 404 in exists())

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
                from hfortix_core.exceptions import (
                    get_error_description,
                    raise_for_status,
                )

                # Try to parse JSON response (most FortiOS errors are JSON)
                json_response = response.json()

                # Add error description if error code present
                error_code = json_response.get("error")
                if error_code and "error_description" not in json_response:
                    json_response["error_description"] = get_error_description(
                        error_code
                    )

                # Log the error with details (unless silent mode)
                if not silent:
                    status = json_response.get("status")
                    http_status = json_response.get(
                        "http_status", response.status_code
                    )
                    error_desc = json_response.get(
                        "error_description", "Unknown error"
                    )

                    logger.error(
                        "Request failed: HTTP %d, status=%s, error=%s, description='%s'",  # noqa: E501
                        http_status,
                        status,
                        error_code,
                        error_desc,
                    )

                # Use FortiOS-specific error handling with enhanced context
                raise_for_status(
                    json_response,
                    endpoint=endpoint,
                    method=method,
                    params=params,
                )

            except ValueError:
                # Response is not JSON (could be binary or HTML error page)
                # This can happen with binary endpoints or proxy/firewall
                # errors
                if not silent:
                    logger.error(
                        "Request failed: HTTP %d (non-JSON response, %d bytes)",
                        response.status_code,
                        len(response.content),
                    )
                response.raise_for_status()

    def _log_audit(
        self,
        method: str,
        endpoint: str,
        api_type: str,
        path: str,
        data: Optional[dict[str, Any]],
        params: Optional[dict[str, Any]],
        status_code: int,
        success: bool,
        duration_ms: int,
        request_id: str,
        error: Optional[str] = None,
    ) -> None:
        """
        Log API operation to audit handlers

        Args:
            method: HTTP method
            endpoint: Full API endpoint
            api_type: API type (cmdb, monitor, etc.)
            path: Relative path
            data: Request data (will be sanitized)
            params: Request params (will be sanitized)
            status_code: HTTP status code
            success: Whether operation succeeded
            duration_ms: Duration in milliseconds
            request_id: Request ID
            error: Error message if failed
        """
        # Skip if no audit handler or callback configured
        if not self._audit_handler and not self._audit_callback:
            return

        try:
            from datetime import datetime, timezone

            # Determine action from method and path
            action = self._infer_action(method, path)

            # Extract object type and name from path
            object_type, object_name = self._extract_object_info(path, data)

            # Build operation dict
            operation: dict[str, Any] = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "request_id": request_id,
                "method": method.upper(),
                "endpoint": endpoint,
                "api_type": api_type,
                "path": path,
                "vdom": params.get("vdom") if params else None,
                "action": action,
                "object_type": object_type,
                "object_name": object_name,
                "data": self._sanitize_data(data) if data else None,
                "params": self._sanitize_data(params) if params else None,
                "status_code": status_code,
                "success": success,
                "duration_ms": duration_ms,
                "host": self._url.replace("https://", "").replace(
                    "http://", ""
                ),
                "read_only_mode": self._read_only
                and method in ("POST", "PUT", "DELETE"),
            }

            # Add error if present
            if error:
                operation["error"] = error

            # Add user context if provided
            if self._user_context:
                operation["user_context"] = self._user_context

            # Call audit handler if configured
            if self._audit_handler:
                try:
                    self._audit_handler.log_operation(operation)
                except Exception as e:
                    logger.error(
                        f"Audit handler failed: {e}",
                        extra={
                            "error": str(e),
                            "request_id": request_id,
                        },
                        exc_info=True,
                    )

            # Call audit callback if configured
            if self._audit_callback:
                try:
                    self._audit_callback(operation)
                except Exception as e:
                    logger.error(
                        f"Audit callback failed: {e}",
                        extra={
                            "error": str(e),
                            "request_id": request_id,
                        },
                        exc_info=True,
                    )

        except Exception as e:
            # Don't let audit failures break API operations
            logger.error(
                f"Audit logging failed: {e}",
                extra={"error": str(e), "request_id": request_id},
                exc_info=True,
            )

    @staticmethod
    def _infer_action(method: str, path: str) -> str:
        """Infer high-level action from method and path"""
        method = method.upper()

        if method == "GET":
            # Heuristic: if path ends with a specific name, it's a read,
            # otherwise it's a list
            parts = path.strip("/").split("/")
            if len(parts) > 0 and parts[-1] and not parts[-1].startswith("?"):
                # Has a trailing identifier
                return "read"
            return "list"
        elif method == "POST":
            return "create"
        elif method == "PUT":
            return "update"
        elif method == "DELETE":
            return "delete"
        else:
            return "unknown"

    @staticmethod
    def _extract_object_info(
        path: str, data: Optional[dict[str, Any]]
    ) -> tuple[str, Optional[str]]:
        """
        Extract object type and name from path and data

        Returns:
            Tuple of (object_type, object_name)
        """
        # Clean path
        path = path.strip("/")

        # Object type is the full path with dots instead of slashes
        # e.g., "firewall/address" -> "firewall.address"
        object_type = path.replace("/", ".")

        # Try to extract object name from:
        # 1. Last path component (if it looks like a name)
        # 2. 'name' field in data
        # 3. 'mkey' field in data
        object_name = None

        parts = path.split("/")
        if len(parts) > 0:
            last_part = parts[-1]
            # If last part doesn't look like an endpoint, use it as name
            if last_part and not last_part.startswith("?"):
                object_name = last_part

        # Override with data if available
        if data:
            if "name" in data:
                object_name = str(data["name"])
            elif "mkey" in data:
                object_name = str(data["mkey"])

        return object_type, object_name

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
        silent: bool = False,
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
            raw_json: If False (default), return only 'results' field. If True,
            return full response
            request_id: Optional correlation ID for tracking requests across
            logs
            silent: If True, suppress error logging (for exists() checks)

        Returns:
            dict: If raw_json=False, returns response['results'] (or full
            response if no 'results' key)
                  If raw_json=True, returns complete API response with status,
                  http_status, etc.
        """
        # Generate request ID if not provided
        if request_id is None:
            request_id = str(uuid.uuid4())[:8]  # Short UUID for readability

        # Normalize path: remove any leading slash so callers may pass
        # either 'firewall/acl' or '/firewall/acl' without causing a
        # double-slash
        # in the constructed URL. Keep internal separators intact.
        path = self._normalize_path(path)

        # URL encode the path, treating / as safe (path separator)
        # Individual path components may already be encoded by endpoint files
        # using
        # encode_path_component(), so quote() with safe='/' won't double-encode
        # already-encoded %XX sequences (e.g., %2F stays as %2F)
        encoded_path = (
            quote(str(path), safe="/%") if isinstance(path, str) else path
        )
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
        except RuntimeError:
            # Structured log for circuit breaker open
            logger.error(
                "Circuit breaker blocked request",
                extra=self._log_context(
                    request_id=request_id,
                    method=method,
                    endpoint=full_path,
                    circuit_state=self._circuit_breaker["state"],
                    consecutive_failures=self._circuit_breaker[
                        "consecutive_failures"
                    ],
                ),
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
            extra=self._log_context(
                request_id=request_id,
                method=method.upper(),
                endpoint=full_path,
                has_data=bool(data),
                has_params=bool(params),
            ),
        )
        if params:
            logger.debug(
                "Request parameters",
                extra=self._log_context(
                    request_id=request_id,
                    params=self._sanitize_data(params),
                ),
            )
        if data:
            logger.debug(
                "Request data",
                extra=self._log_context(
                    request_id=request_id,
                    data=self._sanitize_data(data),
                ),
            )

        # Track timing
        start_time = time.time()

        # Track total requests
        self._retry_stats["total_requests"] += 1

        # ========================================================================
        # Read-Only Mode Check
        # ========================================================================
        # If in read-only mode, block write operations
        if self._read_only and method in ("POST", "PUT", "DELETE"):
            logger.error(
                "READ-ONLY MODE: %s request blocked",
                method,
                extra={
                    "request_id": request_id,
                    "method": method.upper(),
                    "endpoint": full_path,
                    "data": self._sanitize_data(data) if data else None,
                },
            )

            # Track blocked operation
            if self._track_operations:
                from datetime import datetime, timezone

                self._operations.append(
                    {
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "method": method.upper(),
                        "api_type": api_type,
                        "path": f"/{path}",
                        "data": data,
                        "status_code": 403,  # Forbidden
                        "vdom": params.get("vdom") if params else None,
                        "blocked_by_read_only": True,
                    }
                )

            # Raise error - operation blocked
            from hfortix_core.exceptions import ReadOnlyModeError

            raise ReadOnlyModeError(
                f"{method} operation blocked by read-only mode: {full_path}"
            )

        # Proactively check if session needs refresh (username/password auth
        # only)
        if self._should_refresh_session():
            logger.info(
                "Session approaching idle timeout, proactively re-authenticating",  # noqa: E501
                extra={
                    "request_id": request_id,
                    "time_since_last_activity": round(
                        time.time() - (self._session_last_activity or 0), 1
                    ),
                },
            )
            try:
                self.login()
                logger.info("Proactive re-authentication successful")
            except Exception as e:
                logger.warning(
                    "Proactive re-authentication failed, will retry on 401: %s",  # noqa: E501
                    str(e),
                )

        # Retry loop with exponential backoff
        last_error = None
        session_retry_attempted = (
            False  # Track if we've tried re-authenticating
        )

        for attempt in range(self._max_retries + 1):
            try:
                # Update last activity time (for idle timeout tracking)
                if (
                    not self._using_token_auth
                    and self._session_last_activity is not None
                ):
                    self._session_last_activity = time.time()

                # Track active requests and total requests
                self._active_requests += 1
                self._total_requests += 1

                # Store request details for debugging
                self._last_request = {
                    "method": method.upper(),
                    "endpoint": full_path,
                    "params": params,
                    "data": data,
                    "timestamp": time.time(),
                }

                try:
                    # Make request with httpx client
                    res = self._client.request(
                        method=method,
                        url=url,
                        json=data if data else None,
                        params=params if params else None,
                    )

                    # Store response details for debugging
                    self._last_response = {
                        "status_code": res.status_code,
                        "headers": dict(res.headers),
                    }

                except httpx.PoolTimeout:
                    # Track pool exhaustion
                    self._pool_exhaustion_count += 1
                    self._pool_exhaustion_timestamps.append(time.time())
                    logger.warning(
                        "Connection pool exhausted",
                        extra={
                            "request_id": request_id,
                            "endpoint": full_path,
                            "active_requests": self._active_requests,
                            "max_connections": self._max_connections,
                        },
                    )
                    raise
                finally:
                    # Always decrement active requests
                    self._active_requests -= 1

                # Calculate duration
                duration = time.time() - start_time
                self._last_response_time = duration

                # Record response time for adaptive backpressure (if enabled)
                self._record_response_time(endpoint_key, duration)

                # Handle errors (will raise exception if error response)
                self._handle_response_errors(
                    res,
                    endpoint=full_path,
                    method=method.upper(),
                    params=params,
                    silent=silent,
                )

                # Record success in circuit breaker
                self._record_circuit_breaker_success()

                # Record successful request
                self._retry_stats["successful_requests"] += 1

                # Track operation if enabled
                if self._track_operations:
                    from datetime import datetime, timezone

                    self._operations.append(
                        {
                            "timestamp": datetime.now(
                                timezone.utc
                            ).isoformat(),
                            "method": method.upper(),
                            "api_type": api_type,
                            "path": f"/{path}",
                            "data": (
                                data if method in ("POST", "PUT") else None
                            ),
                            "status_code": res.status_code,
                            "vdom": params.get("vdom") if params else None,
                            # Indicates read-only mode was NOT active
                            # (operation executed)
                            "read_only": False,
                        }
                    )

                # Structured log for successful response
                logger.info(
                    "Request completed successfully",
                    extra=self._log_context(
                        request_id=request_id,
                        method=method.upper(),
                        endpoint=full_path,
                        status_code=res.status_code,
                        duration_seconds=round(duration, 3),
                        attempts=attempt + 1,
                    ),
                )

                # Audit logging for successful operations
                self._log_audit(
                    method=method,
                    endpoint=full_path,
                    api_type=api_type,
                    path=path,
                    data=data,
                    params=params,
                    status_code=res.status_code,
                    success=True,
                    duration_ms=int(duration * 1000),
                    request_id=request_id,
                )

                # Warn about slow requests
                if duration > 2.0:
                    logger.warning(
                        "Slow request detected",
                        extra=self._log_context(
                            request_id=request_id,
                            method=method.upper(),
                            endpoint=full_path,
                            duration_seconds=round(duration, 3),
                        ),
                    )

                # Check content type to determine if response is JSON
                content_type = res.headers.get("content-type", "").lower()
                is_json_response = "application/json" in content_type

                # Parse JSON response or return raw content for non-JSON responses
                if is_json_response:
                    try:
                        json_response = res.json()
                    except Exception as json_err:
                        # If JSON parsing fails, log warning and return text
                        logger.warning(
                            f"Failed to parse JSON response: {json_err}",
                            extra=self._log_context(
                                request_id=request_id,
                                endpoint=full_path,
                                content_type=content_type,
                            ),
                        )
                        # Return text content as fallback
                        return {
                            "content": res.text,
                            "http_status": res.status_code,
                        }
                else:
                    # Non-JSON response (e.g., file download, binary data)
                    # Return content with metadata
                    json_response = {
                        "content": res.content,
                        "content_type": content_type,
                        "http_status": res.status_code,
                        "status": "success",
                    }

                # Restore original timeout if we changed it
                if endpoint_timeout:
                    self._client.timeout = original_timeout

                # Normalize keys: FortiOS returns hyphenated keys (tcp-portrange)
                # but Python/TypedDict requires underscores (tcp_portrange)
                from hfortix_core.utils import normalize_keys

                json_response = normalize_keys(json_response)

                # Return full response if raw_json=True, otherwise extract
                # results
                if raw_json:
                    return json_response
                else:
                    # Return 'results' field if present, otherwise full
                    # response
                    return json_response.get("results", json_response)

            except Exception as e:
                last_error = e

                # Special handling for 401 Unauthorized with username/password
                # auth
                # Session may have expired - try to re-authenticate once
                is_401_error = False
                if isinstance(e, httpx.HTTPStatusError):
                    is_401_error = e.response.status_code == 401

                if (
                    not self._using_token_auth
                    and not session_retry_attempted
                    and is_401_error
                    and self._username
                    and self._password
                ):
                    logger.warning(
                        "Session expired (401), attempting to re-authenticate",
                        extra={
                            "request_id": request_id,
                            "method": method.upper(),
                            "endpoint": full_path,
                        },
                    )
                    session_retry_attempted = True
                    try:
                        # Try to login again
                        self.login()
                        logger.info(
                            "Re-authentication successful, retrying request"
                        )
                        # Continue to retry the request with new session
                        continue
                    except Exception as login_error:
                        logger.error(
                            "Re-authentication failed: %s",
                            str(login_error),
                            extra={"request_id": request_id},
                        )
                        # Fall through to normal retry logic

                # Record failure in circuit breaker
                self._record_circuit_breaker_failure(endpoint_key)

                # Check if we should retry
                if self._should_retry(e, attempt, endpoint_key):
                    # Calculate delay with adaptive backpressure
                    response_obj = (
                        getattr(e, "response", None)
                        if isinstance(e, httpx.HTTPStatusError)
                        else None
                    )
                    delay = self._get_retry_delay(
                        attempt, response_obj, endpoint_key
                    )

                    # Structured log for retry
                    logger.info(
                        "Retrying request after delay",
                        extra=self._log_context(
                            request_id=request_id,
                            method=method.upper(),
                            endpoint=full_path,
                            error_type=type(e).__name__,
                            attempt=attempt + 1,
                            max_attempts=self._max_retries + 1,
                            delay_seconds=delay,
                            adaptive_retry=self._adaptive_retry,
                        ),
                    )

                    # Wait before retry
                    time.sleep(delay)
                    continue
                else:
                    # Don't retry, restore timeout and raise the error
                    if endpoint_timeout:
                        self._client.timeout = original_timeout
                    raise

        # If we've exhausted all retries, restore timeout and raise the last
        # error
        if endpoint_timeout:
            self._client.timeout = original_timeout

        if last_error:
            # Record failed request
            self._retry_stats["failed_requests"] += 1

            logger.error(
                "Request failed after all retries",
                extra=self._log_context(
                    request_id=request_id,
                    method=method.upper(),
                    endpoint=full_path,
                    total_attempts=self._max_retries + 1,
                    error_type=type(last_error).__name__,
                ),
            )

            # Audit log the failure
            duration = time.time() - start_time
            error_message = str(last_error)
            status_code = 0

            # Try to extract status code from error
            if hasattr(last_error, "response"):
                response_obj = getattr(last_error, "response", None)
                if response_obj and hasattr(response_obj, "status_code"):
                    status_code = response_obj.status_code

            self._log_audit(
                method=method,
                endpoint=full_path,
                api_type=api_type,
                path=path,
                data=data,
                params=params,
                status_code=status_code,
                success=False,
                duration_ms=int(duration * 1000),
                request_id=request_id,
                error=error_message,
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
        silent: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """GET request
        
        Args:
            api_type: API type (cmdb, monitor, etc.)
            path: Endpoint path
            params: Query parameters
            vdom: Virtual domain
            raw_json: Return raw JSON response
            silent: If True, suppress error logging (for exists() checks)
        """
        return self.request(
            "GET", api_type, path, params=params, vdom=vdom, raw_json=raw_json, silent=silent
        )

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
        path = path.lstrip("/") if isinstance(path, str) else path
        url = f"{self._url}/api/v2/{api_type}/{path}"
        params = params or {}

        # Add vdom if applicable
        if vdom is not None:
            params["vdom"] = vdom
        elif self._vdom is not None and "vdom" not in params:
            params["vdom"] = self._vdom

        # Make request
        res = self._client.get(url, params=params if params else None)

        # Build full endpoint path for error context
        full_path = f"/api/v2/{api_type}/{path}"

        # Handle errors
        self._handle_response_errors(
            res,
            endpoint=full_path,
            method="GET",
            params=params,
        )

        return res.content

    def post(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """POST request - Create new object

        Args:
            scope: Optional scope parameter for global objects
                   ('global' or 'vdom'). Required when creating
                   objects in global scope.
        """
        # Add scope to params if provided
        if scope:
            if params is None:
                params = {}
            params["scope"] = scope

        return self.request(
            "POST",
            api_type,
            path,
            data=data,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def put(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """PUT request - Update existing object

        Args:
            scope: Optional scope parameter for global objects
                   ('global' or 'vdom'). Required when updating
                   objects in global scope.
        """
        # Add scope to params if provided
        if scope:
            if params is None:
                params = {}
            params["scope"] = scope

        return self.request(
            "PUT",
            api_type,
            path,
            data=data,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """DELETE request - Delete object

        Args:
            scope: Optional scope parameter for global objects
                   ('global' or 'vdom'). Required when deleting
                   objects in global scope.
        """
        # Add scope to params if provided
        if scope:
            if params is None:
                params = {}
            params["scope"] = scope

        return self.request(
            "DELETE",
            api_type,
            path,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

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
            raise ValueError(
                f"{parameter_name} is required and cannot be None"
            )

        mkey_str = str(mkey).strip()
        if not mkey_str:
            raise ValueError(f"{parameter_name} cannot be empty")

        return mkey_str

    @staticmethod
    def validate_required_params(
        params: dict[str, Any], required: list[str]
    ) -> None:
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
                raise ValueError(
                    f"Missing required parameters: {', '.join(required)}"
                )
            return

        missing = [
            param
            for param in required
            if param not in params or params[param] is None
        ]
        if missing:
            raise ValueError(
                f"Missing required parameters: {', '.join(missing)}"
            )

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
                f"{parameter_name} must be between {min_val} and {max_val}, got {value}"  # noqa: E501
            )

    @staticmethod
    def validate_choice(
        value: Any, choices: list[Any], parameter_name: str = "value"
    ) -> None:
        """
        Validate that a value is one of the allowed choices

        Args:
            value: The value to validate
            choices: List of allowed values
            parameter_name: Name of the parameter (for error messages)

        Raises:
            ValueError: If value is not in the allowed choices

        Example:
            >>> HTTPClient.validate_choice(protocol, ['tcp', 'udp'],
            'protocol')
        """
        if value not in choices:
            raise ValueError(
                f"{parameter_name} must be one of {choices}, got '{value}'"
            )

    @staticmethod
    def build_params(**kwargs: Any) -> dict[str, Any]:
        """
        Build parameters dict, filtering out None values

        Args:
            **kwargs: Keyword arguments to build params from

        Returns:
            Dictionary with None values removed

        Example:
            >>> params = HTTPClient.build_params(format=['name'],
            datasource=True, other=None)
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
        exc_tb: Optional[Any],
    ) -> None:
        """Exit context manager - ensures session is closed"""
        self.close()

    def close(self) -> None:
        """
        Close the HTTP session and release resources

        If using username/password authentication, this will also logout
        to properly clean up the session.
        """
        # Logout if using username/password auth
        if self._session_token:
            self.logout()

        if self._client:
            self._client.close()
            logger.debug("HTTP client session closed")

    def get_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of all tracked API operations

        Returns all tracked operations (GET/POST/PUT/DELETE) in chronological
        order.
        Only available when track_operations=True was passed to constructor.

        Returns:
            List of operation dictionaries with keys:
                - timestamp: ISO 8601 timestamp
                - method: HTTP method (GET/POST/PUT/DELETE)
                - api_type: API type (cmdb/monitor/log/service)
                - path: API endpoint path
                - data: Request payload (for POST/PUT), None otherwise
                - status_code: HTTP response status code
                - vdom: Virtual domain (if specified)
                - read_only_simulated: True if operation was simulated in
                read-only mode

        Example:
            >>> client = HTTPClient(url="https://192.0.2.10", token="...",
            track_operations=True)
            >>> client.post("cmdb", "/firewall/address", {"name": "test"})
            >>> ops = client.get_operations()
            >>> print(ops[0])
            {
                'timestamp': '2024-12-20T10:30:15Z',
                'method': 'POST',
                'api_type': 'cmdb',
                'path': '/firewall/address',
                'data': {'name': 'test'},
                'status_code': 200,
                'vdom': 'root',
                'read_only_simulated': False
            }
        """
        return self._operations.copy()

    def get_write_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of write operations only (POST/PUT/DELETE)

        Filters tracked operations to return only write operations, excluding
        GET requests.

        Returns:
            List of write operation dictionaries (same format as
            get_operations())

        Example:
            >>> client = HTTPClient(url="https://192.0.2.10", token="...",
            track_operations=True)
            >>> client.get("cmdb", "/firewall/address/test")  # GET - excluded
            >>> client.post("cmdb", "/firewall/address", {"name": "test2"})  #
            POST - included
            >>> client.delete("cmdb", "/firewall/address/test")  # DELETE -
            included
            >>> write_ops = client.get_write_operations()
            >>> len(write_ops)  # Returns 2 (POST and DELETE only)
            2
        """
        return [
            op
            for op in self._operations
            if op["method"] in ("POST", "PUT", "DELETE")
        ]

    @staticmethod
    def make_exists_method(
        get_method: Callable[..., Any],
    ) -> Callable[..., bool]:
        """
        Create an exists() helper that works with both sync and async modes.

        This utility wraps a get() method and returns a function that:
        - Returns True if the object exists
        - Returns False if ResourceNotFoundError is raised
        - Returns False if response has error status (e.g., {'status': 'error'})
        - Works transparently with both sync and async clients

        Args:
            get_method: The get() method to wrap (bound method from endpoint
            instance)

        Returns:
            A function that returns bool (sync) or Coroutine[bool] (async)

        Example:
            class Address:
                def __init__(self, client):
                    self._client = client

                def get(self, name, **kwargs):
                    return self._client.get("cmdb",
                    f"/firewall/address/{name}", **kwargs)

                # Create exists method using the helper
                exists = HTTPClient.make_exists_method(get)
        """
        import inspect

        def _is_error_response(result: Any) -> bool:
            """Check if the result indicates an error (non-existent resource)."""
            if isinstance(result, dict):
                # Check for error status in response
                if result.get("status") == "error":
                    return True
                # Check for http_status indicating not found
                if result.get("http_status") == 404:
                    return True
            return False

        def exists_wrapper(*args: Any, **kwargs: Any) -> Union[bool, Any]:
            """Check if an object exists."""
            from hfortix_core.exceptions import ResourceNotFoundError

            # Call the get method
            result = get_method(*args, **kwargs)

            # Check if we got a coroutine (async mode)
            if inspect.iscoroutine(result):
                # Return async version
                async def _exists_async():
                    try:
                        # Type ignore justified: Runtime check
                        # (inspect.iscoroutine) confirms
                        # result is awaitable, but mypy sees Union[dict,
                        # Coroutine] from protocol
                        # and cannot narrow the type. This is safe and
                        # necessary for dual-mode design.
                        awaited_result = await result
                        # Check for error response
                        if _is_error_response(awaited_result):
                            return False
                        return True
                    except ResourceNotFoundError:
                        return False

                return _exists_async()
            else:
                # Sync mode - check for error response
                if _is_error_response(result):
                    return False
                # If it raised ResourceNotFoundError, we wouldn't be here
                return True

        return exists_wrapper

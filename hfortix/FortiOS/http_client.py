"""
Internal HTTP Client for FortiOS API

This module contains the HTTPClient class which handles all HTTP communication
with FortiGate devices. It is an internal implementation detail and not part
of the public API.

Now powered by httpx for better performance, HTTP/2 support, and modern async capabilities.
"""

from __future__ import annotations

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
        """
        # Normalize URL: remove trailing slashes to prevent double-slash issues
        self._url = url.rstrip('/')
        self._verify = verify
        self._vdom = vdom
        self._max_retries = max_retries
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout
        
        # Initialize httpx client with proper timeout configuration
        self._client = httpx.Client(
            timeout=httpx.Timeout(
                connect=connect_timeout,
                read=read_timeout,
                write=30.0,  # Default write timeout
                pool=10.0    # Default pool timeout
            ),
            verify=verify,
            http2=True,  # Enable HTTP/2 support
            limits=httpx.Limits(
                max_connections=100,
                max_keepalive_connections=20
            )
        )

        # Initialize retry statistics
        self._retry_stats = {
            'total_retries': 0,
            'retry_by_reason': {},
            'retry_by_endpoint': {},
        }

        # Set token if provided
        if token:
            self._client.headers["Authorization"] = f"Bearer {token}"

        logger.debug(
            "HTTP client initialized for %s (max_retries=%d, connect_timeout=%.1fs, read_timeout=%.1fs, http2=enabled)",
            self._url,
            max_retries,
            connect_timeout,
            read_timeout,
        )

    @staticmethod
    def _sanitize_data(data: Optional[dict[str, Any]]) -> dict[str, Any]:
        """
        Remove sensitive fields from data before logging (recursive)
        
        Recursively sanitizes nested dictionaries and lists to prevent
        logging sensitive information like passwords, tokens, keys, etc.
        
        Args:
            data: Data to sanitize
            
        Returns:
            Sanitized copy of data with sensitive values redacted
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
        path = path.lstrip('/') if isinstance(path, str) else path
        
        # URL encode the path, treating / and % as safe characters
        encoded_path = quote(str(path), safe='/%') if isinstance(path, str) else path
        
        return f"{self._url}/api/v2/{api_type}/{encoded_path}"

    def get_retry_stats(self) -> dict[str, Any]:
        """
        Get retry statistics
        
        Returns:
            dict: Retry statistics including:
                - total_retries: Total number of retries across all requests
                - retry_by_reason: Count of retries grouped by reason
                - retry_by_endpoint: Count of retries grouped by endpoint
        
        Example:
            >>> stats = client.get_retry_stats()
            >>> print(f"Total retries: {stats['total_retries']}")
            >>> print(f"Timeout retries: {stats['retry_by_reason'].get('Timeout', 0)}")
        """
        return {
            'total_retries': self._retry_stats['total_retries'],
            'retry_by_reason': self._retry_stats['retry_by_reason'].copy(),
            'retry_by_endpoint': self._retry_stats['retry_by_endpoint'].copy(),
        }

    def _record_retry(self, reason: str, endpoint: str) -> None:
        """
        Record retry statistics
        
        Args:
            reason: Reason for retry (e.g., 'ConnectionError', 'Timeout', 'HTTP 429')
            endpoint: Endpoint being retried
        """
        self._retry_stats['total_retries'] += 1
        
        # Track by reason
        if reason not in self._retry_stats['retry_by_reason']:
            self._retry_stats['retry_by_reason'][reason] = 0
        self._retry_stats['retry_by_reason'][reason] += 1
        
        # Track by endpoint
        if endpoint not in self._retry_stats['retry_by_endpoint']:
            self._retry_stats['retry_by_endpoint'][endpoint] = 0
        self._retry_stats['retry_by_endpoint'][endpoint] += 1

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

        Returns:
            dict: If raw_json=False, returns response['results'] (or full response if no 'results' key)
                  If raw_json=True, returns complete API response with status, http_status, etc.
        """
        # Normalize path: remove any leading slash so callers may pass
        # either 'firewall/acl' or '/firewall/acl' without causing a double-slash
        # in the constructed URL. Keep internal separators intact.
        path = path.lstrip('/') if isinstance(path, str) else path

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

        # Build full API path for logging
        full_path = f"/api/v2/{api_type}/{path}"

        # Log request (DEBUG level)
        logger.debug("→ %s %s", method.upper(), full_path)
        if params:
            logger.debug("  params: %s", params)
        if data:
            logger.debug("  data: %s", self._sanitize_data(data))

        # Track timing
        start_time = time.time()

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

                # Log response (INFO level)
                logger.info("%s %s → %d (%.3fs)", method.upper(), full_path, res.status_code, duration)

                # Warn about slow requests (WARNING level)
                if duration > 2.0:
                    logger.warning("Slow request: %s %s took %.3fs", method.upper(), full_path, duration)

                # Parse JSON response
                json_response = res.json()

                # Return full response if raw_json=True, otherwise extract results
                if raw_json:
                    return json_response
                else:
                    # Return 'results' field if present, otherwise full response
                    return json_response.get("results", json_response)

            except Exception as e:
                last_error = e

                # Check if we should retry
                if self._should_retry(e, attempt):
                    # Calculate delay
                    response_obj = getattr(e, 'response', None) if isinstance(e, httpx.HTTPStatusError) else None
                    delay = self._get_retry_delay(attempt, response_obj)

                    # Log retry
                    logger.info(
                        "Retrying %s %s after %.1fs (attempt %d/%d)",
                        method.upper(),
                        full_path,
                        delay,
                        attempt + 2,
                        self._max_retries + 1,
                    )

                    # Wait before retry
                    time.sleep(delay)
                    continue
                else:
                    # Don't retry, raise the error
                    raise

        # If we've exhausted all retries, raise the last error
        if last_error:
            logger.error(
                "Request failed after %d attempts: %s %s",
                self._max_retries + 1,
                method.upper(),
                full_path,
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

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager - ensures session is closed"""
        self.close()

    def close(self) -> None:
        """Close the HTTP session and release resources"""
        if self._client:
            self._client.close()
            logger.debug("HTTP client session closed")

"""
Internal HTTP Client for FortiOS API

This module contains the HTTPClient class which handles all HTTP communication
with FortiGate devices. It is an internal implementation detail and not part
of the public API.
"""

from __future__ import annotations

import logging
import time
from typing import Any, Optional, TypeAlias, Union
from urllib.parse import quote

import requests

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
        self._url = url
        self._verify = verify
        self._vdom = vdom
        self._max_retries = max_retries
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout
        self._session = requests.Session()
        self._session.verify = verify

        if not verify:
            import urllib3

            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Set token if provided
        if token:
            self._session.headers["Authorization"] = f"Bearer {token}"

        logger.debug(
            "HTTP client initialized for %s (max_retries=%d, connect_timeout=%.1fs, read_timeout=%.1fs)",
            url,
            max_retries,
            connect_timeout,
            read_timeout,
        )

    @staticmethod
    def _sanitize_data(data: Optional[dict[str, Any]]) -> dict[str, Any]:
        """Remove sensitive fields from data before logging"""
        if not data:
            return {}

        safe = dict(data)
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

        for key in list(safe.keys()):
            if any(s in key.lower() for s in sensitive_keys):
                safe[key] = "***REDACTED***"

        return safe

    def _handle_response_errors(self, response: requests.Response) -> None:
        """
        Handle HTTP response errors consistently using FortiOS error handling

        Args:
            response: requests.Response object

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
        if not response.ok:
            try:
                from .exceptions_forti import (get_error_description,
                                               raise_for_status)

                # Parse JSON response
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
                # If response is not JSON, raise standard HTTP error
                logger.error("Request failed: HTTP %d (non-JSON response)", response.status_code)
                response.raise_for_status()

    def request(
        self,
        method: str,
        api_type: str,
        path: str,
        data: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
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
        # URL encode the entire path, treating / as safe (path separator)
        # Note: Individual path components may already be encoded by endpoint files
        # using encode_path_component(), so we only encode other special chars here
        # Do NOT double-encode - quote with safe='/' leaves already-encoded %XX sequences alone
        url = f"{self._url}/api/v2/{api_type}/{path}"
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

        # Make request with configured timeouts
        res = self._session.request(
            method=method,
            url=url,
            json=data if data else None,
            params=params if params else None,
            timeout=(self._connect_timeout, self._read_timeout),
        )

        # Calculate duration
        duration = time.time() - start_time

        # Handle errors
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
        url = f"{self._url}/api/v2/{api_type}/{path}"
        params = params or {}

        # Add vdom if applicable
        if vdom is not None:
            params["vdom"] = vdom
        elif self._vdom is not None and "vdom" not in params:
            params["vdom"] = self._vdom

        # Make request
        res = self._session.get(url, params=params if params else None)

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

    def close(self) -> None:
        """Close the HTTP session and release resources"""
        if self._session:
            self._session.close()

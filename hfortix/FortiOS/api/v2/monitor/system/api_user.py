"""
FortiOS MONITOR - Monitor System Api User

Monitoring endpoint for monitor system api user data.

API Endpoints:
    GET    /monitor/system/api_user

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.api_user.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.api_user.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class GenerateKey:
    """
    Generatekey Operations.

    Provides read-only access for FortiOS generatekey data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize GenerateKey endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        api_user: str | None = None,
        expiry: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Generate a new api-key for the specified api-key-auth admin.

        Args:
            api_user: Generate a new token for this api-user. (optional)
            expiry: Expiry of API key in minutes from now (valid range: 1 -
            10080). This can only be set for Fortinet Support Tool user.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.api_user.generate_key.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if api_user is not None:
            data["api-user"] = api_user
        if expiry is not None:
            data["expiry"] = expiry
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/api-user/generate-key", data=data
        )


class ApiUser:
    """ApiUser operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ApiUser endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.generate_key = GenerateKey(client)

"""
FortiOS MONITOR - Monitor Wifi Ap Profile

Monitoring endpoint for monitor wifi ap profile data.

API Endpoints:
    GET    /monitor/wifi/ap_profile

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.ap_profile.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.ap_profile.get(
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


class CreateDefault:
    """
    Createdefault Operations.

    Provides read-only access for FortiOS createdefault data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CreateDefault endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        platform: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create a default FortiAP profile for the specified platform.

        Args:
            platform: FortiAP platform to create a default profile for.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.ap_profile.create_default.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if platform is not None:
            data["platform"] = platform
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/ap-profile/create-default", data=data
        )


class ApProfile:
    """ApProfile operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ApProfile endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.create_default = CreateDefault(client)

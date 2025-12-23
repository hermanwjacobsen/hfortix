"""
FortiOS MONITOR - Monitor Wifi Ap Channels

Monitoring endpoint for monitor wifi ap channels data.

API Endpoints:
    GET    /monitor/wifi/ap_channels

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.ap_channels.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.ap_channels.get(
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


class ApChannels:
    """
    Apchannels Operations.

    Provides read-only access for FortiOS apchannels data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ApChannels endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        platform_type: str,
        country: str | None = None,
        indoor_outdoor: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the set of channel lists for all possible band/configurations
        for the given FortiAP platform.

        Args:
            platform_type: Short name for platform type (e.g. '220A')
            (required)
            country: Two-letter code for the country the AP is operating in.
            (optional)
            indoor_outdoor: FortiAP indoor/outdoor configuration value (0 for
            indoor, 1 for outdoor, 2 for default). (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.ap_channels.get(platform_type='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["platform_type"] = platform_type
        if country is not None:
            params["country"] = country
        if indoor_outdoor is not None:
            params["indoor_outdoor"] = indoor_outdoor
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/ap_channels", params=params)

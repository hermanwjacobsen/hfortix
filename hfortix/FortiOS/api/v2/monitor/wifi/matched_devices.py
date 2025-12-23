"""
FortiOS MONITOR - Monitor Wifi Matched Devices

Monitoring endpoint for monitor wifi matched devices data.

API Endpoints:
    GET    /monitor/wifi/matched_devices

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.matched_devices.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.matched_devices.get(
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


class MatchedDevices:
    """
    Matcheddevices Operations.

    Provides read-only access for FortiOS matcheddevices data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize MatchedDevices endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mac: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Return a list of devices that match NAC WiFi settings.

        Args:
            mac: WiFi client MAC address. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.matched_devices.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mac is not None:
            params["mac"] = mac
        params.update(kwargs)
        return self._client.get(
            "monitor", "/wifi/matched-devices", params=params
        )

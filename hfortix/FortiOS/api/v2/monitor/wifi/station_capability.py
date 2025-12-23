"""
FortiOS MONITOR - Monitor Wifi Station Capability

Monitoring endpoint for monitor wifi station capability data.

API Endpoints:
    GET    /monitor/wifi/station_capability

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.station_capability.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.station_capability.get(
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


class StationCapability:
    """
    Stationcapability Operations.

    Provides read-only access for FortiOS stationcapability data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize StationCapability endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mac_address: str | None = None,
        min_age: int | None = None,
        max_age: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of stations and their capability to connect to detected
        access points.

        Args:
            mac_address: Station MAC address. (optional)
            min_age: Minimum value for RSSI 2G age and 5G RSSI age, in seconds.
            (optional)
            max_age: Maximum value for RSSI 2G age and 5G RSSI age, in seconds.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.station_capability.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mac_address is not None:
            params["mac_address"] = mac_address
        if min_age is not None:
            params["min_age"] = min_age
        if max_age is not None:
            params["max_age"] = max_age
        params.update(kwargs)
        return self._client.get(
            "monitor", "/wifi/station-capability", params=params
        )

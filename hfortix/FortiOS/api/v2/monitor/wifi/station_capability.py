"""Monitor API - StationCapability operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class StationCapability:
    """StationCapability operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
        """
        Retrieve a list of stations and their capability to connect to detected access points.
        
        Args:
            mac_address: Station MAC address. (optional)
            min_age: Minimum value for RSSI 2G age and 5G RSSI age, in seconds. (optional)
            max_age: Maximum value for RSSI 2G age and 5G RSSI age, in seconds. (optional)
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
            params['mac_address'] = mac_address
        if min_age is not None:
            params['min_age'] = min_age
        if max_age is not None:
            params['max_age'] = max_age
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/station-capability", params=params)

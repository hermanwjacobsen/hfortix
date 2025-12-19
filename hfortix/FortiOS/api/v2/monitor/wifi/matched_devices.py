"""Monitor API - MatchedDevices operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class MatchedDevices:
    """MatchedDevices operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
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
            params['mac'] = mac
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/matched-devices", params=params)

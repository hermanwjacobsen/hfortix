"""Monitor API - NacDevice operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Stats:
    """Stats operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Stats endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Return the current FortiSwitch matched NAC device counts and limits for the FortiGate.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.switch_controller.nac_device.stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/switch-controller/nac-device/stats", params=params)


class NacDevice:
    """NacDevice operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize NacDevice endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.stats = Stats(client)

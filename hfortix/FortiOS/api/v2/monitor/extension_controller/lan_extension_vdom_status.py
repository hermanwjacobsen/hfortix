"""Monitor API - LanExtensionVdomStatus operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LanExtensionVdomStatus:
    """LanExtensionVdomStatus operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LanExtensionVdomStatus endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve information for the FortiGate LAN Extension VDOM.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.extension_controller.lan_extension_vdom_status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/extension-controller/lan-extension-vdom-status", params=params)

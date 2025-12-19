"""Monitor API - InterfaceConnectedAdminsInfo operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InterfaceConnectedAdminsInfo:
    """InterfaceConnectedAdminsInfo operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InterfaceConnectedAdminsInfo endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        interface: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Return admins info that are connected to current interface.
        
        Args:
            interface: Interface that admins is connected through. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.interface_connected_admins_info.get(interface='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['interface'] = interface
        params.update(kwargs)
        return self._client.get("monitor", "/system/interface-connected-admins-info", params=params)

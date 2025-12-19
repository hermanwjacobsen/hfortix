"""Monitor API - Admin operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ChangeVdomMode:
    """ChangeVdomMode operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ChangeVdomMode endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        vdom_mode: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Switch between VDOM modes.
        
        Args:
            vdom_mode: VDOM mode [no-vdom|split-vdom|multi-vdom] (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.admin.change_vdom_mode.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if vdom_mode is not None:
            data['vdom-mode'] = vdom_mode
        data.update(kwargs)
        return self._client.post("monitor", "/system/admin/change-vdom-mode", data=data)


class Admin:
    """Admin operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Admin endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.change_vdom_mode = ChangeVdomMode(client)

"""Monitor API - DisconnectAdmins operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Select:
    """Select operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Select endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        id: int | None = None,
        method: str | None = None,
        admins: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Disconnects logged in administrators.
        
        Args:
            id: Admin ID (optional)
            method: Login method used to connect admin to FortiGate. (optional)
            admins: List of objects with admin id and method. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.disconnect_admins.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if id is not None:
            data['id'] = id
        if method is not None:
            data['method'] = method
        if admins is not None:
            data['admins'] = admins
        data.update(kwargs)
        return self._client.post("monitor", "/system/disconnect-admins/select", data=data)


class DisconnectAdmins:
    """DisconnectAdmins operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize DisconnectAdmins endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.select = Select(client)

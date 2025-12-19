"""Monitor API - Local operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ChangePassword:
    """ChangePassword operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ChangePassword endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        username: str | None = None,
        new_password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Change password for local user.
        
        Args:
            username: User name. (optional)
            new_password: Password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.local.change_password.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if username is not None:
            data['username'] = username
        if new_password is not None:
            data['new_password'] = new_password
        data.update(kwargs)
        return self._client.post("monitor", "/user/local/change-password", data=data)


class Local:
    """Local operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Local endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.change_password = ChangePassword(client)

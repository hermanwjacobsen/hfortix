"""Monitor API - ApProfile operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class CreateDefault:
    """CreateDefault operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CreateDefault endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        platform: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create a default FortiAP profile for the specified platform.
        
        Args:
            platform: FortiAP platform to create a default profile for. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wifi.ap_profile.create_default.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if platform is not None:
            data['platform'] = platform
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/ap-profile/create-default", data=data)


class ApProfile:
    """ApProfile operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ApProfile endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.create_default = CreateDefault(client)

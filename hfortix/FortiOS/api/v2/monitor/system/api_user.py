"""Monitor API - ApiUser operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class GenerateKey:
    """GenerateKey operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize GenerateKey endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        api_user: str | None = None,
        expiry: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Generate a new api-key for the specified api-key-auth admin.
        
        Args:
            api_user: Generate a new token for this api-user. (optional)
            expiry: Expiry of API key in minutes from now (valid range: 1 - 10080). This can only be set for Fortinet Support Tool user. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.api_user.generate_key.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if api_user is not None:
            data['api-user'] = api_user
        if expiry is not None:
            data['expiry'] = expiry
        data.update(kwargs)
        return self._client.post("monitor", "/system/api-user/generate-key", data=data)


class ApiUser:
    """ApiUser operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ApiUser endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.generate_key = GenerateKey(client)

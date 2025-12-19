"""Monitor API - Ike operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Clear:
    """Clear operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Clear endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Clear IKE gateways.
        
        Args:
            mkey: Name of the IKE gateway to clear. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.vpn.ike.clear.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data['mkey'] = mkey
        data.update(kwargs)
        return self._client.post("monitor", "/vpn/ike/clear", data=data)


class Ike:
    """Ike operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ike endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear = Clear(client)

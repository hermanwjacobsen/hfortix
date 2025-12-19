"""Monitor API - CollectedEmail operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class CollectedEmail:
    """CollectedEmail operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CollectedEmail endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List email addresses collected from captive portal.
        
        Args:
            ipv6: Include collected email from IPv6 users. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.collected_email.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ipv6 is not None:
            params['ipv6'] = ipv6
        params.update(kwargs)
        return self._client.get("monitor", "/user/collected-email", params=params)

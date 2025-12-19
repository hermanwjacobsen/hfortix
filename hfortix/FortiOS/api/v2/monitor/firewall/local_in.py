"""Monitor API - LocalIn operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LocalIn:
    """LocalIn operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LocalIn endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        include_ttl: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List implicit and explicit local-in firewall policies.
        
        Args:
            include_ttl: Include TTL local-in policies. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.local_in.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if include_ttl is not None:
            params['include_ttl'] = include_ttl
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/local-in", params=params)

"""Monitor API - ReverseIpLookup operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ReverseIpLookup:
    """ReverseIpLookup operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ReverseIpLookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ip: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve the resolved DNS domain name for a given IP address.
        
        Args:
            ip: IP address (in dot-decimal notation). (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.network.reverse_ip_lookup.get(ip='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['ip'] = ip
        params.update(kwargs)
        return self._client.get("monitor", "/network/reverse-ip-lookup", params=params)

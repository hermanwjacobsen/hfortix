"""Monitor API - Ipconf operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Ipconf:
    """Ipconf operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ipconf endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        devs: list,
        ipaddr: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Determine if there is an IP conflict for a specific IP using ARP.
        
        Args:
            devs: List of interfaces to check for conflict. (required)
            ipaddr: IPv4 address to check for conflict. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.ipconf.get(ipaddr='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['devs'] = devs
        params['ipaddr'] = ipaddr
        params.update(kwargs)
        return self._client.get("monitor", "/system/ipconf", params=params)

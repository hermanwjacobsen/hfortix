"""Monitor API - Lookup operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class HaPeer:
    """HaPeer operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize HaPeer endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        serial: str,
        destination: str,
        ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Performs a route lookup by querying the routing table of an HA peer.
        
        Args:
            serial: HA peer serial number. (required)
            destination: Destination IP/FQDN. (required)
            ipv6: Perform an IPv6 lookup. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.lookup.ha_peer.get(serial='value', destination='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['serial'] = serial
        params['destination'] = destination
        if ipv6 is not None:
            params['ipv6'] = ipv6
        params.update(kwargs)
        return self._client.get("monitor", "/router/lookup/ha-peer", params=params)


class Lookup:
    """Lookup operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Lookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.ha_peer = HaPeer(client)

    def get(
        self,
        destination: str,
        ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Performs a route lookup by querying the routing table.
        
        Args:
            destination: Destination IP/FQDN. (required)
            ipv6: Perform an IPv6 lookup. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.lookup.get(destination='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['destination'] = destination
        if ipv6 is not None:
            params['ipv6'] = ipv6
        params.update(kwargs)
        return self._client.get("monitor", "/router/lookup", params=params)

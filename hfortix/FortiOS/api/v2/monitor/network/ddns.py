"""Monitor API - Ddns operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Lookup:
    """Lookup operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Lookup endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        domain: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Check DDNS FQDN availability.
        
        Args:
            domain: Filter: domain to check. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.network.ddns.lookup.get(domain='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['domain'] = domain
        params.update(kwargs)
        return self._client.get("monitor", "/network/ddns/lookup", params=params)


class Servers:
    """Servers operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Servers endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get DDNS servers.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.network.ddns.servers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/network/ddns/servers", params=params)


class Ddns:
    """Ddns operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ddns endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.lookup = Lookup(client)
        self.servers = Servers(client)

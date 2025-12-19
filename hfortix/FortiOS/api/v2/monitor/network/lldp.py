"""Monitor API - Lldp operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Neighbors:
    """Neighbors operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Neighbors endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        port: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all active LLDP neighbors.
        
        Args:
            scope: Scope of LLDP neighbors [*vdom|global]. (optional)
            port: Filter: specific port name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.network.lldp.neighbors.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params['scope'] = scope
        if port is not None:
            params['port'] = port
        params.update(kwargs)
        return self._client.get("monitor", "/network/lldp/neighbors", params=params)


class Ports:
    """Ports operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ports endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all active LLDP ports.
        
        Args:
            mkey: Filter: specific port name. (optional)
            scope: Scope of LLDP ports [*vdom|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.network.lldp.ports.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params['mkey'] = mkey
        if scope is not None:
            params['scope'] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/network/lldp/ports", params=params)


class Lldp:
    """Lldp operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Lldp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.neighbors = Neighbors(client)
        self.ports = Ports(client)

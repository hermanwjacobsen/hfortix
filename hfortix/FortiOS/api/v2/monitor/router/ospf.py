"""Monitor API - Ospf operations."""

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
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List all discovered OSPF neighbors.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.ospf.neighbors.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/router/ospf/neighbors", params=params)


class Ospf:
    """Ospf operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Ospf endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.neighbors = Neighbors(client)

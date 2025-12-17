"""Load balance server statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class LoadBalance:
    """Load balance server statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize LoadBalance endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        virtual_server: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List all firewall load balance servers.

        Args:
            data_dict: Optional dictionary of parameters
            virtual_server: Filter by virtual server name
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing load balance server information

        Example:
            >>> fgt.api.monitor.firewall.load_balance.list()
            >>> fgt.api.monitor.firewall.load_balance.list(virtual_server='vs1')
        """
        params = data_dict.copy() if data_dict else {}
        if virtual_server is not None:
            params["virtual_server"] = virtual_server
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/load-balance", params=params)

    def get(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        virtual_server: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Get information for a specific load balance server.

        Args:
            data_dict: Optional dictionary of parameters
            virtual_server: Virtual server name to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing load balance server information

        Example:
            >>> fgt.api.monitor.firewall.load_balance.get(virtual_server='vs1')
        """
        params = data_dict.copy() if data_dict else {}
        if virtual_server is not None:
            params["virtual_server"] = virtual_server
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/load-balance", params=params)

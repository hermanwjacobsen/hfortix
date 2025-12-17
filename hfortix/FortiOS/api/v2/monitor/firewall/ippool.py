"""IPv4 pool statistics and mapping operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class IPPool:
    """IPv4 pool statistics and mappings."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize IPPool endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        List IPv4 pool statistics.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing IP pool statistics

        Example:
            >>> fgt.api.monitor.firewall.ippool.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/ippool", params=params)

    def mapping(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get the list of IPv4 mappings for the specified IP pool.

        Args:
            data_dict: Optional dictionary of parameters
            name: IP pool name (required)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing IP pool mappings

        Example:
            >>> fgt.api.monitor.firewall.ippool.mapping(name='my_pool')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/ippool/mapping", params=params)

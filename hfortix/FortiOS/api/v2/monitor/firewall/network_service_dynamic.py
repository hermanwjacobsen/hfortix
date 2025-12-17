"""Dynamic network service IP and port monitoring."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class NetworkServiceDynamic:
    """Dynamic network service IP address and port pairs."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize NetworkServiceDynamic endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List of all dynamic network service IP address and port pairs.

        Args:
            data_dict: Optional dictionary of parameters
            name: Filter by service name
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing dynamic network service information

        Example:
            >>> fgt.api.monitor.firewall.network_service_dynamic.list()
            >>> fgt.api.monitor.firewall.network_service_dynamic.list(name='my_service')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/network-service-dynamic", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get dynamic network service information for a specific service.

        Args:
            data_dict: Optional dictionary of parameters
            name: Service name to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing dynamic network service information

        Example:
            >>> fgt.api.monitor.firewall.network_service_dynamic.get(name='my_service')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/network-service-dynamic", params=params)

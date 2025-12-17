"""IPv6 Fabric Connector dynamic address monitoring."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Address6Dynamic:
    """IPv6 Fabric Connector address objects and resolved IPs."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize Address6Dynamic endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        List of all IPv6 Fabric Connector address objects and the IPs they resolve to.

        Args:
            data_dict: Optional dictionary of parameters
            name: Filter by address object name
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing IPv6 Fabric Connector address resolutions

        Example:
            >>> fgt.api.monitor.firewall.address6_dynamic.list()
            >>> fgt.api.monitor.firewall.address6_dynamic.list(name='aws_instances_v6')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/address6-dynamic", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get IPv6 Fabric Connector address resolution for a specific object.

        Args:
            data_dict: Optional dictionary of parameters
            name: Address object name to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing IPv6 Fabric Connector address resolution

        Example:
            >>> fgt.api.monitor.firewall.address6_dynamic.get(name='aws_instances_v6')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/address6-dynamic", params=params)

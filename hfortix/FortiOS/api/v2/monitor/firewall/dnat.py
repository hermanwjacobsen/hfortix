"""Virtual IP/server (DNAT) statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class DNAT:
    """Virtual IP/server statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize DNAT endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        uuid: Optional[str] = None,
        ip_version: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List hit count statistics for all firewall virtual IP/server.

        Args:
            data_dict: Optional dictionary of parameters
            name: Filter by VIP name
            uuid: Filter by UUID
            ip_version: Filter by IP version
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing VIP/server statistics

        Example:
            >>> fgt.api.monitor.firewall.dnat.list()
            >>> fgt.api.monitor.firewall.dnat.list(name='my_vip')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        if uuid is not None:
            params["uuid"] = uuid
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/dnat", params=params)

    def get(
        self, data_dict: Optional[Dict[str, Any]] = None, name: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Get hit count statistics for a specific virtual IP/server.

        Args:
            data_dict: Optional dictionary of parameters
            name: VIP name to retrieve
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing VIP/server statistics

        Example:
            >>> fgt.api.monitor.firewall.dnat.get(name='my_vip')
        """
        params = data_dict.copy() if data_dict else {}
        if name is not None:
            params["name"] = name
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/dnat", params=params)

    def reset(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Reset hit count statistics for all firewall virtual IPs/servers.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.dnat.reset()
        """
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/dnat/reset", data=data)

    def clear_counters(
        self, data_dict: Optional[Dict[str, Any]] = None, ids: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """
        Reset hit count statistics for one or more firewall virtual IP/server by ID.

        Args:
            data_dict: Optional dictionary of parameters
            ids: Comma-separated list of VIP IDs
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.dnat.clear_counters(ids='1,2,3')
        """
        data = data_dict.copy() if data_dict else {}
        if ids is not None:
            data["ids"] = ids
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/dnat/clear-counters", data=data)

"""Proxy session monitoring."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ProxySessions:
    """Proxy session monitoring."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize ProxySessions endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        srcintf: Optional[str] = None,
        dstintf: Optional[str] = None,
        srcaddr: Optional[str] = None,
        dstaddr: Optional[str] = None,
        srcport: Optional[int] = None,
        dstport: Optional[int] = None,
        protocol: Optional[str] = None,
        policyid: Optional[int] = None,
        username: Optional[str] = None,
        count: Optional[int] = None,
        start: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List all active proxy sessions.

        Args:
            data_dict: Optional dictionary of parameters
            srcintf: Filter by source interface
            dstintf: Filter by destination interface
            srcaddr: Filter by source address
            dstaddr: Filter by destination address
            srcport: Filter by source port
            dstport: Filter by destination port
            protocol: Filter by protocol
            policyid: Filter by policy ID
            username: Filter by username
            count: Maximum number of results
            start: Starting entry index
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing active proxy sessions

        Example:
            >>> fgt.api.monitor.firewall.proxy.sessions.list()
            >>> fgt.api.monitor.firewall.proxy.sessions.list(username='jdoe')
        """
        params = data_dict.copy() if data_dict else {}
        if srcintf is not None:
            params["srcintf"] = srcintf
        if dstintf is not None:
            params["dstintf"] = dstintf
        if srcaddr is not None:
            params["srcaddr"] = srcaddr
        if dstaddr is not None:
            params["dstaddr"] = dstaddr
        if srcport is not None:
            params["srcport"] = srcport
        if dstport is not None:
            params["dstport"] = dstport
        if protocol is not None:
            params["protocol"] = protocol
        if policyid is not None:
            params["policyid"] = policyid
        if username is not None:
            params["username"] = username
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/proxy/sessions", params=params)

    def get(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Get active proxy sessions with specific filters.

        This is an alias for list() that allows filtering sessions.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments (same as list())

        Returns:
            Dictionary containing filtered proxy sessions

        Example:
            >>> fgt.api.monitor.firewall.proxy.sessions.get(username='jdoe', policyid=5)
        """
        return self.list(data_dict=data_dict, **kwargs)


class Proxy:
    """Proxy monitoring sub-endpoints."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize Proxy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client
        self._sessions = ProxySessions(client)

    @property
    def sessions(self):
        """Active proxy session monitoring."""
        return self._sessions

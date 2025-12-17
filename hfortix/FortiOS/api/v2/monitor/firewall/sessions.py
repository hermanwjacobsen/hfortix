"""Firewall session monitoring and control operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Sessions:
    """Active firewall session monitoring and control."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize Sessions endpoint.

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
        srcaddr6: Optional[str] = None,
        dstaddr6: Optional[str] = None,
        srcport: Optional[int] = None,
        dstport: Optional[int] = None,
        protocol: Optional[int] = None,
        policyid: Optional[int] = None,
        username: Optional[str] = None,
        security_policyid: Optional[int] = None,
        application: Optional[str] = None,
        natsourceaddress: Optional[str] = None,
        natsourceport: Optional[int] = None,
        natdestaddress: Optional[str] = None,
        natdestport: Optional[int] = None,
        owner: Optional[str] = None,
        shaper: Optional[str] = None,
        ip_version: Optional[str] = None,
        count: Optional[int] = None,
        start: Optional[int] = None,
        seconds: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List all active firewall sessions.

        Args:
            data_dict: Optional dictionary of parameters
            srcintf: Filter by source interface
            dstintf: Filter by destination interface
            srcaddr: Filter by source address
            dstaddr: Filter by destination address
            srcaddr6: Filter by source IPv6 address
            dstaddr6: Filter by destination IPv6 address
            srcport: Filter by source port
            dstport: Filter by destination port
            protocol: Filter by protocol number
            policyid: Filter by policy ID
            username: Filter by username
            security_policyid: Filter by security policy ID
            application: Filter by application
            natsourceaddress: Filter by NAT source address
            natsourceport: Filter by NAT source port
            natdestaddress: Filter by NAT destination address
            natdestport: Filter by NAT destination port
            owner: Filter by owner
            shaper: Filter by shaper
            ip_version: Filter by IP version (ipv4/ipv6/ipboth)
            count: Maximum number of results to return
            start: Starting entry index
            seconds: Filter sessions older than this many seconds
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing active sessions

        Example:
            >>> # List all sessions
            >>> fgt.api.monitor.firewall.sessions.list()
            >>> # Filter by source address
            >>> fgt.api.monitor.firewall.sessions.list(srcaddr='10.1.1.100')
            >>> # Filter by policy ID
            >>> fgt.api.monitor.firewall.sessions.list(policyid=5)
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
        if srcaddr6 is not None:
            params["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            params["dstaddr6"] = dstaddr6
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
        if security_policyid is not None:
            params["security-policyid"] = security_policyid
        if application is not None:
            params["application"] = application
        if natsourceaddress is not None:
            params["natsourceaddress"] = natsourceaddress
        if natsourceport is not None:
            params["natsourceport"] = natsourceport
        if natdestaddress is not None:
            params["natdestaddress"] = natdestaddress
        if natdestport is not None:
            params["natdestport"] = natdestport
        if owner is not None:
            params["owner"] = owner
        if shaper is not None:
            params["shaper"] = shaper
        if ip_version is not None:
            params["ip_version"] = ip_version
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if seconds is not None:
            params["seconds"] = seconds
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/sessions", params=params)

    def get(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Get active firewall sessions with specific filters.

        This is an alias for list() that allows filtering sessions.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments (same as list())

        Returns:
            Dictionary containing filtered sessions

        Example:
            >>> fgt.api.monitor.firewall.sessions.get(srcaddr='10.1.1.100', policyid=5)
        """
        return self.list(data_dict=data_dict, **kwargs)

    def close(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        srcaddr: Optional[str] = None,
        dstaddr: Optional[str] = None,
        protocol: Optional[int] = None,
        sport: Optional[int] = None,
        dport: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Close a single firewall session that matches all provided criteria.

        Args:
            data_dict: Optional dictionary of parameters
            srcaddr: Source address
            dstaddr: Destination address
            protocol: Protocol number
            sport: Source port
            dport: Destination port
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.session.close(
            ...     srcaddr='10.1.1.100',
            ...     dstaddr='8.8.8.8',
            ...     protocol=6,
            ...     sport=45678,
            ...     dport=443
            ... )
        """
        data = data_dict.copy() if data_dict else {}
        if srcaddr is not None:
            data["srcaddr"] = srcaddr
        if dstaddr is not None:
            data["dstaddr"] = dstaddr
        if protocol is not None:
            data["protocol"] = protocol
        if sport is not None:
            data["sport"] = sport
        if dport is not None:
            data["dport"] = dport
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/session/close", data=data)

    def close_multiple(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        srcintf: Optional[str] = None,
        dstintf: Optional[str] = None,
        srcaddr: Optional[str] = None,
        dstaddr: Optional[str] = None,
        username: Optional[str] = None,
        policyid: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Close multiple IPv4 firewall sessions which match the provided criteria.

        Args:
            data_dict: Optional dictionary of parameters
            srcintf: Source interface
            dstintf: Destination interface
            srcaddr: Source address
            dstaddr: Destination address
            username: Username
            policyid: Policy ID
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.session.close_multiple(srcaddr='10.1.1.100')
        """
        data = data_dict.copy() if data_dict else {}
        if srcintf is not None:
            data["srcintf"] = srcintf
        if dstintf is not None:
            data["dstintf"] = dstintf
        if srcaddr is not None:
            data["srcaddr"] = srcaddr
        if dstaddr is not None:
            data["dstaddr"] = dstaddr
        if username is not None:
            data["username"] = username
        if policyid is not None:
            data["policyid"] = policyid
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/session/close-multiple", data=data)

    def close_multiple6(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        srcaddr6: Optional[str] = None,
        dstaddr6: Optional[str] = None,
        username: Optional[str] = None,
        policyid: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Close multiple IPv6 firewall sessions which match the provided criteria.

        Args:
            data_dict: Optional dictionary of parameters
            srcaddr6: Source IPv6 address
            dstaddr6: Destination IPv6 address
            username: Username
            policyid: Policy ID
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.session.close_multiple6(srcaddr6='2001:db8::1')
        """
        data = data_dict.copy() if data_dict else {}
        if srcaddr6 is not None:
            data["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data["dstaddr6"] = dstaddr6
        if username is not None:
            data["username"] = username
        if policyid is not None:
            data["policyid"] = policyid
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/session6/close-multiple", data=data)

    def close_all(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Immediately close all active IPv4 and IPv6 sessions, as well as IPS sessions of the current VDOM.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.sessions.close_all()
        """
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/session/close-all", data=data)

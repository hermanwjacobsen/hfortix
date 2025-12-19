"""Monitor API - Session operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Close:
    """Close operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Close endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        pro: str | None = None,
        saddr: str | None = None,
        daddr: str | None = None,
        sport: int | None = None,
        dport: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Close a single firewall session that matches all provided criteria.
        
        Args:
            pro: Protocol name [tcp|udp|icmp|...]. (optional)
            saddr: Source address. (optional)
            daddr: Destination address. (optional)
            sport: Source port. (optional)
            dport: Destination port. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.session.close.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if pro is not None:
            data['pro'] = pro
        if saddr is not None:
            data['saddr'] = saddr
        if daddr is not None:
            data['daddr'] = daddr
        if sport is not None:
            data['sport'] = sport
        if dport is not None:
            data['dport'] = dport
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/session/close", data=data)


class CloseAll:
    """CloseAll operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CloseAll endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Immediately close all active IPv4 and IPv6 sessions, as well as IPS sessions of the current VDOM.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.session.close_all.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/session/close-all", data=data)


class CloseMultiple:
    """CloseMultiple operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CloseMultiple endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        proto: str | None = None,
        saddr: str | None = None,
        daddr: str | None = None,
        sport: int | None = None,
        dport: int | None = None,
        naddr: str | None = None,
        nport: int | None = None,
        policy: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Close multiple IPv4 firewall sessions which match the provided criteria.
        
        Args:
            proto: Protocol name [tcp|udp|icmp|...] or number. (optional)
            saddr: Source address. (optional)
            daddr: Destination address. (optional)
            sport: Source port. (optional)
            dport: Destination port. (optional)
            naddr: NAT'd source IP address. (optional)
            nport: NAT'd source port. (optional)
            policy: Policy ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firewall.session.close_multiple.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if proto is not None:
            data['proto'] = proto
        if saddr is not None:
            data['saddr'] = saddr
        if daddr is not None:
            data['daddr'] = daddr
        if sport is not None:
            data['sport'] = sport
        if dport is not None:
            data['dport'] = dport
        if naddr is not None:
            data['naddr'] = naddr
        if nport is not None:
            data['nport'] = nport
        if policy is not None:
            data['policy'] = policy
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/session/close-multiple", data=data)


class Session:
    """Session operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Session endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.close = Close(client)
        self.close_all = CloseAll(client)
        self.close_multiple = CloseMultiple(client)

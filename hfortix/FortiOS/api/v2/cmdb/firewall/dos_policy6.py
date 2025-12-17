"""
FortiOS DoS Policy6 Endpoint
API endpoint for managing IPv6 DoS policies.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class DosPolicy6:
    """
    Manage IPv6 DoS (Denial of Service) policies

    This endpoint configures policies to protect against DoS attacks on IPv6 networks.
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize DoS Policy6 endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._path = "firewall/DoS-policy6"

    def list(
        self, vdom: str | None = None, raw_json: bool = False, **params: Any
    ) -> dict[str, Any]:
        """
        List all IPv6 DoS policies

        Args:
            vdom: Virtual domain name
            raw_json: If True, return raw JSON response without unwrapping
            **params: Additional query parameters

        Returns:
            API response containing list of DoS policies

        Example:
            >>> policies = fgt.cmdb.firewall.dos_policy6.list()
            >>> print(f"Total IPv6 DoS policies: {len(policies['results'])}")
        """
        return self._client.get("cmdb", self._path, vdom=vdom, params=params, raw_json=raw_json)

    def get(
        self,
        policyid: int | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """
        Get IPv6 DoS policy by ID or all policies

        Args:
            policyid: Policy ID (None to get all)
            vdom: Virtual domain name
            **params: Additional query parameters (filter, format, etc.)

        Returns:
            API response with policy details

        Example:
            >>> # Get specific policy
            >>> policy = fgt.cmdb.firewall.dos_policy6.get(policyid=1)
            >>> print(f"Policy name: {policy['results'][0]['name']}")

            >>> # Get all policies
            >>> policies = fgt.cmdb.firewall.dos_policy6.get()
        """
        if policyid is not None:
            path = f"{self._path}/{encode_path_component(str(policyid))}"
        else:
            path = self._path
        return self._client.get("cmdb", path, vdom=vdom, params=params, raw_json=raw_json)

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        policyid: Optional[int] = None,
        name: Optional[str] = None,
        interface: Optional[str | dict[str, str]] = None,
        srcaddr: Optional[list[str] | list[dict[str, str]]] = None,
        dstaddr: Optional[list[str] | list[dict[str, str]]] = None,
        service: Optional[list[str] | list[dict[str, str]]] = None,
        status: str = "enable",
        comments: str | None = None,
        anomaly: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Create IPv6 DoS policy

        Args:
            policyid: Policy ID
            name: Policy name
            interface: Incoming interface name (string) or dict with q_origin_key
            srcaddr: List of source address names or dicts [{'name': 'addr1'}]
            dstaddr: List of destination address names or dicts [{'name': 'addr1'}]
            service: List of service names or dicts [{'name': 'service1'}]
            status: Enable/disable policy ['enable'|'disable']
            comments: Policy comments
            anomaly: Anomaly detection settings (if not provided, uses FortiGate defaults)
                     List of dicts with keys: 'name', 'status', 'action', 'log', 'threshold'

                     Available anomaly types:
                     - tcp_syn_flood (default threshold: 2000)
                     - tcp_port_scan (default threshold: 1000)
                     - tcp_src_session (default threshold: 5000)
                     - tcp_dst_session (default threshold: 5000)
                     - udp_flood (default threshold: 2000)
                     - udp_scan (default threshold: 2000)
                     - udp_src_session (default threshold: 5000)
                     - udp_dst_session (default threshold: 5000)
                     - icmp_flood (default threshold: 250)
                     - icmp_sweep (default threshold: 100)
                     - icmp_src_session (default threshold: 300)
                     - icmp_dst_session (default threshold: 1000)
                     - ip_src_session (default threshold: 5000)
                     - ip_dst_session (default threshold: 5000)
                     - sctp_flood (default threshold: 2000)
                     - sctp_scan (default threshold: 1000)
                     - sctp_src_session (default threshold: 5000)
                     - sctp_dst_session (default threshold: 5000)
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> # Simple format (recommended) - uses default anomaly settings
            >>> result = fgt.cmdb.firewall.dos_policy6.create(
            ...     policyid=1,
            ...     name='dos-policy6-1',
            ...     interface='port3',
            ...     srcaddr=['all'],
            ...     dstaddr=['all'],
            ...     service=['HTTP', 'HTTPS'],
            ...     status='enable',
            ...     comments='Protect against IPv6 DoS attacks'
            ... )

            >>> # Custom anomaly detection settings
            >>> result = fgt.cmdb.firewall.dos_policy6.create(
            ...     policyid=2,
            ...     name='strict-dos-policy6',
            ...     interface='port3',
            ...     srcaddr=['all'],
            ...     dstaddr=['all'],
            ...     service=['HTTP', 'HTTPS'],
            ...     anomaly=[
            ...         {'name': 'tcp_syn_flood', 'status': 'enable', 'action': 'block', 'log': 'enable', 'threshold': 500},
            ...         {'name': 'udp_flood', 'status': 'enable', 'action': 'block', 'log': 'enable', 'threshold': 1000},
            ...         {'name': 'icmp_flood', 'status': 'enable', 'action': 'block', 'log': 'enable', 'threshold': 100}
            ...     ]
            ... )

            >>> # Dict format also supported
            >>> result = fgt.cmdb.firewall.dos_policy6.create(
            ...     policyid=1,
            ...     name='dos-policy6-1',
            ...     interface={'q_origin_key': 'port3'},
            ...     srcaddr=[{'name': 'all'}],
            ...     dstaddr=[{'name': 'all'}],
            ...     service=[{'name': 'ALL'}]
            ... )
        """
        # Support both patterns: data dict or individual kwargs
        if payload_dict is not None:
            # Pattern 1: data dict provided
            payload = payload_dict.copy()
        else:
            # Pattern 2: build from kwargs
            # Convert interface to dict format if string provided
            if interface is not None:
                if isinstance(interface, str):
                    interface_data = {"q_origin_key": interface}
                else:
                    interface_data = interface
            else:
                interface_data = None

            # Convert address lists to dict format if strings provided
            srcaddr_data = None
            if srcaddr is not None:
                srcaddr_data = [
                    {"name": addr} if isinstance(addr, str) else addr for addr in srcaddr
                ]

            dstaddr_data = None
            if dstaddr is not None:
                dstaddr_data = [
                    {"name": addr} if isinstance(addr, str) else addr for addr in dstaddr
                ]

            service_data = None
            if service is not None:
                service_data = [{"name": svc} if isinstance(svc, str) else svc for svc in service]

            payload: Dict[str, Any] = {}
            if policyid is not None:
                payload["policyid"] = policyid
            if name is not None:
                payload["name"] = name
            if interface_data is not None:
                payload["interface"] = interface_data
            if srcaddr_data is not None:
                payload["srcaddr"] = srcaddr_data
            if dstaddr_data is not None:
                payload["dstaddr"] = dstaddr_data
            if service_data is not None:
                payload["service"] = service_data
            if status is not None:
                payload["status"] = status
            if comments is not None:
                payload["comments"] = comments
            if anomaly is not None:
                payload["anomaly"] = anomaly

        return self._client.post("cmdb", self._path, data=payload, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        policyid: Optional[int] = None,
        name: Optional[str] = None,
        interface: str | None = None,
        srcaddr: list[dict[str, str]] | None = None,
        dstaddr: list[dict[str, str]] | None = None,
        service: list[dict[str, str]] | None = None,
        status: str | None = None,
        comments: str | None = None,
        anomaly: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Update IPv6 DoS policy

        Args:
            policyid: Policy ID to update
            name: Policy name
            interface: Incoming interface name
            srcaddr: List of IPv6 source addresses
            dstaddr: List of IPv6 destination addresses
            service: List of services
            status: Enable/disable policy
            comments: Policy comments
            anomaly: Anomaly detection settings
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> result = fgt.cmdb.firewall.dos_policy6.update(
            ...     policyid=1,
            ...     status='disable',
            ...     comments='Temporarily disabled'
            ... )
        """
        # Support both patterns: data dict or individual kwargs
        if payload_dict is not None:
            # Pattern 1: data dict provided
            payload = payload_dict.copy()
            # Extract policyid from data if not provided as param
            if policyid is None:
                policyid = payload.get("policyid")
        else:
            # Pattern 2: build from kwargs
            payload: Dict[str, Any] = {}

            if name is not None:
                payload["name"] = name
            if interface is not None:
                payload["interface"] = interface
            if srcaddr is not None:
                payload["srcaddr"] = srcaddr
            if dstaddr is not None:
                payload["dstaddr"] = dstaddr
            if service is not None:
                payload["service"] = service
            if status is not None:
                payload["status"] = status
            if comments is not None:
                payload["comments"] = comments
            if anomaly is not None:
                payload["anomaly"] = anomaly

        path = f"{self._path}/{encode_path_component(str(policyid))}"
        return self._client.put("cmdb", path, data=payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        policyid: int,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete IPv6 DoS policy

        Args:
            policyid: Policy ID to delete
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> result = fgt.cmdb.firewall.dos_policy6.delete(policyid=1)
        """
        path = f"{self._path}/{encode_path_component(str(policyid))}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, policyid: int, vdom: str | None = None) -> bool:
        """
        Check if IPv6 DoS policy exists

        Args:
            policyid: Policy ID to check
            vdom: Virtual domain name

        Returns:
            True if policy exists, False otherwise

        Example:
            >>> if fgt.cmdb.firewall.dos_policy6.exists(policyid=1):
            ...     print("IPv6 DoS policy exists")
        """
        try:
            result = self.get(policyid=policyid, vdom=vdom, raw_json=True)
            return result.get("status") == "success" and len(result.get("results", [])) > 0
        except Exception:
            return False

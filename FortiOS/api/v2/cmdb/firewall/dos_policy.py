"""
FortiOS DoS Policy Endpoint
API endpoint for managing IPv4 DoS policies.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class DosPolicy:
    """
    Manage IPv4 DoS (Denial of Service) policies
    
    This endpoint configures policies to protect against DoS attacks.
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize DoS Policy endpoint
        
        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._path = 'firewall/DoS-policy'

    def list(self, vdom: str | None = None, **params: Any) -> dict[str, Any]:
        """
        List all IPv4 DoS policies
        
        Args:
            vdom: Virtual domain name
            **params: Additional query parameters
        
        Returns:
            API response containing list of DoS policies
            
        Example:
            >>> policies = fgt.cmdb.firewall.dos_policy.list()
            >>> print(f"Total policies: {len(policies['results'])}")
        """
        return self._client.cmdb._get(self._path, vdom=vdom, params=params)

    def get(self, policyid: int | None = None, vdom: str | None = None, **params: Any) -> dict[str, Any]:
        """
        Get IPv4 DoS policy by ID or all policies
        
        Args:
            policyid: Policy ID (None to get all)
            vdom: Virtual domain name
            **params: Additional query parameters (filter, format, etc.)
        
        Returns:
            API response with policy details
            
        Example:
            >>> # Get specific policy
            >>> policy = fgt.cmdb.firewall.dos_policy.get(policyid=1)
            >>> print(f"Policy name: {policy['results'][0]['name']}")
            
            >>> # Get all policies
            >>> policies = fgt.cmdb.firewall.dos_policy.get()
        """
        if policyid is not None:
            path = f'{self._path}/{policyid}'
        else:
            path = self._path
        return self._client.cmdb._get(path, vdom=vdom, params=params)

    def create(
        self,
        policyid: int,
        name: str,
        interface: str | dict[str, str],
        srcaddr: list[str] | list[dict[str, str]],
        dstaddr: list[str] | list[dict[str, str]],
        service: list[str] | list[dict[str, str]],
        status: str = 'enable',
        comments: str | None = None,
        anomaly: list[dict[str, Any]] | None = None,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Create new IPv4 DoS policy
        
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
            >>> result = fgt.cmdb.firewall.dos_policy.create(
            ...     policyid=1,
            ...     name='dos-policy-1',
            ...     interface='port3',
            ...     srcaddr=['all'],
            ...     dstaddr=['all'],
            ...     service=['HTTP', 'HTTPS'],
            ...     status='enable',
            ...     comments='Protect against DoS attacks'
            ... )
            
            >>> # Custom anomaly detection settings
            >>> result = fgt.cmdb.firewall.dos_policy.create(
            ...     policyid=2,
            ...     name='strict-dos-policy',
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
            >>> result = fgt.cmdb.firewall.dos_policy.create(
            ...     policyid=1,
            ...     name='dos-policy-1',
            ...     interface={'q_origin_key': 'port3'},
            ...     srcaddr=[{'name': 'all'}],
            ...     dstaddr=[{'name': 'all'}],
            ...     service=[{'name': 'ALL'}]
            ... )
        """
        # Convert interface to dict format if string provided
        if isinstance(interface, str):
            interface_data = {'q_origin_key': interface}
        else:
            interface_data = interface
        
        # Convert address lists to dict format if strings provided
        srcaddr_data = [{'name': addr} if isinstance(addr, str) else addr for addr in srcaddr]
        dstaddr_data = [{'name': addr} if isinstance(addr, str) else addr for addr in dstaddr]
        service_data = [{'name': svc} if isinstance(svc, str) else svc for svc in service]
        
        data: dict[str, Any] = {
            'policyid': policyid,
            'name': name,
            'interface': interface_data,
            'srcaddr': srcaddr_data,
            'dstaddr': dstaddr_data,
            'service': service_data,
            'status': status
        }
        
        if comments is not None:
            data['comments'] = comments
        if anomaly is not None:
            data['anomaly'] = anomaly
            
        return self._client.cmdb._post(self._path, data=data, vdom=vdom)

    def update(
        self,
        policyid: int,
        name: str | None = None,
        interface: str | None = None,
        srcaddr: list[dict[str, str]] | None = None,
        dstaddr: list[dict[str, str]] | None = None,
        service: list[dict[str, str]] | None = None,
        status: str | None = None,
        comments: str | None = None,
        anomaly: list[dict[str, Any]] | None = None,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Update existing IPv4 DoS policy
        
        Args:
            policyid: Policy ID to update
            name: Policy name
            interface: Incoming interface name
            srcaddr: List of source addresses
            dstaddr: List of destination addresses
            service: List of services
            status: Enable/disable policy
            comments: Policy comments
            anomaly: Anomaly detection settings
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> result = fgt.cmdb.firewall.dos_policy.update(
            ...     policyid=1,
            ...     status='disable',
            ...     comments='Temporarily disabled'
            ... )
        """
        data: dict[str, Any] = {}
        
        if name is not None:
            data['name'] = name
        if interface is not None:
            data['interface'] = interface
        if srcaddr is not None:
            data['srcaddr'] = srcaddr
        if dstaddr is not None:
            data['dstaddr'] = dstaddr
        if service is not None:
            data['service'] = service
        if status is not None:
            data['status'] = status
        if comments is not None:
            data['comments'] = comments
        if anomaly is not None:
            data['anomaly'] = anomaly
            
        path = f'{self._path}/{policyid}'
        return self._client.cmdb._put(path, data=data, vdom=vdom)

    def delete(self, policyid: int, vdom: str | None = None) -> dict[str, Any]:
        """
        Delete IPv4 DoS policy
        
        Args:
            policyid: Policy ID to delete
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> result = fgt.cmdb.firewall.dos_policy.delete(policyid=1)
        """
        path = f'{self._path}/{policyid}'
        return self._client.cmdb._delete(path, vdom=vdom)

    def exists(self, policyid: int, vdom: str | None = None) -> bool:
        """
        Check if IPv4 DoS policy exists
        
        Args:
            policyid: Policy ID to check
            vdom: Virtual domain name
        
        Returns:
            True if policy exists, False otherwise
            
        Example:
            >>> if fgt.cmdb.firewall.dos_policy.exists(policyid=1):
            ...     print("Policy exists")
        """
        try:
            result = self.get(policyid=policyid, vdom=vdom)
            return result.get('status') == 'success' and len(result.get('results', [])) > 0
        except Exception:
            return False

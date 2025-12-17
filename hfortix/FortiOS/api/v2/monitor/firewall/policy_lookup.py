"""Policy lookup operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class PolicyLookup:
    """Policy lookup by creating dummy packet."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize PolicyLookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def __call__(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        srcintf: Optional[str] = None,
        ipv6: Optional[bool] = None,
        protocol: Optional[int] = None,
        sourceip: Optional[str] = None,
        dest: Optional[str] = None,
        sourceport: Optional[int] = None,
        dest_port: Optional[int] = None,
        icmptype: Optional[int] = None,
        icmpcode: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Performs a policy lookup by creating a dummy packet and asking the kernel which policy would be hit.

        Args:
            data_dict: Optional dictionary of parameters
            srcintf: Source interface name (required)
            ipv6: Whether lookup is for IPv6 (required)
            protocol: Protocol number (required)
            sourceip: Source IP address (required)
            dest: Destination IP address (required)
            sourceport: Source port (required)
            dest_port: Destination port (required)
            icmptype: ICMP type (for ICMP protocol)
            icmpcode: ICMP code (for ICMP protocol)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing matched policy information

        Example:
            >>> fgt.api.monitor.firewall.policy_lookup(
            ...     srcintf='port1',
            ...     ipv6=False,
            ...     protocol=6,
            ...     sourceip='10.1.1.100',
            ...     dest='8.8.8.8',
            ...     sourceport=45678,
            ...     dest_port=443
            ... )
        """
        params = data_dict.copy() if data_dict else {}
        if srcintf is not None:
            params["srcintf"] = srcintf
        if ipv6 is not None:
            params["ipv6"] = ipv6
        if protocol is not None:
            params["protocol"] = protocol
        if sourceip is not None:
            params["sourceip"] = sourceip
        if dest is not None:
            params["dest"] = dest
        if sourceport is not None:
            params["sourceport"] = sourceport
        if dest_port is not None:
            params["dest_port"] = dest_port
        if icmptype is not None:
            params["icmptype"] = icmptype
        if icmpcode is not None:
            params["icmpcode"] = icmpcode
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/policy-lookup", params=params)

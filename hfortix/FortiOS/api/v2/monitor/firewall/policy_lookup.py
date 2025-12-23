"""
FortiOS MONITOR - Monitor Firewall Policy Lookup

Monitoring endpoint for monitor firewall policy lookup data.

API Endpoints:
    GET    /monitor/firewall/policy_lookup

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.policy_lookup.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.policy_lookup.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class PolicyLookup:
    """
    Policylookup Operations.

    Provides read-only access for FortiOS policylookup data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PolicyLookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        srcintf: str,
        sourceip: str,
        protocol: str,
        dest: str,
        ipv6: bool | None = None,
        sourceport: int | None = None,
        destport: int | None = None,
        icmptype: int | None = None,
        icmpcode: int | None = None,
        policy_type: str | None = None,
        auth_type: str | None = None,
        user_group: Any | None = None,
        server_name: str | None = None,
        user_db: str | None = None,
        group_attr_type: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Performs a policy lookup by creating a dummy packet and asking the
        kernel which policy would be hit.

        Args:
            srcintf: Source interface. (required)
            sourceip: Source IP. (required)
            protocol: Protocol. (required)
            dest: Destination IP/FQDN. (required)
            ipv6: Perform an IPv6 lookup? (optional)
            sourceport: Source port. (optional)
            destport: Destination port. (optional)
            icmptype: ICMP type. (optional)
            icmpcode: ICMP code. (optional)
            policy_type: Policy type. [*policy | proxy] (optional)
            auth_type: Authentication type. [user | group | saml | ldap] Note:
            this only works for models that can guarantee WAD workers
            availability, i.e. those that do not disable proxy features
            globally. (optional)
            user_group: Name of local user. Note: this only works for models
            that can guarantee WAD workers availability, i.e. those that do not
            disable proxy features globally. (optional)
            server_name: Remote user/group server name. Note: this only works
            for models that can guarantee WAD workers availability, i.e. those
            that do not disable proxy features globally. (optional)
            user_db: Authentication server to contain user information.
            (optional)
            group_attr_type: Remote user group attribute type. [*name | id]
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.policy_lookup.get(srcintf='value',
            sourceip='value', protocol='value', dest='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["srcint"] = srcintf
        params["sourceip"] = sourceip
        params["protocol"] = protocol
        params["dest"] = dest
        if ipv6 is not None:
            params["ipv6"] = ipv6
        if sourceport is not None:
            params["sourceport"] = sourceport
        if destport is not None:
            params["destport"] = destport
        if icmptype is not None:
            params["icmptype"] = icmptype
        if icmpcode is not None:
            params["icmpcode"] = icmpcode
        if policy_type is not None:
            params["policy_type"] = policy_type
        if auth_type is not None:
            params["auth_type"] = auth_type
        if user_group is not None:
            params["user_group"] = user_group
        if server_name is not None:
            params["server_name"] = server_name
        if user_db is not None:
            params["user_db"] = user_db
        if group_attr_type is not None:
            params["group_attr_type"] = group_attr_type
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/policy-lookup", params=params
        )

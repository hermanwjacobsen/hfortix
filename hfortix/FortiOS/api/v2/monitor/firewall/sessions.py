"""
FortiOS MONITOR - Monitor Firewall Sessions

Monitoring endpoint for monitor firewall sessions data.

API Endpoints:
    GET    /monitor/firewall/sessions

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.sessions.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.sessions.get(
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


class Sessions:
    """
    Sessions Operations.

    Provides read-only access for FortiOS sessions data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Sessions endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        count: int,
        ip_version: str | None = None,
        summary: bool | None = None,
        srcport: str | None = None,
        policyid: str | None = None,
        security_policyid: str | None = None,
        application: str | None = None,
        protocol: str | None = None,
        dstport: str | None = None,
        srcintf: str | None = None,
        dstintf: str | None = None,
        srcintfrole: list | None = None,
        dstintfrole: list | None = None,
        srcaddr: str | None = None,
        srcaddr6: str | None = None,
        srcuuid: str | None = None,
        dstaddr: str | None = None,
        dstaddr6: str | None = None,
        dstuuid: str | None = None,
        username: str | None = None,
        shaper: str | None = None,
        country: str | None = None,
        owner: str | None = None,
        natsourceaddress: str | None = None,
        natsourceport: str | None = None,
        since: str | None = None,
        seconds: str | None = None,
        fortiasic: str | None = None,
        nturbo: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all active firewall sessions (optionally filtered).

        Args:
            count: Maximum number of entries to return. Valid range is [20,
            1000]; if a value is specified out of that range, it will be
            rounded up or down. (required)
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            summary: Enable/disable inclusion of session summary (setup rate,
            total sessions, etc). (optional)
            srcport: Source port. (optional)
            policyid: Policy ID. (optional)
            security_policyid: Filter: Security Policy ID. (optional)
            application: Application ID, or application PROTO/PORT pair. (e.g.
            "TCP/443") (optional)
            protocol: Protocol name [all|igmp|tcp|udp|icmp|etc]. (optional)
            dstport: Destination port. (optional)
            srcintf: Source interface name. (optional)
            dstintf: Destination interface name. (optional)
            srcintfrole: Source interface roles. (optional)
            dstintfrole: Filter: Destination interface roles. (optional)
            srcaddr: Source IPv4 address. (optional)
            srcaddr6: Source IPv6 address. (optional)
            srcuuid: Source UUID. (optional)
            dstaddr: Destination IPv4 address. (optional)
            dstaddr6: Destination IPv6 address. (optional)
            dstuuid: Destination UUID. (optional)
            username: Authenticated username. (optional)
            shaper: Forward traffic shaper name. (optional)
            country: Destination country name. (optional)
            owner: Destination owner. (optional)
            natsourceaddress: NAT source address. (optional)
            natsourceport: NAT source port. (optional)
            since: Only return sessions generated since this Unix timestamp.
            (optional)
            seconds: Only return sessions generated in the last N seconds.
            (optional)
            fortiasic: "true" to show NPU accelerated sessions only, false to
            exclude. (optional)
            nturbo: "true" to include nTurbo sessions, false to exclude.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.sessions.get(count=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["count"] = count
        if ip_version is not None:
            params["ip_version"] = ip_version
        if summary is not None:
            params["summary"] = summary
        if srcport is not None:
            params["srcport"] = srcport
        if policyid is not None:
            params["policyid"] = policyid
        if security_policyid is not None:
            params["security-policyid"] = security_policyid
        if application is not None:
            params["application"] = application
        if protocol is not None:
            params["protocol"] = protocol
        if dstport is not None:
            params["dstport"] = dstport
        if srcintf is not None:
            params["srcint"] = srcintf
        if dstintf is not None:
            params["dstint"] = dstintf
        if srcintfrole is not None:
            params["srcintfrole"] = srcintfrole
        if dstintfrole is not None:
            params["dstintfrole"] = dstintfrole
        if srcaddr is not None:
            params["srcaddr"] = srcaddr
        if srcaddr6 is not None:
            params["srcaddr6"] = srcaddr6
        if srcuuid is not None:
            params["srcuuid"] = srcuuid
        if dstaddr is not None:
            params["dstaddr"] = dstaddr
        if dstaddr6 is not None:
            params["dstaddr6"] = dstaddr6
        if dstuuid is not None:
            params["dstuuid"] = dstuuid
        if username is not None:
            params["username"] = username
        if shaper is not None:
            params["shaper"] = shaper
        if country is not None:
            params["country"] = country
        if owner is not None:
            params["owner"] = owner
        if natsourceaddress is not None:
            params["natsourceaddress"] = natsourceaddress
        if natsourceport is not None:
            params["natsourceport"] = natsourceport
        if since is not None:
            params["since"] = since
        if seconds is not None:
            params["seconds"] = seconds
        if fortiasic is not None:
            params["fortiasic"] = fortiasic
        if nturbo is not None:
            params["nturbo"] = nturbo
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/sessions", params=params)

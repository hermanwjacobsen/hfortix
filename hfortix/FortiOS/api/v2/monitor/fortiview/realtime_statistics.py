"""
FortiOS MONITOR - Monitor Fortiview Realtime Statistics

Monitoring endpoint for monitor fortiview realtime statistics data.

API Endpoints:
    GET    /monitor/fortiview/realtime_statistics

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.fortiview.realtime_statistics.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.fortiview.realtime_statistics.get(
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


class RealtimeStatistics:
    """
    Realtimestatistics Operations.

    Provides read-only access for FortiOS realtimestatistics data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize RealtimeStatistics endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        srcaddr: str | None = None,
        dstaddr: str | None = None,
        srcaddr6: str | None = None,
        dstaddr6: str | None = None,
        srcport: str | None = None,
        dstport: str | None = None,
        srcintf: str | None = None,
        srcintfrole: list | None = None,
        dstintf: str | None = None,
        dstintfrole: list | None = None,
        policyid: str | None = None,
        security_policyid: str | None = None,
        protocol: str | None = None,
        web_category: str | None = None,
        web_domain: str | None = None,
        application: str | None = None,
        country: str | None = None,
        seconds: str | None = None,
        since: str | None = None,
        owner: str | None = None,
        username: str | None = None,
        shaper: str | None = None,
        srcuuid: str | None = None,
        dstuuid: str | None = None,
        sessionid: int | None = None,
        report_by: str | None = None,
        sort_by: str | None = None,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve realtime drill-down and summary data for FortiView.

        Args:
            srcaddr: Source IPv4 address. (optional)
            dstaddr: Destination IPv4 address. (optional)
            srcaddr6: Source IPv6 address. (optional)
            dstaddr6: Destination IPv6 address. (optional)
            srcport: Source TCP port number. (optional)
            dstport: Destination TCP port number. (optional)
            srcintf: Source interface name. (optional)
            srcintfrole: Source interface role name. (optional)
            dstintf: Destination interface name. (optional)
            dstintfrole: Destination interface role name. (optional)
            policyid: Firewall policy ID. (optional)
            security_policyid: NGFW policy ID. (optional)
            protocol: Protocol type. (optional)
            web_category: Web category ID. (optional)
            web_domain: Web domain name. (optional)
            application: Web application type. It can be ID, or protocol/port
            pair. (optional)
            country: Geographic location. (optional)
            seconds: Time in seconds, since the session is established.
            (optional)
            since: Time when the session is established. (optional)
            owner: Owner. (optional)
            username: Session login user name. (optional)
            shaper: Traffic shaper name. (optional)
            srcuuid: UUID of source. (optional)
            dstuuid: UUID of destination. (optional)
            sessionid: FortiView request Session ID. (optional)
            report_by: Report by field. (optional)
            sort_by: Sort by field. (optional)
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.fortiview.realtime_statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
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
        if srcintf is not None:
            params["srcint"] = srcintf
        if srcintfrole is not None:
            params["srcintfrole"] = srcintfrole
        if dstintf is not None:
            params["dstint"] = dstintf
        if dstintfrole is not None:
            params["dstintfrole"] = dstintfrole
        if policyid is not None:
            params["policyid"] = policyid
        if security_policyid is not None:
            params["security-policyid"] = security_policyid
        if protocol is not None:
            params["protocol"] = protocol
        if web_category is not None:
            params["web-category"] = web_category
        if web_domain is not None:
            params["web-domain"] = web_domain
        if application is not None:
            params["application"] = application
        if country is not None:
            params["country"] = country
        if seconds is not None:
            params["seconds"] = seconds
        if since is not None:
            params["since"] = since
        if owner is not None:
            params["owner"] = owner
        if username is not None:
            params["username"] = username
        if shaper is not None:
            params["shaper"] = shaper
        if srcuuid is not None:
            params["srcuuid"] = srcuuid
        if dstuuid is not None:
            params["dstuuid"] = dstuuid
        if sessionid is not None:
            params["sessionid"] = sessionid
        if report_by is not None:
            params["report_by"] = report_by
        if sort_by is not None:
            params["sort_by"] = sort_by
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get(
            "monitor", "/fortiview/realtime-statistics", params=params
        )

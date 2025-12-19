"""Monitor API - RealtimeProxyStatistics operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class RealtimeProxyStatistics:
    """RealtimeProxyStatistics operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize RealtimeProxyStatistics endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        report_by: str | None = None,
        sort_by: str | None = None,
        ip_version: str | None = None,
        srcaddr: str | None = None,
        dstaddr: str | None = None,
        srcaddr6: str | None = None,
        dstaddr6: str | None = None,
        srcport: str | None = None,
        dstport: str | None = None,
        srcintf: str | None = None,
        dstintf: str | None = None,
        policyid: str | None = None,
        proxy_policyid: str | None = None,
        protocol: str | None = None,
        application: str | None = None,
        country: str | None = None,
        seconds: str | None = None,
        since: str | None = None,
        owner: str | None = None,
        username: str | None = None,
        srcuuid: str | None = None,
        dstuuid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve realtime drill-down and summary data for proxy session FortiView statistics.
        
        Args:
            report_by: Report by field. (optional)
            sort_by: Sort by field. (optional)
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            srcaddr: Source IPv4 address. (optional)
            dstaddr: Destination IPv4 address. (optional)
            srcaddr6: Source IPv6 address. (optional)
            dstaddr6: Destination IPv6 address. (optional)
            srcport: Source TCP port number. (optional)
            dstport: Destination TCP port number. (optional)
            srcintf: Source interface name. (optional)
            dstintf: Destination interface name. (optional)
            policyid: Firewall policy ID. (optional)
            proxy_policyid: Explicit proxy policy ID. (optional)
            protocol: Protocol type. (optional)
            application: Web application type. (optional)
            country: Geographic location. (optional)
            seconds: Time in seconds, since the session is established. (optional)
            since: Time when the session is established. (optional)
            owner: Owner. (optional)
            username: Session login user name. (optional)
            srcuuid: UUID of source. (optional)
            dstuuid: UUID of destination. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.fortiview.realtime_proxy_statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if report_by is not None:
            params['report_by'] = report_by
        if sort_by is not None:
            params['sort_by'] = sort_by
        if ip_version is not None:
            params['ip_version'] = ip_version
        if srcaddr is not None:
            params['srcaddr'] = srcaddr
        if dstaddr is not None:
            params['dstaddr'] = dstaddr
        if srcaddr6 is not None:
            params['srcaddr6'] = srcaddr6
        if dstaddr6 is not None:
            params['dstaddr6'] = dstaddr6
        if srcport is not None:
            params['srcport'] = srcport
        if dstport is not None:
            params['dstport'] = dstport
        if srcintf is not None:
            params['srcintf'] = srcintf
        if dstintf is not None:
            params['dstintf'] = dstintf
        if policyid is not None:
            params['policyid'] = policyid
        if proxy_policyid is not None:
            params['proxy-policyid'] = proxy_policyid
        if protocol is not None:
            params['protocol'] = protocol
        if application is not None:
            params['application'] = application
        if country is not None:
            params['country'] = country
        if seconds is not None:
            params['seconds'] = seconds
        if since is not None:
            params['since'] = since
        if owner is not None:
            params['owner'] = owner
        if username is not None:
            params['username'] = username
        if srcuuid is not None:
            params['srcuuid'] = srcuuid
        if dstuuid is not None:
            params['dstuuid'] = dstuuid
        params.update(kwargs)
        return self._client.get("monitor", "/fortiview/realtime-proxy-statistics", params=params)

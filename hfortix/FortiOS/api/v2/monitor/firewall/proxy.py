"""
FortiOS MONITOR - Monitor Firewall Proxy

Monitoring endpoint for monitor firewall proxy data.

API Endpoints:
    GET    /monitor/firewall/proxy

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.proxy.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.proxy.get(
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
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        count: int,
        ip_version: str | None = None,
        summary: bool | None = None,
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
        src_uuid: str | None = None,
        dst_uuid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all active proxy sessions (optionally filtered).

        Args:
            count: Maximum number of entries to return. Valid range is [20,
            1000]; if a value is specified out of that range, it will be
            rounded up or down. (required)
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            summary: Enable/disable inclusion of session summary (setup rate,
            total sessions, etc). (optional)
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
            seconds: Time in seconds, since the session is established.
            (optional)
            since: Time when the session is established. (optional)
            owner: Owner. (optional)
            username: Session login user name. (optional)
            src_uuid: UUID of source. (optional)
            dst_uuid: UUID of destination. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.proxy.sessions.get(count=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["count"] = count
        if ip_version is not None:
            params["ip_version"] = ip_version
        if summary is not None:
            params["summary"] = summary
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
        if dstintf is not None:
            params["dstint"] = dstintf
        if policyid is not None:
            params["policyid"] = policyid
        if proxy_policyid is not None:
            params["proxy-policyid"] = proxy_policyid
        if protocol is not None:
            params["protocol"] = protocol
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
        if src_uuid is not None:
            params["src_uuid"] = src_uuid
        if dst_uuid is not None:
            params["dst_uuid"] = dst_uuid
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/proxy/sessions", params=params
        )


class Proxy:
    """Proxy operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Proxy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.sessions = Sessions(client)

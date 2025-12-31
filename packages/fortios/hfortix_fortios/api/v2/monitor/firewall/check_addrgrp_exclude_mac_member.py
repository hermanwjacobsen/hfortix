"""
FortiOS MONITOR - Monitor Firewall Check Addrgrp Exclude Mac Member

Monitoring endpoint for monitor firewall check addrgrp exclude mac member data.

API Endpoints:
    GET    /monitor/firewall/check_addrgrp_exclude_mac_member

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.check_addrgrp_exclude_mac_member.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.check_addrgrp_exclude_mac_member.get(
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

    from hfortix_core.http.interface import IHTTPClient

__all__ = ["CheckAddrgrpExcludeMacMember"]


class CheckAddrgrpExcludeMacMember:
    """
    Checkaddrgrpexcludemacmember Operations.

    Provides read-only access for FortiOS checkaddrgrpexcludemacmember data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CheckAddrgrpExcludeMacMember endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mkey: str,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Check if the IPv4 or IPv6 address group should exclude mac address type
        member.

        Args:
            mkey: The address group name to be checked. (required)
            ip_version: IP version [ipv4 | ipv6]. Specify the IP version of the
            address / address group. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.firewall.check_addrgrp_exclude_mac_member.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/firewall/check-addrgrp-exclude-mac-member",
            params=params,
        )

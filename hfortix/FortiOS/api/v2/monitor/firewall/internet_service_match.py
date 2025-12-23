"""
FortiOS MONITOR - Monitor Firewall Internet Service Match

Monitoring endpoint for monitor firewall internet service match data.

API Endpoints:
    GET    /monitor/firewall/internet_service_match

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.internet_service_match.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.internet_service_match.get(
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


class InternetServiceMatch:
    """
    Internetservicematch Operations.

    Provides read-only access for FortiOS internetservicematch data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize InternetServiceMatch endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ip: str,
        is_ipv6: bool | None = None,
        ipv4_mask: str | None = None,
        ipv6_prefix: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List internet services that exist at a given IP or Subnet.

        Args:
            ip: IP (in dot-decimal notation). (required)
            is_ipv6: Whether IP is IPv6. If not provided, will determine IP
            version based on given IP, but setting is_ipv6 flag is recommended.
            (optional)
            ipv4_mask: IPv4 address mask (in dot-decimal notation). Required if
            is_ipv6 is false. Example: 255.255.255.255 (optional)
            ipv6_prefix: IPv6 address prefix. Required if is_ipv6 is true.
            Example: 128 (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.internet_service_match.get(ip='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["ip"] = ip
        if is_ipv6 is not None:
            params["is_ipv6"] = is_ipv6
        if ipv4_mask is not None:
            params["ipv4_mask"] = ipv4_mask
        if ipv6_prefix is not None:
            params["ipv6_prefix"] = ipv6_prefix
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/internet-service-match", params=params
        )

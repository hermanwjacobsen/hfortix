"""
FortiOS MONITOR - Monitor Router Ipv6

Monitoring endpoint for monitor router ipv6 data.

API Endpoints:
    GET    /monitor/router/ipv6

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.router.ipv6.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.router.ipv6.get(
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


class Ipv6:
    """
    Ipv6 Operations.

    Provides read-only access for FortiOS ipv6 data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Ipv6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        operator: str | None = None,
        ip_mask: str | None = None,
        gateway: str | None = None,
        type: str | None = None,
        origin: str | None = None,
        interface: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all active IPv6 routing table entries.

        Args:
            operator: Filter logic [*and|or]. (optional)
            ip_mask: Filter: IP/netmask. (optional)
            gateway: Filter: gateway. (optional)
            type: Filter: route type. (optional)
            origin: Filter: router origin. (optional)
            interface: Filter: interface name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.router.ipv6.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if operator is not None:
            params["operator"] = operator
        if ip_mask is not None:
            params["ip_mask"] = ip_mask
        if gateway is not None:
            params["gateway"] = gateway
        if type is not None:
            params["type"] = type
        if origin is not None:
            params["origin"] = origin
        if interface is not None:
            params["interface"] = interface
        params.update(kwargs)
        return self._client.get("monitor", "/router/ipv6", params=params)

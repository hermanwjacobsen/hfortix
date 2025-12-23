"""
FortiOS MONITOR - Monitor Virtual Wan Members

Monitoring endpoint for monitor virtual wan members data.

API Endpoints:
    GET    /monitor/virtual_wan/members

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.virtual_wan.members.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.virtual_wan.members.get(
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


class Members:
    """
    Members Operations.

    Provides read-only access for FortiOS members data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Members endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        interface: Any | None = None,
        zone: str | None = None,
        sla: str | None = None,
        skip_vpn_child: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve interface statistics for each SD-WAN link.

        Args:
            interface: Interface name. "interface" param take precedence over
            "zone" or "sla". If set, will return only return the member that
            matches the interface. (optional)
            zone: SD-WAN zone name. "zone" param take precedence over "sla". If
            set, will only return members of the zone. (optional)
            sla: SLA name. If set, will only return members that are
            participants of the SLA. (optional)
            skip_vpn_child: If set, will skip all VPN child interfaces.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.virtual_wan.members.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if interface is not None:
            params["interface"] = interface
        if zone is not None:
            params["zone"] = zone
        if sla is not None:
            params["sla"] = sla
        if skip_vpn_child is not None:
            params["skip_vpn_child"] = skip_vpn_child
        params.update(kwargs)
        return self._client.get(
            "monitor", "/virtual-wan/members", params=params
        )

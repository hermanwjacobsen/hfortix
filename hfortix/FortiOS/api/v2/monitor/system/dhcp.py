"""
FortiOS MONITOR - Monitor System Dhcp

Monitoring endpoint for monitor system dhcp data.

API Endpoints:
    GET    /monitor/system/dhcp

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.dhcp.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.dhcp.get(
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


class Revoke:
    """
    Revoke Operations.

    Provides read-only access for FortiOS revoke data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Revoke endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ip: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Revoke IPv4 DHCP leases.

        Args:
            ip: Optional list of addresses to revoke. Defaults to all addresses
            if not provided. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.dhcp.revoke.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip is not None:
            data["ip"] = ip
        data.update(kwargs)
        return self._client.post("monitor", "/system/dhcp/revoke", data=data)


class Dhcp:
    """Dhcp operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Dhcp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.revoke = Revoke(client)

    def get(
        self,
        scope: str | None = None,
        ipv6: bool | None = None,
        interface: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all DHCP and DHCPv6 leases.

        Args:
            scope: Scope from which to retrieve DHCP leases [vdom*|global].
            Global scope is only accessible for global administrators.
            (optional)
            ipv6: Include IPv6 addresses in the response. (optional)
            interface: Filter: Retrieve DHCP leases for this interface only.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.dhcp.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        if ipv6 is not None:
            params["ipv6"] = ipv6
        if interface is not None:
            params["interface"] = interface
        params.update(kwargs)
        return self._client.get("monitor", "/system/dhcp", params=params)

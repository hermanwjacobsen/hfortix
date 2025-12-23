"""
FortiOS MONITOR - Monitor System Dhcp6

Monitoring endpoint for monitor system dhcp6 data.

API Endpoints:
    GET    /monitor/system/dhcp6

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.dhcp6.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.dhcp6.get(
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
        Revoke IPv6 DHCP leases.

        Args:
            ip: Optional list of addresses to revoke. Defaults to all addresses
            if not provided. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.dhcp6.revoke.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip is not None:
            data["ip"] = ip
        data.update(kwargs)
        return self._client.post("monitor", "/system/dhcp6/revoke", data=data)


class Dhcp6:
    """Dhcp6 operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Dhcp6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.revoke = Revoke(client)

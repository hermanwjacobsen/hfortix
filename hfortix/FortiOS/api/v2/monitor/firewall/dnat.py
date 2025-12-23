"""
FortiOS MONITOR - Monitor Firewall Dnat

Monitoring endpoint for monitor firewall dnat data.

API Endpoints:
    GET    /monitor/firewall/dnat

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.dnat.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.dnat.get(
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


class ClearCounters:
    """
    Clearcounters Operations.

    Provides read-only access for FortiOS clearcounters data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ClearCounters endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        id: int | None = None,
        is_ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset hit count statistics for one or more firewall virtual IP/server
        by ID.

        Args:
            id: Single IDs to reset. (optional)
            is_ipv6: Clear only IPv6 VIP stats. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.dnat.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if id is not None:
            data["id"] = id
        if is_ipv6 is not None:
            data["is_ipv6"] = is_ipv6
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/dnat/clear-counters", data=data
        )


class Reset:
    """Reset operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Reset endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset hit count statistics for all firewall virtual IPs/servers.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.dnat.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/dnat/reset", data=data)


class Dnat:
    """Dnat operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Dnat endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)

    def get(
        self,
        uuid: Any | None = None,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List hit count statistics for firewall virtual IP/server.

        Args:
            uuid: Filter: Virtual IP UUID. (optional)
            ip_version: Filter: Traffic IP Version. [ ipv4 | ipv6 ], if left
            empty, will retrieve data for both IPv4 and IPv6. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.dnat.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if uuid is not None:
            params["uuid"] = uuid
        if ip_version is not None:
            params["ip_version"] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/dnat", params=params)

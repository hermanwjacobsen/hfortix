"""
FortiOS MONITOR - Monitor Firewall Session6

Monitoring endpoint for monitor firewall session6 data.

API Endpoints:
    GET    /monitor/firewall/session6

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.session6.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.session6.get(
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


class CloseMultiple:
    """
    Closemultiple Operations.

    Provides read-only access for FortiOS closemultiple data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CloseMultiple endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        proto: str | None = None,
        saddr: str | None = None,
        daddr: str | None = None,
        sport: int | None = None,
        dport: int | None = None,
        policy: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Close multiple IPv6 firewall sessions which match the provided
        criteria.

        Args:
            proto: Protocol name [tcp|udp|icmp|...] or number. (optional)
            saddr: Source address. (optional)
            daddr: Destination address. (optional)
            sport: Source port. (optional)
            dport: Destination port. (optional)
            policy: Policy ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.session6.close_multiple.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if proto is not None:
            data["proto"] = proto
        if saddr is not None:
            data["saddr"] = saddr
        if daddr is not None:
            data["daddr"] = daddr
        if sport is not None:
            data["sport"] = sport
        if dport is not None:
            data["dport"] = dport
        if policy is not None:
            data["policy"] = policy
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/session6/close-multiple", data=data
        )


class Session6:
    """Session6 operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Session6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.close_multiple = CloseMultiple(client)

"""
FortiOS MONITOR - Monitor Firewall Ztna Firewall Policy

Monitoring endpoint for monitor firewall ztna firewall policy data.

API Endpoints:
    GET    /monitor/firewall/ztna_firewall_policy

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.ztna_firewall_policy.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.ztna_firewall_policy.get(
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
        policy: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset traffic statistics for one or more ZTNA firewall policies by
        policy ID.

        Args:
            policy: Single ZTNA firewall policy ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.firewall.ztna_firewall_policy.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policy is not None:
            data["policy"] = policy
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/firewall/ztna-firewall-policy/clear-counters",
            data=data,
        )


class ZtnaFirewallPolicy:
    """ZtnaFirewallPolicy operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ZtnaFirewallPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)

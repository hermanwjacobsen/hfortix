"""
FortiOS MONITOR - Monitor Firewall Multicast Policy

Monitoring endpoint for monitor firewall multicast policy data.

API Endpoints:
    GET    /monitor/firewall/multicast_policy

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.multicast_policy.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.multicast_policy.get(
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
        Reset traffic statistics for one or more firewall IPv4 multicast
        policies by policy ID.

        Args:
            policy: Single policy ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.multicast_policy.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policy is not None:
            data["policy"] = policy
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/multicast-policy/clear_counters", data=data
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
        Reset traffic statistics for all IPv4 firewall multicast policies.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.multicast_policy.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/multicast-policy/reset", data=data
        )


class MulticastPolicy:
    """MulticastPolicy operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize MulticastPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)
        self.reset = Reset(client)

    def get(
        self,
        policyid: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List traffic statistics for IPv4 firewall multicast policies.

        Args:
            policyid: Filter: Policy ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.multicast_policy.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/multicast-policy", params=params
        )

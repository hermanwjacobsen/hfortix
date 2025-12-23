"""
FortiOS MONITOR - Monitor Firewall Security Policy

Monitoring endpoint for monitor firewall security policy data.

API Endpoints:
    GET    /monitor/firewall/security_policy

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.security_policy.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.security_policy.get(
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
        Reset traffic statistics for one or more security policies by policy
        ID.

        Args:
            policy: Single policy ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.security_policy.clear_counters.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policy is not None:
            data["policy"] = policy
        data.update(kwargs)
        return self._client.post(
            "monitor", "/firewall/security-policy/clear_counters", data=data
        )


class UpdateGlobalLabel:
    """UpdateGlobalLabel operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize UpdateGlobalLabel endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        policyid: str | None = None,
        current_label: str | None = None,
        new_label: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update the global-label of group starting with the provided leading
        policy ID.

        Args:
            policyid: Leading policy ID of the group to update. (optional)
            current_label: The current global-label of the group. If not
            provided, will assume the current group's label is empty string.
            (optional)
            new_label: The new global-label of the group. If not provided, the
            current group's label will be deleted (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.firewall.security_policy.update_global_label.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if policyid is not None:
            data["policyid"] = policyid
        if current_label is not None:
            data["current-label"] = current_label
        if new_label is not None:
            data["new-label"] = new_label
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/firewall/security-policy/update-global-label",
            data=data,
        )


class SecurityPolicy:
    """SecurityPolicy operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SecurityPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_counters = ClearCounters(client)
        self.update_global_label = UpdateGlobalLabel(client)

    def get(
        self,
        policyid: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List IPS engine statistics for security policies.

        Args:
            policyid: Filter: Policy ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.firewall.security_policy.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if policyid is not None:
            params["policyid"] = policyid
        params.update(kwargs)
        return self._client.get(
            "monitor", "/firewall/security-policy", params=params
        )

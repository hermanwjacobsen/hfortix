"""
FortiOS MONITOR - Monitor Switch Controller Mclag Icl

Monitoring endpoint for monitor switch controller mclag icl data.

API Endpoints:
    GET    /monitor/switch_controller/mclag_icl

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.switch_controller.mclag_icl.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.switch_controller.mclag_icl.get(
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


class EligiblePeer:
    """
    Eligiblepeer Operations.

    Provides read-only access for FortiOS eligiblepeer data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize EligiblePeer endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        fortilink: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Find a pair of FortiSwitches that are eligible to form a tier-1 MC-LAG.

        Args:
            fortilink: FortiLink interface name. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.mclag_icl.eligible_peer.get(fortilink='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["fortilink"] = fortilink
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/mclag-icl/eligible-peer",
            params=params,
        )


class SetTierPlus:
    """SetTierPlus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SetTierPlus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        fortilink: str | None = None,
        parent_peer1: str | None = None,
        parent_peer2: str | None = None,
        peer1: str | None = None,
        peer2: str | None = None,
        isl_port_group: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Setup a tier 2/3 MC-LAG link between a pair of FortiSwitches.

        Args:
            fortilink: FortiLink interface name. (optional)
            parent_peer1: FortiSwitch ID for MC-LAG parent peer 1. (optional)
            parent_peer2: FortiSwitch ID for MC-LAG parent peer 2. (optional)
            peer1: FortiSwitch ID for MC-LAG peer 1. (optional)
            peer2: FortiSwitch ID for MC-LAG peer 2. (optional)
            isl_port_group: ISL port group name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.mclag_icl.set_tier_plus.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if fortilink is not None:
            data["fortilink"] = fortilink
        if parent_peer1 is not None:
            data["parent_peer1"] = parent_peer1
        if parent_peer2 is not None:
            data["parent_peer2"] = parent_peer2
        if peer1 is not None:
            data["peer1"] = peer1
        if peer2 is not None:
            data["peer2"] = peer2
        if isl_port_group is not None:
            data["isl_port_group"] = isl_port_group
        data.update(kwargs)
        return self._client.post(
            "monitor", "/switch-controller/mclag-icl/set-tier-plus", data=data
        )


class SetTier1:
    """SetTier1 operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SetTier1 endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        fortilink: str | None = None,
        peer1: str | None = None,
        peer2: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Setup a tier-1 MC-LAG link between a pair of FortiSwitches.

        Args:
            fortilink: FortiLink interface name. (optional)
            peer1: FortiSwitch ID for MC-LAG peer 1. (optional)
            peer2: FortiSwitch ID for MC-LAG peer 2. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.switch_controller.mclag_icl.set_tier1.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if fortilink is not None:
            data["fortilink"] = fortilink
        if peer1 is not None:
            data["peer1"] = peer1
        if peer2 is not None:
            data["peer2"] = peer2
        data.update(kwargs)
        return self._client.post(
            "monitor", "/switch-controller/mclag-icl/set-tier1", data=data
        )


class TierPlusCandidates:
    """TierPlusCandidates operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TierPlusCandidates endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        fortilink: str,
        parent_peer1: str,
        parent_peer2: str,
        is_tier2: bool,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Find a pair of FortiSwitches that are eligible to form a tier 2/3
        MC-LAG.

        Args:
            fortilink: FortiLink interface name. (required)
            parent_peer1: FortiSwitch ID for MC-LAG parent peer 1. (required)
            parent_peer2: FortiSwitch ID for MC-LAG parent peer 2. (required)
            is_tier2: Whether candidates are for a Tier 2 MC-LAG. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.mclag_icl.tier_plus_candidates.get(fortilink='value',
            parent_peer1='value', parent_peer2='value', is_tier2=True)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["fortilink"] = fortilink
        params["parent_peer1"] = parent_peer1
        params["parent_peer2"] = parent_peer2
        params["is_tier2"] = is_tier2
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/switch-controller/mclag-icl/tier-plus-candidates",
            params=params,
        )


class MclagIcl:
    """MclagIcl operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize MclagIcl endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.eligible_peer = EligiblePeer(client)
        self.set_tier_plus = SetTierPlus(client)
        self.set_tier1 = SetTier1(client)
        self.tier_plus_candidates = TierPlusCandidates(client)

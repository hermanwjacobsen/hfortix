"""Type stubs for ZTNA_FIREWALL_POLICY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_counters import ClearCounters

__all__ = [
    "ClearCounters",
    "ZtnaFirewallPolicy",
]


class ZtnaFirewallPolicy:
    """ZTNA_FIREWALL_POLICY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    clear_counters: ClearCounters

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ztna_firewall_policy category with HTTP client."""
        ...

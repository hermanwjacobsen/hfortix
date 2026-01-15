"""Type stubs for LLDP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .network_policy import NetworkPolicy

__all__ = [
    "NetworkPolicy",
    "Lldp",
]


class Lldp:
    """LLDP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    network_policy: NetworkPolicy

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize lldp category with HTTP client."""
        ...

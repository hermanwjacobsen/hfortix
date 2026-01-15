"""Type stubs for ETHERNET_OAM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .cfm import Cfm

__all__ = [
    "Cfm",
    "EthernetOam",
]


class EthernetOam:
    """ETHERNET_OAM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    cfm: Cfm

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ethernet_oam category with HTTP client."""
        ...

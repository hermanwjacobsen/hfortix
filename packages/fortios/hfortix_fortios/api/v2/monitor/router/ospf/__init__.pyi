"""Type stubs for OSPF category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .neighbors import Neighbors

__all__ = [
    "Neighbors",
    "Ospf",
]


class Ospf:
    """OSPF API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    neighbors: Neighbors

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ospf category with HTTP client."""
        ...

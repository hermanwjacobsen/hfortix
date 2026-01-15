"""Type stubs for DHCP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .server import Server

__all__ = [
    "Server",
    "Dhcp",
]


class Dhcp:
    """DHCP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    server: Server

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize dhcp category with HTTP client."""
        ...

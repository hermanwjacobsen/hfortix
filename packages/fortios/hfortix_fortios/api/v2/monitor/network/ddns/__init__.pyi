"""Type stubs for DDNS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .lookup import Lookup
    from .servers import Servers

__all__ = [
    "Lookup",
    "Servers",
    "Ddns",
]


class Ddns:
    """DDNS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    lookup: Lookup
    servers: Servers

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ddns category with HTTP client."""
        ...

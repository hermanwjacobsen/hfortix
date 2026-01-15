"""Type stubs for REGISTRATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .forticare import Forticare
    from .forticloud import Forticloud
    from .vdom import Vdom

__all__ = [
    "Registration",
]


class Registration:
    """REGISTRATION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    forticare: Forticare
    forticloud: Forticloud
    vdom: Vdom

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize registration category with HTTP client."""
        ...

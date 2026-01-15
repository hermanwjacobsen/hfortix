"""Type stubs for CA category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .import_ import Import

__all__ = [
    "Import",
    "Ca",
]


class Ca:
    """CA API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    import_: Import

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ca category with HTTP client."""
        ...

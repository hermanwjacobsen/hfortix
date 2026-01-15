"""Type stubs for LOCAL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .create import Create
    from .import_ import Import

__all__ = [
    "Create",
    "Import",
    "Local",
]


class Local:
    """LOCAL API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    create: Create
    import_: Import

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize local category with HTTP client."""
        ...

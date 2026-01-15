"""Type stubs for REMOTE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .import_ import Import

__all__ = [
    "Import",
    "Remote",
]


class Remote:
    """REMOTE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    import_: Import

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize remote category with HTTP client."""
        ...

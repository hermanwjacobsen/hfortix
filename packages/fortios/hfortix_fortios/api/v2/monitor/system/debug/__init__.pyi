"""Type stubs for DEBUG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .download import Download

__all__ = [
    "Download",
    "Debug",
]


class Debug:
    """DEBUG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    download: Download

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize debug category with HTTP client."""
        ...

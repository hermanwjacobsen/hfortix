"""Type stubs for AV_ARCHIVE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .download import Download

__all__ = [
    "Download",
    "AvArchive",
]


class AvArchive:
    """AV_ARCHIVE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    download: Download

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize av_archive category with HTTP client."""
        ...

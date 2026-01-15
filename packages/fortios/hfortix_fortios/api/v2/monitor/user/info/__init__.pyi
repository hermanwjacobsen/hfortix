"""Type stubs for INFO category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .query import Query
    from .thumbnail import Thumbnail
    from .thumbnail_file import ThumbnailFile

__all__ = [
    "Query",
    "Thumbnail",
    "ThumbnailFile",
    "Info",
]


class Info:
    """INFO API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    query: Query
    thumbnail: Thumbnail
    thumbnail_file: ThumbnailFile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize info category with HTTP client."""
        ...

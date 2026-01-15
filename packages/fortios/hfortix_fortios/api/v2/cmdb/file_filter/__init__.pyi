"""Type stubs for FILE_FILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .profile import Profile

__all__ = [
    "Profile",
    "FileFilter",
]


class FileFilter:
    """FILE_FILTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    profile: Profile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize file_filter category with HTTP client."""
        ...

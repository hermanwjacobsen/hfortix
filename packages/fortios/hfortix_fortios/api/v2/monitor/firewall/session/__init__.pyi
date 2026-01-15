"""Type stubs for SESSION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .close import Close
    from .close_all import CloseAll
    from .close_multiple import CloseMultiple

__all__ = [
    "Close",
    "CloseAll",
    "CloseMultiple",
    "Session",
]


class Session:
    """SESSION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    close: Close
    close_all: CloseAll
    close_multiple: CloseMultiple

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize session category with HTTP client."""
        ...

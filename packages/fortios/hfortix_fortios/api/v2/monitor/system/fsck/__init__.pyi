"""Type stubs for FSCK category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .start import Start

__all__ = [
    "Start",
    "Fsck",
]


class Fsck:
    """FSCK API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    start: Start

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize fsck category with HTTP client."""
        ...

"""Type stubs for SESSION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .cancel import Cancel

__all__ = [
    "Cancel",
    "Session",
]


class Session:
    """SESSION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    cancel: Cancel

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize session category with HTTP client."""
        ...

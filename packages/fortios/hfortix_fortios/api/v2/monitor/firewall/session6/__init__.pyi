"""Type stubs for SESSION6 category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .close_multiple import CloseMultiple

__all__ = [
    "CloseMultiple",
    "Session6",
]


class Session6:
    """SESSION6 API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    close_multiple: CloseMultiple

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize session6 category with HTTP client."""
        ...

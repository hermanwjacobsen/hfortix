"""Type stubs for SSL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .setting import Setting

__all__ = [
    "Setting",
    "Ssl",
]


class Ssl:
    """SSL API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    setting: Setting

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ssl category with HTTP client."""
        ...

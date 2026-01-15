"""Type stubs for DATABASE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .upgrade import Upgrade

__all__ = [
    "Upgrade",
    "Database",
]


class Database:
    """DATABASE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    upgrade: Upgrade

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize database category with HTTP client."""
        ...

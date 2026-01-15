"""Type stubs for QUERY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .abort import Abort

__all__ = [
    "Abort",
    "Query",
]


class Query:
    """QUERY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    abort: Abort

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize query category with HTTP client."""
        ...

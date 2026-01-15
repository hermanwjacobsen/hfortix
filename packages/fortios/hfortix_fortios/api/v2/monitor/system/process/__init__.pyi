"""Type stubs for PROCESS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .kill import Kill

__all__ = [
    "Kill",
    "Process",
]


class Process:
    """PROCESS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    kill: Kill

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize process category with HTTP client."""
        ...

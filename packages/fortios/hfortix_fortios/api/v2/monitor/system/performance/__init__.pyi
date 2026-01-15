"""Type stubs for PERFORMANCE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .status import Status

__all__ = [
    "Status",
    "Performance",
]


class Performance:
    """PERFORMANCE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    status: Status

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize performance category with HTTP client."""
        ...

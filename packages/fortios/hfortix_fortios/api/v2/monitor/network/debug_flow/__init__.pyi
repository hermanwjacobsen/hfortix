"""Type stubs for DEBUG_FLOW category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .start import Start
    from .stop import Stop

__all__ = [
    "Start",
    "Stop",
    "DebugFlow",
]


class DebugFlow:
    """DEBUG_FLOW API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    start: Start
    stop: Stop

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize debug_flow category with HTTP client."""
        ...

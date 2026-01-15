"""Type stubs for CRASH_LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear import Clear
    from .download import Download

__all__ = [
    "Clear",
    "Download",
    "CrashLog",
]


class CrashLog:
    """CRASH_LOG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    clear: Clear
    download: Download

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize crash_log category with HTTP client."""
        ...

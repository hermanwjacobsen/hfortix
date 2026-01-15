"""Type stubs for SNIFFER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .delete import Delete
    from .download import Download
    from .list import List
    from .meta import Meta
    from .start import Start
    from .stop import Stop

__all__ = [
    "Delete",
    "Download",
    "List",
    "Meta",
    "Start",
    "Stop",
    "Sniffer",
]


class Sniffer:
    """SNIFFER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    delete: Delete
    download: Download
    list: List
    meta: Meta
    start: Start
    stop: Stop

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sniffer category with HTTP client."""
        ...

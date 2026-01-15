"""Type stubs for COM_LOG category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .download import Download
    from .dump import Dump
    from .update import Update

__all__ = [
    "Download",
    "Dump",
    "Update",
    "ComLog",
]


class ComLog:
    """COM_LOG API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    download: Download
    dump: Dump
    update: Update

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize com_log category with HTTP client."""
        ...

"""Type stubs for LOCAL_REPORT category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .delete import Delete
    from .download import Download

__all__ = [
    "Delete",
    "Download",
    "LocalReport",
]


class LocalReport:
    """LOCAL_REPORT API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    delete: Delete
    download: Download

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize local_report category with HTTP client."""
        ...

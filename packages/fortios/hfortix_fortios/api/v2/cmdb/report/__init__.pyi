"""Type stubs for REPORT category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .layout import Layout
    from .setting import Setting

__all__ = [
    "Layout",
    "Setting",
    "Report",
]


class Report:
    """REPORT API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    layout: Layout
    setting: Setting

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize report category with HTTP client."""
        ...

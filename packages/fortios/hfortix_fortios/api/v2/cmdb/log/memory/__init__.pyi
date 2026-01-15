"""Type stubs for MEMORY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .filter import Filter
    from .global_setting import GlobalSetting
    from .setting import Setting

__all__ = [
    "Filter",
    "GlobalSetting",
    "Setting",
    "Memory",
]


class Memory:
    """MEMORY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    filter: Filter
    global_setting: GlobalSetting
    setting: Setting

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize memory category with HTTP client."""
        ...

"""Type stubs for NULL_DEVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .filter import Filter
    from .setting import Setting

__all__ = [
    "Filter",
    "Setting",
    "NullDevice",
]


class NullDevice:
    """NULL_DEVICE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    filter: Filter
    setting: Setting

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize null_device category with HTTP client."""
        ...

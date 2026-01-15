"""Type stubs for IPMACBINDING category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .setting import Setting
    from .table import Table

__all__ = [
    "Setting",
    "Table",
    "Ipmacbinding",
]


class Ipmacbinding:
    """IPMACBINDING API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    setting: Setting
    table: Table

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ipmacbinding category with HTTP client."""
        ...

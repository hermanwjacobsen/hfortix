"""Type stubs for ADMIN category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .change_vdom_mode import ChangeVdomMode

__all__ = [
    "ChangeVdomMode",
    "Admin",
]


class Admin:
    """ADMIN API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    change_vdom_mode: ChangeVdomMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize admin category with HTTP client."""
        ...

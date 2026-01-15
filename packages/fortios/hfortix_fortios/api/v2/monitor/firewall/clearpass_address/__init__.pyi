"""Type stubs for CLEARPASS_ADDRESS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .add import Add
    from .delete import Delete

__all__ = [
    "Add",
    "Delete",
    "ClearpassAddress",
]


class ClearpassAddress:
    """CLEARPASS_ADDRESS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    add: Add
    delete: Delete

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize clearpass_address category with HTTP client."""
        ...

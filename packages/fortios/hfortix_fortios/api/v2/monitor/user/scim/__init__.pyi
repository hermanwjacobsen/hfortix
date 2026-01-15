"""Type stubs for SCIM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .groups import Groups
    from .users import Users

__all__ = [
    "Groups",
    "Users",
    "Scim",
]


class Scim:
    """SCIM API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    groups: Groups
    users: Users

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize scim category with HTTP client."""
        ...

"""Type stubs for SERVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .category import Category
    from .custom import Custom
    from .group import Group

__all__ = [
    "Category",
    "Custom",
    "Group",
    "Service",
]


class Service:
    """SERVICE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    category: Category
    custom: Custom
    group: Group

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize service category with HTTP client."""
        ...

"""Type stubs for APPLICATION category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom import Custom
    from .group import Group
    from .list import List
    from .name import Name
    from .rule_settings import RuleSettings

__all__ = [
    "Custom",
    "Group",
    "List",
    "Name",
    "RuleSettings",
    "Application",
]


class Application:
    """APPLICATION API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    custom: Custom
    group: Group
    list: List
    name: Name
    rule_settings: RuleSettings

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize application category with HTTP client."""
        ...

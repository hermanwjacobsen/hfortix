"""Type stubs for WILDCARD_FQDN category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .custom import Custom
    from .group import Group

__all__ = [
    "Custom",
    "Group",
    "WildcardFqdn",
]


class WildcardFqdn:
    """WILDCARD_FQDN API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    custom: Custom
    group: Group

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize wildcard_fqdn category with HTTP client."""
        ...

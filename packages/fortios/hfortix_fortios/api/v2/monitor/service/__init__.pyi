"""Type stubs for SERVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .ldap import Ldap

__all__ = [
    "Service",
]


class Service:
    """SERVICE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    ldap: Ldap

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize service category with HTTP client."""
        ...

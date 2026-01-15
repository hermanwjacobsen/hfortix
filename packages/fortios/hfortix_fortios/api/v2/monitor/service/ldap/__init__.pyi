"""Type stubs for LDAP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .query import Query

__all__ = [
    "Query",
    "Ldap",
]


class Ldap:
    """LDAP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    query: Query

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ldap category with HTTP client."""
        ...

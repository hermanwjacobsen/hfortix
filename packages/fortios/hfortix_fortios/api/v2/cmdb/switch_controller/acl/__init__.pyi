"""Type stubs for ACL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .group import Group
    from .ingress import Ingress

__all__ = [
    "Group",
    "Ingress",
    "Acl",
]


class Acl:
    """ACL API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    group: Group
    ingress: Ingress

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize acl category with HTTP client."""
        ...

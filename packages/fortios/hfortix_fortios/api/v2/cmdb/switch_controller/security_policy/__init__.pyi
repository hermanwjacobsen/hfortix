"""Type stubs for SECURITY_POLICY category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .local_access import LocalAccess
    from .x802_1x import X8021x

__all__ = [
    "LocalAccess",
    "X8021x",
    "SecurityPolicy",
]


class SecurityPolicy:
    """SECURITY_POLICY API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    local_access: LocalAccess
    x802_1x: X8021x

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize security_policy category with HTTP client."""
        ...

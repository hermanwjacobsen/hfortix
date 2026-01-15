"""Type stubs for DHCP6 category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .revoke import Revoke

__all__ = [
    "Revoke",
    "Dhcp6",
]


class Dhcp6:
    """DHCP6 API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    revoke: Revoke

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize dhcp6 category with HTTP client."""
        ...

"""Type stubs for ICAP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .profile import Profile
    from .server import Server
    from .server_group import ServerGroup

__all__ = [
    "Profile",
    "Server",
    "ServerGroup",
    "Icap",
]


class Icap:
    """ICAP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    profile: Profile
    server: Server
    server_group: ServerGroup

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize icap category with HTTP client."""
        ...

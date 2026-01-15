"""Type stubs for OS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .reboot import Reboot
    from .shutdown import Shutdown

__all__ = [
    "Reboot",
    "Shutdown",
    "Os",
]


class Os:
    """OS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    reboot: Reboot
    shutdown: Shutdown

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize os category with HTTP client."""
        ...

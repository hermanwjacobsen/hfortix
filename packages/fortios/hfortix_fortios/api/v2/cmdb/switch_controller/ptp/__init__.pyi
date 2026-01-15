"""Type stubs for PTP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .interface_policy import InterfacePolicy
    from .profile import Profile

__all__ = [
    "InterfacePolicy",
    "Profile",
    "Ptp",
]


class Ptp:
    """PTP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    interface_policy: InterfacePolicy
    profile: Profile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ptp category with HTTP client."""
        ...

"""Type stubs for ANTIVIRUS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .exempt_list import ExemptList
    from .profile import Profile
    from .quarantine import Quarantine
    from .settings import Settings

__all__ = [
    "ExemptList",
    "Profile",
    "Quarantine",
    "Settings",
    "Antivirus",
]


class Antivirus:
    """ANTIVIRUS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    exempt_list: ExemptList
    profile: Profile
    quarantine: Quarantine
    settings: Settings

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize antivirus category with HTTP client."""
        ...

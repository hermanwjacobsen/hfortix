"""Type stubs for SNMP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .community import Community
    from .mib_view import MibView
    from .rmon_stat import RmonStat
    from .sysinfo import Sysinfo
    from .user import User

__all__ = [
    "Community",
    "MibView",
    "RmonStat",
    "Sysinfo",
    "User",
    "Snmp",
]


class Snmp:
    """SNMP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    community: Community
    mib_view: MibView
    rmon_stat: RmonStat
    sysinfo: Sysinfo
    user: User

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize snmp category with HTTP client."""
        ...

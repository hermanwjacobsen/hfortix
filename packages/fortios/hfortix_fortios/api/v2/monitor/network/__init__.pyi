"""Type stubs for NETWORK category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .arp import Arp
    from .reverse_ip_lookup import ReverseIpLookup
    from .ddns import Ddns
    from .debug_flow import DebugFlow
    from .dns import Dns
    from .fortiguard import Fortiguard
    from .lldp import Lldp

__all__ = [
    "Arp",
    "ReverseIpLookup",
    "Network",
]


class Network:
    """NETWORK API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    ddns: Ddns
    debug_flow: DebugFlow
    dns: Dns
    fortiguard: Fortiguard
    lldp: Lldp
    arp: Arp
    reverse_ip_lookup: ReverseIpLookup

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize network category with HTTP client."""
        ...

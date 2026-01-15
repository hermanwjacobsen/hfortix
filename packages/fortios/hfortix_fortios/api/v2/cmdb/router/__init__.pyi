"""Type stubs for ROUTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .access_list import AccessList
    from .access_list6 import AccessList6
    from .aspath_list import AspathList
    from .auth_path import AuthPath
    from .bfd import Bfd
    from .bfd6 import Bfd6
    from .bgp import Bgp
    from .community_list import CommunityList
    from .extcommunity_list import ExtcommunityList
    from .isis import Isis
    from .key_chain import KeyChain
    from .multicast import Multicast
    from .multicast6 import Multicast6
    from .multicast_flow import MulticastFlow
    from .ospf import Ospf
    from .ospf6 import Ospf6
    from .policy import Policy
    from .policy6 import Policy6
    from .prefix_list import PrefixList
    from .prefix_list6 import PrefixList6
    from .rip import Rip
    from .ripng import Ripng
    from .route_map import RouteMap
    from .setting import Setting
    from .static import Static
    from .static6 import Static6

__all__ = [
    "AccessList",
    "AccessList6",
    "AspathList",
    "AuthPath",
    "Bfd",
    "Bfd6",
    "Bgp",
    "CommunityList",
    "ExtcommunityList",
    "Isis",
    "KeyChain",
    "Multicast",
    "Multicast6",
    "MulticastFlow",
    "Ospf",
    "Ospf6",
    "Policy",
    "Policy6",
    "PrefixList",
    "PrefixList6",
    "Rip",
    "Ripng",
    "RouteMap",
    "Setting",
    "Static",
    "Static6",
    "Router",
]


class Router:
    """ROUTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    access_list: AccessList
    access_list6: AccessList6
    aspath_list: AspathList
    auth_path: AuthPath
    bfd: Bfd
    bfd6: Bfd6
    bgp: Bgp
    community_list: CommunityList
    extcommunity_list: ExtcommunityList
    isis: Isis
    key_chain: KeyChain
    multicast: Multicast
    multicast6: Multicast6
    multicast_flow: MulticastFlow
    ospf: Ospf
    ospf6: Ospf6
    policy: Policy
    policy6: Policy6
    prefix_list: PrefixList
    prefix_list6: PrefixList6
    rip: Rip
    ripng: Ripng
    route_map: RouteMap
    setting: Setting
    static: Static
    static6: Static6

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize router category with HTTP client."""
        ...

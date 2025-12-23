"""FortiOS CMDB - Router category"""

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
    "Osp",
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
]


class Router:
    """
    Router category wrapper.

    This class provides access to all router CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize Router with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.access_list = AccessList(client)
        self.access_list6 = AccessList6(client)
        self.aspath_list = AspathList(client)
        self.auth_path = AuthPath(client)
        self.bfd = Bfd(client)
        self.bfd6 = Bfd6(client)
        self.bgp = Bgp(client)
        self.community_list = CommunityList(client)
        self.extcommunity_list = ExtcommunityList(client)
        self.isis = Isis(client)
        self.key_chain = KeyChain(client)
        self.multicast = Multicast(client)
        self.multicast6 = Multicast6(client)
        self.multicast_flow = MulticastFlow(client)
        self.ospf = Ospf(client)
        self.ospf6 = Ospf6(client)
        self.policy = Policy(client)
        self.policy6 = Policy6(client)
        self.prefix_list = PrefixList(client)
        self.prefix_list6 = PrefixList6(client)
        self.rip = Rip(client)
        self.ripng = Ripng(client)
        self.route_map = RouteMap(client)
        self.setting = Setting(client)
        self.static = Static(client)
        self.static6 = Static6(client)

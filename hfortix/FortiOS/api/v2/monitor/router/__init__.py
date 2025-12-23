"""
FortiOS Monitor - Router
Router monitoring and BGP/OSPF operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient

__all__ = ["Router"]

from .bgp import Bgp
from .charts import Charts
from .ipv4 import Ipv4
from .ipv6 import Ipv6
from .lookup import Lookup
from .lookup_policy import LookupPolicy
from .ospf import Ospf
from .policy import Policy
from .policy6 import Policy6
from .sdwan import Sdwan
from .statistics import Statistics


class Router:
    """Router Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Router Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.bgp = Bgp(client)
        self.charts = Charts(client)
        self.ipv4 = Ipv4(client)
        self.ipv6 = Ipv6(client)
        self.lookup = Lookup(client)
        self.lookup_policy = LookupPolicy(client)
        self.ospf = Ospf(client)
        self.policy = Policy(client)
        self.policy6 = Policy6(client)
        self.sdwan = Sdwan(client)
        self.statistics = Statistics(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "bgp",
            "charts",
            "ipv4",
            "ipv6",
            "lookup",
            "lookup_policy",
            "osp",
            "policy",
            "policy6",
            "sdwan",
            "statistics",
        ]

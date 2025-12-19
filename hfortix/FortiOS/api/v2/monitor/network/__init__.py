"""
FortiOS Monitor - Network
Network monitoring operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Network"]

from .arp import Arp
from .ddns import Ddns
from .debug_flow import DebugFlow
from .dns import Dns
from .fortiguard import Fortiguard
from .lldp import Lldp
from .reverse_ip_lookup import ReverseIpLookup


class Network:
    """Network Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Network Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.arp = Arp(client)
        self.ddns = Ddns(client)
        self.debug_flow = DebugFlow(client)
        self.dns = Dns(client)
        self.fortiguard = Fortiguard(client)
        self.lldp = Lldp(client)
        self.reverse_ip_lookup = ReverseIpLookup(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "arp",
            "ddns",
            "debug_flow",
            "dns",
            "fortiguard",
            "lldp",
            "reverse_ip_lookup"
        ]

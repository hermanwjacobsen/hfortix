"""
FortiOS Monitor - Virtual Wan
Virtual WAN monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["VirtualWan"]

from .health_check import HealthCheck
from .interface_log import InterfaceLog
from .members import Members
from .sla_log import SlaLog
from .sladb import Sladb


class VirtualWan:
    """VirtualWan Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize VirtualWan Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.health_check = HealthCheck(client)
        self.interface_log = InterfaceLog(client)
        self.members = Members(client)
        self.sla_log = SlaLog(client)
        self.sladb = Sladb(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["health_check", "interface_log", "members", "sla_log", "sladb"]

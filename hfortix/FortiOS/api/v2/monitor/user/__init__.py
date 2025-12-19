"""
FortiOS Monitor - User
User authentication and monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["User"]

from .banned import Banned
from .collected_email import CollectedEmail
from .device import Device
from .firewall import Firewall
from .fortitoken import Fortitoken
from .fortitoken_cloud import FortitokenCloud
from .fsso import Fsso
from .guest import Guest
from .info import Info
from .local import Local
from .password_policy_conform import PasswordPolicyConform
from .proxy import Proxy
from .query import Query
from .radius import Radius
from .scim import Scim
from .tacacs_plus import TacacsPlus


class User:
    """User Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize User Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.banned = Banned(client)
        self.collected_email = CollectedEmail(client)
        self.device = Device(client)
        self.firewall = Firewall(client)
        self.fortitoken = Fortitoken(client)
        self.fortitoken_cloud = FortitokenCloud(client)
        self.fsso = Fsso(client)
        self.guest = Guest(client)
        self.info = Info(client)
        self.local = Local(client)
        self.password_policy_conform = PasswordPolicyConform(client)
        self.proxy = Proxy(client)
        self.query = Query(client)
        self.radius = Radius(client)
        self.scim = Scim(client)
        self.tacacs_plus = TacacsPlus(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "banned",
            "collected_email",
            "device",
            "firewall",
            "fortitoken",
            "fortitoken_cloud",
            "fsso",
            "guest",
            "info",
            "local",
            "password_policy_conform",
            "proxy",
            "query",
            "radius",
            "scim",
            "tacacs_plus"
        ]

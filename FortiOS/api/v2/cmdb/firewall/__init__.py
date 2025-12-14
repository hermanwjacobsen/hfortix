"""
FortiOS Firewall API
Firewall configuration endpoints
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import FortiOS

from .ipmacbinding import Ipmacbinding
from .schedule import Schedule
from .service import Service
from .shaper import Shaper
from .ssh import Ssh
from .ssl import Ssl
from .wildcard_fqdn import WildcardFqdn


class Firewall:
    """
    Firewall API helper class
    Provides access to firewall configuration endpoints
    """

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Firewall helper

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize sub-category classes (firewall.* API paths)
        from .ipmacbinding import Ipmacbinding
        from .schedule import Schedule
        from .service import Service
        from .shaper import Shaper
        from .ssh import Ssh

        self.ipmacbinding = Ipmacbinding(client)
        self.schedule = Schedule(client)
        self.service = Service(client)
        self.shaper = Shaper(client)
        self.ssh = Ssh(client)
        self.ssl = Ssl(client)
        self.wildcard_fqdn = WildcardFqdn(client)

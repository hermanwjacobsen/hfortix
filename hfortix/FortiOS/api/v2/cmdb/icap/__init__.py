"""
FortiOS ICAP API

Internet Content Adaptation Protocol (ICAP) configuration for content inspection.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Icap:
    """ICAP API endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

        from .profile import Profile
        from .server import Server
        from .server_group import ServerGroup

        self.profile = Profile(client)
        self.server = Server(client)
        self.server_group = ServerGroup(client)

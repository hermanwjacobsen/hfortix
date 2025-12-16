"""
FortiOS Service API
Service operations endpoints (sniffer, security rating, etc.)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient

__all__ = ["Service"]


class Service:
    """
    Service API helper class
    Provides access to service endpoints
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Service helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .security_rating.security_rating import SecurityRating
        from .sniffer.sniffer import Sniffer
        from .system.system import System

        self.sniffer = Sniffer(client)
        self.security_rating = SecurityRating(client)
        self.system = System(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["sniffer", "security_rating", "system"]

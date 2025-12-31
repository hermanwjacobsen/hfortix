"""
FortiOS Monitor - Service
Service monitoring operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

__all__ = ["Service"]

from .ldap import Ldap


class Service:
    """Service Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Service Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.ldap = Ldap(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["ldap"]

"""
FortiOS CMDB Diameter Filter API
Diameter filter configuration endpoints
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["DiameterFilter"]


class DiameterFilter:
    """
    Diameter Filter API helper class
    Provides access to diameter-filter configuration endpoints
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Diameter Filter helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .profile import Profile

        self.profile = Profile(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["profile"]

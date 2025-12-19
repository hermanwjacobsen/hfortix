"""
FortiOS Monitor - Registration
Device registration operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Registration"]

from .forticare import Forticare
from .forticloud import Forticloud
from .vdom import Vdom


class Registration:
    """Registration Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Registration Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.forticare = Forticare(client)
        self.forticloud = Forticloud(client)
        self.vdom = Vdom(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "forticare",
            "forticloud",
            "vdom"
        ]

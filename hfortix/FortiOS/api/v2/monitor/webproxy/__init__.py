"""
FortiOS Monitor - Webproxy
Web proxy monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Webproxy"]

from .pacfile import Pacfile


class Webproxy:
    """Webproxy Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Webproxy Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.pacfile = Pacfile(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["pacfile"]

"""
FortiOS Monitor - Webcache
Web cache monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

__all__ = ["Webcache"]

from .stats import Stats


class Webcache:
    """Webcache Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Webcache Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.stats = Stats(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["stats"]

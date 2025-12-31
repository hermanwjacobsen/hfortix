"""
FortiOS Monitor - Geoip
GeoIP lookup operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

__all__ = ["Geoip"]

from .geoip_query import GeoipQuery


class Geoip:
    """Geoip Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Geoip Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.geoip_query = GeoipQuery(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["geoip_query"]

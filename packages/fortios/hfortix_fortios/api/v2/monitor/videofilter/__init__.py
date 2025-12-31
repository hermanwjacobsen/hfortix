"""
FortiOS Monitor - Videofilter
Video filter monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

__all__ = ["Videofilter"]

from .fortiguard_categories import FortiguardCategories


class Videofilter:
    """Videofilter Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Videofilter Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.fortiguard_categories = FortiguardCategories(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["fortiguard_categories"]

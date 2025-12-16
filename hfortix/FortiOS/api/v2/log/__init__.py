"""
FortiOS Log API
Log retrieval endpoints for various log sources
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient

__all__ = ["Log"]


class Log:
    """
    Log API helper class
    Provides access to log endpoints
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Log helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        from .disk.disk import Disk
        from .fortianalyzer.fortianalyzer import FortiAnalyzer
        from .forticloud.forticloud import FortiCloud
        from .memory.memory import Memory
        from .search.search import Search

        self.disk = Disk(client)
        self.fortianalyzer = FortiAnalyzer(client)
        self.memory = Memory(client)
        self.forticloud = FortiCloud(client)
        self.search = Search(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["disk", "fortianalyzer", "memory", "forticloud", "search"]

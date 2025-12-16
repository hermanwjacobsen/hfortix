"""
FortiOS CMDB - File Filter

File filter configuration for content inspection.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["FileFilter"]

from .profile import Profile


class FileFilter:
    """
    File Filter helper class

    Provides access to file filter configuration endpoints.
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize File Filter helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoint classes
        self.profile = Profile(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["profile"]

"""
FortiExtender Controller Monitor API

This module provides access to FortiExtender monitoring endpoints.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient


class ExtenderController:
    """FortiExtender Controller monitoring."""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize ExtenderController monitor.

        Args:
            client: HTTP client implementing IHTTPClient protocol for API
            communication
        """
        self._client = client
        self._extender: Extender | None = None

    @property
    def extender(self):
        """
        Access FortiExtender sub-endpoint.

        Returns:
            Extender instance
        """
        if self._extender is None:
            from .extender import Extender

            self._extender = Extender(self._client)
        return self._extender

    def __dir__(self):
        """Return list of available attributes."""
        return ["extender"]

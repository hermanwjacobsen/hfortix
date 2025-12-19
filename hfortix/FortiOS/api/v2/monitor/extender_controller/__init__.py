"""
FortiExtender Controller Monitor API

This module provides access to FortiExtender monitoring endpoints.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ExtenderController:
    """FortiExtender Controller monitoring."""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ExtenderController monitor.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client
        self._extender = None

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

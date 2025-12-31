"""
FortiOS Monitor - Fortiview
FortiView statistics and monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

__all__ = ["Fortiview"]

from .historical_statistics import HistoricalStatistics
from .realtime_proxy_statistics import RealtimeProxyStatistics
from .realtime_statistics import RealtimeStatistics
from .session import Session


class Fortiview:
    """Fortiview Monitor category class"""

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize Fortiview Monitor category

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client

        # Initialize endpoints
        self.historical_statistics = HistoricalStatistics(client)
        self.realtime_proxy_statistics = RealtimeProxyStatistics(client)
        self.realtime_statistics = RealtimeStatistics(client)
        self.session = Session(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "historical_statistics",
            "realtime_proxy_statistics",
            "realtime_statistics",
            "session",
        ]

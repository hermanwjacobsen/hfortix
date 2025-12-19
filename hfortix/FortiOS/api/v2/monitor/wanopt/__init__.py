"""
FortiOS Monitor - Wanopt
WAN optimization monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Wanopt"]

from .history import History
from .peer_stats import PeerStats
from .webcache import Webcache


class Wanopt:
    """Wanopt Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Wanopt Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.history = History(client)
        self.peer_stats = PeerStats(client)
        self.webcache = Webcache(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["history", "peer_stats", "webcache"]

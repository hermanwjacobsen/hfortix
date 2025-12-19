"""
FortiOS Monitor - Ips
IPS monitoring and operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Ips"]

from .anomaly import Anomaly
from .hold_signatures import HoldSignatures
from .metadata import Metadata
from .rate_based import RateBased
from .session import Session


class Ips:
    """Ips Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Ips Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.anomaly = Anomaly(client)
        self.hold_signatures = HoldSignatures(client)
        self.metadata = Metadata(client)
        self.rate_based = RateBased(client)
        self.session = Session(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "anomaly",
            "hold_signatures",
            "metadata",
            "rate_based",
            "session"
        ]

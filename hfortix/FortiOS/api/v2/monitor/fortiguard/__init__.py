"""
FortiOS Monitor - Fortiguard
FortiGuard service monitoring and operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Fortiguard"]

from .answers import Answers
from .redirect_portal import RedirectPortal
from .service_communication_stats import ServiceCommunicationStats


class Fortiguard:
    """Fortiguard Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Fortiguard Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.answers = Answers(client)
        self.redirect_portal = RedirectPortal(client)
        self.service_communication_stats = ServiceCommunicationStats(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "answers",
            "redirect_portal",
            "service_communication_stats"
        ]

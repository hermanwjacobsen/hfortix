"""
FortiOS Monitor - Sdwan
SD-WAN monitoring and health checks
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Sdwan"]

from .link_monitor_metrics import LinkMonitorMetrics


class Sdwan:
    """Sdwan Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Sdwan Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.link_monitor_metrics = LinkMonitorMetrics(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["link_monitor_metrics"]

"""
FortiOS Monitor - Azure
Azure SDN connector monitoring and operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Azure"]

from .application_list import ApplicationList


class Azure:
    """Azure Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Azure Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.application_list = ApplicationList(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["application_list"]

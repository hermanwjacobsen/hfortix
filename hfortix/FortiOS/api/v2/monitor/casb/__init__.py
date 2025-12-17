"""
FortiOS Monitor - CASB
CASB (Cloud Access Security Broker) monitoring operations
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Casb"]

from .saas_application import SaasApplication


class Casb:
    """CASB Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize CASB Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.saas_application = SaasApplication(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["saas_application"]

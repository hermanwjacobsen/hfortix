"""
FortiOS Monitor - Webfilter
Web filter monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Webfilter"]

from .category_quota import CategoryQuota
from .fortiguard_categories import FortiguardCategories
from .malicious_urls import MaliciousUrls
from .override import Override
from .trusted_urls import TrustedUrls


class Webfilter:
    """Webfilter Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Webfilter Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.category_quota = CategoryQuota(client)
        self.fortiguard_categories = FortiguardCategories(client)
        self.malicious_urls = MaliciousUrls(client)
        self.override = Override(client)
        self.trusted_urls = TrustedUrls(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["category_quota", "fortiguard_categories", "malicious_urls", "override", "trusted_urls"]

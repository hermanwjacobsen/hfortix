"""
FortiOS Monitor - Utm
UTM (Unified Threat Management) monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Utm"]

from .antivirus import Antivirus
from .app_lookup import AppLookup
from .application_categories import ApplicationCategories
from .blacklisted_certificates import BlacklistedCertificates
from .rating_lookup import RatingLookup


class Utm:
    """Utm Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Utm Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.antivirus = Antivirus(client)
        self.app_lookup = AppLookup(client)
        self.application_categories = ApplicationCategories(client)
        self.blacklisted_certificates = BlacklistedCertificates(client)
        self.rating_lookup = RatingLookup(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ["antivirus", "app_lookup", "application_categories", "blacklisted_certificates", "rating_lookup"]

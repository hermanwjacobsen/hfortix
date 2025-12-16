"""
FortiOS CMDB - Firewall Service

Service configuration sub-category grouping related endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient, HTTPResponse


class Service:
    """Service sub-category grouping related endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Service sub-category

        Args:
            client: HTTPClient instance
        """
        self._client = client

    @property
    def category(self):
        """Access category endpoint"""
        if not hasattr(self, "_category"):
            from .service_category import ServiceCategory

            self._category = ServiceCategory(self._client)
        return self._category

    @property
    def custom(self):
        """Access custom endpoint"""
        if not hasattr(self, "_custom"):
            from .service_custom import ServiceCustom

            self._custom = ServiceCustom(self._client)
        return self._custom

    @property
    def group(self):
        """Access group endpoint"""
        if not hasattr(self, "_group"):
            from .service_group import ServiceGroup

            self._group = ServiceGroup(self._client)
        return self._group

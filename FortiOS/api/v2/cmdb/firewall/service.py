"""
FortiOS CMDB - Firewall Service

Service configuration sub-category grouping related endpoints.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....client import FortiOS


class Service:
    """Service sub-category grouping related endpoints"""

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Service sub-category

        Args:
            client: FortiOS client instance
        """
        self._client = client

    @property
    def category(self):
        """Access category endpoint"""
        from .service_category import ServiceCategory
        return ServiceCategory(self._client)

    @property
    def custom(self):
        """Access custom endpoint"""
        from .service_custom import ServiceCustom
        return ServiceCustom(self._client)

    @property
    def group(self):
        """Access group endpoint"""
        from .service_group import ServiceGroup
        return ServiceGroup(self._client)

"""
FortiOS Monitor - License
License status and management
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["License"]

from .database import Database
from .fortianalyzer_status import FortianalyzerStatus
from .forticare_org_list import ForticareOrgList
from .forticare_resellers import ForticareResellers
from .status import Status


class License:
    """License Monitor category class"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize License Monitor category

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize endpoints
        self.database = Database(client)
        self.fortianalyzer_status = FortianalyzerStatus(client)
        self.forticare_org_list = ForticareOrgList(client)
        self.forticare_resellers = ForticareResellers(client)
        self.status = Status(client)

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            "database",
            "fortianalyzer_status",
            "forticare_org_list",
            "forticare_resellers",
            "status"
        ]

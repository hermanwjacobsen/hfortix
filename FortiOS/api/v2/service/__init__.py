"""
FortiOS Service API
Service endpoints for operations and diagnostics
"""
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ...client import FortiOS


class Service:
    """
    Service API helper class
    Provides access to service endpoints
    """

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Service helper

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize endpoint classes
        from .security_rating.security_rating import SecurityRating
        from .sniffer.sniffer import Sniffer
        from .system.system import System

        self.sniffer = Sniffer(client)
        self.security_rating = SecurityRating(client)
        self.system = System(client)

    def get(
        self,
        endpoint: str,
        params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """
        GET request to service API endpoint

        Args:
            endpoint: API endpoint path (without /api/v2/service/)
            params: Query parameters

        Returns:
            dict: API response
        """
        return self._client.get('service', endpoint, params=params)

    def post(
        self,
        endpoint: str,
        data: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """
        POST request to service API endpoint

        Args:
            endpoint: API endpoint path (without /api/v2/service/)
            data: Request body data

        Returns:
            dict: API response
        """
        return self._client.post('service', endpoint, data=data)

"""
FortiOS Log API
Log retrieval endpoints for various log sources
"""
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ...client import FortiOS


class Log:
    """
    Log API helper class
    Provides access to log endpoints
    """

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Log helper

        Args:
            client: FortiOS client instance
        """
        self._client = client

        # Initialize endpoint classes
        from .disk.disk import Disk
        from .fortianalyzer.fortianalyzer import FortiAnalyzer
        from .forticloud.forticloud import FortiCloud
        from .memory.memory import Memory
        from .search.search import Search

        self.disk = Disk(client)
        self.fortianalyzer = FortiAnalyzer(client)
        self.memory = Memory(client)
        self.forticloud = FortiCloud(client)
        self.search = Search(client)

    def get(
        self,
        endpoint: str,
        params: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        """
        GET request to log API endpoint

        Args:
            endpoint: API endpoint path (without /api/v2/log/)
            params: Query parameters

        Returns:
            dict: API response
        """
        return self._client.get('log', endpoint, params=params)

    def get_binary(
        self,
        endpoint: str,
        params: Optional[dict[str, Any]] = None
    ) -> bytes:
        """
        GET request to log API endpoint returning binary data

        Args:
            endpoint: API endpoint path (without /api/v2/log/)
            params: Query parameters

        Returns:
            bytes: Binary response data
        """
        return self._client.get_binary('log', endpoint, params=params)

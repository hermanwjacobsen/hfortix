"""
FortiOS Log Search API

This module provides methods to manage log search sessions.
"""
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....client import FortiOS


class Search:
    """
    Log Search API for FortiOS.

    Provides methods to manage log search sessions (abort, status).
    """

    def __init__(self, client: 'FortiOS') -> None:
        """Initialize Search log API with FortiOS client."""
        self._client = client

    def abort(self, session_id: int, **kwargs: Any) -> dict[str, Any]:
        """
        Abort a running log search session.

        Args:
            session_id (int): Session ID to abort
            **kwargs: Additional parameters to pass

        Returns:
            dict: Abort operation result

        Example:
            >>> # Start a search and get session_id
            >>> search_result = fgt.log.disk.raw('virus', rows=1000)
            >>> session_id = search_result.get('session_id')

            >>> # Abort the search session
            >>> result = fgt.log.search.abort(session_id)
            >>> print(f"Aborted: {result['status']}")

            >>> # Abort by session ID directly
            >>> result = fgt.log.search.abort(12345)
        """
        endpoint = f'search/abort/{session_id}'
        return self._client.post('log', endpoint, data=kwargs if kwargs else None)

    def status(self, session_id: int, **kwargs: Any) -> dict[str, Any]:
        """
        Returns status of log search session, if it is active or not.

        This is only applicable for disk log search.

        Args:
            session_id (int): Session ID to check
            **kwargs: Additional parameters to pass

        Returns:
            dict: Session status information

        Example:
            >>> # Check status of a search session
            >>> status = fgt.log.search.status(12345)
            >>> print(f"Active: {status.get('active', False)}")
            >>> print(f"Progress: {status.get('progress', 0)}%")

            >>> # After starting a disk search
            >>> search = fgt.log.disk.raw('virus', rows=10000)
            >>> session_id = search.get('session_id')
            >>>
            >>> # Check if still running
            >>> status = fgt.log.search.status(session_id)
            >>> if status.get('active'):
            ...     print("Search still running...")
            ... else:
            ...     print("Search completed!")
        """
        endpoint = f'search/status/{session_id}'
        return self._client.get('log', endpoint, params=kwargs if kwargs else None)

"""
FortiOS Log Search API

This module provides methods to manage log search sessions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Search:
    """
    Log Search API for FortiOS.

    Provides methods to manage log search sessions (abort, status).
    """

    def __init__(self, client: "HTTPClient") -> None:
        """Initialize Search log API with FortiOS client."""
        self._client = client

    def abort(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        session_id: Optional[int] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Abort a running log search session.

        Args:
            data_dict (dict, optional): Dictionary with 'session_id' key
            session_id (int, optional): Session ID to abort
            **kwargs: Additional parameters to pass

        Returns:
            dict: Abort operation result

        Examples:
            >>> # Dictionary pattern
            >>> result = fgt.log.search.abort(data_dict={'session_id': 12345})

            >>> # Keyword pattern
            >>> result = fgt.log.search.abort(session_id=12345)

            >>> # After starting a search
            >>> search_result = fgt.log.disk.raw('virus', rows=1000)
            >>> result = fgt.log.search.abort(session_id=search_result['session_id'])
        """
        if data_dict is not None:
            sid = data_dict.get("session_id", session_id)
        else:
            sid = session_id

        if sid is None:
            raise ValueError("session_id is required")

        endpoint = f"search/abort/{sid}"
        return self._client.post(
            "log", endpoint, data=kwargs if kwargs else None, raw_json=raw_json
        )

    def status(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        session_id: Optional[int] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Returns status of log search session, if it is active or not.

        This is only applicable for disk log search.

        Args:
            data_dict (dict, optional): Dictionary with 'session_id' key
            session_id (int, optional): Session ID to check
            **kwargs: Additional parameters to pass

        Returns:
            dict: Session status information

        Examples:
            >>> # Dictionary pattern
            >>> status = fgt.log.search.status(data_dict={'session_id': 12345})

            >>> # Keyword pattern
            >>> status = fgt.log.search.status(session_id=12345)
            >>> print(f"Active: {status.get('active', False)}")

            >>> # After starting a disk search
            >>> search = fgt.log.disk.raw('virus', rows=10000)
            >>> status = fgt.log.search.status(session_id=search['session_id'])
            >>> if status.get('active'):
            ...     print("Search still running...")
            ... else:
            ...     print("Search completed!")
        """
        if data_dict is not None:
            sid = data_dict.get("session_id", session_id)
        else:
            sid = session_id

        if sid is None:
            raise ValueError("session_id is required")

        endpoint = f"search/status/{sid}"
        return self._client.get(
            "log", endpoint, params=kwargs if kwargs else None, raw_json=raw_json
        )

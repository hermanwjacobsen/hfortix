"""
FortiOS LOG - Log Search Search

Log retrieval endpoint for log search search logs.

API Endpoints:
    GET    /log/search/search

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.log.search.search.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.log.search.search.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Abort:
    """
    Abort Operations.

    Provides read-only access for FortiOS abort data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def post(
        self,
        session_id: int,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Abort a running log search session.

        Supports dual approach:
        1. Individual parameters: post(session_id=12345)
        2. Payload dict: post(session_id=12345, payload_dict={'extra_param':
        'value'})

        Args:
            session_id: Session ID of the log search to abort (required)
            payload_dict: Alternative to individual parameters - pass all
            params as dict
            raw_json: Return raw JSON response without parsing
            **kwargs: Additional parameters to pass to the API

        Returns:
            Dictionary containing abort operation result

        Examples:
            # Abort a search session
            result = fgt.api.log.search.abort.post(session_id=12345)

            # After starting a search
            search_result = fgt.api.log.disk.virus.raw.get(rows=10000)
            result =
            fgt.api.log.search.abort.post(session_id=search_result['session_id'])
        """
        if payload_dict:
            data = payload_dict.copy()
        else:
            data = {}

        data.update(kwargs)

        endpoint = f"search/abort/{session_id}"
        return self._client.post("log", endpoint, data=data, raw_json=raw_json)


class Status:
    """Status search session endpoint resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        session_id: int,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Returns status of log search session, if it is active or not.

        This is only applicable for disk log search.

        Supports dual approach:
        1. Individual parameters: get(session_id=12345)
        2. Payload dict: get(session_id=12345, payload_dict={'extra_param':
        'value'})

        Args:
            session_id: Session ID of the log search to check status (required)
            payload_dict: Alternative to individual parameters - pass all
            params as dict
            raw_json: Return raw JSON response without parsing
            **kwargs: Additional parameters to pass to the API

        Returns:
            Dictionary containing session status information

        Examples:
            # Check search status
            status = fgt.api.log.search.status.get(session_id=12345)
            print(f"Active: {status.get('active', False)}")

            # After starting a disk search
            search = fgt.api.log.disk.virus.raw.get(rows=10000)
            status =
            fgt.api.log.search.status.get(session_id=search['session_id'])
            if status.get('active'):
                print("Search still running...")
            else:
                print("Search completed!")
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}

        params.update(kwargs)

        endpoint = f"search/status/{session_id}"
        return self._client.get(
            "log", endpoint, params=params, raw_json=raw_json
        )


class Search:
    """
    Log Search API for FortiOS.

    Provides methods to manage log search sessions.

    Attributes:
        abort: Abort a running log search session
        status: Check status of a log search session

    Examples:
        # Abort a search session
        fgt.api.log.search.abort.post(session_id=12345)

        # Check search status
        status = fgt.api.log.search.status.get(session_id=12345)
    """

    def __init__(self, client: "IHTTPClient") -> None:
        """Initialize Search log API with FortiOS client."""
        self._client = client
        self.abort = Abort(client)
        self.status = Status(client)


__all__ = ["Search", "Abort", "Status"]

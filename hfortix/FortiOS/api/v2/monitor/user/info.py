"""
FortiOS MONITOR - Monitor User Info

Monitoring endpoint for monitor user info data.

API Endpoints:
    GET    /monitor/user/info

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.info.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.info.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Query:
    """
    Query Operations.

    Provides read-only access for FortiOS query data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Query endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        timestamp_from: int | None = None,
        timestamp_to: int | None = None,
        filters: list | None = None,
        query_type: str | None = None,
        query_id: int | None = None,
        cache_query: bool | None = None,
        key_only: bool | None = None,
        filter_logic: str | None = None,
        total_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Query user info.

        Args:
            timestamp_from: To get entries since the timestamp for unified
            historical query. (optional)
            timestamp_to: To get entries before the timestamp for unified
            historical query. (optional)
            filters: A list of filters. Type:{"type": string, "value": string,
            "op": string}. Op: filter operator
            [exact|contains|greaterThanEqualTo|lessThanEqualTo]. Default is
            exact. (optional)
            query_type: Query type [latest|unified_latest|unified_history].
            Default is latest. (optional)
            query_id: Provide a query ID to continue getting data for that
            unified request. Only available for unified query types. (optional)
            cache_query: Cache query result for 5 mins and return query ID.
            Only available for unified query types. Default is false.
            (optional)
            key_only: Return primary key fields only. Default is false.
            (optional)
            filter_logic: The logic between filters [and|or]). Default is and.
            (optional)
            total_only: Whether the query should return just the total number
            of identities present. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.info.query.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if timestamp_from is not None:
            params["timestamp_from"] = timestamp_from
        if timestamp_to is not None:
            params["timestamp_to"] = timestamp_to
        if filters is not None:
            params["filters"] = filters
        if query_type is not None:
            params["query_type"] = query_type
        if query_id is not None:
            params["query_id"] = query_id
        if cache_query is not None:
            params["cache_query"] = cache_query
        if key_only is not None:
            params["key_only"] = key_only
        if filter_logic is not None:
            params["filter_logic"] = filter_logic
        if total_only is not None:
            params["total_only"] = total_only
        params.update(kwargs)
        return self._client.get("monitor", "/user/info/query", params=params)


class Thumbnail:
    """Thumbnail operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Thumbnail endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        filters: list,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get user info thumbnail.

        Args:
            filters: A list of filters. Type:{"type": string, "value": string}
            (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.info.thumbnail.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params["filters"] = filters
        params.update(kwargs)
        return self._client.get(
            "monitor", "/user/info/thumbnail", params=params
        )


class ThumbnailFile:
    """ThumbnailFile operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ThumbnailFile endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        filename: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get user info thumbnail by given file name.

        Args:
            filename: Thumbnail file name. The file name is from thumbnailPhoto
            field of user info query. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.info.thumbnail_file.get(filename='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["filename"] = filename
        params.update(kwargs)
        return self._client.get(
            "monitor", "/user/info/thumbnail-file", params=params
        )


class Info:
    """Info operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Info endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.query = Query(client)
        self.thumbnail = Thumbnail(client)
        self.thumbnail_file = ThumbnailFile(client)

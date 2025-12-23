"""
FortiOS MONITOR - Monitor Fortiguard Answers

Monitoring endpoint for monitor fortiguard answers data.

API Endpoints:
    GET    /monitor/fortiguard/answers

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.fortiguard.answers.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.fortiguard.answers.get(
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


class Answers:
    """
    Answers Operations.

    Provides read-only access for FortiOS answers data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Answers endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        page: int | None = None,
        pagesize: int | None = None,
        sortkey: str | None = None,
        topics: str | None = None,
        limit: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of questions on answers.

        Args:
            page: Page number to retrieve. (optional)
            pagesize: Page size of a list of response. (optional)
            sortkey: Sort key of a list of response. (optional)
            topics: Topic to retrieve. (optional)
            limit: Limit of the number of entries. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.fortiguard.answers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if page is not None:
            params["page"] = page
        if pagesize is not None:
            params["pagesize"] = pagesize
        if sortkey is not None:
            params["sortkey"] = sortkey
        if topics is not None:
            params["topics"] = topics
        if limit is not None:
            params["limit"] = limit
        params.update(kwargs)
        return self._client.get(
            "monitor", "/fortiguard/answers", params=params
        )

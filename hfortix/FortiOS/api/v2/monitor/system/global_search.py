"""
FortiOS MONITOR - Monitor System Global Search

Monitoring endpoint for monitor system global search data.

API Endpoints:
    GET    /monitor/system/global_search

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.global_search.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.global_search.get(
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


class GlobalSearch:
    """
    Globalsearch Operations.

    Provides read-only access for FortiOS globalsearch data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize GlobalSearch endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        search: str,
        scope: str | None = None,
        search_tables: list | None = None,
        skip_tables: list | None = None,
        exact: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Search for CMDB table objects based on search phrase.

        Args:
            search: Phrase used for searching. (required)
            scope: Search scope [vdom|global]. (optional)
            search_tables: Array of CMDB tables to search on. If not defined,
            global search function will do a search on all tables that the
            current user has read permission on. E.g ['firewall.address',
            'firewall.address6']. (optional)
            skip_tables: Array of CMDB tables to be skipped when doing global
            search. E.g. ['firewall.address', 'firewall.address6']. (optional)
            exact: If true, only entries with exact match will be returned.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.global_search.get(search='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["search"] = search
        if scope is not None:
            params["scope"] = scope
        if search_tables is not None:
            params["search_tables"] = search_tables
        if skip_tables is not None:
            params["skip_tables"] = skip_tables
        if exact is not None:
            params["exact"] = exact
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/global-search", params=params
        )

"""
FortiOS MONITOR - Monitor Log Fortianalyzer Queue

Monitoring endpoint for monitor log fortianalyzer queue data.

API Endpoints:
    GET    /monitor/log/fortianalyzer_queue

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.fortianalyzer_queue.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.fortianalyzer_queue.get(
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


class FortianalyzerQueue:
    """
    Fortianalyzerqueue Operations.

    Provides read-only access for FortiOS fortianalyzerqueue data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize FortianalyzerQueue endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve information on FortiAnalyzer's queue state.

        Args:
            scope: Scope from which to retrieve FortiAnalyzer's queue state
            [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.log.fortianalyzer_queue.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/log/fortianalyzer-queue", params=params
        )

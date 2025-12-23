"""
FortiOS MONITOR - Monitor Log Fortianalyzer

Monitoring endpoint for monitor log fortianalyzer data.

API Endpoints:
    GET    /monitor/log/fortianalyzer

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.fortianalyzer.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.fortianalyzer.get(
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


class Fortianalyzer:
    """
    Fortianalyzer Operations.

    Provides read-only access for FortiOS fortianalyzer data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Fortianalyzer endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        server: str | None = None,
        srcip: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Return FortiAnalyzer/FortiManager log status.

        Args:
            scope: Scope from which to test the connectivity of the
            FortiAnalyzer address [vdom|global]. (optional)
            server: FortiAnalyzer/FortiManager address. (optional)
            srcip: The IP to use to make the request to the FortiAnalyzer
            [<ip>|auto]. When set to "auto" it will use the FortiGate's routing
            table to determine the IP to make the request from. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.log.fortianalyzer.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        if server is not None:
            params["server"] = server
        if srcip is not None:
            params["srcip"] = srcip
        params.update(kwargs)
        return self._client.get("monitor", "/log/fortianalyzer", params=params)

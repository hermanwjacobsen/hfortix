"""
FortiOS MONITOR - Monitor Utm App Lookup

Monitoring endpoint for monitor utm app lookup data.

API Endpoints:
    GET    /monitor/utm/app_lookup

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.utm.app_lookup.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.utm.app_lookup.get(
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


class AppLookup:
    """
    Applookup Operations.

    Provides read-only access for FortiOS applookup data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize AppLookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        hosts: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Query ISDB to resolve hosts to application control entries.

        Args:
            hosts: List of hosts to resolve. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.utm.app_lookup.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if hosts is not None:
            params["hosts"] = hosts
        params.update(kwargs)
        return self._client.get("monitor", "/utm/app-lookup", params=params)

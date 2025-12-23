"""
FortiOS MONITOR - Monitor Log Stats

Monitoring endpoint for monitor log stats data.

API Endpoints:
    GET    /monitor/log/stats

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.stats.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.stats.get(
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


class Reset:
    """
    Reset Operations.

    Provides read-only access for FortiOS reset data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Reset endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset logging statistics for all log devices.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.log.stats.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/log/stats/reset", data=data)


class Stats:
    """Stats operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Stats endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reset = Reset(client)

    def get(
        self,
        dev: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Return number of logs sent by category per day for a specific log
        device.

        Args:
            dev: Log device [*memory | disk | fortianalyzer | forticloud].
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.log.stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if dev is not None:
            params["dev"] = dev
        params.update(kwargs)
        return self._client.get("monitor", "/log/stats", params=params)

"""
FortiOS MONITOR - Monitor System Time

Monitoring endpoint for monitor system time data.

API Endpoints:
    GET    /monitor/system/time

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.time.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.time.get(
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


class Set:
    """
    Set Operations.

    Provides read-only access for FortiOS set data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Set endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
        hour: int | None = None,
        minute: int | None = None,
        second: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Sets current system time stamp.

        Args:
            year: Specifies the year for setting/updating time manually.
            (optional)
            month: Specifies the month (0 - 11) for setting/updating time
            manually. (optional)
            day: Specifies the day for setting/updating time manually.
            (optional)
            hour: Specifies the hour (0 - 23) for setting/updating time
            manually. (optional)
            minute: Specifies the minute (0 - 59) for setting/updating time
            manually. (optional)
            second: Specifies the second (0 - 59) for setting/updating time
            manually. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.time.set.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if year is not None:
            data["year"] = year
        if month is not None:
            data["month"] = month
        if day is not None:
            data["day"] = day
        if hour is not None:
            data["hour"] = hour
        if minute is not None:
            data["minute"] = minute
        if second is not None:
            data["second"] = second
        data.update(kwargs)
        return self._client.post("monitor", "/system/time/set", data=data)


class Time:
    """Time operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Time endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.set = Set(client)

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Gets current system time stamp.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.time.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/system/time", params=params)

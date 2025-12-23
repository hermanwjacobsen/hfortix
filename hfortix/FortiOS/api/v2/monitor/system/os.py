"""
FortiOS MONITOR - Monitor System Os

Monitoring endpoint for monitor system os data.

API Endpoints:
    GET    /monitor/system/os

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.os.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.os.get(
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


class Reboot:
    """
    Reboot Operations.

    Provides read-only access for FortiOS reboot data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Reboot endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        event_log_message: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Immediately reboot this device.

        Args:
            event_log_message: Message to be logged in event log. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.os.reboot.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if event_log_message is not None:
            data["event_log_message"] = event_log_message
        data.update(kwargs)
        return self._client.post("monitor", "/system/os/reboot", data=data)


class Shutdown:
    """Shutdown operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Shutdown endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        event_log_message: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Immediately shutdown this device.

        Args:
            event_log_message: Message to be logged in event log. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.os.shutdown.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if event_log_message is not None:
            data["event_log_message"] = event_log_message
        data.update(kwargs)
        return self._client.post("monitor", "/system/os/shutdown", data=data)


class Os:
    """Os operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Os endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reboot = Reboot(client)
        self.shutdown = Shutdown(client)

"""
FortiOS MONITOR - Monitor System Process

Monitoring endpoint for monitor system process data.

API Endpoints:
    GET    /monitor/system/process

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.process.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.process.get(
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


class Kill:
    """
    Kill Operations.

    Provides read-only access for FortiOS kill data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Kill endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        pid: int | None = None,
        signal: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Kill a running process.

        Args:
            pid: The process ID. (optional)
            signal: Signal to use when killing the process [9 (SIGKILL) | 11
            (SIGSEGV) | 15 (SIGTERM)]. Defaults to 15. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.process.kill.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if pid is not None:
            data["pid"] = pid
        if signal is not None:
            data["signal"] = signal
        data.update(kwargs)
        return self._client.post("monitor", "/system/process/kill", data=data)


class Process:
    """Process operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Process endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.kill = Kill(client)

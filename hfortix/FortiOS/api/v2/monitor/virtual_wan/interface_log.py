"""
FortiOS MONITOR - Monitor Virtual Wan Interface Log

Monitoring endpoint for monitor virtual wan interface log data.

API Endpoints:
    GET    /monitor/virtual_wan/interface_log

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.virtual_wan.interface_log.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.virtual_wan.interface_log.get(
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


class InterfaceLog:
    """
    Interfacelog Operations.

    Provides read-only access for FortiOS interfacelog data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize InterfaceLog endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        interface: str | None = None,
        since: int | None = None,
        seconds: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve log of SD-WAN interface quality information.

        Args:
            interface: Filter: Interface name. (optional)
            since: Filter: Only return SLA logs generated since this Unix
            timestamp. (optional)
            seconds: Filter: Only return SLA logs generated in the last N
            seconds. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.virtual_wan.interface_log.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if interface is not None:
            params["interface"] = interface
        if since is not None:
            params["since"] = since
        if seconds is not None:
            params["seconds"] = seconds
        params.update(kwargs)
        return self._client.get(
            "monitor", "/virtual-wan/interface-log", params=params
        )

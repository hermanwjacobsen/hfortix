"""
FortiOS MONITOR - Monitor Log Device

Monitoring endpoint for monitor log device data.

API Endpoints:
    GET    /monitor/log/device

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.device.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.device.get(
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


class State:
    """
    State Operations.

    Provides read-only access for FortiOS state data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize State endpoint.

        Args:
            client: HTTPClient instance
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
        Retrieve information on state of log devices.

        Args:
            scope: Scope from which to retrieve log device state
            [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.log.device.state.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/log/device/state", params=params)


class Device:
    """Device operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Device endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.state = State(client)

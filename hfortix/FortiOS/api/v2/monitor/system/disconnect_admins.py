"""
FortiOS MONITOR - Monitor System Disconnect Admins

Monitoring endpoint for monitor system disconnect admins data.

API Endpoints:
    GET    /monitor/system/disconnect_admins

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.disconnect_admins.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.disconnect_admins.get(
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


class Select:
    """
    Select Operations.

    Provides read-only access for FortiOS select data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Select endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        id: int | None = None,
        method: str | None = None,
        admins: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Disconnects logged in administrators.

        Args:
            id: Admin ID (optional)
            method: Login method used to connect admin to FortiGate. (optional)
            admins: List of objects with admin id and method. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.disconnect_admins.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if id is not None:
            data["id"] = id
        if method is not None:
            data["method"] = method
        if admins is not None:
            data["admins"] = admins
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/disconnect-admins/select", data=data
        )


class DisconnectAdmins:
    """DisconnectAdmins operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize DisconnectAdmins endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.select = Select(client)

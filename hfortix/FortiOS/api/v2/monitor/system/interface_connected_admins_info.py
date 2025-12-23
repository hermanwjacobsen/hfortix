"""
FortiOS MONITOR - Monitor System Interface Connected Admins Info

Monitoring endpoint for monitor system interface connected admins info data.

API Endpoints:
    GET    /monitor/system/interface_connected_admins_info

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.interface_connected_admins_info.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.interface_connected_admins_info.get(
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


class InterfaceConnectedAdminsInfo:
    """
    Interfaceconnectedadminsinfo Operations.

    Provides read-only access for FortiOS interfaceconnectedadminsinfo data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize InterfaceConnectedAdminsInfo endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        interface: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Return admins info that are connected to current interface.

        Args:
            interface: Interface that admins is connected through. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.interface_connected_admins_info.get(interface='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["interface"] = interface
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/interface-connected-admins-info", params=params
        )

"""
FortiOS MONITOR - Monitor Wifi Unassociated Devices

Monitoring endpoint for monitor wifi unassociated devices data.

API Endpoints:
    GET    /monitor/wifi/unassociated_devices

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.unassociated_devices.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.unassociated_devices.get(
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


class UnassociatedDevices:
    """
    Unassociateddevices Operations.

    Provides read-only access for FortiOS unassociateddevices data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize UnassociatedDevices endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        with_triangulation: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
                Retrieve a list of unassociated and BLE devices
        Access Group: wifi.

                Args:
                    with_triangulation: Enable to include regions of FortiAP
                    detecting the device. (optional)
                    payload_dict: Optional dictionary of parameters
                    raw_json: Return raw JSON response if True
                    **kwargs: Additional parameters as keyword arguments

                Returns:
                    Dictionary containing API response

                Example:
                    >>> fgt.api.monitor.wifi.unassociated_devices.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if with_triangulation is not None:
            params["with_triangulation"] = with_triangulation
        params.update(kwargs)
        return self._client.get(
            "monitor", "/wifi/unassociated-devices", params=params
        )

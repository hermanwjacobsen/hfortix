"""
FortiOS MONITOR - Monitor Wifi Ap Names

Monitoring endpoint for monitor wifi ap names data.

API Endpoints:
    GET    /monitor/wifi/ap_names

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.ap_names.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.ap_names.get(
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


class ApNames:
    """
    Apnames Operations.

    Provides read-only access for FortiOS apnames data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ApNames endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
                Retrieve list of objects, each containing the valid serial
                number prefix, platform short name
        Access Group: wifi.

                Args:
                    payload_dict: Optional dictionary of parameters
                    raw_json: Return raw JSON response if True
                    **kwargs: Additional parameters as keyword arguments

                Returns:
                    Dictionary containing API response

                Example:
                    >>> fgt.api.monitor.wifi.ap_names.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/ap-names", params=params)

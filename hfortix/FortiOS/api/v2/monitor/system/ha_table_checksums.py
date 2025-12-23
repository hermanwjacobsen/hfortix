"""
FortiOS MONITOR - Monitor System Ha Table Checksums

Monitoring endpoint for monitor system ha table checksums data.

API Endpoints:
    GET    /monitor/system/ha_table_checksums

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.ha_table_checksums.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.ha_table_checksums.get(
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


class HaTableChecksums:
    """
    Hatablechecksums Operations.

    Provides read-only access for FortiOS hatablechecksums data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize HaTableChecksums endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        serial_no: str,
        vdom_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List of table checksums for members of HA cluster.

        Args:
            serial_no: Serial number of the HA member. (required)
            vdom_name: VDOM name of the HA member. If not specified, fetch
            table checksums for global. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.ha_table_checksums.get(serial_no='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["serial_no"] = serial_no
        if vdom_name is not None:
            params["vdom_name"] = vdom_name
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/ha-table-checksums", params=params
        )

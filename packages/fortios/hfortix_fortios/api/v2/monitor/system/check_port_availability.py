"""
FortiOS MONITOR - Monitor System Check Port Availability

Monitoring endpoint for monitor system check port availability data.

API Endpoints:
    GET    /monitor/system/check_port_availability

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.check_port_availability.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.check_port_availability.get(
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

    from hfortix_core.http.interface import IHTTPClient


class CheckPortAvailability:
    """
    Checkportavailability Operations.

    Provides read-only access for FortiOS checkportavailability data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CheckPortAvailability endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        port_ranges: list,
        service: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Check whether a list of TCP port ranges is available for a certain
        service.

        Args:
            port_ranges: List of TCP port range objects to check against.
            (required)
            service: The service in which the ports could be available.
            'service' options are [reserved | sysglobal | webproxy | ftpproxy |
            sslvpn | slaprobe | fsso | ftm_push]. If 'service' is not
            specified, the port ranges availability is checked against all
            services. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.check_port_availability.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params["port_ranges"] = port_ranges
        if service is not None:
            params["service"] = service
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/check-port-availability", params=params
        )

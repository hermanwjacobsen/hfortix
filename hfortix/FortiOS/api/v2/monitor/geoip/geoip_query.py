"""
FortiOS MONITOR - Monitor Geoip Geoip Query

Monitoring endpoint for monitor geoip geoip query data.

API Endpoints:
    GET    /monitor/geoip/geoip_query

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.geoip.geoip_query.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.geoip.geoip_query.get(
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
        ip_addresses: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve location details for IPs queried against FortiGuard's geoip
        service.

        Args:
            ip_addresses: One or more IP address strings to query for location
            details. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.geoip.geoip_query.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ip_addresses is not None:
            data["ip_addresses"] = ip_addresses
        data.update(kwargs)
        return self._client.post(
            "monitor", "/geoip/geoip-query/select", data=data
        )


class GeoipQuery:
    """GeoipQuery operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize GeoipQuery endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.select = Select(client)

"""
FortiOS MONITOR - Monitor Virtual Wan Health Check

Monitoring endpoint for monitor virtual wan health check data.

API Endpoints:
    GET    /monitor/virtual_wan/health_check

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.virtual_wan.health_check.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.virtual_wan.health_check.get(
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


class HealthCheck:
    """
    Healthcheck Operations.

    Provides read-only access for FortiOS healthcheck data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize HealthCheck endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        health_check_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve health-check statistics for each SD-WAN link.

        Args:
            health_check_name: Health check name. If not provided, will return
            results of all health checks. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.virtual_wan.health_check.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if health_check_name is not None:
            params["health_check_name"] = health_check_name
        params.update(kwargs)
        return self._client.get(
            "monitor", "/virtual-wan/health-check", params=params
        )

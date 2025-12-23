"""
FortiOS MONITOR - Monitor Fortiguard Service Communication Stats

Monitoring endpoint for monitor fortiguard service communication stats data.

API Endpoints:
    GET    /monitor/fortiguard/service_communication_stats

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.fortiguard.service_communication_stats.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.fortiguard.service_communication_stats.get(
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


class ServiceCommunicationStats:
    """
    Servicecommunicationstats Operations.

    Provides read-only access for FortiOS servicecommunicationstats data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ServiceCommunicationStats endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        service_type: str | None = None,
        timeslot: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve historical statistics for communication with FortiGuard
        services.

        Args:
            service_type: To get stats for
            [forticare|fortiguard_download|fortiguard_query|forticloud_log|fortisandbox_cloud|fortiguard.com|sdns|fortitoken_registration|sms_service].
            Defaults to all stats if not provided. (optional)
            timeslot: History timeslot of stats [1_hour|24_hour|1_week].
            Defaults to all timeslots if not provided. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.fortiguard.service_communication_stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if service_type is not None:
            params["service_type"] = service_type
        if timeslot is not None:
            params["timeslot"] = timeslot
        params.update(kwargs)
        return self._client.get(
            "monitor", "/fortiguard/service-communication-stats", params=params
        )

"""
FortiOS MONITOR - Monitor Sdwan Link Monitor Metrics

Monitoring endpoint for monitor sdwan link monitor metrics data.

API Endpoints:
    GET    /monitor/sdwan/link_monitor_metrics

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.sdwan.link_monitor_metrics.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.sdwan.link_monitor_metrics.get(
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


class Report:
    """
    Report Operations.

    Provides read-only access for FortiOS report data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Report endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        agent_ip: str | None = None,
        application_name: str | None = None,
        application_id: int | None = None,
        latency: str | None = None,
        jitter: str | None = None,
        packet_loss: str | None = None,
        ntt: str | None = None,
        srt: str | None = None,
        application_error: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Report the application-level performance metrics collected by other
        fabric devices.

        Args:
            agent_ip: IPv4 or IPv6 address. (optional)
            application_name: Destination application that the FMR agent is
            monitoring. (optional)
            application_id: Destination application ID based on the FortiGuard
            Application Control DB. (optional)
            latency: Latency to report (ms). (optional)
            jitter: Jitter to report (ms). (optional)
            packet_loss: Packet loss to report [0, 100]. (optional)
            ntt: Network transmit time (ms). (optional)
            srt: Server response time (ms). (optional)
            application_error: Application errors in the current session.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.sdwan.link_monitor_metrics.report.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if agent_ip is not None:
            data["agent_ip"] = agent_ip
        if application_name is not None:
            data["application_name"] = application_name
        if application_id is not None:
            data["application_id"] = application_id
        if latency is not None:
            data["latency"] = latency
        if jitter is not None:
            data["jitter"] = jitter
        if packet_loss is not None:
            data["packet_loss"] = packet_loss
        if ntt is not None:
            data["ntt"] = ntt
        if srt is not None:
            data["srt"] = srt
        if application_error is not None:
            data["application_error"] = application_error
        data.update(kwargs)
        return self._client.post(
            "monitor", "/sdwan/link-monitor-metrics/report", data=data
        )


class LinkMonitorMetrics:
    """LinkMonitorMetrics operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize LinkMonitorMetrics endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.report = Report(client)

"""
FortiOS MONITOR - Monitor Virtual Wan Sla Log

Monitoring endpoint for monitor virtual wan sla log data.

API Endpoints:
    GET    /monitor/virtual_wan/sla_log

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.virtual_wan.sla_log.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.virtual_wan.sla_log.get(
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


class SlaLog:
    """
    Slalog Operations.

    Provides read-only access for FortiOS slalog data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SlaLog endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        sla: Any | None = None,
        interface: str | None = None,
        since: int | None = None,
        seconds: int | None = None,
        latest: bool | None = None,
        min_sample_interval: int | None = None,
        sampling_interval: int | None = None,
        skip_vpn_child: bool | None = None,
        include_sla_targets_met: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve logs of SLA probe results for the specified SD-WAN SLA or
        health check name.

        Args:
            sla: Filter: SLA name. (optional)
            interface: Filter: Interface name. (optional)
            since: Filter: Only return SLA logs generated since this Unix
            timestamp. (optional)
            seconds: Filter: Only return SLA logs generated in the last N
            seconds. (optional)
            latest: If set, will only return the latest log, in the meantime,
            since, seconds, or sampling_interval will be ignored. (optional)
            min_sample_interval: Minimum seconds between kept log samples.
            Returned samples may not be evenly spaced (default: 5). (optional)
            sampling_interval: Deprecated: Use min_sample_interval instead
            (optional)
            skip_vpn_child: If set, will skip all VPN child interfaces.
            (optional)
            include_sla_targets_met: If set, will return SLA targets that are
            met. Can only be used when "latest" is set. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.virtual_wan.sla_log.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if sla is not None:
            params["sla"] = sla
        if interface is not None:
            params["interface"] = interface
        if since is not None:
            params["since"] = since
        if seconds is not None:
            params["seconds"] = seconds
        if latest is not None:
            params["latest"] = latest
        if min_sample_interval is not None:
            params["min_sample_interval"] = min_sample_interval
        if sampling_interval is not None:
            params["sampling_interval"] = sampling_interval
        if skip_vpn_child is not None:
            params["skip_vpn_child"] = skip_vpn_child
        if include_sla_targets_met is not None:
            params["include_sla_targets_met"] = include_sla_targets_met
        params.update(kwargs)
        return self._client.get(
            "monitor", "/virtual-wan/sla-log", params=params
        )

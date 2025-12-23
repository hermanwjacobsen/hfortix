"""
FortiOS MONITOR - Monitor System Traffic History

Monitoring endpoint for monitor system traffic history data.

API Endpoints:
    GET    /monitor/system/traffic_history

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.traffic_history.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.traffic_history.get(
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


class EnableAppBandwidthTracking:
    """
    Enableappbandwidthtracking Operations.

    Provides read-only access for FortiOS enableappbandwidthtracking data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize EnableAppBandwidthTracking endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Enable FortiView application bandwidth tracking.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.traffic_history.enable_app_bandwidth_tracking.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/system/traffic-history/enable-app-bandwidth-tracking",
            data=data,
        )


class Interface:
    """Interface operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Interface endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        interface: str,
        time_period: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve history traffic stats for an interface.

        Args:
            interface: Interface name. (required)
            time_period: Time period to retrieve data for [hour | day | week].
            (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.traffic_history.interface.get(interface='value',
            time_period='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["interface"] = interface
        params["time_period"] = time_period
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/traffic-history/interface", params=params
        )


class TopApplications:
    """TopApplications operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TopApplications endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        time_period: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve top FortiView applications traffic stats by bandwidth.

        Args:
            time_period: Time period to retrieve data for [hour | day | week].
            (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.traffic_history.top_applications.get(time_period='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["time_period"] = time_period
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/system/traffic-history/top-applications",
            params=params,
        )


class TrafficHistory:
    """TrafficHistory operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TrafficHistory endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.enable_app_bandwidth_tracking = EnableAppBandwidthTracking(client)
        self.interface = Interface(client)
        self.top_applications = TopApplications(client)

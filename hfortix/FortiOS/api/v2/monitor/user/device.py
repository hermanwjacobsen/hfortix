"""
FortiOS MONITOR - Monitor User Device

Monitoring endpoint for monitor user device data.

API Endpoints:
    GET    /monitor/user/device

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.device.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.device.get(
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


class IotQuery:
    """
    Iotquery Operations.

    Provides read-only access for FortiOS iotquery data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize IotQuery endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mac: str,
        ip: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve IoT/OT information for a given device from user device store.

        Args:
            mac: Main MAC address of the device. (required)
            ip: IP address of the device. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.device.iot_query.get(mac='value',
            ip='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mac"] = mac
        params["ip"] = ip
        params.update(kwargs)
        return self._client.get(
            "monitor", "/user/device/iot-query", params=params
        )


class PurdueLevel:
    """PurdueLevel operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PurdueLevel endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mac: str | None = None,
        ip: str | None = None,
        level: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update the Purdue level of device from device store.

        Args:
            mac: Main MAC address of the device. (optional)
            ip: IP address of the device. (optional)
            level: Purdue level of the device [1|1.5|2|2.5|3|3.5|4|5|5.5].
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.device.purdue_level.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mac is not None:
            data["mac"] = mac
        if ip is not None:
            data["ip"] = ip
        if level is not None:
            data["level"] = level
        data.update(kwargs)
        return self._client.post(
            "monitor", "/user/device/purdue-level", data=data
        )


class Query:
    """Query operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Query endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        timestamp_from: int | None = None,
        timestamp_to: int | None = None,
        filters: list | None = None,
        query_type: str | None = None,
        view_type: str | None = None,
        query_id: int | None = None,
        cache_query: bool | None = None,
        key_only: bool | None = None,
        filter_logic: str | None = None,
        total_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve user devices from user device store.

        Args:
            timestamp_from: To get entries since the timestamp for unified
            historical query. (optional)
            timestamp_to: To get entries before the timestamp for unified
            historical query. (optional)
            filters: A list of filters. Type:{"type": string, "value": string,
            "op": string}. Op: filter operator
            [exact|contains|greaterThanEqualTo|lessThanEqualTo]. Default is
            exact. (optional)
            query_type: Query type [latest|unified_latest|unified_history].
            Default is latest. (optional)
            view_type: View type
            [device|fortiswitch_client|forticlient|iot_vuln_info]. Default is
            device. (optional)
            query_id: Provide a query ID to continue getting data for that
            unified request. Only available for unified query types. (optional)
            cache_query: Cache query result for 5 mins and return query ID.
            Only available for unified query types. Default is false.
            (optional)
            key_only: Return primary key fields only. Default is false.
            (optional)
            filter_logic: The logic between filters [and|or]). Default is and.
            (optional)
            total_only: Whether the query should return just the total number
            of devices present. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.device.query.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if timestamp_from is not None:
            params["timestamp_from"] = timestamp_from
        if timestamp_to is not None:
            params["timestamp_to"] = timestamp_to
        if filters is not None:
            params["filters"] = filters
        if query_type is not None:
            params["query_type"] = query_type
        if view_type is not None:
            params["view_type"] = view_type
        if query_id is not None:
            params["query_id"] = query_id
        if cache_query is not None:
            params["cache_query"] = cache_query
        if key_only is not None:
            params["key_only"] = key_only
        if filter_logic is not None:
            params["filter_logic"] = filter_logic
        if total_only is not None:
            params["total_only"] = total_only
        params.update(kwargs)
        return self._client.get("monitor", "/user/device/query", params=params)


class Stats:
    """Stats operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Stats endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        stat_key: str,
        timestamp_to: int,
        stat_query_type: str | None = None,
        timestamp_from: int | None = None,
        filters: list | None = None,
        filter_logic: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve user devices stats from device store by given stat item.

        Args:
            stat_key: key of the stats count on
            [os_name|hardware_type|detected_interface|is_online|max_vuln_level|fortiswitch_id|fortiswitch_port_name].
            fortiswitch_id and fortiswitch_port_name only for
            fortiswitch_client stats query type (required)
            timestamp_to: To get entries before the timestamp for stats query.
            (required)
            stat_query_type: Stat query type
            [device|fortiswitch_client|forticlient]. Default is device.
            (optional)
            timestamp_from: To get entries since the timestamp for stats query.
            (optional)
            filters: A list of filters. Type:{"type": string, "value": string,
            "op": string}. Only is_online type is supported. Op: filter
            operator [exact|contains]. Default is exact. (optional)
            filter_logic: The logic between filters [and|or]). Default is and.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.device.stats.get(stat_key='value',
            timestamp_to=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["stat-key"] = stat_key
        params["timestamp_to"] = timestamp_to
        if stat_query_type is not None:
            params["stat-query-type"] = stat_query_type
        if timestamp_from is not None:
            params["timestamp_from"] = timestamp_from
        if filters is not None:
            params["filters"] = filters
        if filter_logic is not None:
            params["filter_logic"] = filter_logic
        params.update(kwargs)
        return self._client.get("monitor", "/user/device/stats", params=params)


class Device:
    """Device operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Device endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.iot_query = IotQuery(client)
        self.purdue_level = PurdueLevel(client)
        self.query = Query(client)
        self.stats = Stats(client)

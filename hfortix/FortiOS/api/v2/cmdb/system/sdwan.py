"""
FortiOS CMDB - Cmdb System Sdwan

Configuration endpoint for managing cmdb system sdwan objects.

API Endpoints:
    GET    /cmdb/system/sdwan
    PUT    /cmdb/system/sdwan/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.sdwan.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.sdwan.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.sdwan.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.sdwan.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.sdwan.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Sdwan:
    """
    Sdwan Operations.

    Provides CRUD operations for FortiOS sdwan configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Sdwan endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/system/sdwan"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        load_balance_mode: str | None = None,
        speedtest_bypass_routing: str | None = None,
        duplication_max_num: int | None = None,
        duplication_max_discrepancy: int | None = None,
        neighbor_hold_down: str | None = None,
        neighbor_hold_down_time: int | None = None,
        app_perf_log_period: int | None = None,
        neighbor_hold_boot_time: int | None = None,
        fail_detect: str | None = None,
        fail_alert_interfaces: list | None = None,
        zone: list | None = None,
        members: list | None = None,
        health_check: list | None = None,
        service: list | None = None,
        neighbor: list | None = None,
        duplication: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            status: Enable/disable SD-WAN. (optional)
            load_balance_mode: Algorithm or mode to use for load balancing
            Internet traffic to SD-WAN members. (optional)
            speedtest_bypass_routing: Enable/disable bypass routing when
            speedtest on a SD-WAN member. (optional)
            duplication_max_num: Maximum number of interface members a packet
            is duplicated in the SD-WAN zone (2 - 4, default = 2; if set to 3,
            the original packet plus 2 more copies are created). (optional)
            duplication_max_discrepancy: Maximum discrepancy between two
            packets for deduplication in milliseconds (250 - 1000, default =
            250). (optional)
            neighbor_hold_down: Enable/disable hold switching from the
            secondary neighbor to the primary neighbor. (optional)
            neighbor_hold_down_time: Waiting period in seconds when switching
            from the secondary neighbor to the primary neighbor when hold-down
            is disabled. (0 - 10000000, default = 0). (optional)
            app_perf_log_period: Time interval in seconds that application
            performance logs are generated (0 - 3600, default = 0). (optional)
            neighbor_hold_boot_time: Waiting period in seconds when switching
            from the primary neighbor to the secondary neighbor from the
            neighbor start. (0 - 10000000, default = 0). (optional)
            fail_detect: Enable/disable SD-WAN Internet connection status
            checking (failure detection). (optional)
            fail_alert_interfaces: Physical interfaces that will be alerted.
            (optional)
            zone: Configure SD-WAN zones. (optional)
            members: FortiGate interfaces added to the SD-WAN. (optional)
            health_check: SD-WAN status checking or health checking. Identify a
            server on the Internet and determine how SD-WAN verifies that the
            FortiGate can communicate with it. (optional)
            service: Create SD-WAN rules (also called services) to control how
            sessions are distributed to interfaces in the SD-WAN. (optional)
            neighbor: Create SD-WAN neighbor from BGP neighbor table to control
            route advertisements according to SLA status. (optional)
            duplication: Create SD-WAN duplication rule. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/system/sdwan"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if load_balance_mode is not None:
            data_payload["load-balance-mode"] = load_balance_mode
        if speedtest_bypass_routing is not None:
            data_payload["speedtest-bypass-routing"] = speedtest_bypass_routing
        if duplication_max_num is not None:
            data_payload["duplication-max-num"] = duplication_max_num
        if duplication_max_discrepancy is not None:
            data_payload["duplication-max-discrepancy"] = (
                duplication_max_discrepancy
            )
        if neighbor_hold_down is not None:
            data_payload["neighbor-hold-down"] = neighbor_hold_down
        if neighbor_hold_down_time is not None:
            data_payload["neighbor-hold-down-time"] = neighbor_hold_down_time
        if app_perf_log_period is not None:
            data_payload["app-perf-log-period"] = app_perf_log_period
        if neighbor_hold_boot_time is not None:
            data_payload["neighbor-hold-boot-time"] = neighbor_hold_boot_time
        if fail_detect is not None:
            data_payload["fail-detect"] = fail_detect
        if fail_alert_interfaces is not None:
            data_payload["fail-alert-interfaces"] = fail_alert_interfaces
        if zone is not None:
            data_payload["zone"] = zone
        if members is not None:
            data_payload["members"] = members
        if health_check is not None:
            data_payload["health-check"] = health_check
        if service is not None:
            data_payload["service"] = service
        if neighbor is not None:
            data_payload["neighbor"] = neighbor
        if duplication is not None:
            data_payload["duplication"] = duplication
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

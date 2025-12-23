"""
FortiOS CMDB - Cmdb Switch Controller Flow Tracking

Configuration endpoint for managing cmdb switch controller flow tracking
objects.

API Endpoints:
    GET    /cmdb/switch-controller/flow_tracking
    PUT    /cmdb/switch-controller/flow_tracking/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.flow_tracking.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller.flow_tracking.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.flow_tracking.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.flow_tracking.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.flow_tracking.delete(name="item_name")

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


class FlowTracking:
    """
    Flowtracking Operations.

    Provides CRUD operations for FortiOS flowtracking configuration.

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
        Initialize FlowTracking endpoint.

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
        endpoint = "/switch-controller/flow-tracking"
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
        sample_mode: str | None = None,
        sample_rate: int | None = None,
        collectors: list | None = None,
        level: str | None = None,
        max_export_pkt_size: int | None = None,
        template_export_period: int | None = None,
        timeout_general: int | None = None,
        timeout_icmp: int | None = None,
        timeout_max: int | None = None,
        timeout_tcp: int | None = None,
        timeout_tcp_fin: int | None = None,
        timeout_tcp_rst: int | None = None,
        timeout_udp: int | None = None,
        aggregates: list | None = None,
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
            sample_mode: Configure sample mode for the flow tracking.
            (optional)
            sample_rate: Configure sample rate for the perimeter and
            device-ingress sampling(0 - 99999). (optional)
            collectors: Configure collectors for the flow. (optional)
            level: Configure flow tracking level. (optional)
            max_export_pkt_size: Configure flow max export packet size
            (512-9216, default=512 bytes). (optional)
            template_export_period: Configure template export period (1-60,
            default=5 minutes). (optional)
            timeout_general: Configure flow session general timeout (60-604800,
            default=3600 seconds). (optional)
            timeout_icmp: Configure flow session ICMP timeout (60-604800,
            default=300 seconds). (optional)
            timeout_max: Configure flow session max timeout (60-604800,
            default=604800 seconds). (optional)
            timeout_tcp: Configure flow session TCP timeout (60-604800,
            default=3600 seconds). (optional)
            timeout_tcp_fin: Configure flow session TCP FIN timeout (60-604800,
            default=300 seconds). (optional)
            timeout_tcp_rst: Configure flow session TCP RST timeout (60-604800,
            default=120 seconds). (optional)
            timeout_udp: Configure flow session UDP timeout (60-604800,
            default=300 seconds). (optional)
            aggregates: Configure aggregates in which all traffic sessions
            matching the IP Address will be grouped into the same flow.
            (optional)
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
        endpoint = "/switch-controller/flow-tracking"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if sample_mode is not None:
            data_payload["sample-mode"] = sample_mode
        if sample_rate is not None:
            data_payload["sample-rate"] = sample_rate
        if collectors is not None:
            data_payload["collectors"] = collectors
        if level is not None:
            data_payload["level"] = level
        if max_export_pkt_size is not None:
            data_payload["max-export-pkt-size"] = max_export_pkt_size
        if template_export_period is not None:
            data_payload["template-export-period"] = template_export_period
        if timeout_general is not None:
            data_payload["timeout-general"] = timeout_general
        if timeout_icmp is not None:
            data_payload["timeout-icmp"] = timeout_icmp
        if timeout_max is not None:
            data_payload["timeout-max"] = timeout_max
        if timeout_tcp is not None:
            data_payload["timeout-tcp"] = timeout_tcp
        if timeout_tcp_fin is not None:
            data_payload["timeout-tcp-fin"] = timeout_tcp_fin
        if timeout_tcp_rst is not None:
            data_payload["timeout-tcp-rst"] = timeout_tcp_rst
        if timeout_udp is not None:
            data_payload["timeout-udp"] = timeout_udp
        if aggregates is not None:
            data_payload["aggregates"] = aggregates
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

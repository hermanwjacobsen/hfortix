"""
FortiOS CMDB - Cmdb Router Ospf6

Configuration endpoint for managing cmdb router ospf6 objects.

API Endpoints:
    GET    /cmdb/router/ospf6
    PUT    /cmdb/router/ospf6/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router.ospf6.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.router.ospf6.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.router.ospf6.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.router.ospf6.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.router.ospf6.delete(name="item_name")

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


class Ospf6:
    """
    Ospf6 Operations.

    Provides CRUD operations for FortiOS ospf6 configuration.

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
        Initialize Ospf6 endpoint.

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
        endpoint = "/router/ospf6"
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
        abr_type: str | None = None,
        auto_cost_ref_bandwidth: int | None = None,
        default_information_originate: str | None = None,
        log_neighbour_changes: str | None = None,
        default_information_metric: int | None = None,
        default_information_metric_type: str | None = None,
        default_information_route_map: str | None = None,
        default_metric: int | None = None,
        router_id: str | None = None,
        spf_timers: str | None = None,
        bfd: str | None = None,
        restart_mode: str | None = None,
        restart_period: int | None = None,
        restart_on_topology_change: str | None = None,
        area: list | None = None,
        ospf6_interface: list | None = None,
        redistribute: list | None = None,
        passive_interface: list | None = None,
        summary_address: list | None = None,
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
            abr_type: Area border router type. (optional)
            auto_cost_ref_bandwidth: Reference bandwidth in terms of megabits
            per second. (optional)
            default_information_originate: Enable/disable generation of default
            route. (optional)
            log_neighbour_changes: Log OSPFv3 neighbor changes. (optional)
            default_information_metric: Default information metric. (optional)
            default_information_metric_type: Default information metric type.
            (optional)
            default_information_route_map: Default information route map.
            (optional)
            default_metric: Default metric of redistribute routes. (optional)
            router_id: A.B.C.D, in IPv4 address format. (optional)
            spf_timers: SPF calculation frequency. (optional)
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD).
            (optional)
            restart_mode: OSPFv3 restart mode (graceful or none). (optional)
            restart_period: Graceful restart period in seconds. (optional)
            restart_on_topology_change: Enable/disable continuing graceful
            restart upon topology change. (optional)
            area: OSPF6 area configuration. (optional)
            ospf6_interface: OSPF6 interface configuration. (optional)
            redistribute: Redistribute configuration. (optional)
            passive_interface: Passive interface configuration. (optional)
            summary_address: IPv6 address summary configuration. (optional)
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
        endpoint = "/router/ospf6"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if abr_type is not None:
            data_payload["abr-type"] = abr_type
        if auto_cost_ref_bandwidth is not None:
            data_payload["auto-cost-ref-bandwidth"] = auto_cost_ref_bandwidth
        if default_information_originate is not None:
            data_payload["default-information-originate"] = (
                default_information_originate
            )
        if log_neighbour_changes is not None:
            data_payload["log-neighbour-changes"] = log_neighbour_changes
        if default_information_metric is not None:
            data_payload["default-information-metric"] = (
                default_information_metric
            )
        if default_information_metric_type is not None:
            data_payload["default-information-metric-type"] = (
                default_information_metric_type
            )
        if default_information_route_map is not None:
            data_payload["default-information-route-map"] = (
                default_information_route_map
            )
        if default_metric is not None:
            data_payload["default-metric"] = default_metric
        if router_id is not None:
            data_payload["router-id"] = router_id
        if spf_timers is not None:
            data_payload["spf-timers"] = spf_timers
        if bfd is not None:
            data_payload["bfd"] = bfd
        if restart_mode is not None:
            data_payload["restart-mode"] = restart_mode
        if restart_period is not None:
            data_payload["restart-period"] = restart_period
        if restart_on_topology_change is not None:
            data_payload["restart-on-topology-change"] = (
                restart_on_topology_change
            )
        if area is not None:
            data_payload["area"] = area
        if ospf6_interface is not None:
            data_payload["ospf6-interface"] = ospf6_interface
        if redistribute is not None:
            data_payload["redistribute"] = redistribute
        if passive_interface is not None:
            data_payload["passive-interface"] = passive_interface
        if summary_address is not None:
            data_payload["summary-address"] = summary_address
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

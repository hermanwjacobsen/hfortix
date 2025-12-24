"""
FortiOS CMDB - Cmdb Wireless Controller Hotspot20 H2qp Wan Metric

Configuration endpoint for managing cmdb wireless controller hotspot20 h2qp wan
metric objects.

API Endpoints:
    GET    /cmdb/wireless-controller/hotspot20_h2qp_wan_metric
    POST   /cmdb/wireless-controller/hotspot20_h2qp_wan_metric
    GET    /cmdb/wireless-controller/hotspot20_h2qp_wan_metric
    PUT    /cmdb/wireless-controller/hotspot20_h2qp_wan_metric/{identifier}
    DELETE /cmdb/wireless-controller/hotspot20_h2qp_wan_metric/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_wan_metric.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_wan_metric.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_wan_metric.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_wan_metric.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.hotspot20_h2qp_wan_metric.delete(name="item_name")

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


class Hotspot20H2qpWanMetric:
    """
    Hotspot20H2Qpwanmetric Operations.

    Provides CRUD operations for FortiOS hotspot20h2qpwanmetric configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Hotspot20H2qpWanMetric endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
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

        # Build endpoint path
        if name:
            endpoint = f"/wireless-controller.hotspot20/h2qp-wan-metric/{name}"
        else:
            endpoint = "/wireless-controller.hotspot20/h2qp-wan-metric"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        link_status: str | None = None,
        symmetric_wan_link: str | None = None,
        link_at_capacity: str | None = None,
        uplink_speed: int | None = None,
        downlink_speed: int | None = None,
        uplink_load: int | None = None,
        downlink_load: int | None = None,
        load_measurement_duration: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: WAN metric name. (optional)
            link_status: Link status. (optional)
            symmetric_wan_link: WAN link symmetry. (optional)
            link_at_capacity: Link at capacity. (optional)
            uplink_speed: Uplink speed (in kilobits/s). (optional)
            downlink_speed: Downlink speed (in kilobits/s). (optional)
            uplink_load: Uplink load. (optional)
            downlink_load: Downlink load. (optional)
            load_measurement_duration: Load measurement duration (in tenths of
            a second). (optional)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/wireless-controller.hotspot20/h2qp-wan-metric/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if link_status is not None:
            data_payload["link-status"] = link_status
        if symmetric_wan_link is not None:
            data_payload["symmetric-wan-link"] = symmetric_wan_link
        if link_at_capacity is not None:
            data_payload["link-at-capacity"] = link_at_capacity
        if uplink_speed is not None:
            data_payload["uplink-speed"] = uplink_speed
        if downlink_speed is not None:
            data_payload["downlink-speed"] = downlink_speed
        if uplink_load is not None:
            data_payload["uplink-load"] = uplink_load
        if downlink_load is not None:
            data_payload["downlink-load"] = downlink_load
        if load_measurement_duration is not None:
            data_payload["load-measurement-duration"] = (
                load_measurement_duration
            )
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/wireless-controller.hotspot20/h2qp-wan-metric/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        link_status: str | None = None,
        symmetric_wan_link: str | None = None,
        link_at_capacity: str | None = None,
        uplink_speed: int | None = None,
        downlink_speed: int | None = None,
        uplink_load: int | None = None,
        downlink_load: int | None = None,
        load_measurement_duration: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: WAN metric name. (optional)
            link_status: Link status. (optional)
            symmetric_wan_link: WAN link symmetry. (optional)
            link_at_capacity: Link at capacity. (optional)
            uplink_speed: Uplink speed (in kilobits/s). (optional)
            downlink_speed: Downlink speed (in kilobits/s). (optional)
            uplink_load: Uplink load. (optional)
            downlink_load: Downlink load. (optional)
            load_measurement_duration: Load measurement duration (in tenths of
            a second). (optional)
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
        endpoint = "/wireless-controller.hotspot20/h2qp-wan-metric"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if link_status is not None:
            data_payload["link-status"] = link_status
        if symmetric_wan_link is not None:
            data_payload["symmetric-wan-link"] = symmetric_wan_link
        if link_at_capacity is not None:
            data_payload["link-at-capacity"] = link_at_capacity
        if uplink_speed is not None:
            data_payload["uplink-speed"] = uplink_speed
        if downlink_speed is not None:
            data_payload["downlink-speed"] = downlink_speed
        if uplink_load is not None:
            data_payload["uplink-load"] = uplink_load
        if downlink_load is not None:
            data_payload["downlink-load"] = downlink_load
        if load_measurement_duration is not None:
            data_payload["load-measurement-duration"] = (
                load_measurement_duration
            )
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

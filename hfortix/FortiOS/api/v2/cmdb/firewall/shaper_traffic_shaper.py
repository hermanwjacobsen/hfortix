"""
FortiOS CMDB - Cmdb Firewall Shaper Traffic Shaper

Configuration endpoint for managing cmdb firewall shaper traffic shaper
objects.

API Endpoints:
    GET    /cmdb/firewall/shaper_traffic_shaper
    POST   /cmdb/firewall/shaper_traffic_shaper
    GET    /cmdb/firewall/shaper_traffic_shaper
    PUT    /cmdb/firewall/shaper_traffic_shaper/{identifier}
    DELETE /cmdb/firewall/shaper_traffic_shaper/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.shaper_traffic_shaper.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.firewall.shaper_traffic_shaper.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.shaper_traffic_shaper.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.shaper_traffic_shaper.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.firewall.shaper_traffic_shaper.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class ShaperTrafficShaper:
    """
    Shapertrafficshaper Operations.

    Provides CRUD operations for FortiOS shapertrafficshaper configuration.

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
        Initialize ShaperTrafficShaper endpoint.

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
            endpoint = f"/firewall.shaper/traffic-shaper/{name}"
        else:
            endpoint = "/firewall.shaper/traffic-shaper"
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
        guaranteed_bandwidth: int | None = None,
        maximum_bandwidth: int | None = None,
        bandwidth_unit: str | None = None,
        priority: str | None = None,
        per_policy: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        dscp_marking_method: str | None = None,
        exceed_bandwidth: int | None = None,
        exceed_dscp: str | None = None,
        maximum_dscp: str | None = None,
        cos_marking: str | None = None,
        cos_marking_method: str | None = None,
        cos: str | None = None,
        exceed_cos: str | None = None,
        maximum_cos: str | None = None,
        overhead: int | None = None,
        exceed_class_id: int | None = None,
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
            name: Traffic shaper name. (optional)
            guaranteed_bandwidth: Amount of bandwidth guaranteed for this
            shaper (0 - 80000000). Units depend on the bandwidth-unit setting.
            (optional)
            maximum_bandwidth: Upper bandwidth limit enforced by this shaper (0
            - 80000000). 0 means no limit. Units depend on the bandwidth-unit
            setting. (optional)
            bandwidth_unit: Unit of measurement for guaranteed and maximum
            bandwidth for this shaper (Kbps, Mbps or Gbps). (optional)
            priority: Higher priority traffic is more likely to be forwarded
            without delays and without compromising the guaranteed bandwidth.
            (optional)
            per_policy: Enable/disable applying a separate shaper for each
            policy. For example, if enabled the guaranteed bandwidth is applied
            separately for each policy. (optional)
            diffserv: Enable/disable changing the DiffServ setting applied to
            traffic accepted by this shaper. (optional)
            diffservcode: DiffServ setting to be applied to traffic accepted by
            this shaper. (optional)
            dscp_marking_method: Select DSCP marking method. (optional)
            exceed_bandwidth: Exceed bandwidth used for DSCP/VLAN CoS
            multi-stage marking. Units depend on the bandwidth-unit setting.
            (optional)
            exceed_dscp: DSCP mark for traffic in guaranteed-bandwidth and
            exceed-bandwidth. (optional)
            maximum_dscp: DSCP mark for traffic in exceed-bandwidth and
            maximum-bandwidth. (optional)
            cos_marking: Enable/disable VLAN CoS marking. (optional)
            cos_marking_method: Select VLAN CoS marking method. (optional)
            cos: VLAN CoS mark. (optional)
            exceed_cos: VLAN CoS mark for traffic in [guaranteed-bandwidth,
            exceed-bandwidth]. (optional)
            maximum_cos: VLAN CoS mark for traffic in [exceed-bandwidth,
            maximum-bandwidth]. (optional)
            overhead: Per-packet size overhead used in rate computations.
            (optional)
            exceed_class_id: Class ID for traffic in guaranteed-bandwidth and
            maximum-bandwidth. (optional)
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
        endpoint = f"/firewall.shaper/traffic-shaper/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if guaranteed_bandwidth is not None:
            data_payload["guaranteed-bandwidth"] = guaranteed_bandwidth
        if maximum_bandwidth is not None:
            data_payload["maximum-bandwidth"] = maximum_bandwidth
        if bandwidth_unit is not None:
            data_payload["bandwidth-unit"] = bandwidth_unit
        if priority is not None:
            data_payload["priority"] = priority
        if per_policy is not None:
            data_payload["per-policy"] = per_policy
        if diffserv is not None:
            data_payload["diffserv"] = diffserv
        if diffservcode is not None:
            data_payload["diffservcode"] = diffservcode
        if dscp_marking_method is not None:
            data_payload["dscp-marking-method"] = dscp_marking_method
        if exceed_bandwidth is not None:
            data_payload["exceed-bandwidth"] = exceed_bandwidth
        if exceed_dscp is not None:
            data_payload["exceed-dscp"] = exceed_dscp
        if maximum_dscp is not None:
            data_payload["maximum-dscp"] = maximum_dscp
        if cos_marking is not None:
            data_payload["cos-marking"] = cos_marking
        if cos_marking_method is not None:
            data_payload["cos-marking-method"] = cos_marking_method
        if cos is not None:
            data_payload["cos"] = cos
        if exceed_cos is not None:
            data_payload["exceed-cos"] = exceed_cos
        if maximum_cos is not None:
            data_payload["maximum-cos"] = maximum_cos
        if overhead is not None:
            data_payload["overhead"] = overhead
        if exceed_class_id is not None:
            data_payload["exceed-class-id"] = exceed_class_id
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
        endpoint = f"/firewall.shaper/traffic-shaper/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(name=name, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        guaranteed_bandwidth: int | None = None,
        maximum_bandwidth: int | None = None,
        bandwidth_unit: str | None = None,
        priority: str | None = None,
        per_policy: str | None = None,
        diffserv: str | None = None,
        diffservcode: str | None = None,
        dscp_marking_method: str | None = None,
        exceed_bandwidth: int | None = None,
        exceed_dscp: str | None = None,
        maximum_dscp: str | None = None,
        cos_marking: str | None = None,
        cos_marking_method: str | None = None,
        cos: str | None = None,
        exceed_cos: str | None = None,
        maximum_cos: str | None = None,
        overhead: int | None = None,
        exceed_class_id: int | None = None,
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
            name: Traffic shaper name. (optional)
            guaranteed_bandwidth: Amount of bandwidth guaranteed for this
            shaper (0 - 80000000). Units depend on the bandwidth-unit setting.
            (optional)
            maximum_bandwidth: Upper bandwidth limit enforced by this shaper (0
            - 80000000). 0 means no limit. Units depend on the bandwidth-unit
            setting. (optional)
            bandwidth_unit: Unit of measurement for guaranteed and maximum
            bandwidth for this shaper (Kbps, Mbps or Gbps). (optional)
            priority: Higher priority traffic is more likely to be forwarded
            without delays and without compromising the guaranteed bandwidth.
            (optional)
            per_policy: Enable/disable applying a separate shaper for each
            policy. For example, if enabled the guaranteed bandwidth is applied
            separately for each policy. (optional)
            diffserv: Enable/disable changing the DiffServ setting applied to
            traffic accepted by this shaper. (optional)
            diffservcode: DiffServ setting to be applied to traffic accepted by
            this shaper. (optional)
            dscp_marking_method: Select DSCP marking method. (optional)
            exceed_bandwidth: Exceed bandwidth used for DSCP/VLAN CoS
            multi-stage marking. Units depend on the bandwidth-unit setting.
            (optional)
            exceed_dscp: DSCP mark for traffic in guaranteed-bandwidth and
            exceed-bandwidth. (optional)
            maximum_dscp: DSCP mark for traffic in exceed-bandwidth and
            maximum-bandwidth. (optional)
            cos_marking: Enable/disable VLAN CoS marking. (optional)
            cos_marking_method: Select VLAN CoS marking method. (optional)
            cos: VLAN CoS mark. (optional)
            exceed_cos: VLAN CoS mark for traffic in [guaranteed-bandwidth,
            exceed-bandwidth]. (optional)
            maximum_cos: VLAN CoS mark for traffic in [exceed-bandwidth,
            maximum-bandwidth]. (optional)
            overhead: Per-packet size overhead used in rate computations.
            (optional)
            exceed_class_id: Class ID for traffic in guaranteed-bandwidth and
            maximum-bandwidth. (optional)
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
        endpoint = "/firewall.shaper/traffic-shaper"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if guaranteed_bandwidth is not None:
            data_payload["guaranteed-bandwidth"] = guaranteed_bandwidth
        if maximum_bandwidth is not None:
            data_payload["maximum-bandwidth"] = maximum_bandwidth
        if bandwidth_unit is not None:
            data_payload["bandwidth-unit"] = bandwidth_unit
        if priority is not None:
            data_payload["priority"] = priority
        if per_policy is not None:
            data_payload["per-policy"] = per_policy
        if diffserv is not None:
            data_payload["diffserv"] = diffserv
        if diffservcode is not None:
            data_payload["diffservcode"] = diffservcode
        if dscp_marking_method is not None:
            data_payload["dscp-marking-method"] = dscp_marking_method
        if exceed_bandwidth is not None:
            data_payload["exceed-bandwidth"] = exceed_bandwidth
        if exceed_dscp is not None:
            data_payload["exceed-dscp"] = exceed_dscp
        if maximum_dscp is not None:
            data_payload["maximum-dscp"] = maximum_dscp
        if cos_marking is not None:
            data_payload["cos-marking"] = cos_marking
        if cos_marking_method is not None:
            data_payload["cos-marking-method"] = cos_marking_method
        if cos is not None:
            data_payload["cos"] = cos
        if exceed_cos is not None:
            data_payload["exceed-cos"] = exceed_cos
        if maximum_cos is not None:
            data_payload["maximum-cos"] = maximum_cos
        if overhead is not None:
            data_payload["overhead"] = overhead
        if exceed_class_id is not None:
            data_payload["exceed-class-id"] = exceed_class_id
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

"""
FortiOS CMDB - Cmdb Firewall Shaping Policy

Configuration endpoint for managing cmdb firewall shaping policy objects.

API Endpoints:
    GET    /cmdb/firewall/shaping_policy
    POST   /cmdb/firewall/shaping_policy
    GET    /cmdb/firewall/shaping_policy
    PUT    /cmdb/firewall/shaping_policy/{identifier}
    DELETE /cmdb/firewall/shaping_policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.shaping_policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.shaping_policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.shaping_policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.shaping_policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.shaping_policy.delete(name="item_name")

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


class ShapingPolicy:
    """
    Shapingpolicy Operations.

    Provides CRUD operations for FortiOS shapingpolicy configuration.

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
        Initialize ShapingPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/firewall/shaping-policy/{id}"
        else:
            endpoint = "/firewall/shaping-policy"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        status: str | None = None,
        ip_version: str | None = None,
        traffic_type: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        internet_service: str | None = None,
        internet_service_name: list | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: list | None = None,
        internet_service_src_group: list | None = None,
        internet_service_src_custom: list | None = None,
        internet_service_src_custom_group: list | None = None,
        internet_service_src_fortiguard: list | None = None,
        service: list | None = None,
        schedule: str | None = None,
        users: list | None = None,
        groups: list | None = None,
        application: list | None = None,
        app_category: list | None = None,
        app_group: list | None = None,
        url_category: list | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        class_id: int | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        cos_mask: str | None = None,
        cos: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            id: Shaping policy ID (0 - 4294967295). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            name: Shaping policy name. (optional)
            comment: Comments. (optional)
            status: Enable/disable this traffic shaping policy. (optional)
            ip_version: Apply this traffic shaping policy to IPv4 or IPv6
            traffic. (optional)
            traffic_type: Traffic type. (optional)
            srcaddr: IPv4 source address and address group names. (optional)
            dstaddr: IPv4 destination address and address group names.
            (optional)
            srcaddr6: IPv6 source address and address group names. (optional)
            dstaddr6: IPv6 destination address and address group names.
            (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address and service are not used.
            (optional)
            internet_service_name: Internet Service ID. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service_src: Enable/disable use of Internet Services in
            source for this policy. If enabled, source address is not used.
            (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_group: Internet Service source group name.
            (optional)
            internet_service_src_custom: Custom Internet Service source name.
            (optional)
            internet_service_src_custom_group: Custom Internet Service source
            group name. (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source
            name. (optional)
            service: Service and service group names. (optional)
            schedule: Schedule name. (optional)
            users: Apply this traffic shaping policy to individual users that
            have authenticated with the FortiGate. (optional)
            groups: Apply this traffic shaping policy to user groups that have
            authenticated with the FortiGate. (optional)
            application: IDs of one or more applications that this shaper
            applies application control traffic shaping to. (optional)
            app_category: IDs of one or more application categories that this
            shaper applies application control traffic shaping to. (optional)
            app_group: One or more application group names. (optional)
            url_category: IDs of one or more FortiGuard Web Filtering
            categories that this shaper applies traffic shaping to. (optional)
            srcintf: One or more incoming (ingress) interfaces. (optional)
            dstintf: One or more outgoing (egress) interfaces. (optional)
            tos_mask: Non-zero bit positions are used for comparison while zero
            bit positions are ignored. (optional)
            tos: ToS (Type of Service) value used for comparison. (optional)
            tos_negate: Enable negated TOS match. (optional)
            traffic_shaper: Traffic shaper to apply to traffic forwarded by the
            firewall policy. (optional)
            traffic_shaper_reverse: Traffic shaper to apply to response traffic
            received by the firewall policy. (optional)
            per_ip_shaper: Per-IP traffic shaper to apply with this policy.
            (optional)
            class_id: Traffic class ID. (optional)
            diffserv_forward: Enable to change packet's DiffServ values to the
            specified diffservcode-forward value. (optional)
            diffserv_reverse: Enable to change packet's reverse (reply)
            DiffServ values to the specified diffservcode-rev value. (optional)
            diffservcode_forward: Change packet's DiffServ to this value.
            (optional)
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this
            value. (optional)
            cos_mask: VLAN CoS evaluated bits. (optional)
            cos: VLAN CoS bit pattern. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/firewall/shaping-policy/{id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if id is not None:
            data_payload["id"] = id
        if uuid is not None:
            data_payload["uuid"] = uuid
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if status is not None:
            data_payload["status"] = status
        if ip_version is not None:
            data_payload["ip-version"] = ip_version
        if traffic_type is not None:
            data_payload["traffic-type"] = traffic_type
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_name is not None:
            data_payload["internet-service-name"] = internet_service_name
        if internet_service_group is not None:
            data_payload["internet-service-group"] = internet_service_group
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            data_payload["internet-service-custom-group"] = (
                internet_service_custom_group
            )
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if internet_service_src is not None:
            data_payload["internet-service-src"] = internet_service_src
        if internet_service_src_name is not None:
            data_payload["internet-service-src-name"] = (
                internet_service_src_name
            )
        if internet_service_src_group is not None:
            data_payload["internet-service-src-group"] = (
                internet_service_src_group
            )
        if internet_service_src_custom is not None:
            data_payload["internet-service-src-custom"] = (
                internet_service_src_custom
            )
        if internet_service_src_custom_group is not None:
            data_payload["internet-service-src-custom-group"] = (
                internet_service_src_custom_group
            )
        if internet_service_src_fortiguard is not None:
            data_payload["internet-service-src-fortiguard"] = (
                internet_service_src_fortiguard
            )
        if service is not None:
            data_payload["service"] = service
        if schedule is not None:
            data_payload["schedule"] = schedule
        if users is not None:
            data_payload["users"] = users
        if groups is not None:
            data_payload["groups"] = groups
        if application is not None:
            data_payload["application"] = application
        if app_category is not None:
            data_payload["app-category"] = app_category
        if app_group is not None:
            data_payload["app-group"] = app_group
        if url_category is not None:
            data_payload["url-category"] = url_category
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if tos_mask is not None:
            data_payload["tos-mask"] = tos_mask
        if tos is not None:
            data_payload["tos"] = tos
        if tos_negate is not None:
            data_payload["tos-negate"] = tos_negate
        if traffic_shaper is not None:
            data_payload["traffic-shaper"] = traffic_shaper
        if traffic_shaper_reverse is not None:
            data_payload["traffic-shaper-reverse"] = traffic_shaper_reverse
        if per_ip_shaper is not None:
            data_payload["per-ip-shaper"] = per_ip_shaper
        if class_id is not None:
            data_payload["class-id"] = class_id
        if diffserv_forward is not None:
            data_payload["diffserv-forward"] = diffserv_forward
        if diffserv_reverse is not None:
            data_payload["diffserv-reverse"] = diffserv_reverse
        if diffservcode_forward is not None:
            data_payload["diffservcode-forward"] = diffservcode_forward
        if diffservcode_rev is not None:
            data_payload["diffservcode-rev"] = diffservcode_rev
        if cos_mask is not None:
            data_payload["cos-mask"] = cos_mask
        if cos is not None:
            data_payload["cos"] = cos
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/firewall/shaping-policy/{id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            id: Object identifier
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
        result = self.get(id=id, vdom=vdom)

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
        id: int | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        status: str | None = None,
        ip_version: str | None = None,
        traffic_type: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        srcaddr6: list | None = None,
        dstaddr6: list | None = None,
        internet_service: str | None = None,
        internet_service_name: list | None = None,
        internet_service_group: list | None = None,
        internet_service_custom: list | None = None,
        internet_service_custom_group: list | None = None,
        internet_service_fortiguard: list | None = None,
        internet_service_src: str | None = None,
        internet_service_src_name: list | None = None,
        internet_service_src_group: list | None = None,
        internet_service_src_custom: list | None = None,
        internet_service_src_custom_group: list | None = None,
        internet_service_src_fortiguard: list | None = None,
        service: list | None = None,
        schedule: str | None = None,
        users: list | None = None,
        groups: list | None = None,
        application: list | None = None,
        app_category: list | None = None,
        app_group: list | None = None,
        url_category: list | None = None,
        srcintf: list | None = None,
        dstintf: list | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        class_id: int | None = None,
        diffserv_forward: str | None = None,
        diffserv_reverse: str | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        cos_mask: str | None = None,
        cos: str | None = None,
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
            id: Shaping policy ID (0 - 4294967295). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            name: Shaping policy name. (optional)
            comment: Comments. (optional)
            status: Enable/disable this traffic shaping policy. (optional)
            ip_version: Apply this traffic shaping policy to IPv4 or IPv6
            traffic. (optional)
            traffic_type: Traffic type. (optional)
            srcaddr: IPv4 source address and address group names. (optional)
            dstaddr: IPv4 destination address and address group names.
            (optional)
            srcaddr6: IPv6 source address and address group names. (optional)
            dstaddr6: IPv6 destination address and address group names.
            (optional)
            internet_service: Enable/disable use of Internet Services for this
            policy. If enabled, destination address and service are not used.
            (optional)
            internet_service_name: Internet Service ID. (optional)
            internet_service_group: Internet Service group name. (optional)
            internet_service_custom: Custom Internet Service name. (optional)
            internet_service_custom_group: Custom Internet Service group name.
            (optional)
            internet_service_fortiguard: FortiGuard Internet Service name.
            (optional)
            internet_service_src: Enable/disable use of Internet Services in
            source for this policy. If enabled, source address is not used.
            (optional)
            internet_service_src_name: Internet Service source name. (optional)
            internet_service_src_group: Internet Service source group name.
            (optional)
            internet_service_src_custom: Custom Internet Service source name.
            (optional)
            internet_service_src_custom_group: Custom Internet Service source
            group name. (optional)
            internet_service_src_fortiguard: FortiGuard Internet Service source
            name. (optional)
            service: Service and service group names. (optional)
            schedule: Schedule name. (optional)
            users: Apply this traffic shaping policy to individual users that
            have authenticated with the FortiGate. (optional)
            groups: Apply this traffic shaping policy to user groups that have
            authenticated with the FortiGate. (optional)
            application: IDs of one or more applications that this shaper
            applies application control traffic shaping to. (optional)
            app_category: IDs of one or more application categories that this
            shaper applies application control traffic shaping to. (optional)
            app_group: One or more application group names. (optional)
            url_category: IDs of one or more FortiGuard Web Filtering
            categories that this shaper applies traffic shaping to. (optional)
            srcintf: One or more incoming (ingress) interfaces. (optional)
            dstintf: One or more outgoing (egress) interfaces. (optional)
            tos_mask: Non-zero bit positions are used for comparison while zero
            bit positions are ignored. (optional)
            tos: ToS (Type of Service) value used for comparison. (optional)
            tos_negate: Enable negated TOS match. (optional)
            traffic_shaper: Traffic shaper to apply to traffic forwarded by the
            firewall policy. (optional)
            traffic_shaper_reverse: Traffic shaper to apply to response traffic
            received by the firewall policy. (optional)
            per_ip_shaper: Per-IP traffic shaper to apply with this policy.
            (optional)
            class_id: Traffic class ID. (optional)
            diffserv_forward: Enable to change packet's DiffServ values to the
            specified diffservcode-forward value. (optional)
            diffserv_reverse: Enable to change packet's reverse (reply)
            DiffServ values to the specified diffservcode-rev value. (optional)
            diffservcode_forward: Change packet's DiffServ to this value.
            (optional)
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this
            value. (optional)
            cos_mask: VLAN CoS evaluated bits. (optional)
            cos: VLAN CoS bit pattern. (optional)
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
        endpoint = "/firewall/shaping-policy"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if id is not None:
            data_payload["id"] = id
        if uuid is not None:
            data_payload["uuid"] = uuid
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if status is not None:
            data_payload["status"] = status
        if ip_version is not None:
            data_payload["ip-version"] = ip_version
        if traffic_type is not None:
            data_payload["traffic-type"] = traffic_type
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if srcaddr6 is not None:
            data_payload["srcaddr6"] = srcaddr6
        if dstaddr6 is not None:
            data_payload["dstaddr6"] = dstaddr6
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_name is not None:
            data_payload["internet-service-name"] = internet_service_name
        if internet_service_group is not None:
            data_payload["internet-service-group"] = internet_service_group
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_custom_group is not None:
            data_payload["internet-service-custom-group"] = (
                internet_service_custom_group
            )
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if internet_service_src is not None:
            data_payload["internet-service-src"] = internet_service_src
        if internet_service_src_name is not None:
            data_payload["internet-service-src-name"] = (
                internet_service_src_name
            )
        if internet_service_src_group is not None:
            data_payload["internet-service-src-group"] = (
                internet_service_src_group
            )
        if internet_service_src_custom is not None:
            data_payload["internet-service-src-custom"] = (
                internet_service_src_custom
            )
        if internet_service_src_custom_group is not None:
            data_payload["internet-service-src-custom-group"] = (
                internet_service_src_custom_group
            )
        if internet_service_src_fortiguard is not None:
            data_payload["internet-service-src-fortiguard"] = (
                internet_service_src_fortiguard
            )
        if service is not None:
            data_payload["service"] = service
        if schedule is not None:
            data_payload["schedule"] = schedule
        if users is not None:
            data_payload["users"] = users
        if groups is not None:
            data_payload["groups"] = groups
        if application is not None:
            data_payload["application"] = application
        if app_category is not None:
            data_payload["app-category"] = app_category
        if app_group is not None:
            data_payload["app-group"] = app_group
        if url_category is not None:
            data_payload["url-category"] = url_category
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if tos_mask is not None:
            data_payload["tos-mask"] = tos_mask
        if tos is not None:
            data_payload["tos"] = tos
        if tos_negate is not None:
            data_payload["tos-negate"] = tos_negate
        if traffic_shaper is not None:
            data_payload["traffic-shaper"] = traffic_shaper
        if traffic_shaper_reverse is not None:
            data_payload["traffic-shaper-reverse"] = traffic_shaper_reverse
        if per_ip_shaper is not None:
            data_payload["per-ip-shaper"] = per_ip_shaper
        if class_id is not None:
            data_payload["class-id"] = class_id
        if diffserv_forward is not None:
            data_payload["diffserv-forward"] = diffserv_forward
        if diffserv_reverse is not None:
            data_payload["diffserv-reverse"] = diffserv_reverse
        if diffservcode_forward is not None:
            data_payload["diffservcode-forward"] = diffservcode_forward
        if diffservcode_rev is not None:
            data_payload["diffservcode-rev"] = diffservcode_rev
        if cos_mask is not None:
            data_payload["cos-mask"] = cos_mask
        if cos is not None:
            data_payload["cos"] = cos
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

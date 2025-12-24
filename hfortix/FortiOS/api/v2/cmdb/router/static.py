"""
FortiOS CMDB - Cmdb Router Static

Configuration endpoint for managing cmdb router static objects.

API Endpoints:
    GET    /cmdb/router/static
    POST   /cmdb/router/static
    GET    /cmdb/router/static
    PUT    /cmdb/router/static/{identifier}
    DELETE /cmdb/router/static/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router.static.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.router.static.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.router.static.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.router.static.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.router.static.delete(name="item_name")

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


class Static:
    """
    Static Operations.

    Provides CRUD operations for FortiOS static configuration.

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
        Initialize Static endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        seq_num: str | None = None,
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
            seq_num: Object identifier (optional for list, required for
            specific)
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
        if seq_num:
            endpoint = f"/router/static/{seq_num}"
        else:
            endpoint = "/router/static"
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
        seq_num: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        dst: str | None = None,
        src: str | None = None,
        gateway: str | None = None,
        preferred_source: str | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        device: str | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: list | None = None,
        dstaddr: str | None = None,
        internet_service: int | None = None,
        internet_service_custom: str | None = None,
        internet_service_fortiguard: str | None = None,
        link_monitor_exempt: str | None = None,
        tag: int | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            seq_num: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            seq_num: Sequence number. (optional)
            status: Enable/disable this static route. (optional)
            dst: Destination IP and mask for this route. (optional)
            src: Source prefix for this route. (optional)
            gateway: Gateway IP for this route. (optional)
            preferred_source: Preferred source IP for this route. (optional)
            distance: Administrative distance (1 - 255). (optional)
            weight: Administrative weight (0 - 255). (optional)
            priority: Administrative priority (1 - 65535). (optional)
            device: Gateway out interface or tunnel. (optional)
            comment: Optional comments. (optional)
            blackhole: Enable/disable black hole. (optional)
            dynamic_gateway: Enable use of dynamic gateway retrieved from a
            DHCP or PPP server. (optional)
            sdwan_zone: Choose SD-WAN Zone. (optional)
            dstaddr: Name of firewall address or address group. (optional)
            internet_service: Application ID in the Internet service database.
            (optional)
            internet_service_custom: Application name in the Internet service
            custom database. (optional)
            internet_service_fortiguard: Application name in the Internet
            service fortiguard database. (optional)
            link_monitor_exempt: Enable/disable withdrawal of this static route
            when link monitor or health check is down. (optional)
            tag: Route tag. (optional)
            vrf: Virtual Routing Forwarding ID. (optional)
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD).
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

        # Build endpoint path
        if not seq_num:
            raise ValueError("seq_num is required for put()")
        endpoint = f"/router/static/{seq_num}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if seq_num is not None:
            data_payload["seq-num"] = seq_num
        if status is not None:
            data_payload["status"] = status
        if dst is not None:
            data_payload["dst"] = dst
        if src is not None:
            data_payload["src"] = src
        if gateway is not None:
            data_payload["gateway"] = gateway
        if preferred_source is not None:
            data_payload["preferred-source"] = preferred_source
        if distance is not None:
            data_payload["distance"] = distance
        if weight is not None:
            data_payload["weight"] = weight
        if priority is not None:
            data_payload["priority"] = priority
        if device is not None:
            data_payload["device"] = device
        if comment is not None:
            data_payload["comment"] = comment
        if blackhole is not None:
            data_payload["blackhole"] = blackhole
        if dynamic_gateway is not None:
            data_payload["dynamic-gateway"] = dynamic_gateway
        if sdwan_zone is not None:
            data_payload["sdwan-zone"] = sdwan_zone
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if link_monitor_exempt is not None:
            data_payload["link-monitor-exempt"] = link_monitor_exempt
        if tag is not None:
            data_payload["tag"] = tag
        if vrf is not None:
            data_payload["vr"] = vrf
        if bfd is not None:
            data_payload["bfd"] = bfd
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        seq_num: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            seq_num: Object identifier (required)
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
        if not seq_num:
            raise ValueError("seq_num is required for delete()")
        endpoint = f"/router/static/{seq_num}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        seq_num: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            seq_num: Object identifier
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
        result = self.get(seq_num=seq_num, vdom=vdom)

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
        seq_num: int | None = None,
        status: str | None = None,
        dst: str | None = None,
        src: str | None = None,
        gateway: str | None = None,
        preferred_source: str | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        device: str | None = None,
        comment: str | None = None,
        blackhole: str | None = None,
        dynamic_gateway: str | None = None,
        sdwan_zone: list | None = None,
        dstaddr: str | None = None,
        internet_service: int | None = None,
        internet_service_custom: str | None = None,
        internet_service_fortiguard: str | None = None,
        link_monitor_exempt: str | None = None,
        tag: int | None = None,
        vrf: int | None = None,
        bfd: str | None = None,
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
            seq_num: Sequence number. (optional)
            status: Enable/disable this static route. (optional)
            dst: Destination IP and mask for this route. (optional)
            src: Source prefix for this route. (optional)
            gateway: Gateway IP for this route. (optional)
            preferred_source: Preferred source IP for this route. (optional)
            distance: Administrative distance (1 - 255). (optional)
            weight: Administrative weight (0 - 255). (optional)
            priority: Administrative priority (1 - 65535). (optional)
            device: Gateway out interface or tunnel. (optional)
            comment: Optional comments. (optional)
            blackhole: Enable/disable black hole. (optional)
            dynamic_gateway: Enable use of dynamic gateway retrieved from a
            DHCP or PPP server. (optional)
            sdwan_zone: Choose SD-WAN Zone. (optional)
            dstaddr: Name of firewall address or address group. (optional)
            internet_service: Application ID in the Internet service database.
            (optional)
            internet_service_custom: Application name in the Internet service
            custom database. (optional)
            internet_service_fortiguard: Application name in the Internet
            service fortiguard database. (optional)
            link_monitor_exempt: Enable/disable withdrawal of this static route
            when link monitor or health check is down. (optional)
            tag: Route tag. (optional)
            vrf: Virtual Routing Forwarding ID. (optional)
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD).
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
        endpoint = "/router/static"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if seq_num is not None:
            data_payload["seq-num"] = seq_num
        if status is not None:
            data_payload["status"] = status
        if dst is not None:
            data_payload["dst"] = dst
        if src is not None:
            data_payload["src"] = src
        if gateway is not None:
            data_payload["gateway"] = gateway
        if preferred_source is not None:
            data_payload["preferred-source"] = preferred_source
        if distance is not None:
            data_payload["distance"] = distance
        if weight is not None:
            data_payload["weight"] = weight
        if priority is not None:
            data_payload["priority"] = priority
        if device is not None:
            data_payload["device"] = device
        if comment is not None:
            data_payload["comment"] = comment
        if blackhole is not None:
            data_payload["blackhole"] = blackhole
        if dynamic_gateway is not None:
            data_payload["dynamic-gateway"] = dynamic_gateway
        if sdwan_zone is not None:
            data_payload["sdwan-zone"] = sdwan_zone
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if internet_service is not None:
            data_payload["internet-service"] = internet_service
        if internet_service_custom is not None:
            data_payload["internet-service-custom"] = internet_service_custom
        if internet_service_fortiguard is not None:
            data_payload["internet-service-fortiguard"] = (
                internet_service_fortiguard
            )
        if link_monitor_exempt is not None:
            data_payload["link-monitor-exempt"] = link_monitor_exempt
        if tag is not None:
            data_payload["tag"] = tag
        if vrf is not None:
            data_payload["vr"] = vrf
        if bfd is not None:
            data_payload["bfd"] = bfd
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

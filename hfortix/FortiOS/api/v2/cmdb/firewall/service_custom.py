"""
FortiOS CMDB - Cmdb Firewall Service Custom

Configuration endpoint for managing cmdb firewall service custom objects.

API Endpoints:
    GET    /cmdb/firewall/service_custom
    POST   /cmdb/firewall/service_custom
    GET    /cmdb/firewall/service_custom
    PUT    /cmdb/firewall/service_custom/{identifier}
    DELETE /cmdb/firewall/service_custom/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.service_custom.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.service_custom.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.service_custom.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.service_custom.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.service_custom.delete(name="item_name")

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


class ServiceCustom:
    """
    Servicecustom Operations.

    Provides CRUD operations for FortiOS servicecustom configuration.

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
        Initialize ServiceCustom endpoint.

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
            endpoint = f"/firewall.service/custom/{name}"
        else:
            endpoint = "/firewall.service/custom"
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
        uuid: str | None = None,
        proxy: str | None = None,
        category: str | None = None,
        protocol: str | None = None,
        helper: str | None = None,
        iprange: str | None = None,
        fqdn: str | None = None,
        protocol_number: int | None = None,
        icmptype: int | None = None,
        icmpcode: int | None = None,
        tcp_portrange: str | None = None,
        udp_portrange: str | None = None,
        udplite_portrange: str | None = None,
        sctp_portrange: str | None = None,
        tcp_halfclose_timer: int | None = None,
        tcp_halfopen_timer: int | None = None,
        tcp_timewait_timer: int | None = None,
        tcp_rst_timer: int | None = None,
        udp_idle_timer: int | None = None,
        session_ttl: str | None = None,
        check_reset_range: str | None = None,
        comment: str | None = None,
        color: int | None = None,
        app_service_type: str | None = None,
        app_category: list | None = None,
        application: list | None = None,
        fabric_object: str | None = None,
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
            name: Custom service name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            proxy: Enable/disable web proxy service. (optional)
            category: Service category. (optional)
            protocol: Protocol type based on IANA numbers. (optional)
            helper: Helper name. (optional)
            iprange: Start and end of the IP range associated with service.
            (optional)
            fqdn: Fully qualified domain name. (optional)
            protocol_number: IP protocol number. (optional)
            icmptype: ICMP type. (optional)
            icmpcode: ICMP code. (optional)
            tcp_portrange: Multiple TCP port ranges. (optional)
            udp_portrange: Multiple UDP port ranges. (optional)
            udplite_portrange: Multiple UDP-Lite port ranges. (optional)
            sctp_portrange: Multiple SCTP port ranges. (optional)
            tcp_halfclose_timer: Wait time to close a TCP session waiting for
            an unanswered FIN packet (1 - 86400 sec, 0 = default). (optional)
            tcp_halfopen_timer: Wait time to close a TCP session waiting for an
            unanswered open session packet (1 - 86400 sec, 0 = default).
            (optional)
            tcp_timewait_timer: Set the length of the TCP TIME-WAIT state in
            seconds (1 - 300 sec, 0 = default). (optional)
            tcp_rst_timer: Set the length of the TCP CLOSE state in seconds (5
            - 300 sec, 0 = default). (optional)
            udp_idle_timer: Number of seconds before an idle UDP/UDP-Lite
            connection times out (0 - 86400 sec, 0 = default). (optional)
            session_ttl: Session TTL (300 - 2764800, 0 = default). (optional)
            check_reset_range: Configure the type of ICMP error message
            verification. (optional)
            comment: Comment. (optional)
            color: Color of icon on the GUI. (optional)
            app_service_type: Application service type. (optional)
            app_category: Application category ID. (optional)
            application: Application ID. (optional)
            fabric_object: Security Fabric global object setting. (optional)
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
        endpoint = f"/firewall.service/custom/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if proxy is not None:
            data_payload["proxy"] = proxy
        if category is not None:
            data_payload["category"] = category
        if protocol is not None:
            data_payload["protocol"] = protocol
        if helper is not None:
            data_payload["helper"] = helper
        if iprange is not None:
            data_payload["iprange"] = iprange
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if protocol_number is not None:
            data_payload["protocol-number"] = protocol_number
        if icmptype is not None:
            data_payload["icmptype"] = icmptype
        if icmpcode is not None:
            data_payload["icmpcode"] = icmpcode
        if tcp_portrange is not None:
            data_payload["tcp-portrange"] = tcp_portrange
        if udp_portrange is not None:
            data_payload["udp-portrange"] = udp_portrange
        if udplite_portrange is not None:
            data_payload["udplite-portrange"] = udplite_portrange
        if sctp_portrange is not None:
            data_payload["sctp-portrange"] = sctp_portrange
        if tcp_halfclose_timer is not None:
            data_payload["tcp-halfclose-timer"] = tcp_halfclose_timer
        if tcp_halfopen_timer is not None:
            data_payload["tcp-halfopen-timer"] = tcp_halfopen_timer
        if tcp_timewait_timer is not None:
            data_payload["tcp-timewait-timer"] = tcp_timewait_timer
        if tcp_rst_timer is not None:
            data_payload["tcp-rst-timer"] = tcp_rst_timer
        if udp_idle_timer is not None:
            data_payload["udp-idle-timer"] = udp_idle_timer
        if session_ttl is not None:
            data_payload["session-ttl"] = session_ttl
        if check_reset_range is not None:
            data_payload["check-reset-range"] = check_reset_range
        if comment is not None:
            data_payload["comment"] = comment
        if color is not None:
            data_payload["color"] = color
        if app_service_type is not None:
            data_payload["app-service-type"] = app_service_type
        if app_category is not None:
            data_payload["app-category"] = app_category
        if application is not None:
            data_payload["application"] = application
        if fabric_object is not None:
            data_payload["fabric-object"] = fabric_object
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
        endpoint = f"/firewall.service/custom/{name}"
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
        uuid: str | None = None,
        proxy: str | None = None,
        category: str | None = None,
        protocol: str | None = None,
        helper: str | None = None,
        iprange: str | None = None,
        fqdn: str | None = None,
        protocol_number: int | None = None,
        icmptype: int | None = None,
        icmpcode: int | None = None,
        tcp_portrange: str | None = None,
        udp_portrange: str | None = None,
        udplite_portrange: str | None = None,
        sctp_portrange: str | None = None,
        tcp_halfclose_timer: int | None = None,
        tcp_halfopen_timer: int | None = None,
        tcp_timewait_timer: int | None = None,
        tcp_rst_timer: int | None = None,
        udp_idle_timer: int | None = None,
        session_ttl: str | None = None,
        check_reset_range: str | None = None,
        comment: str | None = None,
        color: int | None = None,
        app_service_type: str | None = None,
        app_category: list | None = None,
        application: list | None = None,
        fabric_object: str | None = None,
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
            name: Custom service name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            proxy: Enable/disable web proxy service. (optional)
            category: Service category. (optional)
            protocol: Protocol type based on IANA numbers. (optional)
            helper: Helper name. (optional)
            iprange: Start and end of the IP range associated with service.
            (optional)
            fqdn: Fully qualified domain name. (optional)
            protocol_number: IP protocol number. (optional)
            icmptype: ICMP type. (optional)
            icmpcode: ICMP code. (optional)
            tcp_portrange: Multiple TCP port ranges. (optional)
            udp_portrange: Multiple UDP port ranges. (optional)
            udplite_portrange: Multiple UDP-Lite port ranges. (optional)
            sctp_portrange: Multiple SCTP port ranges. (optional)
            tcp_halfclose_timer: Wait time to close a TCP session waiting for
            an unanswered FIN packet (1 - 86400 sec, 0 = default). (optional)
            tcp_halfopen_timer: Wait time to close a TCP session waiting for an
            unanswered open session packet (1 - 86400 sec, 0 = default).
            (optional)
            tcp_timewait_timer: Set the length of the TCP TIME-WAIT state in
            seconds (1 - 300 sec, 0 = default). (optional)
            tcp_rst_timer: Set the length of the TCP CLOSE state in seconds (5
            - 300 sec, 0 = default). (optional)
            udp_idle_timer: Number of seconds before an idle UDP/UDP-Lite
            connection times out (0 - 86400 sec, 0 = default). (optional)
            session_ttl: Session TTL (300 - 2764800, 0 = default). (optional)
            check_reset_range: Configure the type of ICMP error message
            verification. (optional)
            comment: Comment. (optional)
            color: Color of icon on the GUI. (optional)
            app_service_type: Application service type. (optional)
            app_category: Application category ID. (optional)
            application: Application ID. (optional)
            fabric_object: Security Fabric global object setting. (optional)
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
        endpoint = "/firewall.service/custom"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if proxy is not None:
            data_payload["proxy"] = proxy
        if category is not None:
            data_payload["category"] = category
        if protocol is not None:
            data_payload["protocol"] = protocol
        if helper is not None:
            data_payload["helper"] = helper
        if iprange is not None:
            data_payload["iprange"] = iprange
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if protocol_number is not None:
            data_payload["protocol-number"] = protocol_number
        if icmptype is not None:
            data_payload["icmptype"] = icmptype
        if icmpcode is not None:
            data_payload["icmpcode"] = icmpcode
        if tcp_portrange is not None:
            data_payload["tcp-portrange"] = tcp_portrange
        if udp_portrange is not None:
            data_payload["udp-portrange"] = udp_portrange
        if udplite_portrange is not None:
            data_payload["udplite-portrange"] = udplite_portrange
        if sctp_portrange is not None:
            data_payload["sctp-portrange"] = sctp_portrange
        if tcp_halfclose_timer is not None:
            data_payload["tcp-halfclose-timer"] = tcp_halfclose_timer
        if tcp_halfopen_timer is not None:
            data_payload["tcp-halfopen-timer"] = tcp_halfopen_timer
        if tcp_timewait_timer is not None:
            data_payload["tcp-timewait-timer"] = tcp_timewait_timer
        if tcp_rst_timer is not None:
            data_payload["tcp-rst-timer"] = tcp_rst_timer
        if udp_idle_timer is not None:
            data_payload["udp-idle-timer"] = udp_idle_timer
        if session_ttl is not None:
            data_payload["session-ttl"] = session_ttl
        if check_reset_range is not None:
            data_payload["check-reset-range"] = check_reset_range
        if comment is not None:
            data_payload["comment"] = comment
        if color is not None:
            data_payload["color"] = color
        if app_service_type is not None:
            data_payload["app-service-type"] = app_service_type
        if app_category is not None:
            data_payload["app-category"] = app_category
        if application is not None:
            data_payload["application"] = application
        if fabric_object is not None:
            data_payload["fabric-object"] = fabric_object
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

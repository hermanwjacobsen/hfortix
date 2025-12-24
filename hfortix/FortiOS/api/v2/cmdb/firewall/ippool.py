"""
FortiOS CMDB - Cmdb Firewall Ippool

Configuration endpoint for managing cmdb firewall ippool objects.

API Endpoints:
    GET    /cmdb/firewall/ippool
    POST   /cmdb/firewall/ippool
    GET    /cmdb/firewall/ippool
    PUT    /cmdb/firewall/ippool/{identifier}
    DELETE /cmdb/firewall/ippool/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.ippool.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.ippool.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.ippool.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.ippool.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.ippool.delete(name="item_name")

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


class Ippool:
    """
    Ippool Operations.

    Provides CRUD operations for FortiOS ippool configuration.

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
        Initialize Ippool endpoint.

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
            endpoint = f"/firewall/ippool/{name}"
        else:
            endpoint = "/firewall/ippool"
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
        type: str | None = None,
        startip: str | None = None,
        endip: str | None = None,
        startport: int | None = None,
        endport: int | None = None,
        source_startip: str | None = None,
        source_endip: str | None = None,
        block_size: int | None = None,
        port_per_user: int | None = None,
        num_blocks_per_user: int | None = None,
        pba_timeout: int | None = None,
        pba_interim_log: int | None = None,
        permit_any_host: str | None = None,
        arp_reply: str | None = None,
        arp_intf: str | None = None,
        associated_interface: str | None = None,
        comments: str | None = None,
        nat64: str | None = None,
        add_nat64_route: str | None = None,
        source_prefix6: str | None = None,
        client_prefix_length: int | None = None,
        tcp_session_quota: int | None = None,
        udp_session_quota: int | None = None,
        icmp_session_quota: int | None = None,
        privileged_port_use_pba: str | None = None,
        subnet_broadcast_in_ippool: str | None = None,
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
            name: IP pool name. (optional)
            type: IP pool type: overload, one-to-one, fixed-port-range,
            port-block-allocation, cgn-resource-allocation (hyperscale vdom
            only) (optional)
            startip: First IPv4 address (inclusive) in the range for the
            address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0). (optional)
            endip: Final IPv4 address (inclusive) in the range for the address
            pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0). (optional)
            startport: First port number (inclusive) in the range for the
            address pool (1024 - 65535, Default: 5117). (optional)
            endport: Final port number (inclusive) in the range for the address
            pool (1024 - 65535, Default: 65533). (optional)
            source_startip: First IPv4 address (inclusive) in the range of the
            source addresses to be translated (format = xxx.xxx.xxx.xxx,
            default = 0.0.0.0). (optional)
            source_endip: Final IPv4 address (inclusive) in the range of the
            source addresses to be translated (format xxx.xxx.xxx.xxx, Default:
            0.0.0.0). (optional)
            block_size: Number of addresses in a block (64 - 4096, default =
            128). (optional)
            port_per_user: Number of port for each user (32 - 60416, default =
            0, which is auto). (optional)
            num_blocks_per_user: Number of addresses blocks that can be used by
            a user (1 to 128, default = 8). (optional)
            pba_timeout: Port block allocation timeout (seconds). (optional)
            pba_interim_log: Port block allocation interim logging interval
            (600 - 86400 seconds, default = 0 which disables interim logging).
            (optional)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets
            from any host. (optional)
            arp_reply: Enable/disable replying to ARP requests when an IP Pool
            is added to a policy (default = enable). (optional)
            arp_intf: Select an interface from available options that will
            reply to ARP requests. (If blank, any is selected). (optional)
            associated_interface: Associated interface name. (optional)
            comments: Comment. (optional)
            nat64: Enable/disable NAT64. (optional)
            add_nat64_route: Enable/disable adding NAT64 route. (optional)
            source_prefix6: Source IPv6 network to be translated (format =
            xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx, default = ::/0).
            (optional)
            client_prefix_length: Subnet length of a single deterministic NAT64
            client (1 - 128, default = 64). (optional)
            tcp_session_quota: Maximum number of concurrent TCP sessions
            allowed per client (0 - 2097000, default = 0 which means no limit).
            (optional)
            udp_session_quota: Maximum number of concurrent UDP sessions
            allowed per client (0 - 2097000, default = 0 which means no limit).
            (optional)
            icmp_session_quota: Maximum number of concurrent ICMP sessions
            allowed per client (0 - 2097000, default = 0 which means no limit).
            (optional)
            privileged_port_use_pba: Enable/disable selection of the external
            port from the port block allocation for NAT'ing privileged ports
            (deafult = disable). (optional)
            subnet_broadcast_in_ippool: Enable/disable inclusion of the
            subnetwork address and broadcast IP address in the NAT64 IP pool.
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
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/firewall/ippool/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if startip is not None:
            data_payload["startip"] = startip
        if endip is not None:
            data_payload["endip"] = endip
        if startport is not None:
            data_payload["startport"] = startport
        if endport is not None:
            data_payload["endport"] = endport
        if source_startip is not None:
            data_payload["source-startip"] = source_startip
        if source_endip is not None:
            data_payload["source-endip"] = source_endip
        if block_size is not None:
            data_payload["block-size"] = block_size
        if port_per_user is not None:
            data_payload["port-per-user"] = port_per_user
        if num_blocks_per_user is not None:
            data_payload["num-blocks-per-user"] = num_blocks_per_user
        if pba_timeout is not None:
            data_payload["pba-timeout"] = pba_timeout
        if pba_interim_log is not None:
            data_payload["pba-interim-log"] = pba_interim_log
        if permit_any_host is not None:
            data_payload["permit-any-host"] = permit_any_host
        if arp_reply is not None:
            data_payload["arp-reply"] = arp_reply
        if arp_intf is not None:
            data_payload["arp-int"] = arp_intf
        if associated_interface is not None:
            data_payload["associated-interface"] = associated_interface
        if comments is not None:
            data_payload["comments"] = comments
        if nat64 is not None:
            data_payload["nat64"] = nat64
        if add_nat64_route is not None:
            data_payload["add-nat64-route"] = add_nat64_route
        if source_prefix6 is not None:
            data_payload["source-prefix6"] = source_prefix6
        if client_prefix_length is not None:
            data_payload["client-prefix-length"] = client_prefix_length
        if tcp_session_quota is not None:
            data_payload["tcp-session-quota"] = tcp_session_quota
        if udp_session_quota is not None:
            data_payload["udp-session-quota"] = udp_session_quota
        if icmp_session_quota is not None:
            data_payload["icmp-session-quota"] = icmp_session_quota
        if privileged_port_use_pba is not None:
            data_payload["privileged-port-use-pba"] = privileged_port_use_pba
        if subnet_broadcast_in_ippool is not None:
            data_payload["subnet-broadcast-in-ippool"] = (
                subnet_broadcast_in_ippool
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
        endpoint = f"/firewall/ippool/{name}"
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
        type: str | None = None,
        startip: str | None = None,
        endip: str | None = None,
        startport: int | None = None,
        endport: int | None = None,
        source_startip: str | None = None,
        source_endip: str | None = None,
        block_size: int | None = None,
        port_per_user: int | None = None,
        num_blocks_per_user: int | None = None,
        pba_timeout: int | None = None,
        pba_interim_log: int | None = None,
        permit_any_host: str | None = None,
        arp_reply: str | None = None,
        arp_intf: str | None = None,
        associated_interface: str | None = None,
        comments: str | None = None,
        nat64: str | None = None,
        add_nat64_route: str | None = None,
        source_prefix6: str | None = None,
        client_prefix_length: int | None = None,
        tcp_session_quota: int | None = None,
        udp_session_quota: int | None = None,
        icmp_session_quota: int | None = None,
        privileged_port_use_pba: str | None = None,
        subnet_broadcast_in_ippool: str | None = None,
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
            name: IP pool name. (optional)
            type: IP pool type: overload, one-to-one, fixed-port-range,
            port-block-allocation, cgn-resource-allocation (hyperscale vdom
            only) (optional)
            startip: First IPv4 address (inclusive) in the range for the
            address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0). (optional)
            endip: Final IPv4 address (inclusive) in the range for the address
            pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0). (optional)
            startport: First port number (inclusive) in the range for the
            address pool (1024 - 65535, Default: 5117). (optional)
            endport: Final port number (inclusive) in the range for the address
            pool (1024 - 65535, Default: 65533). (optional)
            source_startip: First IPv4 address (inclusive) in the range of the
            source addresses to be translated (format = xxx.xxx.xxx.xxx,
            default = 0.0.0.0). (optional)
            source_endip: Final IPv4 address (inclusive) in the range of the
            source addresses to be translated (format xxx.xxx.xxx.xxx, Default:
            0.0.0.0). (optional)
            block_size: Number of addresses in a block (64 - 4096, default =
            128). (optional)
            port_per_user: Number of port for each user (32 - 60416, default =
            0, which is auto). (optional)
            num_blocks_per_user: Number of addresses blocks that can be used by
            a user (1 to 128, default = 8). (optional)
            pba_timeout: Port block allocation timeout (seconds). (optional)
            pba_interim_log: Port block allocation interim logging interval
            (600 - 86400 seconds, default = 0 which disables interim logging).
            (optional)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets
            from any host. (optional)
            arp_reply: Enable/disable replying to ARP requests when an IP Pool
            is added to a policy (default = enable). (optional)
            arp_intf: Select an interface from available options that will
            reply to ARP requests. (If blank, any is selected). (optional)
            associated_interface: Associated interface name. (optional)
            comments: Comment. (optional)
            nat64: Enable/disable NAT64. (optional)
            add_nat64_route: Enable/disable adding NAT64 route. (optional)
            source_prefix6: Source IPv6 network to be translated (format =
            xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx, default = ::/0).
            (optional)
            client_prefix_length: Subnet length of a single deterministic NAT64
            client (1 - 128, default = 64). (optional)
            tcp_session_quota: Maximum number of concurrent TCP sessions
            allowed per client (0 - 2097000, default = 0 which means no limit).
            (optional)
            udp_session_quota: Maximum number of concurrent UDP sessions
            allowed per client (0 - 2097000, default = 0 which means no limit).
            (optional)
            icmp_session_quota: Maximum number of concurrent ICMP sessions
            allowed per client (0 - 2097000, default = 0 which means no limit).
            (optional)
            privileged_port_use_pba: Enable/disable selection of the external
            port from the port block allocation for NAT'ing privileged ports
            (deafult = disable). (optional)
            subnet_broadcast_in_ippool: Enable/disable inclusion of the
            subnetwork address and broadcast IP address in the NAT64 IP pool.
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
        endpoint = "/firewall/ippool"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if startip is not None:
            data_payload["startip"] = startip
        if endip is not None:
            data_payload["endip"] = endip
        if startport is not None:
            data_payload["startport"] = startport
        if endport is not None:
            data_payload["endport"] = endport
        if source_startip is not None:
            data_payload["source-startip"] = source_startip
        if source_endip is not None:
            data_payload["source-endip"] = source_endip
        if block_size is not None:
            data_payload["block-size"] = block_size
        if port_per_user is not None:
            data_payload["port-per-user"] = port_per_user
        if num_blocks_per_user is not None:
            data_payload["num-blocks-per-user"] = num_blocks_per_user
        if pba_timeout is not None:
            data_payload["pba-timeout"] = pba_timeout
        if pba_interim_log is not None:
            data_payload["pba-interim-log"] = pba_interim_log
        if permit_any_host is not None:
            data_payload["permit-any-host"] = permit_any_host
        if arp_reply is not None:
            data_payload["arp-reply"] = arp_reply
        if arp_intf is not None:
            data_payload["arp-int"] = arp_intf
        if associated_interface is not None:
            data_payload["associated-interface"] = associated_interface
        if comments is not None:
            data_payload["comments"] = comments
        if nat64 is not None:
            data_payload["nat64"] = nat64
        if add_nat64_route is not None:
            data_payload["add-nat64-route"] = add_nat64_route
        if source_prefix6 is not None:
            data_payload["source-prefix6"] = source_prefix6
        if client_prefix_length is not None:
            data_payload["client-prefix-length"] = client_prefix_length
        if tcp_session_quota is not None:
            data_payload["tcp-session-quota"] = tcp_session_quota
        if udp_session_quota is not None:
            data_payload["udp-session-quota"] = udp_session_quota
        if icmp_session_quota is not None:
            data_payload["icmp-session-quota"] = icmp_session_quota
        if privileged_port_use_pba is not None:
            data_payload["privileged-port-use-pba"] = privileged_port_use_pba
        if subnet_broadcast_in_ippool is not None:
            data_payload["subnet-broadcast-in-ippool"] = (
                subnet_broadcast_in_ippool
            )
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

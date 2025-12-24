"""
FortiOS CMDB - Cmdb System Dhcp6 Server

Configuration endpoint for managing cmdb system dhcp6 server objects.

API Endpoints:
    GET    /cmdb/system/dhcp6_server
    POST   /cmdb/system/dhcp6_server
    GET    /cmdb/system/dhcp6_server
    PUT    /cmdb/system/dhcp6_server/{identifier}
    DELETE /cmdb/system/dhcp6_server/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.dhcp6_server.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.dhcp6_server.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.dhcp6_server.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.dhcp6_server.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.dhcp6_server.delete(name="item_name")

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


class Dhcp6Server:
    """
    Dhcp6Server Operations.

    Provides CRUD operations for FortiOS dhcp6server configuration.

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
        Initialize Dhcp6Server endpoint.

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
            endpoint = f"/system.dhcp6/server/{id}"
        else:
            endpoint = "/system.dhcp6/server"
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
        status: str | None = None,
        rapid_commit: str | None = None,
        lease_time: int | None = None,
        dns_service: str | None = None,
        dns_search_list: str | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        domain: str | None = None,
        subnet: str | None = None,
        interface: str | None = None,
        delegated_prefix_route: str | None = None,
        options: list | None = None,
        upstream_interface: str | None = None,
        delegated_prefix_iaid: int | None = None,
        ip_mode: str | None = None,
        prefix_mode: str | None = None,
        prefix_range: list | None = None,
        ip_range: list | None = None,
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
            id: ID. (optional)
            status: Enable/disable this DHCPv6 configuration. (optional)
            rapid_commit: Enable/disable allow/disallow rapid commit.
            (optional)
            lease_time: Lease time in seconds, 0 means unlimited. (optional)
            dns_service: Options for assigning DNS servers to DHCPv6 clients.
            (optional)
            dns_search_list: DNS search list options. (optional)
            dns_server1: DNS server 1. (optional)
            dns_server2: DNS server 2. (optional)
            dns_server3: DNS server 3. (optional)
            dns_server4: DNS server 4. (optional)
            domain: Domain name suffix for the IP addresses that the DHCP
            server assigns to clients. (optional)
            subnet: Subnet or subnet-id if the IP mode is delegated. (optional)
            interface: DHCP server can assign IP configurations to clients
            connected to this interface. (optional)
            delegated_prefix_route: Enable/disable automatically adding of
            routing for delegated prefix. (optional)
            options: DHCPv6 options. (optional)
            upstream_interface: Interface name from where delegated information
            is provided. (optional)
            delegated_prefix_iaid: IAID of obtained delegated-prefix from the
            upstream interface. (optional)
            ip_mode: Method used to assign client IP. (optional)
            prefix_mode: Assigning a prefix from a DHCPv6 client or RA.
            (optional)
            prefix_range: DHCP prefix configuration. (optional)
            ip_range: DHCP IP range configuration. (optional)
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
        endpoint = f"/system.dhcp6/server/{id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if rapid_commit is not None:
            data_payload["rapid-commit"] = rapid_commit
        if lease_time is not None:
            data_payload["lease-time"] = lease_time
        if dns_service is not None:
            data_payload["dns-service"] = dns_service
        if dns_search_list is not None:
            data_payload["dns-search-list"] = dns_search_list
        if dns_server1 is not None:
            data_payload["dns-server1"] = dns_server1
        if dns_server2 is not None:
            data_payload["dns-server2"] = dns_server2
        if dns_server3 is not None:
            data_payload["dns-server3"] = dns_server3
        if dns_server4 is not None:
            data_payload["dns-server4"] = dns_server4
        if domain is not None:
            data_payload["domain"] = domain
        if subnet is not None:
            data_payload["subnet"] = subnet
        if interface is not None:
            data_payload["interface"] = interface
        if delegated_prefix_route is not None:
            data_payload["delegated-prefix-route"] = delegated_prefix_route
        if options is not None:
            data_payload["options"] = options
        if upstream_interface is not None:
            data_payload["upstream-interface"] = upstream_interface
        if delegated_prefix_iaid is not None:
            data_payload["delegated-prefix-iaid"] = delegated_prefix_iaid
        if ip_mode is not None:
            data_payload["ip-mode"] = ip_mode
        if prefix_mode is not None:
            data_payload["prefix-mode"] = prefix_mode
        if prefix_range is not None:
            data_payload["prefix-range"] = prefix_range
        if ip_range is not None:
            data_payload["ip-range"] = ip_range
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
        endpoint = f"/system.dhcp6/server/{id}"
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
        status: str | None = None,
        rapid_commit: str | None = None,
        lease_time: int | None = None,
        dns_service: str | None = None,
        dns_search_list: str | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        domain: str | None = None,
        subnet: str | None = None,
        interface: str | None = None,
        delegated_prefix_route: str | None = None,
        options: list | None = None,
        upstream_interface: str | None = None,
        delegated_prefix_iaid: int | None = None,
        ip_mode: str | None = None,
        prefix_mode: str | None = None,
        prefix_range: list | None = None,
        ip_range: list | None = None,
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
            id: ID. (optional)
            status: Enable/disable this DHCPv6 configuration. (optional)
            rapid_commit: Enable/disable allow/disallow rapid commit.
            (optional)
            lease_time: Lease time in seconds, 0 means unlimited. (optional)
            dns_service: Options for assigning DNS servers to DHCPv6 clients.
            (optional)
            dns_search_list: DNS search list options. (optional)
            dns_server1: DNS server 1. (optional)
            dns_server2: DNS server 2. (optional)
            dns_server3: DNS server 3. (optional)
            dns_server4: DNS server 4. (optional)
            domain: Domain name suffix for the IP addresses that the DHCP
            server assigns to clients. (optional)
            subnet: Subnet or subnet-id if the IP mode is delegated. (optional)
            interface: DHCP server can assign IP configurations to clients
            connected to this interface. (optional)
            delegated_prefix_route: Enable/disable automatically adding of
            routing for delegated prefix. (optional)
            options: DHCPv6 options. (optional)
            upstream_interface: Interface name from where delegated information
            is provided. (optional)
            delegated_prefix_iaid: IAID of obtained delegated-prefix from the
            upstream interface. (optional)
            ip_mode: Method used to assign client IP. (optional)
            prefix_mode: Assigning a prefix from a DHCPv6 client or RA.
            (optional)
            prefix_range: DHCP prefix configuration. (optional)
            ip_range: DHCP IP range configuration. (optional)
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
        endpoint = "/system.dhcp6/server"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if rapid_commit is not None:
            data_payload["rapid-commit"] = rapid_commit
        if lease_time is not None:
            data_payload["lease-time"] = lease_time
        if dns_service is not None:
            data_payload["dns-service"] = dns_service
        if dns_search_list is not None:
            data_payload["dns-search-list"] = dns_search_list
        if dns_server1 is not None:
            data_payload["dns-server1"] = dns_server1
        if dns_server2 is not None:
            data_payload["dns-server2"] = dns_server2
        if dns_server3 is not None:
            data_payload["dns-server3"] = dns_server3
        if dns_server4 is not None:
            data_payload["dns-server4"] = dns_server4
        if domain is not None:
            data_payload["domain"] = domain
        if subnet is not None:
            data_payload["subnet"] = subnet
        if interface is not None:
            data_payload["interface"] = interface
        if delegated_prefix_route is not None:
            data_payload["delegated-prefix-route"] = delegated_prefix_route
        if options is not None:
            data_payload["options"] = options
        if upstream_interface is not None:
            data_payload["upstream-interface"] = upstream_interface
        if delegated_prefix_iaid is not None:
            data_payload["delegated-prefix-iaid"] = delegated_prefix_iaid
        if ip_mode is not None:
            data_payload["ip-mode"] = ip_mode
        if prefix_mode is not None:
            data_payload["prefix-mode"] = prefix_mode
        if prefix_range is not None:
            data_payload["prefix-range"] = prefix_range
        if ip_range is not None:
            data_payload["ip-range"] = ip_range
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

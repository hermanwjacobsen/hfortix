"""
FortiOS CMDB - Cmdb Web Proxy Forward Server

Configuration endpoint for managing cmdb web proxy forward server objects.

API Endpoints:
    GET    /cmdb/web-proxy/forward_server
    POST   /cmdb/web-proxy/forward_server
    GET    /cmdb/web-proxy/forward_server
    PUT    /cmdb/web-proxy/forward_server/{identifier}
    DELETE /cmdb/web-proxy/forward_server/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.web_proxy.forward_server.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.web_proxy.forward_server.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.web_proxy.forward_server.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.web_proxy.forward_server.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.web_proxy.forward_server.delete(name="item_name")

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


class ForwardServer:
    """
    Forwardserver Operations.

    Provides CRUD operations for FortiOS forwardserver configuration.

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
        Initialize ForwardServer endpoint.

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
            endpoint = f"/web-proxy/forward-server/{name}"
        else:
            endpoint = "/web-proxy/forward-server"
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
        addr_type: str | None = None,
        ip: str | None = None,
        ipv6: str | None = None,
        fqdn: str | None = None,
        port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        comment: str | None = None,
        masquerade: str | None = None,
        healthcheck: str | None = None,
        monitor: str | None = None,
        server_down_option: str | None = None,
        username: str | None = None,
        password: str | None = None,
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
            name: Server name. (optional)
            addr_type: Address type of the forwarding proxy server: IP or FQDN.
            (optional)
            ip: Forward proxy server IP address. (optional)
            ipv6: Forward proxy server IPv6 address. (optional)
            fqdn: Forward server Fully Qualified Domain Name (FQDN). (optional)
            port: Port number that the forwarding server expects to receive
            HTTP sessions on (1 - 65535, default = 3128). (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            comment: Comment. (optional)
            masquerade: Enable/disable use of the IP address of the outgoing
            interface as the client IP address (default = enable) (optional)
            healthcheck: Enable/disable forward server health checking.
            Attempts to connect through the remote forwarding server to a
            destination to verify that the forwarding server is operating
            normally. (optional)
            monitor: URL for forward server health check monitoring (default =
            www.google.com). (optional)
            server_down_option: Action to take when the forward server is found
            to be down: block sessions until the server is back up or pass
            sessions to their destination. (optional)
            username: HTTP authentication user name. (optional)
            password: HTTP authentication password. (optional)
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
        endpoint = f"/web-proxy/forward-server/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if ip is not None:
            data_payload["ip"] = ip
        if ipv6 is not None:
            data_payload["ipv6"] = ipv6
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if port is not None:
            data_payload["port"] = port
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if comment is not None:
            data_payload["comment"] = comment
        if masquerade is not None:
            data_payload["masquerade"] = masquerade
        if healthcheck is not None:
            data_payload["healthcheck"] = healthcheck
        if monitor is not None:
            data_payload["monitor"] = monitor
        if server_down_option is not None:
            data_payload["server-down-option"] = server_down_option
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
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
        endpoint = f"/web-proxy/forward-server/{name}"
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
        addr_type: str | None = None,
        ip: str | None = None,
        ipv6: str | None = None,
        fqdn: str | None = None,
        port: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        comment: str | None = None,
        masquerade: str | None = None,
        healthcheck: str | None = None,
        monitor: str | None = None,
        server_down_option: str | None = None,
        username: str | None = None,
        password: str | None = None,
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
            name: Server name. (optional)
            addr_type: Address type of the forwarding proxy server: IP or FQDN.
            (optional)
            ip: Forward proxy server IP address. (optional)
            ipv6: Forward proxy server IPv6 address. (optional)
            fqdn: Forward server Fully Qualified Domain Name (FQDN). (optional)
            port: Port number that the forwarding server expects to receive
            HTTP sessions on (1 - 65535, default = 3128). (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            comment: Comment. (optional)
            masquerade: Enable/disable use of the IP address of the outgoing
            interface as the client IP address (default = enable) (optional)
            healthcheck: Enable/disable forward server health checking.
            Attempts to connect through the remote forwarding server to a
            destination to verify that the forwarding server is operating
            normally. (optional)
            monitor: URL for forward server health check monitoring (default =
            www.google.com). (optional)
            server_down_option: Action to take when the forward server is found
            to be down: block sessions until the server is back up or pass
            sessions to their destination. (optional)
            username: HTTP authentication user name. (optional)
            password: HTTP authentication password. (optional)
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
        endpoint = "/web-proxy/forward-server"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if ip is not None:
            data_payload["ip"] = ip
        if ipv6 is not None:
            data_payload["ipv6"] = ipv6
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if port is not None:
            data_payload["port"] = port
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if comment is not None:
            data_payload["comment"] = comment
        if masquerade is not None:
            data_payload["masquerade"] = masquerade
        if healthcheck is not None:
            data_payload["healthcheck"] = healthcheck
        if monitor is not None:
            data_payload["monitor"] = monitor
        if server_down_option is not None:
            data_payload["server-down-option"] = server_down_option
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

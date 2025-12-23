"""
FortiOS CMDB - Cmdb System Wccp

Configuration endpoint for managing cmdb system wccp objects.

API Endpoints:
    GET    /cmdb/system/wccp
    POST   /cmdb/system/wccp
    GET    /cmdb/system/wccp
    PUT    /cmdb/system/wccp/{identifier}
    DELETE /cmdb/system/wccp/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.wccp.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.wccp.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.wccp.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.wccp.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.wccp.delete(name="item_name")

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


class Wccp:
    """
    Wccp Operations.

    Provides CRUD operations for FortiOS wccp configuration.

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
        Initialize Wccp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        service_id: str | None = None,
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
            service_id: Object identifier (optional for list, required for
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
        if service_id:
            endpoint = f"/system/wccp/{service_id}"
        else:
            endpoint = "/system/wccp"
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
        service_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        router_id: str | None = None,
        cache_id: str | None = None,
        group_address: str | None = None,
        server_list: str | None = None,
        router_list: str | None = None,
        ports_defined: str | None = None,
        server_type: str | None = None,
        ports: str | None = None,
        authentication: str | None = None,
        password: str | None = None,
        forward_method: str | None = None,
        cache_engine_method: str | None = None,
        service_type: str | None = None,
        primary_hash: str | None = None,
        priority: int | None = None,
        protocol: int | None = None,
        assignment_weight: int | None = None,
        assignment_bucket_format: str | None = None,
        return_method: str | None = None,
        assignment_method: str | None = None,
        assignment_srcaddr_mask: str | None = None,
        assignment_dstaddr_mask: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            service_id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            service_id: Service ID. (optional)
            router_id: IP address known to all cache engines. If all cache
            engines connect to the same FortiGate interface, use the default
            0.0.0.0. (optional)
            cache_id: IP address known to all routers. If the addresses are the
            same, use the default 0.0.0.0. (optional)
            group_address: IP multicast address used by the cache routers. For
            the FortiGate to ignore multicast WCCP traffic, use the default
            0.0.0.0. (optional)
            server_list: IP addresses and netmasks for up to four cache
            servers. (optional)
            router_list: IP addresses of one or more WCCP routers. (optional)
            ports_defined: Match method. (optional)
            server_type: Cache server type. (optional)
            ports: Service ports. (optional)
            authentication: Enable/disable MD5 authentication. (optional)
            password: Password for MD5 authentication. (optional)
            forward_method: Method used to forward traffic to the cache
            servers. (optional)
            cache_engine_method: Method used to forward traffic to the routers
            or to return to the cache engine. (optional)
            service_type: WCCP service type used by the cache server for
            logical interception and redirection of traffic. (optional)
            primary_hash: Hash method. (optional)
            priority: Service priority. (optional)
            protocol: Service protocol. (optional)
            assignment_weight: Assignment of hash weight/ratio for the WCCP
            cache engine. (optional)
            assignment_bucket_format: Assignment bucket format for the WCCP
            cache engine. (optional)
            return_method: Method used to decline a redirected packet and
            return it to the FortiGate unit. (optional)
            assignment_method: Hash key assignment preference. (optional)
            assignment_srcaddr_mask: Assignment source address mask. (optional)
            assignment_dstaddr_mask: Assignment destination address mask.
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
        if not service_id:
            raise ValueError("service_id is required for put()")
        endpoint = f"/system/wccp/{service_id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if service_id is not None:
            data_payload["service-id"] = service_id
        if router_id is not None:
            data_payload["router-id"] = router_id
        if cache_id is not None:
            data_payload["cache-id"] = cache_id
        if group_address is not None:
            data_payload["group-address"] = group_address
        if server_list is not None:
            data_payload["server-list"] = server_list
        if router_list is not None:
            data_payload["router-list"] = router_list
        if ports_defined is not None:
            data_payload["ports-defined"] = ports_defined
        if server_type is not None:
            data_payload["server-type"] = server_type
        if ports is not None:
            data_payload["ports"] = ports
        if authentication is not None:
            data_payload["authentication"] = authentication
        if password is not None:
            data_payload["password"] = password
        if forward_method is not None:
            data_payload["forward-method"] = forward_method
        if cache_engine_method is not None:
            data_payload["cache-engine-method"] = cache_engine_method
        if service_type is not None:
            data_payload["service-type"] = service_type
        if primary_hash is not None:
            data_payload["primary-hash"] = primary_hash
        if priority is not None:
            data_payload["priority"] = priority
        if protocol is not None:
            data_payload["protocol"] = protocol
        if assignment_weight is not None:
            data_payload["assignment-weight"] = assignment_weight
        if assignment_bucket_format is not None:
            data_payload["assignment-bucket-format"] = assignment_bucket_format
        if return_method is not None:
            data_payload["return-method"] = return_method
        if assignment_method is not None:
            data_payload["assignment-method"] = assignment_method
        if assignment_srcaddr_mask is not None:
            data_payload["assignment-srcaddr-mask"] = assignment_srcaddr_mask
        if assignment_dstaddr_mask is not None:
            data_payload["assignment-dstaddr-mask"] = assignment_dstaddr_mask
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        service_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            service_id: Object identifier (required)
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
        if not service_id:
            raise ValueError("service_id is required for delete()")
        endpoint = f"/system/wccp/{service_id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        service_id: str | None = None,
        router_id: str | None = None,
        cache_id: str | None = None,
        group_address: str | None = None,
        server_list: str | None = None,
        router_list: str | None = None,
        ports_defined: str | None = None,
        server_type: str | None = None,
        ports: str | None = None,
        authentication: str | None = None,
        password: str | None = None,
        forward_method: str | None = None,
        cache_engine_method: str | None = None,
        service_type: str | None = None,
        primary_hash: str | None = None,
        priority: int | None = None,
        protocol: int | None = None,
        assignment_weight: int | None = None,
        assignment_bucket_format: str | None = None,
        return_method: str | None = None,
        assignment_method: str | None = None,
        assignment_srcaddr_mask: str | None = None,
        assignment_dstaddr_mask: str | None = None,
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
            service_id: Service ID. (optional)
            router_id: IP address known to all cache engines. If all cache
            engines connect to the same FortiGate interface, use the default
            0.0.0.0. (optional)
            cache_id: IP address known to all routers. If the addresses are the
            same, use the default 0.0.0.0. (optional)
            group_address: IP multicast address used by the cache routers. For
            the FortiGate to ignore multicast WCCP traffic, use the default
            0.0.0.0. (optional)
            server_list: IP addresses and netmasks for up to four cache
            servers. (optional)
            router_list: IP addresses of one or more WCCP routers. (optional)
            ports_defined: Match method. (optional)
            server_type: Cache server type. (optional)
            ports: Service ports. (optional)
            authentication: Enable/disable MD5 authentication. (optional)
            password: Password for MD5 authentication. (optional)
            forward_method: Method used to forward traffic to the cache
            servers. (optional)
            cache_engine_method: Method used to forward traffic to the routers
            or to return to the cache engine. (optional)
            service_type: WCCP service type used by the cache server for
            logical interception and redirection of traffic. (optional)
            primary_hash: Hash method. (optional)
            priority: Service priority. (optional)
            protocol: Service protocol. (optional)
            assignment_weight: Assignment of hash weight/ratio for the WCCP
            cache engine. (optional)
            assignment_bucket_format: Assignment bucket format for the WCCP
            cache engine. (optional)
            return_method: Method used to decline a redirected packet and
            return it to the FortiGate unit. (optional)
            assignment_method: Hash key assignment preference. (optional)
            assignment_srcaddr_mask: Assignment source address mask. (optional)
            assignment_dstaddr_mask: Assignment destination address mask.
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
        endpoint = "/system/wccp"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if service_id is not None:
            data_payload["service-id"] = service_id
        if router_id is not None:
            data_payload["router-id"] = router_id
        if cache_id is not None:
            data_payload["cache-id"] = cache_id
        if group_address is not None:
            data_payload["group-address"] = group_address
        if server_list is not None:
            data_payload["server-list"] = server_list
        if router_list is not None:
            data_payload["router-list"] = router_list
        if ports_defined is not None:
            data_payload["ports-defined"] = ports_defined
        if server_type is not None:
            data_payload["server-type"] = server_type
        if ports is not None:
            data_payload["ports"] = ports
        if authentication is not None:
            data_payload["authentication"] = authentication
        if password is not None:
            data_payload["password"] = password
        if forward_method is not None:
            data_payload["forward-method"] = forward_method
        if cache_engine_method is not None:
            data_payload["cache-engine-method"] = cache_engine_method
        if service_type is not None:
            data_payload["service-type"] = service_type
        if primary_hash is not None:
            data_payload["primary-hash"] = primary_hash
        if priority is not None:
            data_payload["priority"] = priority
        if protocol is not None:
            data_payload["protocol"] = protocol
        if assignment_weight is not None:
            data_payload["assignment-weight"] = assignment_weight
        if assignment_bucket_format is not None:
            data_payload["assignment-bucket-format"] = assignment_bucket_format
        if return_method is not None:
            data_payload["return-method"] = return_method
        if assignment_method is not None:
            data_payload["assignment-method"] = assignment_method
        if assignment_srcaddr_mask is not None:
            data_payload["assignment-srcaddr-mask"] = assignment_srcaddr_mask
        if assignment_dstaddr_mask is not None:
            data_payload["assignment-dstaddr-mask"] = assignment_dstaddr_mask
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

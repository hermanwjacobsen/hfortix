"""
FortiOS CMDB - Cmdb Firewall Address6

Configuration endpoint for managing cmdb firewall address6 objects.

API Endpoints:
    GET    /cmdb/firewall/address6
    POST   /cmdb/firewall/address6
    GET    /cmdb/firewall/address6
    PUT    /cmdb/firewall/address6/{identifier}
    DELETE /cmdb/firewall/address6/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.address6.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.address6.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.address6.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.address6.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.address6.delete(name="item_name")

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


class Address6:
    """
    Address6 Operations.

    Provides CRUD operations for FortiOS address6 configuration.

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
        Initialize Address6 endpoint.

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
            endpoint = f"/firewall/address6/{name}"
        else:
            endpoint = "/firewall/address6"
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
        type: str | None = None,
        route_tag: int | None = None,
        macaddr: list | None = None,
        sdn: str | None = None,
        ip6: str | None = None,
        wildcard: str | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        cache_ttl: int | None = None,
        color: int | None = None,
        obj_id: str | None = None,
        tagging: list | None = None,
        comment: str | None = None,
        template: str | None = None,
        subnet_segment: list | None = None,
        host_type: str | None = None,
        host: str | None = None,
        tenant: str | None = None,
        epg_name: str | None = None,
        sdn_tag: str | None = None,
        list: list | None = None,
        sdn_addr_type: str | None = None,
        passive_fqdn_learning: str | None = None,
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
            name: Address name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            type: Type of IPv6 address object (default = ipprefix). (optional)
            route_tag: route-tag address. (optional)
            macaddr: Multiple MAC address ranges. (optional)
            sdn: SDN. (optional)
            ip6: IPv6 address prefix (format:
            xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx). (optional)
            wildcard: IPv6 address and wildcard netmask. (optional)
            start_ip: First IP address (inclusive) in the range for the address
            (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). (optional)
            end_ip: Final IP address (inclusive) in the range for the address
            (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). (optional)
            fqdn: Fully qualified domain name. (optional)
            country: IPv6 addresses associated to a specific country.
            (optional)
            cache_ttl: Minimal TTL of individual IPv6 addresses in FQDN cache.
            (optional)
            color: Integer value to determine the color of the icon in the GUI
            (range 1 to 32, default = 0, which sets the value to 1). (optional)
            obj_id: Object ID for NSX. (optional)
            tagging: Config object tagging. (optional)
            comment: Comment. (optional)
            template: IPv6 address template. (optional)
            subnet_segment: IPv6 subnet segments. (optional)
            host_type: Host type. (optional)
            host: Host Address. (optional)
            tenant: Tenant. (optional)
            epg_name: Endpoint group name. (optional)
            sdn_tag: SDN Tag. (optional)
            list: IP address list. (optional)
            sdn_addr_type: Type of addresses to collect. (optional)
            passive_fqdn_learning: Enable/disable passive learning of FQDNs.
            When enabled, the FortiGate learns, trusts, and saves FQDNs from
            endpoint DNS queries (default = enable). (optional)
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
        endpoint = f"/firewall/address6/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if type is not None:
            data_payload["type"] = type
        if route_tag is not None:
            data_payload["route-tag"] = route_tag
        if macaddr is not None:
            data_payload["macaddr"] = macaddr
        if sdn is not None:
            data_payload["sdn"] = sdn
        if ip6 is not None:
            data_payload["ip6"] = ip6
        if wildcard is not None:
            data_payload["wildcard"] = wildcard
        if start_ip is not None:
            data_payload["start-ip"] = start_ip
        if end_ip is not None:
            data_payload["end-ip"] = end_ip
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if country is not None:
            data_payload["country"] = country
        if cache_ttl is not None:
            data_payload["cache-ttl"] = cache_ttl
        if color is not None:
            data_payload["color"] = color
        if obj_id is not None:
            data_payload["obj-id"] = obj_id
        if tagging is not None:
            data_payload["tagging"] = tagging
        if comment is not None:
            data_payload["comment"] = comment
        if template is not None:
            data_payload["template"] = template
        if subnet_segment is not None:
            data_payload["subnet-segment"] = subnet_segment
        if host_type is not None:
            data_payload["host-type"] = host_type
        if host is not None:
            data_payload["host"] = host
        if tenant is not None:
            data_payload["tenant"] = tenant
        if epg_name is not None:
            data_payload["epg-name"] = epg_name
        if sdn_tag is not None:
            data_payload["sdn-tag"] = sdn_tag
        if list is not None:
            data_payload["list"] = list
        if sdn_addr_type is not None:
            data_payload["sdn-addr-type"] = sdn_addr_type
        if passive_fqdn_learning is not None:
            data_payload["passive-fqdn-learning"] = passive_fqdn_learning
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
        endpoint = f"/firewall/address6/{name}"
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
        type: str | None = None,
        route_tag: int | None = None,
        macaddr: list | None = None,
        sdn: str | None = None,
        ip6: str | None = None,
        wildcard: str | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        cache_ttl: int | None = None,
        color: int | None = None,
        obj_id: str | None = None,
        tagging: list | None = None,
        comment: str | None = None,
        template: str | None = None,
        subnet_segment: list | None = None,
        host_type: str | None = None,
        host: str | None = None,
        tenant: str | None = None,
        epg_name: str | None = None,
        sdn_tag: str | None = None,
        list: list | None = None,
        sdn_addr_type: str | None = None,
        passive_fqdn_learning: str | None = None,
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
            name: Address name. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            type: Type of IPv6 address object (default = ipprefix). (optional)
            route_tag: route-tag address. (optional)
            macaddr: Multiple MAC address ranges. (optional)
            sdn: SDN. (optional)
            ip6: IPv6 address prefix (format:
            xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx). (optional)
            wildcard: IPv6 address and wildcard netmask. (optional)
            start_ip: First IP address (inclusive) in the range for the address
            (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). (optional)
            end_ip: Final IP address (inclusive) in the range for the address
            (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). (optional)
            fqdn: Fully qualified domain name. (optional)
            country: IPv6 addresses associated to a specific country.
            (optional)
            cache_ttl: Minimal TTL of individual IPv6 addresses in FQDN cache.
            (optional)
            color: Integer value to determine the color of the icon in the GUI
            (range 1 to 32, default = 0, which sets the value to 1). (optional)
            obj_id: Object ID for NSX. (optional)
            tagging: Config object tagging. (optional)
            comment: Comment. (optional)
            template: IPv6 address template. (optional)
            subnet_segment: IPv6 subnet segments. (optional)
            host_type: Host type. (optional)
            host: Host Address. (optional)
            tenant: Tenant. (optional)
            epg_name: Endpoint group name. (optional)
            sdn_tag: SDN Tag. (optional)
            list: IP address list. (optional)
            sdn_addr_type: Type of addresses to collect. (optional)
            passive_fqdn_learning: Enable/disable passive learning of FQDNs.
            When enabled, the FortiGate learns, trusts, and saves FQDNs from
            endpoint DNS queries (default = enable). (optional)
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
        endpoint = "/firewall/address6"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if type is not None:
            data_payload["type"] = type
        if route_tag is not None:
            data_payload["route-tag"] = route_tag
        if macaddr is not None:
            data_payload["macaddr"] = macaddr
        if sdn is not None:
            data_payload["sdn"] = sdn
        if ip6 is not None:
            data_payload["ip6"] = ip6
        if wildcard is not None:
            data_payload["wildcard"] = wildcard
        if start_ip is not None:
            data_payload["start-ip"] = start_ip
        if end_ip is not None:
            data_payload["end-ip"] = end_ip
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if country is not None:
            data_payload["country"] = country
        if cache_ttl is not None:
            data_payload["cache-ttl"] = cache_ttl
        if color is not None:
            data_payload["color"] = color
        if obj_id is not None:
            data_payload["obj-id"] = obj_id
        if tagging is not None:
            data_payload["tagging"] = tagging
        if comment is not None:
            data_payload["comment"] = comment
        if template is not None:
            data_payload["template"] = template
        if subnet_segment is not None:
            data_payload["subnet-segment"] = subnet_segment
        if host_type is not None:
            data_payload["host-type"] = host_type
        if host is not None:
            data_payload["host"] = host
        if tenant is not None:
            data_payload["tenant"] = tenant
        if epg_name is not None:
            data_payload["epg-name"] = epg_name
        if sdn_tag is not None:
            data_payload["sdn-tag"] = sdn_tag
        if list is not None:
            data_payload["list"] = list
        if sdn_addr_type is not None:
            data_payload["sdn-addr-type"] = sdn_addr_type
        if passive_fqdn_learning is not None:
            data_payload["passive-fqdn-learning"] = passive_fqdn_learning
        if fabric_object is not None:
            data_payload["fabric-object"] = fabric_object
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

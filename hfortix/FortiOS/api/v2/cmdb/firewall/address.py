"""
FortiOS CMDB - Cmdb Firewall Address

Configuration endpoint for managing cmdb firewall address objects.

API Endpoints:
    GET    /cmdb/firewall/address
    POST   /cmdb/firewall/address
    GET    /cmdb/firewall/address
    PUT    /cmdb/firewall/address/{identifier}
    DELETE /cmdb/firewall/address/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.address.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.address.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.address.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.address.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.address.delete(name="item_name")

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


class Address:
    """
    Address Operations.

    Provides CRUD operations for FortiOS address configuration.

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
        Initialize Address endpoint.

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
            endpoint = f"/firewall/address/{name}"
        else:
            endpoint = "/firewall/address"
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
        subnet: str | None = None,
        type: str | None = None,
        route_tag: int | None = None,
        sub_type: str | None = None,
        clearpass_spt: str | None = None,
        macaddr: list | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        wildcard_fqdn: str | None = None,
        cache_ttl: int | None = None,
        wildcard: str | None = None,
        sdn: str | None = None,
        fsso_group: list | None = None,
        sso_attribute_value: list | None = None,
        interface: str | None = None,
        tenant: str | None = None,
        organization: str | None = None,
        epg_name: str | None = None,
        subnet_name: str | None = None,
        sdn_tag: str | None = None,
        policy_group: str | None = None,
        obj_tag: str | None = None,
        obj_type: str | None = None,
        tag_detection_level: str | None = None,
        tag_type: str | None = None,
        hw_vendor: str | None = None,
        hw_model: str | None = None,
        os: str | None = None,
        sw_version: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        sdn_addr_type: str | None = None,
        node_ip_only: str | None = None,
        obj_id: str | None = None,
        list: list | None = None,
        tagging: list | None = None,
        allow_routing: str | None = None,
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
            subnet: IP address and subnet mask of address. (optional)
            type: Type of address. (optional)
            route_tag: route-tag address. (optional)
            sub_type: Sub-type of address. (optional)
            clearpass_spt: SPT (System Posture Token) value. (optional)
            macaddr: Multiple MAC address ranges. (optional)
            start_ip: First IP address (inclusive) in the range for the
            address. (optional)
            end_ip: Final IP address (inclusive) in the range for the address.
            (optional)
            fqdn: Fully Qualified Domain Name address. (optional)
            country: IP addresses associated to a specific country. (optional)
            wildcard_fqdn: Fully Qualified Domain Name with wildcard
            characters. (optional)
            cache_ttl: Defines the minimal TTL of individual IP addresses in
            FQDN cache measured in seconds. (optional)
            wildcard: IP address and wildcard netmask. (optional)
            sdn: SDN. (optional)
            fsso_group: FSSO group(s). (optional)
            sso_attribute_value: RADIUS attributes value. (optional)
            interface: Name of interface whose IP address is to be used.
            (optional)
            tenant: Tenant. (optional)
            organization: Organization domain name (Syntax:
            organization/domain). (optional)
            epg_name: Endpoint group name. (optional)
            subnet_name: Subnet name. (optional)
            sdn_tag: SDN Tag. (optional)
            policy_group: Policy group name. (optional)
            obj_tag: Tag of dynamic address object. (optional)
            obj_type: Object type. (optional)
            tag_detection_level: Tag detection level of dynamic address object.
            (optional)
            tag_type: Tag type of dynamic address object. (optional)
            hw_vendor: Dynamic address matching hardware vendor. (optional)
            hw_model: Dynamic address matching hardware model. (optional)
            os: Dynamic address matching operating system. (optional)
            sw_version: Dynamic address matching software version. (optional)
            comment: Comment. (optional)
            associated_interface: Network interface associated with address.
            (optional)
            color: Color of icon on the GUI. (optional)
            sdn_addr_type: Type of addresses to collect. (optional)
            node_ip_only: Enable/disable collection of node addresses only in
            Kubernetes. (optional)
            obj_id: Object ID for NSX. (optional)
            list: IP address list. (optional)
            tagging: Config object tagging. (optional)
            allow_routing: Enable/disable use of this address in routing
            configurations. (optional)
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
        endpoint = f"/firewall/address/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if subnet is not None:
            data_payload["subnet"] = subnet
        if type is not None:
            data_payload["type"] = type
        if route_tag is not None:
            data_payload["route-tag"] = route_tag
        if sub_type is not None:
            data_payload["sub-type"] = sub_type
        if clearpass_spt is not None:
            data_payload["clearpass-spt"] = clearpass_spt
        if macaddr is not None:
            data_payload["macaddr"] = macaddr
        if start_ip is not None:
            data_payload["start-ip"] = start_ip
        if end_ip is not None:
            data_payload["end-ip"] = end_ip
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if country is not None:
            data_payload["country"] = country
        if wildcard_fqdn is not None:
            data_payload["wildcard-fqdn"] = wildcard_fqdn
        if cache_ttl is not None:
            data_payload["cache-ttl"] = cache_ttl
        if wildcard is not None:
            data_payload["wildcard"] = wildcard
        if sdn is not None:
            data_payload["sdn"] = sdn
        if fsso_group is not None:
            data_payload["fsso-group"] = fsso_group
        if sso_attribute_value is not None:
            data_payload["sso-attribute-value"] = sso_attribute_value
        if interface is not None:
            data_payload["interface"] = interface
        if tenant is not None:
            data_payload["tenant"] = tenant
        if organization is not None:
            data_payload["organization"] = organization
        if epg_name is not None:
            data_payload["epg-name"] = epg_name
        if subnet_name is not None:
            data_payload["subnet-name"] = subnet_name
        if sdn_tag is not None:
            data_payload["sdn-tag"] = sdn_tag
        if policy_group is not None:
            data_payload["policy-group"] = policy_group
        if obj_tag is not None:
            data_payload["obj-tag"] = obj_tag
        if obj_type is not None:
            data_payload["obj-type"] = obj_type
        if tag_detection_level is not None:
            data_payload["tag-detection-level"] = tag_detection_level
        if tag_type is not None:
            data_payload["tag-type"] = tag_type
        if hw_vendor is not None:
            data_payload["hw-vendor"] = hw_vendor
        if hw_model is not None:
            data_payload["hw-model"] = hw_model
        if os is not None:
            data_payload["os"] = os
        if sw_version is not None:
            data_payload["sw-version"] = sw_version
        if comment is not None:
            data_payload["comment"] = comment
        if associated_interface is not None:
            data_payload["associated-interface"] = associated_interface
        if color is not None:
            data_payload["color"] = color
        if sdn_addr_type is not None:
            data_payload["sdn-addr-type"] = sdn_addr_type
        if node_ip_only is not None:
            data_payload["node-ip-only"] = node_ip_only
        if obj_id is not None:
            data_payload["obj-id"] = obj_id
        if list is not None:
            data_payload["list"] = list
        if tagging is not None:
            data_payload["tagging"] = tagging
        if allow_routing is not None:
            data_payload["allow-routing"] = allow_routing
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
        endpoint = f"/firewall/address/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ):
        """
        Check if an object exists.

        Automatically works in both sync and async modes.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            bool (sync mode) or Coroutine[bool] (async mode)

        Example (Sync):
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")

        Example (Async):
            >>> if await fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect
        from typing import Any, cast

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
        subnet: str | None = None,
        type: str | None = None,
        route_tag: int | None = None,
        sub_type: str | None = None,
        clearpass_spt: str | None = None,
        macaddr: list | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        wildcard_fqdn: str | None = None,
        cache_ttl: int | None = None,
        wildcard: str | None = None,
        sdn: str | None = None,
        fsso_group: list | None = None,
        sso_attribute_value: list | None = None,
        interface: str | None = None,
        tenant: str | None = None,
        organization: str | None = None,
        epg_name: str | None = None,
        subnet_name: str | None = None,
        sdn_tag: str | None = None,
        policy_group: str | None = None,
        obj_tag: str | None = None,
        obj_type: str | None = None,
        tag_detection_level: str | None = None,
        tag_type: str | None = None,
        hw_vendor: str | None = None,
        hw_model: str | None = None,
        os: str | None = None,
        sw_version: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        sdn_addr_type: str | None = None,
        node_ip_only: str | None = None,
        obj_id: str | None = None,
        list: list | None = None,
        tagging: list | None = None,
        allow_routing: str | None = None,
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
            subnet: IP address and subnet mask of address. (optional)
            type: Type of address. (optional)
            route_tag: route-tag address. (optional)
            sub_type: Sub-type of address. (optional)
            clearpass_spt: SPT (System Posture Token) value. (optional)
            macaddr: Multiple MAC address ranges. (optional)
            start_ip: First IP address (inclusive) in the range for the
            address. (optional)
            end_ip: Final IP address (inclusive) in the range for the address.
            (optional)
            fqdn: Fully Qualified Domain Name address. (optional)
            country: IP addresses associated to a specific country. (optional)
            wildcard_fqdn: Fully Qualified Domain Name with wildcard
            characters. (optional)
            cache_ttl: Defines the minimal TTL of individual IP addresses in
            FQDN cache measured in seconds. (optional)
            wildcard: IP address and wildcard netmask. (optional)
            sdn: SDN. (optional)
            fsso_group: FSSO group(s). (optional)
            sso_attribute_value: RADIUS attributes value. (optional)
            interface: Name of interface whose IP address is to be used.
            (optional)
            tenant: Tenant. (optional)
            organization: Organization domain name (Syntax:
            organization/domain). (optional)
            epg_name: Endpoint group name. (optional)
            subnet_name: Subnet name. (optional)
            sdn_tag: SDN Tag. (optional)
            policy_group: Policy group name. (optional)
            obj_tag: Tag of dynamic address object. (optional)
            obj_type: Object type. (optional)
            tag_detection_level: Tag detection level of dynamic address object.
            (optional)
            tag_type: Tag type of dynamic address object. (optional)
            hw_vendor: Dynamic address matching hardware vendor. (optional)
            hw_model: Dynamic address matching hardware model. (optional)
            os: Dynamic address matching operating system. (optional)
            sw_version: Dynamic address matching software version. (optional)
            comment: Comment. (optional)
            associated_interface: Network interface associated with address.
            (optional)
            color: Color of icon on the GUI. (optional)
            sdn_addr_type: Type of addresses to collect. (optional)
            node_ip_only: Enable/disable collection of node addresses only in
            Kubernetes. (optional)
            obj_id: Object ID for NSX. (optional)
            list: IP address list. (optional)
            tagging: Config object tagging. (optional)
            allow_routing: Enable/disable use of this address in routing
            configurations. (optional)
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
        endpoint = "/firewall/address"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if uuid is not None:
            data_payload["uuid"] = uuid
        if subnet is not None:
            data_payload["subnet"] = subnet
        if type is not None:
            data_payload["type"] = type
        if route_tag is not None:
            data_payload["route-tag"] = route_tag
        if sub_type is not None:
            data_payload["sub-type"] = sub_type
        if clearpass_spt is not None:
            data_payload["clearpass-spt"] = clearpass_spt
        if macaddr is not None:
            data_payload["macaddr"] = macaddr
        if start_ip is not None:
            data_payload["start-ip"] = start_ip
        if end_ip is not None:
            data_payload["end-ip"] = end_ip
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if country is not None:
            data_payload["country"] = country
        if wildcard_fqdn is not None:
            data_payload["wildcard-fqdn"] = wildcard_fqdn
        if cache_ttl is not None:
            data_payload["cache-ttl"] = cache_ttl
        if wildcard is not None:
            data_payload["wildcard"] = wildcard
        if sdn is not None:
            data_payload["sdn"] = sdn
        if fsso_group is not None:
            data_payload["fsso-group"] = fsso_group
        if sso_attribute_value is not None:
            data_payload["sso-attribute-value"] = sso_attribute_value
        if interface is not None:
            data_payload["interface"] = interface
        if tenant is not None:
            data_payload["tenant"] = tenant
        if organization is not None:
            data_payload["organization"] = organization
        if epg_name is not None:
            data_payload["epg-name"] = epg_name
        if subnet_name is not None:
            data_payload["subnet-name"] = subnet_name
        if sdn_tag is not None:
            data_payload["sdn-tag"] = sdn_tag
        if policy_group is not None:
            data_payload["policy-group"] = policy_group
        if obj_tag is not None:
            data_payload["obj-tag"] = obj_tag
        if obj_type is not None:
            data_payload["obj-type"] = obj_type
        if tag_detection_level is not None:
            data_payload["tag-detection-level"] = tag_detection_level
        if tag_type is not None:
            data_payload["tag-type"] = tag_type
        if hw_vendor is not None:
            data_payload["hw-vendor"] = hw_vendor
        if hw_model is not None:
            data_payload["hw-model"] = hw_model
        if os is not None:
            data_payload["os"] = os
        if sw_version is not None:
            data_payload["sw-version"] = sw_version
        if comment is not None:
            data_payload["comment"] = comment
        if associated_interface is not None:
            data_payload["associated-interface"] = associated_interface
        if color is not None:
            data_payload["color"] = color
        if sdn_addr_type is not None:
            data_payload["sdn-addr-type"] = sdn_addr_type
        if node_ip_only is not None:
            data_payload["node-ip-only"] = node_ip_only
        if obj_id is not None:
            data_payload["obj-id"] = obj_id
        if list is not None:
            data_payload["list"] = list
        if tagging is not None:
            data_payload["tagging"] = tagging
        if allow_routing is not None:
            data_payload["allow-routing"] = allow_routing
        if passive_fqdn_learning is not None:
            data_payload["passive-fqdn-learning"] = passive_fqdn_learning
        if fabric_object is not None:
            data_payload["fabric-object"] = fabric_object
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

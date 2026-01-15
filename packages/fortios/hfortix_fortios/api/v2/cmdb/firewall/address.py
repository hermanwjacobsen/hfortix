"""
FortiOS CMDB - Firewall address

Configuration endpoint for managing cmdb firewall/address objects.

API Endpoints:
    GET    /cmdb/firewall/address
    POST   /cmdb/firewall/address
    PUT    /cmdb/firewall/address/{identifier}
    DELETE /cmdb/firewall/address/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_address.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.firewall_address.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
    normalize_table_field,  # For table field normalization
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Address(CRUDEndpoint, MetadataMixin):
    """Address Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "address"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "macaddr": {
            "mkey": "macaddr",
            "required_fields": ['macaddr'],
            "example": "[{'macaddr': 'value'}]",
        },
        "fsso_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "sso_attribute_value": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "list": {
            "mkey": "ip",
            "required_fields": ['ip'],
            "example": "[{'ip': '192.168.1.10'}]",
        },
        "tagging": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
    }
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Address endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        q_datasource: bool | None = None,
        q_skip_to: int | None = None,
        q_with_meta: bool | None = None,
        q_with_contents_hash: bool | None = None,
        q_skip: bool | None = None,
        q_format: list[str] | None = None,
        q_key: str | None = None,
        q_pattern: str | None = None,
        q_scope: str | None = None,
        q_exclude_default_values: bool | None = None,
        q_datasource_format: dict[str, Any] | None = None,
        q_unfiltered_count: int | None = None,
        q_stat_items: str | None = None,
        q_primary_keys: str | None = None,
        q_action: Literal["default", "schema"] | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve firewall/address configuration.

        Configure IPv4 addresses.

        Args:
            name: String identifier to retrieve specific object.
                If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance or list of FortiObject instances. Returns Coroutine if using async client.
            Use .dict, .json, or .raw properties to access as dictionary.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all firewall/address objects
            >>> result = fgt.api.cmdb.firewall_address.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/address by name
            >>> result = fgt.api.cmdb.firewall_address.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_address.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_address.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_address.get_schema()

        See Also:
            - post(): Create new firewall/address object
            - put(): Update existing firewall/address object
            - delete(): Remove firewall/address object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if q_datasource is not None:
            params["datasource"] = q_datasource
        if q_skip_to is not None:
            params["skip_to"] = q_skip_to
        if q_with_meta is not None:
            params["with_meta"] = q_with_meta
        if q_with_contents_hash is not None:
            params["with_contents_hash"] = q_with_contents_hash
        if q_skip is not None:
            params["skip"] = q_skip
        if q_format is not None:
            params["format"] = q_format
        if q_key is not None:
            params["key"] = q_key
        if q_pattern is not None:
            params["pattern"] = q_pattern
        if q_scope is not None:
            params["scope"] = q_scope
        if q_exclude_default_values is not None:
            params["exclude-default-values"] = q_exclude_default_values
        if q_datasource_format is not None:
            params["datasource_format"] = q_datasource_format
        if q_unfiltered_count is not None:
            params["unfiltered_count"] = q_unfiltered_count
        if q_stat_items is not None:
            params["stat-items"] = q_stat_items
        if q_primary_keys is not None:
            params["primary_keys"] = q_primary_keys
        if q_action is not None:
            params["action"] = q_action
        
        if name:
            endpoint = "/firewall/address/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/firewall/address"
            unwrap_single = False
        
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.firewall_address.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_address.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        subnet: Any | None = None,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = None,
        route_tag: int | None = None,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = None,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = None,
        macaddr: str | list[str] | list[dict[str, Any]] | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        wildcard_fqdn: str | None = None,
        cache_ttl: int | None = None,
        wildcard: Any | None = None,
        sdn: str | None = None,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = None,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = None,
        interface: str | None = None,
        tenant: str | None = None,
        organization: str | None = None,
        epg_name: str | None = None,
        subnet_name: str | None = None,
        sdn_tag: str | None = None,
        policy_group: str | None = None,
        obj_tag: str | None = None,
        obj_type: Literal["ip", "mac"] | None = None,
        tag_detection_level: str | None = None,
        tag_type: str | None = None,
        hw_vendor: str | None = None,
        hw_model: str | None = None,
        os: str | None = None,
        sw_version: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        filter: str | None = None,
        sdn_addr_type: Literal["private", "public", "all"] | None = None,
        node_ip_only: Literal["enable", "disable"] | None = None,
        obj_id: str | None = None,
        list: str | list[str] | list[dict[str, Any]] | None = None,
        tagging: str | list[str] | list[dict[str, Any]] | None = None,
        allow_routing: Literal["enable", "disable"] | None = None,
        passive_fqdn_learning: Literal["disable", "enable"] | None = None,
        fabric_object: Literal["enable", "disable"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing firewall/address object.

        Configure IPv4 addresses.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Address name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            subnet: IP address and subnet mask of address.
            type: Type of address.
            route_tag: route-tag address.
            sub_type: Sub-type of address.
            clearpass_spt: SPT (System Posture Token) value.
            macaddr: Multiple MAC address ranges.
                Default format: [{'macaddr': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'macaddr': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'macaddr': 'val1'}, ...]
                  - List of dicts: [{'macaddr': 'value'}] (recommended)
            start_ip: First IP address (inclusive) in the range for the address.
            end_ip: Final IP address (inclusive) in the range for the address.
            fqdn: Fully Qualified Domain Name address.
            country: IP addresses associated to a specific country.
            wildcard_fqdn: Fully Qualified Domain Name with wildcard characters.
            cache_ttl: Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds.
            wildcard: IP address and wildcard netmask.
            sdn: SDN.
            fsso_group: FSSO group(s).
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            sso_attribute_value: RADIUS attributes value.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            interface: Name of interface whose IP address is to be used.
            tenant: Tenant.
            organization: Organization domain name (Syntax: organization/domain).
            epg_name: Endpoint group name.
            subnet_name: Subnet name.
            sdn_tag: SDN Tag.
            policy_group: Policy group name.
            obj_tag: Tag of dynamic address object.
            obj_type: Object type.
            tag_detection_level: Tag detection level of dynamic address object.
            tag_type: Tag type of dynamic address object.
            hw_vendor: Dynamic address matching hardware vendor.
            hw_model: Dynamic address matching hardware model.
            os: Dynamic address matching operating system.
            sw_version: Dynamic address matching software version.
            comment: Comment.
            associated_interface: Network interface associated with address.
            color: Color of icon on the GUI.
            filter: Match criteria filter.
            sdn_addr_type: Type of addresses to collect.
            node_ip_only: Enable/disable collection of node addresses only in Kubernetes.
            obj_id: Object ID for NSX.
            list: IP address list.
                Default format: [{'ip': '192.168.1.10'}]
                Supported formats:
                  - Single string: "value" → [{'ip': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'ip': 'val1'}, ...]
                  - List of dicts: [{'ip': '192.168.1.10'}] (recommended)
            tagging: Config object tagging.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            allow_routing: Enable/disable use of this address in routing configurations.
            passive_fqdn_learning: Enable/disable passive learning of FQDNs.  When enabled, the FortiGate learns, trusts, and saves FQDNs from endpoint DNS queries (default = enable).
            fabric_object: Security Fabric global object setting.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_address.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_address.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if macaddr is not None:
            macaddr = normalize_table_field(
                macaddr,
                mkey="macaddr",
                required_fields=['macaddr'],
                field_name="macaddr",
                example="[{'macaddr': 'value'}]",
            )
        if fsso_group is not None:
            fsso_group = normalize_table_field(
                fsso_group,
                mkey="name",
                required_fields=['name'],
                field_name="fsso_group",
                example="[{'name': 'value'}]",
            )
        if sso_attribute_value is not None:
            sso_attribute_value = normalize_table_field(
                sso_attribute_value,
                mkey="name",
                required_fields=['name'],
                field_name="sso_attribute_value",
                example="[{'name': 'value'}]",
            )
        if list is not None:
            list = normalize_table_field(
                list,
                mkey="ip",
                required_fields=['ip'],
                field_name="list",
                example="[{'ip': '192.168.1.10'}]",
            )
        if tagging is not None:
            tagging = normalize_table_field(
                tagging,
                mkey="name",
                required_fields=['name'],
                field_name="tagging",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            uuid=uuid,
            subnet=subnet,
            type=type,
            route_tag=route_tag,
            sub_type=sub_type,
            clearpass_spt=clearpass_spt,
            macaddr=macaddr,
            start_ip=start_ip,
            end_ip=end_ip,
            fqdn=fqdn,
            country=country,
            wildcard_fqdn=wildcard_fqdn,
            cache_ttl=cache_ttl,
            wildcard=wildcard,
            sdn=sdn,
            fsso_group=fsso_group,
            sso_attribute_value=sso_attribute_value,
            interface=interface,
            tenant=tenant,
            organization=organization,
            epg_name=epg_name,
            subnet_name=subnet_name,
            sdn_tag=sdn_tag,
            policy_group=policy_group,
            obj_tag=obj_tag,
            obj_type=obj_type,
            tag_detection_level=tag_detection_level,
            tag_type=tag_type,
            hw_vendor=hw_vendor,
            hw_model=hw_model,
            os=os,
            sw_version=sw_version,
            comment=comment,
            associated_interface=associated_interface,
            color=color,
            filter=filter,
            sdn_addr_type=sdn_addr_type,
            node_ip_only=node_ip_only,
            obj_id=obj_id,
            list=list,
            tagging=tagging,
            allow_routing=allow_routing,
            passive_fqdn_learning=passive_fqdn_learning,
            fabric_object=fabric_object,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.address import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/address",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/firewall/address/" + str(name_value)

        # Add explicit query parameters for PUT
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_before is not None:
            params["before"] = q_before
        if q_after is not None:
            params["after"] = q_after
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )

    # ========================================================================
    # POST Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        subnet: Any | None = None,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = None,
        route_tag: int | None = None,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = None,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = None,
        macaddr: str | list[str] | list[dict[str, Any]] | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        wildcard_fqdn: str | None = None,
        cache_ttl: int | None = None,
        wildcard: Any | None = None,
        sdn: str | None = None,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = None,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = None,
        interface: str | None = None,
        tenant: str | None = None,
        organization: str | None = None,
        epg_name: str | None = None,
        subnet_name: str | None = None,
        sdn_tag: str | None = None,
        policy_group: str | None = None,
        obj_tag: str | None = None,
        obj_type: Literal["ip", "mac"] | None = None,
        tag_detection_level: str | None = None,
        tag_type: str | None = None,
        hw_vendor: str | None = None,
        hw_model: str | None = None,
        os: str | None = None,
        sw_version: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        filter: str | None = None,
        sdn_addr_type: Literal["private", "public", "all"] | None = None,
        node_ip_only: Literal["enable", "disable"] | None = None,
        obj_id: str | None = None,
        list: str | list[str] | list[dict[str, Any]] | None = None,
        tagging: str | list[str] | list[dict[str, Any]] | None = None,
        allow_routing: Literal["enable", "disable"] | None = None,
        passive_fqdn_learning: Literal["disable", "enable"] | None = None,
        fabric_object: Literal["enable", "disable"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new firewall/address object.

        Configure IPv4 addresses.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Address name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            subnet: IP address and subnet mask of address.
            type: Type of address.
            route_tag: route-tag address.
            sub_type: Sub-type of address.
            clearpass_spt: SPT (System Posture Token) value.
            macaddr: Multiple MAC address ranges.
                Default format: [{'macaddr': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'macaddr': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'macaddr': 'val1'}, ...]
                  - List of dicts: [{'macaddr': 'value'}] (recommended)
            start_ip: First IP address (inclusive) in the range for the address.
            end_ip: Final IP address (inclusive) in the range for the address.
            fqdn: Fully Qualified Domain Name address.
            country: IP addresses associated to a specific country.
            wildcard_fqdn: Fully Qualified Domain Name with wildcard characters.
            cache_ttl: Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds.
            wildcard: IP address and wildcard netmask.
            sdn: SDN.
            fsso_group: FSSO group(s).
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            sso_attribute_value: RADIUS attributes value.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            interface: Name of interface whose IP address is to be used.
            tenant: Tenant.
            organization: Organization domain name (Syntax: organization/domain).
            epg_name: Endpoint group name.
            subnet_name: Subnet name.
            sdn_tag: SDN Tag.
            policy_group: Policy group name.
            obj_tag: Tag of dynamic address object.
            obj_type: Object type.
            tag_detection_level: Tag detection level of dynamic address object.
            tag_type: Tag type of dynamic address object.
            hw_vendor: Dynamic address matching hardware vendor.
            hw_model: Dynamic address matching hardware model.
            os: Dynamic address matching operating system.
            sw_version: Dynamic address matching software version.
            comment: Comment.
            associated_interface: Network interface associated with address.
            color: Color of icon on the GUI.
            filter: Match criteria filter.
            sdn_addr_type: Type of addresses to collect.
            node_ip_only: Enable/disable collection of node addresses only in Kubernetes.
            obj_id: Object ID for NSX.
            list: IP address list.
                Default format: [{'ip': '192.168.1.10'}]
                Supported formats:
                  - Single string: "value" → [{'ip': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'ip': 'val1'}, ...]
                  - List of dicts: [{'ip': '192.168.1.10'}] (recommended)
            tagging: Config object tagging.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            allow_routing: Enable/disable use of this address in routing configurations.
            passive_fqdn_learning: Enable/disable passive learning of FQDNs.  When enabled, the FortiGate learns, trusts, and saves FQDNs from endpoint DNS queries (default = enable).
            fabric_object: Security Fabric global object setting.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_address.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Address.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_address.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Address.required_fields()) }}
            
            Use Address.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if macaddr is not None:
            macaddr = normalize_table_field(
                macaddr,
                mkey="macaddr",
                required_fields=['macaddr'],
                field_name="macaddr",
                example="[{'macaddr': 'value'}]",
            )
        if fsso_group is not None:
            fsso_group = normalize_table_field(
                fsso_group,
                mkey="name",
                required_fields=['name'],
                field_name="fsso_group",
                example="[{'name': 'value'}]",
            )
        if sso_attribute_value is not None:
            sso_attribute_value = normalize_table_field(
                sso_attribute_value,
                mkey="name",
                required_fields=['name'],
                field_name="sso_attribute_value",
                example="[{'name': 'value'}]",
            )
        if list is not None:
            list = normalize_table_field(
                list,
                mkey="ip",
                required_fields=['ip'],
                field_name="list",
                example="[{'ip': '192.168.1.10'}]",
            )
        if tagging is not None:
            tagging = normalize_table_field(
                tagging,
                mkey="name",
                required_fields=['name'],
                field_name="tagging",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            uuid=uuid,
            subnet=subnet,
            type=type,
            route_tag=route_tag,
            sub_type=sub_type,
            clearpass_spt=clearpass_spt,
            macaddr=macaddr,
            start_ip=start_ip,
            end_ip=end_ip,
            fqdn=fqdn,
            country=country,
            wildcard_fqdn=wildcard_fqdn,
            cache_ttl=cache_ttl,
            wildcard=wildcard,
            sdn=sdn,
            fsso_group=fsso_group,
            sso_attribute_value=sso_attribute_value,
            interface=interface,
            tenant=tenant,
            organization=organization,
            epg_name=epg_name,
            subnet_name=subnet_name,
            sdn_tag=sdn_tag,
            policy_group=policy_group,
            obj_tag=obj_tag,
            obj_type=obj_type,
            tag_detection_level=tag_detection_level,
            tag_type=tag_type,
            hw_vendor=hw_vendor,
            hw_model=hw_model,
            os=os,
            sw_version=sw_version,
            comment=comment,
            associated_interface=associated_interface,
            color=color,
            filter=filter,
            sdn_addr_type=sdn_addr_type,
            node_ip_only=node_ip_only,
            obj_id=obj_id,
            list=list,
            tagging=tagging,
            allow_routing=allow_routing,
            passive_fqdn_learning=passive_fqdn_learning,
            fabric_object=fabric_object,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.address import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/address",
            )

        endpoint = "/firewall/address"
        
        # Add explicit query parameters for POST
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_nkey is not None:
            params["nkey"] = q_nkey
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )

    # ========================================================================
    # DELETE Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def delete(
        self,
        name: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete firewall/address object.

        Configure IPv4 addresses.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_address.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/firewall/address/" + str(name)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/address object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_address.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_address.exists(name=1):
            ...     fgt.api.cmdb.firewall_address.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/firewall/address"
        endpoint = f"{endpoint}/{name}"
        
        # Make request with silent=True to suppress 404 error logging
        # (404 is expected when checking existence - it just means "doesn't exist")
        # Use _wrapped_client to access the underlying HTTPClient directly
        # (self._client is ResponseProcessingClient, _wrapped_client is HTTPClient)
        try:
            result = self._client._wrapped_client.get(
                "cmdb",
                endpoint,
                params=None,
                vdom=vdom,
                raw_json=True,
                silent=True,
            )
            
            if isinstance(result, dict):
                # Synchronous response - check status
                return result.get("status") == "success"
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await result
                    return r.get("status") == "success"
                return _check()
        except Exception:
            # Any error (404, network, etc.) means we can't confirm existence
            return False


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        subnet: Any | None = None,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = None,
        route_tag: int | None = None,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = None,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = None,
        macaddr: str | list[str] | list[dict[str, Any]] | None = None,
        start_ip: str | None = None,
        end_ip: str | None = None,
        fqdn: str | None = None,
        country: str | None = None,
        wildcard_fqdn: str | None = None,
        cache_ttl: int | None = None,
        wildcard: Any | None = None,
        sdn: str | None = None,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = None,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = None,
        interface: str | None = None,
        tenant: str | None = None,
        organization: str | None = None,
        epg_name: str | None = None,
        subnet_name: str | None = None,
        sdn_tag: str | None = None,
        policy_group: str | None = None,
        obj_tag: str | None = None,
        obj_type: Literal["ip", "mac"] | None = None,
        tag_detection_level: str | None = None,
        tag_type: str | None = None,
        hw_vendor: str | None = None,
        hw_model: str | None = None,
        os: str | None = None,
        sw_version: str | None = None,
        comment: str | None = None,
        associated_interface: str | None = None,
        color: int | None = None,
        filter: str | None = None,
        sdn_addr_type: Literal["private", "public", "all"] | None = None,
        node_ip_only: Literal["enable", "disable"] | None = None,
        obj_id: str | None = None,
        list: str | list[str] | list[dict[str, Any]] | None = None,
        tagging: str | list[str] | list[dict[str, Any]] | None = None,
        allow_routing: Literal["enable", "disable"] | None = None,
        passive_fqdn_learning: Literal["disable", "enable"] | None = None,
        fabric_object: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/address object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            uuid: Field uuid
            subnet: Field subnet
            type: Field type
            route_tag: Field route-tag
            sub_type: Field sub-type
            clearpass_spt: Field clearpass-spt
            macaddr: Field macaddr
            start_ip: Field start-ip
            end_ip: Field end-ip
            fqdn: Field fqdn
            country: Field country
            wildcard_fqdn: Field wildcard-fqdn
            cache_ttl: Field cache-ttl
            wildcard: Field wildcard
            sdn: Field sdn
            fsso_group: Field fsso-group
            sso_attribute_value: Field sso-attribute-value
            interface: Field interface
            tenant: Field tenant
            organization: Field organization
            epg_name: Field epg-name
            subnet_name: Field subnet-name
            sdn_tag: Field sdn-tag
            policy_group: Field policy-group
            obj_tag: Field obj-tag
            obj_type: Field obj-type
            tag_detection_level: Field tag-detection-level
            tag_type: Field tag-type
            hw_vendor: Field hw-vendor
            hw_model: Field hw-model
            os: Field os
            sw_version: Field sw-version
            comment: Field comment
            associated_interface: Field associated-interface
            color: Field color
            filter: Field filter
            sdn_addr_type: Field sdn-addr-type
            node_ip_only: Field node-ip-only
            obj_id: Field obj-id
            list: Field list
            tagging: Field tagging
            allow_routing: Field allow-routing
            passive_fqdn_learning: Field passive-fqdn-learning
            fabric_object: Field fabric-object
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.firewall_address.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_address.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_address.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        # Build payload using helper function with auto-normalization
        payload_data = build_api_payload(
            name=name,
            uuid=uuid,
            subnet=subnet,
            type=type,
            route_tag=route_tag,
            sub_type=sub_type,
            clearpass_spt=clearpass_spt,
            macaddr=macaddr,
            start_ip=start_ip,
            end_ip=end_ip,
            fqdn=fqdn,
            country=country,
            wildcard_fqdn=wildcard_fqdn,
            cache_ttl=cache_ttl,
            wildcard=wildcard,
            sdn=sdn,
            fsso_group=fsso_group,
            sso_attribute_value=sso_attribute_value,
            interface=interface,
            tenant=tenant,
            organization=organization,
            epg_name=epg_name,
            subnet_name=subnet_name,
            sdn_tag=sdn_tag,
            policy_group=policy_group,
            obj_tag=obj_tag,
            obj_type=obj_type,
            tag_detection_level=tag_detection_level,
            tag_type=tag_type,
            hw_vendor=hw_vendor,
            hw_model=hw_model,
            os=os,
            sw_version=sw_version,
            comment=comment,
            associated_interface=associated_interface,
            color=color,
            filter=filter,
            sdn_addr_type=sdn_addr_type,
            node_ip_only=node_ip_only,
            obj_id=obj_id,
            list=list,
            tagging=tagging,
            allow_routing=allow_routing,
            passive_fqdn_learning=passive_fqdn_learning,
            fabric_object=fabric_object,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("name")
        if not mkey_value:
            raise ValueError("name is required for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_data, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_data, vdom=vdom, **kwargs)

    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move firewall/address object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.firewall_address.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/address",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone firewall/address object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.firewall_address.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/address",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )



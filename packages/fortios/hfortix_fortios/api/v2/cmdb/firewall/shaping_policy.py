"""
FortiOS CMDB - Firewall shaping_policy

Configuration endpoint for managing cmdb firewall/shaping_policy objects.

API Endpoints:
    GET    /cmdb/firewall/shaping_policy
    POST   /cmdb/firewall/shaping_policy
    PUT    /cmdb/firewall/shaping_policy/{identifier}
    DELETE /cmdb/firewall/shaping_policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_shaping_policy.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.firewall_shaping_policy.post(
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

class ShapingPolicy(CRUDEndpoint, MetadataMixin):
    """ShapingPolicy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "shaping_policy"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "srcaddr": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "dstaddr": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "srcaddr6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "dstaddr6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_name": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_custom": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_custom_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_fortiguard": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_src_name": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_src_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_src_custom": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_src_custom_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_src_fortiguard": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "service": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "users": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "groups": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "application": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "app_category": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "app_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "url_category": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "srcintf": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "dstintf": {
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
        """Initialize ShapingPolicy endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        id: int | None = None,
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
        Retrieve firewall/shaping_policy configuration.

        Configure shaping policies.

        Args:
            id: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/shaping_policy objects
            >>> result = fgt.api.cmdb.firewall_shaping_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/shaping_policy by id
            >>> result = fgt.api.cmdb.firewall_shaping_policy.get(id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_shaping_policy.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_shaping_policy.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_shaping_policy.get_schema()

        See Also:
            - post(): Create new firewall/shaping_policy object
            - put(): Update existing firewall/shaping_policy object
            - delete(): Remove firewall/shaping_policy object
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
        
        if id:
            endpoint = "/firewall/shaping-policy/" + str(id)
            unwrap_single = True
        else:
            endpoint = "/firewall/shaping-policy"
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
            >>> schema = fgt.api.cmdb.firewall_shaping_policy.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_shaping_policy.get_schema(format="json-schema")
        
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
        id: int | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        ip_version: Literal["4", "6"] | None = None,
        traffic_type: Literal["forwarding", "local-in", "local-out"] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        schedule: str | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        application: str | list[str] | list[dict[str, Any]] | None = None,
        app_category: str | list[str] | list[dict[str, Any]] | None = None,
        app_group: str | list[str] | list[dict[str, Any]] | None = None,
        url_category: str | list[str] | list[dict[str, Any]] | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: Literal["enable", "disable"] | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        class_id: int | None = None,
        diffserv_forward: Literal["enable", "disable"] | None = None,
        diffserv_reverse: Literal["enable", "disable"] | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        cos_mask: str | None = None,
        cos: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing firewall/shaping_policy object.

        Configure shaping policies.

        Args:
            payload_dict: Object data as dict. Must include id (primary key).
            id: Shaping policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            name: Shaping policy name.
            comment: Comments.
            status: Enable/disable this traffic shaping policy.
            ip_version: Apply this traffic shaping policy to IPv4 or IPv6 traffic.
            traffic_type: Traffic type.
            srcaddr: IPv4 source address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: IPv4 destination address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr6: IPv6 source address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: IPv6 destination address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.
            internet_service_name: Internet Service ID.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_group: Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_custom: Custom Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_custom_group: Custom Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_fortiguard: FortiGuard Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src: Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.
            internet_service_src_name: Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_group: Internet Service source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_custom: Custom Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_custom_group: Custom Internet Service source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_fortiguard: FortiGuard Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service: Service and service group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            schedule: Schedule name.
            users: Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            groups: Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            application: IDs of one or more applications that this shaper applies application control traffic shaping to.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            app_category: IDs of one or more application categories that this shaper applies application control traffic shaping to.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            app_group: One or more application group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            url_category: IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            srcintf: One or more incoming (ingress) interfaces.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstintf: One or more outgoing (egress) interfaces.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            tos_mask: Non-zero bit positions are used for comparison while zero bit positions are ignored.
            tos: ToS (Type of Service) value used for comparison.
            tos_negate: Enable negated TOS match.
            traffic_shaper: Traffic shaper to apply to traffic forwarded by the firewall policy.
            traffic_shaper_reverse: Traffic shaper to apply to response traffic received by the firewall policy.
            per_ip_shaper: Per-IP traffic shaper to apply with this policy.
            class_id: Traffic class ID.
            diffserv_forward: Enable to change packet's DiffServ values to the specified diffservcode-forward value.
            diffserv_reverse: Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.
            diffservcode_forward: Change packet's DiffServ to this value.
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this value.
            cos_mask: VLAN CoS evaluated bits.
            cos: VLAN CoS bit pattern.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_shaping_policy.put(
            ...     id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_shaping_policy.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if srcaddr is not None:
            srcaddr = normalize_table_field(
                srcaddr,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr",
                example="[{'name': 'value'}]",
            )
        if dstaddr is not None:
            dstaddr = normalize_table_field(
                dstaddr,
                mkey="name",
                required_fields=['name'],
                field_name="dstaddr",
                example="[{'name': 'value'}]",
            )
        if srcaddr6 is not None:
            srcaddr6 = normalize_table_field(
                srcaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr6",
                example="[{'name': 'value'}]",
            )
        if dstaddr6 is not None:
            dstaddr6 = normalize_table_field(
                dstaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="dstaddr6",
                example="[{'name': 'value'}]",
            )
        if internet_service_name is not None:
            internet_service_name = normalize_table_field(
                internet_service_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_name",
                example="[{'name': 'value'}]",
            )
        if internet_service_group is not None:
            internet_service_group = normalize_table_field(
                internet_service_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_custom is not None:
            internet_service_custom = normalize_table_field(
                internet_service_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service_custom_group is not None:
            internet_service_custom_group = normalize_table_field(
                internet_service_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_fortiguard is not None:
            internet_service_fortiguard = normalize_table_field(
                internet_service_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_fortiguard",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_name is not None:
            internet_service_src_name = normalize_table_field(
                internet_service_src_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_name",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_group is not None:
            internet_service_src_group = normalize_table_field(
                internet_service_src_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_custom is not None:
            internet_service_src_custom = normalize_table_field(
                internet_service_src_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_custom_group is not None:
            internet_service_src_custom_group = normalize_table_field(
                internet_service_src_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_fortiguard is not None:
            internet_service_src_fortiguard = normalize_table_field(
                internet_service_src_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_fortiguard",
                example="[{'name': 'value'}]",
            )
        if service is not None:
            service = normalize_table_field(
                service,
                mkey="name",
                required_fields=['name'],
                field_name="service",
                example="[{'name': 'value'}]",
            )
        if users is not None:
            users = normalize_table_field(
                users,
                mkey="name",
                required_fields=['name'],
                field_name="users",
                example="[{'name': 'value'}]",
            )
        if groups is not None:
            groups = normalize_table_field(
                groups,
                mkey="name",
                required_fields=['name'],
                field_name="groups",
                example="[{'name': 'value'}]",
            )
        if application is not None:
            application = normalize_table_field(
                application,
                mkey="id",
                required_fields=['id'],
                field_name="application",
                example="[{'id': 1}]",
            )
        if app_category is not None:
            app_category = normalize_table_field(
                app_category,
                mkey="id",
                required_fields=['id'],
                field_name="app_category",
                example="[{'id': 1}]",
            )
        if app_group is not None:
            app_group = normalize_table_field(
                app_group,
                mkey="name",
                required_fields=['name'],
                field_name="app_group",
                example="[{'name': 'value'}]",
            )
        if url_category is not None:
            url_category = normalize_table_field(
                url_category,
                mkey="id",
                required_fields=['id'],
                field_name="url_category",
                example="[{'id': 1}]",
            )
        if srcintf is not None:
            srcintf = normalize_table_field(
                srcintf,
                mkey="name",
                required_fields=['name'],
                field_name="srcintf",
                example="[{'name': 'value'}]",
            )
        if dstintf is not None:
            dstintf = normalize_table_field(
                dstintf,
                mkey="name",
                required_fields=['name'],
                field_name="dstintf",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            id=id,
            uuid=uuid,
            name=name,
            comment=comment,
            status=status,
            ip_version=ip_version,
            traffic_type=traffic_type,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            service=service,
            schedule=schedule,
            users=users,
            groups=groups,
            application=application,
            app_category=app_category,
            app_group=app_group,
            url_category=url_category,
            srcintf=srcintf,
            dstintf=dstintf,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            class_id=class_id,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            cos_mask=cos_mask,
            cos=cos,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.shaping_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/shaping_policy",
            )
        
        id_value = payload_data.get("id")
        if not id_value:
            raise ValueError("id is required for PUT")
        endpoint = "/firewall/shaping-policy/" + str(id_value)

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
        id: int | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        ip_version: Literal["4", "6"] | None = None,
        traffic_type: Literal["forwarding", "local-in", "local-out"] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        schedule: str | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        application: str | list[str] | list[dict[str, Any]] | None = None,
        app_category: str | list[str] | list[dict[str, Any]] | None = None,
        app_group: str | list[str] | list[dict[str, Any]] | None = None,
        url_category: str | list[str] | list[dict[str, Any]] | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: Literal["enable", "disable"] | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        class_id: int | None = None,
        diffserv_forward: Literal["enable", "disable"] | None = None,
        diffserv_reverse: Literal["enable", "disable"] | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        cos_mask: str | None = None,
        cos: str | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new firewall/shaping_policy object.

        Configure shaping policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            id: Shaping policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            name: Shaping policy name.
            comment: Comments.
            status: Enable/disable this traffic shaping policy.
            ip_version: Apply this traffic shaping policy to IPv4 or IPv6 traffic.
            traffic_type: Traffic type.
            srcaddr: IPv4 source address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: IPv4 destination address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr6: IPv6 source address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: IPv6 destination address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.
            internet_service_name: Internet Service ID.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_group: Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_custom: Custom Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_custom_group: Custom Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_fortiguard: FortiGuard Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src: Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.
            internet_service_src_name: Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_group: Internet Service source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_custom: Custom Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_custom_group: Custom Internet Service source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_src_fortiguard: FortiGuard Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service: Service and service group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            schedule: Schedule name.
            users: Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            groups: Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            application: IDs of one or more applications that this shaper applies application control traffic shaping to.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            app_category: IDs of one or more application categories that this shaper applies application control traffic shaping to.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            app_group: One or more application group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            url_category: IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            srcintf: One or more incoming (ingress) interfaces.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstintf: One or more outgoing (egress) interfaces.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            tos_mask: Non-zero bit positions are used for comparison while zero bit positions are ignored.
            tos: ToS (Type of Service) value used for comparison.
            tos_negate: Enable negated TOS match.
            traffic_shaper: Traffic shaper to apply to traffic forwarded by the firewall policy.
            traffic_shaper_reverse: Traffic shaper to apply to response traffic received by the firewall policy.
            per_ip_shaper: Per-IP traffic shaper to apply with this policy.
            class_id: Traffic class ID.
            diffserv_forward: Enable to change packet's DiffServ values to the specified diffservcode-forward value.
            diffserv_reverse: Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.
            diffservcode_forward: Change packet's DiffServ to this value.
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this value.
            cos_mask: VLAN CoS evaluated bits.
            cos: VLAN CoS bit pattern.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_shaping_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = ShapingPolicy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_shaping_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(ShapingPolicy.required_fields()) }}
            
            Use ShapingPolicy.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if srcaddr is not None:
            srcaddr = normalize_table_field(
                srcaddr,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr",
                example="[{'name': 'value'}]",
            )
        if dstaddr is not None:
            dstaddr = normalize_table_field(
                dstaddr,
                mkey="name",
                required_fields=['name'],
                field_name="dstaddr",
                example="[{'name': 'value'}]",
            )
        if srcaddr6 is not None:
            srcaddr6 = normalize_table_field(
                srcaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr6",
                example="[{'name': 'value'}]",
            )
        if dstaddr6 is not None:
            dstaddr6 = normalize_table_field(
                dstaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="dstaddr6",
                example="[{'name': 'value'}]",
            )
        if internet_service_name is not None:
            internet_service_name = normalize_table_field(
                internet_service_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_name",
                example="[{'name': 'value'}]",
            )
        if internet_service_group is not None:
            internet_service_group = normalize_table_field(
                internet_service_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_custom is not None:
            internet_service_custom = normalize_table_field(
                internet_service_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service_custom_group is not None:
            internet_service_custom_group = normalize_table_field(
                internet_service_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_fortiguard is not None:
            internet_service_fortiguard = normalize_table_field(
                internet_service_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_fortiguard",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_name is not None:
            internet_service_src_name = normalize_table_field(
                internet_service_src_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_name",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_group is not None:
            internet_service_src_group = normalize_table_field(
                internet_service_src_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_custom is not None:
            internet_service_src_custom = normalize_table_field(
                internet_service_src_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_custom_group is not None:
            internet_service_src_custom_group = normalize_table_field(
                internet_service_src_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service_src_fortiguard is not None:
            internet_service_src_fortiguard = normalize_table_field(
                internet_service_src_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_src_fortiguard",
                example="[{'name': 'value'}]",
            )
        if service is not None:
            service = normalize_table_field(
                service,
                mkey="name",
                required_fields=['name'],
                field_name="service",
                example="[{'name': 'value'}]",
            )
        if users is not None:
            users = normalize_table_field(
                users,
                mkey="name",
                required_fields=['name'],
                field_name="users",
                example="[{'name': 'value'}]",
            )
        if groups is not None:
            groups = normalize_table_field(
                groups,
                mkey="name",
                required_fields=['name'],
                field_name="groups",
                example="[{'name': 'value'}]",
            )
        if application is not None:
            application = normalize_table_field(
                application,
                mkey="id",
                required_fields=['id'],
                field_name="application",
                example="[{'id': 1}]",
            )
        if app_category is not None:
            app_category = normalize_table_field(
                app_category,
                mkey="id",
                required_fields=['id'],
                field_name="app_category",
                example="[{'id': 1}]",
            )
        if app_group is not None:
            app_group = normalize_table_field(
                app_group,
                mkey="name",
                required_fields=['name'],
                field_name="app_group",
                example="[{'name': 'value'}]",
            )
        if url_category is not None:
            url_category = normalize_table_field(
                url_category,
                mkey="id",
                required_fields=['id'],
                field_name="url_category",
                example="[{'id': 1}]",
            )
        if srcintf is not None:
            srcintf = normalize_table_field(
                srcintf,
                mkey="name",
                required_fields=['name'],
                field_name="srcintf",
                example="[{'name': 'value'}]",
            )
        if dstintf is not None:
            dstintf = normalize_table_field(
                dstintf,
                mkey="name",
                required_fields=['name'],
                field_name="dstintf",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            id=id,
            uuid=uuid,
            name=name,
            comment=comment,
            status=status,
            ip_version=ip_version,
            traffic_type=traffic_type,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            service=service,
            schedule=schedule,
            users=users,
            groups=groups,
            application=application,
            app_category=app_category,
            app_group=app_group,
            url_category=url_category,
            srcintf=srcintf,
            dstintf=dstintf,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            class_id=class_id,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            cos_mask=cos_mask,
            cos=cos,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.shaping_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/shaping_policy",
            )

        endpoint = "/firewall/shaping-policy"
        
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
        id: int | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete firewall/shaping_policy object.

        Configure shaping policies.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_shaping_policy.delete(id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not id:
            raise ValueError("id is required for DELETE")
        endpoint = "/firewall/shaping-policy/" + str(id)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/shaping_policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_shaping_policy.exists(id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_shaping_policy.exists(id=1):
            ...     fgt.api.cmdb.firewall_shaping_policy.delete(id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                id=id,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        id: int | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        ip_version: Literal["4", "6"] | None = None,
        traffic_type: Literal["forwarding", "local-in", "local-out"] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        schedule: str | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        application: str | list[str] | list[dict[str, Any]] | None = None,
        app_category: str | list[str] | list[dict[str, Any]] | None = None,
        app_group: str | list[str] | list[dict[str, Any]] | None = None,
        url_category: str | list[str] | list[dict[str, Any]] | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: Literal["enable", "disable"] | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        class_id: int | None = None,
        diffserv_forward: Literal["enable", "disable"] | None = None,
        diffserv_reverse: Literal["enable", "disable"] | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        cos_mask: str | None = None,
        cos: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/shaping_policy object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (id) in the payload.

        Args:
            payload_dict: Resource data including id (primary key)
            id: Field id
            uuid: Field uuid
            name: Field name
            comment: Field comment
            status: Field status
            ip_version: Field ip-version
            traffic_type: Field traffic-type
            srcaddr: Field srcaddr
            dstaddr: Field dstaddr
            srcaddr6: Field srcaddr6
            dstaddr6: Field dstaddr6
            internet_service: Field internet-service
            internet_service_name: Field internet-service-name
            internet_service_group: Field internet-service-group
            internet_service_custom: Field internet-service-custom
            internet_service_custom_group: Field internet-service-custom-group
            internet_service_fortiguard: Field internet-service-fortiguard
            internet_service_src: Field internet-service-src
            internet_service_src_name: Field internet-service-src-name
            internet_service_src_group: Field internet-service-src-group
            internet_service_src_custom: Field internet-service-src-custom
            internet_service_src_custom_group: Field internet-service-src-custom-group
            internet_service_src_fortiguard: Field internet-service-src-fortiguard
            service: Field service
            schedule: Field schedule
            users: Field users
            groups: Field groups
            application: Field application
            app_category: Field app-category
            app_group: Field app-group
            url_category: Field url-category
            srcintf: Field srcintf
            dstintf: Field dstintf
            tos_mask: Field tos-mask
            tos: Field tos
            tos_negate: Field tos-negate
            traffic_shaper: Field traffic-shaper
            traffic_shaper_reverse: Field traffic-shaper-reverse
            per_ip_shaper: Field per-ip-shaper
            class_id: Field class-id
            diffserv_forward: Field diffserv-forward
            diffserv_reverse: Field diffserv-reverse
            diffservcode_forward: Field diffservcode-forward
            diffservcode_rev: Field diffservcode-rev
            cos_mask: Field cos-mask
            cos: Field cos
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.firewall_shaping_policy.set(
            ...     id=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_shaping_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_shaping_policy.set(payload_dict=obj_data)
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
            id=id,
            uuid=uuid,
            name=name,
            comment=comment,
            status=status,
            ip_version=ip_version,
            traffic_type=traffic_type,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            service=service,
            schedule=schedule,
            users=users,
            groups=groups,
            application=application,
            app_category=app_category,
            app_group=app_group,
            url_category=url_category,
            srcintf=srcintf,
            dstintf=dstintf,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            class_id=class_id,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            cos_mask=cos_mask,
            cos=cos,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("id")
        if not mkey_value:
            raise ValueError("id is required for set()")
        
        # Check if resource exists
        if self.exists(id=mkey_value, vdom=vdom):
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
        id: int,
        action: Literal["before", "after"],
        reference_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move firewall/shaping_policy object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.firewall_shaping_policy.move(
            ...     id=100,
            ...     action="before",
            ...     reference_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/shaping-policy",
            params={
                "id": id,
                "action": "move",
                action: reference_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        id: int,
        new_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone firewall/shaping_policy object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            id: Identifier of object to clone
            new_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.firewall_shaping_policy.clone(
            ...     id=1,
            ...     new_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/shaping-policy",
            params={
                "id": id,
                "new_id": new_id,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if firewall/shaping_policy object exists.
        
        Args:
            id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_shaping_policy.exists(id=1):
            ...     fgt.api.cmdb.firewall_shaping_policy.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                id=id,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


"""
FortiOS CMDB - Firewall security_policy

Configuration endpoint for managing cmdb firewall/security_policy objects.

API Endpoints:
    GET    /cmdb/firewall/security_policy
    POST   /cmdb/firewall/security_policy
    PUT    /cmdb/firewall/security_policy/{identifier}
    DELETE /cmdb/firewall/security_policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_security_policy.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.firewall_security_policy.post(
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

class SecurityPolicy(CRUDEndpoint, MetadataMixin):
    """SecurityPolicy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "security_policy"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
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
        "internet_service6_name": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_custom": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_custom_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_fortiguard": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_src_name": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_src_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_src_custom": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_src_custom_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_src_fortiguard": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "service": {
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
        "groups": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "users": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "fsso_groups": {
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
        """Initialize SecurityPolicy endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        policyid: int | None = None,
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
        Retrieve firewall/security_policy configuration.

        Configure NGFW IPv4/IPv6 application policies.

        Args:
            policyid: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/security_policy objects
            >>> result = fgt.api.cmdb.firewall_security_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/security_policy by policyid
            >>> result = fgt.api.cmdb.firewall_security_policy.get(policyid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_security_policy.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_security_policy.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_security_policy.get_schema()

        See Also:
            - post(): Create new firewall/security_policy object
            - put(): Update existing firewall/security_policy object
            - delete(): Remove firewall/security_policy object
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
        
        if policyid:
            endpoint = "/firewall/security-policy/" + str(policyid)
            unwrap_single = True
        else:
            endpoint = "/firewall/security-policy"
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
            >>> schema = fgt.api.cmdb.firewall_security_policy.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_security_policy.get_schema(format="json-schema")
        
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
        uuid: str | None = None,
        policyid: int | None = None,
        name: str | None = None,
        comments: str | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6_negate: Literal["enable", "disable"] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6_negate: Literal["enable", "disable"] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_negate: Literal["enable", "disable"] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src: Literal["enable", "disable"] | None = None,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_negate: Literal["enable", "disable"] | None = None,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        enforce_default_app_port: Literal["enable", "disable"] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny"] | None = None,
        send_deny_packet: Literal["disable", "enable"] | None = None,
        schedule: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        learning_mode: Literal["enable", "disable"] | None = None,
        nat46: Literal["enable", "disable"] | None = None,
        nat64: Literal["enable", "disable"] | None = None,
        profile_type: Literal["single", "group"] | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        application: str | list[str] | list[dict[str, Any]] | None = None,
        app_category: str | list[str] | list[dict[str, Any]] | None = None,
        url_category: str | list[str] | None = None,
        app_group: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing firewall/security_policy object.

        Configure NGFW IPv4/IPv6 application policies.

        Args:
            payload_dict: Object data as dict. Must include policyid (primary key).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            policyid: Policy ID.
            name: Policy name.
            comments: Comment.
            srcintf: Incoming (ingress) interface.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstintf: Outgoing (egress) interface.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr: Source IPv4 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr_negate: When enabled srcaddr specifies what the source address must NOT be.
            dstaddr: Destination IPv4 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr_negate: When enabled dstaddr specifies what the destination address must NOT be.
            srcaddr6: Source IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source address must NOT be.
            dstaddr6: Destination IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6_negate: When enabled dstaddr6 specifies what the destination address must NOT be.
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.
            internet_service_name: Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_negate: When enabled internet-service specifies what the service must NOT be.
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
            internet_service_src_negate: When enabled internet-service-src specifies what the service must NOT be.
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
            internet_service6: Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.
            internet_service6_name: IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_negate: When enabled internet-service6 specifies what the service must NOT be.
            internet_service6_group: Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom: Custom IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom_group: Custom IPv6 Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src: Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.
            internet_service6_src_name: IPv6 Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_negate: When enabled internet-service6-src specifies what the service must NOT be.
            internet_service6_src_group: Internet Service6 source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_custom: Custom IPv6 Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_custom_group: Custom Internet Service6 source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            enforce_default_app_port: Enable/disable default application port enforcement for allowed applications.
            service: Service and service group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service_negate: When enabled service specifies what the service must NOT be.
            action: Policy action (accept/deny).
            send_deny_packet: Enable to send a reply when a session is denied or blocked by a firewall policy.
            schedule: Schedule name.
            status: Enable or disable this policy.
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions.
            learning_mode: Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated.
            nat46: Enable/disable NAT46.
            nat64: Enable/disable NAT64.
            profile_type: Determine whether the firewall policy allows security profile groups or single profiles only.
            profile_group: Name of profile group.
            profile_protocol_options: Name of an existing Protocol options profile.
            ssl_ssh_profile: Name of an existing SSL SSH profile.
            av_profile: Name of an existing Antivirus profile.
            webfilter_profile: Name of an existing Web filter profile.
            dnsfilter_profile: Name of an existing DNS filter profile.
            emailfilter_profile: Name of an existing email filter profile.
            dlp_profile: Name of an existing DLP profile.
            file_filter_profile: Name of an existing file-filter profile.
            ips_sensor: Name of an existing IPS sensor.
            application_list: Name of an existing Application list.
            voip_profile: Name of an existing VoIP (voipd) profile.
            ips_voip_filter: Name of an existing VoIP (ips) profile.
            sctp_filter_profile: Name of an existing SCTP filter profile.
            diameter_filter_profile: Name of an existing Diameter filter profile.
            virtual_patch_profile: Name of an existing virtual-patch profile.
            icap_profile: Name of an existing ICAP profile.
            videofilter_profile: Name of an existing VideoFilter profile.
            ssh_filter_profile: Name of an existing SSH filter profile.
            casb_profile: Name of an existing CASB profile.
            application: Application ID list.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            app_category: Application category ID list.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            url_category: URL categories or groups.
            app_group: Application group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            groups: Names of user groups that can authenticate with this policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            users: Names of individual users that can authenticate with this policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            fsso_groups: Names of FSSO groups.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_security_policy.put(
            ...     policyid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_security_policy.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
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
        if internet_service6_name is not None:
            internet_service6_name = normalize_table_field(
                internet_service6_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_name",
                example="[{'name': 'value'}]",
            )
        if internet_service6_group is not None:
            internet_service6_group = normalize_table_field(
                internet_service6_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_custom is not None:
            internet_service6_custom = normalize_table_field(
                internet_service6_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service6_custom_group is not None:
            internet_service6_custom_group = normalize_table_field(
                internet_service6_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_fortiguard is not None:
            internet_service6_fortiguard = normalize_table_field(
                internet_service6_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_fortiguard",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_name is not None:
            internet_service6_src_name = normalize_table_field(
                internet_service6_src_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_name",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_group is not None:
            internet_service6_src_group = normalize_table_field(
                internet_service6_src_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_custom is not None:
            internet_service6_src_custom = normalize_table_field(
                internet_service6_src_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_custom_group is not None:
            internet_service6_src_custom_group = normalize_table_field(
                internet_service6_src_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_fortiguard is not None:
            internet_service6_src_fortiguard = normalize_table_field(
                internet_service6_src_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_fortiguard",
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
        if groups is not None:
            groups = normalize_table_field(
                groups,
                mkey="name",
                required_fields=['name'],
                field_name="groups",
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
        if fsso_groups is not None:
            fsso_groups = normalize_table_field(
                fsso_groups,
                mkey="name",
                required_fields=['name'],
                field_name="fsso_groups",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            uuid=uuid,
            policyid=policyid,
            name=name,
            comments=comments,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            srcaddr_negate=srcaddr_negate,
            dstaddr=dstaddr,
            dstaddr_negate=dstaddr_negate,
            srcaddr6=srcaddr6,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr6=dstaddr6,
            dstaddr6_negate=dstaddr6_negate,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_negate=internet_service_negate,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_negate=internet_service_src_negate,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_negate=internet_service6_negate,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_negate=internet_service6_src_negate,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            enforce_default_app_port=enforce_default_app_port,
            service=service,
            service_negate=service_negate,
            action=action,
            send_deny_packet=send_deny_packet,
            schedule=schedule,
            status=status,
            logtraffic=logtraffic,
            learning_mode=learning_mode,
            nat46=nat46,
            nat64=nat64,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            voip_profile=voip_profile,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            diameter_filter_profile=diameter_filter_profile,
            virtual_patch_profile=virtual_patch_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            application=application,
            app_category=app_category,
            url_category=url_category,
            app_group=app_group,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.security_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/security_policy",
            )
        
        policyid_value = payload_data.get("policyid")
        if not policyid_value:
            raise ValueError("policyid is required for PUT")
        endpoint = "/firewall/security-policy/" + str(policyid_value)

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
        uuid: str | None = None,
        policyid: int | None = None,
        name: str | None = None,
        comments: str | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6_negate: Literal["enable", "disable"] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6_negate: Literal["enable", "disable"] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_negate: Literal["enable", "disable"] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src: Literal["enable", "disable"] | None = None,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_negate: Literal["enable", "disable"] | None = None,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        enforce_default_app_port: Literal["enable", "disable"] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny"] | None = None,
        send_deny_packet: Literal["disable", "enable"] | None = None,
        schedule: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        learning_mode: Literal["enable", "disable"] | None = None,
        nat46: Literal["enable", "disable"] | None = None,
        nat64: Literal["enable", "disable"] | None = None,
        profile_type: Literal["single", "group"] | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        application: str | list[str] | list[dict[str, Any]] | None = None,
        app_category: str | list[str] | list[dict[str, Any]] | None = None,
        url_category: str | list[str] | None = None,
        app_group: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new firewall/security_policy object.

        Configure NGFW IPv4/IPv6 application policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            policyid: Policy ID.
            name: Policy name.
            comments: Comment.
            srcintf: Incoming (ingress) interface.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstintf: Outgoing (egress) interface.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr: Source IPv4 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr_negate: When enabled srcaddr specifies what the source address must NOT be.
            dstaddr: Destination IPv4 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr_negate: When enabled dstaddr specifies what the destination address must NOT be.
            srcaddr6: Source IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr6_negate: When enabled srcaddr6 specifies what the source address must NOT be.
            dstaddr6: Destination IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6_negate: When enabled dstaddr6 specifies what the destination address must NOT be.
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.
            internet_service_name: Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service_negate: When enabled internet-service specifies what the service must NOT be.
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
            internet_service_src_negate: When enabled internet-service-src specifies what the service must NOT be.
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
            internet_service6: Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.
            internet_service6_name: IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_negate: When enabled internet-service6 specifies what the service must NOT be.
            internet_service6_group: Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom: Custom IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom_group: Custom IPv6 Internet Service group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src: Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.
            internet_service6_src_name: IPv6 Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_negate: When enabled internet-service6-src specifies what the service must NOT be.
            internet_service6_src_group: Internet Service6 source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_custom: Custom IPv6 Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_custom_group: Custom Internet Service6 source group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_src_fortiguard: FortiGuard IPv6 Internet Service source name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            enforce_default_app_port: Enable/disable default application port enforcement for allowed applications.
            service: Service and service group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service_negate: When enabled service specifies what the service must NOT be.
            action: Policy action (accept/deny).
            send_deny_packet: Enable to send a reply when a session is denied or blocked by a firewall policy.
            schedule: Schedule name.
            status: Enable or disable this policy.
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions.
            learning_mode: Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated.
            nat46: Enable/disable NAT46.
            nat64: Enable/disable NAT64.
            profile_type: Determine whether the firewall policy allows security profile groups or single profiles only.
            profile_group: Name of profile group.
            profile_protocol_options: Name of an existing Protocol options profile.
            ssl_ssh_profile: Name of an existing SSL SSH profile.
            av_profile: Name of an existing Antivirus profile.
            webfilter_profile: Name of an existing Web filter profile.
            dnsfilter_profile: Name of an existing DNS filter profile.
            emailfilter_profile: Name of an existing email filter profile.
            dlp_profile: Name of an existing DLP profile.
            file_filter_profile: Name of an existing file-filter profile.
            ips_sensor: Name of an existing IPS sensor.
            application_list: Name of an existing Application list.
            voip_profile: Name of an existing VoIP (voipd) profile.
            ips_voip_filter: Name of an existing VoIP (ips) profile.
            sctp_filter_profile: Name of an existing SCTP filter profile.
            diameter_filter_profile: Name of an existing Diameter filter profile.
            virtual_patch_profile: Name of an existing virtual-patch profile.
            icap_profile: Name of an existing ICAP profile.
            videofilter_profile: Name of an existing VideoFilter profile.
            ssh_filter_profile: Name of an existing SSH filter profile.
            casb_profile: Name of an existing CASB profile.
            application: Application ID list.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            app_category: Application category ID list.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            url_category: URL categories or groups.
            app_group: Application group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            groups: Names of user groups that can authenticate with this policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            users: Names of individual users that can authenticate with this policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            fsso_groups: Names of FSSO groups.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_security_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created policyid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = SecurityPolicy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_security_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(SecurityPolicy.required_fields()) }}
            
            Use SecurityPolicy.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
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
        if internet_service6_name is not None:
            internet_service6_name = normalize_table_field(
                internet_service6_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_name",
                example="[{'name': 'value'}]",
            )
        if internet_service6_group is not None:
            internet_service6_group = normalize_table_field(
                internet_service6_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_custom is not None:
            internet_service6_custom = normalize_table_field(
                internet_service6_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service6_custom_group is not None:
            internet_service6_custom_group = normalize_table_field(
                internet_service6_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_fortiguard is not None:
            internet_service6_fortiguard = normalize_table_field(
                internet_service6_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_fortiguard",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_name is not None:
            internet_service6_src_name = normalize_table_field(
                internet_service6_src_name,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_name",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_group is not None:
            internet_service6_src_group = normalize_table_field(
                internet_service6_src_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_custom is not None:
            internet_service6_src_custom = normalize_table_field(
                internet_service6_src_custom,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_custom",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_custom_group is not None:
            internet_service6_src_custom_group = normalize_table_field(
                internet_service6_src_custom_group,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_custom_group",
                example="[{'name': 'value'}]",
            )
        if internet_service6_src_fortiguard is not None:
            internet_service6_src_fortiguard = normalize_table_field(
                internet_service6_src_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_src_fortiguard",
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
        if groups is not None:
            groups = normalize_table_field(
                groups,
                mkey="name",
                required_fields=['name'],
                field_name="groups",
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
        if fsso_groups is not None:
            fsso_groups = normalize_table_field(
                fsso_groups,
                mkey="name",
                required_fields=['name'],
                field_name="fsso_groups",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            uuid=uuid,
            policyid=policyid,
            name=name,
            comments=comments,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            srcaddr_negate=srcaddr_negate,
            dstaddr=dstaddr,
            dstaddr_negate=dstaddr_negate,
            srcaddr6=srcaddr6,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr6=dstaddr6,
            dstaddr6_negate=dstaddr6_negate,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_negate=internet_service_negate,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_negate=internet_service_src_negate,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_negate=internet_service6_negate,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_negate=internet_service6_src_negate,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            enforce_default_app_port=enforce_default_app_port,
            service=service,
            service_negate=service_negate,
            action=action,
            send_deny_packet=send_deny_packet,
            schedule=schedule,
            status=status,
            logtraffic=logtraffic,
            learning_mode=learning_mode,
            nat46=nat46,
            nat64=nat64,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            voip_profile=voip_profile,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            diameter_filter_profile=diameter_filter_profile,
            virtual_patch_profile=virtual_patch_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            application=application,
            app_category=app_category,
            url_category=url_category,
            app_group=app_group,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.security_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/security_policy",
            )

        endpoint = "/firewall/security-policy"
        
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
        policyid: int | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete firewall/security_policy object.

        Configure NGFW IPv4/IPv6 application policies.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If policyid is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_security_policy.delete(policyid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not policyid:
            raise ValueError("policyid is required for DELETE")
        endpoint = "/firewall/security-policy/" + str(policyid)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/security_policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_security_policy.exists(policyid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_security_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_security_policy.delete(policyid=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/firewall/security_policy"
        endpoint = f"{endpoint}/{policyid}"
        
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
        uuid: str | None = None,
        policyid: int | None = None,
        name: str | None = None,
        comments: str | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6_negate: Literal["enable", "disable"] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6_negate: Literal["enable", "disable"] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_negate: Literal["enable", "disable"] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src: Literal["enable", "disable"] | None = None,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_negate: Literal["enable", "disable"] | None = None,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        enforce_default_app_port: Literal["enable", "disable"] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny"] | None = None,
        send_deny_packet: Literal["disable", "enable"] | None = None,
        schedule: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        learning_mode: Literal["enable", "disable"] | None = None,
        nat46: Literal["enable", "disable"] | None = None,
        nat64: Literal["enable", "disable"] | None = None,
        profile_type: Literal["single", "group"] | None = None,
        profile_group: str | None = None,
        profile_protocol_options: str | None = None,
        ssl_ssh_profile: str | None = None,
        av_profile: str | None = None,
        webfilter_profile: str | None = None,
        dnsfilter_profile: str | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile: str | None = None,
        file_filter_profile: str | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        voip_profile: str | None = None,
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        diameter_filter_profile: str | None = None,
        virtual_patch_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        application: str | list[str] | list[dict[str, Any]] | None = None,
        app_category: str | list[str] | list[dict[str, Any]] | None = None,
        url_category: str | list[str] | list[dict[str, Any]] | None = None,
        app_group: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/security_policy object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (policyid) in the payload.

        Args:
            payload_dict: Resource data including policyid (primary key)
            uuid: Field uuid
            policyid: Field policyid
            name: Field name
            comments: Field comments
            srcintf: Field srcintf
            dstintf: Field dstintf
            srcaddr: Field srcaddr
            srcaddr_negate: Field srcaddr-negate
            dstaddr: Field dstaddr
            dstaddr_negate: Field dstaddr-negate
            srcaddr6: Field srcaddr6
            srcaddr6_negate: Field srcaddr6-negate
            dstaddr6: Field dstaddr6
            dstaddr6_negate: Field dstaddr6-negate
            internet_service: Field internet-service
            internet_service_name: Field internet-service-name
            internet_service_negate: Field internet-service-negate
            internet_service_group: Field internet-service-group
            internet_service_custom: Field internet-service-custom
            internet_service_custom_group: Field internet-service-custom-group
            internet_service_fortiguard: Field internet-service-fortiguard
            internet_service_src: Field internet-service-src
            internet_service_src_name: Field internet-service-src-name
            internet_service_src_negate: Field internet-service-src-negate
            internet_service_src_group: Field internet-service-src-group
            internet_service_src_custom: Field internet-service-src-custom
            internet_service_src_custom_group: Field internet-service-src-custom-group
            internet_service_src_fortiguard: Field internet-service-src-fortiguard
            internet_service6: Field internet-service6
            internet_service6_name: Field internet-service6-name
            internet_service6_negate: Field internet-service6-negate
            internet_service6_group: Field internet-service6-group
            internet_service6_custom: Field internet-service6-custom
            internet_service6_custom_group: Field internet-service6-custom-group
            internet_service6_fortiguard: Field internet-service6-fortiguard
            internet_service6_src: Field internet-service6-src
            internet_service6_src_name: Field internet-service6-src-name
            internet_service6_src_negate: Field internet-service6-src-negate
            internet_service6_src_group: Field internet-service6-src-group
            internet_service6_src_custom: Field internet-service6-src-custom
            internet_service6_src_custom_group: Field internet-service6-src-custom-group
            internet_service6_src_fortiguard: Field internet-service6-src-fortiguard
            enforce_default_app_port: Field enforce-default-app-port
            service: Field service
            service_negate: Field service-negate
            action: Field action
            send_deny_packet: Field send-deny-packet
            schedule: Field schedule
            status: Field status
            logtraffic: Field logtraffic
            learning_mode: Field learning-mode
            nat46: Field nat46
            nat64: Field nat64
            profile_type: Field profile-type
            profile_group: Field profile-group
            profile_protocol_options: Field profile-protocol-options
            ssl_ssh_profile: Field ssl-ssh-profile
            av_profile: Field av-profile
            webfilter_profile: Field webfilter-profile
            dnsfilter_profile: Field dnsfilter-profile
            emailfilter_profile: Field emailfilter-profile
            dlp_profile: Field dlp-profile
            file_filter_profile: Field file-filter-profile
            ips_sensor: Field ips-sensor
            application_list: Field application-list
            voip_profile: Field voip-profile
            ips_voip_filter: Field ips-voip-filter
            sctp_filter_profile: Field sctp-filter-profile
            diameter_filter_profile: Field diameter-filter-profile
            virtual_patch_profile: Field virtual-patch-profile
            icap_profile: Field icap-profile
            videofilter_profile: Field videofilter-profile
            ssh_filter_profile: Field ssh-filter-profile
            casb_profile: Field casb-profile
            application: Field application
            app_category: Field app-category
            url_category: Field url-category
            app_group: Field app-group
            groups: Field groups
            users: Field users
            fsso_groups: Field fsso-groups
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.firewall_security_policy.set(
            ...     policyid=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_security_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_security_policy.set(payload_dict=obj_data)
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
            uuid=uuid,
            policyid=policyid,
            name=name,
            comments=comments,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            srcaddr_negate=srcaddr_negate,
            dstaddr=dstaddr,
            dstaddr_negate=dstaddr_negate,
            srcaddr6=srcaddr6,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr6=dstaddr6,
            dstaddr6_negate=dstaddr6_negate,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_negate=internet_service_negate,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_negate=internet_service_src_negate,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            internet_service_src_custom_group=internet_service_src_custom_group,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_negate=internet_service6_negate,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_negate=internet_service6_src_negate,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            enforce_default_app_port=enforce_default_app_port,
            service=service,
            service_negate=service_negate,
            action=action,
            send_deny_packet=send_deny_packet,
            schedule=schedule,
            status=status,
            logtraffic=logtraffic,
            learning_mode=learning_mode,
            nat46=nat46,
            nat64=nat64,
            profile_type=profile_type,
            profile_group=profile_group,
            profile_protocol_options=profile_protocol_options,
            ssl_ssh_profile=ssl_ssh_profile,
            av_profile=av_profile,
            webfilter_profile=webfilter_profile,
            dnsfilter_profile=dnsfilter_profile,
            emailfilter_profile=emailfilter_profile,
            dlp_profile=dlp_profile,
            file_filter_profile=file_filter_profile,
            ips_sensor=ips_sensor,
            application_list=application_list,
            voip_profile=voip_profile,
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            diameter_filter_profile=diameter_filter_profile,
            virtual_patch_profile=virtual_patch_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            application=application,
            app_category=app_category,
            url_category=url_category,
            app_group=app_group,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("policyid")
        if not mkey_value:
            raise ValueError("policyid is required for set()")
        
        # Check if resource exists
        if self.exists(policyid=mkey_value, vdom=vdom):
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
        policyid: int,
        action: Literal["before", "after"],
        reference_policyid: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move firewall/security_policy object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            policyid: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_policyid: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.firewall_security_policy.move(
            ...     policyid=100,
            ...     action="before",
            ...     reference_policyid=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/security-policy",
            params={
                "policyid": policyid,
                "action": "move",
                action: reference_policyid,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        policyid: int,
        new_policyid: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone firewall/security_policy object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            policyid: Identifier of object to clone
            new_policyid: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.firewall_security_policy.clone(
            ...     policyid=1,
            ...     new_policyid=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/security-policy",
            params={
                "policyid": policyid,
                "new_policyid": new_policyid,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )



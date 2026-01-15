"""
FortiOS CMDB - Firewall proxy_policy

Configuration endpoint for managing cmdb firewall/proxy_policy objects.

API Endpoints:
    GET    /cmdb/firewall/proxy_policy
    POST   /cmdb/firewall/proxy_policy
    PUT    /cmdb/firewall/proxy_policy/{identifier}
    DELETE /cmdb/firewall/proxy_policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_proxy_policy.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.firewall_proxy_policy.post(
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

class ProxyPolicy(CRUDEndpoint, MetadataMixin):
    """ProxyPolicy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "proxy_policy"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "access_proxy": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "access_proxy6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "ztna_proxy": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
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
        "srcaddr": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "poolname": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "poolname6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "dstaddr": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "ztna_ems_tag": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "url_risk": {
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
        "service": {
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
        """Initialize ProxyPolicy endpoint."""
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
        Retrieve firewall/proxy_policy configuration.

        Configure proxy policies.

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
            >>> # Get all firewall/proxy_policy objects
            >>> result = fgt.api.cmdb.firewall_proxy_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/proxy_policy by policyid
            >>> result = fgt.api.cmdb.firewall_proxy_policy.get(policyid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_proxy_policy.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_proxy_policy.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_proxy_policy.get_schema()

        See Also:
            - post(): Create new firewall/proxy_policy object
            - put(): Update existing firewall/proxy_policy object
            - delete(): Remove firewall/proxy_policy object
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
            endpoint = "/firewall/proxy-policy/" + str(policyid)
            unwrap_single = True
        else:
            endpoint = "/firewall/proxy-policy"
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
            >>> schema = fgt.api.cmdb.firewall_proxy_policy.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_proxy_policy.get_schema(format="json-schema")
        
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
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = None,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = None,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        poolname: str | list[str] | list[dict[str, Any]] | None = None,
        poolname6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        device_ownership: Literal["enable", "disable"] | None = None,
        url_risk: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        schedule: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        session_ttl: int | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        http_tunnel_auth: Literal["enable", "disable"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: Literal["enable", "disable"] | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
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
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        replacemsg_override_group: str | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        redirect_url: str | None = None,
        https_sub_category: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: Literal["enable", "disable"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing firewall/proxy_policy object.

        Configure proxy policies.

        Args:
            payload_dict: Object data as dict. Must include policyid (primary key).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            policyid: Policy ID.
            name: Policy name.
            proxy: Type of explicit proxy.
            access_proxy: IPv4 access proxy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            access_proxy6: IPv6 access proxy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_proxy: ZTNA proxies.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcintf: Source interface names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstintf: Destination interface names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr: Source address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            poolname: Name of IP pool object.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            poolname6: Name of IPv6 pool object.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: Destination address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_ems_tag: ZTNA EMS Tag names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_tags_match_logic: ZTNA tag matching logic.
            device_ownership: When enabled, the ownership enforcement will be done at policy level.
            url_risk: URL risk level name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.
            internet_service_negate: When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.
            internet_service_name: Internet Service name.
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
            internet_service6: Enable/disable use of Internet Services IPv6 for this policy. If enabled, destination IPv6 address and service are not used.
            internet_service6_negate: When enabled, Internet Services match against any internet service IPv6 EXCEPT the selected Internet Service IPv6.
            internet_service6_name: Internet Service IPv6 name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_group: Internet Service IPv6 group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom: Custom Internet Service IPv6 name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom_group: Custom Internet Service IPv6 group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_fortiguard: FortiGuard Internet Service IPv6 name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service: Name of service objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr_negate: When enabled, source addresses match against any address EXCEPT the specified source addresses.
            dstaddr_negate: When enabled, destination addresses match against any address EXCEPT the specified destination addresses.
            ztna_ems_tag_negate: When enabled, ZTNA EMS tags match against any tag EXCEPT the specified ZTNA EMS tags.
            service_negate: When enabled, services match against any service EXCEPT the specified destination services.
            action: Accept or deny traffic matching the policy parameters.
            status: Enable/disable the active status of the policy.
            schedule: Name of schedule object.
            logtraffic: Enable/disable logging traffic through the policy.
            session_ttl: TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).
            srcaddr6: IPv6 source address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: IPv6 destination address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            groups: Names of group objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            users: Names of user objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            http_tunnel_auth: Enable/disable HTTP tunnel authentication.
            ssh_policy_redirect: Redirect SSH traffic to matching transparent proxy policy.
            webproxy_forward_server: Web proxy forward server name.
            isolator_server: Isolator server name.
            webproxy_profile: Name of web proxy profile.
            transparent: Enable to use the IP address of the client to connect to the server.
            webcache: Enable/disable web caching.
            webcache_https: Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).
            disclaimer: Web proxy disclaimer setting: by domain, policy, or user.
            utm_status: Enable the use of UTM profiles/sensors/lists.
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
            ips_voip_filter: Name of an existing VoIP (ips) profile.
            sctp_filter_profile: Name of an existing SCTP filter profile.
            icap_profile: Name of an existing ICAP profile.
            videofilter_profile: Name of an existing VideoFilter profile.
            waf_profile: Name of an existing Web application firewall profile.
            ssh_filter_profile: Name of an existing SSH filter profile.
            casb_profile: Name of an existing CASB profile.
            replacemsg_override_group: Authentication replacement message override group.
            logtraffic_start: Enable/disable policy log traffic start.
            log_http_transaction: Enable/disable HTTP transaction log.
            comments: Optional comments.
            block_notification: Enable/disable block notification.
            redirect_url: Redirect URL for further explicit web proxy processing.
            https_sub_category: Enable/disable HTTPS sub-category policy matching.
            decrypted_traffic_mirror: Decrypted traffic mirror.
            detect_https_in_http_request: Enable/disable detection of HTTPS in HTTP request.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_proxy_policy.put(
            ...     policyid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_proxy_policy.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if access_proxy is not None:
            access_proxy = normalize_table_field(
                access_proxy,
                mkey="name",
                required_fields=['name'],
                field_name="access_proxy",
                example="[{'name': 'value'}]",
            )
        if access_proxy6 is not None:
            access_proxy6 = normalize_table_field(
                access_proxy6,
                mkey="name",
                required_fields=['name'],
                field_name="access_proxy6",
                example="[{'name': 'value'}]",
            )
        if ztna_proxy is not None:
            ztna_proxy = normalize_table_field(
                ztna_proxy,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_proxy",
                example="[{'name': 'value'}]",
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
        if srcaddr is not None:
            srcaddr = normalize_table_field(
                srcaddr,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr",
                example="[{'name': 'value'}]",
            )
        if poolname is not None:
            poolname = normalize_table_field(
                poolname,
                mkey="name",
                required_fields=['name'],
                field_name="poolname",
                example="[{'name': 'value'}]",
            )
        if poolname6 is not None:
            poolname6 = normalize_table_field(
                poolname6,
                mkey="name",
                required_fields=['name'],
                field_name="poolname6",
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
        if ztna_ems_tag is not None:
            ztna_ems_tag = normalize_table_field(
                ztna_ems_tag,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_ems_tag",
                example="[{'name': 'value'}]",
            )
        if url_risk is not None:
            url_risk = normalize_table_field(
                url_risk,
                mkey="name",
                required_fields=['name'],
                field_name="url_risk",
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
        if service is not None:
            service = normalize_table_field(
                service,
                mkey="name",
                required_fields=['name'],
                field_name="service",
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
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            uuid=uuid,
            policyid=policyid,
            name=name,
            proxy=proxy,
            access_proxy=access_proxy,
            access_proxy6=access_proxy6,
            ztna_proxy=ztna_proxy,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            poolname=poolname,
            poolname6=poolname6,
            dstaddr=dstaddr,
            ztna_ems_tag=ztna_ems_tag,
            ztna_tags_match_logic=ztna_tags_match_logic,
            device_ownership=device_ownership,
            url_risk=url_risk,
            internet_service=internet_service,
            internet_service_negate=internet_service_negate,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service6=internet_service6,
            internet_service6_negate=internet_service6_negate,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            service=service,
            srcaddr_negate=srcaddr_negate,
            dstaddr_negate=dstaddr_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            action=action,
            status=status,
            schedule=schedule,
            logtraffic=logtraffic,
            session_ttl=session_ttl,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            groups=groups,
            users=users,
            http_tunnel_auth=http_tunnel_auth,
            ssh_policy_redirect=ssh_policy_redirect,
            webproxy_forward_server=webproxy_forward_server,
            isolator_server=isolator_server,
            webproxy_profile=webproxy_profile,
            transparent=transparent,
            webcache=webcache,
            webcache_https=webcache_https,
            disclaimer=disclaimer,
            utm_status=utm_status,
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
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            replacemsg_override_group=replacemsg_override_group,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            comments=comments,
            block_notification=block_notification,
            redirect_url=redirect_url,
            https_sub_category=https_sub_category,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            detect_https_in_http_request=detect_https_in_http_request,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.proxy_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/proxy_policy",
            )
        
        policyid_value = payload_data.get("policyid")
        if not policyid_value:
            raise ValueError("policyid is required for PUT")
        endpoint = "/firewall/proxy-policy/" + str(policyid_value)

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
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = None,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = None,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        poolname: str | list[str] | list[dict[str, Any]] | None = None,
        poolname6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        device_ownership: Literal["enable", "disable"] | None = None,
        url_risk: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        schedule: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        session_ttl: int | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        http_tunnel_auth: Literal["enable", "disable"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: Literal["enable", "disable"] | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
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
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        replacemsg_override_group: str | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        redirect_url: str | None = None,
        https_sub_category: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: Literal["enable", "disable"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new firewall/proxy_policy object.

        Configure proxy policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            policyid: Policy ID.
            name: Policy name.
            proxy: Type of explicit proxy.
            access_proxy: IPv4 access proxy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            access_proxy6: IPv6 access proxy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_proxy: ZTNA proxies.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcintf: Source interface names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstintf: Destination interface names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr: Source address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            poolname: Name of IP pool object.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            poolname6: Name of IPv6 pool object.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: Destination address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_ems_tag: ZTNA EMS Tag names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_tags_match_logic: ZTNA tag matching logic.
            device_ownership: When enabled, the ownership enforcement will be done at policy level.
            url_risk: URL risk level name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.
            internet_service_negate: When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.
            internet_service_name: Internet Service name.
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
            internet_service6: Enable/disable use of Internet Services IPv6 for this policy. If enabled, destination IPv6 address and service are not used.
            internet_service6_negate: When enabled, Internet Services match against any internet service IPv6 EXCEPT the selected Internet Service IPv6.
            internet_service6_name: Internet Service IPv6 name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_group: Internet Service IPv6 group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom: Custom Internet Service IPv6 name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_custom_group: Custom Internet Service IPv6 group name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service6_fortiguard: FortiGuard Internet Service IPv6 name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service: Name of service objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr_negate: When enabled, source addresses match against any address EXCEPT the specified source addresses.
            dstaddr_negate: When enabled, destination addresses match against any address EXCEPT the specified destination addresses.
            ztna_ems_tag_negate: When enabled, ZTNA EMS tags match against any tag EXCEPT the specified ZTNA EMS tags.
            service_negate: When enabled, services match against any service EXCEPT the specified destination services.
            action: Accept or deny traffic matching the policy parameters.
            status: Enable/disable the active status of the policy.
            schedule: Name of schedule object.
            logtraffic: Enable/disable logging traffic through the policy.
            session_ttl: TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).
            srcaddr6: IPv6 source address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: IPv6 destination address objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            groups: Names of group objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            users: Names of user objects.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            http_tunnel_auth: Enable/disable HTTP tunnel authentication.
            ssh_policy_redirect: Redirect SSH traffic to matching transparent proxy policy.
            webproxy_forward_server: Web proxy forward server name.
            isolator_server: Isolator server name.
            webproxy_profile: Name of web proxy profile.
            transparent: Enable to use the IP address of the client to connect to the server.
            webcache: Enable/disable web caching.
            webcache_https: Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).
            disclaimer: Web proxy disclaimer setting: by domain, policy, or user.
            utm_status: Enable the use of UTM profiles/sensors/lists.
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
            ips_voip_filter: Name of an existing VoIP (ips) profile.
            sctp_filter_profile: Name of an existing SCTP filter profile.
            icap_profile: Name of an existing ICAP profile.
            videofilter_profile: Name of an existing VideoFilter profile.
            waf_profile: Name of an existing Web application firewall profile.
            ssh_filter_profile: Name of an existing SSH filter profile.
            casb_profile: Name of an existing CASB profile.
            replacemsg_override_group: Authentication replacement message override group.
            logtraffic_start: Enable/disable policy log traffic start.
            log_http_transaction: Enable/disable HTTP transaction log.
            comments: Optional comments.
            block_notification: Enable/disable block notification.
            redirect_url: Redirect URL for further explicit web proxy processing.
            https_sub_category: Enable/disable HTTPS sub-category policy matching.
            decrypted_traffic_mirror: Decrypted traffic mirror.
            detect_https_in_http_request: Enable/disable detection of HTTPS in HTTP request.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_proxy_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created policyid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = ProxyPolicy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_proxy_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(ProxyPolicy.required_fields()) }}
            
            Use ProxyPolicy.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if access_proxy is not None:
            access_proxy = normalize_table_field(
                access_proxy,
                mkey="name",
                required_fields=['name'],
                field_name="access_proxy",
                example="[{'name': 'value'}]",
            )
        if access_proxy6 is not None:
            access_proxy6 = normalize_table_field(
                access_proxy6,
                mkey="name",
                required_fields=['name'],
                field_name="access_proxy6",
                example="[{'name': 'value'}]",
            )
        if ztna_proxy is not None:
            ztna_proxy = normalize_table_field(
                ztna_proxy,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_proxy",
                example="[{'name': 'value'}]",
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
        if srcaddr is not None:
            srcaddr = normalize_table_field(
                srcaddr,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr",
                example="[{'name': 'value'}]",
            )
        if poolname is not None:
            poolname = normalize_table_field(
                poolname,
                mkey="name",
                required_fields=['name'],
                field_name="poolname",
                example="[{'name': 'value'}]",
            )
        if poolname6 is not None:
            poolname6 = normalize_table_field(
                poolname6,
                mkey="name",
                required_fields=['name'],
                field_name="poolname6",
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
        if ztna_ems_tag is not None:
            ztna_ems_tag = normalize_table_field(
                ztna_ems_tag,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_ems_tag",
                example="[{'name': 'value'}]",
            )
        if url_risk is not None:
            url_risk = normalize_table_field(
                url_risk,
                mkey="name",
                required_fields=['name'],
                field_name="url_risk",
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
        if service is not None:
            service = normalize_table_field(
                service,
                mkey="name",
                required_fields=['name'],
                field_name="service",
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
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            uuid=uuid,
            policyid=policyid,
            name=name,
            proxy=proxy,
            access_proxy=access_proxy,
            access_proxy6=access_proxy6,
            ztna_proxy=ztna_proxy,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            poolname=poolname,
            poolname6=poolname6,
            dstaddr=dstaddr,
            ztna_ems_tag=ztna_ems_tag,
            ztna_tags_match_logic=ztna_tags_match_logic,
            device_ownership=device_ownership,
            url_risk=url_risk,
            internet_service=internet_service,
            internet_service_negate=internet_service_negate,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service6=internet_service6,
            internet_service6_negate=internet_service6_negate,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            service=service,
            srcaddr_negate=srcaddr_negate,
            dstaddr_negate=dstaddr_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            action=action,
            status=status,
            schedule=schedule,
            logtraffic=logtraffic,
            session_ttl=session_ttl,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            groups=groups,
            users=users,
            http_tunnel_auth=http_tunnel_auth,
            ssh_policy_redirect=ssh_policy_redirect,
            webproxy_forward_server=webproxy_forward_server,
            isolator_server=isolator_server,
            webproxy_profile=webproxy_profile,
            transparent=transparent,
            webcache=webcache,
            webcache_https=webcache_https,
            disclaimer=disclaimer,
            utm_status=utm_status,
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
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            replacemsg_override_group=replacemsg_override_group,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            comments=comments,
            block_notification=block_notification,
            redirect_url=redirect_url,
            https_sub_category=https_sub_category,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            detect_https_in_http_request=detect_https_in_http_request,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.proxy_policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/proxy_policy",
            )

        endpoint = "/firewall/proxy-policy"
        
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
        Delete firewall/proxy_policy object.

        Configure proxy policies.

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
            >>> result = fgt.api.cmdb.firewall_proxy_policy.delete(policyid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not policyid:
            raise ValueError("policyid is required for DELETE")
        endpoint = "/firewall/proxy-policy/" + str(policyid)

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
        Check if firewall/proxy_policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_proxy_policy.exists(policyid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_proxy_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_proxy_policy.delete(policyid=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                policyid=policyid,
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
        uuid: str | None = None,
        policyid: int | None = None,
        name: str | None = None,
        proxy: Literal["explicit-web", "transparent-web", "ftp", "ssh", "ssh-tunnel", "access-proxy", "ztna-proxy", "wanopt"] | None = None,
        access_proxy: str | list[str] | list[dict[str, Any]] | None = None,
        access_proxy6: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_proxy: str | list[str] | list[dict[str, Any]] | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        poolname: str | list[str] | list[dict[str, Any]] | None = None,
        poolname6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        device_ownership: Literal["enable", "disable"] | None = None,
        url_risk: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        action: Literal["accept", "deny", "redirect", "isolate"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        schedule: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        session_ttl: int | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        http_tunnel_auth: Literal["enable", "disable"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_forward_server: str | None = None,
        isolator_server: str | None = None,
        webproxy_profile: str | None = None,
        transparent: Literal["enable", "disable"] | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        disclaimer: Literal["disable", "domain", "policy", "user"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
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
        ips_voip_filter: str | None = None,
        sctp_filter_profile: str | None = None,
        icap_profile: str | None = None,
        videofilter_profile: str | None = None,
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        replacemsg_override_group: str | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        redirect_url: str | None = None,
        https_sub_category: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        detect_https_in_http_request: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/proxy_policy object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (policyid) in the payload.

        Args:
            payload_dict: Resource data including policyid (primary key)
            uuid: Field uuid
            policyid: Field policyid
            name: Field name
            proxy: Field proxy
            access_proxy: Field access-proxy
            access_proxy6: Field access-proxy6
            ztna_proxy: Field ztna-proxy
            srcintf: Field srcintf
            dstintf: Field dstintf
            srcaddr: Field srcaddr
            poolname: Field poolname
            poolname6: Field poolname6
            dstaddr: Field dstaddr
            ztna_ems_tag: Field ztna-ems-tag
            ztna_tags_match_logic: Field ztna-tags-match-logic
            device_ownership: Field device-ownership
            url_risk: Field url-risk
            internet_service: Field internet-service
            internet_service_negate: Field internet-service-negate
            internet_service_name: Field internet-service-name
            internet_service_group: Field internet-service-group
            internet_service_custom: Field internet-service-custom
            internet_service_custom_group: Field internet-service-custom-group
            internet_service_fortiguard: Field internet-service-fortiguard
            internet_service6: Field internet-service6
            internet_service6_negate: Field internet-service6-negate
            internet_service6_name: Field internet-service6-name
            internet_service6_group: Field internet-service6-group
            internet_service6_custom: Field internet-service6-custom
            internet_service6_custom_group: Field internet-service6-custom-group
            internet_service6_fortiguard: Field internet-service6-fortiguard
            service: Field service
            srcaddr_negate: Field srcaddr-negate
            dstaddr_negate: Field dstaddr-negate
            ztna_ems_tag_negate: Field ztna-ems-tag-negate
            service_negate: Field service-negate
            action: Field action
            status: Field status
            schedule: Field schedule
            logtraffic: Field logtraffic
            session_ttl: Field session-ttl
            srcaddr6: Field srcaddr6
            dstaddr6: Field dstaddr6
            groups: Field groups
            users: Field users
            http_tunnel_auth: Field http-tunnel-auth
            ssh_policy_redirect: Field ssh-policy-redirect
            webproxy_forward_server: Field webproxy-forward-server
            isolator_server: Field isolator-server
            webproxy_profile: Field webproxy-profile
            transparent: Field transparent
            webcache: Field webcache
            webcache_https: Field webcache-https
            disclaimer: Field disclaimer
            utm_status: Field utm-status
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
            ips_voip_filter: Field ips-voip-filter
            sctp_filter_profile: Field sctp-filter-profile
            icap_profile: Field icap-profile
            videofilter_profile: Field videofilter-profile
            waf_profile: Field waf-profile
            ssh_filter_profile: Field ssh-filter-profile
            casb_profile: Field casb-profile
            replacemsg_override_group: Field replacemsg-override-group
            logtraffic_start: Field logtraffic-start
            log_http_transaction: Field log-http-transaction
            comments: Field comments
            block_notification: Field block-notification
            redirect_url: Field redirect-url
            https_sub_category: Field https-sub-category
            decrypted_traffic_mirror: Field decrypted-traffic-mirror
            detect_https_in_http_request: Field detect-https-in-http-request
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.firewall_proxy_policy.set(
            ...     policyid=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_proxy_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_proxy_policy.set(payload_dict=obj_data)
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
            proxy=proxy,
            access_proxy=access_proxy,
            access_proxy6=access_proxy6,
            ztna_proxy=ztna_proxy,
            srcintf=srcintf,
            dstintf=dstintf,
            srcaddr=srcaddr,
            poolname=poolname,
            poolname6=poolname6,
            dstaddr=dstaddr,
            ztna_ems_tag=ztna_ems_tag,
            ztna_tags_match_logic=ztna_tags_match_logic,
            device_ownership=device_ownership,
            url_risk=url_risk,
            internet_service=internet_service,
            internet_service_negate=internet_service_negate,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service6=internet_service6,
            internet_service6_negate=internet_service6_negate,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_fortiguard=internet_service6_fortiguard,
            service=service,
            srcaddr_negate=srcaddr_negate,
            dstaddr_negate=dstaddr_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            action=action,
            status=status,
            schedule=schedule,
            logtraffic=logtraffic,
            session_ttl=session_ttl,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            groups=groups,
            users=users,
            http_tunnel_auth=http_tunnel_auth,
            ssh_policy_redirect=ssh_policy_redirect,
            webproxy_forward_server=webproxy_forward_server,
            isolator_server=isolator_server,
            webproxy_profile=webproxy_profile,
            transparent=transparent,
            webcache=webcache,
            webcache_https=webcache_https,
            disclaimer=disclaimer,
            utm_status=utm_status,
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
            ips_voip_filter=ips_voip_filter,
            sctp_filter_profile=sctp_filter_profile,
            icap_profile=icap_profile,
            videofilter_profile=videofilter_profile,
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            replacemsg_override_group=replacemsg_override_group,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            comments=comments,
            block_notification=block_notification,
            redirect_url=redirect_url,
            https_sub_category=https_sub_category,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            detect_https_in_http_request=detect_https_in_http_request,
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
        Move firewall/proxy_policy object to a new position.
        
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
            >>> fgt.api.cmdb.firewall_proxy_policy.move(
            ...     policyid=100,
            ...     action="before",
            ...     reference_policyid=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/proxy-policy",
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
        Clone firewall/proxy_policy object.
        
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
            >>> fgt.api.cmdb.firewall_proxy_policy.clone(
            ...     policyid=1,
            ...     new_policyid=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/proxy-policy",
            params={
                "policyid": policyid,
                "new_policyid": new_policyid,
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
        policyid: int,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if firewall/proxy_policy object exists.
        
        Args:
            policyid: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_proxy_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_proxy_policy.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                policyid=policyid,
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


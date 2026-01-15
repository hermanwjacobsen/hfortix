"""
FortiOS CMDB - Firewall policy

Configuration endpoint for managing cmdb firewall/policy objects.

API Endpoints:
    GET    /cmdb/firewall/policy
    POST   /cmdb/firewall/policy
    PUT    /cmdb/firewall/policy/{identifier}
    DELETE /cmdb/firewall/policy/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_policy.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.firewall_policy.post(
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

class Policy(CRUDEndpoint, MetadataMixin):
    """Policy Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "policy"
    
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
        "ztna_ems_tag": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "ztna_ems_tag_secondary": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "ztna_geo_tag": {
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
        "network_service_dynamic": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_custom_group": {
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
        "network_service_src_dynamic": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_src_custom_group": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "src_vendor_mac": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
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
        "rtp_addr": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "service": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "pcp_poolname": {
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
        "ntlm_enabled_browsers": {
            "mkey": "user-agent-string",
            "required_fields": ['user-agent-string'],
            "example": "[{'user-agent-string': 'value'}]",
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
        "custom_log_fields": {
            "mkey": "field-id",
            "required_fields": ['field-id'],
            "example": "[{'field-id': 'value'}]",
        },
        "sgt": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "internet_service_fortiguard": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service_src_fortiguard": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_fortiguard": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internet_service6_src_fortiguard": {
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
        """Initialize Policy endpoint."""
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
        Retrieve firewall/policy configuration.

        Configure IPv4/IPv6 policies.

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
            >>> # Get all firewall/policy objects
            >>> result = fgt.api.cmdb.firewall_policy.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/policy by policyid
            >>> result = fgt.api.cmdb.firewall_policy.get(policyid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_policy.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_policy.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_policy.get_schema()

        See Also:
            - post(): Create new firewall/policy object
            - put(): Update existing firewall/policy object
            - delete(): Remove firewall/policy object
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
            endpoint = "/firewall/policy/" + str(policyid)
            unwrap_single = True
        else:
            endpoint = "/firewall/policy"
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
            >>> schema = fgt.api.cmdb.firewall_policy.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_policy.get_schema(format="json-schema")
        
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
        policyid: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        action: Literal["accept", "deny", "ipsec"] | None = None,
        nat64: Literal["enable", "disable"] | None = None,
        nat46: Literal["enable", "disable"] | None = None,
        ztna_status: Literal["enable", "disable"] | None = None,
        ztna_device_ownership: Literal["enable", "disable"] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        reputation_minimum: int | None = None,
        reputation_direction: Literal["source", "destination"] | None = None,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src: Literal["enable", "disable"] | None = None,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        reputation_minimum6: int | None = None,
        reputation_direction6: Literal["source", "destination"] | None = None,
        rtp_nat: Literal["disable", "enable"] | None = None,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = None,
        send_deny_packet: Literal["disable", "enable"] | None = None,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = None,
        schedule: str | None = None,
        schedule_timeout: Literal["enable", "disable"] | None = None,
        policy_expiry: Literal["enable", "disable"] | None = None,
        policy_expiry_date: Any | None = None,
        policy_expiry_date_utc: str | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: Literal["enable", "disable"] | None = None,
        anti_replay: Literal["enable", "disable"] | None = None,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = None,
        geoip_anycast: Literal["enable", "disable"] | None = None,
        geoip_match: Literal["physical-location", "registered-location"] | None = None,
        dynamic_shaping: Literal["enable", "disable"] | None = None,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = None,
        app_monitor: Literal["enable", "disable"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        inspection_mode: Literal["proxy", "flow"] | None = None,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        ztna_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_profile: str | None = None,
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
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        capture_packet: Literal["enable", "disable"] | None = None,
        auto_asic_offload: Literal["enable", "disable"] | None = None,
        wanopt: Literal["enable", "disable"] | None = None,
        wanopt_detection: Literal["active", "passive", "off"] | None = None,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = None,
        wanopt_profile: str | None = None,
        wanopt_peer: str | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        webproxy_forward_server: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        nat: Literal["enable", "disable"] | None = None,
        pcp_outbound: Literal["enable", "disable"] | None = None,
        pcp_inbound: Literal["enable", "disable"] | None = None,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = None,
        permit_any_host: Literal["enable", "disable"] | None = None,
        permit_stun_host: Literal["enable", "disable"] | None = None,
        fixedport: Literal["enable", "disable"] | None = None,
        port_preserve: Literal["enable", "disable"] | None = None,
        port_random: Literal["enable", "disable"] | None = None,
        ippool: Literal["enable", "disable"] | None = None,
        poolname: str | list[str] | list[dict[str, Any]] | None = None,
        poolname6: str | list[str] | list[dict[str, Any]] | None = None,
        session_ttl: str | None = None,
        vlan_cos_fwd: int | None = None,
        vlan_cos_rev: int | None = None,
        inbound: Literal["enable", "disable"] | None = None,
        outbound: Literal["enable", "disable"] | None = None,
        natinbound: Literal["enable", "disable"] | None = None,
        natoutbound: Literal["enable", "disable"] | None = None,
        fec: Literal["enable", "disable"] | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        ntlm: Literal["enable", "disable"] | None = None,
        ntlm_guest: Literal["enable", "disable"] | None = None,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_agent_for_ntlm: str | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = None,
        auth_path: Literal["enable", "disable"] | None = None,
        disclaimer: Literal["enable", "disable"] | None = None,
        email_collect: Literal["enable", "disable"] | None = None,
        vpntunnel: str | None = None,
        natip: str | None = None,
        match_vip: Literal["enable", "disable"] | None = None,
        match_vip_only: Literal["enable", "disable"] | None = None,
        diffserv_copy: Literal["enable", "disable"] | None = None,
        diffserv_forward: Literal["enable", "disable"] | None = None,
        diffserv_reverse: Literal["enable", "disable"] | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        tcp_mss_sender: int | None = None,
        tcp_mss_receiver: int | None = None,
        comments: str | None = None,
        auth_cert: str | None = None,
        auth_redirect_addr: str | None = None,
        redirect_url: str | None = None,
        identity_based_route: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = None,
        replacemsg_override_group: str | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        srcaddr6_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr6_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_src_negate: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_src_negate: Literal["enable", "disable"] | None = None,
        timeout_send_rst: Literal["enable", "disable"] | None = None,
        captive_portal_exempt: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        dsri: Literal["enable", "disable"] | None = None,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = None,
        vlan_filter: str | None = None,
        sgt_check: Literal["enable", "disable"] | None = None,
        sgt: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing firewall/policy object.

        Configure IPv4/IPv6 policies.

        Args:
            payload_dict: Object data as dict. Must include policyid (primary key).
            policyid: Policy ID (0 - 4294967294).
            status: Enable or disable this policy.
            name: Policy name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
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
            action: Policy action (accept/deny/ipsec).
            nat64: Enable/disable NAT64.
            nat46: Enable/disable NAT46.
            ztna_status: Enable/disable zero trust access.
            ztna_device_ownership: Enable/disable zero trust device ownership.
            srcaddr: Source IPv4 address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: Destination IPv4 address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr6: Source IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: Destination IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_ems_tag: Source ztna-ems-tag names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_ems_tag_secondary: Source ztna-ems-tag-secondary names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_tags_match_logic: ZTNA tag matching logic.
            ztna_geo_tag: Source ztna-geo-tag names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.
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
            network_service_dynamic: Dynamic Network Service name.
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
            network_service_src_dynamic: Dynamic Network Service source name.
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
            reputation_minimum: Minimum Reputation to take action.
            reputation_direction: Direction of the initial traffic for reputation to take effect.
            src_vendor_mac: Vendor MAC source ID.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            internet_service6: Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used.
            internet_service6_name: IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
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
            internet_service6_custom_group: Custom Internet Service6 group name.
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
            reputation_minimum6: IPv6 Minimum Reputation to take action.
            reputation_direction6: Direction of the initial traffic for IPv6 reputation to take effect.
            rtp_nat: Enable Real Time Protocol (RTP) NAT.
            rtp_addr: Address names if this is an RTP NAT policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            send_deny_packet: Enable to send a reply when a session is denied or blocked by a firewall policy.
            firewall_session_dirty: How to handle sessions if the configuration of this firewall policy changes.
            schedule: Schedule name.
            schedule_timeout: Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity.
            policy_expiry: Enable/disable policy expiry.
            policy_expiry_date: Policy expiry date (YYYY-MM-DD HH:MM:SS).
            policy_expiry_date_utc: Policy expiry date and time, in epoch format.
            service: Service and service group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            tos_mask: Non-zero bit positions are used for comparison while zero bit positions are ignored.
            tos: ToS (Type of Service) value used for comparison.
            tos_negate: Enable negated TOS match.
            anti_replay: Enable/disable anti-replay check.
            tcp_session_without_syn: Enable/disable creation of TCP session without SYN flag.
            geoip_anycast: Enable/disable recognition of anycast IP addresses using the geography IP database.
            geoip_match: Match geography address based either on its physical location or registered location.
            dynamic_shaping: Enable/disable dynamic RADIUS defined traffic shaping.
            passive_wan_health_measurement: Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled.
            app_monitor: Enable/disable application TCP metrics in session logs.When enabled, auto-asic-offload is disabled.
            utm_status: Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.
            inspection_mode: Policy inspection mode (Flow/proxy). Default is Flow mode.
            http_policy_redirect: Redirect HTTP(S) traffic to matching transparent web proxy policy.
            ssh_policy_redirect: Redirect SSH traffic to matching transparent proxy policy.
            ztna_policy_redirect: Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
            webproxy_profile: Webproxy profile name.
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
            waf_profile: Name of an existing Web application firewall profile.
            ssh_filter_profile: Name of an existing SSH filter profile.
            casb_profile: Name of an existing CASB profile.
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions.
            logtraffic_start: Record logs when a session starts.
            log_http_transaction: Enable/disable HTTP transaction log.
            capture_packet: Enable/disable capture packets.
            auto_asic_offload: Enable/disable policy traffic ASIC offloading.
            wanopt: Enable/disable WAN optimization.
            wanopt_detection: WAN optimization auto-detection mode.
            wanopt_passive_opt: WAN optimization passive mode options. This option decides what IP address will be used to connect server.
            wanopt_profile: WAN optimization profile.
            wanopt_peer: WAN optimization peer.
            webcache: Enable/disable web cache.
            webcache_https: Enable/disable web cache for HTTPS.
            webproxy_forward_server: Webproxy forward server name.
            traffic_shaper: Traffic shaper.
            traffic_shaper_reverse: Reverse traffic shaper.
            per_ip_shaper: Per-IP traffic shaper.
            nat: Enable/disable source NAT.
            pcp_outbound: Enable/disable PCP outbound SNAT.
            pcp_inbound: Enable/disable PCP inbound DNAT.
            pcp_poolname: PCP pool names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets from any host.
            permit_stun_host: Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.
            fixedport: Enable to prevent source NAT from changing a session's source port.
            port_preserve: Enable/disable preservation of the original source port from source NAT if it has not been used.
            port_random: Enable/disable random source port selection for source NAT.
            ippool: Enable to use IP Pools for source NAT.
            poolname: IP Pool names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            poolname6: IPv6 pool names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            session_ttl: TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).
            vlan_cos_fwd: VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.
            vlan_cos_rev: VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.
            inbound: Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.
            outbound: Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.
            natinbound: Policy-based IPsec VPN: apply destination NAT to inbound traffic.
            natoutbound: Policy-based IPsec VPN: apply source NAT to outbound traffic.
            fec: Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.
            wccp: Enable/disable forwarding traffic matching this policy to a configured WCCP server.
            ntlm: Enable/disable NTLM authentication.
            ntlm_guest: Enable/disable NTLM guest user access.
            ntlm_enabled_browsers: HTTP-User-Agent value of supported browsers.
                Default format: [{'user-agent-string': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'user-agent-string': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'user-agent-string': 'val1'}, ...]
                  - List of dicts: [{'user-agent-string': 'value'}] (recommended)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication.
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
            auth_path: Enable/disable authentication-based routing.
            disclaimer: Enable/disable user authentication disclaimer.
            email_collect: Enable/disable email collection.
            vpntunnel: Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
            natip: Policy-based IPsec VPN: source NAT IP address for outgoing traffic.
            match_vip: Enable to match packets that have had their destination addresses changed by a VIP.
            match_vip_only: Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.
            diffserv_copy: Enable to copy packet's DiffServ values from session's original direction to its reply direction.
            diffserv_forward: Enable to change packet's DiffServ values to the specified diffservcode-forward value.
            diffserv_reverse: Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.
            diffservcode_forward: Change packet's DiffServ to this value.
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this value.
            tcp_mss_sender: Sender TCP maximum segment size (MSS).
            tcp_mss_receiver: Receiver TCP maximum segment size (MSS).
            comments: Comment.
            auth_cert: HTTPS server certificate for policy authentication.
            auth_redirect_addr: HTTP-to-HTTPS redirect address for firewall authentication.
            redirect_url: URL users are directed to after seeing and accepting the disclaimer or authenticating.
            identity_based_route: Name of identity-based routing rule.
            block_notification: Enable/disable block notification.
            custom_log_fields: Custom fields to append to log messages for this policy.
                Default format: [{'field-id': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'field-id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'field-id': 'val1'}, ...]
                  - List of dicts: [{'field-id': 'value'}] (recommended)
            replacemsg_override_group: Override the default replacement message group for this policy.
            srcaddr_negate: When enabled srcaddr specifies what the source address must NOT be.
            srcaddr6_negate: When enabled srcaddr6 specifies what the source address must NOT be.
            dstaddr_negate: When enabled dstaddr specifies what the destination address must NOT be.
            dstaddr6_negate: When enabled dstaddr6 specifies what the destination address must NOT be.
            ztna_ems_tag_negate: When enabled ztna-ems-tag specifies what the tags must NOT be.
            service_negate: When enabled service specifies what the service must NOT be.
            internet_service_negate: When enabled internet-service specifies what the service must NOT be.
            internet_service_src_negate: When enabled internet-service-src specifies what the service must NOT be.
            internet_service6_negate: When enabled internet-service6 specifies what the service must NOT be.
            internet_service6_src_negate: When enabled internet-service6-src specifies what the service must NOT be.
            timeout_send_rst: Enable/disable sending RST packets when TCP sessions expire.
            captive_portal_exempt: Enable to exempt some users from the captive portal.
            decrypted_traffic_mirror: Decrypted traffic mirror.
            dsri: Enable DSRI to ignore HTTP server responses.
            radius_mac_auth_bypass: Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.
            radius_ip_auth_bypass: Enable IP authentication bypass. The bypassed IP address must be received from RADIUS server.
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee packet order of 3-way handshake.
            vlan_filter: VLAN ranges to allow
            sgt_check: Enable/disable security group tags (SGT) check.
            sgt: Security group tags.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            internet_service_fortiguard: FortiGuard Internet Service name.
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
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service name.
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
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_policy.put(
            ...     policyid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_policy.put(payload_dict=payload)

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
        if ztna_ems_tag is not None:
            ztna_ems_tag = normalize_table_field(
                ztna_ems_tag,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_ems_tag",
                example="[{'name': 'value'}]",
            )
        if ztna_ems_tag_secondary is not None:
            ztna_ems_tag_secondary = normalize_table_field(
                ztna_ems_tag_secondary,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_ems_tag_secondary",
                example="[{'name': 'value'}]",
            )
        if ztna_geo_tag is not None:
            ztna_geo_tag = normalize_table_field(
                ztna_geo_tag,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_geo_tag",
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
        if network_service_dynamic is not None:
            network_service_dynamic = normalize_table_field(
                network_service_dynamic,
                mkey="name",
                required_fields=['name'],
                field_name="network_service_dynamic",
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
        if network_service_src_dynamic is not None:
            network_service_src_dynamic = normalize_table_field(
                network_service_src_dynamic,
                mkey="name",
                required_fields=['name'],
                field_name="network_service_src_dynamic",
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
        if src_vendor_mac is not None:
            src_vendor_mac = normalize_table_field(
                src_vendor_mac,
                mkey="id",
                required_fields=['id'],
                field_name="src_vendor_mac",
                example="[{'id': 1}]",
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
        if rtp_addr is not None:
            rtp_addr = normalize_table_field(
                rtp_addr,
                mkey="name",
                required_fields=['name'],
                field_name="rtp_addr",
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
        if pcp_poolname is not None:
            pcp_poolname = normalize_table_field(
                pcp_poolname,
                mkey="name",
                required_fields=['name'],
                field_name="pcp_poolname",
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
        if ntlm_enabled_browsers is not None:
            ntlm_enabled_browsers = normalize_table_field(
                ntlm_enabled_browsers,
                mkey="user-agent-string",
                required_fields=['user-agent-string'],
                field_name="ntlm_enabled_browsers",
                example="[{'user-agent-string': 'value'}]",
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
        if custom_log_fields is not None:
            custom_log_fields = normalize_table_field(
                custom_log_fields,
                mkey="field-id",
                required_fields=['field-id'],
                field_name="custom_log_fields",
                example="[{'field-id': 'value'}]",
            )
        if sgt is not None:
            sgt = normalize_table_field(
                sgt,
                mkey="id",
                required_fields=['id'],
                field_name="sgt",
                example="[{'id': 1}]",
            )
        if internet_service_fortiguard is not None:
            internet_service_fortiguard = normalize_table_field(
                internet_service_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_fortiguard",
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
        if internet_service6_fortiguard is not None:
            internet_service6_fortiguard = normalize_table_field(
                internet_service6_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_fortiguard",
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
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            policyid=policyid,
            status=status,
            name=name,
            uuid=uuid,
            srcintf=srcintf,
            dstintf=dstintf,
            action=action,
            nat64=nat64,
            nat46=nat46,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            network_service_dynamic=network_service_dynamic,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_custom_group=internet_service_src_custom_group,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            src_vendor_mac=src_vendor_mac,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule=schedule,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            service=service,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            anti_replay=anti_replay,
            tcp_session_without_syn=tcp_session_without_syn,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            dynamic_shaping=dynamic_shaping,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            utm_status=utm_status,
            inspection_mode=inspection_mode,
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            ztna_policy_redirect=ztna_policy_redirect,
            webproxy_profile=webproxy_profile,
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
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            auto_asic_offload=auto_asic_offload,
            wanopt=wanopt,
            wanopt_detection=wanopt_detection,
            wanopt_passive_opt=wanopt_passive_opt,
            wanopt_profile=wanopt_profile,
            wanopt_peer=wanopt_peer,
            webcache=webcache,
            webcache_https=webcache_https,
            webproxy_forward_server=webproxy_forward_server,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            nat=nat,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            fixedport=fixedport,
            port_preserve=port_preserve,
            port_random=port_random,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            session_ttl=session_ttl,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            fec=fec,
            wccp=wccp,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            auth_path=auth_path,
            disclaimer=disclaimer,
            email_collect=email_collect,
            vpntunnel=vpntunnel,
            natip=natip,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            comments=comments,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            redirect_url=redirect_url,
            identity_based_route=identity_based_route,
            block_notification=block_notification,
            custom_log_fields=custom_log_fields,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr_negate=dstaddr_negate,
            dstaddr6_negate=dstaddr6_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            internet_service_negate=internet_service_negate,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src_negate=internet_service6_src_negate,
            timeout_send_rst=timeout_send_rst,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dsri=dsri,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            delay_tcp_npu_session=delay_tcp_npu_session,
            vlan_filter=vlan_filter,
            sgt_check=sgt_check,
            sgt=sgt,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/policy",
            )
        
        policyid_value = payload_data.get("policyid")
        if not policyid_value:
            raise ValueError("policyid is required for PUT")
        endpoint = "/firewall/policy/" + str(policyid_value)

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
        policyid: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        action: Literal["accept", "deny", "ipsec"] | None = None,
        nat64: Literal["enable", "disable"] | None = None,
        nat46: Literal["enable", "disable"] | None = None,
        ztna_status: Literal["enable", "disable"] | None = None,
        ztna_device_ownership: Literal["enable", "disable"] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        reputation_minimum: int | None = None,
        reputation_direction: Literal["source", "destination"] | None = None,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src: Literal["enable", "disable"] | None = None,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        reputation_minimum6: int | None = None,
        reputation_direction6: Literal["source", "destination"] | None = None,
        rtp_nat: Literal["disable", "enable"] | None = None,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = None,
        send_deny_packet: Literal["disable", "enable"] | None = None,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = None,
        schedule: str | None = None,
        schedule_timeout: Literal["enable", "disable"] | None = None,
        policy_expiry: Literal["enable", "disable"] | None = None,
        policy_expiry_date: Any | None = None,
        policy_expiry_date_utc: str | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: Literal["enable", "disable"] | None = None,
        anti_replay: Literal["enable", "disable"] | None = None,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = None,
        geoip_anycast: Literal["enable", "disable"] | None = None,
        geoip_match: Literal["physical-location", "registered-location"] | None = None,
        dynamic_shaping: Literal["enable", "disable"] | None = None,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = None,
        app_monitor: Literal["enable", "disable"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        inspection_mode: Literal["proxy", "flow"] | None = None,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        ztna_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_profile: str | None = None,
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
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        capture_packet: Literal["enable", "disable"] | None = None,
        auto_asic_offload: Literal["enable", "disable"] | None = None,
        wanopt: Literal["enable", "disable"] | None = None,
        wanopt_detection: Literal["active", "passive", "off"] | None = None,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = None,
        wanopt_profile: str | None = None,
        wanopt_peer: str | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        webproxy_forward_server: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        nat: Literal["enable", "disable"] | None = None,
        pcp_outbound: Literal["enable", "disable"] | None = None,
        pcp_inbound: Literal["enable", "disable"] | None = None,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = None,
        permit_any_host: Literal["enable", "disable"] | None = None,
        permit_stun_host: Literal["enable", "disable"] | None = None,
        fixedport: Literal["enable", "disable"] | None = None,
        port_preserve: Literal["enable", "disable"] | None = None,
        port_random: Literal["enable", "disable"] | None = None,
        ippool: Literal["enable", "disable"] | None = None,
        poolname: str | list[str] | list[dict[str, Any]] | None = None,
        poolname6: str | list[str] | list[dict[str, Any]] | None = None,
        session_ttl: str | None = None,
        vlan_cos_fwd: int | None = None,
        vlan_cos_rev: int | None = None,
        inbound: Literal["enable", "disable"] | None = None,
        outbound: Literal["enable", "disable"] | None = None,
        natinbound: Literal["enable", "disable"] | None = None,
        natoutbound: Literal["enable", "disable"] | None = None,
        fec: Literal["enable", "disable"] | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        ntlm: Literal["enable", "disable"] | None = None,
        ntlm_guest: Literal["enable", "disable"] | None = None,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_agent_for_ntlm: str | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = None,
        auth_path: Literal["enable", "disable"] | None = None,
        disclaimer: Literal["enable", "disable"] | None = None,
        email_collect: Literal["enable", "disable"] | None = None,
        vpntunnel: str | None = None,
        natip: str | None = None,
        match_vip: Literal["enable", "disable"] | None = None,
        match_vip_only: Literal["enable", "disable"] | None = None,
        diffserv_copy: Literal["enable", "disable"] | None = None,
        diffserv_forward: Literal["enable", "disable"] | None = None,
        diffserv_reverse: Literal["enable", "disable"] | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        tcp_mss_sender: int | None = None,
        tcp_mss_receiver: int | None = None,
        comments: str | None = None,
        auth_cert: str | None = None,
        auth_redirect_addr: str | None = None,
        redirect_url: str | None = None,
        identity_based_route: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = None,
        replacemsg_override_group: str | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        srcaddr6_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr6_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_src_negate: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_src_negate: Literal["enable", "disable"] | None = None,
        timeout_send_rst: Literal["enable", "disable"] | None = None,
        captive_portal_exempt: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        dsri: Literal["enable", "disable"] | None = None,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = None,
        vlan_filter: str | None = None,
        sgt_check: Literal["enable", "disable"] | None = None,
        sgt: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new firewall/policy object.

        Configure IPv4/IPv6 policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            policyid: Policy ID (0 - 4294967294).
            status: Enable or disable this policy.
            name: Policy name.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
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
            action: Policy action (accept/deny/ipsec).
            nat64: Enable/disable NAT64.
            nat46: Enable/disable NAT46.
            ztna_status: Enable/disable zero trust access.
            ztna_device_ownership: Enable/disable zero trust device ownership.
            srcaddr: Source IPv4 address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: Destination IPv4 address and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            srcaddr6: Source IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: Destination IPv6 address name and address group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_ems_tag: Source ztna-ems-tag names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_ems_tag_secondary: Source ztna-ems-tag-secondary names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ztna_tags_match_logic: ZTNA tag matching logic.
            ztna_geo_tag: Source ztna-geo-tag names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            internet_service: Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.
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
            network_service_dynamic: Dynamic Network Service name.
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
            network_service_src_dynamic: Dynamic Network Service source name.
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
            reputation_minimum: Minimum Reputation to take action.
            reputation_direction: Direction of the initial traffic for reputation to take effect.
            src_vendor_mac: Vendor MAC source ID.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            internet_service6: Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used.
            internet_service6_name: IPv6 Internet Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
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
            internet_service6_custom_group: Custom Internet Service6 group name.
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
            reputation_minimum6: IPv6 Minimum Reputation to take action.
            reputation_direction6: Direction of the initial traffic for IPv6 reputation to take effect.
            rtp_nat: Enable Real Time Protocol (RTP) NAT.
            rtp_addr: Address names if this is an RTP NAT policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            send_deny_packet: Enable to send a reply when a session is denied or blocked by a firewall policy.
            firewall_session_dirty: How to handle sessions if the configuration of this firewall policy changes.
            schedule: Schedule name.
            schedule_timeout: Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity.
            policy_expiry: Enable/disable policy expiry.
            policy_expiry_date: Policy expiry date (YYYY-MM-DD HH:MM:SS).
            policy_expiry_date_utc: Policy expiry date and time, in epoch format.
            service: Service and service group names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            tos_mask: Non-zero bit positions are used for comparison while zero bit positions are ignored.
            tos: ToS (Type of Service) value used for comparison.
            tos_negate: Enable negated TOS match.
            anti_replay: Enable/disable anti-replay check.
            tcp_session_without_syn: Enable/disable creation of TCP session without SYN flag.
            geoip_anycast: Enable/disable recognition of anycast IP addresses using the geography IP database.
            geoip_match: Match geography address based either on its physical location or registered location.
            dynamic_shaping: Enable/disable dynamic RADIUS defined traffic shaping.
            passive_wan_health_measurement: Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled.
            app_monitor: Enable/disable application TCP metrics in session logs.When enabled, auto-asic-offload is disabled.
            utm_status: Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.
            inspection_mode: Policy inspection mode (Flow/proxy). Default is Flow mode.
            http_policy_redirect: Redirect HTTP(S) traffic to matching transparent web proxy policy.
            ssh_policy_redirect: Redirect SSH traffic to matching transparent proxy policy.
            ztna_policy_redirect: Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
            webproxy_profile: Webproxy profile name.
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
            waf_profile: Name of an existing Web application firewall profile.
            ssh_filter_profile: Name of an existing SSH filter profile.
            casb_profile: Name of an existing CASB profile.
            logtraffic: Enable or disable logging. Log all sessions or security profile sessions.
            logtraffic_start: Record logs when a session starts.
            log_http_transaction: Enable/disable HTTP transaction log.
            capture_packet: Enable/disable capture packets.
            auto_asic_offload: Enable/disable policy traffic ASIC offloading.
            wanopt: Enable/disable WAN optimization.
            wanopt_detection: WAN optimization auto-detection mode.
            wanopt_passive_opt: WAN optimization passive mode options. This option decides what IP address will be used to connect server.
            wanopt_profile: WAN optimization profile.
            wanopt_peer: WAN optimization peer.
            webcache: Enable/disable web cache.
            webcache_https: Enable/disable web cache for HTTPS.
            webproxy_forward_server: Webproxy forward server name.
            traffic_shaper: Traffic shaper.
            traffic_shaper_reverse: Reverse traffic shaper.
            per_ip_shaper: Per-IP traffic shaper.
            nat: Enable/disable source NAT.
            pcp_outbound: Enable/disable PCP outbound SNAT.
            pcp_inbound: Enable/disable PCP inbound DNAT.
            pcp_poolname: PCP pool names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            permit_any_host: Enable/disable fullcone NAT. Accept UDP packets from any host.
            permit_stun_host: Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.
            fixedport: Enable to prevent source NAT from changing a session's source port.
            port_preserve: Enable/disable preservation of the original source port from source NAT if it has not been used.
            port_random: Enable/disable random source port selection for source NAT.
            ippool: Enable to use IP Pools for source NAT.
            poolname: IP Pool names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            poolname6: IPv6 pool names.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            session_ttl: TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).
            vlan_cos_fwd: VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.
            vlan_cos_rev: VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.
            inbound: Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.
            outbound: Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.
            natinbound: Policy-based IPsec VPN: apply destination NAT to inbound traffic.
            natoutbound: Policy-based IPsec VPN: apply source NAT to outbound traffic.
            fec: Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.
            wccp: Enable/disable forwarding traffic matching this policy to a configured WCCP server.
            ntlm: Enable/disable NTLM authentication.
            ntlm_guest: Enable/disable NTLM guest user access.
            ntlm_enabled_browsers: HTTP-User-Agent value of supported browsers.
                Default format: [{'user-agent-string': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'user-agent-string': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'user-agent-string': 'val1'}, ...]
                  - List of dicts: [{'user-agent-string': 'value'}] (recommended)
            fsso_agent_for_ntlm: FSSO agent to use for NTLM authentication.
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
            auth_path: Enable/disable authentication-based routing.
            disclaimer: Enable/disable user authentication disclaimer.
            email_collect: Enable/disable email collection.
            vpntunnel: Policy-based IPsec VPN: name of the IPsec VPN Phase 1.
            natip: Policy-based IPsec VPN: source NAT IP address for outgoing traffic.
            match_vip: Enable to match packets that have had their destination addresses changed by a VIP.
            match_vip_only: Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.
            diffserv_copy: Enable to copy packet's DiffServ values from session's original direction to its reply direction.
            diffserv_forward: Enable to change packet's DiffServ values to the specified diffservcode-forward value.
            diffserv_reverse: Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.
            diffservcode_forward: Change packet's DiffServ to this value.
            diffservcode_rev: Change packet's reverse (reply) DiffServ to this value.
            tcp_mss_sender: Sender TCP maximum segment size (MSS).
            tcp_mss_receiver: Receiver TCP maximum segment size (MSS).
            comments: Comment.
            auth_cert: HTTPS server certificate for policy authentication.
            auth_redirect_addr: HTTP-to-HTTPS redirect address for firewall authentication.
            redirect_url: URL users are directed to after seeing and accepting the disclaimer or authenticating.
            identity_based_route: Name of identity-based routing rule.
            block_notification: Enable/disable block notification.
            custom_log_fields: Custom fields to append to log messages for this policy.
                Default format: [{'field-id': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'field-id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'field-id': 'val1'}, ...]
                  - List of dicts: [{'field-id': 'value'}] (recommended)
            replacemsg_override_group: Override the default replacement message group for this policy.
            srcaddr_negate: When enabled srcaddr specifies what the source address must NOT be.
            srcaddr6_negate: When enabled srcaddr6 specifies what the source address must NOT be.
            dstaddr_negate: When enabled dstaddr specifies what the destination address must NOT be.
            dstaddr6_negate: When enabled dstaddr6 specifies what the destination address must NOT be.
            ztna_ems_tag_negate: When enabled ztna-ems-tag specifies what the tags must NOT be.
            service_negate: When enabled service specifies what the service must NOT be.
            internet_service_negate: When enabled internet-service specifies what the service must NOT be.
            internet_service_src_negate: When enabled internet-service-src specifies what the service must NOT be.
            internet_service6_negate: When enabled internet-service6 specifies what the service must NOT be.
            internet_service6_src_negate: When enabled internet-service6-src specifies what the service must NOT be.
            timeout_send_rst: Enable/disable sending RST packets when TCP sessions expire.
            captive_portal_exempt: Enable to exempt some users from the captive portal.
            decrypted_traffic_mirror: Decrypted traffic mirror.
            dsri: Enable DSRI to ignore HTTP server responses.
            radius_mac_auth_bypass: Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.
            radius_ip_auth_bypass: Enable IP authentication bypass. The bypassed IP address must be received from RADIUS server.
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee packet order of 3-way handshake.
            vlan_filter: VLAN ranges to allow
            sgt_check: Enable/disable security group tags (SGT) check.
            sgt: Security group tags.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            internet_service_fortiguard: FortiGuard Internet Service name.
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
            internet_service6_fortiguard: FortiGuard IPv6 Internet Service name.
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
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_policy.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created policyid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Policy.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_policy.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Policy.required_fields()) }}
            
            Use Policy.help('field_name') to get field details.

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
        if ztna_ems_tag is not None:
            ztna_ems_tag = normalize_table_field(
                ztna_ems_tag,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_ems_tag",
                example="[{'name': 'value'}]",
            )
        if ztna_ems_tag_secondary is not None:
            ztna_ems_tag_secondary = normalize_table_field(
                ztna_ems_tag_secondary,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_ems_tag_secondary",
                example="[{'name': 'value'}]",
            )
        if ztna_geo_tag is not None:
            ztna_geo_tag = normalize_table_field(
                ztna_geo_tag,
                mkey="name",
                required_fields=['name'],
                field_name="ztna_geo_tag",
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
        if network_service_dynamic is not None:
            network_service_dynamic = normalize_table_field(
                network_service_dynamic,
                mkey="name",
                required_fields=['name'],
                field_name="network_service_dynamic",
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
        if network_service_src_dynamic is not None:
            network_service_src_dynamic = normalize_table_field(
                network_service_src_dynamic,
                mkey="name",
                required_fields=['name'],
                field_name="network_service_src_dynamic",
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
        if src_vendor_mac is not None:
            src_vendor_mac = normalize_table_field(
                src_vendor_mac,
                mkey="id",
                required_fields=['id'],
                field_name="src_vendor_mac",
                example="[{'id': 1}]",
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
        if rtp_addr is not None:
            rtp_addr = normalize_table_field(
                rtp_addr,
                mkey="name",
                required_fields=['name'],
                field_name="rtp_addr",
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
        if pcp_poolname is not None:
            pcp_poolname = normalize_table_field(
                pcp_poolname,
                mkey="name",
                required_fields=['name'],
                field_name="pcp_poolname",
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
        if ntlm_enabled_browsers is not None:
            ntlm_enabled_browsers = normalize_table_field(
                ntlm_enabled_browsers,
                mkey="user-agent-string",
                required_fields=['user-agent-string'],
                field_name="ntlm_enabled_browsers",
                example="[{'user-agent-string': 'value'}]",
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
        if custom_log_fields is not None:
            custom_log_fields = normalize_table_field(
                custom_log_fields,
                mkey="field-id",
                required_fields=['field-id'],
                field_name="custom_log_fields",
                example="[{'field-id': 'value'}]",
            )
        if sgt is not None:
            sgt = normalize_table_field(
                sgt,
                mkey="id",
                required_fields=['id'],
                field_name="sgt",
                example="[{'id': 1}]",
            )
        if internet_service_fortiguard is not None:
            internet_service_fortiguard = normalize_table_field(
                internet_service_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service_fortiguard",
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
        if internet_service6_fortiguard is not None:
            internet_service6_fortiguard = normalize_table_field(
                internet_service6_fortiguard,
                mkey="name",
                required_fields=['name'],
                field_name="internet_service6_fortiguard",
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
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            policyid=policyid,
            status=status,
            name=name,
            uuid=uuid,
            srcintf=srcintf,
            dstintf=dstintf,
            action=action,
            nat64=nat64,
            nat46=nat46,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            network_service_dynamic=network_service_dynamic,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_custom_group=internet_service_src_custom_group,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            src_vendor_mac=src_vendor_mac,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule=schedule,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            service=service,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            anti_replay=anti_replay,
            tcp_session_without_syn=tcp_session_without_syn,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            dynamic_shaping=dynamic_shaping,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            utm_status=utm_status,
            inspection_mode=inspection_mode,
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            ztna_policy_redirect=ztna_policy_redirect,
            webproxy_profile=webproxy_profile,
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
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            auto_asic_offload=auto_asic_offload,
            wanopt=wanopt,
            wanopt_detection=wanopt_detection,
            wanopt_passive_opt=wanopt_passive_opt,
            wanopt_profile=wanopt_profile,
            wanopt_peer=wanopt_peer,
            webcache=webcache,
            webcache_https=webcache_https,
            webproxy_forward_server=webproxy_forward_server,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            nat=nat,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            fixedport=fixedport,
            port_preserve=port_preserve,
            port_random=port_random,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            session_ttl=session_ttl,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            fec=fec,
            wccp=wccp,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            auth_path=auth_path,
            disclaimer=disclaimer,
            email_collect=email_collect,
            vpntunnel=vpntunnel,
            natip=natip,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            comments=comments,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            redirect_url=redirect_url,
            identity_based_route=identity_based_route,
            block_notification=block_notification,
            custom_log_fields=custom_log_fields,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr_negate=dstaddr_negate,
            dstaddr6_negate=dstaddr6_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            internet_service_negate=internet_service_negate,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src_negate=internet_service6_src_negate,
            timeout_send_rst=timeout_send_rst,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dsri=dsri,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            delay_tcp_npu_session=delay_tcp_npu_session,
            vlan_filter=vlan_filter,
            sgt_check=sgt_check,
            sgt=sgt,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.policy import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/policy",
            )

        endpoint = "/firewall/policy"
        
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
        Delete firewall/policy object.

        Configure IPv4/IPv6 policies.

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
            >>> result = fgt.api.cmdb.firewall_policy.delete(policyid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not policyid:
            raise ValueError("policyid is required for DELETE")
        endpoint = "/firewall/policy/" + str(policyid)

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
        Check if firewall/policy object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_policy.exists(policyid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_policy.delete(policyid=1)

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
        policyid: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        name: str | None = None,
        uuid: str | None = None,
        srcintf: str | list[str] | list[dict[str, Any]] | None = None,
        dstintf: str | list[str] | list[dict[str, Any]] | None = None,
        action: Literal["accept", "deny", "ipsec"] | None = None,
        nat64: Literal["enable", "disable"] | None = None,
        nat46: Literal["enable", "disable"] | None = None,
        ztna_status: Literal["enable", "disable"] | None = None,
        ztna_device_ownership: Literal["enable", "disable"] | None = None,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_ems_tag_secondary: str | list[str] | list[dict[str, Any]] | None = None,
        ztna_tags_match_logic: Literal["or", "and"] | None = None,
        ztna_geo_tag: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service: Literal["enable", "disable"] | None = None,
        internet_service_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom: str | list[str] | list[dict[str, Any]] | None = None,
        network_service_dynamic: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src: Literal["enable", "disable"] | None = None,
        internet_service_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        network_service_src_dynamic: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        reputation_minimum: int | None = None,
        reputation_direction: Literal["source", "destination"] | None = None,
        src_vendor_mac: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6: Literal["enable", "disable"] | None = None,
        internet_service6_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src: Literal["enable", "disable"] | None = None,
        internet_service6_src_name: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_group: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_custom_group: str | list[str] | list[dict[str, Any]] | None = None,
        reputation_minimum6: int | None = None,
        reputation_direction6: Literal["source", "destination"] | None = None,
        rtp_nat: Literal["disable", "enable"] | None = None,
        rtp_addr: str | list[str] | list[dict[str, Any]] | None = None,
        send_deny_packet: Literal["disable", "enable"] | None = None,
        firewall_session_dirty: Literal["check-all", "check-new"] | None = None,
        schedule: str | None = None,
        schedule_timeout: Literal["enable", "disable"] | None = None,
        policy_expiry: Literal["enable", "disable"] | None = None,
        policy_expiry_date: Any | None = None,
        policy_expiry_date_utc: str | None = None,
        service: str | list[str] | list[dict[str, Any]] | None = None,
        tos_mask: str | None = None,
        tos: str | None = None,
        tos_negate: Literal["enable", "disable"] | None = None,
        anti_replay: Literal["enable", "disable"] | None = None,
        tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = None,
        geoip_anycast: Literal["enable", "disable"] | None = None,
        geoip_match: Literal["physical-location", "registered-location"] | None = None,
        dynamic_shaping: Literal["enable", "disable"] | None = None,
        passive_wan_health_measurement: Literal["enable", "disable"] | None = None,
        app_monitor: Literal["enable", "disable"] | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        inspection_mode: Literal["proxy", "flow"] | None = None,
        http_policy_redirect: Literal["enable", "disable", "legacy"] | None = None,
        ssh_policy_redirect: Literal["enable", "disable"] | None = None,
        ztna_policy_redirect: Literal["enable", "disable"] | None = None,
        webproxy_profile: str | None = None,
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
        waf_profile: str | None = None,
        ssh_filter_profile: str | None = None,
        casb_profile: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        logtraffic_start: Literal["enable", "disable"] | None = None,
        log_http_transaction: Literal["enable", "disable"] | None = None,
        capture_packet: Literal["enable", "disable"] | None = None,
        auto_asic_offload: Literal["enable", "disable"] | None = None,
        wanopt: Literal["enable", "disable"] | None = None,
        wanopt_detection: Literal["active", "passive", "off"] | None = None,
        wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = None,
        wanopt_profile: str | None = None,
        wanopt_peer: str | None = None,
        webcache: Literal["enable", "disable"] | None = None,
        webcache_https: Literal["disable", "enable"] | None = None,
        webproxy_forward_server: str | None = None,
        traffic_shaper: str | None = None,
        traffic_shaper_reverse: str | None = None,
        per_ip_shaper: str | None = None,
        nat: Literal["enable", "disable"] | None = None,
        pcp_outbound: Literal["enable", "disable"] | None = None,
        pcp_inbound: Literal["enable", "disable"] | None = None,
        pcp_poolname: str | list[str] | list[dict[str, Any]] | None = None,
        permit_any_host: Literal["enable", "disable"] | None = None,
        permit_stun_host: Literal["enable", "disable"] | None = None,
        fixedport: Literal["enable", "disable"] | None = None,
        port_preserve: Literal["enable", "disable"] | None = None,
        port_random: Literal["enable", "disable"] | None = None,
        ippool: Literal["enable", "disable"] | None = None,
        poolname: str | list[str] | list[dict[str, Any]] | None = None,
        poolname6: str | list[str] | list[dict[str, Any]] | None = None,
        session_ttl: str | None = None,
        vlan_cos_fwd: int | None = None,
        vlan_cos_rev: int | None = None,
        inbound: Literal["enable", "disable"] | None = None,
        outbound: Literal["enable", "disable"] | None = None,
        natinbound: Literal["enable", "disable"] | None = None,
        natoutbound: Literal["enable", "disable"] | None = None,
        fec: Literal["enable", "disable"] | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        ntlm: Literal["enable", "disable"] | None = None,
        ntlm_guest: Literal["enable", "disable"] | None = None,
        ntlm_enabled_browsers: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_agent_for_ntlm: str | None = None,
        groups: str | list[str] | list[dict[str, Any]] | None = None,
        users: str | list[str] | list[dict[str, Any]] | None = None,
        fsso_groups: str | list[str] | list[dict[str, Any]] | None = None,
        auth_path: Literal["enable", "disable"] | None = None,
        disclaimer: Literal["enable", "disable"] | None = None,
        email_collect: Literal["enable", "disable"] | None = None,
        vpntunnel: str | None = None,
        natip: str | None = None,
        match_vip: Literal["enable", "disable"] | None = None,
        match_vip_only: Literal["enable", "disable"] | None = None,
        diffserv_copy: Literal["enable", "disable"] | None = None,
        diffserv_forward: Literal["enable", "disable"] | None = None,
        diffserv_reverse: Literal["enable", "disable"] | None = None,
        diffservcode_forward: str | None = None,
        diffservcode_rev: str | None = None,
        tcp_mss_sender: int | None = None,
        tcp_mss_receiver: int | None = None,
        comments: str | None = None,
        auth_cert: str | None = None,
        auth_redirect_addr: str | None = None,
        redirect_url: str | None = None,
        identity_based_route: str | None = None,
        block_notification: Literal["enable", "disable"] | None = None,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = None,
        replacemsg_override_group: str | None = None,
        srcaddr_negate: Literal["enable", "disable"] | None = None,
        srcaddr6_negate: Literal["enable", "disable"] | None = None,
        dstaddr_negate: Literal["enable", "disable"] | None = None,
        dstaddr6_negate: Literal["enable", "disable"] | None = None,
        ztna_ems_tag_negate: Literal["enable", "disable"] | None = None,
        service_negate: Literal["enable", "disable"] | None = None,
        internet_service_negate: Literal["enable", "disable"] | None = None,
        internet_service_src_negate: Literal["enable", "disable"] | None = None,
        internet_service6_negate: Literal["enable", "disable"] | None = None,
        internet_service6_src_negate: Literal["enable", "disable"] | None = None,
        timeout_send_rst: Literal["enable", "disable"] | None = None,
        captive_portal_exempt: Literal["enable", "disable"] | None = None,
        decrypted_traffic_mirror: str | None = None,
        dsri: Literal["enable", "disable"] | None = None,
        radius_mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = None,
        vlan_filter: str | None = None,
        sgt_check: Literal["enable", "disable"] | None = None,
        sgt: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        internet_service6_src_fortiguard: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/policy object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (policyid) in the payload.

        Args:
            payload_dict: Resource data including policyid (primary key)
            policyid: Field policyid
            status: Field status
            name: Field name
            uuid: Field uuid
            srcintf: Field srcintf
            dstintf: Field dstintf
            action: Field action
            nat64: Field nat64
            nat46: Field nat46
            ztna_status: Field ztna-status
            ztna_device_ownership: Field ztna-device-ownership
            srcaddr: Field srcaddr
            dstaddr: Field dstaddr
            srcaddr6: Field srcaddr6
            dstaddr6: Field dstaddr6
            ztna_ems_tag: Field ztna-ems-tag
            ztna_ems_tag_secondary: Field ztna-ems-tag-secondary
            ztna_tags_match_logic: Field ztna-tags-match-logic
            ztna_geo_tag: Field ztna-geo-tag
            internet_service: Field internet-service
            internet_service_name: Field internet-service-name
            internet_service_group: Field internet-service-group
            internet_service_custom: Field internet-service-custom
            network_service_dynamic: Field network-service-dynamic
            internet_service_custom_group: Field internet-service-custom-group
            internet_service_src: Field internet-service-src
            internet_service_src_name: Field internet-service-src-name
            internet_service_src_group: Field internet-service-src-group
            internet_service_src_custom: Field internet-service-src-custom
            network_service_src_dynamic: Field network-service-src-dynamic
            internet_service_src_custom_group: Field internet-service-src-custom-group
            reputation_minimum: Field reputation-minimum
            reputation_direction: Field reputation-direction
            src_vendor_mac: Field src-vendor-mac
            internet_service6: Field internet-service6
            internet_service6_name: Field internet-service6-name
            internet_service6_group: Field internet-service6-group
            internet_service6_custom: Field internet-service6-custom
            internet_service6_custom_group: Field internet-service6-custom-group
            internet_service6_src: Field internet-service6-src
            internet_service6_src_name: Field internet-service6-src-name
            internet_service6_src_group: Field internet-service6-src-group
            internet_service6_src_custom: Field internet-service6-src-custom
            internet_service6_src_custom_group: Field internet-service6-src-custom-group
            reputation_minimum6: Field reputation-minimum6
            reputation_direction6: Field reputation-direction6
            rtp_nat: Field rtp-nat
            rtp_addr: Field rtp-addr
            send_deny_packet: Field send-deny-packet
            firewall_session_dirty: Field firewall-session-dirty
            schedule: Field schedule
            schedule_timeout: Field schedule-timeout
            policy_expiry: Field policy-expiry
            policy_expiry_date: Field policy-expiry-date
            policy_expiry_date_utc: Field policy-expiry-date-utc
            service: Field service
            tos_mask: Field tos-mask
            tos: Field tos
            tos_negate: Field tos-negate
            anti_replay: Field anti-replay
            tcp_session_without_syn: Field tcp-session-without-syn
            geoip_anycast: Field geoip-anycast
            geoip_match: Field geoip-match
            dynamic_shaping: Field dynamic-shaping
            passive_wan_health_measurement: Field passive-wan-health-measurement
            app_monitor: Field app-monitor
            utm_status: Field utm-status
            inspection_mode: Field inspection-mode
            http_policy_redirect: Field http-policy-redirect
            ssh_policy_redirect: Field ssh-policy-redirect
            ztna_policy_redirect: Field ztna-policy-redirect
            webproxy_profile: Field webproxy-profile
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
            waf_profile: Field waf-profile
            ssh_filter_profile: Field ssh-filter-profile
            casb_profile: Field casb-profile
            logtraffic: Field logtraffic
            logtraffic_start: Field logtraffic-start
            log_http_transaction: Field log-http-transaction
            capture_packet: Field capture-packet
            auto_asic_offload: Field auto-asic-offload
            wanopt: Field wanopt
            wanopt_detection: Field wanopt-detection
            wanopt_passive_opt: Field wanopt-passive-opt
            wanopt_profile: Field wanopt-profile
            wanopt_peer: Field wanopt-peer
            webcache: Field webcache
            webcache_https: Field webcache-https
            webproxy_forward_server: Field webproxy-forward-server
            traffic_shaper: Field traffic-shaper
            traffic_shaper_reverse: Field traffic-shaper-reverse
            per_ip_shaper: Field per-ip-shaper
            nat: Field nat
            pcp_outbound: Field pcp-outbound
            pcp_inbound: Field pcp-inbound
            pcp_poolname: Field pcp-poolname
            permit_any_host: Field permit-any-host
            permit_stun_host: Field permit-stun-host
            fixedport: Field fixedport
            port_preserve: Field port-preserve
            port_random: Field port-random
            ippool: Field ippool
            poolname: Field poolname
            poolname6: Field poolname6
            session_ttl: Field session-ttl
            vlan_cos_fwd: Field vlan-cos-fwd
            vlan_cos_rev: Field vlan-cos-rev
            inbound: Field inbound
            outbound: Field outbound
            natinbound: Field natinbound
            natoutbound: Field natoutbound
            fec: Field fec
            wccp: Field wccp
            ntlm: Field ntlm
            ntlm_guest: Field ntlm-guest
            ntlm_enabled_browsers: Field ntlm-enabled-browsers
            fsso_agent_for_ntlm: Field fsso-agent-for-ntlm
            groups: Field groups
            users: Field users
            fsso_groups: Field fsso-groups
            auth_path: Field auth-path
            disclaimer: Field disclaimer
            email_collect: Field email-collect
            vpntunnel: Field vpntunnel
            natip: Field natip
            match_vip: Field match-vip
            match_vip_only: Field match-vip-only
            diffserv_copy: Field diffserv-copy
            diffserv_forward: Field diffserv-forward
            diffserv_reverse: Field diffserv-reverse
            diffservcode_forward: Field diffservcode-forward
            diffservcode_rev: Field diffservcode-rev
            tcp_mss_sender: Field tcp-mss-sender
            tcp_mss_receiver: Field tcp-mss-receiver
            comments: Field comments
            auth_cert: Field auth-cert
            auth_redirect_addr: Field auth-redirect-addr
            redirect_url: Field redirect-url
            identity_based_route: Field identity-based-route
            block_notification: Field block-notification
            custom_log_fields: Field custom-log-fields
            replacemsg_override_group: Field replacemsg-override-group
            srcaddr_negate: Field srcaddr-negate
            srcaddr6_negate: Field srcaddr6-negate
            dstaddr_negate: Field dstaddr-negate
            dstaddr6_negate: Field dstaddr6-negate
            ztna_ems_tag_negate: Field ztna-ems-tag-negate
            service_negate: Field service-negate
            internet_service_negate: Field internet-service-negate
            internet_service_src_negate: Field internet-service-src-negate
            internet_service6_negate: Field internet-service6-negate
            internet_service6_src_negate: Field internet-service6-src-negate
            timeout_send_rst: Field timeout-send-rst
            captive_portal_exempt: Field captive-portal-exempt
            decrypted_traffic_mirror: Field decrypted-traffic-mirror
            dsri: Field dsri
            radius_mac_auth_bypass: Field radius-mac-auth-bypass
            radius_ip_auth_bypass: Field radius-ip-auth-bypass
            delay_tcp_npu_session: Field delay-tcp-npu-session
            vlan_filter: Field vlan-filter
            sgt_check: Field sgt-check
            sgt: Field sgt
            internet_service_fortiguard: Field internet-service-fortiguard
            internet_service_src_fortiguard: Field internet-service-src-fortiguard
            internet_service6_fortiguard: Field internet-service6-fortiguard
            internet_service6_src_fortiguard: Field internet-service6-src-fortiguard
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.firewall_policy.set(
            ...     policyid=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_policy.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_policy.set(payload_dict=obj_data)
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
            policyid=policyid,
            status=status,
            name=name,
            uuid=uuid,
            srcintf=srcintf,
            dstintf=dstintf,
            action=action,
            nat64=nat64,
            nat46=nat46,
            ztna_status=ztna_status,
            ztna_device_ownership=ztna_device_ownership,
            srcaddr=srcaddr,
            dstaddr=dstaddr,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            ztna_ems_tag=ztna_ems_tag,
            ztna_ems_tag_secondary=ztna_ems_tag_secondary,
            ztna_tags_match_logic=ztna_tags_match_logic,
            ztna_geo_tag=ztna_geo_tag,
            internet_service=internet_service,
            internet_service_name=internet_service_name,
            internet_service_group=internet_service_group,
            internet_service_custom=internet_service_custom,
            network_service_dynamic=network_service_dynamic,
            internet_service_custom_group=internet_service_custom_group,
            internet_service_src=internet_service_src,
            internet_service_src_name=internet_service_src_name,
            internet_service_src_group=internet_service_src_group,
            internet_service_src_custom=internet_service_src_custom,
            network_service_src_dynamic=network_service_src_dynamic,
            internet_service_src_custom_group=internet_service_src_custom_group,
            reputation_minimum=reputation_minimum,
            reputation_direction=reputation_direction,
            src_vendor_mac=src_vendor_mac,
            internet_service6=internet_service6,
            internet_service6_name=internet_service6_name,
            internet_service6_group=internet_service6_group,
            internet_service6_custom=internet_service6_custom,
            internet_service6_custom_group=internet_service6_custom_group,
            internet_service6_src=internet_service6_src,
            internet_service6_src_name=internet_service6_src_name,
            internet_service6_src_group=internet_service6_src_group,
            internet_service6_src_custom=internet_service6_src_custom,
            internet_service6_src_custom_group=internet_service6_src_custom_group,
            reputation_minimum6=reputation_minimum6,
            reputation_direction6=reputation_direction6,
            rtp_nat=rtp_nat,
            rtp_addr=rtp_addr,
            send_deny_packet=send_deny_packet,
            firewall_session_dirty=firewall_session_dirty,
            schedule=schedule,
            schedule_timeout=schedule_timeout,
            policy_expiry=policy_expiry,
            policy_expiry_date=policy_expiry_date,
            policy_expiry_date_utc=policy_expiry_date_utc,
            service=service,
            tos_mask=tos_mask,
            tos=tos,
            tos_negate=tos_negate,
            anti_replay=anti_replay,
            tcp_session_without_syn=tcp_session_without_syn,
            geoip_anycast=geoip_anycast,
            geoip_match=geoip_match,
            dynamic_shaping=dynamic_shaping,
            passive_wan_health_measurement=passive_wan_health_measurement,
            app_monitor=app_monitor,
            utm_status=utm_status,
            inspection_mode=inspection_mode,
            http_policy_redirect=http_policy_redirect,
            ssh_policy_redirect=ssh_policy_redirect,
            ztna_policy_redirect=ztna_policy_redirect,
            webproxy_profile=webproxy_profile,
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
            waf_profile=waf_profile,
            ssh_filter_profile=ssh_filter_profile,
            casb_profile=casb_profile,
            logtraffic=logtraffic,
            logtraffic_start=logtraffic_start,
            log_http_transaction=log_http_transaction,
            capture_packet=capture_packet,
            auto_asic_offload=auto_asic_offload,
            wanopt=wanopt,
            wanopt_detection=wanopt_detection,
            wanopt_passive_opt=wanopt_passive_opt,
            wanopt_profile=wanopt_profile,
            wanopt_peer=wanopt_peer,
            webcache=webcache,
            webcache_https=webcache_https,
            webproxy_forward_server=webproxy_forward_server,
            traffic_shaper=traffic_shaper,
            traffic_shaper_reverse=traffic_shaper_reverse,
            per_ip_shaper=per_ip_shaper,
            nat=nat,
            pcp_outbound=pcp_outbound,
            pcp_inbound=pcp_inbound,
            pcp_poolname=pcp_poolname,
            permit_any_host=permit_any_host,
            permit_stun_host=permit_stun_host,
            fixedport=fixedport,
            port_preserve=port_preserve,
            port_random=port_random,
            ippool=ippool,
            poolname=poolname,
            poolname6=poolname6,
            session_ttl=session_ttl,
            vlan_cos_fwd=vlan_cos_fwd,
            vlan_cos_rev=vlan_cos_rev,
            inbound=inbound,
            outbound=outbound,
            natinbound=natinbound,
            natoutbound=natoutbound,
            fec=fec,
            wccp=wccp,
            ntlm=ntlm,
            ntlm_guest=ntlm_guest,
            ntlm_enabled_browsers=ntlm_enabled_browsers,
            fsso_agent_for_ntlm=fsso_agent_for_ntlm,
            groups=groups,
            users=users,
            fsso_groups=fsso_groups,
            auth_path=auth_path,
            disclaimer=disclaimer,
            email_collect=email_collect,
            vpntunnel=vpntunnel,
            natip=natip,
            match_vip=match_vip,
            match_vip_only=match_vip_only,
            diffserv_copy=diffserv_copy,
            diffserv_forward=diffserv_forward,
            diffserv_reverse=diffserv_reverse,
            diffservcode_forward=diffservcode_forward,
            diffservcode_rev=diffservcode_rev,
            tcp_mss_sender=tcp_mss_sender,
            tcp_mss_receiver=tcp_mss_receiver,
            comments=comments,
            auth_cert=auth_cert,
            auth_redirect_addr=auth_redirect_addr,
            redirect_url=redirect_url,
            identity_based_route=identity_based_route,
            block_notification=block_notification,
            custom_log_fields=custom_log_fields,
            replacemsg_override_group=replacemsg_override_group,
            srcaddr_negate=srcaddr_negate,
            srcaddr6_negate=srcaddr6_negate,
            dstaddr_negate=dstaddr_negate,
            dstaddr6_negate=dstaddr6_negate,
            ztna_ems_tag_negate=ztna_ems_tag_negate,
            service_negate=service_negate,
            internet_service_negate=internet_service_negate,
            internet_service_src_negate=internet_service_src_negate,
            internet_service6_negate=internet_service6_negate,
            internet_service6_src_negate=internet_service6_src_negate,
            timeout_send_rst=timeout_send_rst,
            captive_portal_exempt=captive_portal_exempt,
            decrypted_traffic_mirror=decrypted_traffic_mirror,
            dsri=dsri,
            radius_mac_auth_bypass=radius_mac_auth_bypass,
            radius_ip_auth_bypass=radius_ip_auth_bypass,
            delay_tcp_npu_session=delay_tcp_npu_session,
            vlan_filter=vlan_filter,
            sgt_check=sgt_check,
            sgt=sgt,
            internet_service_fortiguard=internet_service_fortiguard,
            internet_service_src_fortiguard=internet_service_src_fortiguard,
            internet_service6_fortiguard=internet_service6_fortiguard,
            internet_service6_src_fortiguard=internet_service6_src_fortiguard,
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
        Move firewall/policy object to a new position.
        
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
            >>> fgt.api.cmdb.firewall_policy.move(
            ...     policyid=100,
            ...     action="before",
            ...     reference_policyid=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/policy",
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
        Clone firewall/policy object.
        
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
            >>> fgt.api.cmdb.firewall_policy.clone(
            ...     policyid=1,
            ...     new_policyid=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/policy",
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
        Check if firewall/policy object exists.
        
        Args:
            policyid: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_policy.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_policy.post(payload_dict=data)
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


"""
FortiOS CMDB - System settings

Configuration endpoint for managing cmdb system/settings objects.

API Endpoints:
    GET    /cmdb/system/settings
    POST   /cmdb/system/settings
    PUT    /cmdb/system/settings/{identifier}
    DELETE /cmdb/system/settings/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_settings.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_settings.post(
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

class Settings(CRUDEndpoint, MetadataMixin):
    """Settings Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "settings"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "gui_default_policy_columns": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
    }
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Settings endpoint."""
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
        Retrieve system/settings configuration.

        Configure VDOM settings.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
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
            >>> # Get all system/settings objects
            >>> result = fgt.api.cmdb.system_settings.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_settings.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_settings.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_settings.get_schema()

        See Also:
            - post(): Create new system/settings object
            - put(): Update existing system/settings object
            - delete(): Remove system/settings object
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
            endpoint = f"/system/settings/{name}"
            unwrap_single = True
        else:
            endpoint = "/system/settings"
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
            >>> schema = fgt.api.cmdb.system_settings.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_settings.get_schema(format="json-schema")
        
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
        comments: str | None = None,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = None,
        lan_extension_controller_addr: str | None = None,
        lan_extension_controller_port: int | None = None,
        opmode: Literal["nat", "transparent"] | None = None,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = None,
        http_external_dest: Literal["fortiweb", "forticache"] | None = None,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = None,
        manageip: str | None = None,
        gateway: str | None = None,
        ip: Any | None = None,
        manageip6: str | None = None,
        gateway6: str | None = None,
        ip6: str | None = None,
        device: str | None = None,
        bfd: Literal["enable", "disable"] | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_required_min_rx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = None,
        utf8_spam_tagging: Literal["enable", "disable"] | None = None,
        wccp_cache_engine: Literal["enable", "disable"] | None = None,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = None,
        vpn_stats_period: int | None = None,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = None,
        mac_ttl: int | None = None,
        fw_session_hairpin: Literal["enable", "disable"] | None = None,
        prp_trailer_action: Literal["enable", "disable"] | None = None,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = None,
        dhcp_proxy: Literal["enable", "disable"] | None = None,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        dhcp_proxy_interface: str | None = None,
        dhcp_proxy_vrf_select: int | None = None,
        dhcp_server_ip: str | list[str] | None = None,
        dhcp6_server_ip: str | list[str] | None = None,
        central_nat: Literal["enable", "disable"] | None = None,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = None,
        lldp_reception: Literal["enable", "disable", "global"] | None = None,
        lldp_transmission: Literal["enable", "disable", "global"] | None = None,
        link_down_access: Literal["enable", "disable"] | None = None,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = None,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = None,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = None,
        detect_unknown_esp: Literal["enable", "disable"] | None = None,
        intree_ses_best_route: Literal["force", "disable"] | None = None,
        auxiliary_session: Literal["enable", "disable"] | None = None,
        asymroute: Literal["enable", "disable"] | None = None,
        asymroute_icmp: Literal["enable", "disable"] | None = None,
        tcp_session_without_syn: Literal["enable", "disable"] | None = None,
        ses_denied_traffic: Literal["enable", "disable"] | None = None,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = None,
        strict_src_check: Literal["enable", "disable"] | None = None,
        allow_linkdown_path: Literal["enable", "disable"] | None = None,
        asymroute6: Literal["enable", "disable"] | None = None,
        asymroute6_icmp: Literal["enable", "disable"] | None = None,
        sctp_session_without_init: Literal["enable", "disable"] | None = None,
        sip_expectation: Literal["enable", "disable"] | None = None,
        sip_nat_trace: Literal["enable", "disable"] | None = None,
        h323_direct_model: Literal["disable", "enable"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        sip_tcp_port: int | list[str] | None = None,
        sip_udp_port: int | list[str] | None = None,
        sip_ssl_port: int | None = None,
        sccp_port: int | None = None,
        multicast_forward: Literal["enable", "disable"] | None = None,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = None,
        multicast_skip_policy: Literal["enable", "disable"] | None = None,
        allow_subnet_overlap: Literal["enable", "disable"] | None = None,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = None,
        ecmp_max_paths: int | None = None,
        discovered_device_timeout: int | None = None,
        email_portal_check_dns: Literal["disable", "enable"] | None = None,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = None,
        gui_icap: Literal["enable", "disable"] | None = None,
        gui_implicit_policy: Literal["enable", "disable"] | None = None,
        gui_dns_database: Literal["enable", "disable"] | None = None,
        gui_load_balance: Literal["enable", "disable"] | None = None,
        gui_multicast_policy: Literal["enable", "disable"] | None = None,
        gui_dos_policy: Literal["enable", "disable"] | None = None,
        gui_object_colors: Literal["enable", "disable"] | None = None,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = None,
        gui_voip_profile: Literal["enable", "disable"] | None = None,
        gui_ap_profile: Literal["enable", "disable"] | None = None,
        gui_security_profile_group: Literal["enable", "disable"] | None = None,
        gui_local_in_policy: Literal["enable", "disable"] | None = None,
        gui_wanopt_cache: Literal["enable", "disable"] | None = None,
        gui_explicit_proxy: Literal["enable", "disable"] | None = None,
        gui_dynamic_routing: Literal["enable", "disable"] | None = None,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = None,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = None,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = None,
        gui_threat_weight: Literal["enable", "disable"] | None = None,
        gui_spamfilter: Literal["enable", "disable"] | None = None,
        gui_file_filter: Literal["enable", "disable"] | None = None,
        gui_application_control: Literal["enable", "disable"] | None = None,
        gui_ips: Literal["enable", "disable"] | None = None,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = None,
        gui_vpn: Literal["enable", "disable"] | None = None,
        gui_sslvpn: Literal["enable", "disable"] | None = None,
        gui_wireless_controller: Literal["enable", "disable"] | None = None,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = None,
        gui_switch_controller: Literal["enable", "disable"] | None = None,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = None,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = None,
        gui_traffic_shaping: Literal["enable", "disable"] | None = None,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = None,
        gui_antivirus: Literal["enable", "disable"] | None = None,
        gui_webfilter: Literal["enable", "disable"] | None = None,
        gui_videofilter: Literal["enable", "disable"] | None = None,
        gui_dnsfilter: Literal["enable", "disable"] | None = None,
        gui_waf_profile: Literal["enable", "disable"] | None = None,
        gui_dlp_profile: Literal["enable", "disable"] | None = None,
        gui_dlp_advanced: Literal["enable", "disable"] | None = None,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = None,
        gui_casb: Literal["enable", "disable"] | None = None,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = None,
        gui_advanced_policy: Literal["enable", "disable"] | None = None,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = None,
        gui_email_collection: Literal["enable", "disable"] | None = None,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = None,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = None,
        gui_ztna: Literal["enable", "disable"] | None = None,
        gui_ot: Literal["enable", "disable"] | None = None,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = None,
        gui_gtp: Literal["enable", "disable"] | None = None,
        location_id: str | None = None,
        ike_session_resume: Literal["enable", "disable"] | None = None,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = None,
        ike_dn_format: Literal["with-space", "no-space"] | None = None,
        ike_port: int | None = None,
        ike_tcp_port: int | None = None,
        ike_policy_route: Literal["enable", "disable"] | None = None,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = None,
        block_land_attack: Literal["disable", "enable"] | None = None,
        default_app_port_as_service: Literal["enable", "disable"] | None = None,
        fqdn_session_check: Literal["enable", "disable"] | None = None,
        ext_resource_session_check: Literal["enable", "disable"] | None = None,
        dyn_addr_session_check: Literal["enable", "disable"] | None = None,
        default_policy_expiry_days: int | None = None,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = None,
        internet_service_database_cache: Literal["disable", "enable"] | None = None,
        internet_service_app_ctrl_size: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/settings object.

        Configure VDOM settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            comments: VDOM comments.
            vdom_type: Vdom type (traffic, lan-extension or admin).
            lan_extension_controller_addr: Controller IP address or FQDN to connect.
            lan_extension_controller_port: Controller port to connect.
            opmode: Firewall operation mode (NAT or Transparent).
            ngfw_mode: Next Generation Firewall (NGFW) mode.
            http_external_dest: Offload HTTP traffic to FortiWeb or FortiCache.
            firewall_session_dirty: Select how to manage sessions affected by firewall policy configuration changes.
            manageip: Transparent mode IPv4 management IP address and netmask.
            gateway: Transparent mode IPv4 default gateway IP address.
            ip: IP address and netmask.
            manageip6: Transparent mode IPv6 management IP address and netmask.
            gateway6: Transparent mode IPv6 default gateway IP address.
            ip6: IPv6 address prefix for NAT mode.
            device: Interface to use for management access for NAT mode.
            bfd: Enable/disable Bi-directional Forwarding Detection (BFD) on all interfaces.
            bfd_desired_min_tx: BFD desired minimal transmit interval (1 - 100000 ms, default = 250).
            bfd_required_min_rx: BFD required minimal receive interval (1 - 100000 ms, default = 250).
            bfd_detect_mult: BFD detection multiplier (1 - 50, default = 3).
            bfd_dont_enforce_src_port: Enable to not enforce verifying the source port of BFD Packets.
            utf8_spam_tagging: Enable/disable converting antispam tags to UTF-8 for better non-ASCII character support.
            wccp_cache_engine: Enable/disable WCCP cache engine.
            vpn_stats_log: Enable/disable periodic VPN log statistics for one or more types of VPN. Separate names with a space.
            vpn_stats_period: Period to send VPN log statistics (0 or 60 - 86400 sec).
            v4_ecmp_mode: IPv4 Equal-cost multi-path (ECMP) routing and load balancing mode.
            mac_ttl: Duration of MAC addresses in Transparent mode (300 - 8640000 sec, default = 300).
            fw_session_hairpin: Enable/disable checking for a matching policy each time hairpin traffic goes through the FortiGate.
            prp_trailer_action: Enable/disable action to take on PRP trailer.
            snat_hairpin_traffic: Enable/disable source NAT (SNAT) for VIP hairpin traffic.
            dhcp_proxy: Enable/disable the DHCP Proxy.
            dhcp_proxy_interface_select_method: Specify how to select outgoing interface to reach server.
            dhcp_proxy_interface: Specify outgoing interface to reach server.
            dhcp_proxy_vrf_select: VRF ID used for connection to server.
            dhcp_server_ip: DHCP Server IPv4 address.
            dhcp6_server_ip: DHCPv6 server IPv6 address.
            central_nat: Enable/disable central NAT.
            gui_default_policy_columns: Default columns to display for policy lists on GUI.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP) reception for this VDOM or apply global settings to this VDOM.
            lldp_transmission: Enable/disable Link Layer Discovery Protocol (LLDP) transmission for this VDOM or apply global settings to this VDOM.
            link_down_access: Enable/disable link down access traffic.
            nat46_generate_ipv6_fragment_header: Enable/disable NAT46 IPv6 fragment header generation.
            nat46_force_ipv4_packet_forwarding: Enable/disable mandatory IPv4 packet forwarding in NAT46.
            nat64_force_ipv6_packet_forwarding: Enable/disable mandatory IPv6 packet forwarding in NAT64.
            detect_unknown_esp: Enable/disable detection of unknown ESP packets (default = enable).
            intree_ses_best_route: Force the intree session to always use the best route.
            auxiliary_session: Enable/disable auxiliary session.
            asymroute: Enable/disable IPv4 asymmetric routing.
            asymroute_icmp: Enable/disable ICMP asymmetric routing.
            tcp_session_without_syn: Enable/disable allowing TCP session without SYN flags.
            ses_denied_traffic: Enable/disable including denied session in the session table.
            ses_denied_multicast_traffic: Enable/disable including denied multicast session in the session table.
            strict_src_check: Enable/disable strict source verification.
            allow_linkdown_path: Enable/disable link down path.
            asymroute6: Enable/disable asymmetric IPv6 routing.
            asymroute6_icmp: Enable/disable asymmetric ICMPv6 routing.
            sctp_session_without_init: Enable/disable SCTP session creation without SCTP INIT.
            sip_expectation: Enable/disable the SIP kernel session helper to create an expectation for port 5060.
            sip_nat_trace: Enable/disable recording the original SIP source IP address when NAT is used.
            h323_direct_model: Enable/disable H323 direct model.
            status: Enable/disable this VDOM.
            sip_tcp_port: TCP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).
            sip_udp_port: UDP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).
            sip_ssl_port: TCP port the SIP proxy monitors for SIP SSL/TLS traffic (0 - 65535, default = 5061).
            sccp_port: TCP port the SCCP proxy monitors for SCCP traffic (0 - 65535, default = 2000).
            multicast_forward: Enable/disable multicast forwarding.
            multicast_ttl_notchange: Enable/disable preventing the FortiGate from changing the TTL for forwarded multicast packets.
            multicast_skip_policy: Enable/disable allowing multicast traffic through the FortiGate without a policy check.
            allow_subnet_overlap: Enable/disable allowing interface subnets to use overlapping IP addresses.
            deny_tcp_with_icmp: Enable/disable denying TCP by sending an ICMP communication prohibited packet.
            ecmp_max_paths: Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Set to 1 to disable ECMP routing (1 - 255, default = 255).
            discovered_device_timeout: Timeout for discovered devices (1 - 365 days, default = 28).
            email_portal_check_dns: Enable/disable using DNS to validate email addresses collected by a captive portal.
            default_voip_alg_mode: Configure how the FortiGate handles VoIP traffic when a policy that accepts the traffic doesn't include a VoIP profile.
            gui_icap: Enable/disable ICAP on the GUI.
            gui_implicit_policy: Enable/disable implicit firewall policies on the GUI.
            gui_dns_database: Enable/disable DNS database settings on the GUI.
            gui_load_balance: Enable/disable server load balancing on the GUI.
            gui_multicast_policy: Enable/disable multicast firewall policies on the GUI.
            gui_dos_policy: Enable/disable DoS policies on the GUI.
            gui_object_colors: Enable/disable object colors on the GUI.
            gui_route_tag_address_creation: Enable/disable route-tag addresses on the GUI.
            gui_voip_profile: Enable/disable VoIP profiles on the GUI.
            gui_ap_profile: Enable/disable FortiAP profiles on the GUI.
            gui_security_profile_group: Enable/disable Security Profile Groups on the GUI.
            gui_local_in_policy: Enable/disable Local-In policies on the GUI.
            gui_wanopt_cache: Enable/disable WAN Optimization and Web Caching on the GUI.
            gui_explicit_proxy: Enable/disable the explicit proxy on the GUI.
            gui_dynamic_routing: Enable/disable dynamic routing on the GUI.
            gui_sslvpn_personal_bookmarks: Enable/disable SSL-VPN personal bookmark management on the GUI.
            gui_sslvpn_realms: Enable/disable SSL-VPN realms on the GUI.
            gui_policy_based_ipsec: Enable/disable policy-based IPsec VPN on the GUI.
            gui_threat_weight: Enable/disable threat weight on the GUI.
            gui_spamfilter: Enable/disable Antispam on the GUI.
            gui_file_filter: Enable/disable File-filter on the GUI.
            gui_application_control: Enable/disable application control on the GUI.
            gui_ips: Enable/disable IPS on the GUI.
            gui_dhcp_advanced: Enable/disable advanced DHCP options on the GUI.
            gui_vpn: Enable/disable IPsec VPN settings pages on the GUI.
            gui_sslvpn: Enable/disable SSL-VPN settings pages on the GUI.
            gui_wireless_controller: Enable/disable the wireless controller on the GUI.
            gui_advanced_wireless_features: Enable/disable advanced wireless features in GUI.
            gui_switch_controller: Enable/disable the switch controller on the GUI.
            gui_fortiap_split_tunneling: Enable/disable FortiAP split tunneling on the GUI.
            gui_webfilter_advanced: Enable/disable advanced web filtering on the GUI.
            gui_traffic_shaping: Enable/disable traffic shaping on the GUI.
            gui_wan_load_balancing: Enable/disable SD-WAN on the GUI.
            gui_antivirus: Enable/disable AntiVirus on the GUI.
            gui_webfilter: Enable/disable Web filtering on the GUI.
            gui_videofilter: Enable/disable Video filtering on the GUI.
            gui_dnsfilter: Enable/disable DNS Filtering on the GUI.
            gui_waf_profile: Enable/disable Web Application Firewall on the GUI.
            gui_dlp_profile: Enable/disable Data Loss Prevention on the GUI.
            gui_dlp_advanced: Enable/disable Show advanced DLP expressions on the GUI.
            gui_virtual_patch_profile: Enable/disable Virtual Patching on the GUI.
            gui_casb: Enable/disable Inline-CASB on the GUI.
            gui_fortiextender_controller: Enable/disable FortiExtender on the GUI.
            gui_advanced_policy: Enable/disable advanced policy configuration on the GUI.
            gui_allow_unnamed_policy: Enable/disable the requirement for policy naming on the GUI.
            gui_email_collection: Enable/disable email collection on the GUI.
            gui_multiple_interface_policy: Enable/disable adding multiple interfaces to a policy on the GUI.
            gui_policy_disclaimer: Enable/disable policy disclaimer on the GUI.
            gui_ztna: Enable/disable Zero Trust Network Access features on the GUI.
            gui_ot: Enable/disable Operational technology features on the GUI.
            gui_dynamic_device_os_id: Enable/disable Create dynamic addresses to manage known devices.
            gui_gtp: Enable/disable Manage general radio packet service (GPRS) protocols on the GUI.
            location_id: Local location ID in the form of an IPv4 address.
            ike_session_resume: Enable/disable IKEv2 session resumption (RFC 5723).
            ike_quick_crash_detect: Enable/disable IKE quick crash detection (RFC 6290).
            ike_dn_format: Configure IKE ASN.1 Distinguished Name format conventions.
            ike_port: UDP port for IKE/IPsec traffic (default 500).
            ike_tcp_port: TCP port for IKE/IPsec traffic (default 443).
            ike_policy_route: Enable/disable IKE Policy Based Routing (PBR).
            ike_detailed_event_logs: Enable/disable detail log for IKE events.
            block_land_attack: Enable/disable blocking of land attacks.
            default_app_port_as_service: Enable/disable policy service enforcement based on application default ports.
            fqdn_session_check: Enable/disable dirty session check caused by FQDN updates.
            ext_resource_session_check: Enable/disable dirty session check caused by external resource updates.
            dyn_addr_session_check: Enable/disable dirty session check caused by dynamic address updates.
            default_policy_expiry_days: Default policy expiry in days (0 - 365 days, default = 30).
            gui_enforce_change_summary: Enforce change summaries for select tables in the GUI.
            internet_service_database_cache: Enable/disable Internet Service database caching.
            internet_service_app_ctrl_size: Maximum number of tuple entries (protocol, port, IP address, application ID) stored by the FortiGate unit (0 - 4294967295, default = 32768). A smaller value limits the FortiGate unit from learning about internet applications.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_settings.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_settings.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if gui_default_policy_columns is not None:
            gui_default_policy_columns = normalize_table_field(
                gui_default_policy_columns,
                mkey="name",
                required_fields=['name'],
                field_name="gui_default_policy_columns",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            comments=comments,
            vdom_type=vdom_type,
            lan_extension_controller_addr=lan_extension_controller_addr,
            lan_extension_controller_port=lan_extension_controller_port,
            opmode=opmode,
            ngfw_mode=ngfw_mode,
            http_external_dest=http_external_dest,
            firewall_session_dirty=firewall_session_dirty,
            manageip=manageip,
            gateway=gateway,
            ip=ip,
            manageip6=manageip6,
            gateway6=gateway6,
            ip6=ip6,
            device=device,
            bfd=bfd,
            bfd_desired_min_tx=bfd_desired_min_tx,
            bfd_required_min_rx=bfd_required_min_rx,
            bfd_detect_mult=bfd_detect_mult,
            bfd_dont_enforce_src_port=bfd_dont_enforce_src_port,
            utf8_spam_tagging=utf8_spam_tagging,
            wccp_cache_engine=wccp_cache_engine,
            vpn_stats_log=vpn_stats_log,
            vpn_stats_period=vpn_stats_period,
            v4_ecmp_mode=v4_ecmp_mode,
            mac_ttl=mac_ttl,
            fw_session_hairpin=fw_session_hairpin,
            prp_trailer_action=prp_trailer_action,
            snat_hairpin_traffic=snat_hairpin_traffic,
            dhcp_proxy=dhcp_proxy,
            dhcp_proxy_interface_select_method=dhcp_proxy_interface_select_method,
            dhcp_proxy_interface=dhcp_proxy_interface,
            dhcp_proxy_vrf_select=dhcp_proxy_vrf_select,
            dhcp_server_ip=dhcp_server_ip,
            dhcp6_server_ip=dhcp6_server_ip,
            central_nat=central_nat,
            gui_default_policy_columns=gui_default_policy_columns,
            lldp_reception=lldp_reception,
            lldp_transmission=lldp_transmission,
            link_down_access=link_down_access,
            nat46_generate_ipv6_fragment_header=nat46_generate_ipv6_fragment_header,
            nat46_force_ipv4_packet_forwarding=nat46_force_ipv4_packet_forwarding,
            nat64_force_ipv6_packet_forwarding=nat64_force_ipv6_packet_forwarding,
            detect_unknown_esp=detect_unknown_esp,
            intree_ses_best_route=intree_ses_best_route,
            auxiliary_session=auxiliary_session,
            asymroute=asymroute,
            asymroute_icmp=asymroute_icmp,
            tcp_session_without_syn=tcp_session_without_syn,
            ses_denied_traffic=ses_denied_traffic,
            ses_denied_multicast_traffic=ses_denied_multicast_traffic,
            strict_src_check=strict_src_check,
            allow_linkdown_path=allow_linkdown_path,
            asymroute6=asymroute6,
            asymroute6_icmp=asymroute6_icmp,
            sctp_session_without_init=sctp_session_without_init,
            sip_expectation=sip_expectation,
            sip_nat_trace=sip_nat_trace,
            h323_direct_model=h323_direct_model,
            status=status,
            sip_tcp_port=sip_tcp_port,
            sip_udp_port=sip_udp_port,
            sip_ssl_port=sip_ssl_port,
            sccp_port=sccp_port,
            multicast_forward=multicast_forward,
            multicast_ttl_notchange=multicast_ttl_notchange,
            multicast_skip_policy=multicast_skip_policy,
            allow_subnet_overlap=allow_subnet_overlap,
            deny_tcp_with_icmp=deny_tcp_with_icmp,
            ecmp_max_paths=ecmp_max_paths,
            discovered_device_timeout=discovered_device_timeout,
            email_portal_check_dns=email_portal_check_dns,
            default_voip_alg_mode=default_voip_alg_mode,
            gui_icap=gui_icap,
            gui_implicit_policy=gui_implicit_policy,
            gui_dns_database=gui_dns_database,
            gui_load_balance=gui_load_balance,
            gui_multicast_policy=gui_multicast_policy,
            gui_dos_policy=gui_dos_policy,
            gui_object_colors=gui_object_colors,
            gui_route_tag_address_creation=gui_route_tag_address_creation,
            gui_voip_profile=gui_voip_profile,
            gui_ap_profile=gui_ap_profile,
            gui_security_profile_group=gui_security_profile_group,
            gui_local_in_policy=gui_local_in_policy,
            gui_wanopt_cache=gui_wanopt_cache,
            gui_explicit_proxy=gui_explicit_proxy,
            gui_dynamic_routing=gui_dynamic_routing,
            gui_sslvpn_personal_bookmarks=gui_sslvpn_personal_bookmarks,
            gui_sslvpn_realms=gui_sslvpn_realms,
            gui_policy_based_ipsec=gui_policy_based_ipsec,
            gui_threat_weight=gui_threat_weight,
            gui_spamfilter=gui_spamfilter,
            gui_file_filter=gui_file_filter,
            gui_application_control=gui_application_control,
            gui_ips=gui_ips,
            gui_dhcp_advanced=gui_dhcp_advanced,
            gui_vpn=gui_vpn,
            gui_sslvpn=gui_sslvpn,
            gui_wireless_controller=gui_wireless_controller,
            gui_advanced_wireless_features=gui_advanced_wireless_features,
            gui_switch_controller=gui_switch_controller,
            gui_fortiap_split_tunneling=gui_fortiap_split_tunneling,
            gui_webfilter_advanced=gui_webfilter_advanced,
            gui_traffic_shaping=gui_traffic_shaping,
            gui_wan_load_balancing=gui_wan_load_balancing,
            gui_antivirus=gui_antivirus,
            gui_webfilter=gui_webfilter,
            gui_videofilter=gui_videofilter,
            gui_dnsfilter=gui_dnsfilter,
            gui_waf_profile=gui_waf_profile,
            gui_dlp_profile=gui_dlp_profile,
            gui_dlp_advanced=gui_dlp_advanced,
            gui_virtual_patch_profile=gui_virtual_patch_profile,
            gui_casb=gui_casb,
            gui_fortiextender_controller=gui_fortiextender_controller,
            gui_advanced_policy=gui_advanced_policy,
            gui_allow_unnamed_policy=gui_allow_unnamed_policy,
            gui_email_collection=gui_email_collection,
            gui_multiple_interface_policy=gui_multiple_interface_policy,
            gui_policy_disclaimer=gui_policy_disclaimer,
            gui_ztna=gui_ztna,
            gui_ot=gui_ot,
            gui_dynamic_device_os_id=gui_dynamic_device_os_id,
            gui_gtp=gui_gtp,
            location_id=location_id,
            ike_session_resume=ike_session_resume,
            ike_quick_crash_detect=ike_quick_crash_detect,
            ike_dn_format=ike_dn_format,
            ike_port=ike_port,
            ike_tcp_port=ike_tcp_port,
            ike_policy_route=ike_policy_route,
            ike_detailed_event_logs=ike_detailed_event_logs,
            block_land_attack=block_land_attack,
            default_app_port_as_service=default_app_port_as_service,
            fqdn_session_check=fqdn_session_check,
            ext_resource_session_check=ext_resource_session_check,
            dyn_addr_session_check=dyn_addr_session_check,
            default_policy_expiry_days=default_policy_expiry_days,
            gui_enforce_change_summary=gui_enforce_change_summary,
            internet_service_database_cache=internet_service_database_cache,
            internet_service_app_ctrl_size=internet_service_app_ctrl_size,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.settings import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/settings",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/system/settings"

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
        Move system/settings object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_settings.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/settings",
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
        Clone system/settings object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_settings.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/settings",
            params={
                "name": name,
                "new_name": new_name,
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
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/settings object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_settings.exists(name="myobj"):
            ...     fgt.api.cmdb.system_settings.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
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


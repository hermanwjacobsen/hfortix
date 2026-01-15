"""
FortiOS CMDB - System interface

Configuration endpoint for managing cmdb system/interface objects.

API Endpoints:
    GET    /cmdb/system/interface
    POST   /cmdb/system/interface
    PUT    /cmdb/system/interface/{identifier}
    DELETE /cmdb/system/interface/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_interface.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_interface.post(
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

class Interface(CRUDEndpoint, MetadataMixin):
    """Interface Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "interface"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "client_options": {
            "mkey": "id",
            "required_fields": ['id', 'code'],
            "example": "[{'id': 1, 'code': 1}]",
        },
        "fail_alert_interfaces": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "member": {
            "mkey": "interface-name",
            "required_fields": ['interface-name'],
            "example": "[{'interface-name': 'value'}]",
        },
        "security_groups": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "vrrp": {
            "mkey": "vrid",
            "required_fields": ['vrid', 'vrip'],
            "example": "[{'vrid': 1, 'vrip': '192.168.1.10'}]",
        },
        "secondaryip": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "dhcp_snooping_server_list": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
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
        """Initialize Interface endpoint."""
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
        Retrieve system/interface configuration.

        Configure interfaces.

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
            >>> # Get all system/interface objects
            >>> result = fgt.api.cmdb.system_interface.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/interface by name
            >>> result = fgt.api.cmdb.system_interface.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_interface.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_interface.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_interface.get_schema()

        See Also:
            - post(): Create new system/interface object
            - put(): Update existing system/interface object
            - delete(): Remove system/interface object
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
            endpoint = "/system/interface/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/system/interface"
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
            >>> schema = fgt.api.cmdb.system_interface.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_interface.get_schema(format="json-schema")
        
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
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: Literal["enable", "disable"] | None = None,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = None,
        mode: Literal["static", "dhcp", "pppoe"] | None = None,
        client_options: str | list[str] | list[dict[str, Any]] | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = None,
        dhcp_relay_service: Literal["disable", "enable"] | None = None,
        dhcp_relay_ip: str | list[str] | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = None,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = None,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = None,
        dhcp_smart_relay: Literal["disable", "enable"] | None = None,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = None,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = None,
        management_ip: Any | None = None,
        ip: Any | None = None,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = None,
        gwdetect: Literal["enable", "disable"] | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = None,
        ha_priority: int | None = None,
        fail_detect: Literal["enable", "disable"] | None = None,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = None,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = None,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = None,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = None,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        idle_timeout: int | None = None,
        multilink: Literal["enable", "disable"] | None = None,
        mrru: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: Literal["enable", "disable"] | None = None,
        dns_server_override: Literal["enable", "disable"] | None = None,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = None,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_client: Literal["enable", "disable"] | None = None,
        pptp_user: str | None = None,
        pptp_password: Any | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_timeout: int | None = None,
        arpforward: Literal["enable", "disable"] | None = None,
        ndiscforward: Literal["enable", "disable"] | None = None,
        broadcast_forward: Literal["enable", "disable"] | None = None,
        bfd: Literal["global", "enable", "disable"] | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: Literal["enable", "disable"] | None = None,
        icmp_send_redirect: Literal["enable", "disable"] | None = None,
        icmp_accept_redirect: Literal["enable", "disable"] | None = None,
        reachable_time: int | None = None,
        vlanforward: Literal["enable", "disable"] | None = None,
        stpforward: Literal["enable", "disable"] | None = None,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = None,
        ips_sniffer_mode: Literal["enable", "disable"] | None = None,
        ident_accept: Literal["enable", "disable"] | None = None,
        ipmac: Literal["enable", "disable"] | None = None,
        subst: Literal["enable", "disable"] | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = None,
        status: Literal["up", "down"] | None = None,
        netbios_forward: Literal["disable", "enable"] | None = None,
        wins_ip: str | None = None,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = None,
        dedicated_to: Literal["none", "management"] | None = None,
        trust_ip_1: Any | None = None,
        trust_ip_2: Any | None = None,
        trust_ip_3: Any | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        ring_rx: int | None = None,
        ring_tx: int | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: Literal["enable", "disable"] | None = None,
        drop_fragment: Literal["enable", "disable"] | None = None,
        src_check: Literal["enable", "disable"] | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: Literal["tx", "rx", "both"] | None = None,
        explicit_web_proxy: Literal["enable", "disable"] | None = None,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = None,
        proxy_captive_portal: Literal["enable", "disable"] | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: Literal["enable", "disable"] | None = None,
        mtu_override: Literal["enable", "disable"] | None = None,
        mtu: int | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        forward_domain: int | None = None,
        remote_ip: Any | None = None,
        member: str | list[str] | list[dict[str, Any]] | None = None,
        lacp_mode: Literal["static", "passive", "active"] | None = None,
        lacp_ha_secondary: Literal["enable", "disable"] | None = None,
        system_id_type: Literal["auto", "user"] | None = None,
        system_id: str | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = None,
        link_up_delay: int | None = None,
        aggregate_type: Literal["physical", "vxlan"] | None = None,
        priority_override: Literal["enable", "disable"] | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = None,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = None,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: str | list[str] | list[dict[str, Any]] | None = None,
        ike_saml_server: str | None = None,
        device_identification: Literal["enable", "disable"] | None = None,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = None,
        device_user_identification: Literal["enable", "disable"] | None = None,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = None,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: Literal["enable", "disable"] | None = None,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = None,
        vrrp: str | list[str] | list[dict[str, Any]] | None = None,
        phy_setting: str | None = None,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = None,
        snmp_index: int | None = None,
        secondary_IP: Literal["enable", "disable"] | None = None,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = None,
        preserve_session_route: Literal["enable", "disable"] | None = None,
        auto_auth_extension_device: Literal["enable", "disable"] | None = None,
        ap_discover: Literal["enable", "disable"] | None = None,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = None,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = None,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = None,
        fortilink_split_interface: Literal["enable", "disable"] | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = None,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = None,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = None,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = None,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = None,
        switch_controller_offload: Literal["enable", "disable"] | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: str | list[str] | list[dict[str, Any]] | None = None,
        eap_supplicant: Literal["enable", "disable"] | None = None,
        eap_method: Literal["tls", "peap"] | None = None,
        eap_identity: str | None = None,
        eap_password: Any | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        ipv6: str | None = None,
        physical: Any | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/interface object.

        Configure interfaces.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Name.
            vdom: Interface is in this virtual domain (VDOM).
            vrf: Virtual Routing Forwarding ID.
            cli_conn_status: CLI connection status.
            fortilink: Enable FortiLink to dedicate this interface to manage other Fortinet devices.
            switch_controller_source_ip: Source IP address used in FortiLink over L3 connections.
            mode: Addressing mode (static, DHCP, PPPoE).
            client_options: DHCP client options.
                Default format: [{'id': 1, 'code': 1}]
                Required format: List of dicts with keys: id, code
                  (String format not allowed due to multiple required fields)
            distance: Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.
            priority: Priority of learned routes.
            dhcp_relay_interface_select_method: Specify how to select outgoing interface to reach server.
            dhcp_relay_interface: Specify outgoing interface to reach server.
            dhcp_relay_vrf_select: VRF ID used for connection to server.
            dhcp_broadcast_flag: Enable/disable setting of the broadcast flag in messages sent by the DHCP client (default = enable).
            dhcp_relay_service: Enable/disable allowing this interface to act as a DHCP relay.
            dhcp_relay_ip: DHCP relay IP address.
            dhcp_relay_source_ip: IP address used by the DHCP relay as its source IP.
            dhcp_relay_circuit_id: DHCP relay circuit ID.
            dhcp_relay_link_selection: DHCP relay link selection.
            dhcp_relay_request_all_server: Enable/disable sending of DHCP requests to all servers.
            dhcp_relay_allow_no_end_option: Enable/disable relaying DHCP messages with no end option.
            dhcp_relay_type: DHCP relay type (regular or IPsec).
            dhcp_smart_relay: Enable/disable DHCP smart relay.
            dhcp_relay_agent_option: Enable/disable DHCP relay agent option.
            dhcp_classless_route_addition: Enable/disable addition of classless static routes retrieved from DHCP server.
            management_ip: High Availability in-band management IP address of this interface.
            ip: Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.
            allowaccess: Permitted types of management access to this interface.
            gwdetect: Enable/disable detect gateway alive for first.
            ping_serv_status: PING server status.
            detectserver: Gateway's ping server for this IP.
            detectprotocol: Protocols used to detect the server.
            ha_priority: HA election priority for the PING server.
            fail_detect: Enable/disable fail detection features for this interface.
            fail_detect_option: Options for detecting that this interface has failed.
            fail_alert_method: Select link-failed-signal or link-down method to alert about a failed link.
            fail_action_on_extender: Action on FortiExtender when interface fail.
            fail_alert_interfaces: Names of the FortiGate interfaces to which the link failure alert is sent.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dhcp_client_identifier: DHCP client identifier.
            dhcp_renew_time: DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server.
            ipunnumbered: Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.
            username: Username of the PPPoE account, provided by your ISP.
            pppoe_egress_cos: CoS in VLAN tag for outgoing PPPoE/PPP packets.
            pppoe_unnumbered_negotiate: Enable/disable PPPoE unnumbered negotiation.
            password: PPPoE account's password.
            idle_timeout: PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.
            multilink: Enable/disable PPP multilink support.
            mrru: PPP MRRU (296 - 65535, default = 1500).
            detected_peer_mtu: MTU of detected peer (0 - 4294967295).
            disc_retry_timeout: Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout.
            padt_retry_timeout: PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time.
            service_name: PPPoE service name.
            ac_name: PPPoE server name.
            lcp_echo_interval: Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.
            lcp_max_echo_fails: Maximum missed LCP echo messages before disconnect.
            defaultgw: Enable to get the gateway IP from the DHCP or PPPoE server.
            dns_server_override: Enable/disable use DNS acquired by DHCP or PPPoE.
            dns_server_protocol: DNS transport protocols.
            auth_type: PPP authentication type to use.
            pptp_client: Enable/disable PPTP client.
            pptp_user: PPTP user name.
            pptp_password: PPTP password.
            pptp_server_ip: PPTP server IP address.
            pptp_auth_type: PPTP authentication type.
            pptp_timeout: Idle timer in minutes (0 for disabled).
            arpforward: Enable/disable ARP forwarding.
            ndiscforward: Enable/disable NDISC forwarding.
            broadcast_forward: Enable/disable broadcast forwarding.
            bfd: Bidirectional Forwarding Detection (BFD) settings.
            bfd_desired_min_tx: BFD desired minimal transmit interval.
            bfd_detect_mult: BFD detection multiplier.
            bfd_required_min_rx: BFD required minimal receive interval.
            l2forward: Enable/disable l2 forwarding.
            icmp_send_redirect: Enable/disable sending of ICMP redirects.
            icmp_accept_redirect: Enable/disable ICMP accept redirect.
            reachable_time: IPv4 reachable time in milliseconds (30000 - 3600000, default = 30000).
            vlanforward: Enable/disable traffic forwarding between VLANs on this interface.
            stpforward: Enable/disable STP forwarding.
            stpforward_mode: Configure STP forwarding mode.
            ips_sniffer_mode: Enable/disable the use of this interface as a one-armed sniffer.
            ident_accept: Enable/disable authentication for this interface.
            ipmac: Enable/disable IP/MAC binding.
            subst: Enable to always send packets from this interface to a destination MAC address.
            macaddr: Change the interface's MAC address.
            virtual_mac: Change the interface's virtual MAC address.
            substitute_dst_mac: Destination MAC address that all packets are sent to from this interface.
            speed: Interface speed. The default setting and the options available depend on the interface hardware.
            status: Bring the interface up or shut the interface down.
            netbios_forward: Enable/disable NETBIOS forwarding.
            wins_ip: WINS server IP.
            type: Interface type.
            dedicated_to: Configure interface for single purpose.
            trust_ip_1: Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip_2: Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip_3: Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip6_1: Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
            trust_ip6_2: Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
            trust_ip6_3: Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
            ring_rx: RX ring size.
            ring_tx: TX ring size.
            wccp: Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.
            netflow_sampler: Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).
            netflow_sample_rate: NetFlow sample rate.  Sample one packet every configured number of packets
(1 - 65535, default = 1, which means standard NetFlow where all packets are sampled).
            netflow_sampler_id: Netflow sampler ID.
            sflow_sampler: Enable/disable sFlow on this interface.
            drop_fragment: Enable/disable drop fragment packets.
            src_check: Enable/disable source IP check.
            sample_rate: sFlow sample rate (10 - 99999).
            polling_interval: sFlow polling interval in seconds (1 - 255).
            sample_direction: Data that NetFlow collects (rx, tx, or both).
            explicit_web_proxy: Enable/disable the explicit web proxy on this interface.
            explicit_ftp_proxy: Enable/disable the explicit FTP proxy on this interface.
            proxy_captive_portal: Enable/disable proxy captive portal on this interface.
            tcp_mss: TCP maximum segment size. 0 means do not change segment size.
            inbandwidth: Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 means unlimited.
            outbandwidth: Bandwidth limit for outgoing traffic (0 - 80000000 kbps).
            egress_shaping_profile: Outgoing traffic shaping profile.
            ingress_shaping_profile: Incoming traffic shaping profile.
            spillover_threshold: Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
            ingress_spillover_threshold: Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
            weight: Default weight for static routes (if route has no weight configured).
            interface: Interface name.
            external: Enable/disable identifying the interface as an external interface (which usually means it's connected to the Internet).
            mtu_override: Enable to set a custom MTU for this interface.
            mtu: MTU value for this interface.
            vlan_protocol: Ethernet protocol of VLAN.
            vlanid: VLAN ID (1 - 4094).
            forward_domain: Transparent mode forward domain.
            remote_ip: Remote IP address of tunnel.
            member: Physical interfaces that belong to the aggregate or redundant interface.
                Default format: [{'interface-name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'interface-name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'interface-name': 'val1'}, ...]
                  - List of dicts: [{'interface-name': 'value'}] (recommended)
            lacp_mode: LACP mode.
            lacp_ha_secondary: LACP HA secondary member.
            system_id_type: Method in which system ID is generated.
            system_id: Define a system ID for the aggregate interface.
            lacp_speed: How often the interface sends LACP messages.
            min_links: Minimum number of aggregated ports that must be up.
            min_links_down: Action to take when less than the configured minimum number of links are active.
            algorithm: Frame distribution algorithm.
            link_up_delay: Number of milliseconds to wait before considering a link is up.
            aggregate_type: Type of aggregation.
            priority_override: Enable/disable fail back to higher priority port once recovered.
            aggregate: Aggregate interface.
            redundant_interface: Redundant interface.
            devindex: Device Index.
            vindex: Switch control interface VLAN ID.
            switch: Contained in switch.
            description: Description.
            alias: Alias will be displayed with the interface name to make it easier to distinguish.
            security_mode: Turn on captive portal authentication for this interface.
            security_mac_auth_bypass: Enable/disable MAC authentication bypass.
            security_ip_auth_bypass: Enable/disable IP authentication bypass.
            security_external_web: URL of external authentication web server.
            security_external_logout: URL of external authentication logout server.
            replacemsg_override_group: Replacement message override group.
            security_redirect_url: URL redirection after disclaimer/authentication.
            auth_cert: HTTPS server certificate.
            auth_portal_addr: Address of captive portal.
            security_exempt_list: Name of security-exempt-list.
            security_groups: User groups that can authenticate with the captive portal.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ike_saml_server: Configure IKE authentication SAML server.
            device_identification: Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.
            exclude_signatures: Exclude IOT or OT application signatures.
            device_user_identification: Enable/disable passive gathering of user identity information about users on this interface.
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP) reception.
            lldp_transmission: Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
            lldp_network_policy: LLDP-MED network policy profile.
            estimated_upstream_bandwidth: Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.
            estimated_downstream_bandwidth: Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.
            measured_upstream_bandwidth: Measured upstream bandwidth (kbps).
            measured_downstream_bandwidth: Measured downstream bandwidth (kbps).
            bandwidth_measure_time: Bandwidth measure time.
            monitor_bandwidth: Enable monitoring bandwidth on this interface.
            vrrp_virtual_mac: Enable/disable use of virtual MAC for VRRP.
            vrrp: VRRP configuration.
                Default format: [{'vrid': 1, 'vrip': '192.168.1.10'}]
                Required format: List of dicts with keys: vrid, vrip
                  (String format not allowed due to multiple required fields)
            phy_setting: PHY settings
            role: Interface role.
            snmp_index: Permanent SNMP Index of the interface.
            secondary_IP: Enable/disable adding a secondary IP to this interface.
            secondaryip: Second IP address of interface.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            preserve_session_route: Enable/disable preservation of session route when dirty.
            auto_auth_extension_device: Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.
            ap_discover: Enable/disable automatic registration of unknown FortiAP devices.
            fortilink_neighbor_detect: Protocol for FortiGate neighbor discovery.
            ip_managed_by_fortiipam: Enable/disable automatic IP address assignment of this interface by FortiIPAM.
            managed_subnetwork_size: Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate unit's DHCP server settings.
            fortilink_split_interface: Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.
            internal: Implicitly created.
            fortilink_backup_link: FortiLink split interface backup link.
            switch_controller_access_vlan: Block FortiSwitch port-to-port traffic.
            switch_controller_traffic_policy: Switch controller traffic policy for the VLAN.
            switch_controller_rspan_mode: Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.
            switch_controller_netflow_collect: NetFlow collection and processing.
            switch_controller_mgmt_vlan: VLAN to use for FortiLink management purposes.
            switch_controller_igmp_snooping: Switch controller IGMP snooping.
            switch_controller_igmp_snooping_proxy: Switch controller IGMP snooping proxy.
            switch_controller_igmp_snooping_fast_leave: Switch controller IGMP snooping fast-leave.
            switch_controller_dhcp_snooping: Switch controller DHCP snooping.
            switch_controller_dhcp_snooping_verify_mac: Switch controller DHCP snooping verify MAC.
            switch_controller_dhcp_snooping_option82: Switch controller DHCP snooping option82.
            dhcp_snooping_server_list: Configure DHCP server access list.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            switch_controller_arp_inspection: Enable/disable/Monitor FortiSwitch ARP inspection.
            switch_controller_learning_limit: Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default).
            switch_controller_nac: Integrated FortiLink settings for managed FortiSwitch.
            switch_controller_dynamic: Integrated FortiLink settings for managed FortiSwitch.
            switch_controller_feature: Interface's purpose when assigning traffic (read only).
            switch_controller_iot_scanning: Enable/disable managed FortiSwitch IoT scanning.
            switch_controller_offload: Enable/disable managed FortiSwitch routing offload.
            switch_controller_offload_ip: IP for routing offload on FortiSwitch.
            switch_controller_offload_gw: Enable/disable managed FortiSwitch routing offload gateway.
            swc_vlan: Creation status for switch-controller VLANs.
            swc_first_create: Initial create for switch-controller VLANs.
            color: Color of icon on the GUI.
            tagging: Config object tagging.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            eap_supplicant: Enable/disable EAP-Supplicant.
            eap_method: EAP method.
            eap_identity: EAP identity.
            eap_password: EAP password.
            eap_ca_cert: EAP CA certificate name.
            eap_user_cert: EAP user certificate name.
            default_purdue_level: default purdue level of device detected on this interface.
            ipv6: IPv6 of interface.
            physical: Print physical interface information.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_interface.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_interface.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if client_options is not None:
            client_options = normalize_table_field(
                client_options,
                mkey="id",
                required_fields=['id', 'code'],
                field_name="client_options",
                example="[{'id': 1, 'code': 1}]",
            )
        if fail_alert_interfaces is not None:
            fail_alert_interfaces = normalize_table_field(
                fail_alert_interfaces,
                mkey="name",
                required_fields=['name'],
                field_name="fail_alert_interfaces",
                example="[{'name': 'value'}]",
            )
        if member is not None:
            member = normalize_table_field(
                member,
                mkey="interface-name",
                required_fields=['interface-name'],
                field_name="member",
                example="[{'interface-name': 'value'}]",
            )
        if security_groups is not None:
            security_groups = normalize_table_field(
                security_groups,
                mkey="name",
                required_fields=['name'],
                field_name="security_groups",
                example="[{'name': 'value'}]",
            )
        if vrrp is not None:
            vrrp = normalize_table_field(
                vrrp,
                mkey="vrid",
                required_fields=['vrid', 'vrip'],
                field_name="vrrp",
                example="[{'vrid': 1, 'vrip': '192.168.1.10'}]",
            )
        if secondaryip is not None:
            secondaryip = normalize_table_field(
                secondaryip,
                mkey="id",
                required_fields=['id'],
                field_name="secondaryip",
                example="[{'id': 1}]",
            )
        if dhcp_snooping_server_list is not None:
            dhcp_snooping_server_list = normalize_table_field(
                dhcp_snooping_server_list,
                mkey="name",
                required_fields=['name'],
                field_name="dhcp_snooping_server_list",
                example="[{'name': 'value'}]",
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
            vrf=vrf,
            cli_conn_status=cli_conn_status,
            fortilink=fortilink,
            switch_controller_source_ip=switch_controller_source_ip,
            mode=mode,
            client_options=client_options,
            distance=distance,
            priority=priority,
            dhcp_relay_interface_select_method=dhcp_relay_interface_select_method,
            dhcp_relay_interface=dhcp_relay_interface,
            dhcp_relay_vrf_select=dhcp_relay_vrf_select,
            dhcp_broadcast_flag=dhcp_broadcast_flag,
            dhcp_relay_service=dhcp_relay_service,
            dhcp_relay_ip=dhcp_relay_ip,
            dhcp_relay_source_ip=dhcp_relay_source_ip,
            dhcp_relay_circuit_id=dhcp_relay_circuit_id,
            dhcp_relay_link_selection=dhcp_relay_link_selection,
            dhcp_relay_request_all_server=dhcp_relay_request_all_server,
            dhcp_relay_allow_no_end_option=dhcp_relay_allow_no_end_option,
            dhcp_relay_type=dhcp_relay_type,
            dhcp_smart_relay=dhcp_smart_relay,
            dhcp_relay_agent_option=dhcp_relay_agent_option,
            dhcp_classless_route_addition=dhcp_classless_route_addition,
            management_ip=management_ip,
            ip=ip,
            allowaccess=allowaccess,
            gwdetect=gwdetect,
            ping_serv_status=ping_serv_status,
            detectserver=detectserver,
            detectprotocol=detectprotocol,
            ha_priority=ha_priority,
            fail_detect=fail_detect,
            fail_detect_option=fail_detect_option,
            fail_alert_method=fail_alert_method,
            fail_action_on_extender=fail_action_on_extender,
            fail_alert_interfaces=fail_alert_interfaces,
            dhcp_client_identifier=dhcp_client_identifier,
            dhcp_renew_time=dhcp_renew_time,
            ipunnumbered=ipunnumbered,
            username=username,
            pppoe_egress_cos=pppoe_egress_cos,
            pppoe_unnumbered_negotiate=pppoe_unnumbered_negotiate,
            password=password,
            idle_timeout=idle_timeout,
            multilink=multilink,
            mrru=mrru,
            detected_peer_mtu=detected_peer_mtu,
            disc_retry_timeout=disc_retry_timeout,
            padt_retry_timeout=padt_retry_timeout,
            service_name=service_name,
            ac_name=ac_name,
            lcp_echo_interval=lcp_echo_interval,
            lcp_max_echo_fails=lcp_max_echo_fails,
            defaultgw=defaultgw,
            dns_server_override=dns_server_override,
            dns_server_protocol=dns_server_protocol,
            auth_type=auth_type,
            pptp_client=pptp_client,
            pptp_user=pptp_user,
            pptp_password=pptp_password,
            pptp_server_ip=pptp_server_ip,
            pptp_auth_type=pptp_auth_type,
            pptp_timeout=pptp_timeout,
            arpforward=arpforward,
            ndiscforward=ndiscforward,
            broadcast_forward=broadcast_forward,
            bfd=bfd,
            bfd_desired_min_tx=bfd_desired_min_tx,
            bfd_detect_mult=bfd_detect_mult,
            bfd_required_min_rx=bfd_required_min_rx,
            l2forward=l2forward,
            icmp_send_redirect=icmp_send_redirect,
            icmp_accept_redirect=icmp_accept_redirect,
            reachable_time=reachable_time,
            vlanforward=vlanforward,
            stpforward=stpforward,
            stpforward_mode=stpforward_mode,
            ips_sniffer_mode=ips_sniffer_mode,
            ident_accept=ident_accept,
            ipmac=ipmac,
            subst=subst,
            macaddr=macaddr,
            virtual_mac=virtual_mac,
            substitute_dst_mac=substitute_dst_mac,
            speed=speed,
            status=status,
            netbios_forward=netbios_forward,
            wins_ip=wins_ip,
            type=type,
            dedicated_to=dedicated_to,
            trust_ip_1=trust_ip_1,
            trust_ip_2=trust_ip_2,
            trust_ip_3=trust_ip_3,
            trust_ip6_1=trust_ip6_1,
            trust_ip6_2=trust_ip6_2,
            trust_ip6_3=trust_ip6_3,
            ring_rx=ring_rx,
            ring_tx=ring_tx,
            wccp=wccp,
            netflow_sampler=netflow_sampler,
            netflow_sample_rate=netflow_sample_rate,
            netflow_sampler_id=netflow_sampler_id,
            sflow_sampler=sflow_sampler,
            drop_fragment=drop_fragment,
            src_check=src_check,
            sample_rate=sample_rate,
            polling_interval=polling_interval,
            sample_direction=sample_direction,
            explicit_web_proxy=explicit_web_proxy,
            explicit_ftp_proxy=explicit_ftp_proxy,
            proxy_captive_portal=proxy_captive_portal,
            tcp_mss=tcp_mss,
            inbandwidth=inbandwidth,
            outbandwidth=outbandwidth,
            egress_shaping_profile=egress_shaping_profile,
            ingress_shaping_profile=ingress_shaping_profile,
            spillover_threshold=spillover_threshold,
            ingress_spillover_threshold=ingress_spillover_threshold,
            weight=weight,
            interface=interface,
            external=external,
            mtu_override=mtu_override,
            mtu=mtu,
            vlan_protocol=vlan_protocol,
            vlanid=vlanid,
            forward_domain=forward_domain,
            remote_ip=remote_ip,
            member=member,
            lacp_mode=lacp_mode,
            lacp_ha_secondary=lacp_ha_secondary,
            system_id_type=system_id_type,
            system_id=system_id,
            lacp_speed=lacp_speed,
            min_links=min_links,
            min_links_down=min_links_down,
            algorithm=algorithm,
            link_up_delay=link_up_delay,
            aggregate_type=aggregate_type,
            priority_override=priority_override,
            aggregate=aggregate,
            redundant_interface=redundant_interface,
            devindex=devindex,
            vindex=vindex,
            switch=switch,
            description=description,
            alias=alias,
            security_mode=security_mode,
            security_mac_auth_bypass=security_mac_auth_bypass,
            security_ip_auth_bypass=security_ip_auth_bypass,
            security_external_web=security_external_web,
            security_external_logout=security_external_logout,
            replacemsg_override_group=replacemsg_override_group,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            security_exempt_list=security_exempt_list,
            security_groups=security_groups,
            ike_saml_server=ike_saml_server,
            device_identification=device_identification,
            exclude_signatures=exclude_signatures,
            device_user_identification=device_user_identification,
            lldp_reception=lldp_reception,
            lldp_transmission=lldp_transmission,
            lldp_network_policy=lldp_network_policy,
            estimated_upstream_bandwidth=estimated_upstream_bandwidth,
            estimated_downstream_bandwidth=estimated_downstream_bandwidth,
            measured_upstream_bandwidth=measured_upstream_bandwidth,
            measured_downstream_bandwidth=measured_downstream_bandwidth,
            bandwidth_measure_time=bandwidth_measure_time,
            monitor_bandwidth=monitor_bandwidth,
            vrrp_virtual_mac=vrrp_virtual_mac,
            vrrp=vrrp,
            phy_setting=phy_setting,
            role=role,
            snmp_index=snmp_index,
            secondary_IP=secondary_IP,
            secondaryip=secondaryip,
            preserve_session_route=preserve_session_route,
            auto_auth_extension_device=auto_auth_extension_device,
            ap_discover=ap_discover,
            fortilink_neighbor_detect=fortilink_neighbor_detect,
            ip_managed_by_fortiipam=ip_managed_by_fortiipam,
            managed_subnetwork_size=managed_subnetwork_size,
            fortilink_split_interface=fortilink_split_interface,
            internal=internal,
            fortilink_backup_link=fortilink_backup_link,
            switch_controller_access_vlan=switch_controller_access_vlan,
            switch_controller_traffic_policy=switch_controller_traffic_policy,
            switch_controller_rspan_mode=switch_controller_rspan_mode,
            switch_controller_netflow_collect=switch_controller_netflow_collect,
            switch_controller_mgmt_vlan=switch_controller_mgmt_vlan,
            switch_controller_igmp_snooping=switch_controller_igmp_snooping,
            switch_controller_igmp_snooping_proxy=switch_controller_igmp_snooping_proxy,
            switch_controller_igmp_snooping_fast_leave=switch_controller_igmp_snooping_fast_leave,
            switch_controller_dhcp_snooping=switch_controller_dhcp_snooping,
            switch_controller_dhcp_snooping_verify_mac=switch_controller_dhcp_snooping_verify_mac,
            switch_controller_dhcp_snooping_option82=switch_controller_dhcp_snooping_option82,
            dhcp_snooping_server_list=dhcp_snooping_server_list,
            switch_controller_arp_inspection=switch_controller_arp_inspection,
            switch_controller_learning_limit=switch_controller_learning_limit,
            switch_controller_nac=switch_controller_nac,
            switch_controller_dynamic=switch_controller_dynamic,
            switch_controller_feature=switch_controller_feature,
            switch_controller_iot_scanning=switch_controller_iot_scanning,
            switch_controller_offload=switch_controller_offload,
            switch_controller_offload_ip=switch_controller_offload_ip,
            switch_controller_offload_gw=switch_controller_offload_gw,
            swc_vlan=swc_vlan,
            swc_first_create=swc_first_create,
            color=color,
            tagging=tagging,
            eap_supplicant=eap_supplicant,
            eap_method=eap_method,
            eap_identity=eap_identity,
            eap_password=eap_password,
            eap_ca_cert=eap_ca_cert,
            eap_user_cert=eap_user_cert,
            default_purdue_level=default_purdue_level,
            ipv6=ipv6,
            physical=physical,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/interface",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/interface/" + str(name_value)

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
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: Literal["enable", "disable"] | None = None,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = None,
        mode: Literal["static", "dhcp", "pppoe"] | None = None,
        client_options: str | list[str] | list[dict[str, Any]] | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = None,
        dhcp_relay_service: Literal["disable", "enable"] | None = None,
        dhcp_relay_ip: str | list[str] | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = None,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = None,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = None,
        dhcp_smart_relay: Literal["disable", "enable"] | None = None,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = None,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = None,
        management_ip: Any | None = None,
        ip: Any | None = None,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = None,
        gwdetect: Literal["enable", "disable"] | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = None,
        ha_priority: int | None = None,
        fail_detect: Literal["enable", "disable"] | None = None,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = None,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = None,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = None,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = None,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        idle_timeout: int | None = None,
        multilink: Literal["enable", "disable"] | None = None,
        mrru: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: Literal["enable", "disable"] | None = None,
        dns_server_override: Literal["enable", "disable"] | None = None,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = None,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_client: Literal["enable", "disable"] | None = None,
        pptp_user: str | None = None,
        pptp_password: Any | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_timeout: int | None = None,
        arpforward: Literal["enable", "disable"] | None = None,
        ndiscforward: Literal["enable", "disable"] | None = None,
        broadcast_forward: Literal["enable", "disable"] | None = None,
        bfd: Literal["global", "enable", "disable"] | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: Literal["enable", "disable"] | None = None,
        icmp_send_redirect: Literal["enable", "disable"] | None = None,
        icmp_accept_redirect: Literal["enable", "disable"] | None = None,
        reachable_time: int | None = None,
        vlanforward: Literal["enable", "disable"] | None = None,
        stpforward: Literal["enable", "disable"] | None = None,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = None,
        ips_sniffer_mode: Literal["enable", "disable"] | None = None,
        ident_accept: Literal["enable", "disable"] | None = None,
        ipmac: Literal["enable", "disable"] | None = None,
        subst: Literal["enable", "disable"] | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = None,
        status: Literal["up", "down"] | None = None,
        netbios_forward: Literal["disable", "enable"] | None = None,
        wins_ip: str | None = None,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = None,
        dedicated_to: Literal["none", "management"] | None = None,
        trust_ip_1: Any | None = None,
        trust_ip_2: Any | None = None,
        trust_ip_3: Any | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        ring_rx: int | None = None,
        ring_tx: int | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: Literal["enable", "disable"] | None = None,
        drop_fragment: Literal["enable", "disable"] | None = None,
        src_check: Literal["enable", "disable"] | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: Literal["tx", "rx", "both"] | None = None,
        explicit_web_proxy: Literal["enable", "disable"] | None = None,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = None,
        proxy_captive_portal: Literal["enable", "disable"] | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: Literal["enable", "disable"] | None = None,
        mtu_override: Literal["enable", "disable"] | None = None,
        mtu: int | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        forward_domain: int | None = None,
        remote_ip: Any | None = None,
        member: str | list[str] | list[dict[str, Any]] | None = None,
        lacp_mode: Literal["static", "passive", "active"] | None = None,
        lacp_ha_secondary: Literal["enable", "disable"] | None = None,
        system_id_type: Literal["auto", "user"] | None = None,
        system_id: str | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = None,
        link_up_delay: int | None = None,
        aggregate_type: Literal["physical", "vxlan"] | None = None,
        priority_override: Literal["enable", "disable"] | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = None,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = None,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: str | list[str] | list[dict[str, Any]] | None = None,
        ike_saml_server: str | None = None,
        device_identification: Literal["enable", "disable"] | None = None,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = None,
        device_user_identification: Literal["enable", "disable"] | None = None,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = None,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: Literal["enable", "disable"] | None = None,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = None,
        vrrp: str | list[str] | list[dict[str, Any]] | None = None,
        phy_setting: str | None = None,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = None,
        snmp_index: int | None = None,
        secondary_IP: Literal["enable", "disable"] | None = None,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = None,
        preserve_session_route: Literal["enable", "disable"] | None = None,
        auto_auth_extension_device: Literal["enable", "disable"] | None = None,
        ap_discover: Literal["enable", "disable"] | None = None,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = None,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = None,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = None,
        fortilink_split_interface: Literal["enable", "disable"] | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = None,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = None,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = None,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = None,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = None,
        switch_controller_offload: Literal["enable", "disable"] | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: str | list[str] | list[dict[str, Any]] | None = None,
        eap_supplicant: Literal["enable", "disable"] | None = None,
        eap_method: Literal["tls", "peap"] | None = None,
        eap_identity: str | None = None,
        eap_password: Any | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        ipv6: str | None = None,
        physical: Any | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/interface object.

        Configure interfaces.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Name.
            vdom: Interface is in this virtual domain (VDOM).
            vrf: Virtual Routing Forwarding ID.
            cli_conn_status: CLI connection status.
            fortilink: Enable FortiLink to dedicate this interface to manage other Fortinet devices.
            switch_controller_source_ip: Source IP address used in FortiLink over L3 connections.
            mode: Addressing mode (static, DHCP, PPPoE).
            client_options: DHCP client options.
                Default format: [{'id': 1, 'code': 1}]
                Required format: List of dicts with keys: id, code
                  (String format not allowed due to multiple required fields)
            distance: Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.
            priority: Priority of learned routes.
            dhcp_relay_interface_select_method: Specify how to select outgoing interface to reach server.
            dhcp_relay_interface: Specify outgoing interface to reach server.
            dhcp_relay_vrf_select: VRF ID used for connection to server.
            dhcp_broadcast_flag: Enable/disable setting of the broadcast flag in messages sent by the DHCP client (default = enable).
            dhcp_relay_service: Enable/disable allowing this interface to act as a DHCP relay.
            dhcp_relay_ip: DHCP relay IP address.
            dhcp_relay_source_ip: IP address used by the DHCP relay as its source IP.
            dhcp_relay_circuit_id: DHCP relay circuit ID.
            dhcp_relay_link_selection: DHCP relay link selection.
            dhcp_relay_request_all_server: Enable/disable sending of DHCP requests to all servers.
            dhcp_relay_allow_no_end_option: Enable/disable relaying DHCP messages with no end option.
            dhcp_relay_type: DHCP relay type (regular or IPsec).
            dhcp_smart_relay: Enable/disable DHCP smart relay.
            dhcp_relay_agent_option: Enable/disable DHCP relay agent option.
            dhcp_classless_route_addition: Enable/disable addition of classless static routes retrieved from DHCP server.
            management_ip: High Availability in-band management IP address of this interface.
            ip: Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.
            allowaccess: Permitted types of management access to this interface.
            gwdetect: Enable/disable detect gateway alive for first.
            ping_serv_status: PING server status.
            detectserver: Gateway's ping server for this IP.
            detectprotocol: Protocols used to detect the server.
            ha_priority: HA election priority for the PING server.
            fail_detect: Enable/disable fail detection features for this interface.
            fail_detect_option: Options for detecting that this interface has failed.
            fail_alert_method: Select link-failed-signal or link-down method to alert about a failed link.
            fail_action_on_extender: Action on FortiExtender when interface fail.
            fail_alert_interfaces: Names of the FortiGate interfaces to which the link failure alert is sent.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dhcp_client_identifier: DHCP client identifier.
            dhcp_renew_time: DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server.
            ipunnumbered: Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.
            username: Username of the PPPoE account, provided by your ISP.
            pppoe_egress_cos: CoS in VLAN tag for outgoing PPPoE/PPP packets.
            pppoe_unnumbered_negotiate: Enable/disable PPPoE unnumbered negotiation.
            password: PPPoE account's password.
            idle_timeout: PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.
            multilink: Enable/disable PPP multilink support.
            mrru: PPP MRRU (296 - 65535, default = 1500).
            detected_peer_mtu: MTU of detected peer (0 - 4294967295).
            disc_retry_timeout: Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout.
            padt_retry_timeout: PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time.
            service_name: PPPoE service name.
            ac_name: PPPoE server name.
            lcp_echo_interval: Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.
            lcp_max_echo_fails: Maximum missed LCP echo messages before disconnect.
            defaultgw: Enable to get the gateway IP from the DHCP or PPPoE server.
            dns_server_override: Enable/disable use DNS acquired by DHCP or PPPoE.
            dns_server_protocol: DNS transport protocols.
            auth_type: PPP authentication type to use.
            pptp_client: Enable/disable PPTP client.
            pptp_user: PPTP user name.
            pptp_password: PPTP password.
            pptp_server_ip: PPTP server IP address.
            pptp_auth_type: PPTP authentication type.
            pptp_timeout: Idle timer in minutes (0 for disabled).
            arpforward: Enable/disable ARP forwarding.
            ndiscforward: Enable/disable NDISC forwarding.
            broadcast_forward: Enable/disable broadcast forwarding.
            bfd: Bidirectional Forwarding Detection (BFD) settings.
            bfd_desired_min_tx: BFD desired minimal transmit interval.
            bfd_detect_mult: BFD detection multiplier.
            bfd_required_min_rx: BFD required minimal receive interval.
            l2forward: Enable/disable l2 forwarding.
            icmp_send_redirect: Enable/disable sending of ICMP redirects.
            icmp_accept_redirect: Enable/disable ICMP accept redirect.
            reachable_time: IPv4 reachable time in milliseconds (30000 - 3600000, default = 30000).
            vlanforward: Enable/disable traffic forwarding between VLANs on this interface.
            stpforward: Enable/disable STP forwarding.
            stpforward_mode: Configure STP forwarding mode.
            ips_sniffer_mode: Enable/disable the use of this interface as a one-armed sniffer.
            ident_accept: Enable/disable authentication for this interface.
            ipmac: Enable/disable IP/MAC binding.
            subst: Enable to always send packets from this interface to a destination MAC address.
            macaddr: Change the interface's MAC address.
            virtual_mac: Change the interface's virtual MAC address.
            substitute_dst_mac: Destination MAC address that all packets are sent to from this interface.
            speed: Interface speed. The default setting and the options available depend on the interface hardware.
            status: Bring the interface up or shut the interface down.
            netbios_forward: Enable/disable NETBIOS forwarding.
            wins_ip: WINS server IP.
            type: Interface type.
            dedicated_to: Configure interface for single purpose.
            trust_ip_1: Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip_2: Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip_3: Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip6_1: Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
            trust_ip6_2: Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
            trust_ip6_3: Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).
            ring_rx: RX ring size.
            ring_tx: TX ring size.
            wccp: Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.
            netflow_sampler: Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).
            netflow_sample_rate: NetFlow sample rate.  Sample one packet every configured number of packets
(1 - 65535, default = 1, which means standard NetFlow where all packets are sampled).
            netflow_sampler_id: Netflow sampler ID.
            sflow_sampler: Enable/disable sFlow on this interface.
            drop_fragment: Enable/disable drop fragment packets.
            src_check: Enable/disable source IP check.
            sample_rate: sFlow sample rate (10 - 99999).
            polling_interval: sFlow polling interval in seconds (1 - 255).
            sample_direction: Data that NetFlow collects (rx, tx, or both).
            explicit_web_proxy: Enable/disable the explicit web proxy on this interface.
            explicit_ftp_proxy: Enable/disable the explicit FTP proxy on this interface.
            proxy_captive_portal: Enable/disable proxy captive portal on this interface.
            tcp_mss: TCP maximum segment size. 0 means do not change segment size.
            inbandwidth: Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 means unlimited.
            outbandwidth: Bandwidth limit for outgoing traffic (0 - 80000000 kbps).
            egress_shaping_profile: Outgoing traffic shaping profile.
            ingress_shaping_profile: Incoming traffic shaping profile.
            spillover_threshold: Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
            ingress_spillover_threshold: Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
            weight: Default weight for static routes (if route has no weight configured).
            interface: Interface name.
            external: Enable/disable identifying the interface as an external interface (which usually means it's connected to the Internet).
            mtu_override: Enable to set a custom MTU for this interface.
            mtu: MTU value for this interface.
            vlan_protocol: Ethernet protocol of VLAN.
            vlanid: VLAN ID (1 - 4094).
            forward_domain: Transparent mode forward domain.
            remote_ip: Remote IP address of tunnel.
            member: Physical interfaces that belong to the aggregate or redundant interface.
                Default format: [{'interface-name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'interface-name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'interface-name': 'val1'}, ...]
                  - List of dicts: [{'interface-name': 'value'}] (recommended)
            lacp_mode: LACP mode.
            lacp_ha_secondary: LACP HA secondary member.
            system_id_type: Method in which system ID is generated.
            system_id: Define a system ID for the aggregate interface.
            lacp_speed: How often the interface sends LACP messages.
            min_links: Minimum number of aggregated ports that must be up.
            min_links_down: Action to take when less than the configured minimum number of links are active.
            algorithm: Frame distribution algorithm.
            link_up_delay: Number of milliseconds to wait before considering a link is up.
            aggregate_type: Type of aggregation.
            priority_override: Enable/disable fail back to higher priority port once recovered.
            aggregate: Aggregate interface.
            redundant_interface: Redundant interface.
            devindex: Device Index.
            vindex: Switch control interface VLAN ID.
            switch: Contained in switch.
            description: Description.
            alias: Alias will be displayed with the interface name to make it easier to distinguish.
            security_mode: Turn on captive portal authentication for this interface.
            security_mac_auth_bypass: Enable/disable MAC authentication bypass.
            security_ip_auth_bypass: Enable/disable IP authentication bypass.
            security_external_web: URL of external authentication web server.
            security_external_logout: URL of external authentication logout server.
            replacemsg_override_group: Replacement message override group.
            security_redirect_url: URL redirection after disclaimer/authentication.
            auth_cert: HTTPS server certificate.
            auth_portal_addr: Address of captive portal.
            security_exempt_list: Name of security-exempt-list.
            security_groups: User groups that can authenticate with the captive portal.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ike_saml_server: Configure IKE authentication SAML server.
            device_identification: Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.
            exclude_signatures: Exclude IOT or OT application signatures.
            device_user_identification: Enable/disable passive gathering of user identity information about users on this interface.
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP) reception.
            lldp_transmission: Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
            lldp_network_policy: LLDP-MED network policy profile.
            estimated_upstream_bandwidth: Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.
            estimated_downstream_bandwidth: Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.
            measured_upstream_bandwidth: Measured upstream bandwidth (kbps).
            measured_downstream_bandwidth: Measured downstream bandwidth (kbps).
            bandwidth_measure_time: Bandwidth measure time.
            monitor_bandwidth: Enable monitoring bandwidth on this interface.
            vrrp_virtual_mac: Enable/disable use of virtual MAC for VRRP.
            vrrp: VRRP configuration.
                Default format: [{'vrid': 1, 'vrip': '192.168.1.10'}]
                Required format: List of dicts with keys: vrid, vrip
                  (String format not allowed due to multiple required fields)
            phy_setting: PHY settings
            role: Interface role.
            snmp_index: Permanent SNMP Index of the interface.
            secondary_IP: Enable/disable adding a secondary IP to this interface.
            secondaryip: Second IP address of interface.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            preserve_session_route: Enable/disable preservation of session route when dirty.
            auto_auth_extension_device: Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.
            ap_discover: Enable/disable automatic registration of unknown FortiAP devices.
            fortilink_neighbor_detect: Protocol for FortiGate neighbor discovery.
            ip_managed_by_fortiipam: Enable/disable automatic IP address assignment of this interface by FortiIPAM.
            managed_subnetwork_size: Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate unit's DHCP server settings.
            fortilink_split_interface: Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.
            internal: Implicitly created.
            fortilink_backup_link: FortiLink split interface backup link.
            switch_controller_access_vlan: Block FortiSwitch port-to-port traffic.
            switch_controller_traffic_policy: Switch controller traffic policy for the VLAN.
            switch_controller_rspan_mode: Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.
            switch_controller_netflow_collect: NetFlow collection and processing.
            switch_controller_mgmt_vlan: VLAN to use for FortiLink management purposes.
            switch_controller_igmp_snooping: Switch controller IGMP snooping.
            switch_controller_igmp_snooping_proxy: Switch controller IGMP snooping proxy.
            switch_controller_igmp_snooping_fast_leave: Switch controller IGMP snooping fast-leave.
            switch_controller_dhcp_snooping: Switch controller DHCP snooping.
            switch_controller_dhcp_snooping_verify_mac: Switch controller DHCP snooping verify MAC.
            switch_controller_dhcp_snooping_option82: Switch controller DHCP snooping option82.
            dhcp_snooping_server_list: Configure DHCP server access list.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            switch_controller_arp_inspection: Enable/disable/Monitor FortiSwitch ARP inspection.
            switch_controller_learning_limit: Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default).
            switch_controller_nac: Integrated FortiLink settings for managed FortiSwitch.
            switch_controller_dynamic: Integrated FortiLink settings for managed FortiSwitch.
            switch_controller_feature: Interface's purpose when assigning traffic (read only).
            switch_controller_iot_scanning: Enable/disable managed FortiSwitch IoT scanning.
            switch_controller_offload: Enable/disable managed FortiSwitch routing offload.
            switch_controller_offload_ip: IP for routing offload on FortiSwitch.
            switch_controller_offload_gw: Enable/disable managed FortiSwitch routing offload gateway.
            swc_vlan: Creation status for switch-controller VLANs.
            swc_first_create: Initial create for switch-controller VLANs.
            color: Color of icon on the GUI.
            tagging: Config object tagging.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            eap_supplicant: Enable/disable EAP-Supplicant.
            eap_method: EAP method.
            eap_identity: EAP identity.
            eap_password: EAP password.
            eap_ca_cert: EAP CA certificate name.
            eap_user_cert: EAP user certificate name.
            default_purdue_level: default purdue level of device detected on this interface.
            ipv6: IPv6 of interface.
            physical: Print physical interface information.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_interface.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Interface.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_interface.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Interface.required_fields()) }}
            
            Use Interface.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if client_options is not None:
            client_options = normalize_table_field(
                client_options,
                mkey="id",
                required_fields=['id', 'code'],
                field_name="client_options",
                example="[{'id': 1, 'code': 1}]",
            )
        if fail_alert_interfaces is not None:
            fail_alert_interfaces = normalize_table_field(
                fail_alert_interfaces,
                mkey="name",
                required_fields=['name'],
                field_name="fail_alert_interfaces",
                example="[{'name': 'value'}]",
            )
        if member is not None:
            member = normalize_table_field(
                member,
                mkey="interface-name",
                required_fields=['interface-name'],
                field_name="member",
                example="[{'interface-name': 'value'}]",
            )
        if security_groups is not None:
            security_groups = normalize_table_field(
                security_groups,
                mkey="name",
                required_fields=['name'],
                field_name="security_groups",
                example="[{'name': 'value'}]",
            )
        if vrrp is not None:
            vrrp = normalize_table_field(
                vrrp,
                mkey="vrid",
                required_fields=['vrid', 'vrip'],
                field_name="vrrp",
                example="[{'vrid': 1, 'vrip': '192.168.1.10'}]",
            )
        if secondaryip is not None:
            secondaryip = normalize_table_field(
                secondaryip,
                mkey="id",
                required_fields=['id'],
                field_name="secondaryip",
                example="[{'id': 1}]",
            )
        if dhcp_snooping_server_list is not None:
            dhcp_snooping_server_list = normalize_table_field(
                dhcp_snooping_server_list,
                mkey="name",
                required_fields=['name'],
                field_name="dhcp_snooping_server_list",
                example="[{'name': 'value'}]",
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
            vrf=vrf,
            cli_conn_status=cli_conn_status,
            fortilink=fortilink,
            switch_controller_source_ip=switch_controller_source_ip,
            mode=mode,
            client_options=client_options,
            distance=distance,
            priority=priority,
            dhcp_relay_interface_select_method=dhcp_relay_interface_select_method,
            dhcp_relay_interface=dhcp_relay_interface,
            dhcp_relay_vrf_select=dhcp_relay_vrf_select,
            dhcp_broadcast_flag=dhcp_broadcast_flag,
            dhcp_relay_service=dhcp_relay_service,
            dhcp_relay_ip=dhcp_relay_ip,
            dhcp_relay_source_ip=dhcp_relay_source_ip,
            dhcp_relay_circuit_id=dhcp_relay_circuit_id,
            dhcp_relay_link_selection=dhcp_relay_link_selection,
            dhcp_relay_request_all_server=dhcp_relay_request_all_server,
            dhcp_relay_allow_no_end_option=dhcp_relay_allow_no_end_option,
            dhcp_relay_type=dhcp_relay_type,
            dhcp_smart_relay=dhcp_smart_relay,
            dhcp_relay_agent_option=dhcp_relay_agent_option,
            dhcp_classless_route_addition=dhcp_classless_route_addition,
            management_ip=management_ip,
            ip=ip,
            allowaccess=allowaccess,
            gwdetect=gwdetect,
            ping_serv_status=ping_serv_status,
            detectserver=detectserver,
            detectprotocol=detectprotocol,
            ha_priority=ha_priority,
            fail_detect=fail_detect,
            fail_detect_option=fail_detect_option,
            fail_alert_method=fail_alert_method,
            fail_action_on_extender=fail_action_on_extender,
            fail_alert_interfaces=fail_alert_interfaces,
            dhcp_client_identifier=dhcp_client_identifier,
            dhcp_renew_time=dhcp_renew_time,
            ipunnumbered=ipunnumbered,
            username=username,
            pppoe_egress_cos=pppoe_egress_cos,
            pppoe_unnumbered_negotiate=pppoe_unnumbered_negotiate,
            password=password,
            idle_timeout=idle_timeout,
            multilink=multilink,
            mrru=mrru,
            detected_peer_mtu=detected_peer_mtu,
            disc_retry_timeout=disc_retry_timeout,
            padt_retry_timeout=padt_retry_timeout,
            service_name=service_name,
            ac_name=ac_name,
            lcp_echo_interval=lcp_echo_interval,
            lcp_max_echo_fails=lcp_max_echo_fails,
            defaultgw=defaultgw,
            dns_server_override=dns_server_override,
            dns_server_protocol=dns_server_protocol,
            auth_type=auth_type,
            pptp_client=pptp_client,
            pptp_user=pptp_user,
            pptp_password=pptp_password,
            pptp_server_ip=pptp_server_ip,
            pptp_auth_type=pptp_auth_type,
            pptp_timeout=pptp_timeout,
            arpforward=arpforward,
            ndiscforward=ndiscforward,
            broadcast_forward=broadcast_forward,
            bfd=bfd,
            bfd_desired_min_tx=bfd_desired_min_tx,
            bfd_detect_mult=bfd_detect_mult,
            bfd_required_min_rx=bfd_required_min_rx,
            l2forward=l2forward,
            icmp_send_redirect=icmp_send_redirect,
            icmp_accept_redirect=icmp_accept_redirect,
            reachable_time=reachable_time,
            vlanforward=vlanforward,
            stpforward=stpforward,
            stpforward_mode=stpforward_mode,
            ips_sniffer_mode=ips_sniffer_mode,
            ident_accept=ident_accept,
            ipmac=ipmac,
            subst=subst,
            macaddr=macaddr,
            virtual_mac=virtual_mac,
            substitute_dst_mac=substitute_dst_mac,
            speed=speed,
            status=status,
            netbios_forward=netbios_forward,
            wins_ip=wins_ip,
            type=type,
            dedicated_to=dedicated_to,
            trust_ip_1=trust_ip_1,
            trust_ip_2=trust_ip_2,
            trust_ip_3=trust_ip_3,
            trust_ip6_1=trust_ip6_1,
            trust_ip6_2=trust_ip6_2,
            trust_ip6_3=trust_ip6_3,
            ring_rx=ring_rx,
            ring_tx=ring_tx,
            wccp=wccp,
            netflow_sampler=netflow_sampler,
            netflow_sample_rate=netflow_sample_rate,
            netflow_sampler_id=netflow_sampler_id,
            sflow_sampler=sflow_sampler,
            drop_fragment=drop_fragment,
            src_check=src_check,
            sample_rate=sample_rate,
            polling_interval=polling_interval,
            sample_direction=sample_direction,
            explicit_web_proxy=explicit_web_proxy,
            explicit_ftp_proxy=explicit_ftp_proxy,
            proxy_captive_portal=proxy_captive_portal,
            tcp_mss=tcp_mss,
            inbandwidth=inbandwidth,
            outbandwidth=outbandwidth,
            egress_shaping_profile=egress_shaping_profile,
            ingress_shaping_profile=ingress_shaping_profile,
            spillover_threshold=spillover_threshold,
            ingress_spillover_threshold=ingress_spillover_threshold,
            weight=weight,
            interface=interface,
            external=external,
            mtu_override=mtu_override,
            mtu=mtu,
            vlan_protocol=vlan_protocol,
            vlanid=vlanid,
            forward_domain=forward_domain,
            remote_ip=remote_ip,
            member=member,
            lacp_mode=lacp_mode,
            lacp_ha_secondary=lacp_ha_secondary,
            system_id_type=system_id_type,
            system_id=system_id,
            lacp_speed=lacp_speed,
            min_links=min_links,
            min_links_down=min_links_down,
            algorithm=algorithm,
            link_up_delay=link_up_delay,
            aggregate_type=aggregate_type,
            priority_override=priority_override,
            aggregate=aggregate,
            redundant_interface=redundant_interface,
            devindex=devindex,
            vindex=vindex,
            switch=switch,
            description=description,
            alias=alias,
            security_mode=security_mode,
            security_mac_auth_bypass=security_mac_auth_bypass,
            security_ip_auth_bypass=security_ip_auth_bypass,
            security_external_web=security_external_web,
            security_external_logout=security_external_logout,
            replacemsg_override_group=replacemsg_override_group,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            security_exempt_list=security_exempt_list,
            security_groups=security_groups,
            ike_saml_server=ike_saml_server,
            device_identification=device_identification,
            exclude_signatures=exclude_signatures,
            device_user_identification=device_user_identification,
            lldp_reception=lldp_reception,
            lldp_transmission=lldp_transmission,
            lldp_network_policy=lldp_network_policy,
            estimated_upstream_bandwidth=estimated_upstream_bandwidth,
            estimated_downstream_bandwidth=estimated_downstream_bandwidth,
            measured_upstream_bandwidth=measured_upstream_bandwidth,
            measured_downstream_bandwidth=measured_downstream_bandwidth,
            bandwidth_measure_time=bandwidth_measure_time,
            monitor_bandwidth=monitor_bandwidth,
            vrrp_virtual_mac=vrrp_virtual_mac,
            vrrp=vrrp,
            phy_setting=phy_setting,
            role=role,
            snmp_index=snmp_index,
            secondary_IP=secondary_IP,
            secondaryip=secondaryip,
            preserve_session_route=preserve_session_route,
            auto_auth_extension_device=auto_auth_extension_device,
            ap_discover=ap_discover,
            fortilink_neighbor_detect=fortilink_neighbor_detect,
            ip_managed_by_fortiipam=ip_managed_by_fortiipam,
            managed_subnetwork_size=managed_subnetwork_size,
            fortilink_split_interface=fortilink_split_interface,
            internal=internal,
            fortilink_backup_link=fortilink_backup_link,
            switch_controller_access_vlan=switch_controller_access_vlan,
            switch_controller_traffic_policy=switch_controller_traffic_policy,
            switch_controller_rspan_mode=switch_controller_rspan_mode,
            switch_controller_netflow_collect=switch_controller_netflow_collect,
            switch_controller_mgmt_vlan=switch_controller_mgmt_vlan,
            switch_controller_igmp_snooping=switch_controller_igmp_snooping,
            switch_controller_igmp_snooping_proxy=switch_controller_igmp_snooping_proxy,
            switch_controller_igmp_snooping_fast_leave=switch_controller_igmp_snooping_fast_leave,
            switch_controller_dhcp_snooping=switch_controller_dhcp_snooping,
            switch_controller_dhcp_snooping_verify_mac=switch_controller_dhcp_snooping_verify_mac,
            switch_controller_dhcp_snooping_option82=switch_controller_dhcp_snooping_option82,
            dhcp_snooping_server_list=dhcp_snooping_server_list,
            switch_controller_arp_inspection=switch_controller_arp_inspection,
            switch_controller_learning_limit=switch_controller_learning_limit,
            switch_controller_nac=switch_controller_nac,
            switch_controller_dynamic=switch_controller_dynamic,
            switch_controller_feature=switch_controller_feature,
            switch_controller_iot_scanning=switch_controller_iot_scanning,
            switch_controller_offload=switch_controller_offload,
            switch_controller_offload_ip=switch_controller_offload_ip,
            switch_controller_offload_gw=switch_controller_offload_gw,
            swc_vlan=swc_vlan,
            swc_first_create=swc_first_create,
            color=color,
            tagging=tagging,
            eap_supplicant=eap_supplicant,
            eap_method=eap_method,
            eap_identity=eap_identity,
            eap_password=eap_password,
            eap_ca_cert=eap_ca_cert,
            eap_user_cert=eap_user_cert,
            default_purdue_level=default_purdue_level,
            ipv6=ipv6,
            physical=physical,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.interface import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/interface",
            )

        endpoint = "/system/interface"
        
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
        Delete system/interface object.

        Configure interfaces.

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
            >>> result = fgt.api.cmdb.system_interface.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/interface/" + str(name)

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
        Check if system/interface object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_interface.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_interface.exists(name=1):
            ...     fgt.api.cmdb.system_interface.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
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
        name: str | None = None,
        vrf: int | None = None,
        cli_conn_status: int | None = None,
        fortilink: Literal["enable", "disable"] | None = None,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = None,
        mode: Literal["static", "dhcp", "pppoe"] | None = None,
        client_options: str | list[str] | list[dict[str, Any]] | None = None,
        distance: int | None = None,
        priority: int | None = None,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        dhcp_relay_interface: str | None = None,
        dhcp_relay_vrf_select: int | None = None,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = None,
        dhcp_relay_service: Literal["disable", "enable"] | None = None,
        dhcp_relay_ip: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_relay_source_ip: str | None = None,
        dhcp_relay_circuit_id: str | None = None,
        dhcp_relay_link_selection: str | None = None,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = None,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = None,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = None,
        dhcp_smart_relay: Literal["disable", "enable"] | None = None,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = None,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = None,
        management_ip: Any | None = None,
        ip: Any | None = None,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | list[dict[str, Any]] | None = None,
        gwdetect: Literal["enable", "disable"] | None = None,
        ping_serv_status: int | None = None,
        detectserver: str | None = None,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | list[dict[str, Any]] | None = None,
        ha_priority: int | None = None,
        fail_detect: Literal["enable", "disable"] | None = None,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | list[dict[str, Any]] | None = None,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = None,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = None,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_client_identifier: str | None = None,
        dhcp_renew_time: int | None = None,
        ipunnumbered: str | None = None,
        username: str | None = None,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = None,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        idle_timeout: int | None = None,
        multilink: Literal["enable", "disable"] | None = None,
        mrru: int | None = None,
        detected_peer_mtu: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        defaultgw: Literal["enable", "disable"] | None = None,
        dns_server_override: Literal["enable", "disable"] | None = None,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | list[dict[str, Any]] | None = None,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_client: Literal["enable", "disable"] | None = None,
        pptp_user: str | None = None,
        pptp_password: Any | None = None,
        pptp_server_ip: str | None = None,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = None,
        pptp_timeout: int | None = None,
        arpforward: Literal["enable", "disable"] | None = None,
        ndiscforward: Literal["enable", "disable"] | None = None,
        broadcast_forward: Literal["enable", "disable"] | None = None,
        bfd: Literal["global", "enable", "disable"] | None = None,
        bfd_desired_min_tx: int | None = None,
        bfd_detect_mult: int | None = None,
        bfd_required_min_rx: int | None = None,
        l2forward: Literal["enable", "disable"] | None = None,
        icmp_send_redirect: Literal["enable", "disable"] | None = None,
        icmp_accept_redirect: Literal["enable", "disable"] | None = None,
        reachable_time: int | None = None,
        vlanforward: Literal["enable", "disable"] | None = None,
        stpforward: Literal["enable", "disable"] | None = None,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = None,
        ips_sniffer_mode: Literal["enable", "disable"] | None = None,
        ident_accept: Literal["enable", "disable"] | None = None,
        ipmac: Literal["enable", "disable"] | None = None,
        subst: Literal["enable", "disable"] | None = None,
        macaddr: str | None = None,
        virtual_mac: str | None = None,
        substitute_dst_mac: str | None = None,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = None,
        status: Literal["up", "down"] | None = None,
        netbios_forward: Literal["disable", "enable"] | None = None,
        wins_ip: str | None = None,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = None,
        dedicated_to: Literal["none", "management"] | None = None,
        trust_ip_1: Any | None = None,
        trust_ip_2: Any | None = None,
        trust_ip_3: Any | None = None,
        trust_ip6_1: str | None = None,
        trust_ip6_2: str | None = None,
        trust_ip6_3: str | None = None,
        ring_rx: int | None = None,
        ring_tx: int | None = None,
        wccp: Literal["enable", "disable"] | None = None,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = None,
        netflow_sample_rate: int | None = None,
        netflow_sampler_id: int | None = None,
        sflow_sampler: Literal["enable", "disable"] | None = None,
        drop_fragment: Literal["enable", "disable"] | None = None,
        src_check: Literal["enable", "disable"] | None = None,
        sample_rate: int | None = None,
        polling_interval: int | None = None,
        sample_direction: Literal["tx", "rx", "both"] | None = None,
        explicit_web_proxy: Literal["enable", "disable"] | None = None,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = None,
        proxy_captive_portal: Literal["enable", "disable"] | None = None,
        tcp_mss: int | None = None,
        inbandwidth: int | None = None,
        outbandwidth: int | None = None,
        egress_shaping_profile: str | None = None,
        ingress_shaping_profile: str | None = None,
        spillover_threshold: int | None = None,
        ingress_spillover_threshold: int | None = None,
        weight: int | None = None,
        interface: str | None = None,
        external: Literal["enable", "disable"] | None = None,
        mtu_override: Literal["enable", "disable"] | None = None,
        mtu: int | None = None,
        vlan_protocol: Literal["8021q", "8021ad"] | None = None,
        vlanid: int | None = None,
        forward_domain: int | None = None,
        remote_ip: Any | None = None,
        member: str | list[str] | list[dict[str, Any]] | None = None,
        lacp_mode: Literal["static", "passive", "active"] | None = None,
        lacp_ha_secondary: Literal["enable", "disable"] | None = None,
        system_id_type: Literal["auto", "user"] | None = None,
        system_id: str | None = None,
        lacp_speed: Literal["slow", "fast"] | None = None,
        min_links: int | None = None,
        min_links_down: Literal["operational", "administrative"] | None = None,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = None,
        link_up_delay: int | None = None,
        aggregate_type: Literal["physical", "vxlan"] | None = None,
        priority_override: Literal["enable", "disable"] | None = None,
        aggregate: str | None = None,
        redundant_interface: str | None = None,
        devindex: int | None = None,
        vindex: int | None = None,
        switch: str | None = None,
        description: str | None = None,
        alias: str | None = None,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = None,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = None,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = None,
        security_external_web: str | None = None,
        security_external_logout: str | None = None,
        replacemsg_override_group: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        security_exempt_list: str | None = None,
        security_groups: str | list[str] | list[dict[str, Any]] | None = None,
        ike_saml_server: str | None = None,
        device_identification: Literal["enable", "disable"] | None = None,
        exclude_signatures: Literal["iot", "ot"] | list[str] | list[dict[str, Any]] | None = None,
        device_user_identification: Literal["enable", "disable"] | None = None,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = None,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = None,
        lldp_network_policy: str | None = None,
        estimated_upstream_bandwidth: int | None = None,
        estimated_downstream_bandwidth: int | None = None,
        measured_upstream_bandwidth: int | None = None,
        measured_downstream_bandwidth: int | None = None,
        bandwidth_measure_time: int | None = None,
        monitor_bandwidth: Literal["enable", "disable"] | None = None,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = None,
        vrrp: str | list[str] | list[dict[str, Any]] | None = None,
        phy_setting: str | None = None,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = None,
        snmp_index: int | None = None,
        secondary_IP: Literal["enable", "disable"] | None = None,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = None,
        preserve_session_route: Literal["enable", "disable"] | None = None,
        auto_auth_extension_device: Literal["enable", "disable"] | None = None,
        ap_discover: Literal["enable", "disable"] | None = None,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = None,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = None,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = None,
        fortilink_split_interface: Literal["enable", "disable"] | None = None,
        internal: int | None = None,
        fortilink_backup_link: int | None = None,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = None,
        switch_controller_traffic_policy: str | None = None,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = None,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = None,
        switch_controller_mgmt_vlan: int | None = None,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = None,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = None,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = None,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = None,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = None,
        switch_controller_learning_limit: int | None = None,
        switch_controller_nac: str | None = None,
        switch_controller_dynamic: str | None = None,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = None,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = None,
        switch_controller_offload: Literal["enable", "disable"] | None = None,
        switch_controller_offload_ip: str | None = None,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = None,
        swc_vlan: int | None = None,
        swc_first_create: int | None = None,
        color: int | None = None,
        tagging: str | list[str] | list[dict[str, Any]] | None = None,
        eap_supplicant: Literal["enable", "disable"] | None = None,
        eap_method: Literal["tls", "peap"] | None = None,
        eap_identity: str | None = None,
        eap_password: Any | None = None,
        eap_ca_cert: str | None = None,
        eap_user_cert: str | None = None,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        ipv6: str | None = None,
        physical: Any | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/interface object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            vrf: Field vrf
            cli_conn_status: Field cli-conn-status
            fortilink: Field fortilink
            switch_controller_source_ip: Field switch-controller-source-ip
            mode: Field mode
            client_options: Field client-options
            distance: Field distance
            priority: Field priority
            dhcp_relay_interface_select_method: Field dhcp-relay-interface-select-method
            dhcp_relay_interface: Field dhcp-relay-interface
            dhcp_relay_vrf_select: Field dhcp-relay-vrf-select
            dhcp_broadcast_flag: Field dhcp-broadcast-flag
            dhcp_relay_service: Field dhcp-relay-service
            dhcp_relay_ip: Field dhcp-relay-ip
            dhcp_relay_source_ip: Field dhcp-relay-source-ip
            dhcp_relay_circuit_id: Field dhcp-relay-circuit-id
            dhcp_relay_link_selection: Field dhcp-relay-link-selection
            dhcp_relay_request_all_server: Field dhcp-relay-request-all-server
            dhcp_relay_allow_no_end_option: Field dhcp-relay-allow-no-end-option
            dhcp_relay_type: Field dhcp-relay-type
            dhcp_smart_relay: Field dhcp-smart-relay
            dhcp_relay_agent_option: Field dhcp-relay-agent-option
            dhcp_classless_route_addition: Field dhcp-classless-route-addition
            management_ip: Field management-ip
            ip: Field ip
            allowaccess: Field allowaccess
            gwdetect: Field gwdetect
            ping_serv_status: Field ping-serv-status
            detectserver: Field detectserver
            detectprotocol: Field detectprotocol
            ha_priority: Field ha-priority
            fail_detect: Field fail-detect
            fail_detect_option: Field fail-detect-option
            fail_alert_method: Field fail-alert-method
            fail_action_on_extender: Field fail-action-on-extender
            fail_alert_interfaces: Field fail-alert-interfaces
            dhcp_client_identifier: Field dhcp-client-identifier
            dhcp_renew_time: Field dhcp-renew-time
            ipunnumbered: Field ipunnumbered
            username: Field username
            pppoe_egress_cos: Field pppoe-egress-cos
            pppoe_unnumbered_negotiate: Field pppoe-unnumbered-negotiate
            password: Field password
            idle_timeout: Field idle-timeout
            multilink: Field multilink
            mrru: Field mrru
            detected_peer_mtu: Field detected-peer-mtu
            disc_retry_timeout: Field disc-retry-timeout
            padt_retry_timeout: Field padt-retry-timeout
            service_name: Field service-name
            ac_name: Field ac-name
            lcp_echo_interval: Field lcp-echo-interval
            lcp_max_echo_fails: Field lcp-max-echo-fails
            defaultgw: Field defaultgw
            dns_server_override: Field dns-server-override
            dns_server_protocol: Field dns-server-protocol
            auth_type: Field auth-type
            pptp_client: Field pptp-client
            pptp_user: Field pptp-user
            pptp_password: Field pptp-password
            pptp_server_ip: Field pptp-server-ip
            pptp_auth_type: Field pptp-auth-type
            pptp_timeout: Field pptp-timeout
            arpforward: Field arpforward
            ndiscforward: Field ndiscforward
            broadcast_forward: Field broadcast-forward
            bfd: Field bfd
            bfd_desired_min_tx: Field bfd-desired-min-tx
            bfd_detect_mult: Field bfd-detect-mult
            bfd_required_min_rx: Field bfd-required-min-rx
            l2forward: Field l2forward
            icmp_send_redirect: Field icmp-send-redirect
            icmp_accept_redirect: Field icmp-accept-redirect
            reachable_time: Field reachable-time
            vlanforward: Field vlanforward
            stpforward: Field stpforward
            stpforward_mode: Field stpforward-mode
            ips_sniffer_mode: Field ips-sniffer-mode
            ident_accept: Field ident-accept
            ipmac: Field ipmac
            subst: Field subst
            macaddr: Field macaddr
            virtual_mac: Field virtual-mac
            substitute_dst_mac: Field substitute-dst-mac
            speed: Field speed
            status: Field status
            netbios_forward: Field netbios-forward
            wins_ip: Field wins-ip
            type: Field type
            dedicated_to: Field dedicated-to
            trust_ip_1: Field trust-ip-1
            trust_ip_2: Field trust-ip-2
            trust_ip_3: Field trust-ip-3
            trust_ip6_1: Field trust-ip6-1
            trust_ip6_2: Field trust-ip6-2
            trust_ip6_3: Field trust-ip6-3
            ring_rx: Field ring-rx
            ring_tx: Field ring-tx
            wccp: Field wccp
            netflow_sampler: Field netflow-sampler
            netflow_sample_rate: Field netflow-sample-rate
            netflow_sampler_id: Field netflow-sampler-id
            sflow_sampler: Field sflow-sampler
            drop_fragment: Field drop-fragment
            src_check: Field src-check
            sample_rate: Field sample-rate
            polling_interval: Field polling-interval
            sample_direction: Field sample-direction
            explicit_web_proxy: Field explicit-web-proxy
            explicit_ftp_proxy: Field explicit-ftp-proxy
            proxy_captive_portal: Field proxy-captive-portal
            tcp_mss: Field tcp-mss
            inbandwidth: Field inbandwidth
            outbandwidth: Field outbandwidth
            egress_shaping_profile: Field egress-shaping-profile
            ingress_shaping_profile: Field ingress-shaping-profile
            spillover_threshold: Field spillover-threshold
            ingress_spillover_threshold: Field ingress-spillover-threshold
            weight: Field weight
            interface: Field interface
            external: Field external
            mtu_override: Field mtu-override
            mtu: Field mtu
            vlan_protocol: Field vlan-protocol
            vlanid: Field vlanid
            forward_domain: Field forward-domain
            remote_ip: Field remote-ip
            member: Field member
            lacp_mode: Field lacp-mode
            lacp_ha_secondary: Field lacp-ha-secondary
            system_id_type: Field system-id-type
            system_id: Field system-id
            lacp_speed: Field lacp-speed
            min_links: Field min-links
            min_links_down: Field min-links-down
            algorithm: Field algorithm
            link_up_delay: Field link-up-delay
            aggregate_type: Field aggregate-type
            priority_override: Field priority-override
            aggregate: Field aggregate
            redundant_interface: Field redundant-interface
            devindex: Field devindex
            vindex: Field vindex
            switch: Field switch
            description: Field description
            alias: Field alias
            security_mode: Field security-mode
            security_mac_auth_bypass: Field security-mac-auth-bypass
            security_ip_auth_bypass: Field security-ip-auth-bypass
            security_external_web: Field security-external-web
            security_external_logout: Field security-external-logout
            replacemsg_override_group: Field replacemsg-override-group
            security_redirect_url: Field security-redirect-url
            auth_cert: Field auth-cert
            auth_portal_addr: Field auth-portal-addr
            security_exempt_list: Field security-exempt-list
            security_groups: Field security-groups
            ike_saml_server: Field ike-saml-server
            device_identification: Field device-identification
            exclude_signatures: Field exclude-signatures
            device_user_identification: Field device-user-identification
            lldp_reception: Field lldp-reception
            lldp_transmission: Field lldp-transmission
            lldp_network_policy: Field lldp-network-policy
            estimated_upstream_bandwidth: Field estimated-upstream-bandwidth
            estimated_downstream_bandwidth: Field estimated-downstream-bandwidth
            measured_upstream_bandwidth: Field measured-upstream-bandwidth
            measured_downstream_bandwidth: Field measured-downstream-bandwidth
            bandwidth_measure_time: Field bandwidth-measure-time
            monitor_bandwidth: Field monitor-bandwidth
            vrrp_virtual_mac: Field vrrp-virtual-mac
            vrrp: Field vrrp
            phy_setting: Field phy-setting
            role: Field role
            snmp_index: Field snmp-index
            secondary_IP: Field secondary-IP
            secondaryip: Field secondaryip
            preserve_session_route: Field preserve-session-route
            auto_auth_extension_device: Field auto-auth-extension-device
            ap_discover: Field ap-discover
            fortilink_neighbor_detect: Field fortilink-neighbor-detect
            ip_managed_by_fortiipam: Field ip-managed-by-fortiipam
            managed_subnetwork_size: Field managed-subnetwork-size
            fortilink_split_interface: Field fortilink-split-interface
            internal: Field internal
            fortilink_backup_link: Field fortilink-backup-link
            switch_controller_access_vlan: Field switch-controller-access-vlan
            switch_controller_traffic_policy: Field switch-controller-traffic-policy
            switch_controller_rspan_mode: Field switch-controller-rspan-mode
            switch_controller_netflow_collect: Field switch-controller-netflow-collect
            switch_controller_mgmt_vlan: Field switch-controller-mgmt-vlan
            switch_controller_igmp_snooping: Field switch-controller-igmp-snooping
            switch_controller_igmp_snooping_proxy: Field switch-controller-igmp-snooping-proxy
            switch_controller_igmp_snooping_fast_leave: Field switch-controller-igmp-snooping-fast-leave
            switch_controller_dhcp_snooping: Field switch-controller-dhcp-snooping
            switch_controller_dhcp_snooping_verify_mac: Field switch-controller-dhcp-snooping-verify-mac
            switch_controller_dhcp_snooping_option82: Field switch-controller-dhcp-snooping-option82
            dhcp_snooping_server_list: Field dhcp-snooping-server-list
            switch_controller_arp_inspection: Field switch-controller-arp-inspection
            switch_controller_learning_limit: Field switch-controller-learning-limit
            switch_controller_nac: Field switch-controller-nac
            switch_controller_dynamic: Field switch-controller-dynamic
            switch_controller_feature: Field switch-controller-feature
            switch_controller_iot_scanning: Field switch-controller-iot-scanning
            switch_controller_offload: Field switch-controller-offload
            switch_controller_offload_ip: Field switch-controller-offload-ip
            switch_controller_offload_gw: Field switch-controller-offload-gw
            swc_vlan: Field swc-vlan
            swc_first_create: Field swc-first-create
            color: Field color
            tagging: Field tagging
            eap_supplicant: Field eap-supplicant
            eap_method: Field eap-method
            eap_identity: Field eap-identity
            eap_password: Field eap-password
            eap_ca_cert: Field eap-ca-cert
            eap_user_cert: Field eap-user-cert
            default_purdue_level: Field default-purdue-level
            ipv6: Field ipv6
            physical: Field physical
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_interface.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_interface.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_interface.set(payload_dict=obj_data)
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
            vrf=vrf,
            cli_conn_status=cli_conn_status,
            fortilink=fortilink,
            switch_controller_source_ip=switch_controller_source_ip,
            mode=mode,
            client_options=client_options,
            distance=distance,
            priority=priority,
            dhcp_relay_interface_select_method=dhcp_relay_interface_select_method,
            dhcp_relay_interface=dhcp_relay_interface,
            dhcp_relay_vrf_select=dhcp_relay_vrf_select,
            dhcp_broadcast_flag=dhcp_broadcast_flag,
            dhcp_relay_service=dhcp_relay_service,
            dhcp_relay_ip=dhcp_relay_ip,
            dhcp_relay_source_ip=dhcp_relay_source_ip,
            dhcp_relay_circuit_id=dhcp_relay_circuit_id,
            dhcp_relay_link_selection=dhcp_relay_link_selection,
            dhcp_relay_request_all_server=dhcp_relay_request_all_server,
            dhcp_relay_allow_no_end_option=dhcp_relay_allow_no_end_option,
            dhcp_relay_type=dhcp_relay_type,
            dhcp_smart_relay=dhcp_smart_relay,
            dhcp_relay_agent_option=dhcp_relay_agent_option,
            dhcp_classless_route_addition=dhcp_classless_route_addition,
            management_ip=management_ip,
            ip=ip,
            allowaccess=allowaccess,
            gwdetect=gwdetect,
            ping_serv_status=ping_serv_status,
            detectserver=detectserver,
            detectprotocol=detectprotocol,
            ha_priority=ha_priority,
            fail_detect=fail_detect,
            fail_detect_option=fail_detect_option,
            fail_alert_method=fail_alert_method,
            fail_action_on_extender=fail_action_on_extender,
            fail_alert_interfaces=fail_alert_interfaces,
            dhcp_client_identifier=dhcp_client_identifier,
            dhcp_renew_time=dhcp_renew_time,
            ipunnumbered=ipunnumbered,
            username=username,
            pppoe_egress_cos=pppoe_egress_cos,
            pppoe_unnumbered_negotiate=pppoe_unnumbered_negotiate,
            password=password,
            idle_timeout=idle_timeout,
            multilink=multilink,
            mrru=mrru,
            detected_peer_mtu=detected_peer_mtu,
            disc_retry_timeout=disc_retry_timeout,
            padt_retry_timeout=padt_retry_timeout,
            service_name=service_name,
            ac_name=ac_name,
            lcp_echo_interval=lcp_echo_interval,
            lcp_max_echo_fails=lcp_max_echo_fails,
            defaultgw=defaultgw,
            dns_server_override=dns_server_override,
            dns_server_protocol=dns_server_protocol,
            auth_type=auth_type,
            pptp_client=pptp_client,
            pptp_user=pptp_user,
            pptp_password=pptp_password,
            pptp_server_ip=pptp_server_ip,
            pptp_auth_type=pptp_auth_type,
            pptp_timeout=pptp_timeout,
            arpforward=arpforward,
            ndiscforward=ndiscforward,
            broadcast_forward=broadcast_forward,
            bfd=bfd,
            bfd_desired_min_tx=bfd_desired_min_tx,
            bfd_detect_mult=bfd_detect_mult,
            bfd_required_min_rx=bfd_required_min_rx,
            l2forward=l2forward,
            icmp_send_redirect=icmp_send_redirect,
            icmp_accept_redirect=icmp_accept_redirect,
            reachable_time=reachable_time,
            vlanforward=vlanforward,
            stpforward=stpforward,
            stpforward_mode=stpforward_mode,
            ips_sniffer_mode=ips_sniffer_mode,
            ident_accept=ident_accept,
            ipmac=ipmac,
            subst=subst,
            macaddr=macaddr,
            virtual_mac=virtual_mac,
            substitute_dst_mac=substitute_dst_mac,
            speed=speed,
            status=status,
            netbios_forward=netbios_forward,
            wins_ip=wins_ip,
            type=type,
            dedicated_to=dedicated_to,
            trust_ip_1=trust_ip_1,
            trust_ip_2=trust_ip_2,
            trust_ip_3=trust_ip_3,
            trust_ip6_1=trust_ip6_1,
            trust_ip6_2=trust_ip6_2,
            trust_ip6_3=trust_ip6_3,
            ring_rx=ring_rx,
            ring_tx=ring_tx,
            wccp=wccp,
            netflow_sampler=netflow_sampler,
            netflow_sample_rate=netflow_sample_rate,
            netflow_sampler_id=netflow_sampler_id,
            sflow_sampler=sflow_sampler,
            drop_fragment=drop_fragment,
            src_check=src_check,
            sample_rate=sample_rate,
            polling_interval=polling_interval,
            sample_direction=sample_direction,
            explicit_web_proxy=explicit_web_proxy,
            explicit_ftp_proxy=explicit_ftp_proxy,
            proxy_captive_portal=proxy_captive_portal,
            tcp_mss=tcp_mss,
            inbandwidth=inbandwidth,
            outbandwidth=outbandwidth,
            egress_shaping_profile=egress_shaping_profile,
            ingress_shaping_profile=ingress_shaping_profile,
            spillover_threshold=spillover_threshold,
            ingress_spillover_threshold=ingress_spillover_threshold,
            weight=weight,
            interface=interface,
            external=external,
            mtu_override=mtu_override,
            mtu=mtu,
            vlan_protocol=vlan_protocol,
            vlanid=vlanid,
            forward_domain=forward_domain,
            remote_ip=remote_ip,
            member=member,
            lacp_mode=lacp_mode,
            lacp_ha_secondary=lacp_ha_secondary,
            system_id_type=system_id_type,
            system_id=system_id,
            lacp_speed=lacp_speed,
            min_links=min_links,
            min_links_down=min_links_down,
            algorithm=algorithm,
            link_up_delay=link_up_delay,
            aggregate_type=aggregate_type,
            priority_override=priority_override,
            aggregate=aggregate,
            redundant_interface=redundant_interface,
            devindex=devindex,
            vindex=vindex,
            switch=switch,
            description=description,
            alias=alias,
            security_mode=security_mode,
            security_mac_auth_bypass=security_mac_auth_bypass,
            security_ip_auth_bypass=security_ip_auth_bypass,
            security_external_web=security_external_web,
            security_external_logout=security_external_logout,
            replacemsg_override_group=replacemsg_override_group,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            security_exempt_list=security_exempt_list,
            security_groups=security_groups,
            ike_saml_server=ike_saml_server,
            device_identification=device_identification,
            exclude_signatures=exclude_signatures,
            device_user_identification=device_user_identification,
            lldp_reception=lldp_reception,
            lldp_transmission=lldp_transmission,
            lldp_network_policy=lldp_network_policy,
            estimated_upstream_bandwidth=estimated_upstream_bandwidth,
            estimated_downstream_bandwidth=estimated_downstream_bandwidth,
            measured_upstream_bandwidth=measured_upstream_bandwidth,
            measured_downstream_bandwidth=measured_downstream_bandwidth,
            bandwidth_measure_time=bandwidth_measure_time,
            monitor_bandwidth=monitor_bandwidth,
            vrrp_virtual_mac=vrrp_virtual_mac,
            vrrp=vrrp,
            phy_setting=phy_setting,
            role=role,
            snmp_index=snmp_index,
            secondary_IP=secondary_IP,
            secondaryip=secondaryip,
            preserve_session_route=preserve_session_route,
            auto_auth_extension_device=auto_auth_extension_device,
            ap_discover=ap_discover,
            fortilink_neighbor_detect=fortilink_neighbor_detect,
            ip_managed_by_fortiipam=ip_managed_by_fortiipam,
            managed_subnetwork_size=managed_subnetwork_size,
            fortilink_split_interface=fortilink_split_interface,
            internal=internal,
            fortilink_backup_link=fortilink_backup_link,
            switch_controller_access_vlan=switch_controller_access_vlan,
            switch_controller_traffic_policy=switch_controller_traffic_policy,
            switch_controller_rspan_mode=switch_controller_rspan_mode,
            switch_controller_netflow_collect=switch_controller_netflow_collect,
            switch_controller_mgmt_vlan=switch_controller_mgmt_vlan,
            switch_controller_igmp_snooping=switch_controller_igmp_snooping,
            switch_controller_igmp_snooping_proxy=switch_controller_igmp_snooping_proxy,
            switch_controller_igmp_snooping_fast_leave=switch_controller_igmp_snooping_fast_leave,
            switch_controller_dhcp_snooping=switch_controller_dhcp_snooping,
            switch_controller_dhcp_snooping_verify_mac=switch_controller_dhcp_snooping_verify_mac,
            switch_controller_dhcp_snooping_option82=switch_controller_dhcp_snooping_option82,
            dhcp_snooping_server_list=dhcp_snooping_server_list,
            switch_controller_arp_inspection=switch_controller_arp_inspection,
            switch_controller_learning_limit=switch_controller_learning_limit,
            switch_controller_nac=switch_controller_nac,
            switch_controller_dynamic=switch_controller_dynamic,
            switch_controller_feature=switch_controller_feature,
            switch_controller_iot_scanning=switch_controller_iot_scanning,
            switch_controller_offload=switch_controller_offload,
            switch_controller_offload_ip=switch_controller_offload_ip,
            switch_controller_offload_gw=switch_controller_offload_gw,
            swc_vlan=swc_vlan,
            swc_first_create=swc_first_create,
            color=color,
            tagging=tagging,
            eap_supplicant=eap_supplicant,
            eap_method=eap_method,
            eap_identity=eap_identity,
            eap_password=eap_password,
            eap_ca_cert=eap_ca_cert,
            eap_user_cert=eap_user_cert,
            default_purdue_level=default_purdue_level,
            ipv6=ipv6,
            physical=physical,
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
        Move system/interface object to a new position.
        
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
            >>> fgt.api.cmdb.system_interface.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/interface",
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
        Clone system/interface object.
        
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
            >>> fgt.api.cmdb.system_interface.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/interface",
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
        Check if system/interface object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_interface.exists(name=1):
            ...     fgt.api.cmdb.system_interface.post(payload_dict=data)
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


"""
FortiOS CMDB - System global_

Configuration endpoint for managing cmdb system/global_ objects.

API Endpoints:
    GET    /cmdb/system/global_
    POST   /cmdb/system/global_
    PUT    /cmdb/system/global_/{identifier}
    DELETE /cmdb/system/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_global_.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_global_.post(
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

class Global(CRUDEndpoint, MetadataMixin):
    """Global Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "global_"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "internet_service_download_list": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
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
        """Initialize Global endpoint."""
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
        Retrieve system/global_ configuration.

        Configure global attributes.

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
            >>> # Get all system/global_ objects
            >>> result = fgt.api.cmdb.system_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_global_.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_global_.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_global_.get_schema()

        See Also:
            - post(): Create new system/global_ object
            - put(): Update existing system/global_ object
            - delete(): Remove system/global_ object
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
            endpoint = f"/system/global/{name}"
            unwrap_single = True
        else:
            endpoint = "/system/global"
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
            >>> schema = fgt.api.cmdb.system_global_.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_global_.get_schema(format="json-schema")
        
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
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = None,
        gui_ipv6: Literal["enable", "disable"] | None = None,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = None,
        gui_local_out: Literal["enable", "disable"] | None = None,
        gui_certificates: Literal["enable", "disable"] | None = None,
        gui_custom_language: Literal["enable", "disable"] | None = None,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = None,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = None,
        gui_display_hostname: Literal["enable", "disable"] | None = None,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = None,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = None,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = None,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = None,
        gui_workflow_management: Literal["enable", "disable"] | None = None,
        gui_cdn_usage: Literal["enable", "disable"] | None = None,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = None,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = None,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = None,
        admintimeout: int | None = None,
        admin_console_timeout: int | None = None,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = None,
        ssd_trim_hour: int | None = None,
        ssd_trim_min: int | None = None,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = None,
        ssd_trim_date: int | None = None,
        admin_concurrent: Literal["enable", "disable"] | None = None,
        admin_lockout_threshold: int | None = None,
        admin_lockout_duration: int | None = None,
        refresh: int | None = None,
        interval: int | None = None,
        failtime: int | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        daily_restart: Literal["enable", "disable"] | None = None,
        restart_time: str | None = None,
        wad_restart_mode: Literal["none", "time", "memory"] | None = None,
        wad_restart_start_time: str | None = None,
        wad_restart_end_time: str | None = None,
        wad_p2s_max_body_size: int | None = None,
        radius_port: int | None = None,
        speedtestd_server_port: int | None = None,
        speedtestd_ctrl_port: int | None = None,
        admin_login_max: int | None = None,
        remoteauthtimeout: int | None = None,
        ldapconntimeout: int | None = None,
        batch_cmdb: Literal["enable", "disable"] | None = None,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = None,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = None,
        autorun_log_fsck: Literal["enable", "disable"] | None = None,
        timezone: str | None = None,
        traffic_priority: Literal["tos", "dscp"] | None = None,
        traffic_priority_level: Literal["low", "medium", "high"] | None = None,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = None,
        quic_max_datagram_size: int | None = None,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = None,
        quic_ack_thresold: int | None = None,
        quic_pmtud: Literal["enable", "disable"] | None = None,
        quic_tls_handshake_timeout: int | None = None,
        anti_replay: Literal["disable", "loose", "strict"] | None = None,
        send_pmtu_icmp: Literal["enable", "disable"] | None = None,
        honor_df: Literal["enable", "disable"] | None = None,
        pmtu_discovery: Literal["enable", "disable"] | None = None,
        revision_image_auto_backup: Literal["enable", "disable"] | None = None,
        revision_backup_on_logout: Literal["enable", "disable"] | None = None,
        management_vdom: str | None = None,
        hostname: str | None = None,
        alias: str | None = None,
        strong_crypto: Literal["enable", "disable"] | None = None,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = None,
        snat_route_change: Literal["enable", "disable"] | None = None,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = None,
        speedtest_server: Literal["enable", "disable"] | None = None,
        cli_audit_log: Literal["enable", "disable"] | None = None,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = None,
        fds_statistics: Literal["enable", "disable"] | None = None,
        fds_statistics_period: int | None = None,
        tcp_option: Literal["enable", "disable"] | None = None,
        lldp_transmission: Literal["enable", "disable"] | None = None,
        lldp_reception: Literal["enable", "disable"] | None = None,
        proxy_auth_timeout: int | None = None,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = None,
        proxy_re_authentication_time: int | None = None,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = None,
        proxy_auth_lifetime_timeout: int | None = None,
        proxy_resource_mode: Literal["enable", "disable"] | None = None,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = None,
        sys_perf_log_interval: int | None = None,
        check_protocol_header: Literal["loose", "strict"] | None = None,
        vip_arp_range: Literal["unlimited", "restricted"] | None = None,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = None,
        allow_traffic_redirect: Literal["enable", "disable"] | None = None,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = None,
        strict_dirty_session_check: Literal["enable", "disable"] | None = None,
        tcp_halfclose_timer: int | None = None,
        tcp_halfopen_timer: int | None = None,
        tcp_timewait_timer: int | None = None,
        tcp_rst_timer: int | None = None,
        udp_idle_timer: int | None = None,
        block_session_timer: int | None = None,
        ip_src_port_range: str | None = None,
        pre_login_banner: Literal["enable", "disable"] | None = None,
        post_login_banner: Literal["disable", "enable"] | None = None,
        tftp: Literal["enable", "disable"] | None = None,
        av_failopen: Literal["pass", "off", "one-shot"] | None = None,
        av_failopen_session: Literal["enable", "disable"] | None = None,
        memory_use_threshold_extreme: int | None = None,
        memory_use_threshold_red: int | None = None,
        memory_use_threshold_green: int | None = None,
        ip_fragment_mem_thresholds: int | None = None,
        ip_fragment_timeout: int | None = None,
        ipv6_fragment_timeout: int | None = None,
        cpu_use_threshold: int | None = None,
        log_single_cpu_high: Literal["enable", "disable"] | None = None,
        check_reset_range: Literal["strict", "disable"] | None = None,
        upgrade_report: Literal["enable", "disable"] | None = None,
        admin_port: int | None = None,
        admin_sport: int | None = None,
        admin_host: str | None = None,
        admin_https_redirect: Literal["enable", "disable"] | None = None,
        admin_hsts_max_age: int | None = None,
        admin_ssh_password: Literal["enable", "disable"] | None = None,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = None,
        admin_ssh_port: int | None = None,
        admin_ssh_grace_time: int | None = None,
        admin_ssh_v1: Literal["enable", "disable"] | None = None,
        admin_telnet: Literal["enable", "disable"] | None = None,
        admin_telnet_port: int | None = None,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = None,
        admin_forticloud_sso_default_profile: str | None = None,
        default_service_source_port: str | None = None,
        admin_server_cert: str | None = None,
        admin_https_pki_required: Literal["enable", "disable"] | None = None,
        wifi_certificate: str | None = None,
        dhcp_lease_backup_interval: int | None = None,
        wifi_ca_certificate: str | None = None,
        auth_http_port: int | None = None,
        auth_https_port: int | None = None,
        auth_ike_saml_port: int | None = None,
        auth_keepalive: Literal["enable", "disable"] | None = None,
        policy_auth_concurrent: int | None = None,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = None,
        auth_cert: str | None = None,
        clt_cert_req: Literal["enable", "disable"] | None = None,
        fortiservice_port: int | None = None,
        cfg_save: Literal["automatic", "manual", "revert"] | None = None,
        cfg_revert_timeout: int | None = None,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = None,
        admin_scp: Literal["enable", "disable"] | None = None,
        wireless_controller: Literal["enable", "disable"] | None = None,
        wireless_controller_port: int | None = None,
        fortiextender_data_port: int | None = None,
        fortiextender: Literal["disable", "enable"] | None = None,
        extender_controller_reserved_network: Any | None = None,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = None,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = None,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = None,
        switch_controller: Literal["disable", "enable"] | None = None,
        switch_controller_reserved_network: Any | None = None,
        dnsproxy_worker_count: int | None = None,
        url_filter_count: int | None = None,
        httpd_max_worker_count: int | None = None,
        proxy_worker_count: int | None = None,
        scanunit_count: int | None = None,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = None,
        ipv6_accept_dad: int | None = None,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = None,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = None,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = None,
        csr_ca_attribute: Literal["enable", "disable"] | None = None,
        wimax_4g_usb: Literal["enable", "disable"] | None = None,
        cert_chain_max: int | None = None,
        sslvpn_max_worker_count: int | None = None,
        sslvpn_affinity: str | None = None,
        sslvpn_web_mode: Literal["enable", "disable"] | None = None,
        two_factor_ftk_expiry: int | None = None,
        two_factor_email_expiry: int | None = None,
        two_factor_sms_expiry: int | None = None,
        two_factor_fac_expiry: int | None = None,
        two_factor_ftm_expiry: int | None = None,
        per_user_bal: Literal["enable", "disable"] | None = None,
        wad_worker_count: int | None = None,
        wad_worker_dev_cache: int | None = None,
        wad_csvc_cs_count: int | None = None,
        wad_csvc_db_count: int | None = None,
        wad_source_affinity: Literal["disable", "enable"] | None = None,
        wad_memory_change_granularity: int | None = None,
        login_timestamp: Literal["enable", "disable"] | None = None,
        ip_conflict_detection: Literal["enable", "disable"] | None = None,
        miglogd_children: int | None = None,
        log_daemon_cpu_threshold: int | None = None,
        special_file_23_support: Literal["disable", "enable"] | None = None,
        log_uuid_address: Literal["enable", "disable"] | None = None,
        log_ssl_connection: Literal["enable", "disable"] | None = None,
        gui_rest_api_cache: Literal["enable", "disable"] | None = None,
        rest_api_key_url_query: Literal["enable", "disable"] | None = None,
        arp_max_entry: int | None = None,
        ha_affinity: str | None = None,
        bfd_affinity: str | None = None,
        cmdbsvr_affinity: str | None = None,
        av_affinity: str | None = None,
        wad_affinity: str | None = None,
        ips_affinity: str | None = None,
        miglog_affinity: str | None = None,
        syslog_affinity: str | None = None,
        url_filter_affinity: str | None = None,
        router_affinity: str | None = None,
        ndp_max_entry: int | None = None,
        br_fdb_max_entry: int | None = None,
        max_route_cache_size: int | None = None,
        ipsec_qat_offload: Literal["enable", "disable"] | None = None,
        device_idle_timeout: int | None = None,
        user_device_store_max_devices: int | None = None,
        user_device_store_max_device_mem: int | None = None,
        user_device_store_max_users: int | None = None,
        user_device_store_max_unified_mem: int | None = None,
        gui_device_latitude: str | None = None,
        gui_device_longitude: str | None = None,
        private_data_encryption: Literal["disable", "enable"] | None = None,
        auto_auth_extension_device: Literal["enable", "disable"] | None = None,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = None,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = None,
        gui_date_time_source: Literal["system", "browser"] | None = None,
        igmp_state_limit: int | None = None,
        cloud_communication: Literal["enable", "disable"] | None = None,
        ipsec_ha_seqjump_rate: int | None = None,
        fortitoken_cloud: Literal["enable", "disable"] | None = None,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = None,
        fortitoken_cloud_region: str | None = None,
        fortitoken_cloud_sync_interval: int | None = None,
        faz_disk_buffer_size: int | None = None,
        irq_time_accounting: Literal["auto", "force"] | None = None,
        management_ip: str | None = None,
        management_port: int | None = None,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = None,
        forticonverter_integration: Literal["enable", "disable"] | None = None,
        forticonverter_config_upload: Literal["once", "disable"] | None = None,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = None,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = None,
        geoip_full_db: Literal["enable", "disable"] | None = None,
        early_tcp_npu_session: Literal["enable", "disable"] | None = None,
        npu_neighbor_update: Literal["enable", "disable"] | None = None,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = None,
        interface_subnet_usage: Literal["disable", "enable"] | None = None,
        sflowd_max_children_num: int | None = None,
        fortigslb_integration: Literal["disable", "enable"] | None = None,
        user_history_password_threshold: int | None = None,
        auth_session_auto_backup: Literal["enable", "disable"] | None = None,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = None,
        scim_https_port: int | None = None,
        scim_http_port: int | None = None,
        scim_server_cert: str | None = None,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = None,
        tls_session_cache: Literal["enable", "disable"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/global_ object.

        Configure global attributes.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            language: GUI display language.
            gui_ipv6: Enable/disable IPv6 settings on the GUI.
            gui_replacement_message_groups: Enable/disable replacement message groups on the GUI.
            gui_local_out: Enable/disable Local-out traffic on the GUI.
            gui_certificates: Enable/disable the System > Certificate GUI page, allowing you to add and configure certificates from the GUI.
            gui_custom_language: Enable/disable custom languages in GUI.
            gui_wireless_opensecurity: Enable/disable wireless open security option on the GUI.
            gui_app_detection_sdwan: Enable/disable Allow app-detection based SD-WAN.
            gui_display_hostname: Enable/disable displaying the FortiGate's hostname on the GUI login page.
            gui_fortigate_cloud_sandbox: Enable/disable displaying FortiGate Cloud Sandbox on the GUI.
            gui_firmware_upgrade_warning: Enable/disable the firmware upgrade warning on the GUI.
            gui_forticare_registration_setup_warning: Enable/disable the FortiCare registration setup warning on the GUI.
            gui_auto_upgrade_setup_warning: Enable/disable the automatic patch upgrade setup prompt on the GUI.
            gui_workflow_management: Enable/disable Workflow management features on the GUI.
            gui_cdn_usage: Enable/disable Load GUI static files from a CDN.
            admin_https_ssl_versions: Allowed TLS versions for web administration.
            admin_https_ssl_ciphersuites: Select one or more TLS 1.3 ciphersuites to enable. Does not affect ciphers in TLS 1.2 and below. At least one must be enabled. To disable all, remove TLS1.3 from admin-https-ssl-versions.
            admin_https_ssl_banned_ciphers: Select one or more cipher technologies that cannot be used in GUI HTTPS negotiations. Only applies to TLS 1.2 and below.
            admintimeout: Number of minutes before an idle administrator session times out (1 - 480 minutes (8 hours), default = 5). A shorter idle timeout is more secure.
            admin_console_timeout: Console login timeout that overrides the admin timeout value (15 - 300 seconds, default = 0, which disables the timeout).
            ssd_trim_freq: How often to run SSD Trim (default = weekly). SSD Trim prevents SSD drive data loss by finding and isolating errors.
            ssd_trim_hour: Hour of the day on which to run SSD Trim (0 - 23, default = 1).
            ssd_trim_min: Minute of the hour on which to run SSD Trim (0 - 59, 60 for random).
            ssd_trim_weekday: Day of week to run SSD Trim.
            ssd_trim_date: Date within a month to run ssd trim.
            admin_concurrent: Enable/disable concurrent administrator logins. Use policy-auth-concurrent for firewall authenticated users.
            admin_lockout_threshold: Number of failed login attempts before an administrator account is locked out for the admin-lockout-duration.
            admin_lockout_duration: Amount of time in seconds that an administrator account is locked out after reaching the admin-lockout-threshold for repeated failed login attempts.
            refresh: Statistics refresh interval second(s) in GUI.
            interval: Dead gateway detection interval.
            failtime: Fail-time for server lost.
            purdue_level: Purdue Level of this FortiGate.
            daily_restart: Enable/disable daily restart of FortiGate unit. Use the restart-time option to set the time of day for the restart.
            restart_time: Daily restart time (hh:mm).
            wad_restart_mode: WAD worker restart mode (default = none).
            wad_restart_start_time: WAD workers daily restart time (hh:mm).
            wad_restart_end_time: WAD workers daily restart end time (hh:mm).
            wad_p2s_max_body_size: Maximum size of the body of the local out HTTP request (1 - 32 Mbytes, default = 4).
            radius_port: RADIUS service port number.
            speedtestd_server_port: Speedtest server port number.
            speedtestd_ctrl_port: Speedtest server controller port number.
            admin_login_max: Maximum number of administrators who can be logged in at the same time (1 - 100, default = 100).
            remoteauthtimeout: Number of seconds that the FortiGate waits for responses from remote RADIUS, LDAP, or TACACS+ authentication servers. (1-300 sec, default = 5).
            ldapconntimeout: Global timeout for connections with remote LDAP servers in milliseconds (1 - 300000, default 500).
            batch_cmdb: Enable/disable batch mode, allowing you to enter a series of CLI commands that will execute as a group once they are loaded.
            multi_factor_authentication: Enforce all login methods to require an additional authentication factor (default = optional).
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default = TLSv1.2).
            autorun_log_fsck: Enable/disable automatic log partition check after ungraceful shutdown.
            timezone: Timezone database name. Enter ? to view the list of timezone.
            traffic_priority: Choose Type of Service (ToS) or Differentiated Services Code Point (DSCP) for traffic prioritization in traffic shaping.
            traffic_priority_level: Default system-wide level of priority for traffic prioritization.
            quic_congestion_control_algo: QUIC congestion control algorithm (default = cubic).
            quic_max_datagram_size: Maximum transmit datagram size (1200 - 1500, default = 1500).
            quic_udp_payload_size_shaping_per_cid: Enable/disable UDP payload size shaping per connection ID (default = enable).
            quic_ack_thresold: Maximum number of unacknowledged packets before sending ACK (2 - 5, default = 3).
            quic_pmtud: Enable/disable path MTU discovery (default = enable).
            quic_tls_handshake_timeout: Time-to-live (TTL) for TLS handshake in seconds (1 - 60, default = 5).
            anti_replay: Level of checking for packet replay and TCP sequence checking.
            send_pmtu_icmp: Enable/disable sending of path maximum transmission unit (PMTU) - ICMP destination unreachable packet and to support PMTUD protocol on your network to reduce fragmentation of packets.
            honor_df: Enable/disable honoring of Don't-Fragment (DF) flag.
            pmtu_discovery: Enable/disable path MTU discovery.
            revision_image_auto_backup: Enable/disable back-up of the latest image revision after the firmware is upgraded.
            revision_backup_on_logout: Enable/disable back-up of the latest configuration revision when an administrator logs out of the CLI or GUI.
            management_vdom: Management virtual domain name.
            hostname: FortiGate unit's hostname. Most models will truncate names longer than 24 characters. Some models support hostnames up to 35 characters.
            alias: Alias for your FortiGate unit.
            strong_crypto: Enable to use strong encryption and only allow strong ciphers and digest for HTTPS/SSH/TLS/SSL functions.
            ssl_static_key_ciphers: Enable/disable static key ciphers in SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256, AES256-SHA256).
            snat_route_change: Enable/disable the ability to change the source NAT route.
            ipv6_snat_route_change: Enable/disable the ability to change the IPv6 source NAT route.
            speedtest_server: Enable/disable speed test server.
            cli_audit_log: Enable/disable CLI audit log.
            dh_params: Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols.
            fds_statistics: Enable/disable sending IPS, Application Control, and AntiVirus data to FortiGuard. This data is used to improve FortiGuard services and is not shared with external parties and is protected by Fortinet's privacy policy.
            fds_statistics_period: FortiGuard statistics collection period in minutes. (1 - 1440 min (1 min to 24 hours), default = 60).
            tcp_option: Enable SACK, timestamp and MSS TCP options.
            lldp_transmission: Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP) reception.
            proxy_auth_timeout: Authentication timeout in minutes for authenticated users (1 - 10000 min, default = 10).
            proxy_keep_alive_mode: Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was authenticated.
            proxy_re_authentication_time: The time limit that users must re-authenticate if proxy-keep-alive-mode is set to re-authenticate (1  - 86400 sec, default=30s.
            proxy_auth_lifetime: Enable/disable authenticated users lifetime control. This is a cap on the total time a proxy user can be authenticated for after which re-authentication will take place.
            proxy_auth_lifetime_timeout: Lifetime timeout in minutes for authenticated users (5  - 65535 min, default=480 (8 hours)).
            proxy_resource_mode: Enable/disable use of the maximum memory usage on the FortiGate unit's proxy processing of resources, such as block lists, allow lists, and external resources.
            proxy_cert_use_mgmt_vdom: Enable/disable using management VDOM to send requests.
            sys_perf_log_interval: Time in minutes between updates of performance statistics logging. (1 - 15 min, default = 5, 0 = disabled).
            check_protocol_header: Level of checking performed on protocol headers. Strict checking is more thorough but may affect performance. Loose checking is OK in most cases.
            vip_arp_range: Controls the number of ARPs that the FortiGate sends for a Virtual IP (VIP) address range.
            reset_sessionless_tcp: Action to perform if the FortiGate receives a TCP packet but cannot find a corresponding session in its session table. NAT/Route mode only.
            allow_traffic_redirect: Disable to prevent traffic with same local ingress and egress interface from being forwarded without policy check.
            ipv6_allow_traffic_redirect: Disable to prevent IPv6 traffic with same local ingress and egress interface from being forwarded without policy check.
            strict_dirty_session_check: Enable to check the session against the original policy when revalidating. This can prevent dropping of redirected sessions when web-filtering and authentication are enabled together. If this option is enabled, the FortiGate unit deletes a session if a routing or policy change causes the session to no longer match the policy that originally allowed the session.
            tcp_halfclose_timer: Number of seconds the FortiGate unit should wait to close a session after one peer has sent a FIN packet but the other has not responded (1 - 86400 sec (1 day), default = 120).
            tcp_halfopen_timer: Number of seconds the FortiGate unit should wait to close a session after one peer has sent an open session packet but the other has not responded (1 - 86400 sec (1 day), default = 10).
            tcp_timewait_timer: Length of the TCP TIME-WAIT state in seconds (1 - 300 sec, default = 1).
            tcp_rst_timer: Length of the TCP CLOSE state in seconds (5 - 300 sec, default = 5).
            udp_idle_timer: UDP connection session timeout. This command can be useful in managing CPU and memory resources (1 - 86400 seconds (1 day), default = 60).
            block_session_timer: Duration in seconds for blocked sessions (1 - 300 sec  (5 minutes), default = 30).
            ip_src_port_range: IP source port range used for traffic originating from the FortiGate unit.
            pre_login_banner: Enable/disable displaying the administrator access disclaimer message on the login page before an administrator logs in.
            post_login_banner: Enable/disable displaying the administrator access disclaimer message after an administrator successfully logs in.
            tftp: Enable/disable TFTP.
            av_failopen: Set the action to take if the FortiGate is running low on memory or the proxy connection limit has been reached.
            av_failopen_session: When enabled and a proxy for a protocol runs out of room in its session table, that protocol goes into failopen mode and enacts the action specified by av-failopen.
            memory_use_threshold_extreme: Threshold at which memory usage is considered extreme (new sessions are dropped) (% of total RAM, default = 95).
            memory_use_threshold_red: Threshold at which memory usage forces the FortiGate to enter conserve mode (% of total RAM, default = 88).
            memory_use_threshold_green: Threshold at which memory usage forces the FortiGate to exit conserve mode (% of total RAM, default = 82).
            ip_fragment_mem_thresholds: Maximum memory (MB) used to reassemble IPv4/IPv6 fragments.
            ip_fragment_timeout: Timeout value in seconds for any fragment not being reassembled
            ipv6_fragment_timeout: Timeout value in seconds for any IPv6 fragment not being reassembled
            cpu_use_threshold: Threshold at which CPU usage is reported (% of total CPU, default = 90).
            log_single_cpu_high: Enable/disable logging the event of a single CPU core reaching CPU usage threshold.
            check_reset_range: Configure ICMP error message verification. You can either apply strict RST range checking or disable it.
            upgrade_report: Enable/disable the generation of an upgrade report when upgrading the firmware.
            admin_port: Administrative access port for HTTP. (1 - 65535, default = 80).
            admin_sport: Administrative access port for HTTPS. (1 - 65535, default = 443).
            admin_host: Administrative host for HTTP and HTTPS. When set, will be used in lieu of the client's Host header for any redirection.
            admin_https_redirect: Enable/disable redirection of HTTP administration access to HTTPS.
            admin_hsts_max_age: HTTPS Strict-Transport-Security header max-age in seconds. A value of 0 will reset any HSTS records in the browser.When admin-https-redirect is disabled the header max-age will be 0.
            admin_ssh_password: Enable/disable password authentication for SSH admin access.
            admin_restrict_local: Enable/disable local admin authentication restriction when remote authenticator is up and running (default = disable).
            admin_ssh_port: Administrative access port for SSH. (1 - 65535, default = 22).
            admin_ssh_grace_time: Maximum time in seconds permitted between making an SSH connection to the FortiGate unit and authenticating (10 - 3600 sec (1 hour), default 120).
            admin_ssh_v1: Enable/disable SSH v1 compatibility.
            admin_telnet: Enable/disable TELNET service.
            admin_telnet_port: Administrative access port for TELNET. (1 - 65535, default = 23).
            admin_forticloud_sso_login: Enable/disable FortiCloud admin login via SSO.
            admin_forticloud_sso_default_profile: Override access profile.
            default_service_source_port: Default service source port range (default = 1 - 65535).
            admin_server_cert: Server certificate that the FortiGate uses for HTTPS administrative connections.
            admin_https_pki_required: Enable/disable admin login method. Enable to force administrators to provide a valid certificate to log in if PKI is enabled. Disable to allow administrators to log in with a certificate or password.
            wifi_certificate: Certificate to use for WiFi authentication.
            dhcp_lease_backup_interval: DHCP leases backup interval in seconds (10 - 3600, default = 60).
            wifi_ca_certificate: CA certificate that verifies the WiFi certificate.
            auth_http_port: User authentication HTTP port. (1 - 65535, default = 1000).
            auth_https_port: User authentication HTTPS port. (1 - 65535, default = 1003).
            auth_ike_saml_port: User IKE SAML authentication port (0 - 65535, default = 1001).
            auth_keepalive: Enable to prevent user authentication sessions from timing out when idle.
            policy_auth_concurrent: Number of concurrent firewall use logins from the same user (1 - 100, default = 0 means no limit).
            auth_session_limit: Action to take when the number of allowed user authenticated sessions is reached.
            auth_cert: Server certificate that the FortiGate uses for HTTPS firewall authentication connections.
            clt_cert_req: Enable/disable requiring administrators to have a client certificate to log into the GUI using HTTPS.
            fortiservice_port: FortiService port (1 - 65535, default = 8013). Used by FortiClient endpoint compliance. Older versions of FortiClient used a different port.
            cfg_save: Configuration file save mode for CLI changes.
            cfg_revert_timeout: Time-out for reverting to the last saved configuration. (10 - 4294967295 seconds, default = 600).
            reboot_upon_config_restore: Enable/disable reboot of system upon restoring configuration.
            admin_scp: Enable/disable SCP support for system configuration backup, restore, and firmware file upload.
            wireless_controller: Enable/disable the wireless controller feature to use the FortiGate unit to manage FortiAPs.
            wireless_controller_port: Port used for the control channel in wireless controller mode (wireless-mode is ac). The data channel port is the control channel port number plus one (1024 - 49150, default = 5246).
            fortiextender_data_port: FortiExtender data port (1024 - 49150, default = 25246).
            fortiextender: Enable/disable FortiExtender.
            extender_controller_reserved_network: Configure reserved network subnet for managed LAN extension FortiExtender units. This is available when the FortiExtender daemon is running.
            fortiextender_discovery_lockdown: Enable/disable FortiExtender CAPWAP lockdown.
            fortiextender_vlan_mode: Enable/disable FortiExtender VLAN mode.
            fortiextender_provision_on_authorization: Enable/disable automatic provisioning of latest FortiExtender firmware on authorization.
            switch_controller: Enable/disable switch controller feature. Switch controller allows you to manage FortiSwitch from the FortiGate itself.
            switch_controller_reserved_network: Configure reserved network subnet for managed switches. This is available when the switch controller is enabled.
            dnsproxy_worker_count: DNS proxy worker count. For a FortiGate with multiple logical CPUs, you can set the DNS process number from 1 to the number of logical CPUs.
            url_filter_count: URL filter daemon count.
            httpd_max_worker_count: Maximum number of simultaneous HTTP requests that will be served. This number may affect GUI and REST API performance (0 - 128, default = 0 means let system decide).
            proxy_worker_count: Proxy worker count.
            scanunit_count: Number of scanunits. The range and the default depend on the number of CPUs. Only available on FortiGate units with multiple CPUs.
            fgd_alert_subscription: Type of alert to retrieve from FortiGuard.
            ipv6_accept_dad: Enable/disable acceptance of IPv6 Duplicate Address Detection (DAD).
            ipv6_allow_anycast_probe: Enable/disable IPv6 address probe through Anycast.
            ipv6_allow_multicast_probe: Enable/disable IPv6 address probe through Multicast.
            ipv6_allow_local_in_silent_drop: Enable/disable silent drop of IPv6 local-in traffic.
            csr_ca_attribute: Enable/disable the CA attribute in certificates. Some CA servers reject CSRs that have the CA attribute.
            wimax_4g_usb: Enable/disable comparability with WiMAX 4G USB devices.
            cert_chain_max: Maximum number of certificates that can be traversed in a certificate chain.
            sslvpn_max_worker_count: Maximum number of Agentless VPN processes. Upper limit for this value is the number of CPUs and depends on the model. Default value of zero means the sslvpnd daemon decides the number of worker processes.
            sslvpn_affinity: Agentless VPN CPU affinity.
            sslvpn_web_mode: Enable/disable Agentless VPN web mode.
            two_factor_ftk_expiry: FortiToken authentication session timeout (60 - 600 sec (10 minutes), default = 60).
            two_factor_email_expiry: Email-based two-factor authentication session timeout (30 - 300 seconds (5 minutes), default = 60).
            two_factor_sms_expiry: SMS-based two-factor authentication session timeout (30 - 300 sec, default = 60).
            two_factor_fac_expiry: FortiAuthenticator token authentication session timeout (10 - 3600 seconds (1 hour), default = 60).
            two_factor_ftm_expiry: FortiToken Mobile session timeout (1 - 168 hours (7 days), default = 72).
            per_user_bal: Enable/disable per-user block/allow list filter.
            wad_worker_count: Number of explicit proxy WAN optimization daemon (WAD) processes. By default WAN optimization, explicit proxy, and web caching is handled by all of the CPU cores in a FortiGate unit.
            wad_worker_dev_cache: Number of cached devices for each ZTNA proxy worker. The default value is tuned by memory consumption. Set the option to 0 to disable the cache.
            wad_csvc_cs_count: Number of concurrent WAD-cache-service object-cache processes.
            wad_csvc_db_count: Number of concurrent WAD-cache-service byte-cache processes.
            wad_source_affinity: Enable/disable dispatching traffic to WAD workers based on source affinity.
            wad_memory_change_granularity: Minimum percentage change in system memory usage detected by the wad daemon prior to adjusting TCP window size for any active connection.
            login_timestamp: Enable/disable login time recording.
            ip_conflict_detection: Enable/disable logging of IPv4 address conflict detection.
            miglogd_children: Number of logging (miglogd) processes to be allowed to run. Higher number can reduce performance; lower number can slow log processing time. 
            log_daemon_cpu_threshold: Configure syslog daemon process spawning threshold. Use a percentage threshold of syslogd CPU usage (1 - 99) or set to zero to use dynamic scheduling based on the number of packets in the syslogd queue (default = 0).
            special_file_23_support: Enable/disable detection of those special format files when using Data Loss Prevention.
            log_uuid_address: Enable/disable insertion of address UUIDs to traffic logs.
            log_ssl_connection: Enable/disable logging of SSL connection events.
            gui_rest_api_cache: Enable/disable REST API result caching on FortiGate.
            rest_api_key_url_query: Enable/disable support for passing REST API keys through URL query parameters.
            arp_max_entry: Maximum number of dynamically learned MAC addresses that can be added to the ARP table (131072 - 2147483647, default = 131072).
            ha_affinity: Affinity setting for HA daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            bfd_affinity: Affinity setting for BFD daemon (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            cmdbsvr_affinity: Affinity setting for cmdbsvr (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            av_affinity: Affinity setting for AV scanning (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            wad_affinity: Affinity setting for wad (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            ips_affinity: Affinity setting for IPS (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx; allowed CPUs must be less than total number of IPS engine daemons).
            miglog_affinity: Affinity setting for logging (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            syslog_affinity: Affinity setting for syslog (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            url_filter_affinity: URL filter CPU affinity.
            router_affinity: Affinity setting for BFD/VRRP/BGP/OSPF daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
            ndp_max_entry: Maximum number of NDP table entries (set to 65,536 or higher; if set to 0, kernel holds 65,536 entries).
            br_fdb_max_entry: Maximum number of bridge forwarding database (FDB) entries.
            max_route_cache_size: Maximum number of IP route cache entries (0 - 2147483647).
            ipsec_qat_offload: Enable/disable QAT offloading (Intel QuickAssist) for IPsec VPN traffic. QuickAssist can accelerate IPsec encryption and decryption.
            device_idle_timeout: Time in seconds that a device must be idle to automatically log the device user out. (30 - 31536000 sec (30 sec to 1 year), default = 300).
            user_device_store_max_devices: Maximum number of devices allowed in user device store.
            user_device_store_max_device_mem: Maximum percentage of total system memory allowed to be used for devices in the user device store.
            user_device_store_max_users: Maximum number of users allowed in user device store.
            user_device_store_max_unified_mem: Maximum unified memory allowed in user device store.
            gui_device_latitude: Add the latitude of the location of this FortiGate to position it on the Threat Map.
            gui_device_longitude: Add the longitude of the location of this FortiGate to position it on the Threat Map.
            private_data_encryption: Enable/disable private data encryption using an AES 128-bit key or passpharse.
            auto_auth_extension_device: Enable/disable automatic authorization of dedicated Fortinet extension devices.
            gui_theme: Color scheme for the administration GUI.
            gui_date_format: Default date format used throughout GUI.
            gui_date_time_source: Source from which the FortiGate GUI uses to display date and time entries.
            igmp_state_limit: Maximum number of IGMP memberships (96 - 64000, default = 3200).
            cloud_communication: Enable/disable all cloud communication.
            ipsec_ha_seqjump_rate: ESP jump ahead rate (1G - 10G pps equivalent).
            fortitoken_cloud: Enable/disable FortiToken Cloud service.
            fortitoken_cloud_push_status: Enable/disable FTM push service of FortiToken Cloud.
            fortitoken_cloud_region: Region domain of FortiToken Cloud(unset to non-region).
            fortitoken_cloud_sync_interval: Interval in which to clean up remote users in FortiToken Cloud (0 - 336 hours (14 days), default = 24, disable = 0).
            faz_disk_buffer_size: Maximum disk buffer size to temporarily store logs destined for FortiAnalyzer. To be used in the event that FortiAnalyzer is unavailable.
            irq_time_accounting: Configure CPU IRQ time accounting mode.
            management_ip: Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric.
            management_port: Overriding port for management connection (Overrides admin port).
            management_port_use_admin_sport: Enable/disable use of the admin-sport setting for the management port. If disabled, FortiGate will allow user to specify management-port.
            forticonverter_integration: Enable/disable FortiConverter integration service.
            forticonverter_config_upload: Enable/disable config upload to FortiConverter.
            internet_service_database: Configure which Internet Service database size to download from FortiGuard and use.
            internet_service_download_list: Configure which on-demand Internet Service IDs are to be downloaded.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            geoip_full_db: When enabled, the full geographic database will be loaded into the kernel which enables geographic information in traffic logs - required for FortiView countries. Disabling this option will conserve memory.
            early_tcp_npu_session: Enable/disable early TCP NPU session.
            npu_neighbor_update: Enable/disable sending of ARP/ICMP6 probing packets to update neighbors for offloaded sessions.
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee packet order of 3-way handshake.
            interface_subnet_usage: Enable/disable allowing use of interface-subnet setting in firewall addresses (default = enable).
            sflowd_max_children_num: Maximum number of sflowd child processes allowed to run.
            fortigslb_integration: Enable/disable integration with the FortiGSLB cloud service.
            user_history_password_threshold: Maximum number of previous passwords saved per admin/user (3 - 15, default = 3).
            auth_session_auto_backup: Enable/disable automatic and periodic backup of authentication sessions (default = disable). Sessions are restored upon bootup.
            auth_session_auto_backup_interval: Configure automatic authentication session backup interval (default = 15min).
            scim_https_port: SCIM port (0 - 65535, default = 44559).
            scim_http_port: SCIM http port (0 - 65535, default = 44558).
            scim_server_cert: Server certificate that the FortiGate uses for SCIM connections.
            application_bandwidth_tracking: Enable/disable application bandwidth tracking.
            tls_session_cache: Enable/disable TLS session cache.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if internet_service_download_list is not None:
            internet_service_download_list = normalize_table_field(
                internet_service_download_list,
                mkey="id",
                required_fields=['id'],
                field_name="internet_service_download_list",
                example="[{'id': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            language=language,
            gui_ipv6=gui_ipv6,
            gui_replacement_message_groups=gui_replacement_message_groups,
            gui_local_out=gui_local_out,
            gui_certificates=gui_certificates,
            gui_custom_language=gui_custom_language,
            gui_wireless_opensecurity=gui_wireless_opensecurity,
            gui_app_detection_sdwan=gui_app_detection_sdwan,
            gui_display_hostname=gui_display_hostname,
            gui_fortigate_cloud_sandbox=gui_fortigate_cloud_sandbox,
            gui_firmware_upgrade_warning=gui_firmware_upgrade_warning,
            gui_forticare_registration_setup_warning=gui_forticare_registration_setup_warning,
            gui_auto_upgrade_setup_warning=gui_auto_upgrade_setup_warning,
            gui_workflow_management=gui_workflow_management,
            gui_cdn_usage=gui_cdn_usage,
            admin_https_ssl_versions=admin_https_ssl_versions,
            admin_https_ssl_ciphersuites=admin_https_ssl_ciphersuites,
            admin_https_ssl_banned_ciphers=admin_https_ssl_banned_ciphers,
            admintimeout=admintimeout,
            admin_console_timeout=admin_console_timeout,
            ssd_trim_freq=ssd_trim_freq,
            ssd_trim_hour=ssd_trim_hour,
            ssd_trim_min=ssd_trim_min,
            ssd_trim_weekday=ssd_trim_weekday,
            ssd_trim_date=ssd_trim_date,
            admin_concurrent=admin_concurrent,
            admin_lockout_threshold=admin_lockout_threshold,
            admin_lockout_duration=admin_lockout_duration,
            refresh=refresh,
            interval=interval,
            failtime=failtime,
            purdue_level=purdue_level,
            daily_restart=daily_restart,
            restart_time=restart_time,
            wad_restart_mode=wad_restart_mode,
            wad_restart_start_time=wad_restart_start_time,
            wad_restart_end_time=wad_restart_end_time,
            wad_p2s_max_body_size=wad_p2s_max_body_size,
            radius_port=radius_port,
            speedtestd_server_port=speedtestd_server_port,
            speedtestd_ctrl_port=speedtestd_ctrl_port,
            admin_login_max=admin_login_max,
            remoteauthtimeout=remoteauthtimeout,
            ldapconntimeout=ldapconntimeout,
            batch_cmdb=batch_cmdb,
            multi_factor_authentication=multi_factor_authentication,
            ssl_min_proto_version=ssl_min_proto_version,
            autorun_log_fsck=autorun_log_fsck,
            timezone=timezone,
            traffic_priority=traffic_priority,
            traffic_priority_level=traffic_priority_level,
            quic_congestion_control_algo=quic_congestion_control_algo,
            quic_max_datagram_size=quic_max_datagram_size,
            quic_udp_payload_size_shaping_per_cid=quic_udp_payload_size_shaping_per_cid,
            quic_ack_thresold=quic_ack_thresold,
            quic_pmtud=quic_pmtud,
            quic_tls_handshake_timeout=quic_tls_handshake_timeout,
            anti_replay=anti_replay,
            send_pmtu_icmp=send_pmtu_icmp,
            honor_df=honor_df,
            pmtu_discovery=pmtu_discovery,
            revision_image_auto_backup=revision_image_auto_backup,
            revision_backup_on_logout=revision_backup_on_logout,
            management_vdom=management_vdom,
            hostname=hostname,
            alias=alias,
            strong_crypto=strong_crypto,
            ssl_static_key_ciphers=ssl_static_key_ciphers,
            snat_route_change=snat_route_change,
            ipv6_snat_route_change=ipv6_snat_route_change,
            speedtest_server=speedtest_server,
            cli_audit_log=cli_audit_log,
            dh_params=dh_params,
            fds_statistics=fds_statistics,
            fds_statistics_period=fds_statistics_period,
            tcp_option=tcp_option,
            lldp_transmission=lldp_transmission,
            lldp_reception=lldp_reception,
            proxy_auth_timeout=proxy_auth_timeout,
            proxy_keep_alive_mode=proxy_keep_alive_mode,
            proxy_re_authentication_time=proxy_re_authentication_time,
            proxy_auth_lifetime=proxy_auth_lifetime,
            proxy_auth_lifetime_timeout=proxy_auth_lifetime_timeout,
            proxy_resource_mode=proxy_resource_mode,
            proxy_cert_use_mgmt_vdom=proxy_cert_use_mgmt_vdom,
            sys_perf_log_interval=sys_perf_log_interval,
            check_protocol_header=check_protocol_header,
            vip_arp_range=vip_arp_range,
            reset_sessionless_tcp=reset_sessionless_tcp,
            allow_traffic_redirect=allow_traffic_redirect,
            ipv6_allow_traffic_redirect=ipv6_allow_traffic_redirect,
            strict_dirty_session_check=strict_dirty_session_check,
            tcp_halfclose_timer=tcp_halfclose_timer,
            tcp_halfopen_timer=tcp_halfopen_timer,
            tcp_timewait_timer=tcp_timewait_timer,
            tcp_rst_timer=tcp_rst_timer,
            udp_idle_timer=udp_idle_timer,
            block_session_timer=block_session_timer,
            ip_src_port_range=ip_src_port_range,
            pre_login_banner=pre_login_banner,
            post_login_banner=post_login_banner,
            tftp=tftp,
            av_failopen=av_failopen,
            av_failopen_session=av_failopen_session,
            memory_use_threshold_extreme=memory_use_threshold_extreme,
            memory_use_threshold_red=memory_use_threshold_red,
            memory_use_threshold_green=memory_use_threshold_green,
            ip_fragment_mem_thresholds=ip_fragment_mem_thresholds,
            ip_fragment_timeout=ip_fragment_timeout,
            ipv6_fragment_timeout=ipv6_fragment_timeout,
            cpu_use_threshold=cpu_use_threshold,
            log_single_cpu_high=log_single_cpu_high,
            check_reset_range=check_reset_range,
            upgrade_report=upgrade_report,
            admin_port=admin_port,
            admin_sport=admin_sport,
            admin_host=admin_host,
            admin_https_redirect=admin_https_redirect,
            admin_hsts_max_age=admin_hsts_max_age,
            admin_ssh_password=admin_ssh_password,
            admin_restrict_local=admin_restrict_local,
            admin_ssh_port=admin_ssh_port,
            admin_ssh_grace_time=admin_ssh_grace_time,
            admin_ssh_v1=admin_ssh_v1,
            admin_telnet=admin_telnet,
            admin_telnet_port=admin_telnet_port,
            admin_forticloud_sso_login=admin_forticloud_sso_login,
            admin_forticloud_sso_default_profile=admin_forticloud_sso_default_profile,
            default_service_source_port=default_service_source_port,
            admin_server_cert=admin_server_cert,
            admin_https_pki_required=admin_https_pki_required,
            wifi_certificate=wifi_certificate,
            dhcp_lease_backup_interval=dhcp_lease_backup_interval,
            wifi_ca_certificate=wifi_ca_certificate,
            auth_http_port=auth_http_port,
            auth_https_port=auth_https_port,
            auth_ike_saml_port=auth_ike_saml_port,
            auth_keepalive=auth_keepalive,
            policy_auth_concurrent=policy_auth_concurrent,
            auth_session_limit=auth_session_limit,
            auth_cert=auth_cert,
            clt_cert_req=clt_cert_req,
            fortiservice_port=fortiservice_port,
            cfg_save=cfg_save,
            cfg_revert_timeout=cfg_revert_timeout,
            reboot_upon_config_restore=reboot_upon_config_restore,
            admin_scp=admin_scp,
            wireless_controller=wireless_controller,
            wireless_controller_port=wireless_controller_port,
            fortiextender_data_port=fortiextender_data_port,
            fortiextender=fortiextender,
            extender_controller_reserved_network=extender_controller_reserved_network,
            fortiextender_discovery_lockdown=fortiextender_discovery_lockdown,
            fortiextender_vlan_mode=fortiextender_vlan_mode,
            fortiextender_provision_on_authorization=fortiextender_provision_on_authorization,
            switch_controller=switch_controller,
            switch_controller_reserved_network=switch_controller_reserved_network,
            dnsproxy_worker_count=dnsproxy_worker_count,
            url_filter_count=url_filter_count,
            httpd_max_worker_count=httpd_max_worker_count,
            proxy_worker_count=proxy_worker_count,
            scanunit_count=scanunit_count,
            fgd_alert_subscription=fgd_alert_subscription,
            ipv6_accept_dad=ipv6_accept_dad,
            ipv6_allow_anycast_probe=ipv6_allow_anycast_probe,
            ipv6_allow_multicast_probe=ipv6_allow_multicast_probe,
            ipv6_allow_local_in_silent_drop=ipv6_allow_local_in_silent_drop,
            csr_ca_attribute=csr_ca_attribute,
            wimax_4g_usb=wimax_4g_usb,
            cert_chain_max=cert_chain_max,
            sslvpn_max_worker_count=sslvpn_max_worker_count,
            sslvpn_affinity=sslvpn_affinity,
            sslvpn_web_mode=sslvpn_web_mode,
            two_factor_ftk_expiry=two_factor_ftk_expiry,
            two_factor_email_expiry=two_factor_email_expiry,
            two_factor_sms_expiry=two_factor_sms_expiry,
            two_factor_fac_expiry=two_factor_fac_expiry,
            two_factor_ftm_expiry=two_factor_ftm_expiry,
            per_user_bal=per_user_bal,
            wad_worker_count=wad_worker_count,
            wad_worker_dev_cache=wad_worker_dev_cache,
            wad_csvc_cs_count=wad_csvc_cs_count,
            wad_csvc_db_count=wad_csvc_db_count,
            wad_source_affinity=wad_source_affinity,
            wad_memory_change_granularity=wad_memory_change_granularity,
            login_timestamp=login_timestamp,
            ip_conflict_detection=ip_conflict_detection,
            miglogd_children=miglogd_children,
            log_daemon_cpu_threshold=log_daemon_cpu_threshold,
            special_file_23_support=special_file_23_support,
            log_uuid_address=log_uuid_address,
            log_ssl_connection=log_ssl_connection,
            gui_rest_api_cache=gui_rest_api_cache,
            rest_api_key_url_query=rest_api_key_url_query,
            arp_max_entry=arp_max_entry,
            ha_affinity=ha_affinity,
            bfd_affinity=bfd_affinity,
            cmdbsvr_affinity=cmdbsvr_affinity,
            av_affinity=av_affinity,
            wad_affinity=wad_affinity,
            ips_affinity=ips_affinity,
            miglog_affinity=miglog_affinity,
            syslog_affinity=syslog_affinity,
            url_filter_affinity=url_filter_affinity,
            router_affinity=router_affinity,
            ndp_max_entry=ndp_max_entry,
            br_fdb_max_entry=br_fdb_max_entry,
            max_route_cache_size=max_route_cache_size,
            ipsec_qat_offload=ipsec_qat_offload,
            device_idle_timeout=device_idle_timeout,
            user_device_store_max_devices=user_device_store_max_devices,
            user_device_store_max_device_mem=user_device_store_max_device_mem,
            user_device_store_max_users=user_device_store_max_users,
            user_device_store_max_unified_mem=user_device_store_max_unified_mem,
            gui_device_latitude=gui_device_latitude,
            gui_device_longitude=gui_device_longitude,
            private_data_encryption=private_data_encryption,
            auto_auth_extension_device=auto_auth_extension_device,
            gui_theme=gui_theme,
            gui_date_format=gui_date_format,
            gui_date_time_source=gui_date_time_source,
            igmp_state_limit=igmp_state_limit,
            cloud_communication=cloud_communication,
            ipsec_ha_seqjump_rate=ipsec_ha_seqjump_rate,
            fortitoken_cloud=fortitoken_cloud,
            fortitoken_cloud_push_status=fortitoken_cloud_push_status,
            fortitoken_cloud_region=fortitoken_cloud_region,
            fortitoken_cloud_sync_interval=fortitoken_cloud_sync_interval,
            faz_disk_buffer_size=faz_disk_buffer_size,
            irq_time_accounting=irq_time_accounting,
            management_ip=management_ip,
            management_port=management_port,
            management_port_use_admin_sport=management_port_use_admin_sport,
            forticonverter_integration=forticonverter_integration,
            forticonverter_config_upload=forticonverter_config_upload,
            internet_service_database=internet_service_database,
            internet_service_download_list=internet_service_download_list,
            geoip_full_db=geoip_full_db,
            early_tcp_npu_session=early_tcp_npu_session,
            npu_neighbor_update=npu_neighbor_update,
            delay_tcp_npu_session=delay_tcp_npu_session,
            interface_subnet_usage=interface_subnet_usage,
            sflowd_max_children_num=sflowd_max_children_num,
            fortigslb_integration=fortigslb_integration,
            user_history_password_threshold=user_history_password_threshold,
            auth_session_auto_backup=auth_session_auto_backup,
            auth_session_auto_backup_interval=auth_session_auto_backup_interval,
            scim_https_port=scim_https_port,
            scim_http_port=scim_http_port,
            scim_server_cert=scim_server_cert,
            application_bandwidth_tracking=application_bandwidth_tracking,
            tls_session_cache=tls_session_cache,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/global_",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/system/global"

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
        Move system/global_ object to a new position.
        
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
            >>> fgt.api.cmdb.system_global_.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/global",
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
        Clone system/global_ object.
        
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
            >>> fgt.api.cmdb.system_global_.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/global",
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
        Check if system/global_ object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_global_.exists(name="myobj"):
            ...     fgt.api.cmdb.system_global_.post(payload_dict=data)
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/system/global_"
        endpoint = f"{endpoint}/{quote_path_param(name)}"
        
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


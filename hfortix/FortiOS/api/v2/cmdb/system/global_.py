"""
FortiOS CMDB - Cmdb System Global

Configuration endpoint for managing cmdb system global objects.

API Endpoints:
    GET    /cmdb/system/global_
    PUT    /cmdb/system/global_/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.global_.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.global_.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.global_.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.global_.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.global_.delete(name="item_name")

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


class Global:
    """
    Global Operations.

    Provides CRUD operations for FortiOS global configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Global endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
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
        endpoint = "/system/global"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        language: str | None = None,
        gui_allow_incompatible_fabric_fgt: str | None = None,
        gui_ipv6: str | None = None,
        gui_replacement_message_groups: str | None = None,
        gui_local_out: str | None = None,
        gui_certificates: str | None = None,
        gui_custom_language: str | None = None,
        gui_wireless_opensecurity: str | None = None,
        gui_app_detection_sdwan: str | None = None,
        gui_display_hostname: str | None = None,
        gui_fortigate_cloud_sandbox: str | None = None,
        gui_firmware_upgrade_warning: str | None = None,
        gui_forticare_registration_setup_warning: str | None = None,
        gui_auto_upgrade_setup_warning: str | None = None,
        gui_workflow_management: str | None = None,
        gui_cdn_usage: str | None = None,
        admin_https_ssl_versions: str | None = None,
        admin_https_ssl_ciphersuites: str | None = None,
        admin_https_ssl_banned_ciphers: str | None = None,
        admintimeout: int | None = None,
        admin_console_timeout: int | None = None,
        ssd_trim_freq: str | None = None,
        ssd_trim_hour: int | None = None,
        ssd_trim_min: int | None = None,
        ssd_trim_weekday: str | None = None,
        ssd_trim_date: int | None = None,
        admin_concurrent: str | None = None,
        admin_lockout_threshold: int | None = None,
        admin_lockout_duration: int | None = None,
        refresh: int | None = None,
        interval: int | None = None,
        failtime: int | None = None,
        purdue_level: str | None = None,
        daily_restart: str | None = None,
        restart_time: str | None = None,
        wad_restart_mode: str | None = None,
        wad_restart_start_time: str | None = None,
        wad_restart_end_time: str | None = None,
        wad_p2s_max_body_size: int | None = None,
        radius_port: int | None = None,
        speedtestd_server_port: int | None = None,
        speedtestd_ctrl_port: int | None = None,
        admin_login_max: int | None = None,
        remoteauthtimeout: int | None = None,
        ldapconntimeout: int | None = None,
        batch_cmdb: str | None = None,
        multi_factor_authentication: str | None = None,
        ssl_min_proto_version: str | None = None,
        autorun_log_fsck: str | None = None,
        timezone: str | None = None,
        traffic_priority: str | None = None,
        traffic_priority_level: str | None = None,
        quic_congestion_control_algo: str | None = None,
        quic_max_datagram_size: int | None = None,
        quic_udp_payload_size_shaping_per_cid: str | None = None,
        quic_ack_thresold: int | None = None,
        quic_pmtud: str | None = None,
        quic_tls_handshake_timeout: int | None = None,
        anti_replay: str | None = None,
        send_pmtu_icmp: str | None = None,
        honor_df: str | None = None,
        pmtu_discovery: str | None = None,
        virtual_switch_vlan: str | None = None,
        revision_image_auto_backup: str | None = None,
        revision_backup_on_logout: str | None = None,
        management_vdom: str | None = None,
        hostname: str | None = None,
        alias: str | None = None,
        strong_crypto: str | None = None,
        ssl_static_key_ciphers: str | None = None,
        snat_route_change: str | None = None,
        ipv6_snat_route_change: str | None = None,
        speedtest_server: str | None = None,
        cli_audit_log: str | None = None,
        dh_params: str | None = None,
        fds_statistics: str | None = None,
        fds_statistics_period: int | None = None,
        tcp_option: str | None = None,
        lldp_transmission: str | None = None,
        lldp_reception: str | None = None,
        proxy_auth_timeout: int | None = None,
        proxy_keep_alive_mode: str | None = None,
        proxy_re_authentication_time: int | None = None,
        proxy_auth_lifetime: str | None = None,
        proxy_auth_lifetime_timeout: int | None = None,
        proxy_resource_mode: str | None = None,
        proxy_cert_use_mgmt_vdom: str | None = None,
        sys_perf_log_interval: int | None = None,
        check_protocol_header: str | None = None,
        vip_arp_range: str | None = None,
        reset_sessionless_tcp: str | None = None,
        allow_traffic_redirect: str | None = None,
        ipv6_allow_traffic_redirect: str | None = None,
        strict_dirty_session_check: str | None = None,
        tcp_halfclose_timer: int | None = None,
        tcp_halfopen_timer: int | None = None,
        tcp_timewait_timer: int | None = None,
        tcp_rst_timer: int | None = None,
        udp_idle_timer: int | None = None,
        block_session_timer: int | None = None,
        ip_src_port_range: str | None = None,
        pre_login_banner: str | None = None,
        post_login_banner: str | None = None,
        tftp: str | None = None,
        av_failopen: str | None = None,
        av_failopen_session: str | None = None,
        memory_use_threshold_extreme: int | None = None,
        memory_use_threshold_red: int | None = None,
        memory_use_threshold_green: int | None = None,
        ip_fragment_mem_thresholds: int | None = None,
        ip_fragment_timeout: int | None = None,
        ipv6_fragment_timeout: int | None = None,
        cpu_use_threshold: int | None = None,
        log_single_cpu_high: str | None = None,
        check_reset_range: str | None = None,
        single_vdom_npuvlink: str | None = None,
        vdom_mode: str | None = None,
        long_vdom_name: str | None = None,
        upgrade_report: str | None = None,
        edit_vdom_prompt: str | None = None,
        admin_port: int | None = None,
        admin_sport: int | None = None,
        admin_host: str | None = None,
        admin_https_redirect: str | None = None,
        admin_hsts_max_age: int | None = None,
        admin_ssh_password: str | None = None,
        admin_restrict_local: str | None = None,
        admin_ssh_port: int | None = None,
        admin_ssh_grace_time: int | None = None,
        admin_ssh_v1: str | None = None,
        admin_telnet: str | None = None,
        admin_telnet_port: int | None = None,
        admin_forticloud_sso_login: str | None = None,
        admin_forticloud_sso_default_profile: str | None = None,
        default_service_source_port: str | None = None,
        admin_reset_button: str | None = None,
        admin_server_cert: str | None = None,
        admin_https_pki_required: str | None = None,
        wifi_certificate: str | None = None,
        dhcp_lease_backup_interval: int | None = None,
        wifi_ca_certificate: str | None = None,
        auth_http_port: int | None = None,
        auth_https_port: int | None = None,
        auth_ike_saml_port: int | None = None,
        auth_keepalive: str | None = None,
        policy_auth_concurrent: int | None = None,
        auth_session_limit: str | None = None,
        auth_cert: str | None = None,
        clt_cert_req: str | None = None,
        fortiservice_port: int | None = None,
        cfg_save: str | None = None,
        cfg_revert_timeout: int | None = None,
        reboot_upon_config_restore: str | None = None,
        admin_scp: str | None = None,
        wireless_controller: str | None = None,
        wireless_controller_port: int | None = None,
        fortiextender_data_port: int | None = None,
        fortiextender: str | None = None,
        extender_controller_reserved_network: str | None = None,
        fortiextender_discovery_lockdown: str | None = None,
        fortiextender_vlan_mode: str | None = None,
        fortiextender_provision_on_authorization: str | None = None,
        switch_controller: str | None = None,
        switch_controller_reserved_network: str | None = None,
        dnsproxy_worker_count: int | None = None,
        url_filter_count: int | None = None,
        httpd_max_worker_count: int | None = None,
        proxy_worker_count: int | None = None,
        scanunit_count: int | None = None,
        proxy_hardware_acceleration: str | None = None,
        fgd_alert_subscription: str | None = None,
        ipsec_hmac_offload: str | None = None,
        ipv6_accept_dad: int | None = None,
        ipv6_allow_anycast_probe: str | None = None,
        ipv6_allow_multicast_probe: str | None = None,
        ipv6_allow_local_in_silent_drop: str | None = None,
        csr_ca_attribute: str | None = None,
        wimax_4g_usb: str | None = None,
        cert_chain_max: int | None = None,
        two_factor_ftk_expiry: int | None = None,
        two_factor_email_expiry: int | None = None,
        two_factor_sms_expiry: int | None = None,
        two_factor_fac_expiry: int | None = None,
        two_factor_ftm_expiry: int | None = None,
        wad_worker_count: int | None = None,
        wad_worker_dev_cache: int | None = None,
        wad_csvc_cs_count: int | None = None,
        wad_csvc_db_count: int | None = None,
        wad_source_affinity: str | None = None,
        wad_memory_change_granularity: int | None = None,
        login_timestamp: str | None = None,
        ip_conflict_detection: str | None = None,
        miglogd_children: int | None = None,
        log_daemon_cpu_threshold: int | None = None,
        special_file_23_support: str | None = None,
        log_uuid_address: str | None = None,
        log_ssl_connection: str | None = None,
        rest_api_key_url_query: str | None = None,
        gui_cdn_domain_override: str | None = None,
        arp_max_entry: int | None = None,
        ha_affinity: str | None = None,
        bfd_affinity: str | None = None,
        cmdbsvr_affinity: str | None = None,
        ndp_max_entry: int | None = None,
        br_fdb_max_entry: int | None = None,
        max_route_cache_size: int | None = None,
        ipsec_asic_offload: str | None = None,
        device_idle_timeout: int | None = None,
        user_device_store_max_devices: int | None = None,
        user_device_store_max_device_mem: int | None = None,
        user_device_store_max_users: int | None = None,
        user_device_store_max_unified_mem: int | None = None,
        gui_device_latitude: str | None = None,
        gui_device_longitude: str | None = None,
        private_data_encryption: str | None = None,
        auto_auth_extension_device: str | None = None,
        gui_theme: str | None = None,
        gui_date_format: str | None = None,
        gui_date_time_source: str | None = None,
        igmp_state_limit: int | None = None,
        cloud_communication: str | None = None,
        ipsec_ha_seqjump_rate: int | None = None,
        fortitoken_cloud: str | None = None,
        fortitoken_cloud_push_status: str | None = None,
        fortitoken_cloud_region: str | None = None,
        fortitoken_cloud_sync_interval: int | None = None,
        faz_disk_buffer_size: int | None = None,
        irq_time_accounting: str | None = None,
        management_ip: str | None = None,
        management_port: int | None = None,
        management_port_use_admin_sport: str | None = None,
        forticonverter_integration: str | None = None,
        forticonverter_config_upload: str | None = None,
        internet_service_database: str | None = None,
        internet_service_download_list: list | None = None,
        geoip_full_db: str | None = None,
        early_tcp_npu_session: str | None = None,
        npu_neighbor_update: str | None = None,
        delay_tcp_npu_session: str | None = None,
        interface_subnet_usage: str | None = None,
        sflowd_max_children_num: int | None = None,
        fortigslb_integration: str | None = None,
        user_history_password_threshold: int | None = None,
        auth_session_auto_backup: str | None = None,
        auth_session_auto_backup_interval: str | None = None,
        scim_https_port: int | None = None,
        scim_http_port: int | None = None,
        scim_server_cert: str | None = None,
        application_bandwidth_tracking: str | None = None,
        tls_session_cache: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            language: GUI display language. (optional)
            gui_allow_incompatible_fabric_fgt: Enable/disable Allow FGT with
            incompatible firmware to be treated as compatible in security
            fabric on the GUI. May cause unexpected error. (optional)
            gui_ipv6: Enable/disable IPv6 settings on the GUI. (optional)
            gui_replacement_message_groups: Enable/disable replacement message
            groups on the GUI. (optional)
            gui_local_out: Enable/disable Local-out traffic on the GUI.
            (optional)
            gui_certificates: Enable/disable the System > Certificate GUI page,
            allowing you to add and configure certificates from the GUI.
            (optional)
            gui_custom_language: Enable/disable custom languages in GUI.
            (optional)
            gui_wireless_opensecurity: Enable/disable wireless open security
            option on the GUI. (optional)
            gui_app_detection_sdwan: Enable/disable Allow app-detection based
            SD-WAN. (optional)
            gui_display_hostname: Enable/disable displaying the FortiGate's
            hostname on the GUI login page. (optional)
            gui_fortigate_cloud_sandbox: Enable/disable displaying FortiGate
            Cloud Sandbox on the GUI. (optional)
            gui_firmware_upgrade_warning: Enable/disable the firmware upgrade
            warning on the GUI. (optional)
            gui_forticare_registration_setup_warning: Enable/disable the
            FortiCare registration setup warning on the GUI. (optional)
            gui_auto_upgrade_setup_warning: Enable/disable the automatic patch
            upgrade setup prompt on the GUI. (optional)
            gui_workflow_management: Enable/disable Workflow management
            features on the GUI. (optional)
            gui_cdn_usage: Enable/disable Load GUI static files from a CDN.
            (optional)
            admin_https_ssl_versions: Allowed TLS versions for web
            administration. (optional)
            admin_https_ssl_ciphersuites: Select one or more TLS 1.3
            ciphersuites to enable. Does not affect ciphers in TLS 1.2 and
            below. At least one must be enabled. To disable all, remove TLS1.3
            from admin-https-ssl-versions. (optional)
            admin_https_ssl_banned_ciphers: Select one or more cipher
            technologies that cannot be used in GUI HTTPS negotiations. Only
            applies to TLS 1.2 and below. (optional)
            admintimeout: Number of minutes before an idle administrator
            session times out (1 - 480 minutes (8 hours), default = 5). A
            shorter idle timeout is more secure. (optional)
            admin_console_timeout: Console login timeout that overrides the
            admin timeout value (15 - 300 seconds, default = 0, which disables
            the timeout). (optional)
            ssd_trim_freq: How often to run SSD Trim (default = weekly). SSD
            Trim prevents SSD drive data loss by finding and isolating errors.
            (optional)
            ssd_trim_hour: Hour of the day on which to run SSD Trim (0 - 23,
            default = 1). (optional)
            ssd_trim_min: Minute of the hour on which to run SSD Trim (0 - 59,
            60 for random). (optional)
            ssd_trim_weekday: Day of week to run SSD Trim. (optional)
            ssd_trim_date: Date within a month to run ssd trim. (optional)
            admin_concurrent: Enable/disable concurrent administrator logins.
            Use policy-auth-concurrent for firewall authenticated users.
            (optional)
            admin_lockout_threshold: Number of failed login attempts before an
            administrator account is locked out for the admin-lockout-duration.
            (optional)
            admin_lockout_duration: Amount of time in seconds that an
            administrator account is locked out after reaching the
            admin-lockout-threshold for repeated failed login attempts.
            (optional)
            refresh: Statistics refresh interval second(s) in GUI. (optional)
            interval: Dead gateway detection interval. (optional)
            failtime: Fail-time for server lost. (optional)
            purdue_level: Purdue Level of this FortiGate. (optional)
            daily_restart: Enable/disable daily restart of FortiGate unit. Use
            the restart-time option to set the time of day for the restart.
            (optional)
            restart_time: Daily restart time (hh:mm). (optional)
            wad_restart_mode: WAD worker restart mode (default = none).
            (optional)
            wad_restart_start_time: WAD workers daily restart time (hh:mm).
            (optional)
            wad_restart_end_time: WAD workers daily restart end time (hh:mm).
            (optional)
            wad_p2s_max_body_size: Maximum size of the body of the local out
            HTTP request (1 - 32 Mbytes, default = 4). (optional)
            radius_port: RADIUS service port number. (optional)
            speedtestd_server_port: Speedtest server port number. (optional)
            speedtestd_ctrl_port: Speedtest server controller port number.
            (optional)
            admin_login_max: Maximum number of administrators who can be logged
            in at the same time (1 - 100, default = 100). (optional)
            remoteauthtimeout: Number of seconds that the FortiGate waits for
            responses from remote RADIUS, LDAP, or TACACS+ authentication
            servers. (1-300 sec, default = 5). (optional)
            ldapconntimeout: Global timeout for connections with remote LDAP
            servers in milliseconds (1 - 300000, default 500). (optional)
            batch_cmdb: Enable/disable batch mode, allowing you to enter a
            series of CLI commands that will execute as a group once they are
            loaded. (optional)
            multi_factor_authentication: Enforce all login methods to require
            an additional authentication factor (default = optional).
            (optional)
            ssl_min_proto_version: Minimum supported protocol version for
            SSL/TLS connections (default = TLSv1.2). (optional)
            autorun_log_fsck: Enable/disable automatic log partition check
            after ungraceful shutdown. (optional)
            timezone: Timezone database name. Enter ? to view the list of
            timezone. (optional)
            traffic_priority: Choose Type of Service (ToS) or Differentiated
            Services Code Point (DSCP) for traffic prioritization in traffic
            shaping. (optional)
            traffic_priority_level: Default system-wide level of priority for
            traffic prioritization. (optional)
            quic_congestion_control_algo: QUIC congestion control algorithm
            (default = cubic). (optional)
            quic_max_datagram_size: Maximum transmit datagram size (1200 -
            1500, default = 1500). (optional)
            quic_udp_payload_size_shaping_per_cid: Enable/disable UDP payload
            size shaping per connection ID (default = enable). (optional)
            quic_ack_thresold: Maximum number of unacknowledged packets before
            sending ACK (2 - 5, default = 3). (optional)
            quic_pmtud: Enable/disable path MTU discovery (default = enable).
            (optional)
            quic_tls_handshake_timeout: Time-to-live (TTL) for TLS handshake in
            seconds (1 - 60, default = 5). (optional)
            anti_replay: Level of checking for packet replay and TCP sequence
            checking. (optional)
            send_pmtu_icmp: Enable/disable sending of path maximum transmission
            unit (PMTU) - ICMP destination unreachable packet and to support
            PMTUD protocol on your network to reduce fragmentation of packets.
            (optional)
            honor_df: Enable/disable honoring of Don't-Fragment (DF) flag.
            (optional)
            pmtu_discovery: Enable/disable path MTU discovery. (optional)
            virtual_switch_vlan: Enable/disable virtual switch VLAN. (optional)
            revision_image_auto_backup: Enable/disable back-up of the latest
            image revision after the firmware is upgraded. (optional)
            revision_backup_on_logout: Enable/disable back-up of the latest
            configuration revision when an administrator logs out of the CLI or
            GUI. (optional)
            management_vdom: Management virtual domain name. (optional)
            hostname: FortiGate unit's hostname. Most models will truncate
            names longer than 24 characters. Some models support hostnames up
            to 35 characters. (optional)
            alias: Alias for your FortiGate unit. (optional)
            strong_crypto: Enable to use strong encryption and only allow
            strong ciphers and digest for HTTPS/SSH/TLS/SSL functions.
            (optional)
            ssl_static_key_ciphers: Enable/disable static key ciphers in
            SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256,
            AES256-SHA256). (optional)
            snat_route_change: Enable/disable the ability to change the source
            NAT route. (optional)
            ipv6_snat_route_change: Enable/disable the ability to change the
            IPv6 source NAT route. (optional)
            speedtest_server: Enable/disable speed test server. (optional)
            cli_audit_log: Enable/disable CLI audit log. (optional)
            dh_params: Number of bits to use in the Diffie-Hellman exchange for
            HTTPS/SSH protocols. (optional)
            fds_statistics: Enable/disable sending IPS, Application Control,
            and AntiVirus data to FortiGuard. This data is used to improve
            FortiGuard services and is not shared with external parties and is
            protected by Fortinet's privacy policy. (optional)
            fds_statistics_period: FortiGuard statistics collection period in
            minutes. (1 - 1440 min (1 min to 24 hours), default = 60).
            (optional)
            tcp_option: Enable SACK, timestamp and MSS TCP options. (optional)
            lldp_transmission: Enable/disable Link Layer Discovery Protocol
            (LLDP) transmission. (optional)
            lldp_reception: Enable/disable Link Layer Discovery Protocol (LLDP)
            reception. (optional)
            proxy_auth_timeout: Authentication timeout in minutes for
            authenticated users (1 - 10000 min, default = 10). (optional)
            proxy_keep_alive_mode: Control if users must re-authenticate after
            a session is closed, traffic has been idle, or from the point at
            which the user was authenticated. (optional)
            proxy_re_authentication_time: The time limit that users must
            re-authenticate if proxy-keep-alive-mode is set to re-authenticate
            (1 - 86400 sec, default=30s. (optional)
            proxy_auth_lifetime: Enable/disable authenticated users lifetime
            control. This is a cap on the total time a proxy user can be
            authenticated for after which re-authentication will take place.
            (optional)
            proxy_auth_lifetime_timeout: Lifetime timeout in minutes for
            authenticated users (5 - 65535 min, default=480 (8 hours)).
            (optional)
            proxy_resource_mode: Enable/disable use of the maximum memory usage
            on the FortiGate unit's proxy processing of resources, such as
            block lists, allow lists, and external resources. (optional)
            proxy_cert_use_mgmt_vdom: Enable/disable using management VDOM to
            send requests. (optional)
            sys_perf_log_interval: Time in minutes between updates of
            performance statistics logging. (1 - 15 min, default = 5, 0 =
            disabled). (optional)
            check_protocol_header: Level of checking performed on protocol
            headers. Strict checking is more thorough but may affect
            performance. Loose checking is OK in most cases. (optional)
            vip_arp_range: Controls the number of ARPs that the FortiGate sends
            for a Virtual IP (VIP) address range. (optional)
            reset_sessionless_tcp: Action to perform if the FortiGate receives
            a TCP packet but cannot find a corresponding session in its session
            table. NAT/Route mode only. (optional)
            allow_traffic_redirect: Disable to prevent traffic with same local
            ingress and egress interface from being forwarded without policy
            check. (optional)
            ipv6_allow_traffic_redirect: Disable to prevent IPv6 traffic with
            same local ingress and egress interface from being forwarded
            without policy check. (optional)
            strict_dirty_session_check: Enable to check the session against the
            original policy when revalidating. This can prevent dropping of
            redirected sessions when web-filtering and authentication are
            enabled together. If this option is enabled, the FortiGate unit
            deletes a session if a routing or policy change causes the session
            to no longer match the policy that originally allowed the session.
            (optional)
            tcp_halfclose_timer: Number of seconds the FortiGate unit should
            wait to close a session after one peer has sent a FIN packet but
            the other has not responded (1 - 86400 sec (1 day), default = 120).
            (optional)
            tcp_halfopen_timer: Number of seconds the FortiGate unit should
            wait to close a session after one peer has sent an open session
            packet but the other has not responded (1 - 86400 sec (1 day),
            default = 10). (optional)
            tcp_timewait_timer: Length of the TCP TIME-WAIT state in seconds (1
            - 300 sec, default = 1). (optional)
            tcp_rst_timer: Length of the TCP CLOSE state in seconds (5 - 300
            sec, default = 5). (optional)
            udp_idle_timer: UDP connection session timeout. This command can be
            useful in managing CPU and memory resources (1 - 86400 seconds (1
            day), default = 60). (optional)
            block_session_timer: Duration in seconds for blocked sessions (1 -
            300 sec (5 minutes), default = 30). (optional)
            ip_src_port_range: IP source port range used for traffic
            originating from the FortiGate unit. (optional)
            pre_login_banner: Enable/disable displaying the administrator
            access disclaimer message on the login page before an administrator
            logs in. (optional)
            post_login_banner: Enable/disable displaying the administrator
            access disclaimer message after an administrator successfully logs
            in. (optional)
            tftp: Enable/disable TFTP. (optional)
            av_failopen: Set the action to take if the FortiGate is running low
            on memory or the proxy connection limit has been reached.
            (optional)
            av_failopen_session: When enabled and a proxy for a protocol runs
            out of room in its session table, that protocol goes into failopen
            mode and enacts the action specified by av-failopen. (optional)
            memory_use_threshold_extreme: Threshold at which memory usage is
            considered extreme (new sessions are dropped) (% of total RAM,
            default = 95). (optional)
            memory_use_threshold_red: Threshold at which memory usage forces
            the FortiGate to enter conserve mode (% of total RAM, default =
            88). (optional)
            memory_use_threshold_green: Threshold at which memory usage forces
            the FortiGate to exit conserve mode (% of total RAM, default = 82).
            (optional)
            ip_fragment_mem_thresholds: Maximum memory (MB) used to reassemble
            IPv4/IPv6 fragments. (optional)
            ip_fragment_timeout: Timeout value in seconds for any fragment not
            being reassembled (optional)
            ipv6_fragment_timeout: Timeout value in seconds for any IPv6
            fragment not being reassembled (optional)
            cpu_use_threshold: Threshold at which CPU usage is reported (% of
            total CPU, default = 90). (optional)
            log_single_cpu_high: Enable/disable logging the event of a single
            CPU core reaching CPU usage threshold. (optional)
            check_reset_range: Configure ICMP error message verification. You
            can either apply strict RST range checking or disable it.
            (optional)
            single_vdom_npuvlink: Enable/disable NPU VDOMs links for single
            VDOM. (optional)
            vdom_mode: Enable/disable support for multiple virtual domains
            (VDOMs). (optional)
            long_vdom_name: Enable/disable long VDOM name support. (optional)
            upgrade_report: Enable/disable the generation of an upgrade report
            when upgrading the firmware. (optional)
            edit_vdom_prompt: Enable/disable edit new VDOM prompt. (optional)
            admin_port: Administrative access port for HTTP. (1 - 65535,
            default = 80). (optional)
            admin_sport: Administrative access port for HTTPS. (1 - 65535,
            default = 443). (optional)
            admin_host: Administrative host for HTTP and HTTPS. When set, will
            be used in lieu of the client's Host header for any redirection.
            (optional)
            admin_https_redirect: Enable/disable redirection of HTTP
            administration access to HTTPS. (optional)
            admin_hsts_max_age: HTTPS Strict-Transport-Security header max-age
            in seconds. A value of 0 will reset any HSTS records in the
            browser.When admin-https-redirect is disabled the header max-age
            will be 0. (optional)
            admin_ssh_password: Enable/disable password authentication for SSH
            admin access. (optional)
            admin_restrict_local: Enable/disable local admin authentication
            restriction when remote authenticator is up and running (default =
            disable). (optional)
            admin_ssh_port: Administrative access port for SSH. (1 - 65535,
            default = 22). (optional)
            admin_ssh_grace_time: Maximum time in seconds permitted between
            making an SSH connection to the FortiGate unit and authenticating
            (10 - 3600 sec (1 hour), default 120). (optional)
            admin_ssh_v1: Enable/disable SSH v1 compatibility. (optional)
            admin_telnet: Enable/disable TELNET service. (optional)
            admin_telnet_port: Administrative access port for TELNET. (1 -
            65535, default = 23). (optional)
            admin_forticloud_sso_login: Enable/disable FortiCloud admin login
            via SSO. (optional)
            admin_forticloud_sso_default_profile: Override access profile.
            (optional)
            default_service_source_port: Default service source port range
            (default = 1 - 65535). (optional)
            admin_reset_button: Press the reset button can reset to factory
            default. (optional)
            admin_server_cert: Server certificate that the FortiGate uses for
            HTTPS administrative connections. (optional)
            admin_https_pki_required: Enable/disable admin login method. Enable
            to force administrators to provide a valid certificate to log in if
            PKI is enabled. Disable to allow administrators to log in with a
            certificate or password. (optional)
            wifi_certificate: Certificate to use for WiFi authentication.
            (optional)
            dhcp_lease_backup_interval: DHCP leases backup interval in seconds
            (10 - 3600, default = 60). (optional)
            wifi_ca_certificate: CA certificate that verifies the WiFi
            certificate. (optional)
            auth_http_port: User authentication HTTP port. (1 - 65535, default
            = 1000). (optional)
            auth_https_port: User authentication HTTPS port. (1 - 65535,
            default = 1003). (optional)
            auth_ike_saml_port: User IKE SAML authentication port (0 - 65535,
            default = 1001). (optional)
            auth_keepalive: Enable to prevent user authentication sessions from
            timing out when idle. (optional)
            policy_auth_concurrent: Number of concurrent firewall use logins
            from the same user (1 - 100, default = 0 means no limit).
            (optional)
            auth_session_limit: Action to take when the number of allowed user
            authenticated sessions is reached. (optional)
            auth_cert: Server certificate that the FortiGate uses for HTTPS
            firewall authentication connections. (optional)
            clt_cert_req: Enable/disable requiring administrators to have a
            client certificate to log into the GUI using HTTPS. (optional)
            fortiservice_port: FortiService port (1 - 65535, default = 8013).
            Used by FortiClient endpoint compliance. Older versions of
            FortiClient used a different port. (optional)
            cfg_save: Configuration file save mode for CLI changes. (optional)
            cfg_revert_timeout: Time-out for reverting to the last saved
            configuration. (10 - 4294967295 seconds, default = 600). (optional)
            reboot_upon_config_restore: Enable/disable reboot of system upon
            restoring configuration. (optional)
            admin_scp: Enable/disable SCP support for system configuration
            backup, restore, and firmware file upload. (optional)
            wireless_controller: Enable/disable the wireless controller feature
            to use the FortiGate unit to manage FortiAPs. (optional)
            wireless_controller_port: Port used for the control channel in
            wireless controller mode (wireless-mode is ac). The data channel
            port is the control channel port number plus one (1024 - 49150,
            default = 5246). (optional)
            fortiextender_data_port: FortiExtender data port (1024 - 49150,
            default = 25246). (optional)
            fortiextender: Enable/disable FortiExtender. (optional)
            extender_controller_reserved_network: Configure reserved network
            subnet for managed LAN extension FortiExtender units. This is
            available when the FortiExtender daemon is running. (optional)
            fortiextender_discovery_lockdown: Enable/disable FortiExtender
            CAPWAP lockdown. (optional)
            fortiextender_vlan_mode: Enable/disable FortiExtender VLAN mode.
            (optional)
            fortiextender_provision_on_authorization: Enable/disable automatic
            provisioning of latest FortiExtender firmware on authorization.
            (optional)
            switch_controller: Enable/disable switch controller feature. Switch
            controller allows you to manage FortiSwitch from the FortiGate
            itself. (optional)
            switch_controller_reserved_network: Configure reserved network
            subnet for managed switches. This is available when the switch
            controller is enabled. (optional)
            dnsproxy_worker_count: DNS proxy worker count. For a FortiGate with
            multiple logical CPUs, you can set the DNS process number from 1 to
            the number of logical CPUs. (optional)
            url_filter_count: URL filter daemon count. (optional)
            httpd_max_worker_count: Maximum number of simultaneous HTTP
            requests that will be served. This number may affect GUI and REST
            API performance (0 - 128, default = 0 means let system decide).
            (optional)
            proxy_worker_count: Proxy worker count. (optional)
            scanunit_count: Number of scanunits. The range and the default
            depend on the number of CPUs. Only available on FortiGate units
            with multiple CPUs. (optional)
            proxy_hardware_acceleration: Enable/disable email proxy hardware
            acceleration. (optional)
            fgd_alert_subscription: Type of alert to retrieve from FortiGuard.
            (optional)
            ipsec_hmac_offload: Enable/disable offloading (hardware
            acceleration) of HMAC processing for IPsec VPN. (optional)
            ipv6_accept_dad: Enable/disable acceptance of IPv6 Duplicate
            Address Detection (DAD). (optional)
            ipv6_allow_anycast_probe: Enable/disable IPv6 address probe through
            Anycast. (optional)
            ipv6_allow_multicast_probe: Enable/disable IPv6 address probe
            through Multicast. (optional)
            ipv6_allow_local_in_silent_drop: Enable/disable silent drop of IPv6
            local-in traffic. (optional)
            csr_ca_attribute: Enable/disable the CA attribute in certificates.
            Some CA servers reject CSRs that have the CA attribute. (optional)
            wimax_4g_usb: Enable/disable comparability with WiMAX 4G USB
            devices. (optional)
            cert_chain_max: Maximum number of certificates that can be
            traversed in a certificate chain. (optional)
            two_factor_ftk_expiry: FortiToken authentication session timeout
            (60 - 600 sec (10 minutes), default = 60). (optional)
            two_factor_email_expiry: Email-based two-factor authentication
            session timeout (30 - 300 seconds (5 minutes), default = 60).
            (optional)
            two_factor_sms_expiry: SMS-based two-factor authentication session
            timeout (30 - 300 sec, default = 60). (optional)
            two_factor_fac_expiry: FortiAuthenticator token authentication
            session timeout (10 - 3600 seconds (1 hour), default = 60).
            (optional)
            two_factor_ftm_expiry: FortiToken Mobile session timeout (1 - 168
            hours (7 days), default = 72). (optional)
            wad_worker_count: Number of explicit proxy WAN optimization daemon
            (WAD) processes. By default WAN optimization, explicit proxy, and
            web caching is handled by all of the CPU cores in a FortiGate unit.
            (optional)
            wad_worker_dev_cache: Number of cached devices for each ZTNA proxy
            worker. The default value is tuned by memory consumption. Set the
            option to 0 to disable the cache. (optional)
            wad_csvc_cs_count: Number of concurrent WAD-cache-service
            object-cache processes. (optional)
            wad_csvc_db_count: Number of concurrent WAD-cache-service
            byte-cache processes. (optional)
            wad_source_affinity: Enable/disable dispatching traffic to WAD
            workers based on source affinity. (optional)
            wad_memory_change_granularity: Minimum percentage change in system
            memory usage detected by the wad daemon prior to adjusting TCP
            window size for any active connection. (optional)
            login_timestamp: Enable/disable login time recording. (optional)
            ip_conflict_detection: Enable/disable logging of IPv4 address
            conflict detection. (optional)
            miglogd_children: Number of logging (miglogd) processes to be
            allowed to run. Higher number can reduce performance; lower number
            can slow log processing time. (optional)
            log_daemon_cpu_threshold: Configure syslog daemon process spawning
            threshold. Use a percentage threshold of syslogd CPU usage (1 - 99)
            or set to zero to use dynamic scheduling based on the number of
            packets in the syslogd queue (default = 0). (optional)
            special_file_23_support: Enable/disable detection of those special
            format files when using Data Loss Prevention. (optional)
            log_uuid_address: Enable/disable insertion of address UUIDs to
            traffic logs. (optional)
            log_ssl_connection: Enable/disable logging of SSL connection
            events. (optional)
            rest_api_key_url_query: Enable/disable support for passing REST API
            keys through URL query parameters. (optional)
            gui_cdn_domain_override: Domain of CDN server. (optional)
            arp_max_entry: Maximum number of dynamically learned MAC addresses
            that can be added to the ARP table (131072 - 2147483647, default =
            131072). (optional)
            ha_affinity: Affinity setting for HA daemons (hexadecimal value up
            to 256 bits in the format of xxxxxxxxxxxxxxxx). (optional)
            bfd_affinity: Affinity setting for BFD daemon (hexadecimal value up
            to 256 bits in the format of xxxxxxxxxxxxxxxx). (optional)
            cmdbsvr_affinity: Affinity setting for cmdbsvr (hexadecimal value
            up to 256 bits in the format of xxxxxxxxxxxxxxxx). (optional)
            ndp_max_entry: Maximum number of NDP table entries (set to 65,536
            or higher; if set to 0, kernel holds 65,536 entries). (optional)
            br_fdb_max_entry: Maximum number of bridge forwarding database
            (FDB) entries. (optional)
            max_route_cache_size: Maximum number of IP route cache entries (0 -
            2147483647). (optional)
            ipsec_asic_offload: Enable/disable ASIC offloading (hardware
            acceleration) for IPsec VPN traffic. Hardware acceleration can
            offload IPsec VPN sessions and accelerate encryption and
            decryption. (optional)
            device_idle_timeout: Time in seconds that a device must be idle to
            automatically log the device user out. (30 - 31536000 sec (30 sec
            to 1 year), default = 300). (optional)
            user_device_store_max_devices: Maximum number of devices allowed in
            user device store. (optional)
            user_device_store_max_device_mem: Maximum percentage of total
            system memory allowed to be used for devices in the user device
            store. (optional)
            user_device_store_max_users: Maximum number of users allowed in
            user device store. (optional)
            user_device_store_max_unified_mem: Maximum unified memory allowed
            in user device store. (optional)
            gui_device_latitude: Add the latitude of the location of this
            FortiGate to position it on the Threat Map. (optional)
            gui_device_longitude: Add the longitude of the location of this
            FortiGate to position it on the Threat Map. (optional)
            private_data_encryption: Enable/disable private data encryption
            using an AES 128-bit key or passpharse. (optional)
            auto_auth_extension_device: Enable/disable automatic authorization
            of dedicated Fortinet extension devices. (optional)
            gui_theme: Color scheme for the administration GUI. (optional)
            gui_date_format: Default date format used throughout GUI.
            (optional)
            gui_date_time_source: Source from which the FortiGate GUI uses to
            display date and time entries. (optional)
            igmp_state_limit: Maximum number of IGMP memberships (96 - 64000,
            default = 3200). (optional)
            cloud_communication: Enable/disable all cloud communication.
            (optional)
            ipsec_ha_seqjump_rate: ESP jump ahead rate (1G - 10G pps
            equivalent). (optional)
            fortitoken_cloud: Enable/disable FortiToken Cloud service.
            (optional)
            fortitoken_cloud_push_status: Enable/disable FTM push service of
            FortiToken Cloud. (optional)
            fortitoken_cloud_region: Region domain of FortiToken Cloud(unset to
            non-region). (optional)
            fortitoken_cloud_sync_interval: Interval in which to clean up
            remote users in FortiToken Cloud (0 - 336 hours (14 days), default
            = 24, disable = 0). (optional)
            faz_disk_buffer_size: Maximum disk buffer size to temporarily store
            logs destined for FortiAnalyzer. To be used in the event that
            FortiAnalyzer is unavailable. (optional)
            irq_time_accounting: Configure CPU IRQ time accounting mode.
            (optional)
            management_ip: Management IP address of this FortiGate. Used to log
            into this FortiGate from another FortiGate in the Security Fabric.
            (optional)
            management_port: Overriding port for management connection
            (Overrides admin port). (optional)
            management_port_use_admin_sport: Enable/disable use of the
            admin-sport setting for the management port. If disabled, FortiGate
            will allow user to specify management-port. (optional)
            forticonverter_integration: Enable/disable FortiConverter
            integration service. (optional)
            forticonverter_config_upload: Enable/disable config upload to
            FortiConverter. (optional)
            internet_service_database: Configure which Internet Service
            database size to download from FortiGuard and use. (optional)
            internet_service_download_list: Configure which on-demand Internet
            Service IDs are to be downloaded. (optional)
            geoip_full_db: When enabled, the full geographic database will be
            loaded into the kernel which enables geographic information in
            traffic logs - required for FortiView countries. Disabling this
            option will conserve memory. (optional)
            early_tcp_npu_session: Enable/disable early TCP NPU session.
            (optional)
            npu_neighbor_update: Enable/disable sending of ARP/ICMP6 probing
            packets to update neighbors for offloaded sessions. (optional)
            delay_tcp_npu_session: Enable TCP NPU session delay to guarantee
            packet order of 3-way handshake. (optional)
            interface_subnet_usage: Enable/disable allowing use of
            interface-subnet setting in firewall addresses (default = enable).
            (optional)
            sflowd_max_children_num: Maximum number of sflowd child processes
            allowed to run. (optional)
            fortigslb_integration: Enable/disable integration with the
            FortiGSLB cloud service. (optional)
            user_history_password_threshold: Maximum number of previous
            passwords saved per admin/user (3 - 15, default = 3). (optional)
            auth_session_auto_backup: Enable/disable automatic and periodic
            backup of authentication sessions (default = disable). Sessions are
            restored upon bootup. (optional)
            auth_session_auto_backup_interval: Configure automatic
            authentication session backup interval (default = 15min).
            (optional)
            scim_https_port: SCIM port (0 - 65535, default = 44559). (optional)
            scim_http_port: SCIM http port (0 - 65535, default = 44558).
            (optional)
            scim_server_cert: Server certificate that the FortiGate uses for
            SCIM connections. (optional)
            application_bandwidth_tracking: Enable/disable application
            bandwidth tracking. (optional)
            tls_session_cache: Enable/disable TLS session cache. (optional)
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
        endpoint = "/system/global"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if language is not None:
            data_payload["language"] = language
        if gui_allow_incompatible_fabric_fgt is not None:
            data_payload["gui-allow-incompatible-fabric-fgt"] = (
                gui_allow_incompatible_fabric_fgt
            )
        if gui_ipv6 is not None:
            data_payload["gui-ipv6"] = gui_ipv6
        if gui_replacement_message_groups is not None:
            data_payload["gui-replacement-message-groups"] = (
                gui_replacement_message_groups
            )
        if gui_local_out is not None:
            data_payload["gui-local-out"] = gui_local_out
        if gui_certificates is not None:
            data_payload["gui-certificates"] = gui_certificates
        if gui_custom_language is not None:
            data_payload["gui-custom-language"] = gui_custom_language
        if gui_wireless_opensecurity is not None:
            data_payload["gui-wireless-opensecurity"] = (
                gui_wireless_opensecurity
            )
        if gui_app_detection_sdwan is not None:
            data_payload["gui-app-detection-sdwan"] = gui_app_detection_sdwan
        if gui_display_hostname is not None:
            data_payload["gui-display-hostname"] = gui_display_hostname
        if gui_fortigate_cloud_sandbox is not None:
            data_payload["gui-fortigate-cloud-sandbox"] = (
                gui_fortigate_cloud_sandbox
            )
        if gui_firmware_upgrade_warning is not None:
            data_payload["gui-firmware-upgrade-warning"] = (
                gui_firmware_upgrade_warning
            )
        if gui_forticare_registration_setup_warning is not None:
            data_payload["gui-forticare-registration-setup-warning"] = (
                gui_forticare_registration_setup_warning
            )
        if gui_auto_upgrade_setup_warning is not None:
            data_payload["gui-auto-upgrade-setup-warning"] = (
                gui_auto_upgrade_setup_warning
            )
        if gui_workflow_management is not None:
            data_payload["gui-workflow-management"] = gui_workflow_management
        if gui_cdn_usage is not None:
            data_payload["gui-cdn-usage"] = gui_cdn_usage
        if admin_https_ssl_versions is not None:
            data_payload["admin-https-ssl-versions"] = admin_https_ssl_versions
        if admin_https_ssl_ciphersuites is not None:
            data_payload["admin-https-ssl-ciphersuites"] = (
                admin_https_ssl_ciphersuites
            )
        if admin_https_ssl_banned_ciphers is not None:
            data_payload["admin-https-ssl-banned-ciphers"] = (
                admin_https_ssl_banned_ciphers
            )
        if admintimeout is not None:
            data_payload["admintimeout"] = admintimeout
        if admin_console_timeout is not None:
            data_payload["admin-console-timeout"] = admin_console_timeout
        if ssd_trim_freq is not None:
            data_payload["ssd-trim-freq"] = ssd_trim_freq
        if ssd_trim_hour is not None:
            data_payload["ssd-trim-hour"] = ssd_trim_hour
        if ssd_trim_min is not None:
            data_payload["ssd-trim-min"] = ssd_trim_min
        if ssd_trim_weekday is not None:
            data_payload["ssd-trim-weekday"] = ssd_trim_weekday
        if ssd_trim_date is not None:
            data_payload["ssd-trim-date"] = ssd_trim_date
        if admin_concurrent is not None:
            data_payload["admin-concurrent"] = admin_concurrent
        if admin_lockout_threshold is not None:
            data_payload["admin-lockout-threshold"] = admin_lockout_threshold
        if admin_lockout_duration is not None:
            data_payload["admin-lockout-duration"] = admin_lockout_duration
        if refresh is not None:
            data_payload["refresh"] = refresh
        if interval is not None:
            data_payload["interval"] = interval
        if failtime is not None:
            data_payload["failtime"] = failtime
        if purdue_level is not None:
            data_payload["purdue-level"] = purdue_level
        if daily_restart is not None:
            data_payload["daily-restart"] = daily_restart
        if restart_time is not None:
            data_payload["restart-time"] = restart_time
        if wad_restart_mode is not None:
            data_payload["wad-restart-mode"] = wad_restart_mode
        if wad_restart_start_time is not None:
            data_payload["wad-restart-start-time"] = wad_restart_start_time
        if wad_restart_end_time is not None:
            data_payload["wad-restart-end-time"] = wad_restart_end_time
        if wad_p2s_max_body_size is not None:
            data_payload["wad-p2s-max-body-size"] = wad_p2s_max_body_size
        if radius_port is not None:
            data_payload["radius-port"] = radius_port
        if speedtestd_server_port is not None:
            data_payload["speedtestd-server-port"] = speedtestd_server_port
        if speedtestd_ctrl_port is not None:
            data_payload["speedtestd-ctrl-port"] = speedtestd_ctrl_port
        if admin_login_max is not None:
            data_payload["admin-login-max"] = admin_login_max
        if remoteauthtimeout is not None:
            data_payload["remoteauthtimeout"] = remoteauthtimeout
        if ldapconntimeout is not None:
            data_payload["ldapconntimeout"] = ldapconntimeout
        if batch_cmdb is not None:
            data_payload["batch-cmdb"] = batch_cmdb
        if multi_factor_authentication is not None:
            data_payload["multi-factor-authentication"] = (
                multi_factor_authentication
            )
        if ssl_min_proto_version is not None:
            data_payload["ssl-min-proto-version"] = ssl_min_proto_version
        if autorun_log_fsck is not None:
            data_payload["autorun-log-fsck"] = autorun_log_fsck
        if timezone is not None:
            data_payload["timezone"] = timezone
        if traffic_priority is not None:
            data_payload["traffic-priority"] = traffic_priority
        if traffic_priority_level is not None:
            data_payload["traffic-priority-level"] = traffic_priority_level
        if quic_congestion_control_algo is not None:
            data_payload["quic-congestion-control-algo"] = (
                quic_congestion_control_algo
            )
        if quic_max_datagram_size is not None:
            data_payload["quic-max-datagram-size"] = quic_max_datagram_size
        if quic_udp_payload_size_shaping_per_cid is not None:
            data_payload["quic-udp-payload-size-shaping-per-cid"] = (
                quic_udp_payload_size_shaping_per_cid
            )
        if quic_ack_thresold is not None:
            data_payload["quic-ack-thresold"] = quic_ack_thresold
        if quic_pmtud is not None:
            data_payload["quic-pmtud"] = quic_pmtud
        if quic_tls_handshake_timeout is not None:
            data_payload["quic-tls-handshake-timeout"] = (
                quic_tls_handshake_timeout
            )
        if anti_replay is not None:
            data_payload["anti-replay"] = anti_replay
        if send_pmtu_icmp is not None:
            data_payload["send-pmtu-icmp"] = send_pmtu_icmp
        if honor_df is not None:
            data_payload["honor-d"] = honor_df
        if pmtu_discovery is not None:
            data_payload["pmtu-discovery"] = pmtu_discovery
        if virtual_switch_vlan is not None:
            data_payload["virtual-switch-vlan"] = virtual_switch_vlan
        if revision_image_auto_backup is not None:
            data_payload["revision-image-auto-backup"] = (
                revision_image_auto_backup
            )
        if revision_backup_on_logout is not None:
            data_payload["revision-backup-on-logout"] = (
                revision_backup_on_logout
            )
        if management_vdom is not None:
            data_payload["management-vdom"] = management_vdom
        if hostname is not None:
            data_payload["hostname"] = hostname
        if alias is not None:
            data_payload["alias"] = alias
        if strong_crypto is not None:
            data_payload["strong-crypto"] = strong_crypto
        if ssl_static_key_ciphers is not None:
            data_payload["ssl-static-key-ciphers"] = ssl_static_key_ciphers
        if snat_route_change is not None:
            data_payload["snat-route-change"] = snat_route_change
        if ipv6_snat_route_change is not None:
            data_payload["ipv6-snat-route-change"] = ipv6_snat_route_change
        if speedtest_server is not None:
            data_payload["speedtest-server"] = speedtest_server
        if cli_audit_log is not None:
            data_payload["cli-audit-log"] = cli_audit_log
        if dh_params is not None:
            data_payload["dh-params"] = dh_params
        if fds_statistics is not None:
            data_payload["fds-statistics"] = fds_statistics
        if fds_statistics_period is not None:
            data_payload["fds-statistics-period"] = fds_statistics_period
        if tcp_option is not None:
            data_payload["tcp-option"] = tcp_option
        if lldp_transmission is not None:
            data_payload["lldp-transmission"] = lldp_transmission
        if lldp_reception is not None:
            data_payload["lldp-reception"] = lldp_reception
        if proxy_auth_timeout is not None:
            data_payload["proxy-auth-timeout"] = proxy_auth_timeout
        if proxy_keep_alive_mode is not None:
            data_payload["proxy-keep-alive-mode"] = proxy_keep_alive_mode
        if proxy_re_authentication_time is not None:
            data_payload["proxy-re-authentication-time"] = (
                proxy_re_authentication_time
            )
        if proxy_auth_lifetime is not None:
            data_payload["proxy-auth-lifetime"] = proxy_auth_lifetime
        if proxy_auth_lifetime_timeout is not None:
            data_payload["proxy-auth-lifetime-timeout"] = (
                proxy_auth_lifetime_timeout
            )
        if proxy_resource_mode is not None:
            data_payload["proxy-resource-mode"] = proxy_resource_mode
        if proxy_cert_use_mgmt_vdom is not None:
            data_payload["proxy-cert-use-mgmt-vdom"] = proxy_cert_use_mgmt_vdom
        if sys_perf_log_interval is not None:
            data_payload["sys-perf-log-interval"] = sys_perf_log_interval
        if check_protocol_header is not None:
            data_payload["check-protocol-header"] = check_protocol_header
        if vip_arp_range is not None:
            data_payload["vip-arp-range"] = vip_arp_range
        if reset_sessionless_tcp is not None:
            data_payload["reset-sessionless-tcp"] = reset_sessionless_tcp
        if allow_traffic_redirect is not None:
            data_payload["allow-traffic-redirect"] = allow_traffic_redirect
        if ipv6_allow_traffic_redirect is not None:
            data_payload["ipv6-allow-traffic-redirect"] = (
                ipv6_allow_traffic_redirect
            )
        if strict_dirty_session_check is not None:
            data_payload["strict-dirty-session-check"] = (
                strict_dirty_session_check
            )
        if tcp_halfclose_timer is not None:
            data_payload["tcp-halfclose-timer"] = tcp_halfclose_timer
        if tcp_halfopen_timer is not None:
            data_payload["tcp-halfopen-timer"] = tcp_halfopen_timer
        if tcp_timewait_timer is not None:
            data_payload["tcp-timewait-timer"] = tcp_timewait_timer
        if tcp_rst_timer is not None:
            data_payload["tcp-rst-timer"] = tcp_rst_timer
        if udp_idle_timer is not None:
            data_payload["udp-idle-timer"] = udp_idle_timer
        if block_session_timer is not None:
            data_payload["block-session-timer"] = block_session_timer
        if ip_src_port_range is not None:
            data_payload["ip-src-port-range"] = ip_src_port_range
        if pre_login_banner is not None:
            data_payload["pre-login-banner"] = pre_login_banner
        if post_login_banner is not None:
            data_payload["post-login-banner"] = post_login_banner
        if tftp is not None:
            data_payload["tftp"] = tftp
        if av_failopen is not None:
            data_payload["av-failopen"] = av_failopen
        if av_failopen_session is not None:
            data_payload["av-failopen-session"] = av_failopen_session
        if memory_use_threshold_extreme is not None:
            data_payload["memory-use-threshold-extreme"] = (
                memory_use_threshold_extreme
            )
        if memory_use_threshold_red is not None:
            data_payload["memory-use-threshold-red"] = memory_use_threshold_red
        if memory_use_threshold_green is not None:
            data_payload["memory-use-threshold-green"] = (
                memory_use_threshold_green
            )
        if ip_fragment_mem_thresholds is not None:
            data_payload["ip-fragment-mem-thresholds"] = (
                ip_fragment_mem_thresholds
            )
        if ip_fragment_timeout is not None:
            data_payload["ip-fragment-timeout"] = ip_fragment_timeout
        if ipv6_fragment_timeout is not None:
            data_payload["ipv6-fragment-timeout"] = ipv6_fragment_timeout
        if cpu_use_threshold is not None:
            data_payload["cpu-use-threshold"] = cpu_use_threshold
        if log_single_cpu_high is not None:
            data_payload["log-single-cpu-high"] = log_single_cpu_high
        if check_reset_range is not None:
            data_payload["check-reset-range"] = check_reset_range
        if single_vdom_npuvlink is not None:
            data_payload["single-vdom-npuvlink"] = single_vdom_npuvlink
        if vdom_mode is not None:
            data_payload["vdom-mode"] = vdom_mode
        if long_vdom_name is not None:
            data_payload["long-vdom-name"] = long_vdom_name
        if upgrade_report is not None:
            data_payload["upgrade-report"] = upgrade_report
        if edit_vdom_prompt is not None:
            data_payload["edit-vdom-prompt"] = edit_vdom_prompt
        if admin_port is not None:
            data_payload["admin-port"] = admin_port
        if admin_sport is not None:
            data_payload["admin-sport"] = admin_sport
        if admin_host is not None:
            data_payload["admin-host"] = admin_host
        if admin_https_redirect is not None:
            data_payload["admin-https-redirect"] = admin_https_redirect
        if admin_hsts_max_age is not None:
            data_payload["admin-hsts-max-age"] = admin_hsts_max_age
        if admin_ssh_password is not None:
            data_payload["admin-ssh-password"] = admin_ssh_password
        if admin_restrict_local is not None:
            data_payload["admin-restrict-local"] = admin_restrict_local
        if admin_ssh_port is not None:
            data_payload["admin-ssh-port"] = admin_ssh_port
        if admin_ssh_grace_time is not None:
            data_payload["admin-ssh-grace-time"] = admin_ssh_grace_time
        if admin_ssh_v1 is not None:
            data_payload["admin-ssh-v1"] = admin_ssh_v1
        if admin_telnet is not None:
            data_payload["admin-telnet"] = admin_telnet
        if admin_telnet_port is not None:
            data_payload["admin-telnet-port"] = admin_telnet_port
        if admin_forticloud_sso_login is not None:
            data_payload["admin-forticloud-sso-login"] = (
                admin_forticloud_sso_login
            )
        if admin_forticloud_sso_default_profile is not None:
            data_payload["admin-forticloud-sso-default-profile"] = (
                admin_forticloud_sso_default_profile
            )
        if default_service_source_port is not None:
            data_payload["default-service-source-port"] = (
                default_service_source_port
            )
        if admin_reset_button is not None:
            data_payload["admin-reset-button"] = admin_reset_button
        if admin_server_cert is not None:
            data_payload["admin-server-cert"] = admin_server_cert
        if admin_https_pki_required is not None:
            data_payload["admin-https-pki-required"] = admin_https_pki_required
        if wifi_certificate is not None:
            data_payload["wifi-certificate"] = wifi_certificate
        if dhcp_lease_backup_interval is not None:
            data_payload["dhcp-lease-backup-interval"] = (
                dhcp_lease_backup_interval
            )
        if wifi_ca_certificate is not None:
            data_payload["wifi-ca-certificate"] = wifi_ca_certificate
        if auth_http_port is not None:
            data_payload["auth-http-port"] = auth_http_port
        if auth_https_port is not None:
            data_payload["auth-https-port"] = auth_https_port
        if auth_ike_saml_port is not None:
            data_payload["auth-ike-saml-port"] = auth_ike_saml_port
        if auth_keepalive is not None:
            data_payload["auth-keepalive"] = auth_keepalive
        if policy_auth_concurrent is not None:
            data_payload["policy-auth-concurrent"] = policy_auth_concurrent
        if auth_session_limit is not None:
            data_payload["auth-session-limit"] = auth_session_limit
        if auth_cert is not None:
            data_payload["auth-cert"] = auth_cert
        if clt_cert_req is not None:
            data_payload["clt-cert-req"] = clt_cert_req
        if fortiservice_port is not None:
            data_payload["fortiservice-port"] = fortiservice_port
        if cfg_save is not None:
            data_payload["cfg-save"] = cfg_save
        if cfg_revert_timeout is not None:
            data_payload["cfg-revert-timeout"] = cfg_revert_timeout
        if reboot_upon_config_restore is not None:
            data_payload["reboot-upon-config-restore"] = (
                reboot_upon_config_restore
            )
        if admin_scp is not None:
            data_payload["admin-scp"] = admin_scp
        if wireless_controller is not None:
            data_payload["wireless-controller"] = wireless_controller
        if wireless_controller_port is not None:
            data_payload["wireless-controller-port"] = wireless_controller_port
        if fortiextender_data_port is not None:
            data_payload["fortiextender-data-port"] = fortiextender_data_port
        if fortiextender is not None:
            data_payload["fortiextender"] = fortiextender
        if extender_controller_reserved_network is not None:
            data_payload["extender-controller-reserved-network"] = (
                extender_controller_reserved_network
            )
        if fortiextender_discovery_lockdown is not None:
            data_payload["fortiextender-discovery-lockdown"] = (
                fortiextender_discovery_lockdown
            )
        if fortiextender_vlan_mode is not None:
            data_payload["fortiextender-vlan-mode"] = fortiextender_vlan_mode
        if fortiextender_provision_on_authorization is not None:
            data_payload["fortiextender-provision-on-authorization"] = (
                fortiextender_provision_on_authorization
            )
        if switch_controller is not None:
            data_payload["switch-controller"] = switch_controller
        if switch_controller_reserved_network is not None:
            data_payload["switch-controller-reserved-network"] = (
                switch_controller_reserved_network
            )
        if dnsproxy_worker_count is not None:
            data_payload["dnsproxy-worker-count"] = dnsproxy_worker_count
        if url_filter_count is not None:
            data_payload["url-filter-count"] = url_filter_count
        if httpd_max_worker_count is not None:
            data_payload["httpd-max-worker-count"] = httpd_max_worker_count
        if proxy_worker_count is not None:
            data_payload["proxy-worker-count"] = proxy_worker_count
        if scanunit_count is not None:
            data_payload["scanunit-count"] = scanunit_count
        if proxy_hardware_acceleration is not None:
            data_payload["proxy-hardware-acceleration"] = (
                proxy_hardware_acceleration
            )
        if fgd_alert_subscription is not None:
            data_payload["fgd-alert-subscription"] = fgd_alert_subscription
        if ipsec_hmac_offload is not None:
            data_payload["ipsec-hmac-offload"] = ipsec_hmac_offload
        if ipv6_accept_dad is not None:
            data_payload["ipv6-accept-dad"] = ipv6_accept_dad
        if ipv6_allow_anycast_probe is not None:
            data_payload["ipv6-allow-anycast-probe"] = ipv6_allow_anycast_probe
        if ipv6_allow_multicast_probe is not None:
            data_payload["ipv6-allow-multicast-probe"] = (
                ipv6_allow_multicast_probe
            )
        if ipv6_allow_local_in_silent_drop is not None:
            data_payload["ipv6-allow-local-in-silent-drop"] = (
                ipv6_allow_local_in_silent_drop
            )
        if csr_ca_attribute is not None:
            data_payload["csr-ca-attribute"] = csr_ca_attribute
        if wimax_4g_usb is not None:
            data_payload["wimax-4g-usb"] = wimax_4g_usb
        if cert_chain_max is not None:
            data_payload["cert-chain-max"] = cert_chain_max
        if two_factor_ftk_expiry is not None:
            data_payload["two-factor-ftk-expiry"] = two_factor_ftk_expiry
        if two_factor_email_expiry is not None:
            data_payload["two-factor-email-expiry"] = two_factor_email_expiry
        if two_factor_sms_expiry is not None:
            data_payload["two-factor-sms-expiry"] = two_factor_sms_expiry
        if two_factor_fac_expiry is not None:
            data_payload["two-factor-fac-expiry"] = two_factor_fac_expiry
        if two_factor_ftm_expiry is not None:
            data_payload["two-factor-ftm-expiry"] = two_factor_ftm_expiry
        if wad_worker_count is not None:
            data_payload["wad-worker-count"] = wad_worker_count
        if wad_worker_dev_cache is not None:
            data_payload["wad-worker-dev-cache"] = wad_worker_dev_cache
        if wad_csvc_cs_count is not None:
            data_payload["wad-csvc-cs-count"] = wad_csvc_cs_count
        if wad_csvc_db_count is not None:
            data_payload["wad-csvc-db-count"] = wad_csvc_db_count
        if wad_source_affinity is not None:
            data_payload["wad-source-affinity"] = wad_source_affinity
        if wad_memory_change_granularity is not None:
            data_payload["wad-memory-change-granularity"] = (
                wad_memory_change_granularity
            )
        if login_timestamp is not None:
            data_payload["login-timestamp"] = login_timestamp
        if ip_conflict_detection is not None:
            data_payload["ip-conflict-detection"] = ip_conflict_detection
        if miglogd_children is not None:
            data_payload["miglogd-children"] = miglogd_children
        if log_daemon_cpu_threshold is not None:
            data_payload["log-daemon-cpu-threshold"] = log_daemon_cpu_threshold
        if special_file_23_support is not None:
            data_payload["special-file-23-support"] = special_file_23_support
        if log_uuid_address is not None:
            data_payload["log-uuid-address"] = log_uuid_address
        if log_ssl_connection is not None:
            data_payload["log-ssl-connection"] = log_ssl_connection
        if rest_api_key_url_query is not None:
            data_payload["rest-api-key-url-query"] = rest_api_key_url_query
        if gui_cdn_domain_override is not None:
            data_payload["gui-cdn-domain-override"] = gui_cdn_domain_override
        if arp_max_entry is not None:
            data_payload["arp-max-entry"] = arp_max_entry
        if ha_affinity is not None:
            data_payload["ha-affinity"] = ha_affinity
        if bfd_affinity is not None:
            data_payload["bfd-affinity"] = bfd_affinity
        if cmdbsvr_affinity is not None:
            data_payload["cmdbsvr-affinity"] = cmdbsvr_affinity
        if ndp_max_entry is not None:
            data_payload["ndp-max-entry"] = ndp_max_entry
        if br_fdb_max_entry is not None:
            data_payload["br-fdb-max-entry"] = br_fdb_max_entry
        if max_route_cache_size is not None:
            data_payload["max-route-cache-size"] = max_route_cache_size
        if ipsec_asic_offload is not None:
            data_payload["ipsec-asic-offload"] = ipsec_asic_offload
        if device_idle_timeout is not None:
            data_payload["device-idle-timeout"] = device_idle_timeout
        if user_device_store_max_devices is not None:
            data_payload["user-device-store-max-devices"] = (
                user_device_store_max_devices
            )
        if user_device_store_max_device_mem is not None:
            data_payload["user-device-store-max-device-mem"] = (
                user_device_store_max_device_mem
            )
        if user_device_store_max_users is not None:
            data_payload["user-device-store-max-users"] = (
                user_device_store_max_users
            )
        if user_device_store_max_unified_mem is not None:
            data_payload["user-device-store-max-unified-mem"] = (
                user_device_store_max_unified_mem
            )
        if gui_device_latitude is not None:
            data_payload["gui-device-latitude"] = gui_device_latitude
        if gui_device_longitude is not None:
            data_payload["gui-device-longitude"] = gui_device_longitude
        if private_data_encryption is not None:
            data_payload["private-data-encryption"] = private_data_encryption
        if auto_auth_extension_device is not None:
            data_payload["auto-auth-extension-device"] = (
                auto_auth_extension_device
            )
        if gui_theme is not None:
            data_payload["gui-theme"] = gui_theme
        if gui_date_format is not None:
            data_payload["gui-date-format"] = gui_date_format
        if gui_date_time_source is not None:
            data_payload["gui-date-time-source"] = gui_date_time_source
        if igmp_state_limit is not None:
            data_payload["igmp-state-limit"] = igmp_state_limit
        if cloud_communication is not None:
            data_payload["cloud-communication"] = cloud_communication
        if ipsec_ha_seqjump_rate is not None:
            data_payload["ipsec-ha-seqjump-rate"] = ipsec_ha_seqjump_rate
        if fortitoken_cloud is not None:
            data_payload["fortitoken-cloud"] = fortitoken_cloud
        if fortitoken_cloud_push_status is not None:
            data_payload["fortitoken-cloud-push-status"] = (
                fortitoken_cloud_push_status
            )
        if fortitoken_cloud_region is not None:
            data_payload["fortitoken-cloud-region"] = fortitoken_cloud_region
        if fortitoken_cloud_sync_interval is not None:
            data_payload["fortitoken-cloud-sync-interval"] = (
                fortitoken_cloud_sync_interval
            )
        if faz_disk_buffer_size is not None:
            data_payload["faz-disk-buffer-size"] = faz_disk_buffer_size
        if irq_time_accounting is not None:
            data_payload["irq-time-accounting"] = irq_time_accounting
        if management_ip is not None:
            data_payload["management-ip"] = management_ip
        if management_port is not None:
            data_payload["management-port"] = management_port
        if management_port_use_admin_sport is not None:
            data_payload["management-port-use-admin-sport"] = (
                management_port_use_admin_sport
            )
        if forticonverter_integration is not None:
            data_payload["forticonverter-integration"] = (
                forticonverter_integration
            )
        if forticonverter_config_upload is not None:
            data_payload["forticonverter-config-upload"] = (
                forticonverter_config_upload
            )
        if internet_service_database is not None:
            data_payload["internet-service-database"] = (
                internet_service_database
            )
        if internet_service_download_list is not None:
            data_payload["internet-service-download-list"] = (
                internet_service_download_list
            )
        if geoip_full_db is not None:
            data_payload["geoip-full-db"] = geoip_full_db
        if early_tcp_npu_session is not None:
            data_payload["early-tcp-npu-session"] = early_tcp_npu_session
        if npu_neighbor_update is not None:
            data_payload["npu-neighbor-update"] = npu_neighbor_update
        if delay_tcp_npu_session is not None:
            data_payload["delay-tcp-npu-session"] = delay_tcp_npu_session
        if interface_subnet_usage is not None:
            data_payload["interface-subnet-usage"] = interface_subnet_usage
        if sflowd_max_children_num is not None:
            data_payload["sflowd-max-children-num"] = sflowd_max_children_num
        if fortigslb_integration is not None:
            data_payload["fortigslb-integration"] = fortigslb_integration
        if user_history_password_threshold is not None:
            data_payload["user-history-password-threshold"] = (
                user_history_password_threshold
            )
        if auth_session_auto_backup is not None:
            data_payload["auth-session-auto-backup"] = auth_session_auto_backup
        if auth_session_auto_backup_interval is not None:
            data_payload["auth-session-auto-backup-interval"] = (
                auth_session_auto_backup_interval
            )
        if scim_https_port is not None:
            data_payload["scim-https-port"] = scim_https_port
        if scim_http_port is not None:
            data_payload["scim-http-port"] = scim_http_port
        if scim_server_cert is not None:
            data_payload["scim-server-cert"] = scim_server_cert
        if application_bandwidth_tracking is not None:
            data_payload["application-bandwidth-tracking"] = (
                application_bandwidth_tracking
            )
        if tls_session_cache is not None:
            data_payload["tls-session-cache"] = tls_session_cache
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

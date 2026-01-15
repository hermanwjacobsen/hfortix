from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for system/global_ payload fields.
    
    Configure global attributes.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: wifi-ca-certificate)
        - :class:`~.certificate.local.LocalEndpoint` (via: admin-server-cert, auth-cert, scim-server-cert, +1 more)
        - :class:`~.system.accprofile.AccprofileEndpoint` (via: admin-forticloud-sso-default-profile)
        - :class:`~.system.timezone.TimezoneEndpoint` (via: timezone)
        - :class:`~.system.vdom.VdomEndpoint` (via: management-vdom)

    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"]  # GUI display language. | Default: english
    gui_ipv6: Literal["enable", "disable"]  # Enable/disable IPv6 settings on the GUI. | Default: disable
    gui_replacement_message_groups: Literal["enable", "disable"]  # Enable/disable replacement message groups on the G | Default: disable
    gui_local_out: Literal["enable", "disable"]  # Enable/disable Local-out traffic on the GUI. | Default: disable
    gui_certificates: Literal["enable", "disable"]  # Enable/disable the System > Certificate GUI page, | Default: enable
    gui_custom_language: Literal["enable", "disable"]  # Enable/disable custom languages in GUI. | Default: disable
    gui_wireless_opensecurity: Literal["enable", "disable"]  # Enable/disable wireless open security option on th | Default: disable
    gui_app_detection_sdwan: Literal["enable", "disable"]  # Enable/disable Allow app-detection based SD-WAN. | Default: disable
    gui_display_hostname: Literal["enable", "disable"]  # Enable/disable displaying the FortiGate's hostname | Default: disable
    gui_fortigate_cloud_sandbox: Literal["enable", "disable"]  # Enable/disable displaying FortiGate Cloud Sandbox | Default: disable
    gui_firmware_upgrade_warning: Literal["enable", "disable"]  # Enable/disable the firmware upgrade warning on the | Default: enable
    gui_forticare_registration_setup_warning: Literal["enable", "disable"]  # Enable/disable the FortiCare registration setup wa | Default: enable
    gui_auto_upgrade_setup_warning: Literal["enable", "disable"]  # Enable/disable the automatic patch upgrade setup p | Default: enable
    gui_workflow_management: Literal["enable", "disable"]  # Enable/disable Workflow management features on the | Default: disable
    gui_cdn_usage: Literal["enable", "disable"]  # Enable/disable Load GUI static files from a CDN. | Default: enable
    admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"]  # Allowed TLS versions for web administration. | Default: tlsv1-2 tlsv1-3
    admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"]  # Select one or more TLS 1.3 ciphersuites to enable. | Default: TLS-AES-128-GCM-SHA256 TLS-AES-256-GCM-SHA384 TLS-CHACHA20-POLY1305-SHA256
    admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"]  # Select one or more cipher technologies that cannot
    admintimeout: int  # Number of minutes before an idle administrator ses | Default: 5 | Min: 1 | Max: 480
    admin_console_timeout: int  # Console login timeout that overrides the admin tim | Default: 0 | Min: 15 | Max: 300
    ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"]  # How often to run SSD Trim (default = weekly). SSD | Default: weekly
    ssd_trim_hour: int  # Hour of the day on which to run SSD Trim | Default: 1 | Min: 0 | Max: 23
    ssd_trim_min: int  # Minute of the hour on which to run SSD Trim | Default: 60 | Min: 0 | Max: 60
    ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of week to run SSD Trim. | Default: sunday
    ssd_trim_date: int  # Date within a month to run ssd trim. | Default: 1 | Min: 1 | Max: 31
    admin_concurrent: Literal["enable", "disable"]  # Enable/disable concurrent administrator logins. Us | Default: enable
    admin_lockout_threshold: int  # Number of failed login attempts before an administ | Default: 3 | Min: 1 | Max: 10
    admin_lockout_duration: int  # Amount of time in seconds that an administrator ac | Default: 60 | Min: 1 | Max: 2147483647
    refresh: int  # Statistics refresh interval second(s) in GUI. | Default: 0 | Min: 0 | Max: 4294967295
    interval: int  # Dead gateway detection interval. | Default: 5 | Min: 0 | Max: 4294967295
    failtime: int  # Fail-time for server lost. | Default: 5 | Min: 0 | Max: 4294967295
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # Purdue Level of this FortiGate. | Default: 3
    daily_restart: Literal["enable", "disable"]  # Enable/disable daily restart of FortiGate unit. Us | Default: disable
    restart_time: str  # Daily restart time (hh:mm).
    wad_restart_mode: Literal["none", "time", "memory"]  # WAD worker restart mode (default = none). | Default: none
    wad_restart_start_time: str  # WAD workers daily restart time (hh:mm).
    wad_restart_end_time: str  # WAD workers daily restart end time (hh:mm).
    wad_p2s_max_body_size: int  # Maximum size of the body of the local out HTTP req | Default: 4 | Min: 1 | Max: 32
    radius_port: int  # RADIUS service port number. | Default: 1812 | Min: 1 | Max: 65535
    speedtestd_server_port: int  # Speedtest server port number. | Default: 5201 | Min: 1 | Max: 65535
    speedtestd_ctrl_port: int  # Speedtest server controller port number. | Default: 5200 | Min: 1 | Max: 65535
    admin_login_max: int  # Maximum number of administrators who can be logged | Default: 100 | Min: 1 | Max: 100
    remoteauthtimeout: int  # Number of seconds that the FortiGate waits for res | Default: 5 | Min: 1 | Max: 300
    ldapconntimeout: int  # Global timeout for connections with remote LDAP se | Default: 500 | Min: 1 | Max: 300000
    batch_cmdb: Literal["enable", "disable"]  # Enable/disable batch mode, allowing you to enter a | Default: enable
    multi_factor_authentication: Literal["optional", "mandatory"]  # Enforce all login methods to require an additional | Default: optional
    ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: TLSv1-2
    autorun_log_fsck: Literal["enable", "disable"]  # Enable/disable automatic log partition check after | Default: disable
    timezone: str  # Timezone database name. Enter ? to view the list o | MaxLen: 63
    traffic_priority: Literal["tos", "dscp"]  # Choose Type of Service (ToS) or Differentiated Ser | Default: tos
    traffic_priority_level: Literal["low", "medium", "high"]  # Default system-wide level of priority for traffic | Default: medium
    quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"]  # QUIC congestion control algorithm | Default: cubic
    quic_max_datagram_size: int  # Maximum transmit datagram size | Default: 1500 | Min: 1200 | Max: 1500
    quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"]  # Enable/disable UDP payload size shaping per connec | Default: enable
    quic_ack_thresold: int  # Maximum number of unacknowledged packets before se | Default: 3 | Min: 2 | Max: 5
    quic_pmtud: Literal["enable", "disable"]  # Enable/disable path MTU discovery | Default: enable
    quic_tls_handshake_timeout: int  # Time-to-live (TTL) for TLS handshake in seconds | Default: 5 | Min: 1 | Max: 60
    anti_replay: Literal["disable", "loose", "strict"]  # Level of checking for packet replay and TCP sequen | Default: strict
    send_pmtu_icmp: Literal["enable", "disable"]  # Enable/disable sending of path maximum transmissio | Default: enable
    honor_df: Literal["enable", "disable"]  # Enable/disable honoring of Don't-Fragment (DF) fla | Default: enable
    pmtu_discovery: Literal["enable", "disable"]  # Enable/disable path MTU discovery. | Default: disable
    revision_image_auto_backup: Literal["enable", "disable"]  # Enable/disable back-up of the latest image revisio | Default: disable
    revision_backup_on_logout: Literal["enable", "disable"]  # Enable/disable back-up of the latest configuration | Default: disable
    management_vdom: str  # Management virtual domain name. | Default: root | MaxLen: 31
    hostname: str  # FortiGate unit's hostname. Most models will trunca | MaxLen: 35
    alias: str  # Alias for your FortiGate unit. | MaxLen: 35
    strong_crypto: Literal["enable", "disable"]  # Enable to use strong encryption and only allow str | Default: enable
    ssl_static_key_ciphers: Literal["enable", "disable"]  # Enable/disable static key ciphers in SSL/TLS conne | Default: enable
    snat_route_change: Literal["enable", "disable"]  # Enable/disable the ability to change the source NA | Default: disable
    ipv6_snat_route_change: Literal["enable", "disable"]  # Enable/disable the ability to change the IPv6 sour | Default: disable
    speedtest_server: Literal["enable", "disable"]  # Enable/disable speed test server. | Default: disable
    cli_audit_log: Literal["enable", "disable"]  # Enable/disable CLI audit log. | Default: disable
    dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    fds_statistics: Literal["enable", "disable"]  # Enable/disable sending IPS, Application Control, a | Default: enable
    fds_statistics_period: int  # FortiGuard statistics collection period in minutes | Default: 60 | Min: 1 | Max: 1440
    tcp_option: Literal["enable", "disable"]  # Enable SACK, timestamp and MSS TCP options. | Default: enable
    lldp_transmission: Literal["enable", "disable"]  # Enable/disable Link Layer Discovery Protocol | Default: disable
    lldp_reception: Literal["enable", "disable"]  # Enable/disable Link Layer Discovery Protocol | Default: disable
    proxy_auth_timeout: int  # Authentication timeout in minutes for authenticate | Default: 10 | Min: 1 | Max: 10000
    proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"]  # Control if users must re-authenticate after a sess | Default: session
    proxy_re_authentication_time: int  # The time limit that users must re-authenticate if | Default: 30 | Min: 1 | Max: 86400
    proxy_auth_lifetime: Literal["enable", "disable"]  # Enable/disable authenticated users lifetime contro | Default: disable
    proxy_auth_lifetime_timeout: int  # Lifetime timeout in minutes for authenticated user | Default: 480 | Min: 5 | Max: 65535
    proxy_resource_mode: Literal["enable", "disable"]  # Enable/disable use of the maximum memory usage on | Default: disable
    proxy_cert_use_mgmt_vdom: Literal["enable", "disable"]  # Enable/disable using management VDOM to send reque | Default: disable
    sys_perf_log_interval: int  # Time in minutes between updates of performance sta | Default: 5 | Min: 0 | Max: 15
    check_protocol_header: Literal["loose", "strict"]  # Level of checking performed on protocol headers. S | Default: loose
    vip_arp_range: Literal["unlimited", "restricted"]  # Controls the number of ARPs that the FortiGate sen | Default: restricted
    reset_sessionless_tcp: Literal["enable", "disable"]  # Action to perform if the FortiGate receives a TCP | Default: disable
    allow_traffic_redirect: Literal["enable", "disable"]  # Disable to prevent traffic with same local ingress | Default: disable
    ipv6_allow_traffic_redirect: Literal["enable", "disable"]  # Disable to prevent IPv6 traffic with same local in | Default: disable
    strict_dirty_session_check: Literal["enable", "disable"]  # Enable to check the session against the original p | Default: enable
    tcp_halfclose_timer: int  # Number of seconds the FortiGate unit should wait t | Default: 120 | Min: 1 | Max: 86400
    tcp_halfopen_timer: int  # Number of seconds the FortiGate unit should wait t | Default: 10 | Min: 1 | Max: 86400
    tcp_timewait_timer: int  # Length of the TCP TIME-WAIT state in seconds | Default: 1 | Min: 0 | Max: 300
    tcp_rst_timer: int  # Length of the TCP CLOSE state in seconds | Default: 5 | Min: 5 | Max: 300
    udp_idle_timer: int  # UDP connection session timeout. This command can b | Default: 180 | Min: 1 | Max: 86400
    block_session_timer: int  # Duration in seconds for blocked sessions | Default: 30 | Min: 1 | Max: 300
    ip_src_port_range: str  # IP source port range used for traffic originating | Default: 1024-25000
    pre_login_banner: Literal["enable", "disable"]  # Enable/disable displaying the administrator access | Default: disable
    post_login_banner: Literal["disable", "enable"]  # Enable/disable displaying the administrator access | Default: disable
    tftp: Literal["enable", "disable"]  # Enable/disable TFTP. | Default: enable
    av_failopen: Literal["pass", "off", "one-shot"]  # Set the action to take if the FortiGate is running | Default: pass
    av_failopen_session: Literal["enable", "disable"]  # When enabled and a proxy for a protocol runs out o | Default: disable
    memory_use_threshold_extreme: int  # Threshold at which memory usage is considered extr | Default: 95 | Min: 70 | Max: 97
    memory_use_threshold_red: int  # Threshold at which memory usage forces the FortiGa | Default: 88 | Min: 70 | Max: 97
    memory_use_threshold_green: int  # Threshold at which memory usage forces the FortiGa | Default: 82 | Min: 70 | Max: 97
    ip_fragment_mem_thresholds: int  # Maximum memory (MB) used to reassemble IPv4/IPv6 f | Default: 32 | Min: 32 | Max: 2047
    ip_fragment_timeout: int  # Timeout value in seconds for any fragment not bein | Default: 30 | Min: 3 | Max: 30
    ipv6_fragment_timeout: int  # Timeout value in seconds for any IPv6 fragment not | Default: 60 | Min: 5 | Max: 60
    cpu_use_threshold: int  # Threshold at which CPU usage is reported | Default: 90 | Min: 50 | Max: 99
    log_single_cpu_high: Literal["enable", "disable"]  # Enable/disable logging the event of a single CPU c | Default: disable
    check_reset_range: Literal["strict", "disable"]  # Configure ICMP error message verification. You can | Default: disable
    upgrade_report: Literal["enable", "disable"]  # Enable/disable the generation of an upgrade report | Default: enable
    admin_port: int  # Administrative access port for HTTP. | Default: 80 | Min: 1 | Max: 65535
    admin_sport: int  # Administrative access port for HTTPS. | Default: 443 | Min: 1 | Max: 65535
    admin_host: str  # Administrative host for HTTP and HTTPS. When set, | MaxLen: 255
    admin_https_redirect: Literal["enable", "disable"]  # Enable/disable redirection of HTTP administration | Default: enable
    admin_hsts_max_age: int  # HTTPS Strict-Transport-Security header max-age in | Default: 63072000 | Min: 0 | Max: 2147483647
    admin_ssh_password: Literal["enable", "disable"]  # Enable/disable password authentication for SSH adm | Default: enable
    admin_restrict_local: Literal["all", "non-console-only", "disable"]  # Enable/disable local admin authentication restrict | Default: disable
    admin_ssh_port: int  # Administrative access port for SSH. | Default: 22 | Min: 1 | Max: 65535
    admin_ssh_grace_time: int  # Maximum time in seconds permitted between making a | Default: 120 | Min: 10 | Max: 3600
    admin_ssh_v1: Literal["enable", "disable"]  # Enable/disable SSH v1 compatibility. | Default: disable
    admin_telnet: Literal["enable", "disable"]  # Enable/disable TELNET service. | Default: enable
    admin_telnet_port: int  # Administrative access port for TELNET. | Default: 23 | Min: 1 | Max: 65535
    admin_forticloud_sso_login: Literal["enable", "disable"]  # Enable/disable FortiCloud admin login via SSO. | Default: disable
    admin_forticloud_sso_default_profile: str  # Override access profile. | MaxLen: 35
    default_service_source_port: str  # Default service source port range
    admin_server_cert: str  # Server certificate that the FortiGate uses for HTT | Default: Fortinet_GUI_Server | MaxLen: 35
    admin_https_pki_required: Literal["enable", "disable"]  # Enable/disable admin login method. Enable to force | Default: disable
    wifi_certificate: str  # Certificate to use for WiFi authentication. | Default: Fortinet_Wifi | MaxLen: 35
    dhcp_lease_backup_interval: int  # DHCP leases backup interval in seconds | Default: 60 | Min: 10 | Max: 3600
    wifi_ca_certificate: str  # CA certificate that verifies the WiFi certificate. | Default: Fortinet_Wifi_CA | MaxLen: 79
    auth_http_port: int  # User authentication HTTP port. | Default: 1000 | Min: 1 | Max: 65535
    auth_https_port: int  # User authentication HTTPS port. | Default: 1003 | Min: 1 | Max: 65535
    auth_ike_saml_port: int  # User IKE SAML authentication port | Default: 1001 | Min: 0 | Max: 65535
    auth_keepalive: Literal["enable", "disable"]  # Enable to prevent user authentication sessions fro | Default: disable
    policy_auth_concurrent: int  # Number of concurrent firewall use logins from the | Default: 0 | Min: 0 | Max: 100
    auth_session_limit: Literal["block-new", "logout-inactive"]  # Action to take when the number of allowed user aut | Default: block-new
    auth_cert: str  # Server certificate that the FortiGate uses for HTT | Default: Fortinet_Factory | MaxLen: 35
    clt_cert_req: Literal["enable", "disable"]  # Enable/disable requiring administrators to have a | Default: disable
    fortiservice_port: int  # FortiService port (1 - 65535, default = 8013). Use | Default: 8013 | Min: 1 | Max: 65535
    cfg_save: Literal["automatic", "manual", "revert"]  # Configuration file save mode for CLI changes. | Default: automatic
    cfg_revert_timeout: int  # Time-out for reverting to the last saved configura | Default: 600 | Min: 10 | Max: 4294967295
    reboot_upon_config_restore: Literal["enable", "disable"]  # Enable/disable reboot of system upon restoring con | Default: enable
    admin_scp: Literal["enable", "disable"]  # Enable/disable SCP support for system configuratio | Default: disable
    wireless_controller: Literal["enable", "disable"]  # Enable/disable the wireless controller feature to | Default: enable
    wireless_controller_port: int  # Port used for the control channel in wireless cont | Default: 5246 | Min: 1024 | Max: 49150
    fortiextender_data_port: int  # FortiExtender data port | Default: 25246 | Min: 1024 | Max: 49150
    fortiextender: Literal["disable", "enable"]  # Enable/disable FortiExtender. | Default: disable
    extender_controller_reserved_network: str  # Configure reserved network subnet for managed LAN | Default: 10.252.0.1 255.255.0.0
    fortiextender_discovery_lockdown: Literal["disable", "enable"]  # Enable/disable FortiExtender CAPWAP lockdown. | Default: disable
    fortiextender_vlan_mode: Literal["enable", "disable"]  # Enable/disable FortiExtender VLAN mode. | Default: disable
    fortiextender_provision_on_authorization: Literal["enable", "disable"]  # Enable/disable automatic provisioning of latest Fo | Default: disable
    switch_controller: Literal["disable", "enable"]  # Enable/disable switch controller feature. Switch c | Default: disable
    switch_controller_reserved_network: str  # Configure reserved network subnet for managed swit | Default: 10.255.0.1 255.255.0.0
    dnsproxy_worker_count: int  # DNS proxy worker count. For a FortiGate with multi | Default: 1 | Min: 1 | Max: 2
    url_filter_count: int  # URL filter daemon count. | Default: 1 | Min: 1 | Max: 1
    httpd_max_worker_count: int  # Maximum number of simultaneous HTTP requests that | Default: 0 | Min: 0 | Max: 128
    proxy_worker_count: int  # Proxy worker count. | Default: 0 | Min: 1 | Max: 2
    scanunit_count: int  # Number of scanunits. The range and the default dep | Default: 0 | Min: 2 | Max: 2
    fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"]  # Type of alert to retrieve from FortiGuard.
    ipv6_accept_dad: int  # Enable/disable acceptance of IPv6 Duplicate Addres | Default: 1 | Min: 0 | Max: 2
    ipv6_allow_anycast_probe: Literal["enable", "disable"]  # Enable/disable IPv6 address probe through Anycast. | Default: disable
    ipv6_allow_multicast_probe: Literal["enable", "disable"]  # Enable/disable IPv6 address probe through Multicas | Default: disable
    ipv6_allow_local_in_silent_drop: Literal["enable", "disable"]  # Enable/disable silent drop of IPv6 local-in traffi | Default: enable
    csr_ca_attribute: Literal["enable", "disable"]  # Enable/disable the CA attribute in certificates. S | Default: enable
    wimax_4g_usb: Literal["enable", "disable"]  # Enable/disable comparability with WiMAX 4G USB dev | Default: disable
    cert_chain_max: int  # Maximum number of certificates that can be travers | Default: 8 | Min: 1 | Max: 2147483647
    sslvpn_max_worker_count: int  # Maximum number of Agentless VPN processes. Upper l | Default: 0 | Min: 0 | Max: 1
    sslvpn_affinity: str  # Agentless VPN CPU affinity. | Default: 0 | MaxLen: 79
    sslvpn_web_mode: Literal["enable", "disable"]  # Enable/disable Agentless VPN web mode. | Default: disable
    two_factor_ftk_expiry: int  # FortiToken authentication session timeout | Default: 60 | Min: 60 | Max: 600
    two_factor_email_expiry: int  # Email-based two-factor authentication session time | Default: 60 | Min: 30 | Max: 300
    two_factor_sms_expiry: int  # SMS-based two-factor authentication session timeou | Default: 60 | Min: 30 | Max: 300
    two_factor_fac_expiry: int  # FortiAuthenticator token authentication session ti | Default: 60 | Min: 10 | Max: 3600
    two_factor_ftm_expiry: int  # FortiToken Mobile session timeout (1 - 168 hours | Default: 72 | Min: 1 | Max: 168
    per_user_bal: Literal["enable", "disable"]  # Enable/disable per-user block/allow list filter. | Default: disable
    wad_worker_count: int  # Number of explicit proxy WAN optimization daemon | Default: 0 | Min: 0 | Max: 2
    wad_worker_dev_cache: int  # Number of cached devices for each ZTNA proxy worke | Default: 10240 | Min: 0 | Max: 10240
    wad_csvc_cs_count: int  # Number of concurrent WAD-cache-service object-cach | Default: 1 | Min: 1 | Max: 1
    wad_csvc_db_count: int  # Number of concurrent WAD-cache-service byte-cache | Default: 0 | Min: 0 | Max: 2
    wad_source_affinity: Literal["disable", "enable"]  # Enable/disable dispatching traffic to WAD workers | Default: enable
    wad_memory_change_granularity: int  # Minimum percentage change in system memory usage d | Default: 10 | Min: 5 | Max: 25
    login_timestamp: Literal["enable", "disable"]  # Enable/disable login time recording. | Default: disable
    ip_conflict_detection: Literal["enable", "disable"]  # Enable/disable logging of IPv4 address conflict de | Default: disable
    miglogd_children: int  # Number of logging (miglogd) processes to be allowe | Default: 0 | Min: 0 | Max: 15
    log_daemon_cpu_threshold: int  # Configure syslog daemon process spawning threshold | Default: 0 | Min: 0 | Max: 99
    special_file_23_support: Literal["disable", "enable"]  # Enable/disable detection of those special format f | Default: disable
    log_uuid_address: Literal["enable", "disable"]  # Enable/disable insertion of address UUIDs to traff | Default: disable
    log_ssl_connection: Literal["enable", "disable"]  # Enable/disable logging of SSL connection events. | Default: disable
    gui_rest_api_cache: Literal["enable", "disable"]  # Enable/disable REST API result caching on FortiGat | Default: enable
    rest_api_key_url_query: Literal["enable", "disable"]  # Enable/disable support for passing REST API keys t | Default: disable
    arp_max_entry: int  # Maximum number of dynamically learned MAC addresse | Default: 131072 | Min: 131072 | Max: 2147483647
    ha_affinity: str  # Affinity setting for HA daemons | Default: 1 | MaxLen: 79
    bfd_affinity: str  # Affinity setting for BFD daemon | Default: 1 | MaxLen: 79
    cmdbsvr_affinity: str  # Affinity setting for cmdbsvr | Default: 1 | MaxLen: 79
    av_affinity: str  # Affinity setting for AV scanning | Default: 0 | MaxLen: 79
    wad_affinity: str  # Affinity setting for wad | Default: 0 | MaxLen: 79
    ips_affinity: str  # Affinity setting for IPS | Default: 0 | MaxLen: 79
    miglog_affinity: str  # Affinity setting for logging | Default: 0 | MaxLen: 79
    syslog_affinity: str  # Affinity setting for syslog | Default: 0 | MaxLen: 79
    url_filter_affinity: str  # URL filter CPU affinity. | Default: 0 | MaxLen: 79
    router_affinity: str  # Affinity setting for BFD/VRRP/BGP/OSPF daemons | Default: 0 | MaxLen: 79
    ndp_max_entry: int  # Maximum number of NDP table entries | Default: 0 | Min: 65536 | Max: 2147483647
    br_fdb_max_entry: int  # Maximum number of bridge forwarding database (FDB) | Default: 8192 | Min: 8192 | Max: 2147483647
    max_route_cache_size: int  # Maximum number of IP route cache entries | Default: 0 | Min: 0 | Max: 2147483647
    ipsec_qat_offload: Literal["enable", "disable"]  # Enable/disable QAT offloading (Intel QuickAssist) | Default: enable
    device_idle_timeout: int  # Time in seconds that a device must be idle to auto | Default: 300 | Min: 30 | Max: 31536000
    user_device_store_max_devices: int  # Maximum number of devices allowed in user device s | Default: 62524 | Min: 31262 | Max: 89320
    user_device_store_max_device_mem: int  # Maximum percentage of total system memory allowed | Default: 2 | Min: 1 | Max: 5
    user_device_store_max_users: int  # Maximum number of users allowed in user device sto | Default: 62524 | Min: 31262 | Max: 89320
    user_device_store_max_unified_mem: int  # Maximum unified memory allowed in user device stor | Default: 312621670 | Min: 62524334 | Max: 625243340
    gui_device_latitude: str  # Add the latitude of the location of this FortiGate | MaxLen: 19
    gui_device_longitude: str  # Add the longitude of the location of this FortiGat | MaxLen: 19
    private_data_encryption: Literal["disable", "enable"]  # Enable/disable private data encryption using an AE | Default: disable
    auto_auth_extension_device: Literal["enable", "disable"]  # Enable/disable automatic authorization of dedicate | Default: enable
    gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"]  # Color scheme for the administration GUI. | Default: jade
    gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"]  # Default date format used throughout GUI. | Default: yyyy/MM/dd
    gui_date_time_source: Literal["system", "browser"]  # Source from which the FortiGate GUI uses to displa | Default: system
    igmp_state_limit: int  # Maximum number of IGMP memberships | Default: 3200 | Min: 96 | Max: 128000
    cloud_communication: Literal["enable", "disable"]  # Enable/disable all cloud communication. | Default: enable
    ipsec_ha_seqjump_rate: int  # ESP jump ahead rate (1G - 10G pps equivalent). | Default: 10 | Min: 1 | Max: 10
    fortitoken_cloud: Literal["enable", "disable"]  # Enable/disable FortiToken Cloud service. | Default: enable
    fortitoken_cloud_push_status: Literal["enable", "disable"]  # Enable/disable FTM push service of FortiToken Clou | Default: enable
    fortitoken_cloud_region: str  # Region domain of FortiToken Cloud | MaxLen: 63
    fortitoken_cloud_sync_interval: int  # Interval in which to clean up remote users in Fort | Default: 24 | Min: 0 | Max: 336
    faz_disk_buffer_size: int  # Maximum disk buffer size to temporarily store logs | Default: 0
    irq_time_accounting: Literal["auto", "force"]  # Configure CPU IRQ time accounting mode. | Default: auto
    management_ip: str  # Management IP address of this FortiGate. Used to l | MaxLen: 255
    management_port: int  # Overriding port for management connection | Default: 443 | Min: 1 | Max: 65535
    management_port_use_admin_sport: Literal["enable", "disable"]  # Enable/disable use of the admin-sport setting for | Default: enable
    forticonverter_integration: Literal["enable", "disable"]  # Enable/disable FortiConverter integration service. | Default: disable
    forticonverter_config_upload: Literal["once", "disable"]  # Enable/disable config upload to FortiConverter. | Default: disable
    internet_service_database: Literal["mini", "standard", "full", "on-demand"]  # Configure which Internet Service database size to | Default: full
    internet_service_download_list: list[dict[str, Any]]  # Configure which on-demand Internet Service IDs are
    geoip_full_db: Literal["enable", "disable"]  # When enabled, the full geographic database will be | Default: enable
    early_tcp_npu_session: Literal["enable", "disable"]  # Enable/disable early TCP NPU session. | Default: disable
    npu_neighbor_update: Literal["enable", "disable"]  # Enable/disable sending of ARP/ICMP6 probing packet | Default: disable
    delay_tcp_npu_session: Literal["enable", "disable"]  # Enable TCP NPU session delay to guarantee packet o | Default: disable
    interface_subnet_usage: Literal["disable", "enable"]  # Enable/disable allowing use of interface-subnet se | Default: enable
    sflowd_max_children_num: int  # Maximum number of sflowd child processes allowed t | Default: 1 | Min: 0 | Max: 1
    fortigslb_integration: Literal["disable", "enable"]  # Enable/disable integration with the FortiGSLB clou | Default: disable
    user_history_password_threshold: int  # Maximum number of previous passwords saved per adm | Default: 3 | Min: 3 | Max: 15
    auth_session_auto_backup: Literal["enable", "disable"]  # Enable/disable automatic and periodic backup of au | Default: disable
    auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"]  # Configure automatic authentication session backup | Default: 15min
    scim_https_port: int  # SCIM port (0 - 65535, default = 44559). | Default: 44559 | Min: 0 | Max: 65535
    scim_http_port: int  # SCIM http port (0 - 65535, default = 44558). | Default: 44558 | Min: 0 | Max: 65535
    scim_server_cert: str  # Server certificate that the FortiGate uses for SCI | Default: Fortinet_Factory | MaxLen: 35
    application_bandwidth_tracking: Literal["disable", "enable"]  # Enable/disable application bandwidth tracking. | Default: disable
    tls_session_cache: Literal["enable", "disable"]  # Enable/disable TLS session cache. | Default: enable

# Nested TypedDicts for table field children (dict mode)

class GlobalInternetservicedownloadlistItem(TypedDict):
    """Type hints for internet-service-download-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Internet Service ID. | Default: 0 | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class GlobalInternetservicedownloadlistObject:
    """Typed object for internet-service-download-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Internet Service ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class GlobalResponse(TypedDict):
    """
    Type hints for system/global_ API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"]  # GUI display language. | Default: english
    gui_ipv6: Literal["enable", "disable"]  # Enable/disable IPv6 settings on the GUI. | Default: disable
    gui_replacement_message_groups: Literal["enable", "disable"]  # Enable/disable replacement message groups on the G | Default: disable
    gui_local_out: Literal["enable", "disable"]  # Enable/disable Local-out traffic on the GUI. | Default: disable
    gui_certificates: Literal["enable", "disable"]  # Enable/disable the System > Certificate GUI page, | Default: enable
    gui_custom_language: Literal["enable", "disable"]  # Enable/disable custom languages in GUI. | Default: disable
    gui_wireless_opensecurity: Literal["enable", "disable"]  # Enable/disable wireless open security option on th | Default: disable
    gui_app_detection_sdwan: Literal["enable", "disable"]  # Enable/disable Allow app-detection based SD-WAN. | Default: disable
    gui_display_hostname: Literal["enable", "disable"]  # Enable/disable displaying the FortiGate's hostname | Default: disable
    gui_fortigate_cloud_sandbox: Literal["enable", "disable"]  # Enable/disable displaying FortiGate Cloud Sandbox | Default: disable
    gui_firmware_upgrade_warning: Literal["enable", "disable"]  # Enable/disable the firmware upgrade warning on the | Default: enable
    gui_forticare_registration_setup_warning: Literal["enable", "disable"]  # Enable/disable the FortiCare registration setup wa | Default: enable
    gui_auto_upgrade_setup_warning: Literal["enable", "disable"]  # Enable/disable the automatic patch upgrade setup p | Default: enable
    gui_workflow_management: Literal["enable", "disable"]  # Enable/disable Workflow management features on the | Default: disable
    gui_cdn_usage: Literal["enable", "disable"]  # Enable/disable Load GUI static files from a CDN. | Default: enable
    admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"]  # Allowed TLS versions for web administration. | Default: tlsv1-2 tlsv1-3
    admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"]  # Select one or more TLS 1.3 ciphersuites to enable. | Default: TLS-AES-128-GCM-SHA256 TLS-AES-256-GCM-SHA384 TLS-CHACHA20-POLY1305-SHA256
    admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"]  # Select one or more cipher technologies that cannot
    admintimeout: int  # Number of minutes before an idle administrator ses | Default: 5 | Min: 1 | Max: 480
    admin_console_timeout: int  # Console login timeout that overrides the admin tim | Default: 0 | Min: 15 | Max: 300
    ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"]  # How often to run SSD Trim (default = weekly). SSD | Default: weekly
    ssd_trim_hour: int  # Hour of the day on which to run SSD Trim | Default: 1 | Min: 0 | Max: 23
    ssd_trim_min: int  # Minute of the hour on which to run SSD Trim | Default: 60 | Min: 0 | Max: 60
    ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of week to run SSD Trim. | Default: sunday
    ssd_trim_date: int  # Date within a month to run ssd trim. | Default: 1 | Min: 1 | Max: 31
    admin_concurrent: Literal["enable", "disable"]  # Enable/disable concurrent administrator logins. Us | Default: enable
    admin_lockout_threshold: int  # Number of failed login attempts before an administ | Default: 3 | Min: 1 | Max: 10
    admin_lockout_duration: int  # Amount of time in seconds that an administrator ac | Default: 60 | Min: 1 | Max: 2147483647
    refresh: int  # Statistics refresh interval second(s) in GUI. | Default: 0 | Min: 0 | Max: 4294967295
    interval: int  # Dead gateway detection interval. | Default: 5 | Min: 0 | Max: 4294967295
    failtime: int  # Fail-time for server lost. | Default: 5 | Min: 0 | Max: 4294967295
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # Purdue Level of this FortiGate. | Default: 3
    daily_restart: Literal["enable", "disable"]  # Enable/disable daily restart of FortiGate unit. Us | Default: disable
    restart_time: str  # Daily restart time (hh:mm).
    wad_restart_mode: Literal["none", "time", "memory"]  # WAD worker restart mode (default = none). | Default: none
    wad_restart_start_time: str  # WAD workers daily restart time (hh:mm).
    wad_restart_end_time: str  # WAD workers daily restart end time (hh:mm).
    wad_p2s_max_body_size: int  # Maximum size of the body of the local out HTTP req | Default: 4 | Min: 1 | Max: 32
    radius_port: int  # RADIUS service port number. | Default: 1812 | Min: 1 | Max: 65535
    speedtestd_server_port: int  # Speedtest server port number. | Default: 5201 | Min: 1 | Max: 65535
    speedtestd_ctrl_port: int  # Speedtest server controller port number. | Default: 5200 | Min: 1 | Max: 65535
    admin_login_max: int  # Maximum number of administrators who can be logged | Default: 100 | Min: 1 | Max: 100
    remoteauthtimeout: int  # Number of seconds that the FortiGate waits for res | Default: 5 | Min: 1 | Max: 300
    ldapconntimeout: int  # Global timeout for connections with remote LDAP se | Default: 500 | Min: 1 | Max: 300000
    batch_cmdb: Literal["enable", "disable"]  # Enable/disable batch mode, allowing you to enter a | Default: enable
    multi_factor_authentication: Literal["optional", "mandatory"]  # Enforce all login methods to require an additional | Default: optional
    ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: TLSv1-2
    autorun_log_fsck: Literal["enable", "disable"]  # Enable/disable automatic log partition check after | Default: disable
    timezone: str  # Timezone database name. Enter ? to view the list o | MaxLen: 63
    traffic_priority: Literal["tos", "dscp"]  # Choose Type of Service (ToS) or Differentiated Ser | Default: tos
    traffic_priority_level: Literal["low", "medium", "high"]  # Default system-wide level of priority for traffic | Default: medium
    quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"]  # QUIC congestion control algorithm | Default: cubic
    quic_max_datagram_size: int  # Maximum transmit datagram size | Default: 1500 | Min: 1200 | Max: 1500
    quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"]  # Enable/disable UDP payload size shaping per connec | Default: enable
    quic_ack_thresold: int  # Maximum number of unacknowledged packets before se | Default: 3 | Min: 2 | Max: 5
    quic_pmtud: Literal["enable", "disable"]  # Enable/disable path MTU discovery | Default: enable
    quic_tls_handshake_timeout: int  # Time-to-live (TTL) for TLS handshake in seconds | Default: 5 | Min: 1 | Max: 60
    anti_replay: Literal["disable", "loose", "strict"]  # Level of checking for packet replay and TCP sequen | Default: strict
    send_pmtu_icmp: Literal["enable", "disable"]  # Enable/disable sending of path maximum transmissio | Default: enable
    honor_df: Literal["enable", "disable"]  # Enable/disable honoring of Don't-Fragment (DF) fla | Default: enable
    pmtu_discovery: Literal["enable", "disable"]  # Enable/disable path MTU discovery. | Default: disable
    revision_image_auto_backup: Literal["enable", "disable"]  # Enable/disable back-up of the latest image revisio | Default: disable
    revision_backup_on_logout: Literal["enable", "disable"]  # Enable/disable back-up of the latest configuration | Default: disable
    management_vdom: str  # Management virtual domain name. | Default: root | MaxLen: 31
    hostname: str  # FortiGate unit's hostname. Most models will trunca | MaxLen: 35
    alias: str  # Alias for your FortiGate unit. | MaxLen: 35
    strong_crypto: Literal["enable", "disable"]  # Enable to use strong encryption and only allow str | Default: enable
    ssl_static_key_ciphers: Literal["enable", "disable"]  # Enable/disable static key ciphers in SSL/TLS conne | Default: enable
    snat_route_change: Literal["enable", "disable"]  # Enable/disable the ability to change the source NA | Default: disable
    ipv6_snat_route_change: Literal["enable", "disable"]  # Enable/disable the ability to change the IPv6 sour | Default: disable
    speedtest_server: Literal["enable", "disable"]  # Enable/disable speed test server. | Default: disable
    cli_audit_log: Literal["enable", "disable"]  # Enable/disable CLI audit log. | Default: disable
    dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    fds_statistics: Literal["enable", "disable"]  # Enable/disable sending IPS, Application Control, a | Default: enable
    fds_statistics_period: int  # FortiGuard statistics collection period in minutes | Default: 60 | Min: 1 | Max: 1440
    tcp_option: Literal["enable", "disable"]  # Enable SACK, timestamp and MSS TCP options. | Default: enable
    lldp_transmission: Literal["enable", "disable"]  # Enable/disable Link Layer Discovery Protocol | Default: disable
    lldp_reception: Literal["enable", "disable"]  # Enable/disable Link Layer Discovery Protocol | Default: disable
    proxy_auth_timeout: int  # Authentication timeout in minutes for authenticate | Default: 10 | Min: 1 | Max: 10000
    proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"]  # Control if users must re-authenticate after a sess | Default: session
    proxy_re_authentication_time: int  # The time limit that users must re-authenticate if | Default: 30 | Min: 1 | Max: 86400
    proxy_auth_lifetime: Literal["enable", "disable"]  # Enable/disable authenticated users lifetime contro | Default: disable
    proxy_auth_lifetime_timeout: int  # Lifetime timeout in minutes for authenticated user | Default: 480 | Min: 5 | Max: 65535
    proxy_resource_mode: Literal["enable", "disable"]  # Enable/disable use of the maximum memory usage on | Default: disable
    proxy_cert_use_mgmt_vdom: Literal["enable", "disable"]  # Enable/disable using management VDOM to send reque | Default: disable
    sys_perf_log_interval: int  # Time in minutes between updates of performance sta | Default: 5 | Min: 0 | Max: 15
    check_protocol_header: Literal["loose", "strict"]  # Level of checking performed on protocol headers. S | Default: loose
    vip_arp_range: Literal["unlimited", "restricted"]  # Controls the number of ARPs that the FortiGate sen | Default: restricted
    reset_sessionless_tcp: Literal["enable", "disable"]  # Action to perform if the FortiGate receives a TCP | Default: disable
    allow_traffic_redirect: Literal["enable", "disable"]  # Disable to prevent traffic with same local ingress | Default: disable
    ipv6_allow_traffic_redirect: Literal["enable", "disable"]  # Disable to prevent IPv6 traffic with same local in | Default: disable
    strict_dirty_session_check: Literal["enable", "disable"]  # Enable to check the session against the original p | Default: enable
    tcp_halfclose_timer: int  # Number of seconds the FortiGate unit should wait t | Default: 120 | Min: 1 | Max: 86400
    tcp_halfopen_timer: int  # Number of seconds the FortiGate unit should wait t | Default: 10 | Min: 1 | Max: 86400
    tcp_timewait_timer: int  # Length of the TCP TIME-WAIT state in seconds | Default: 1 | Min: 0 | Max: 300
    tcp_rst_timer: int  # Length of the TCP CLOSE state in seconds | Default: 5 | Min: 5 | Max: 300
    udp_idle_timer: int  # UDP connection session timeout. This command can b | Default: 180 | Min: 1 | Max: 86400
    block_session_timer: int  # Duration in seconds for blocked sessions | Default: 30 | Min: 1 | Max: 300
    ip_src_port_range: str  # IP source port range used for traffic originating | Default: 1024-25000
    pre_login_banner: Literal["enable", "disable"]  # Enable/disable displaying the administrator access | Default: disable
    post_login_banner: Literal["disable", "enable"]  # Enable/disable displaying the administrator access | Default: disable
    tftp: Literal["enable", "disable"]  # Enable/disable TFTP. | Default: enable
    av_failopen: Literal["pass", "off", "one-shot"]  # Set the action to take if the FortiGate is running | Default: pass
    av_failopen_session: Literal["enable", "disable"]  # When enabled and a proxy for a protocol runs out o | Default: disable
    memory_use_threshold_extreme: int  # Threshold at which memory usage is considered extr | Default: 95 | Min: 70 | Max: 97
    memory_use_threshold_red: int  # Threshold at which memory usage forces the FortiGa | Default: 88 | Min: 70 | Max: 97
    memory_use_threshold_green: int  # Threshold at which memory usage forces the FortiGa | Default: 82 | Min: 70 | Max: 97
    ip_fragment_mem_thresholds: int  # Maximum memory (MB) used to reassemble IPv4/IPv6 f | Default: 32 | Min: 32 | Max: 2047
    ip_fragment_timeout: int  # Timeout value in seconds for any fragment not bein | Default: 30 | Min: 3 | Max: 30
    ipv6_fragment_timeout: int  # Timeout value in seconds for any IPv6 fragment not | Default: 60 | Min: 5 | Max: 60
    cpu_use_threshold: int  # Threshold at which CPU usage is reported | Default: 90 | Min: 50 | Max: 99
    log_single_cpu_high: Literal["enable", "disable"]  # Enable/disable logging the event of a single CPU c | Default: disable
    check_reset_range: Literal["strict", "disable"]  # Configure ICMP error message verification. You can | Default: disable
    upgrade_report: Literal["enable", "disable"]  # Enable/disable the generation of an upgrade report | Default: enable
    admin_port: int  # Administrative access port for HTTP. | Default: 80 | Min: 1 | Max: 65535
    admin_sport: int  # Administrative access port for HTTPS. | Default: 443 | Min: 1 | Max: 65535
    admin_host: str  # Administrative host for HTTP and HTTPS. When set, | MaxLen: 255
    admin_https_redirect: Literal["enable", "disable"]  # Enable/disable redirection of HTTP administration | Default: enable
    admin_hsts_max_age: int  # HTTPS Strict-Transport-Security header max-age in | Default: 63072000 | Min: 0 | Max: 2147483647
    admin_ssh_password: Literal["enable", "disable"]  # Enable/disable password authentication for SSH adm | Default: enable
    admin_restrict_local: Literal["all", "non-console-only", "disable"]  # Enable/disable local admin authentication restrict | Default: disable
    admin_ssh_port: int  # Administrative access port for SSH. | Default: 22 | Min: 1 | Max: 65535
    admin_ssh_grace_time: int  # Maximum time in seconds permitted between making a | Default: 120 | Min: 10 | Max: 3600
    admin_ssh_v1: Literal["enable", "disable"]  # Enable/disable SSH v1 compatibility. | Default: disable
    admin_telnet: Literal["enable", "disable"]  # Enable/disable TELNET service. | Default: enable
    admin_telnet_port: int  # Administrative access port for TELNET. | Default: 23 | Min: 1 | Max: 65535
    admin_forticloud_sso_login: Literal["enable", "disable"]  # Enable/disable FortiCloud admin login via SSO. | Default: disable
    admin_forticloud_sso_default_profile: str  # Override access profile. | MaxLen: 35
    default_service_source_port: str  # Default service source port range
    admin_server_cert: str  # Server certificate that the FortiGate uses for HTT | Default: Fortinet_GUI_Server | MaxLen: 35
    admin_https_pki_required: Literal["enable", "disable"]  # Enable/disable admin login method. Enable to force | Default: disable
    wifi_certificate: str  # Certificate to use for WiFi authentication. | Default: Fortinet_Wifi | MaxLen: 35
    dhcp_lease_backup_interval: int  # DHCP leases backup interval in seconds | Default: 60 | Min: 10 | Max: 3600
    wifi_ca_certificate: str  # CA certificate that verifies the WiFi certificate. | Default: Fortinet_Wifi_CA | MaxLen: 79
    auth_http_port: int  # User authentication HTTP port. | Default: 1000 | Min: 1 | Max: 65535
    auth_https_port: int  # User authentication HTTPS port. | Default: 1003 | Min: 1 | Max: 65535
    auth_ike_saml_port: int  # User IKE SAML authentication port | Default: 1001 | Min: 0 | Max: 65535
    auth_keepalive: Literal["enable", "disable"]  # Enable to prevent user authentication sessions fro | Default: disable
    policy_auth_concurrent: int  # Number of concurrent firewall use logins from the | Default: 0 | Min: 0 | Max: 100
    auth_session_limit: Literal["block-new", "logout-inactive"]  # Action to take when the number of allowed user aut | Default: block-new
    auth_cert: str  # Server certificate that the FortiGate uses for HTT | Default: Fortinet_Factory | MaxLen: 35
    clt_cert_req: Literal["enable", "disable"]  # Enable/disable requiring administrators to have a | Default: disable
    fortiservice_port: int  # FortiService port (1 - 65535, default = 8013). Use | Default: 8013 | Min: 1 | Max: 65535
    cfg_save: Literal["automatic", "manual", "revert"]  # Configuration file save mode for CLI changes. | Default: automatic
    cfg_revert_timeout: int  # Time-out for reverting to the last saved configura | Default: 600 | Min: 10 | Max: 4294967295
    reboot_upon_config_restore: Literal["enable", "disable"]  # Enable/disable reboot of system upon restoring con | Default: enable
    admin_scp: Literal["enable", "disable"]  # Enable/disable SCP support for system configuratio | Default: disable
    wireless_controller: Literal["enable", "disable"]  # Enable/disable the wireless controller feature to | Default: enable
    wireless_controller_port: int  # Port used for the control channel in wireless cont | Default: 5246 | Min: 1024 | Max: 49150
    fortiextender_data_port: int  # FortiExtender data port | Default: 25246 | Min: 1024 | Max: 49150
    fortiextender: Literal["disable", "enable"]  # Enable/disable FortiExtender. | Default: disable
    extender_controller_reserved_network: str  # Configure reserved network subnet for managed LAN | Default: 10.252.0.1 255.255.0.0
    fortiextender_discovery_lockdown: Literal["disable", "enable"]  # Enable/disable FortiExtender CAPWAP lockdown. | Default: disable
    fortiextender_vlan_mode: Literal["enable", "disable"]  # Enable/disable FortiExtender VLAN mode. | Default: disable
    fortiextender_provision_on_authorization: Literal["enable", "disable"]  # Enable/disable automatic provisioning of latest Fo | Default: disable
    switch_controller: Literal["disable", "enable"]  # Enable/disable switch controller feature. Switch c | Default: disable
    switch_controller_reserved_network: str  # Configure reserved network subnet for managed swit | Default: 10.255.0.1 255.255.0.0
    dnsproxy_worker_count: int  # DNS proxy worker count. For a FortiGate with multi | Default: 1 | Min: 1 | Max: 2
    url_filter_count: int  # URL filter daemon count. | Default: 1 | Min: 1 | Max: 1
    httpd_max_worker_count: int  # Maximum number of simultaneous HTTP requests that | Default: 0 | Min: 0 | Max: 128
    proxy_worker_count: int  # Proxy worker count. | Default: 0 | Min: 1 | Max: 2
    scanunit_count: int  # Number of scanunits. The range and the default dep | Default: 0 | Min: 2 | Max: 2
    fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"]  # Type of alert to retrieve from FortiGuard.
    ipv6_accept_dad: int  # Enable/disable acceptance of IPv6 Duplicate Addres | Default: 1 | Min: 0 | Max: 2
    ipv6_allow_anycast_probe: Literal["enable", "disable"]  # Enable/disable IPv6 address probe through Anycast. | Default: disable
    ipv6_allow_multicast_probe: Literal["enable", "disable"]  # Enable/disable IPv6 address probe through Multicas | Default: disable
    ipv6_allow_local_in_silent_drop: Literal["enable", "disable"]  # Enable/disable silent drop of IPv6 local-in traffi | Default: enable
    csr_ca_attribute: Literal["enable", "disable"]  # Enable/disable the CA attribute in certificates. S | Default: enable
    wimax_4g_usb: Literal["enable", "disable"]  # Enable/disable comparability with WiMAX 4G USB dev | Default: disable
    cert_chain_max: int  # Maximum number of certificates that can be travers | Default: 8 | Min: 1 | Max: 2147483647
    sslvpn_max_worker_count: int  # Maximum number of Agentless VPN processes. Upper l | Default: 0 | Min: 0 | Max: 1
    sslvpn_affinity: str  # Agentless VPN CPU affinity. | Default: 0 | MaxLen: 79
    sslvpn_web_mode: Literal["enable", "disable"]  # Enable/disable Agentless VPN web mode. | Default: disable
    two_factor_ftk_expiry: int  # FortiToken authentication session timeout | Default: 60 | Min: 60 | Max: 600
    two_factor_email_expiry: int  # Email-based two-factor authentication session time | Default: 60 | Min: 30 | Max: 300
    two_factor_sms_expiry: int  # SMS-based two-factor authentication session timeou | Default: 60 | Min: 30 | Max: 300
    two_factor_fac_expiry: int  # FortiAuthenticator token authentication session ti | Default: 60 | Min: 10 | Max: 3600
    two_factor_ftm_expiry: int  # FortiToken Mobile session timeout (1 - 168 hours | Default: 72 | Min: 1 | Max: 168
    per_user_bal: Literal["enable", "disable"]  # Enable/disable per-user block/allow list filter. | Default: disable
    wad_worker_count: int  # Number of explicit proxy WAN optimization daemon | Default: 0 | Min: 0 | Max: 2
    wad_worker_dev_cache: int  # Number of cached devices for each ZTNA proxy worke | Default: 10240 | Min: 0 | Max: 10240
    wad_csvc_cs_count: int  # Number of concurrent WAD-cache-service object-cach | Default: 1 | Min: 1 | Max: 1
    wad_csvc_db_count: int  # Number of concurrent WAD-cache-service byte-cache | Default: 0 | Min: 0 | Max: 2
    wad_source_affinity: Literal["disable", "enable"]  # Enable/disable dispatching traffic to WAD workers | Default: enable
    wad_memory_change_granularity: int  # Minimum percentage change in system memory usage d | Default: 10 | Min: 5 | Max: 25
    login_timestamp: Literal["enable", "disable"]  # Enable/disable login time recording. | Default: disable
    ip_conflict_detection: Literal["enable", "disable"]  # Enable/disable logging of IPv4 address conflict de | Default: disable
    miglogd_children: int  # Number of logging (miglogd) processes to be allowe | Default: 0 | Min: 0 | Max: 15
    log_daemon_cpu_threshold: int  # Configure syslog daemon process spawning threshold | Default: 0 | Min: 0 | Max: 99
    special_file_23_support: Literal["disable", "enable"]  # Enable/disable detection of those special format f | Default: disable
    log_uuid_address: Literal["enable", "disable"]  # Enable/disable insertion of address UUIDs to traff | Default: disable
    log_ssl_connection: Literal["enable", "disable"]  # Enable/disable logging of SSL connection events. | Default: disable
    gui_rest_api_cache: Literal["enable", "disable"]  # Enable/disable REST API result caching on FortiGat | Default: enable
    rest_api_key_url_query: Literal["enable", "disable"]  # Enable/disable support for passing REST API keys t | Default: disable
    arp_max_entry: int  # Maximum number of dynamically learned MAC addresse | Default: 131072 | Min: 131072 | Max: 2147483647
    ha_affinity: str  # Affinity setting for HA daemons | Default: 1 | MaxLen: 79
    bfd_affinity: str  # Affinity setting for BFD daemon | Default: 1 | MaxLen: 79
    cmdbsvr_affinity: str  # Affinity setting for cmdbsvr | Default: 1 | MaxLen: 79
    av_affinity: str  # Affinity setting for AV scanning | Default: 0 | MaxLen: 79
    wad_affinity: str  # Affinity setting for wad | Default: 0 | MaxLen: 79
    ips_affinity: str  # Affinity setting for IPS | Default: 0 | MaxLen: 79
    miglog_affinity: str  # Affinity setting for logging | Default: 0 | MaxLen: 79
    syslog_affinity: str  # Affinity setting for syslog | Default: 0 | MaxLen: 79
    url_filter_affinity: str  # URL filter CPU affinity. | Default: 0 | MaxLen: 79
    router_affinity: str  # Affinity setting for BFD/VRRP/BGP/OSPF daemons | Default: 0 | MaxLen: 79
    ndp_max_entry: int  # Maximum number of NDP table entries | Default: 0 | Min: 65536 | Max: 2147483647
    br_fdb_max_entry: int  # Maximum number of bridge forwarding database (FDB) | Default: 8192 | Min: 8192 | Max: 2147483647
    max_route_cache_size: int  # Maximum number of IP route cache entries | Default: 0 | Min: 0 | Max: 2147483647
    ipsec_qat_offload: Literal["enable", "disable"]  # Enable/disable QAT offloading (Intel QuickAssist) | Default: enable
    device_idle_timeout: int  # Time in seconds that a device must be idle to auto | Default: 300 | Min: 30 | Max: 31536000
    user_device_store_max_devices: int  # Maximum number of devices allowed in user device s | Default: 62524 | Min: 31262 | Max: 89320
    user_device_store_max_device_mem: int  # Maximum percentage of total system memory allowed | Default: 2 | Min: 1 | Max: 5
    user_device_store_max_users: int  # Maximum number of users allowed in user device sto | Default: 62524 | Min: 31262 | Max: 89320
    user_device_store_max_unified_mem: int  # Maximum unified memory allowed in user device stor | Default: 312621670 | Min: 62524334 | Max: 625243340
    gui_device_latitude: str  # Add the latitude of the location of this FortiGate | MaxLen: 19
    gui_device_longitude: str  # Add the longitude of the location of this FortiGat | MaxLen: 19
    private_data_encryption: Literal["disable", "enable"]  # Enable/disable private data encryption using an AE | Default: disable
    auto_auth_extension_device: Literal["enable", "disable"]  # Enable/disable automatic authorization of dedicate | Default: enable
    gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"]  # Color scheme for the administration GUI. | Default: jade
    gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"]  # Default date format used throughout GUI. | Default: yyyy/MM/dd
    gui_date_time_source: Literal["system", "browser"]  # Source from which the FortiGate GUI uses to displa | Default: system
    igmp_state_limit: int  # Maximum number of IGMP memberships | Default: 3200 | Min: 96 | Max: 128000
    cloud_communication: Literal["enable", "disable"]  # Enable/disable all cloud communication. | Default: enable
    ipsec_ha_seqjump_rate: int  # ESP jump ahead rate (1G - 10G pps equivalent). | Default: 10 | Min: 1 | Max: 10
    fortitoken_cloud: Literal["enable", "disable"]  # Enable/disable FortiToken Cloud service. | Default: enable
    fortitoken_cloud_push_status: Literal["enable", "disable"]  # Enable/disable FTM push service of FortiToken Clou | Default: enable
    fortitoken_cloud_region: str  # Region domain of FortiToken Cloud | MaxLen: 63
    fortitoken_cloud_sync_interval: int  # Interval in which to clean up remote users in Fort | Default: 24 | Min: 0 | Max: 336
    faz_disk_buffer_size: int  # Maximum disk buffer size to temporarily store logs | Default: 0
    irq_time_accounting: Literal["auto", "force"]  # Configure CPU IRQ time accounting mode. | Default: auto
    management_ip: str  # Management IP address of this FortiGate. Used to l | MaxLen: 255
    management_port: int  # Overriding port for management connection | Default: 443 | Min: 1 | Max: 65535
    management_port_use_admin_sport: Literal["enable", "disable"]  # Enable/disable use of the admin-sport setting for | Default: enable
    forticonverter_integration: Literal["enable", "disable"]  # Enable/disable FortiConverter integration service. | Default: disable
    forticonverter_config_upload: Literal["once", "disable"]  # Enable/disable config upload to FortiConverter. | Default: disable
    internet_service_database: Literal["mini", "standard", "full", "on-demand"]  # Configure which Internet Service database size to | Default: full
    internet_service_download_list: list[GlobalInternetservicedownloadlistItem]  # Configure which on-demand Internet Service IDs are
    geoip_full_db: Literal["enable", "disable"]  # When enabled, the full geographic database will be | Default: enable
    early_tcp_npu_session: Literal["enable", "disable"]  # Enable/disable early TCP NPU session. | Default: disable
    npu_neighbor_update: Literal["enable", "disable"]  # Enable/disable sending of ARP/ICMP6 probing packet | Default: disable
    delay_tcp_npu_session: Literal["enable", "disable"]  # Enable TCP NPU session delay to guarantee packet o | Default: disable
    interface_subnet_usage: Literal["disable", "enable"]  # Enable/disable allowing use of interface-subnet se | Default: enable
    sflowd_max_children_num: int  # Maximum number of sflowd child processes allowed t | Default: 1 | Min: 0 | Max: 1
    fortigslb_integration: Literal["disable", "enable"]  # Enable/disable integration with the FortiGSLB clou | Default: disable
    user_history_password_threshold: int  # Maximum number of previous passwords saved per adm | Default: 3 | Min: 3 | Max: 15
    auth_session_auto_backup: Literal["enable", "disable"]  # Enable/disable automatic and periodic backup of au | Default: disable
    auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"]  # Configure automatic authentication session backup | Default: 15min
    scim_https_port: int  # SCIM port (0 - 65535, default = 44559). | Default: 44559 | Min: 0 | Max: 65535
    scim_http_port: int  # SCIM http port (0 - 65535, default = 44558). | Default: 44558 | Min: 0 | Max: 65535
    scim_server_cert: str  # Server certificate that the FortiGate uses for SCI | Default: Fortinet_Factory | MaxLen: 35
    application_bandwidth_tracking: Literal["disable", "enable"]  # Enable/disable application bandwidth tracking. | Default: disable
    tls_session_cache: Literal["enable", "disable"]  # Enable/disable TLS session cache. | Default: enable


@final
class GlobalObject:
    """Typed FortiObject for system/global_ with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # GUI display language. | Default: english
    language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"]
    # Enable/disable IPv6 settings on the GUI. | Default: disable
    gui_ipv6: Literal["enable", "disable"]
    # Enable/disable replacement message groups on the GUI. | Default: disable
    gui_replacement_message_groups: Literal["enable", "disable"]
    # Enable/disable Local-out traffic on the GUI. | Default: disable
    gui_local_out: Literal["enable", "disable"]
    # Enable/disable the System > Certificate GUI page, allowing y | Default: enable
    gui_certificates: Literal["enable", "disable"]
    # Enable/disable custom languages in GUI. | Default: disable
    gui_custom_language: Literal["enable", "disable"]
    # Enable/disable wireless open security option on the GUI. | Default: disable
    gui_wireless_opensecurity: Literal["enable", "disable"]
    # Enable/disable Allow app-detection based SD-WAN. | Default: disable
    gui_app_detection_sdwan: Literal["enable", "disable"]
    # Enable/disable displaying the FortiGate's hostname on the GU | Default: disable
    gui_display_hostname: Literal["enable", "disable"]
    # Enable/disable displaying FortiGate Cloud Sandbox on the GUI | Default: disable
    gui_fortigate_cloud_sandbox: Literal["enable", "disable"]
    # Enable/disable the firmware upgrade warning on the GUI. | Default: enable
    gui_firmware_upgrade_warning: Literal["enable", "disable"]
    # Enable/disable the FortiCare registration setup warning on t | Default: enable
    gui_forticare_registration_setup_warning: Literal["enable", "disable"]
    # Enable/disable the automatic patch upgrade setup prompt on t | Default: enable
    gui_auto_upgrade_setup_warning: Literal["enable", "disable"]
    # Enable/disable Workflow management features on the GUI. | Default: disable
    gui_workflow_management: Literal["enable", "disable"]
    # Enable/disable Load GUI static files from a CDN. | Default: enable
    gui_cdn_usage: Literal["enable", "disable"]
    # Allowed TLS versions for web administration. | Default: tlsv1-2 tlsv1-3
    admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"]
    # Select one or more TLS 1.3 ciphersuites to enable. Does not | Default: TLS-AES-128-GCM-SHA256 TLS-AES-256-GCM-SHA384 TLS-CHACHA20-POLY1305-SHA256
    admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"]
    # Select one or more cipher technologies that cannot be used i
    admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"]
    # Number of minutes before an idle administrator session times | Default: 5 | Min: 1 | Max: 480
    admintimeout: int
    # Console login timeout that overrides the admin timeout value | Default: 0 | Min: 15 | Max: 300
    admin_console_timeout: int
    # How often to run SSD Trim (default = weekly). SSD Trim preve | Default: weekly
    ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"]
    # Hour of the day on which to run SSD Trim | Default: 1 | Min: 0 | Max: 23
    ssd_trim_hour: int
    # Minute of the hour on which to run SSD Trim | Default: 60 | Min: 0 | Max: 60
    ssd_trim_min: int
    # Day of week to run SSD Trim. | Default: sunday
    ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Date within a month to run ssd trim. | Default: 1 | Min: 1 | Max: 31
    ssd_trim_date: int
    # Enable/disable concurrent administrator logins. Use policy-a | Default: enable
    admin_concurrent: Literal["enable", "disable"]
    # Number of failed login attempts before an administrator acco | Default: 3 | Min: 1 | Max: 10
    admin_lockout_threshold: int
    # Amount of time in seconds that an administrator account is l | Default: 60 | Min: 1 | Max: 2147483647
    admin_lockout_duration: int
    # Statistics refresh interval second(s) in GUI. | Default: 0 | Min: 0 | Max: 4294967295
    refresh: int
    # Dead gateway detection interval. | Default: 5 | Min: 0 | Max: 4294967295
    interval: int
    # Fail-time for server lost. | Default: 5 | Min: 0 | Max: 4294967295
    failtime: int
    # Purdue Level of this FortiGate. | Default: 3
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # Enable/disable daily restart of FortiGate unit. Use the rest | Default: disable
    daily_restart: Literal["enable", "disable"]
    # Daily restart time (hh:mm).
    restart_time: str
    # WAD worker restart mode (default = none). | Default: none
    wad_restart_mode: Literal["none", "time", "memory"]
    # WAD workers daily restart time (hh:mm).
    wad_restart_start_time: str
    # WAD workers daily restart end time (hh:mm).
    wad_restart_end_time: str
    # Maximum size of the body of the local out HTTP request | Default: 4 | Min: 1 | Max: 32
    wad_p2s_max_body_size: int
    # RADIUS service port number. | Default: 1812 | Min: 1 | Max: 65535
    radius_port: int
    # Speedtest server port number. | Default: 5201 | Min: 1 | Max: 65535
    speedtestd_server_port: int
    # Speedtest server controller port number. | Default: 5200 | Min: 1 | Max: 65535
    speedtestd_ctrl_port: int
    # Maximum number of administrators who can be logged in at the | Default: 100 | Min: 1 | Max: 100
    admin_login_max: int
    # Number of seconds that the FortiGate waits for responses fro | Default: 5 | Min: 1 | Max: 300
    remoteauthtimeout: int
    # Global timeout for connections with remote LDAP servers in m | Default: 500 | Min: 1 | Max: 300000
    ldapconntimeout: int
    # Enable/disable batch mode, allowing you to enter a series of | Default: enable
    batch_cmdb: Literal["enable", "disable"]
    # Enforce all login methods to require an additional authentic | Default: optional
    multi_factor_authentication: Literal["optional", "mandatory"]
    # Minimum supported protocol version for SSL/TLS connections | Default: TLSv1-2
    ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Enable/disable automatic log partition check after ungracefu | Default: disable
    autorun_log_fsck: Literal["enable", "disable"]
    # Timezone database name. Enter ? to view the list of timezone | MaxLen: 63
    timezone: str
    # Choose Type of Service (ToS) or Differentiated Services Code | Default: tos
    traffic_priority: Literal["tos", "dscp"]
    # Default system-wide level of priority for traffic prioritiza | Default: medium
    traffic_priority_level: Literal["low", "medium", "high"]
    # QUIC congestion control algorithm (default = cubic). | Default: cubic
    quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"]
    # Maximum transmit datagram size (1200 - 1500, default = 1500) | Default: 1500 | Min: 1200 | Max: 1500
    quic_max_datagram_size: int
    # Enable/disable UDP payload size shaping per connection ID | Default: enable
    quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"]
    # Maximum number of unacknowledged packets before sending ACK | Default: 3 | Min: 2 | Max: 5
    quic_ack_thresold: int
    # Enable/disable path MTU discovery (default = enable). | Default: enable
    quic_pmtud: Literal["enable", "disable"]
    # Time-to-live (TTL) for TLS handshake in seconds | Default: 5 | Min: 1 | Max: 60
    quic_tls_handshake_timeout: int
    # Level of checking for packet replay and TCP sequence checkin | Default: strict
    anti_replay: Literal["disable", "loose", "strict"]
    # Enable/disable sending of path maximum transmission unit | Default: enable
    send_pmtu_icmp: Literal["enable", "disable"]
    # Enable/disable honoring of Don't-Fragment (DF) flag. | Default: enable
    honor_df: Literal["enable", "disable"]
    # Enable/disable path MTU discovery. | Default: disable
    pmtu_discovery: Literal["enable", "disable"]
    # Enable/disable back-up of the latest image revision after th | Default: disable
    revision_image_auto_backup: Literal["enable", "disable"]
    # Enable/disable back-up of the latest configuration revision | Default: disable
    revision_backup_on_logout: Literal["enable", "disable"]
    # Management virtual domain name. | Default: root | MaxLen: 31
    management_vdom: str
    # FortiGate unit's hostname. Most models will truncate names l | MaxLen: 35
    hostname: str
    # Alias for your FortiGate unit. | MaxLen: 35
    alias: str
    # Enable to use strong encryption and only allow strong cipher | Default: enable
    strong_crypto: Literal["enable", "disable"]
    # Enable/disable static key ciphers in SSL/TLS connections | Default: enable
    ssl_static_key_ciphers: Literal["enable", "disable"]
    # Enable/disable the ability to change the source NAT route. | Default: disable
    snat_route_change: Literal["enable", "disable"]
    # Enable/disable the ability to change the IPv6 source NAT rou | Default: disable
    ipv6_snat_route_change: Literal["enable", "disable"]
    # Enable/disable speed test server. | Default: disable
    speedtest_server: Literal["enable", "disable"]
    # Enable/disable CLI audit log. | Default: disable
    cli_audit_log: Literal["enable", "disable"]
    # Number of bits to use in the Diffie-Hellman exchange for HTT | Default: 2048
    dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"]
    # Enable/disable sending IPS, Application Control, and AntiVir | Default: enable
    fds_statistics: Literal["enable", "disable"]
    # FortiGuard statistics collection period in minutes. | Default: 60 | Min: 1 | Max: 1440
    fds_statistics_period: int
    # Enable SACK, timestamp and MSS TCP options. | Default: enable
    tcp_option: Literal["enable", "disable"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) transmis | Default: disable
    lldp_transmission: Literal["enable", "disable"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) receptio | Default: disable
    lldp_reception: Literal["enable", "disable"]
    # Authentication timeout in minutes for authenticated users | Default: 10 | Min: 1 | Max: 10000
    proxy_auth_timeout: int
    # Control if users must re-authenticate after a session is clo | Default: session
    proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"]
    # The time limit that users must re-authenticate if proxy-keep | Default: 30 | Min: 1 | Max: 86400
    proxy_re_authentication_time: int
    # Enable/disable authenticated users lifetime control. This is | Default: disable
    proxy_auth_lifetime: Literal["enable", "disable"]
    # Lifetime timeout in minutes for authenticated users | Default: 480 | Min: 5 | Max: 65535
    proxy_auth_lifetime_timeout: int
    # Enable/disable use of the maximum memory usage on the FortiG | Default: disable
    proxy_resource_mode: Literal["enable", "disable"]
    # Enable/disable using management VDOM to send requests. | Default: disable
    proxy_cert_use_mgmt_vdom: Literal["enable", "disable"]
    # Time in minutes between updates of performance statistics lo | Default: 5 | Min: 0 | Max: 15
    sys_perf_log_interval: int
    # Level of checking performed on protocol headers. Strict chec | Default: loose
    check_protocol_header: Literal["loose", "strict"]
    # Controls the number of ARPs that the FortiGate sends for a V | Default: restricted
    vip_arp_range: Literal["unlimited", "restricted"]
    # Action to perform if the FortiGate receives a TCP packet but | Default: disable
    reset_sessionless_tcp: Literal["enable", "disable"]
    # Disable to prevent traffic with same local ingress and egres | Default: disable
    allow_traffic_redirect: Literal["enable", "disable"]
    # Disable to prevent IPv6 traffic with same local ingress and | Default: disable
    ipv6_allow_traffic_redirect: Literal["enable", "disable"]
    # Enable to check the session against the original policy when | Default: enable
    strict_dirty_session_check: Literal["enable", "disable"]
    # Number of seconds the FortiGate unit should wait to close a | Default: 120 | Min: 1 | Max: 86400
    tcp_halfclose_timer: int
    # Number of seconds the FortiGate unit should wait to close a | Default: 10 | Min: 1 | Max: 86400
    tcp_halfopen_timer: int
    # Length of the TCP TIME-WAIT state in seconds | Default: 1 | Min: 0 | Max: 300
    tcp_timewait_timer: int
    # Length of the TCP CLOSE state in seconds | Default: 5 | Min: 5 | Max: 300
    tcp_rst_timer: int
    # UDP connection session timeout. This command can be useful i | Default: 180 | Min: 1 | Max: 86400
    udp_idle_timer: int
    # Duration in seconds for blocked sessions (1 - 300 sec | Default: 30 | Min: 1 | Max: 300
    block_session_timer: int
    # IP source port range used for traffic originating from the F | Default: 1024-25000
    ip_src_port_range: str
    # Enable/disable displaying the administrator access disclaime | Default: disable
    pre_login_banner: Literal["enable", "disable"]
    # Enable/disable displaying the administrator access disclaime | Default: disable
    post_login_banner: Literal["disable", "enable"]
    # Enable/disable TFTP. | Default: enable
    tftp: Literal["enable", "disable"]
    # Set the action to take if the FortiGate is running low on me | Default: pass
    av_failopen: Literal["pass", "off", "one-shot"]
    # When enabled and a proxy for a protocol runs out of room in | Default: disable
    av_failopen_session: Literal["enable", "disable"]
    # Threshold at which memory usage is considered extreme | Default: 95 | Min: 70 | Max: 97
    memory_use_threshold_extreme: int
    # Threshold at which memory usage forces the FortiGate to ente | Default: 88 | Min: 70 | Max: 97
    memory_use_threshold_red: int
    # Threshold at which memory usage forces the FortiGate to exit | Default: 82 | Min: 70 | Max: 97
    memory_use_threshold_green: int
    # Maximum memory (MB) used to reassemble IPv4/IPv6 fragments. | Default: 32 | Min: 32 | Max: 2047
    ip_fragment_mem_thresholds: int
    # Timeout value in seconds for any fragment not being reassemb | Default: 30 | Min: 3 | Max: 30
    ip_fragment_timeout: int
    # Timeout value in seconds for any IPv6 fragment not being rea | Default: 60 | Min: 5 | Max: 60
    ipv6_fragment_timeout: int
    # Threshold at which CPU usage is reported | Default: 90 | Min: 50 | Max: 99
    cpu_use_threshold: int
    # Enable/disable logging the event of a single CPU core reachi | Default: disable
    log_single_cpu_high: Literal["enable", "disable"]
    # Configure ICMP error message verification. You can either ap | Default: disable
    check_reset_range: Literal["strict", "disable"]
    # Enable/disable the generation of an upgrade report when upgr | Default: enable
    upgrade_report: Literal["enable", "disable"]
    # Administrative access port for HTTP. | Default: 80 | Min: 1 | Max: 65535
    admin_port: int
    # Administrative access port for HTTPS. | Default: 443 | Min: 1 | Max: 65535
    admin_sport: int
    # Administrative host for HTTP and HTTPS. When set, will be us | MaxLen: 255
    admin_host: str
    # Enable/disable redirection of HTTP administration access to | Default: enable
    admin_https_redirect: Literal["enable", "disable"]
    # HTTPS Strict-Transport-Security header max-age in seconds. A | Default: 63072000 | Min: 0 | Max: 2147483647
    admin_hsts_max_age: int
    # Enable/disable password authentication for SSH admin access. | Default: enable
    admin_ssh_password: Literal["enable", "disable"]
    # Enable/disable local admin authentication restriction when r | Default: disable
    admin_restrict_local: Literal["all", "non-console-only", "disable"]
    # Administrative access port for SSH. | Default: 22 | Min: 1 | Max: 65535
    admin_ssh_port: int
    # Maximum time in seconds permitted between making an SSH conn | Default: 120 | Min: 10 | Max: 3600
    admin_ssh_grace_time: int
    # Enable/disable SSH v1 compatibility. | Default: disable
    admin_ssh_v1: Literal["enable", "disable"]
    # Enable/disable TELNET service. | Default: enable
    admin_telnet: Literal["enable", "disable"]
    # Administrative access port for TELNET. | Default: 23 | Min: 1 | Max: 65535
    admin_telnet_port: int
    # Enable/disable FortiCloud admin login via SSO. | Default: disable
    admin_forticloud_sso_login: Literal["enable", "disable"]
    # Override access profile. | MaxLen: 35
    admin_forticloud_sso_default_profile: str
    # Default service source port range (default = 1 - 65535).
    default_service_source_port: str
    # Server certificate that the FortiGate uses for HTTPS adminis | Default: Fortinet_GUI_Server | MaxLen: 35
    admin_server_cert: str
    # Enable/disable admin login method. Enable to force administr | Default: disable
    admin_https_pki_required: Literal["enable", "disable"]
    # Certificate to use for WiFi authentication. | Default: Fortinet_Wifi | MaxLen: 35
    wifi_certificate: str
    # DHCP leases backup interval in seconds | Default: 60 | Min: 10 | Max: 3600
    dhcp_lease_backup_interval: int
    # CA certificate that verifies the WiFi certificate. | Default: Fortinet_Wifi_CA | MaxLen: 79
    wifi_ca_certificate: str
    # User authentication HTTP port. (1 - 65535, default = 1000). | Default: 1000 | Min: 1 | Max: 65535
    auth_http_port: int
    # User authentication HTTPS port. (1 - 65535, default = 1003). | Default: 1003 | Min: 1 | Max: 65535
    auth_https_port: int
    # User IKE SAML authentication port | Default: 1001 | Min: 0 | Max: 65535
    auth_ike_saml_port: int
    # Enable to prevent user authentication sessions from timing o | Default: disable
    auth_keepalive: Literal["enable", "disable"]
    # Number of concurrent firewall use logins from the same user | Default: 0 | Min: 0 | Max: 100
    policy_auth_concurrent: int
    # Action to take when the number of allowed user authenticated | Default: block-new
    auth_session_limit: Literal["block-new", "logout-inactive"]
    # Server certificate that the FortiGate uses for HTTPS firewal | Default: Fortinet_Factory | MaxLen: 35
    auth_cert: str
    # Enable/disable requiring administrators to have a client cer | Default: disable
    clt_cert_req: Literal["enable", "disable"]
    # FortiService port (1 - 65535, default = 8013). Used by Forti | Default: 8013 | Min: 1 | Max: 65535
    fortiservice_port: int
    # Configuration file save mode for CLI changes. | Default: automatic
    cfg_save: Literal["automatic", "manual", "revert"]
    # Time-out for reverting to the last saved configuration. | Default: 600 | Min: 10 | Max: 4294967295
    cfg_revert_timeout: int
    # Enable/disable reboot of system upon restoring configuration | Default: enable
    reboot_upon_config_restore: Literal["enable", "disable"]
    # Enable/disable SCP support for system configuration backup, | Default: disable
    admin_scp: Literal["enable", "disable"]
    # Enable/disable the wireless controller feature to use the Fo | Default: enable
    wireless_controller: Literal["enable", "disable"]
    # Port used for the control channel in wireless controller mod | Default: 5246 | Min: 1024 | Max: 49150
    wireless_controller_port: int
    # FortiExtender data port (1024 - 49150, default = 25246). | Default: 25246 | Min: 1024 | Max: 49150
    fortiextender_data_port: int
    # Enable/disable FortiExtender. | Default: disable
    fortiextender: Literal["disable", "enable"]
    # Configure reserved network subnet for managed LAN extension | Default: 10.252.0.1 255.255.0.0
    extender_controller_reserved_network: str
    # Enable/disable FortiExtender CAPWAP lockdown. | Default: disable
    fortiextender_discovery_lockdown: Literal["disable", "enable"]
    # Enable/disable FortiExtender VLAN mode. | Default: disable
    fortiextender_vlan_mode: Literal["enable", "disable"]
    # Enable/disable automatic provisioning of latest FortiExtende | Default: disable
    fortiextender_provision_on_authorization: Literal["enable", "disable"]
    # Enable/disable switch controller feature. Switch controller | Default: disable
    switch_controller: Literal["disable", "enable"]
    # Configure reserved network subnet for managed switches. This | Default: 10.255.0.1 255.255.0.0
    switch_controller_reserved_network: str
    # DNS proxy worker count. For a FortiGate with multiple logica | Default: 1 | Min: 1 | Max: 2
    dnsproxy_worker_count: int
    # URL filter daemon count. | Default: 1 | Min: 1 | Max: 1
    url_filter_count: int
    # Maximum number of simultaneous HTTP requests that will be se | Default: 0 | Min: 0 | Max: 128
    httpd_max_worker_count: int
    # Proxy worker count. | Default: 0 | Min: 1 | Max: 2
    proxy_worker_count: int
    # Number of scanunits. The range and the default depend on the | Default: 0 | Min: 2 | Max: 2
    scanunit_count: int
    # Type of alert to retrieve from FortiGuard.
    fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"]
    # Enable/disable acceptance of IPv6 Duplicate Address Detectio | Default: 1 | Min: 0 | Max: 2
    ipv6_accept_dad: int
    # Enable/disable IPv6 address probe through Anycast. | Default: disable
    ipv6_allow_anycast_probe: Literal["enable", "disable"]
    # Enable/disable IPv6 address probe through Multicast. | Default: disable
    ipv6_allow_multicast_probe: Literal["enable", "disable"]
    # Enable/disable silent drop of IPv6 local-in traffic. | Default: enable
    ipv6_allow_local_in_silent_drop: Literal["enable", "disable"]
    # Enable/disable the CA attribute in certificates. Some CA ser | Default: enable
    csr_ca_attribute: Literal["enable", "disable"]
    # Enable/disable comparability with WiMAX 4G USB devices. | Default: disable
    wimax_4g_usb: Literal["enable", "disable"]
    # Maximum number of certificates that can be traversed in a ce | Default: 8 | Min: 1 | Max: 2147483647
    cert_chain_max: int
    # Maximum number of Agentless VPN processes. Upper limit for t | Default: 0 | Min: 0 | Max: 1
    sslvpn_max_worker_count: int
    # Agentless VPN CPU affinity. | Default: 0 | MaxLen: 79
    sslvpn_affinity: str
    # Enable/disable Agentless VPN web mode. | Default: disable
    sslvpn_web_mode: Literal["enable", "disable"]
    # FortiToken authentication session timeout (60 - 600 sec | Default: 60 | Min: 60 | Max: 600
    two_factor_ftk_expiry: int
    # Email-based two-factor authentication session timeout | Default: 60 | Min: 30 | Max: 300
    two_factor_email_expiry: int
    # SMS-based two-factor authentication session timeout | Default: 60 | Min: 30 | Max: 300
    two_factor_sms_expiry: int
    # FortiAuthenticator token authentication session timeout | Default: 60 | Min: 10 | Max: 3600
    two_factor_fac_expiry: int
    # FortiToken Mobile session timeout (1 - 168 hours | Default: 72 | Min: 1 | Max: 168
    two_factor_ftm_expiry: int
    # Enable/disable per-user block/allow list filter. | Default: disable
    per_user_bal: Literal["enable", "disable"]
    # Number of explicit proxy WAN optimization daemon (WAD) proce | Default: 0 | Min: 0 | Max: 2
    wad_worker_count: int
    # Number of cached devices for each ZTNA proxy worker. The def | Default: 10240 | Min: 0 | Max: 10240
    wad_worker_dev_cache: int
    # Number of concurrent WAD-cache-service object-cache processe | Default: 1 | Min: 1 | Max: 1
    wad_csvc_cs_count: int
    # Number of concurrent WAD-cache-service byte-cache processes. | Default: 0 | Min: 0 | Max: 2
    wad_csvc_db_count: int
    # Enable/disable dispatching traffic to WAD workers based on s | Default: enable
    wad_source_affinity: Literal["disable", "enable"]
    # Minimum percentage change in system memory usage detected by | Default: 10 | Min: 5 | Max: 25
    wad_memory_change_granularity: int
    # Enable/disable login time recording. | Default: disable
    login_timestamp: Literal["enable", "disable"]
    # Enable/disable logging of IPv4 address conflict detection. | Default: disable
    ip_conflict_detection: Literal["enable", "disable"]
    # Number of logging (miglogd) processes to be allowed to run. | Default: 0 | Min: 0 | Max: 15
    miglogd_children: int
    # Configure syslog daemon process spawning threshold. Use a pe | Default: 0 | Min: 0 | Max: 99
    log_daemon_cpu_threshold: int
    # Enable/disable detection of those special format files when | Default: disable
    special_file_23_support: Literal["disable", "enable"]
    # Enable/disable insertion of address UUIDs to traffic logs. | Default: disable
    log_uuid_address: Literal["enable", "disable"]
    # Enable/disable logging of SSL connection events. | Default: disable
    log_ssl_connection: Literal["enable", "disable"]
    # Enable/disable REST API result caching on FortiGate. | Default: enable
    gui_rest_api_cache: Literal["enable", "disable"]
    # Enable/disable support for passing REST API keys through URL | Default: disable
    rest_api_key_url_query: Literal["enable", "disable"]
    # Maximum number of dynamically learned MAC addresses that can | Default: 131072 | Min: 131072 | Max: 2147483647
    arp_max_entry: int
    # Affinity setting for HA daemons | Default: 1 | MaxLen: 79
    ha_affinity: str
    # Affinity setting for BFD daemon | Default: 1 | MaxLen: 79
    bfd_affinity: str
    # Affinity setting for cmdbsvr | Default: 1 | MaxLen: 79
    cmdbsvr_affinity: str
    # Affinity setting for AV scanning | Default: 0 | MaxLen: 79
    av_affinity: str
    # Affinity setting for wad | Default: 0 | MaxLen: 79
    wad_affinity: str
    # Affinity setting for IPS | Default: 0 | MaxLen: 79
    ips_affinity: str
    # Affinity setting for logging | Default: 0 | MaxLen: 79
    miglog_affinity: str
    # Affinity setting for syslog | Default: 0 | MaxLen: 79
    syslog_affinity: str
    # URL filter CPU affinity. | Default: 0 | MaxLen: 79
    url_filter_affinity: str
    # Affinity setting for BFD/VRRP/BGP/OSPF daemons | Default: 0 | MaxLen: 79
    router_affinity: str
    # Maximum number of NDP table entries | Default: 0 | Min: 65536 | Max: 2147483647
    ndp_max_entry: int
    # Maximum number of bridge forwarding database (FDB) entries. | Default: 8192 | Min: 8192 | Max: 2147483647
    br_fdb_max_entry: int
    # Maximum number of IP route cache entries (0 - 2147483647). | Default: 0 | Min: 0 | Max: 2147483647
    max_route_cache_size: int
    # Enable/disable QAT offloading (Intel QuickAssist) for IPsec | Default: enable
    ipsec_qat_offload: Literal["enable", "disable"]
    # Time in seconds that a device must be idle to automatically | Default: 300 | Min: 30 | Max: 31536000
    device_idle_timeout: int
    # Maximum number of devices allowed in user device store. | Default: 62524 | Min: 31262 | Max: 89320
    user_device_store_max_devices: int
    # Maximum percentage of total system memory allowed to be used | Default: 2 | Min: 1 | Max: 5
    user_device_store_max_device_mem: int
    # Maximum number of users allowed in user device store. | Default: 62524 | Min: 31262 | Max: 89320
    user_device_store_max_users: int
    # Maximum unified memory allowed in user device store. | Default: 312621670 | Min: 62524334 | Max: 625243340
    user_device_store_max_unified_mem: int
    # Add the latitude of the location of this FortiGate to positi | MaxLen: 19
    gui_device_latitude: str
    # Add the longitude of the location of this FortiGate to posit | MaxLen: 19
    gui_device_longitude: str
    # Enable/disable private data encryption using an AES 128-bit | Default: disable
    private_data_encryption: Literal["disable", "enable"]
    # Enable/disable automatic authorization of dedicated Fortinet | Default: enable
    auto_auth_extension_device: Literal["enable", "disable"]
    # Color scheme for the administration GUI. | Default: jade
    gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"]
    # Default date format used throughout GUI. | Default: yyyy/MM/dd
    gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"]
    # Source from which the FortiGate GUI uses to display date and | Default: system
    gui_date_time_source: Literal["system", "browser"]
    # Maximum number of IGMP memberships | Default: 3200 | Min: 96 | Max: 128000
    igmp_state_limit: int
    # Enable/disable all cloud communication. | Default: enable
    cloud_communication: Literal["enable", "disable"]
    # ESP jump ahead rate (1G - 10G pps equivalent). | Default: 10 | Min: 1 | Max: 10
    ipsec_ha_seqjump_rate: int
    # Enable/disable FortiToken Cloud service. | Default: enable
    fortitoken_cloud: Literal["enable", "disable"]
    # Enable/disable FTM push service of FortiToken Cloud. | Default: enable
    fortitoken_cloud_push_status: Literal["enable", "disable"]
    # Region domain of FortiToken Cloud(unset to non-region). | MaxLen: 63
    fortitoken_cloud_region: str
    # Interval in which to clean up remote users in FortiToken Clo | Default: 24 | Min: 0 | Max: 336
    fortitoken_cloud_sync_interval: int
    # Maximum disk buffer size to temporarily store logs destined | Default: 0
    faz_disk_buffer_size: int
    # Configure CPU IRQ time accounting mode. | Default: auto
    irq_time_accounting: Literal["auto", "force"]
    # Management IP address of this FortiGate. Used to log into th | MaxLen: 255
    management_ip: str
    # Overriding port for management connection | Default: 443 | Min: 1 | Max: 65535
    management_port: int
    # Enable/disable use of the admin-sport setting for the manage | Default: enable
    management_port_use_admin_sport: Literal["enable", "disable"]
    # Enable/disable FortiConverter integration service. | Default: disable
    forticonverter_integration: Literal["enable", "disable"]
    # Enable/disable config upload to FortiConverter. | Default: disable
    forticonverter_config_upload: Literal["once", "disable"]
    # Configure which Internet Service database size to download f | Default: full
    internet_service_database: Literal["mini", "standard", "full", "on-demand"]
    # Configure which on-demand Internet Service IDs are to be dow
    internet_service_download_list: list[GlobalInternetservicedownloadlistObject]
    # When enabled, the full geographic database will be loaded in | Default: enable
    geoip_full_db: Literal["enable", "disable"]
    # Enable/disable early TCP NPU session. | Default: disable
    early_tcp_npu_session: Literal["enable", "disable"]
    # Enable/disable sending of ARP/ICMP6 probing packets to updat | Default: disable
    npu_neighbor_update: Literal["enable", "disable"]
    # Enable TCP NPU session delay to guarantee packet order of 3- | Default: disable
    delay_tcp_npu_session: Literal["enable", "disable"]
    # Enable/disable allowing use of interface-subnet setting in f | Default: enable
    interface_subnet_usage: Literal["disable", "enable"]
    # Maximum number of sflowd child processes allowed to run. | Default: 1 | Min: 0 | Max: 1
    sflowd_max_children_num: int
    # Enable/disable integration with the FortiGSLB cloud service. | Default: disable
    fortigslb_integration: Literal["disable", "enable"]
    # Maximum number of previous passwords saved per admin/user | Default: 3 | Min: 3 | Max: 15
    user_history_password_threshold: int
    # Enable/disable automatic and periodic backup of authenticati | Default: disable
    auth_session_auto_backup: Literal["enable", "disable"]
    # Configure automatic authentication session backup interval | Default: 15min
    auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"]
    # SCIM port (0 - 65535, default = 44559). | Default: 44559 | Min: 0 | Max: 65535
    scim_https_port: int
    # SCIM http port (0 - 65535, default = 44558). | Default: 44558 | Min: 0 | Max: 65535
    scim_http_port: int
    # Server certificate that the FortiGate uses for SCIM connecti | Default: Fortinet_Factory | MaxLen: 35
    scim_server_cert: str
    # Enable/disable application bandwidth tracking. | Default: disable
    application_bandwidth_tracking: Literal["disable", "enable"]
    # Enable/disable TLS session cache. | Default: enable
    tls_session_cache: Literal["enable", "disable"]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Global:
    """
    Configure global attributes.
    
    Path: system/global_
    Category: cmdb
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> dict[str, Any] | FortiObject: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GlobalPayload | None = ...,
        language: Literal["english", "french", "spanish", "portuguese", "japanese", "trach", "simch", "korean"] | None = ...,
        gui_ipv6: Literal["enable", "disable"] | None = ...,
        gui_replacement_message_groups: Literal["enable", "disable"] | None = ...,
        gui_local_out: Literal["enable", "disable"] | None = ...,
        gui_certificates: Literal["enable", "disable"] | None = ...,
        gui_custom_language: Literal["enable", "disable"] | None = ...,
        gui_wireless_opensecurity: Literal["enable", "disable"] | None = ...,
        gui_app_detection_sdwan: Literal["enable", "disable"] | None = ...,
        gui_display_hostname: Literal["enable", "disable"] | None = ...,
        gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = ...,
        gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = ...,
        gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = ...,
        gui_workflow_management: Literal["enable", "disable"] | None = ...,
        gui_cdn_usage: Literal["enable", "disable"] | None = ...,
        admin_https_ssl_versions: Literal["tlsv1-1", "tlsv1-2", "tlsv1-3"] | list[str] | None = ...,
        admin_https_ssl_ciphersuites: Literal["TLS-AES-128-GCM-SHA256", "TLS-AES-256-GCM-SHA384", "TLS-CHACHA20-POLY1305-SHA256", "TLS-AES-128-CCM-SHA256", "TLS-AES-128-CCM-8-SHA256"] | list[str] | None = ...,
        admin_https_ssl_banned_ciphers: Literal["RSA", "DHE", "ECDHE", "DSS", "ECDSA", "AES", "AESGCM", "CAMELLIA", "3DES", "SHA1", "SHA256", "SHA384", "STATIC", "CHACHA20", "ARIA", "AESCCM"] | list[str] | None = ...,
        admintimeout: int | None = ...,
        admin_console_timeout: int | None = ...,
        ssd_trim_freq: Literal["never", "hourly", "daily", "weekly", "monthly"] | None = ...,
        ssd_trim_hour: int | None = ...,
        ssd_trim_min: int | None = ...,
        ssd_trim_weekday: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        ssd_trim_date: int | None = ...,
        admin_concurrent: Literal["enable", "disable"] | None = ...,
        admin_lockout_threshold: int | None = ...,
        admin_lockout_duration: int | None = ...,
        refresh: int | None = ...,
        interval: int | None = ...,
        failtime: int | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        daily_restart: Literal["enable", "disable"] | None = ...,
        restart_time: str | None = ...,
        wad_restart_mode: Literal["none", "time", "memory"] | None = ...,
        wad_restart_start_time: str | None = ...,
        wad_restart_end_time: str | None = ...,
        wad_p2s_max_body_size: int | None = ...,
        radius_port: int | None = ...,
        speedtestd_server_port: int | None = ...,
        speedtestd_ctrl_port: int | None = ...,
        admin_login_max: int | None = ...,
        remoteauthtimeout: int | None = ...,
        ldapconntimeout: int | None = ...,
        batch_cmdb: Literal["enable", "disable"] | None = ...,
        multi_factor_authentication: Literal["optional", "mandatory"] | None = ...,
        ssl_min_proto_version: Literal["SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        autorun_log_fsck: Literal["enable", "disable"] | None = ...,
        timezone: str | None = ...,
        traffic_priority: Literal["tos", "dscp"] | None = ...,
        traffic_priority_level: Literal["low", "medium", "high"] | None = ...,
        quic_congestion_control_algo: Literal["cubic", "bbr", "bbr2", "reno"] | None = ...,
        quic_max_datagram_size: int | None = ...,
        quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = ...,
        quic_ack_thresold: int | None = ...,
        quic_pmtud: Literal["enable", "disable"] | None = ...,
        quic_tls_handshake_timeout: int | None = ...,
        anti_replay: Literal["disable", "loose", "strict"] | None = ...,
        send_pmtu_icmp: Literal["enable", "disable"] | None = ...,
        honor_df: Literal["enable", "disable"] | None = ...,
        pmtu_discovery: Literal["enable", "disable"] | None = ...,
        revision_image_auto_backup: Literal["enable", "disable"] | None = ...,
        revision_backup_on_logout: Literal["enable", "disable"] | None = ...,
        management_vdom: str | None = ...,
        hostname: str | None = ...,
        alias: str | None = ...,
        strong_crypto: Literal["enable", "disable"] | None = ...,
        ssl_static_key_ciphers: Literal["enable", "disable"] | None = ...,
        snat_route_change: Literal["enable", "disable"] | None = ...,
        ipv6_snat_route_change: Literal["enable", "disable"] | None = ...,
        speedtest_server: Literal["enable", "disable"] | None = ...,
        cli_audit_log: Literal["enable", "disable"] | None = ...,
        dh_params: Literal["1024", "1536", "2048", "3072", "4096", "6144", "8192"] | None = ...,
        fds_statistics: Literal["enable", "disable"] | None = ...,
        fds_statistics_period: int | None = ...,
        tcp_option: Literal["enable", "disable"] | None = ...,
        lldp_transmission: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable"] | None = ...,
        proxy_auth_timeout: int | None = ...,
        proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = ...,
        proxy_re_authentication_time: int | None = ...,
        proxy_auth_lifetime: Literal["enable", "disable"] | None = ...,
        proxy_auth_lifetime_timeout: int | None = ...,
        proxy_resource_mode: Literal["enable", "disable"] | None = ...,
        proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = ...,
        sys_perf_log_interval: int | None = ...,
        check_protocol_header: Literal["loose", "strict"] | None = ...,
        vip_arp_range: Literal["unlimited", "restricted"] | None = ...,
        reset_sessionless_tcp: Literal["enable", "disable"] | None = ...,
        allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = ...,
        strict_dirty_session_check: Literal["enable", "disable"] | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        block_session_timer: int | None = ...,
        ip_src_port_range: str | None = ...,
        pre_login_banner: Literal["enable", "disable"] | None = ...,
        post_login_banner: Literal["disable", "enable"] | None = ...,
        tftp: Literal["enable", "disable"] | None = ...,
        av_failopen: Literal["pass", "off", "one-shot"] | None = ...,
        av_failopen_session: Literal["enable", "disable"] | None = ...,
        memory_use_threshold_extreme: int | None = ...,
        memory_use_threshold_red: int | None = ...,
        memory_use_threshold_green: int | None = ...,
        ip_fragment_mem_thresholds: int | None = ...,
        ip_fragment_timeout: int | None = ...,
        ipv6_fragment_timeout: int | None = ...,
        cpu_use_threshold: int | None = ...,
        log_single_cpu_high: Literal["enable", "disable"] | None = ...,
        check_reset_range: Literal["strict", "disable"] | None = ...,
        upgrade_report: Literal["enable", "disable"] | None = ...,
        admin_port: int | None = ...,
        admin_sport: int | None = ...,
        admin_host: str | None = ...,
        admin_https_redirect: Literal["enable", "disable"] | None = ...,
        admin_hsts_max_age: int | None = ...,
        admin_ssh_password: Literal["enable", "disable"] | None = ...,
        admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = ...,
        admin_ssh_port: int | None = ...,
        admin_ssh_grace_time: int | None = ...,
        admin_ssh_v1: Literal["enable", "disable"] | None = ...,
        admin_telnet: Literal["enable", "disable"] | None = ...,
        admin_telnet_port: int | None = ...,
        admin_forticloud_sso_login: Literal["enable", "disable"] | None = ...,
        admin_forticloud_sso_default_profile: str | None = ...,
        default_service_source_port: str | None = ...,
        admin_server_cert: str | None = ...,
        admin_https_pki_required: Literal["enable", "disable"] | None = ...,
        wifi_certificate: str | None = ...,
        dhcp_lease_backup_interval: int | None = ...,
        wifi_ca_certificate: str | None = ...,
        auth_http_port: int | None = ...,
        auth_https_port: int | None = ...,
        auth_ike_saml_port: int | None = ...,
        auth_keepalive: Literal["enable", "disable"] | None = ...,
        policy_auth_concurrent: int | None = ...,
        auth_session_limit: Literal["block-new", "logout-inactive"] | None = ...,
        auth_cert: str | None = ...,
        clt_cert_req: Literal["enable", "disable"] | None = ...,
        fortiservice_port: int | None = ...,
        cfg_save: Literal["automatic", "manual", "revert"] | None = ...,
        cfg_revert_timeout: int | None = ...,
        reboot_upon_config_restore: Literal["enable", "disable"] | None = ...,
        admin_scp: Literal["enable", "disable"] | None = ...,
        wireless_controller: Literal["enable", "disable"] | None = ...,
        wireless_controller_port: int | None = ...,
        fortiextender_data_port: int | None = ...,
        fortiextender: Literal["disable", "enable"] | None = ...,
        extender_controller_reserved_network: str | None = ...,
        fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = ...,
        fortiextender_vlan_mode: Literal["enable", "disable"] | None = ...,
        fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = ...,
        switch_controller: Literal["disable", "enable"] | None = ...,
        switch_controller_reserved_network: str | None = ...,
        dnsproxy_worker_count: int | None = ...,
        url_filter_count: int | None = ...,
        httpd_max_worker_count: int | None = ...,
        proxy_worker_count: int | None = ...,
        scanunit_count: int | None = ...,
        fgd_alert_subscription: Literal["advisory", "latest-threat", "latest-virus", "latest-attack", "new-antivirus-db", "new-attack-db"] | list[str] | None = ...,
        ipv6_accept_dad: int | None = ...,
        ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = ...,
        ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = ...,
        csr_ca_attribute: Literal["enable", "disable"] | None = ...,
        wimax_4g_usb: Literal["enable", "disable"] | None = ...,
        cert_chain_max: int | None = ...,
        sslvpn_max_worker_count: int | None = ...,
        sslvpn_affinity: str | None = ...,
        sslvpn_web_mode: Literal["enable", "disable"] | None = ...,
        two_factor_ftk_expiry: int | None = ...,
        two_factor_email_expiry: int | None = ...,
        two_factor_sms_expiry: int | None = ...,
        two_factor_fac_expiry: int | None = ...,
        two_factor_ftm_expiry: int | None = ...,
        per_user_bal: Literal["enable", "disable"] | None = ...,
        wad_worker_count: int | None = ...,
        wad_worker_dev_cache: int | None = ...,
        wad_csvc_cs_count: int | None = ...,
        wad_csvc_db_count: int | None = ...,
        wad_source_affinity: Literal["disable", "enable"] | None = ...,
        wad_memory_change_granularity: int | None = ...,
        login_timestamp: Literal["enable", "disable"] | None = ...,
        ip_conflict_detection: Literal["enable", "disable"] | None = ...,
        miglogd_children: int | None = ...,
        log_daemon_cpu_threshold: int | None = ...,
        special_file_23_support: Literal["disable", "enable"] | None = ...,
        log_uuid_address: Literal["enable", "disable"] | None = ...,
        log_ssl_connection: Literal["enable", "disable"] | None = ...,
        gui_rest_api_cache: Literal["enable", "disable"] | None = ...,
        rest_api_key_url_query: Literal["enable", "disable"] | None = ...,
        arp_max_entry: int | None = ...,
        ha_affinity: str | None = ...,
        bfd_affinity: str | None = ...,
        cmdbsvr_affinity: str | None = ...,
        av_affinity: str | None = ...,
        wad_affinity: str | None = ...,
        ips_affinity: str | None = ...,
        miglog_affinity: str | None = ...,
        syslog_affinity: str | None = ...,
        url_filter_affinity: str | None = ...,
        router_affinity: str | None = ...,
        ndp_max_entry: int | None = ...,
        br_fdb_max_entry: int | None = ...,
        max_route_cache_size: int | None = ...,
        ipsec_qat_offload: Literal["enable", "disable"] | None = ...,
        device_idle_timeout: int | None = ...,
        user_device_store_max_devices: int | None = ...,
        user_device_store_max_device_mem: int | None = ...,
        user_device_store_max_users: int | None = ...,
        user_device_store_max_unified_mem: int | None = ...,
        gui_device_latitude: str | None = ...,
        gui_device_longitude: str | None = ...,
        private_data_encryption: Literal["disable", "enable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        gui_theme: Literal["jade", "neutrino", "mariner", "graphite", "melongene", "jet-stream", "security-fabric", "retro", "dark-matter", "onyx", "eclipse"] | None = ...,
        gui_date_format: Literal["yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy"] | None = ...,
        gui_date_time_source: Literal["system", "browser"] | None = ...,
        igmp_state_limit: int | None = ...,
        cloud_communication: Literal["enable", "disable"] | None = ...,
        ipsec_ha_seqjump_rate: int | None = ...,
        fortitoken_cloud: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_push_status: Literal["enable", "disable"] | None = ...,
        fortitoken_cloud_region: str | None = ...,
        fortitoken_cloud_sync_interval: int | None = ...,
        faz_disk_buffer_size: int | None = ...,
        irq_time_accounting: Literal["auto", "force"] | None = ...,
        management_ip: str | None = ...,
        management_port: int | None = ...,
        management_port_use_admin_sport: Literal["enable", "disable"] | None = ...,
        forticonverter_integration: Literal["enable", "disable"] | None = ...,
        forticonverter_config_upload: Literal["once", "disable"] | None = ...,
        internet_service_database: Literal["mini", "standard", "full", "on-demand"] | None = ...,
        internet_service_download_list: str | list[str] | list[dict[str, Any]] | None = ...,
        geoip_full_db: Literal["enable", "disable"] | None = ...,
        early_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        npu_neighbor_update: Literal["enable", "disable"] | None = ...,
        delay_tcp_npu_session: Literal["enable", "disable"] | None = ...,
        interface_subnet_usage: Literal["disable", "enable"] | None = ...,
        sflowd_max_children_num: int | None = ...,
        fortigslb_integration: Literal["disable", "enable"] | None = ...,
        user_history_password_threshold: int | None = ...,
        auth_session_auto_backup: Literal["enable", "disable"] | None = ...,
        auth_session_auto_backup_interval: Literal["1min", "5min", "15min", "30min", "1hr"] | None = ...,
        scim_https_port: int | None = ...,
        scim_http_port: int | None = ...,
        scim_server_cert: str | None = ...,
        application_bandwidth_tracking: Literal["disable", "enable"] | None = ...,
        tls_session_cache: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Global",
    "GlobalPayload",
    "GlobalResponse",
    "GlobalObject",
]
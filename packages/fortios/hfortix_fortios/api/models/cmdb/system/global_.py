"""
Pydantic Models for CMDB - system/global_

Runtime validation models for system/global_ configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class GlobalInternetServiceDownloadList(BaseModel):
    """
    Child table model for internet-service-download-list.
    
    Configure which on-demand Internet Service IDs are to be downloaded.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Internet Service ID.")  # datasource: ['firewall.internet-service.id']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class GlobalLanguageEnum(str, Enum):
    """Allowed values for language field."""
    ENGLISH = "english"    FRENCH = "french"    SPANISH = "spanish"    PORTUGUESE = "portuguese"    JAPANESE = "japanese"    TRACH = "trach"    SIMCH = "simch"    KOREAN = "korean"
class GlobalAdmin_https_ssl_ciphersuitesEnum(str, Enum):
    """Allowed values for admin_https_ssl_ciphersuites field."""
    TLS_AES_128_GCM_SHA256 = "TLS-AES-128-GCM-SHA256"    TLS_AES_256_GCM_SHA384 = "TLS-AES-256-GCM-SHA384"    TLS_CHACHA20_POLY1305_SHA256 = "TLS-CHACHA20-POLY1305-SHA256"    TLS_AES_128_CCM_SHA256 = "TLS-AES-128-CCM-SHA256"    TLS_AES_128_CCM_8_SHA256 = "TLS-AES-128-CCM-8-SHA256"
class GlobalAdmin_https_ssl_banned_ciphersEnum(str, Enum):
    """Allowed values for admin_https_ssl_banned_ciphers field."""
    RSA = "RSA"    DHE = "DHE"    ECDHE = "ECDHE"    DSS = "DSS"    ECDSA = "ECDSA"    AES = "AES"    AESGCM = "AESGCM"    CAMELLIA = "CAMELLIA"    3DES = "3DES"    SHA1 = "SHA1"    SHA256 = "SHA256"    SHA384 = "SHA384"    STATIC = "STATIC"    CHACHA20 = "CHACHA20"    ARIA = "ARIA"    AESCCM = "AESCCM"
class GlobalSsd_trim_freqEnum(str, Enum):
    """Allowed values for ssd_trim_freq field."""
    NEVER = "never"    HOURLY = "hourly"    DAILY = "daily"    WEEKLY = "weekly"    MONTHLY = "monthly"
class GlobalSsd_trim_weekdayEnum(str, Enum):
    """Allowed values for ssd_trim_weekday field."""
    SUNDAY = "sunday"    MONDAY = "monday"    TUESDAY = "tuesday"    WEDNESDAY = "wednesday"    THURSDAY = "thursday"    FRIDAY = "friday"    SATURDAY = "saturday"
class GlobalPurdue_levelEnum(str, Enum):
    """Allowed values for purdue_level field."""
    1 = "1"    1_5 = "1.5"    2 = "2"    2_5 = "2.5"    3 = "3"    3_5 = "3.5"    4 = "4"    5 = "5"    5_5 = "5.5"
class GlobalSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"
class GlobalQuic_congestion_control_algoEnum(str, Enum):
    """Allowed values for quic_congestion_control_algo field."""
    CUBIC = "cubic"    BBR = "bbr"    BBR2 = "bbr2"    RENO = "reno"
class GlobalDh_paramsEnum(str, Enum):
    """Allowed values for dh_params field."""
    1024 = "1024"    1536 = "1536"    2048 = "2048"    3072 = "3072"    4096 = "4096"    6144 = "6144"    8192 = "8192"
class GlobalFgd_alert_subscriptionEnum(str, Enum):
    """Allowed values for fgd_alert_subscription field."""
    ADVISORY = "advisory"    LATEST_THREAT = "latest-threat"    LATEST_VIRUS = "latest-virus"    LATEST_ATTACK = "latest-attack"    NEW_ANTIVIRUS_DB = "new-antivirus-db"    NEW_ATTACK_DB = "new-attack-db"
class GlobalGui_themeEnum(str, Enum):
    """Allowed values for gui_theme field."""
    JADE = "jade"    NEUTRINO = "neutrino"    MARINER = "mariner"    GRAPHITE = "graphite"    MELONGENE = "melongene"    JET_STREAM = "jet-stream"    SECURITY_FABRIC = "security-fabric"    RETRO = "retro"    DARK_MATTER = "dark-matter"    ONYX = "onyx"    ECLIPSE = "eclipse"
class GlobalGui_date_formatEnum(str, Enum):
    """Allowed values for gui_date_format field."""
    YYYYMMDD = "yyyy/MM/dd"    DDMMYYYY = "dd/MM/yyyy"    MMDDYYYY = "MM/dd/yyyy"    YYYY_MM_DD = "yyyy-MM-dd"    DD_MM_YYYY = "dd-MM-yyyy"    MM_DD_YYYY = "MM-dd-yyyy"
class GlobalInternet_service_databaseEnum(str, Enum):
    """Allowed values for internet_service_database field."""
    MINI = "mini"    STANDARD = "standard"    FULL = "full"    ON_DEMAND = "on-demand"
class GlobalAuth_session_auto_backup_intervalEnum(str, Enum):
    """Allowed values for auth_session_auto_backup_interval field."""
    1MIN = "1min"    5MIN = "5min"    15MIN = "15min"    30MIN = "30min"    1HR = "1hr"

# ============================================================================
# Main Model
# ============================================================================

class GlobalModel(BaseModel):
    """
    Pydantic model for system/global_ configuration.
    
    Configure global attributes.
    
    Validation Rules:        - language: pattern=        - gui_ipv6: pattern=        - gui_replacement_message_groups: pattern=        - gui_local_out: pattern=        - gui_certificates: pattern=        - gui_custom_language: pattern=        - gui_wireless_opensecurity: pattern=        - gui_app_detection_sdwan: pattern=        - gui_display_hostname: pattern=        - gui_fortigate_cloud_sandbox: pattern=        - gui_firmware_upgrade_warning: pattern=        - gui_forticare_registration_setup_warning: pattern=        - gui_auto_upgrade_setup_warning: pattern=        - gui_workflow_management: pattern=        - gui_cdn_usage: pattern=        - admin_https_ssl_versions: pattern=        - admin_https_ssl_ciphersuites: pattern=        - admin_https_ssl_banned_ciphers: pattern=        - admintimeout: min=1 max=480 pattern=        - admin_console_timeout: min=15 max=300 pattern=        - ssd_trim_freq: pattern=        - ssd_trim_hour: min=0 max=23 pattern=        - ssd_trim_min: min=0 max=60 pattern=        - ssd_trim_weekday: pattern=        - ssd_trim_date: min=1 max=31 pattern=        - admin_concurrent: pattern=        - admin_lockout_threshold: min=1 max=10 pattern=        - admin_lockout_duration: min=1 max=2147483647 pattern=        - refresh: min=0 max=4294967295 pattern=        - interval: min=0 max=4294967295 pattern=        - failtime: min=0 max=4294967295 pattern=        - purdue_level: pattern=        - daily_restart: pattern=        - restart_time: pattern=        - wad_restart_mode: pattern=        - wad_restart_start_time: pattern=        - wad_restart_end_time: pattern=        - wad_p2s_max_body_size: min=1 max=32 pattern=        - radius_port: min=1 max=65535 pattern=        - speedtestd_server_port: min=1 max=65535 pattern=        - speedtestd_ctrl_port: min=1 max=65535 pattern=        - admin_login_max: min=1 max=100 pattern=        - remoteauthtimeout: min=1 max=300 pattern=        - ldapconntimeout: min=1 max=300000 pattern=        - batch_cmdb: pattern=        - multi_factor_authentication: pattern=        - ssl_min_proto_version: pattern=        - autorun_log_fsck: pattern=        - timezone: max_length=63 pattern=        - traffic_priority: pattern=        - traffic_priority_level: pattern=        - quic_congestion_control_algo: pattern=        - quic_max_datagram_size: min=1200 max=1500 pattern=        - quic_udp_payload_size_shaping_per_cid: pattern=        - quic_ack_thresold: min=2 max=5 pattern=        - quic_pmtud: pattern=        - quic_tls_handshake_timeout: min=1 max=60 pattern=        - anti_replay: pattern=        - send_pmtu_icmp: pattern=        - honor_df: pattern=        - pmtu_discovery: pattern=        - revision_image_auto_backup: pattern=        - revision_backup_on_logout: pattern=        - management_vdom: max_length=31 pattern=        - hostname: max_length=35 pattern=        - alias: max_length=35 pattern=        - strong_crypto: pattern=        - ssl_static_key_ciphers: pattern=        - snat_route_change: pattern=        - ipv6_snat_route_change: pattern=        - speedtest_server: pattern=        - cli_audit_log: pattern=        - dh_params: pattern=        - fds_statistics: pattern=        - fds_statistics_period: min=1 max=1440 pattern=        - tcp_option: pattern=        - lldp_transmission: pattern=        - lldp_reception: pattern=        - proxy_auth_timeout: min=1 max=10000 pattern=        - proxy_keep_alive_mode: pattern=        - proxy_re_authentication_time: min=1 max=86400 pattern=        - proxy_auth_lifetime: pattern=        - proxy_auth_lifetime_timeout: min=5 max=65535 pattern=        - proxy_resource_mode: pattern=        - proxy_cert_use_mgmt_vdom: pattern=        - sys_perf_log_interval: min=0 max=15 pattern=        - check_protocol_header: pattern=        - vip_arp_range: pattern=        - reset_sessionless_tcp: pattern=        - allow_traffic_redirect: pattern=        - ipv6_allow_traffic_redirect: pattern=        - strict_dirty_session_check: pattern=        - tcp_halfclose_timer: min=1 max=86400 pattern=        - tcp_halfopen_timer: min=1 max=86400 pattern=        - tcp_timewait_timer: min=0 max=300 pattern=        - tcp_rst_timer: min=5 max=300 pattern=        - udp_idle_timer: min=1 max=86400 pattern=        - block_session_timer: min=1 max=300 pattern=        - ip_src_port_range: pattern=        - pre_login_banner: pattern=        - post_login_banner: pattern=        - tftp: pattern=        - av_failopen: pattern=        - av_failopen_session: pattern=        - memory_use_threshold_extreme: min=70 max=97 pattern=        - memory_use_threshold_red: min=70 max=97 pattern=        - memory_use_threshold_green: min=70 max=97 pattern=        - ip_fragment_mem_thresholds: min=32 max=2047 pattern=        - ip_fragment_timeout: min=3 max=30 pattern=        - ipv6_fragment_timeout: min=5 max=60 pattern=        - cpu_use_threshold: min=50 max=99 pattern=        - log_single_cpu_high: pattern=        - check_reset_range: pattern=        - upgrade_report: pattern=        - admin_port: min=1 max=65535 pattern=        - admin_sport: min=1 max=65535 pattern=        - admin_host: max_length=255 pattern=        - admin_https_redirect: pattern=        - admin_hsts_max_age: min=0 max=2147483647 pattern=        - admin_ssh_password: pattern=        - admin_restrict_local: pattern=        - admin_ssh_port: min=1 max=65535 pattern=        - admin_ssh_grace_time: min=10 max=3600 pattern=        - admin_ssh_v1: pattern=        - admin_telnet: pattern=        - admin_telnet_port: min=1 max=65535 pattern=        - admin_forticloud_sso_login: pattern=        - admin_forticloud_sso_default_profile: max_length=35 pattern=        - default_service_source_port: pattern=        - admin_server_cert: max_length=35 pattern=        - admin_https_pki_required: pattern=        - wifi_certificate: max_length=35 pattern=        - dhcp_lease_backup_interval: min=10 max=3600 pattern=        - wifi_ca_certificate: max_length=79 pattern=        - auth_http_port: min=1 max=65535 pattern=        - auth_https_port: min=1 max=65535 pattern=        - auth_ike_saml_port: min=0 max=65535 pattern=        - auth_keepalive: pattern=        - policy_auth_concurrent: min=0 max=100 pattern=        - auth_session_limit: pattern=        - auth_cert: max_length=35 pattern=        - clt_cert_req: pattern=        - fortiservice_port: min=1 max=65535 pattern=        - cfg_save: pattern=        - cfg_revert_timeout: min=10 max=4294967295 pattern=        - reboot_upon_config_restore: pattern=        - admin_scp: pattern=        - wireless_controller: pattern=        - wireless_controller_port: min=1024 max=49150 pattern=        - fortiextender_data_port: min=1024 max=49150 pattern=        - fortiextender: pattern=        - extender_controller_reserved_network: pattern=        - fortiextender_discovery_lockdown: pattern=        - fortiextender_vlan_mode: pattern=        - fortiextender_provision_on_authorization: pattern=        - switch_controller: pattern=        - switch_controller_reserved_network: pattern=        - dnsproxy_worker_count: min=1 max=2 pattern=        - url_filter_count: min=1 max=1 pattern=        - httpd_max_worker_count: min=0 max=128 pattern=        - proxy_worker_count: min=1 max=2 pattern=        - scanunit_count: min=2 max=2 pattern=        - fgd_alert_subscription: pattern=        - ipv6_accept_dad: min=0 max=2 pattern=        - ipv6_allow_anycast_probe: pattern=        - ipv6_allow_multicast_probe: pattern=        - ipv6_allow_local_in_silent_drop: pattern=        - csr_ca_attribute: pattern=        - wimax_4g_usb: pattern=        - cert_chain_max: min=1 max=2147483647 pattern=        - sslvpn_max_worker_count: min=0 max=1 pattern=        - sslvpn_affinity: max_length=79 pattern=        - sslvpn_web_mode: pattern=        - two_factor_ftk_expiry: min=60 max=600 pattern=        - two_factor_email_expiry: min=30 max=300 pattern=        - two_factor_sms_expiry: min=30 max=300 pattern=        - two_factor_fac_expiry: min=10 max=3600 pattern=        - two_factor_ftm_expiry: min=1 max=168 pattern=        - per_user_bal: pattern=        - wad_worker_count: min=0 max=2 pattern=        - wad_worker_dev_cache: min=0 max=10240 pattern=        - wad_csvc_cs_count: min=1 max=1 pattern=        - wad_csvc_db_count: min=0 max=2 pattern=        - wad_source_affinity: pattern=        - wad_memory_change_granularity: min=5 max=25 pattern=        - login_timestamp: pattern=        - ip_conflict_detection: pattern=        - miglogd_children: min=0 max=15 pattern=        - log_daemon_cpu_threshold: min=0 max=99 pattern=        - special_file_23_support: pattern=        - log_uuid_address: pattern=        - log_ssl_connection: pattern=        - gui_rest_api_cache: pattern=        - rest_api_key_url_query: pattern=        - arp_max_entry: min=131072 max=2147483647 pattern=        - ha_affinity: max_length=79 pattern=        - bfd_affinity: max_length=79 pattern=        - cmdbsvr_affinity: max_length=79 pattern=        - av_affinity: max_length=79 pattern=        - wad_affinity: max_length=79 pattern=        - ips_affinity: max_length=79 pattern=        - miglog_affinity: max_length=79 pattern=        - syslog_affinity: max_length=79 pattern=        - url_filter_affinity: max_length=79 pattern=        - router_affinity: max_length=79 pattern=        - ndp_max_entry: min=65536 max=2147483647 pattern=        - br_fdb_max_entry: min=8192 max=2147483647 pattern=        - max_route_cache_size: min=0 max=2147483647 pattern=        - ipsec_qat_offload: pattern=        - device_idle_timeout: min=30 max=31536000 pattern=        - user_device_store_max_devices: min=31262 max=89320 pattern=        - user_device_store_max_device_mem: min=1 max=5 pattern=        - user_device_store_max_users: min=31262 max=89320 pattern=        - user_device_store_max_unified_mem: min=62524334 max=625243340 pattern=        - gui_device_latitude: max_length=19 pattern=        - gui_device_longitude: max_length=19 pattern=        - private_data_encryption: pattern=        - auto_auth_extension_device: pattern=        - gui_theme: pattern=        - gui_date_format: pattern=        - gui_date_time_source: pattern=        - igmp_state_limit: min=96 max=128000 pattern=        - cloud_communication: pattern=        - ipsec_ha_seqjump_rate: min=1 max=10 pattern=        - fortitoken_cloud: pattern=        - fortitoken_cloud_push_status: pattern=        - fortitoken_cloud_region: max_length=63 pattern=        - fortitoken_cloud_sync_interval: min=0 max=336 pattern=        - faz_disk_buffer_size: pattern=        - irq_time_accounting: pattern=        - management_ip: max_length=255 pattern=        - management_port: min=1 max=65535 pattern=        - management_port_use_admin_sport: pattern=        - forticonverter_integration: pattern=        - forticonverter_config_upload: pattern=        - internet_service_database: pattern=        - internet_service_download_list: pattern=        - geoip_full_db: pattern=        - early_tcp_npu_session: pattern=        - npu_neighbor_update: pattern=        - delay_tcp_npu_session: pattern=        - interface_subnet_usage: pattern=        - sflowd_max_children_num: min=0 max=1 pattern=        - fortigslb_integration: pattern=        - user_history_password_threshold: min=3 max=15 pattern=        - auth_session_auto_backup: pattern=        - auth_session_auto_backup_interval: pattern=        - scim_https_port: min=0 max=65535 pattern=        - scim_http_port: min=0 max=65535 pattern=        - scim_server_cert: max_length=35 pattern=        - application_bandwidth_tracking: pattern=        - tls_session_cache: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    language: LanguageEnum | None = Field(default="english", description="GUI display language.")    
    gui_ipv6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 settings on the GUI.")    
    gui_replacement_message_groups: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable replacement message groups on the GUI.")    
    gui_local_out: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Local-out traffic on the GUI.")    
    gui_certificates: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the System > Certificate GUI page, allowing you to add and configure certificates from the GUI.")    
    gui_custom_language: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable custom languages in GUI.")    
    gui_wireless_opensecurity: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable wireless open security option on the GUI.")    
    gui_app_detection_sdwan: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Allow app-detection based SD-WAN.")    
    gui_display_hostname: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable displaying the FortiGate's hostname on the GUI login page.")    
    gui_fortigate_cloud_sandbox: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable displaying FortiGate Cloud Sandbox on the GUI.")    
    gui_firmware_upgrade_warning: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the firmware upgrade warning on the GUI.")    
    gui_forticare_registration_setup_warning: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the FortiCare registration setup warning on the GUI.")    
    gui_auto_upgrade_setup_warning: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the automatic patch upgrade setup prompt on the GUI.")    
    gui_workflow_management: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Workflow management features on the GUI.")    
    gui_cdn_usage: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Load GUI static files from a CDN.")    
    admin_https_ssl_versions: list[AdminHttpsSslVersions] = Field(default="tlsv1-2 tlsv1-3", description="Allowed TLS versions for web administration.")    
    admin_https_ssl_ciphersuites: list[AdminHttpsSslCiphersuites] = Field(default="TLS-AES-128-GCM-SHA256 TLS-AES-256-GCM-SHA384 TLS-CHACHA20-POLY1305-SHA256", description="Select one or more TLS 1.3 ciphersuites to enable. Does not affect ciphers in TLS 1.2 and below. At least one must be enabled. To disable all, remove TLS1.3 from admin-https-ssl-versions.")    
    admin_https_ssl_banned_ciphers: list[AdminHttpsSslBannedCiphers] = Field(default="", description="Select one or more cipher technologies that cannot be used in GUI HTTPS negotiations. Only applies to TLS 1.2 and below.")    
    admintimeout: int | None = Field(ge=1, le=480, default=5, description="Number of minutes before an idle administrator session times out (1 - 480 minutes (8 hours), default = 5). A shorter idle timeout is more secure.")    
    admin_console_timeout: int | None = Field(ge=15, le=300, default=0, description="Console login timeout that overrides the admin timeout value (15 - 300 seconds, default = 0, which disables the timeout).")    
    ssd_trim_freq: SsdTrimFreqEnum | None = Field(default="weekly", description="How often to run SSD Trim (default = weekly). SSD Trim prevents SSD drive data loss by finding and isolating errors.")    
    ssd_trim_hour: int | None = Field(ge=0, le=23, default=1, description="Hour of the day on which to run SSD Trim (0 - 23, default = 1).")    
    ssd_trim_min: int | None = Field(ge=0, le=60, default=60, description="Minute of the hour on which to run SSD Trim (0 - 59, 60 for random).")    
    ssd_trim_weekday: SsdTrimWeekdayEnum | None = Field(default="sunday", description="Day of week to run SSD Trim.")    
    ssd_trim_date: int | None = Field(ge=1, le=31, default=1, description="Date within a month to run ssd trim.")    
    admin_concurrent: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable concurrent administrator logins. Use policy-auth-concurrent for firewall authenticated users.")    
    admin_lockout_threshold: int | None = Field(ge=1, le=10, default=3, description="Number of failed login attempts before an administrator account is locked out for the admin-lockout-duration.")    
    admin_lockout_duration: int | None = Field(ge=1, le=2147483647, default=60, description="Amount of time in seconds that an administrator account is locked out after reaching the admin-lockout-threshold for repeated failed login attempts.")    
    refresh: int | None = Field(ge=0, le=4294967295, default=0, description="Statistics refresh interval second(s) in GUI.")    
    interval: int | None = Field(ge=0, le=4294967295, default=5, description="Dead gateway detection interval.")    
    failtime: int | None = Field(ge=0, le=4294967295, default=5, description="Fail-time for server lost.")    
    purdue_level: PurdueLevelEnum | None = Field(default="3", description="Purdue Level of this FortiGate.")    
    daily_restart: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable daily restart of FortiGate unit. Use the restart-time option to set the time of day for the restart.")    
    restart_time: str = Field(default="", description="Daily restart time (hh:mm).")    
    wad_restart_mode: Literal["none", "time", "memory"] | None = Field(default="none", description="WAD worker restart mode (default = none).")    
    wad_restart_start_time: str = Field(default="", description="WAD workers daily restart time (hh:mm).")    
    wad_restart_end_time: str = Field(default="", description="WAD workers daily restart end time (hh:mm).")    
    wad_p2s_max_body_size: int | None = Field(ge=1, le=32, default=4, description="Maximum size of the body of the local out HTTP request (1 - 32 Mbytes, default = 4).")    
    radius_port: int | None = Field(ge=1, le=65535, default=1812, description="RADIUS service port number.")    
    speedtestd_server_port: int | None = Field(ge=1, le=65535, default=5201, description="Speedtest server port number.")    
    speedtestd_ctrl_port: int | None = Field(ge=1, le=65535, default=5200, description="Speedtest server controller port number.")    
    admin_login_max: int | None = Field(ge=1, le=100, default=100, description="Maximum number of administrators who can be logged in at the same time (1 - 100, default = 100).")    
    remoteauthtimeout: int | None = Field(ge=1, le=300, default=5, description="Number of seconds that the FortiGate waits for responses from remote RADIUS, LDAP, or TACACS+ authentication servers. (1-300 sec, default = 5).")    
    ldapconntimeout: int | None = Field(ge=1, le=300000, default=500, description="Global timeout for connections with remote LDAP servers in milliseconds (1 - 300000, default 500).")    
    batch_cmdb: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable batch mode, allowing you to enter a series of CLI commands that will execute as a group once they are loaded.")    
    multi_factor_authentication: Literal["optional", "mandatory"] | None = Field(default="optional", description="Enforce all login methods to require an additional authentication factor (default = optional).")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="TLSv1-2", description="Minimum supported protocol version for SSL/TLS connections (default = TLSv1.2).")    
    autorun_log_fsck: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic log partition check after ungraceful shutdown.")    
    timezone: str = Field(max_length=63, default="", description="Timezone database name. Enter ? to view the list of timezone.")  # datasource: ['system.timezone.name']    
    traffic_priority: Literal["tos", "dscp"] = Field(default="tos", description="Choose Type of Service (ToS) or Differentiated Services Code Point (DSCP) for traffic prioritization in traffic shaping.")    
    traffic_priority_level: Literal["low", "medium", "high"] = Field(default="medium", description="Default system-wide level of priority for traffic prioritization.")    
    quic_congestion_control_algo: QuicCongestionControlAlgoEnum | None = Field(default="cubic", description="QUIC congestion control algorithm (default = cubic).")    
    quic_max_datagram_size: int | None = Field(ge=1200, le=1500, default=1500, description="Maximum transmit datagram size (1200 - 1500, default = 1500).")    
    quic_udp_payload_size_shaping_per_cid: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable UDP payload size shaping per connection ID (default = enable).")    
    quic_ack_thresold: int | None = Field(ge=2, le=5, default=3, description="Maximum number of unacknowledged packets before sending ACK (2 - 5, default = 3).")    
    quic_pmtud: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable path MTU discovery (default = enable).")    
    quic_tls_handshake_timeout: int | None = Field(ge=1, le=60, default=5, description="Time-to-live (TTL) for TLS handshake in seconds (1 - 60, default = 5).")    
    anti_replay: Literal["disable", "loose", "strict"] | None = Field(default="strict", description="Level of checking for packet replay and TCP sequence checking.")    
    send_pmtu_icmp: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending of path maximum transmission unit (PMTU) - ICMP destination unreachable packet and to support PMTUD protocol on your network to reduce fragmentation of packets.")    
    honor_df: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable honoring of Don't-Fragment (DF) flag.")    
    pmtu_discovery: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable path MTU discovery.")    
    revision_image_auto_backup: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable back-up of the latest image revision after the firmware is upgraded.")    
    revision_backup_on_logout: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable back-up of the latest configuration revision when an administrator logs out of the CLI or GUI.")    
    management_vdom: str | None = Field(max_length=31, default="root", description="Management virtual domain name.")  # datasource: ['system.vdom.name']    
    hostname: str | None = Field(max_length=35, default="", description="FortiGate unit's hostname. Most models will truncate names longer than 24 characters. Some models support hostnames up to 35 characters.")    
    alias: str | None = Field(max_length=35, default="", description="Alias for your FortiGate unit.")    
    strong_crypto: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to use strong encryption and only allow strong ciphers and digest for HTTPS/SSH/TLS/SSL functions.")    
    ssl_static_key_ciphers: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable static key ciphers in SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256, AES256-SHA256).")    
    snat_route_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the ability to change the source NAT route.")    
    ipv6_snat_route_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the ability to change the IPv6 source NAT route.")    
    speedtest_server: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable speed test server.")    
    cli_audit_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable CLI audit log.")    
    dh_params: DhParamsEnum | None = Field(default="2048", description="Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols.")    
    fds_statistics: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending IPS, Application Control, and AntiVirus data to FortiGuard. This data is used to improve FortiGuard services and is not shared with external parties and is protected by Fortinet's privacy policy.")    
    fds_statistics_period: int | None = Field(ge=1, le=1440, default=60, description="FortiGuard statistics collection period in minutes. (1 - 1440 min (1 min to 24 hours), default = 60).")    
    tcp_option: Literal["enable", "disable"] | None = Field(default="enable", description="Enable SACK, timestamp and MSS TCP options.")    
    lldp_transmission: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Link Layer Discovery Protocol (LLDP) transmission.")    
    lldp_reception: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Link Layer Discovery Protocol (LLDP) reception.")    
    proxy_auth_timeout: int | None = Field(ge=1, le=10000, default=10, description="Authentication timeout in minutes for authenticated users (1 - 10000 min, default = 10).")    
    proxy_keep_alive_mode: Literal["session", "traffic", "re-authentication"] | None = Field(default="session", description="Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was authenticated.")    
    proxy_re_authentication_time: int | None = Field(ge=1, le=86400, default=30, description="The time limit that users must re-authenticate if proxy-keep-alive-mode is set to re-authenticate (1  - 86400 sec, default=30s.")    
    proxy_auth_lifetime: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authenticated users lifetime control. This is a cap on the total time a proxy user can be authenticated for after which re-authentication will take place.")    
    proxy_auth_lifetime_timeout: int | None = Field(ge=5, le=65535, default=480, description="Lifetime timeout in minutes for authenticated users (5  - 65535 min, default=480 (8 hours)).")    
    proxy_resource_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of the maximum memory usage on the FortiGate unit's proxy processing of resources, such as block lists, allow lists, and external resources.")    
    proxy_cert_use_mgmt_vdom: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable using management VDOM to send requests.")    
    sys_perf_log_interval: int | None = Field(ge=0, le=15, default=5, description="Time in minutes between updates of performance statistics logging. (1 - 15 min, default = 5, 0 = disabled).")    
    check_protocol_header: Literal["loose", "strict"] | None = Field(default="loose", description="Level of checking performed on protocol headers. Strict checking is more thorough but may affect performance. Loose checking is OK in most cases.")    
    vip_arp_range: Literal["unlimited", "restricted"] | None = Field(default="restricted", description="Controls the number of ARPs that the FortiGate sends for a Virtual IP (VIP) address range.")    
    reset_sessionless_tcp: Literal["enable", "disable"] | None = Field(default="disable", description="Action to perform if the FortiGate receives a TCP packet but cannot find a corresponding session in its session table. NAT/Route mode only.")    
    allow_traffic_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Disable to prevent traffic with same local ingress and egress interface from being forwarded without policy check.")    
    ipv6_allow_traffic_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Disable to prevent IPv6 traffic with same local ingress and egress interface from being forwarded without policy check.")    
    strict_dirty_session_check: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to check the session against the original policy when revalidating. This can prevent dropping of redirected sessions when web-filtering and authentication are enabled together. If this option is enabled, the FortiGate unit deletes a session if a routing or policy change causes the session to no longer match the policy that originally allowed the session.")    
    tcp_halfclose_timer: int | None = Field(ge=1, le=86400, default=120, description="Number of seconds the FortiGate unit should wait to close a session after one peer has sent a FIN packet but the other has not responded (1 - 86400 sec (1 day), default = 120).")    
    tcp_halfopen_timer: int | None = Field(ge=1, le=86400, default=10, description="Number of seconds the FortiGate unit should wait to close a session after one peer has sent an open session packet but the other has not responded (1 - 86400 sec (1 day), default = 10).")    
    tcp_timewait_timer: int | None = Field(ge=0, le=300, default=1, description="Length of the TCP TIME-WAIT state in seconds (1 - 300 sec, default = 1).")    
    tcp_rst_timer: int | None = Field(ge=5, le=300, default=5, description="Length of the TCP CLOSE state in seconds (5 - 300 sec, default = 5).")    
    udp_idle_timer: int | None = Field(ge=1, le=86400, default=180, description="UDP connection session timeout. This command can be useful in managing CPU and memory resources (1 - 86400 seconds (1 day), default = 60).")    
    block_session_timer: int | None = Field(ge=1, le=300, default=30, description="Duration in seconds for blocked sessions (1 - 300 sec  (5 minutes), default = 30).")    
    ip_src_port_range: str = Field(default="1024-25000", description="IP source port range used for traffic originating from the FortiGate unit.")    
    pre_login_banner: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable displaying the administrator access disclaimer message on the login page before an administrator logs in.")    
    post_login_banner: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable displaying the administrator access disclaimer message after an administrator successfully logs in.")    
    tftp: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable TFTP.")    
    av_failopen: Literal["pass", "off", "one-shot"] | None = Field(default="pass", description="Set the action to take if the FortiGate is running low on memory or the proxy connection limit has been reached.")    
    av_failopen_session: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled and a proxy for a protocol runs out of room in its session table, that protocol goes into failopen mode and enacts the action specified by av-failopen.")    
    memory_use_threshold_extreme: int | None = Field(ge=70, le=97, default=95, description="Threshold at which memory usage is considered extreme (new sessions are dropped) (% of total RAM, default = 95).")    
    memory_use_threshold_red: int | None = Field(ge=70, le=97, default=88, description="Threshold at which memory usage forces the FortiGate to enter conserve mode (% of total RAM, default = 88).")    
    memory_use_threshold_green: int | None = Field(ge=70, le=97, default=82, description="Threshold at which memory usage forces the FortiGate to exit conserve mode (% of total RAM, default = 82).")    
    ip_fragment_mem_thresholds: int | None = Field(ge=32, le=2047, default=32, description="Maximum memory (MB) used to reassemble IPv4/IPv6 fragments.")    
    ip_fragment_timeout: int | None = Field(ge=3, le=30, default=30, description="Timeout value in seconds for any fragment not being reassembled")    
    ipv6_fragment_timeout: int | None = Field(ge=5, le=60, default=60, description="Timeout value in seconds for any IPv6 fragment not being reassembled")    
    cpu_use_threshold: int | None = Field(ge=50, le=99, default=90, description="Threshold at which CPU usage is reported (% of total CPU, default = 90).")    
    log_single_cpu_high: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging the event of a single CPU core reaching CPU usage threshold.")    
    check_reset_range: Literal["strict", "disable"] | None = Field(default="disable", description="Configure ICMP error message verification. You can either apply strict RST range checking or disable it.")    
    upgrade_report: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the generation of an upgrade report when upgrading the firmware.")    
    admin_port: int | None = Field(ge=1, le=65535, default=80, description="Administrative access port for HTTP. (1 - 65535, default = 80).")    
    admin_sport: int | None = Field(ge=1, le=65535, default=443, description="Administrative access port for HTTPS. (1 - 65535, default = 443).")    
    admin_host: str | None = Field(max_length=255, default="", description="Administrative host for HTTP and HTTPS. When set, will be used in lieu of the client's Host header for any redirection.")    
    admin_https_redirect: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable redirection of HTTP administration access to HTTPS.")    
    admin_hsts_max_age: int | None = Field(ge=0, le=2147483647, default=63072000, description="HTTPS Strict-Transport-Security header max-age in seconds. A value of 0 will reset any HSTS records in the browser.When admin-https-redirect is disabled the header max-age will be 0.")    
    admin_ssh_password: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable password authentication for SSH admin access.")    
    admin_restrict_local: Literal["all", "non-console-only", "disable"] | None = Field(default="disable", description="Enable/disable local admin authentication restriction when remote authenticator is up and running (default = disable).")    
    admin_ssh_port: int | None = Field(ge=1, le=65535, default=22, description="Administrative access port for SSH. (1 - 65535, default = 22).")    
    admin_ssh_grace_time: int | None = Field(ge=10, le=3600, default=120, description="Maximum time in seconds permitted between making an SSH connection to the FortiGate unit and authenticating (10 - 3600 sec (1 hour), default 120).")    
    admin_ssh_v1: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SSH v1 compatibility.")    
    admin_telnet: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable TELNET service.")    
    admin_telnet_port: int | None = Field(ge=1, le=65535, default=23, description="Administrative access port for TELNET. (1 - 65535, default = 23).")    
    admin_forticloud_sso_login: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiCloud admin login via SSO.")    
    admin_forticloud_sso_default_profile: str | None = Field(max_length=35, default="", description="Override access profile.")  # datasource: ['system.accprofile.name']    
    default_service_source_port: str | None = Field(default="", description="Default service source port range (default = 1 - 65535).")    
    admin_server_cert: str | None = Field(max_length=35, default="Fortinet_GUI_Server", description="Server certificate that the FortiGate uses for HTTPS administrative connections.")  # datasource: ['certificate.local.name']    
    admin_https_pki_required: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable admin login method. Enable to force administrators to provide a valid certificate to log in if PKI is enabled. Disable to allow administrators to log in with a certificate or password.")    
    wifi_certificate: str | None = Field(max_length=35, default="Fortinet_Wifi", description="Certificate to use for WiFi authentication.")  # datasource: ['certificate.local.name']    
    dhcp_lease_backup_interval: int | None = Field(ge=10, le=3600, default=60, description="DHCP leases backup interval in seconds (10 - 3600, default = 60).")    
    wifi_ca_certificate: str | None = Field(max_length=79, default="Fortinet_Wifi_CA", description="CA certificate that verifies the WiFi certificate.")  # datasource: ['certificate.ca.name']    
    auth_http_port: int | None = Field(ge=1, le=65535, default=1000, description="User authentication HTTP port. (1 - 65535, default = 1000).")    
    auth_https_port: int | None = Field(ge=1, le=65535, default=1003, description="User authentication HTTPS port. (1 - 65535, default = 1003).")    
    auth_ike_saml_port: int | None = Field(ge=0, le=65535, default=1001, description="User IKE SAML authentication port (0 - 65535, default = 1001).")    
    auth_keepalive: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to prevent user authentication sessions from timing out when idle.")    
    policy_auth_concurrent: int | None = Field(ge=0, le=100, default=0, description="Number of concurrent firewall use logins from the same user (1 - 100, default = 0 means no limit).")    
    auth_session_limit: Literal["block-new", "logout-inactive"] | None = Field(default="block-new", description="Action to take when the number of allowed user authenticated sessions is reached.")    
    auth_cert: str | None = Field(max_length=35, default="Fortinet_Factory", description="Server certificate that the FortiGate uses for HTTPS firewall authentication connections.")  # datasource: ['certificate.local.name']    
    clt_cert_req: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable requiring administrators to have a client certificate to log into the GUI using HTTPS.")    
    fortiservice_port: int | None = Field(ge=1, le=65535, default=8013, description="FortiService port (1 - 65535, default = 8013). Used by FortiClient endpoint compliance. Older versions of FortiClient used a different port.")    
    cfg_save: Literal["automatic", "manual", "revert"] | None = Field(default="automatic", description="Configuration file save mode for CLI changes.")    
    cfg_revert_timeout: int | None = Field(ge=10, le=4294967295, default=600, description="Time-out for reverting to the last saved configuration. (10 - 4294967295 seconds, default = 600).")    
    reboot_upon_config_restore: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable reboot of system upon restoring configuration.")    
    admin_scp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SCP support for system configuration backup, restore, and firmware file upload.")    
    wireless_controller: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the wireless controller feature to use the FortiGate unit to manage FortiAPs.")    
    wireless_controller_port: int | None = Field(ge=1024, le=49150, default=5246, description="Port used for the control channel in wireless controller mode (wireless-mode is ac). The data channel port is the control channel port number plus one (1024 - 49150, default = 5246).")    
    fortiextender_data_port: int | None = Field(ge=1024, le=49150, default=25246, description="FortiExtender data port (1024 - 49150, default = 25246).")    
    fortiextender: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable FortiExtender.")    
    extender_controller_reserved_network: Any = Field(default="10.252.0.1 255.255.0.0", description="Configure reserved network subnet for managed LAN extension FortiExtender units. This is available when the FortiExtender daemon is running.")    
    fortiextender_discovery_lockdown: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable FortiExtender CAPWAP lockdown.")    
    fortiextender_vlan_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiExtender VLAN mode.")    
    fortiextender_provision_on_authorization: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic provisioning of latest FortiExtender firmware on authorization.")    
    switch_controller: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable switch controller feature. Switch controller allows you to manage FortiSwitch from the FortiGate itself.")    
    switch_controller_reserved_network: Any = Field(default="10.255.0.1 255.255.0.0", description="Configure reserved network subnet for managed switches. This is available when the switch controller is enabled.")    
    dnsproxy_worker_count: int | None = Field(ge=1, le=2, default=1, description="DNS proxy worker count. For a FortiGate with multiple logical CPUs, you can set the DNS process number from 1 to the number of logical CPUs.")    
    url_filter_count: int | None = Field(ge=1, le=1, default=1, description="URL filter daemon count.")    
    httpd_max_worker_count: int | None = Field(ge=0, le=128, default=0, description="Maximum number of simultaneous HTTP requests that will be served. This number may affect GUI and REST API performance (0 - 128, default = 0 means let system decide).")    
    proxy_worker_count: int | None = Field(ge=1, le=2, default=0, description="Proxy worker count.")    
    scanunit_count: int | None = Field(ge=2, le=2, default=0, description="Number of scanunits. The range and the default depend on the number of CPUs. Only available on FortiGate units with multiple CPUs.")    
    fgd_alert_subscription: list[FgdAlertSubscription] = Field(default="", description="Type of alert to retrieve from FortiGuard.")    
    ipv6_accept_dad: int | None = Field(ge=0, le=2, default=1, description="Enable/disable acceptance of IPv6 Duplicate Address Detection (DAD).")    
    ipv6_allow_anycast_probe: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 address probe through Anycast.")    
    ipv6_allow_multicast_probe: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 address probe through Multicast.")    
    ipv6_allow_local_in_silent_drop: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable silent drop of IPv6 local-in traffic.")    
    csr_ca_attribute: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the CA attribute in certificates. Some CA servers reject CSRs that have the CA attribute.")    
    wimax_4g_usb: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable comparability with WiMAX 4G USB devices.")    
    cert_chain_max: int | None = Field(ge=1, le=2147483647, default=8, description="Maximum number of certificates that can be traversed in a certificate chain.")    
    sslvpn_max_worker_count: int | None = Field(ge=0, le=1, default=0, description="Maximum number of Agentless VPN processes. Upper limit for this value is the number of CPUs and depends on the model. Default value of zero means the sslvpnd daemon decides the number of worker processes.")    
    sslvpn_affinity: str | None = Field(max_length=79, default="0", description="Agentless VPN CPU affinity.")    
    sslvpn_web_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Agentless VPN web mode.")    
    two_factor_ftk_expiry: int | None = Field(ge=60, le=600, default=60, description="FortiToken authentication session timeout (60 - 600 sec (10 minutes), default = 60).")    
    two_factor_email_expiry: int | None = Field(ge=30, le=300, default=60, description="Email-based two-factor authentication session timeout (30 - 300 seconds (5 minutes), default = 60).")    
    two_factor_sms_expiry: int | None = Field(ge=30, le=300, default=60, description="SMS-based two-factor authentication session timeout (30 - 300 sec, default = 60).")    
    two_factor_fac_expiry: int | None = Field(ge=10, le=3600, default=60, description="FortiAuthenticator token authentication session timeout (10 - 3600 seconds (1 hour), default = 60).")    
    two_factor_ftm_expiry: int | None = Field(ge=1, le=168, default=72, description="FortiToken Mobile session timeout (1 - 168 hours (7 days), default = 72).")    
    per_user_bal: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable per-user block/allow list filter.")    
    wad_worker_count: int | None = Field(ge=0, le=2, default=0, description="Number of explicit proxy WAN optimization daemon (WAD) processes. By default WAN optimization, explicit proxy, and web caching is handled by all of the CPU cores in a FortiGate unit.")    
    wad_worker_dev_cache: int | None = Field(ge=0, le=10240, default=10240, description="Number of cached devices for each ZTNA proxy worker. The default value is tuned by memory consumption. Set the option to 0 to disable the cache.")    
    wad_csvc_cs_count: int | None = Field(ge=1, le=1, default=1, description="Number of concurrent WAD-cache-service object-cache processes.")    
    wad_csvc_db_count: int | None = Field(ge=0, le=2, default=0, description="Number of concurrent WAD-cache-service byte-cache processes.")    
    wad_source_affinity: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable dispatching traffic to WAD workers based on source affinity.")    
    wad_memory_change_granularity: int | None = Field(ge=5, le=25, default=10, description="Minimum percentage change in system memory usage detected by the wad daemon prior to adjusting TCP window size for any active connection.")    
    login_timestamp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable login time recording.")    
    ip_conflict_detection: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging of IPv4 address conflict detection.")    
    miglogd_children: int | None = Field(ge=0, le=15, default=0, description="Number of logging (miglogd) processes to be allowed to run. Higher number can reduce performance; lower number can slow log processing time. ")    
    log_daemon_cpu_threshold: int | None = Field(ge=0, le=99, default=0, description="Configure syslog daemon process spawning threshold. Use a percentage threshold of syslogd CPU usage (1 - 99) or set to zero to use dynamic scheduling based on the number of packets in the syslogd queue (default = 0).")    
    special_file_23_support: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable detection of those special format files when using Data Loss Prevention.")    
    log_uuid_address: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable insertion of address UUIDs to traffic logs.")    
    log_ssl_connection: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging of SSL connection events.")    
    gui_rest_api_cache: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable REST API result caching on FortiGate.")    
    rest_api_key_url_query: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable support for passing REST API keys through URL query parameters.")    
    arp_max_entry: int | None = Field(ge=131072, le=2147483647, default=131072, description="Maximum number of dynamically learned MAC addresses that can be added to the ARP table (131072 - 2147483647, default = 131072).")    
    ha_affinity: str | None = Field(max_length=79, default="1", description="Affinity setting for HA daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    bfd_affinity: str | None = Field(max_length=79, default="1", description="Affinity setting for BFD daemon (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    cmdbsvr_affinity: str | None = Field(max_length=79, default="1", description="Affinity setting for cmdbsvr (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    av_affinity: str | None = Field(max_length=79, default="0", description="Affinity setting for AV scanning (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    wad_affinity: str | None = Field(max_length=79, default="0", description="Affinity setting for wad (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    ips_affinity: str | None = Field(max_length=79, default="0", description="Affinity setting for IPS (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx; allowed CPUs must be less than total number of IPS engine daemons).")    
    miglog_affinity: str | None = Field(max_length=79, default="0", description="Affinity setting for logging (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    syslog_affinity: str | None = Field(max_length=79, default="0", description="Affinity setting for syslog (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    url_filter_affinity: str | None = Field(max_length=79, default="0", description="URL filter CPU affinity.")    
    router_affinity: str | None = Field(max_length=79, default="0", description="Affinity setting for BFD/VRRP/BGP/OSPF daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).")    
    ndp_max_entry: int | None = Field(ge=65536, le=2147483647, default=0, description="Maximum number of NDP table entries (set to 65,536 or higher; if set to 0, kernel holds 65,536 entries).")    
    br_fdb_max_entry: int | None = Field(ge=8192, le=2147483647, default=8192, description="Maximum number of bridge forwarding database (FDB) entries.")    
    max_route_cache_size: int | None = Field(ge=0, le=2147483647, default=0, description="Maximum number of IP route cache entries (0 - 2147483647).")    
    ipsec_qat_offload: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable QAT offloading (Intel QuickAssist) for IPsec VPN traffic. QuickAssist can accelerate IPsec encryption and decryption.")    
    device_idle_timeout: int | None = Field(ge=30, le=31536000, default=300, description="Time in seconds that a device must be idle to automatically log the device user out. (30 - 31536000 sec (30 sec to 1 year), default = 300).")    
    user_device_store_max_devices: int | None = Field(ge=31262, le=89320, default=62524, description="Maximum number of devices allowed in user device store.")    
    user_device_store_max_device_mem: int | None = Field(ge=1, le=5, default=2, description="Maximum percentage of total system memory allowed to be used for devices in the user device store.")    
    user_device_store_max_users: int | None = Field(ge=31262, le=89320, default=62524, description="Maximum number of users allowed in user device store.")    
    user_device_store_max_unified_mem: int | None = Field(ge=62524334, le=625243340, default=312621670, description="Maximum unified memory allowed in user device store.")    
    gui_device_latitude: str | None = Field(max_length=19, default="", description="Add the latitude of the location of this FortiGate to position it on the Threat Map.")    
    gui_device_longitude: str | None = Field(max_length=19, default="", description="Add the longitude of the location of this FortiGate to position it on the Threat Map.")    
    private_data_encryption: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable private data encryption using an AES 128-bit key or passpharse.")    
    auto_auth_extension_device: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable automatic authorization of dedicated Fortinet extension devices.")    
    gui_theme: GuiThemeEnum | None = Field(default="jade", description="Color scheme for the administration GUI.")    
    gui_date_format: GuiDateFormatEnum | None = Field(default="yyyy/MM/dd", description="Default date format used throughout GUI.")    
    gui_date_time_source: Literal["system", "browser"] | None = Field(default="system", description="Source from which the FortiGate GUI uses to display date and time entries.")    
    igmp_state_limit: int | None = Field(ge=96, le=128000, default=3200, description="Maximum number of IGMP memberships (96 - 64000, default = 3200).")    
    cloud_communication: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable all cloud communication.")    
    ipsec_ha_seqjump_rate: int | None = Field(ge=1, le=10, default=10, description="ESP jump ahead rate (1G - 10G pps equivalent).")    
    fortitoken_cloud: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiToken Cloud service.")    
    fortitoken_cloud_push_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FTM push service of FortiToken Cloud.")    
    fortitoken_cloud_region: str | None = Field(max_length=63, default="", description="Region domain of FortiToken Cloud(unset to non-region).")    
    fortitoken_cloud_sync_interval: int | None = Field(ge=0, le=336, default=24, description="Interval in which to clean up remote users in FortiToken Cloud (0 - 336 hours (14 days), default = 24, disable = 0).")    
    faz_disk_buffer_size: int | None = Field(default=0, description="Maximum disk buffer size to temporarily store logs destined for FortiAnalyzer. To be used in the event that FortiAnalyzer is unavailable.")    
    irq_time_accounting: Literal["auto", "force"] | None = Field(default="auto", description="Configure CPU IRQ time accounting mode.")    
    management_ip: str | None = Field(max_length=255, default="", description="Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric.")    
    management_port: int | None = Field(ge=1, le=65535, default=443, description="Overriding port for management connection (Overrides admin port).")    
    management_port_use_admin_sport: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of the admin-sport setting for the management port. If disabled, FortiGate will allow user to specify management-port.")    
    forticonverter_integration: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiConverter integration service.")    
    forticonverter_config_upload: Literal["once", "disable"] | None = Field(default="disable", description="Enable/disable config upload to FortiConverter.")    
    internet_service_database: InternetServiceDatabaseEnum | None = Field(default="full", description="Configure which Internet Service database size to download from FortiGuard and use.")    
    internet_service_download_list: list[InternetServiceDownloadList] = Field(default=None, description="Configure which on-demand Internet Service IDs are to be downloaded.")    
    geoip_full_db: Literal["enable", "disable"] | None = Field(default="enable", description="When enabled, the full geographic database will be loaded into the kernel which enables geographic information in traffic logs - required for FortiView countries. Disabling this option will conserve memory.")    
    early_tcp_npu_session: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable early TCP NPU session.")    
    npu_neighbor_update: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending of ARP/ICMP6 probing packets to update neighbors for offloaded sessions.")    
    delay_tcp_npu_session: Literal["enable", "disable"] | None = Field(default="disable", description="Enable TCP NPU session delay to guarantee packet order of 3-way handshake.")    
    interface_subnet_usage: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable allowing use of interface-subnet setting in firewall addresses (default = enable).")    
    sflowd_max_children_num: int | None = Field(ge=0, le=1, default=1, description="Maximum number of sflowd child processes allowed to run.")    
    fortigslb_integration: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable integration with the FortiGSLB cloud service.")    
    user_history_password_threshold: int | None = Field(ge=3, le=15, default=3, description="Maximum number of previous passwords saved per admin/user (3 - 15, default = 3).")    
    auth_session_auto_backup: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic and periodic backup of authentication sessions (default = disable). Sessions are restored upon bootup.")    
    auth_session_auto_backup_interval: AuthSessionAutoBackupIntervalEnum | None = Field(default="15min", description="Configure automatic authentication session backup interval (default = 15min).")    
    scim_https_port: int | None = Field(ge=0, le=65535, default=44559, description="SCIM port (0 - 65535, default = 44559).")    
    scim_http_port: int | None = Field(ge=0, le=65535, default=44558, description="SCIM http port (0 - 65535, default = 44558).")    
    scim_server_cert: str | None = Field(max_length=35, default="Fortinet_Factory", description="Server certificate that the FortiGate uses for SCIM connections.")  # datasource: ['certificate.local.name']    
    application_bandwidth_tracking: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable application bandwidth tracking.")    
    tls_session_cache: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable TLS session cache.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('timezone')
    @classmethod
    def validate_timezone(cls, v: Any) -> Any:
        """
        Validate timezone field.
        
        Datasource: ['system.timezone.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('management_vdom')
    @classmethod
    def validate_management_vdom(cls, v: Any) -> Any:
        """
        Validate management_vdom field.
        
        Datasource: ['system.vdom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('admin_forticloud_sso_default_profile')
    @classmethod
    def validate_admin_forticloud_sso_default_profile(cls, v: Any) -> Any:
        """
        Validate admin_forticloud_sso_default_profile field.
        
        Datasource: ['system.accprofile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('admin_server_cert')
    @classmethod
    def validate_admin_server_cert(cls, v: Any) -> Any:
        """
        Validate admin_server_cert field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('wifi_certificate')
    @classmethod
    def validate_wifi_certificate(cls, v: Any) -> Any:
        """
        Validate wifi_certificate field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('wifi_ca_certificate')
    @classmethod
    def validate_wifi_ca_certificate(cls, v: Any) -> Any:
        """
        Validate wifi_ca_certificate field.
        
        Datasource: ['certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_cert')
    @classmethod
    def validate_auth_cert(cls, v: Any) -> Any:
        """
        Validate auth_cert field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('scim_server_cert')
    @classmethod
    def validate_scim_server_cert(cls, v: Any) -> Any:
        """
        Validate scim_server_cert field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    # ========================================================================
    # Helper Methods
    # ========================================================================
    
    def to_fortios_dict(self) -> dict[str, Any]:
        """
        Convert model to FortiOS API payload format.
        
        Returns:
            Dict suitable for POST/PUT operations
        """
        # Export with exclude_none to avoid sending null values
        return self.model_dump(exclude_none=True, by_alias=True)
    
    @classmethod
    def from_fortios_response(cls, data: dict[str, Any]) -> "":
        """
        Create model instance from FortiOS API response.
        
        Args:
            data: Response data from API
            
        Returns:
            Validated model instance
        """
        return cls(**data)
    # ========================================================================
    # Datasource Validation Methods
    # ========================================================================    
    async def validate_timezone_references(self, client: Any) -> list[str]:
        """
        Validate timezone references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/timezone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     timezone="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_timezone_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "timezone", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.timezone.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Timezone '{value}' not found in "
                "system/timezone"
            )        
        return errors    
    async def validate_management_vdom_references(self, client: Any) -> list[str]:
        """
        Validate management_vdom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/vdom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     management_vdom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_management_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "management_vdom", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.vdom.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Management-Vdom '{value}' not found in "
                "system/vdom"
            )        
        return errors    
    async def validate_admin_forticloud_sso_default_profile_references(self, client: Any) -> list[str]:
        """
        Validate admin_forticloud_sso_default_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/accprofile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     admin_forticloud_sso_default_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_admin_forticloud_sso_default_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "admin_forticloud_sso_default_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.accprofile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Admin-Forticloud-Sso-Default-Profile '{value}' not found in "
                "system/accprofile"
            )        
        return errors    
    async def validate_admin_server_cert_references(self, client: Any) -> list[str]:
        """
        Validate admin_server_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     admin_server_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_admin_server_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "admin_server_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Admin-Server-Cert '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_wifi_certificate_references(self, client: Any) -> list[str]:
        """
        Validate wifi_certificate references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     wifi_certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wifi_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "wifi_certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Wifi-Certificate '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_wifi_ca_certificate_references(self, client: Any) -> list[str]:
        """
        Validate wifi_ca_certificate references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     wifi_ca_certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wifi_ca_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "wifi_ca_certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Wifi-Ca-Certificate '{value}' not found in "
                "certificate/ca"
            )        
        return errors    
    async def validate_auth_cert_references(self, client: Any) -> list[str]:
        """
        Validate auth_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     auth_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Cert '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_internet_service_download_list_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_download_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     internet_service_download_list=[{"id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_download_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_download_list", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("id")
            else:
                value = getattr(item, "id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.internet-service.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Download-List '{value}' not found in "
                    "firewall/internet-service"
                )        
        return errors    
    async def validate_scim_server_cert_references(self, client: Any) -> list[str]:
        """
        Validate scim_server_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     scim_server_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_scim_server_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "scim_server_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Scim-Server-Cert '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_all_references(self, client: Any) -> list[str]:
        """
        Validate ALL datasource references in this model.
        
        Convenience method that runs all validate_*_references() methods
        and aggregates the results.
        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of all validation errors found
            
        Example:
            >>> errors = await policy.validate_all_references(fgt._client)
            >>> if errors:
            ...     for error in errors:
            ...         print(f"  - {error}")
        """
        all_errors = []
        
        errors = await self.validate_timezone_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_management_vdom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_admin_forticloud_sso_default_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_admin_server_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_wifi_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_wifi_ca_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_download_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_scim_server_cert_references(client)
        all_errors.extend(errors)        
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "GlobalModel",    "GlobalInternetServiceDownloadList",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.306016Z
# ============================================================================
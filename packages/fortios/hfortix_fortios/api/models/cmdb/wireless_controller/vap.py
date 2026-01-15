"""
Pydantic Models for CMDB - wireless_controller/vap

Runtime validation models for wireless_controller/vap configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class VapRadiusMacAuthUsergroups(BaseModel):
    """
    Child table model for radius-mac-auth-usergroups.
    
    Selective user groups that are permitted for RADIUS mac authentication.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User group name.")  # datasource: ['user.group.name']
class VapUsergroup(BaseModel):
    """
    Child table model for usergroup.
    
    Firewall user group to be used to authenticate WiFi users.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User group name.")  # datasource: ['user.group.name']
class VapPortalMessageOverrides(BaseModel):
    """
    Child table model for portal-message-overrides.
    
    Individual message overrides.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    auth_disclaimer_page: str | None = Field(max_length=35, default="", description="Override auth-disclaimer-page message with message from portal-message-overrides group.")    
    auth_reject_page: str | None = Field(max_length=35, default="", description="Override auth-reject-page message with message from portal-message-overrides group.")    
    auth_login_page: str | None = Field(max_length=35, default="", description="Override auth-login-page message with message from portal-message-overrides group.")    
    auth_login_failed_page: str | None = Field(max_length=35, default="", description="Override auth-login-failed-page message with message from portal-message-overrides group.")
class VapSelectedUsergroups(BaseModel):
    """
    Child table model for selected-usergroups.
    
    Selective user groups that are permitted to authenticate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User group name.")  # datasource: ['user.group.name']
class VapSchedule(BaseModel):
    """
    Child table model for schedule.
    
    Firewall schedules for enabling this VAP on the FortiAP. This VAP will be enabled when at least one of the schedules is valid. Separate multiple schedule names with a space.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.group.name', 'firewall.schedule.recurring.name', 'firewall.schedule.onetime.name']
class VapVlanName(BaseModel):
    """
    Child table model for vlan-name.
    
    Table for mapping VLAN name to VLAN ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="VLAN name.")    
    vlan_id: list[VlanId] = Field(ge=0, le=4094, default="", description="VLAN IDs (maximum 8 VLAN IDs).")
class VapVlanPool(BaseModel):
    """
    Child table model for vlan-pool.
    
    VLAN pool.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4094, default=0, description="ID.")    
    wtp_group: str | None = Field(max_length=35, default="", description="WTP group name.")  # datasource: ['wireless-controller.wtp-group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class VapSecurityEnum(str, Enum):
    """Allowed values for security field."""
    OPEN = "open"    WEP64 = "wep64"    WEP128 = "wep128"    WPA_PERSONAL = "wpa-personal"    WPA_ENTERPRISE = "wpa-enterprise"    WPA_ONLY_PERSONAL = "wpa-only-personal"    WPA_ONLY_ENTERPRISE = "wpa-only-enterprise"    WPA2_ONLY_PERSONAL = "wpa2-only-personal"    WPA2_ONLY_ENTERPRISE = "wpa2-only-enterprise"    WPA3_ENTERPRISE = "wpa3-enterprise"    WPA3_ONLY_ENTERPRISE = "wpa3-only-enterprise"    WPA3_ENTERPRISE_TRANSITION = "wpa3-enterprise-transition"    WPA3_SAE = "wpa3-sae"    WPA3_SAE_TRANSITION = "wpa3-sae-transition"    OWE = "owe"    OSEN = "osen"
class VapMac_username_delimiterEnum(str, Enum):
    """Allowed values for mac_username_delimiter field."""
    HYPHEN = "hyphen"    SINGLE_HYPHEN = "single-hyphen"    COLON = "colon"    NONE = "none"
class VapMac_password_delimiterEnum(str, Enum):
    """Allowed values for mac_password_delimiter field."""
    HYPHEN = "hyphen"    SINGLE_HYPHEN = "single-hyphen"    COLON = "colon"    NONE = "none"
class VapMac_calling_station_delimiterEnum(str, Enum):
    """Allowed values for mac_calling_station_delimiter field."""
    HYPHEN = "hyphen"    SINGLE_HYPHEN = "single-hyphen"    COLON = "colon"    NONE = "none"
class VapMac_called_station_delimiterEnum(str, Enum):
    """Allowed values for mac_called_station_delimiter field."""
    HYPHEN = "hyphen"    SINGLE_HYPHEN = "single-hyphen"    COLON = "colon"    NONE = "none"
class VapPortal_typeEnum(str, Enum):
    """Allowed values for portal_type field."""
    AUTH = "auth"    AUTHDISCLAIMER = "auth+disclaimer"    DISCLAIMER = "disclaimer"    EMAIL_COLLECT = "email-collect"    CMCC = "cmcc"    CMCC_MACAUTH = "cmcc-macauth"    AUTH_MAC = "auth-mac"    EXTERNAL_AUTH = "external-auth"    EXTERNAL_MACAUTH = "external-macauth"
class VapLdpcEnum(str, Enum):
    """Allowed values for ldpc field."""
    DISABLE = "disable"    RX = "rx"    TX = "tx"    RXTX = "rxtx"
class VapMulticast_rateEnum(str, Enum):
    """Allowed values for multicast_rate field."""
    0 = "0"    6000 = "6000"    12000 = "12000"    24000 = "24000"
class VapBroadcast_suppressionEnum(str, Enum):
    """Allowed values for broadcast_suppression field."""
    DHCP_UP = "dhcp-up"    DHCP_DOWN = "dhcp-down"    DHCP_STARVATION = "dhcp-starvation"    DHCP_UCAST = "dhcp-ucast"    ARP_KNOWN = "arp-known"    ARP_UNKNOWN = "arp-unknown"    ARP_REPLY = "arp-reply"    ARP_POISON = "arp-poison"    ARP_PROXY = "arp-proxy"    NETBIOS_NS = "netbios-ns"    NETBIOS_DS = "netbios-ds"    IPV6 = "ipv6"    ALL_OTHER_MC = "all-other-mc"    ALL_OTHER_BC = "all-other-bc"
class VapIpv6_rulesEnum(str, Enum):
    """Allowed values for ipv6_rules field."""
    DROP_ICMP6RA = "drop-icmp6ra"    DROP_ICMP6RS = "drop-icmp6rs"    DROP_LLMNR6 = "drop-llmnr6"    DROP_ICMP6MLD2 = "drop-icmp6mld2"    DROP_DHCP6S = "drop-dhcp6s"    DROP_DHCP6C = "drop-dhcp6c"    NDP_PROXY = "ndp-proxy"    DROP_NS_DAD = "drop-ns-dad"    DROP_NS_NONDAD = "drop-ns-nondad"
class VapVlan_poolingEnum(str, Enum):
    """Allowed values for vlan_pooling field."""
    WTP_GROUP = "wtp-group"    ROUND_ROBIN = "round-robin"    HASH = "hash"    DISABLE = "disable"
class VapDhcp_option82_circuit_id_insertionEnum(str, Enum):
    """Allowed values for dhcp_option82_circuit_id_insertion field."""
    STYLE_1 = "style-1"    STYLE_2 = "style-2"    STYLE_3 = "style-3"    DISABLE = "disable"
class VapRates_11aEnum(str, Enum):
    """Allowed values for rates_11a field."""
    6 = "6"    6_BASIC = "6-basic"    9 = "9"    9_BASIC = "9-basic"    12 = "12"    12_BASIC = "12-basic"    18 = "18"    18_BASIC = "18-basic"    24 = "24"    24_BASIC = "24-basic"    36 = "36"    36_BASIC = "36-basic"    48 = "48"    48_BASIC = "48-basic"    54 = "54"    54_BASIC = "54-basic"
class VapRates_11bgEnum(str, Enum):
    """Allowed values for rates_11bg field."""
    1 = "1"    1_BASIC = "1-basic"    2 = "2"    2_BASIC = "2-basic"    5_5 = "5.5"    5_5_BASIC = "5.5-basic"    11 = "11"    11_BASIC = "11-basic"    6 = "6"    6_BASIC = "6-basic"    9 = "9"    9_BASIC = "9-basic"    12 = "12"    12_BASIC = "12-basic"    18 = "18"    18_BASIC = "18-basic"    24 = "24"    24_BASIC = "24-basic"    36 = "36"    36_BASIC = "36-basic"    48 = "48"    48_BASIC = "48-basic"    54 = "54"    54_BASIC = "54-basic"
class VapRates_11n_ss12Enum(str, Enum):
    """Allowed values for rates_11n_ss12 field."""
    MCS01 = "mcs0/1"    MCS11 = "mcs1/1"    MCS21 = "mcs2/1"    MCS31 = "mcs3/1"    MCS41 = "mcs4/1"    MCS51 = "mcs5/1"    MCS61 = "mcs6/1"    MCS71 = "mcs7/1"    MCS82 = "mcs8/2"    MCS92 = "mcs9/2"    MCS102 = "mcs10/2"    MCS112 = "mcs11/2"    MCS122 = "mcs12/2"    MCS132 = "mcs13/2"    MCS142 = "mcs14/2"    MCS152 = "mcs15/2"
class VapRates_11n_ss34Enum(str, Enum):
    """Allowed values for rates_11n_ss34 field."""
    MCS163 = "mcs16/3"    MCS173 = "mcs17/3"    MCS183 = "mcs18/3"    MCS193 = "mcs19/3"    MCS203 = "mcs20/3"    MCS213 = "mcs21/3"    MCS223 = "mcs22/3"    MCS233 = "mcs23/3"    MCS244 = "mcs24/4"    MCS254 = "mcs25/4"    MCS264 = "mcs26/4"    MCS274 = "mcs27/4"    MCS284 = "mcs28/4"    MCS294 = "mcs29/4"    MCS304 = "mcs30/4"    MCS314 = "mcs31/4"

# ============================================================================
# Main Model
# ============================================================================

class VapModel(BaseModel):
    """
    Pydantic model for wireless_controller/vap configuration.
    
    Configure Virtual Access Points (VAPs).
    
    Validation Rules:        - name: max_length=15 pattern=        - pre_auth: pattern=        - external_pre_auth: pattern=        - mesh_backhaul: pattern=        - atf_weight: min=0 max=100 pattern=        - max_clients: min=0 max=4294967295 pattern=        - max_clients_ap: min=0 max=4294967295 pattern=        - ssid: max_length=32 pattern=        - broadcast_ssid: pattern=        - security: pattern=        - pmf: pattern=        - pmf_assoc_comeback_timeout: min=1 max=20 pattern=        - pmf_sa_query_retry_timeout: min=1 max=5 pattern=        - beacon_protection: pattern=        - okc: pattern=        - mbo: pattern=        - gas_comeback_delay: min=100 max=10000 pattern=        - gas_fragmentation_limit: min=512 max=4096 pattern=        - mbo_cell_data_conn_pref: pattern=        - 80211k: pattern=        - 80211v: pattern=        - neighbor_report_dual_band: pattern=        - fast_bss_transition: pattern=        - ft_mobility_domain: min=1 max=65535 pattern=        - ft_r0_key_lifetime: min=1 max=65535 pattern=        - ft_over_ds: pattern=        - sae_groups: pattern=        - owe_groups: pattern=        - owe_transition: pattern=        - owe_transition_ssid: max_length=32 pattern=        - additional_akms: pattern=        - eapol_key_retries: pattern=        - tkip_counter_measure: pattern=        - external_web: max_length=1023 pattern=        - external_web_format: pattern=        - external_logout: max_length=127 pattern=        - mac_username_delimiter: pattern=        - mac_password_delimiter: pattern=        - mac_calling_station_delimiter: pattern=        - mac_called_station_delimiter: pattern=        - mac_case: pattern=        - called_station_id_type: pattern=        - mac_auth_bypass: pattern=        - radius_mac_auth: pattern=        - radius_mac_auth_server: max_length=35 pattern=        - radius_mac_auth_block_interval: min=30 max=864000 pattern=        - radius_mac_mpsk_auth: pattern=        - radius_mac_mpsk_timeout: min=300 max=864000 pattern=        - radius_mac_auth_usergroups: pattern=        - auth: pattern=        - encrypt: pattern=        - keyindex: min=1 max=4 pattern=        - key: max_length=128 pattern=        - passphrase: max_length=128 pattern=        - sae_password: max_length=128 pattern=        - sae_h2e_only: pattern=        - sae_hnp_only: pattern=        - sae_pk: pattern=        - sae_private_key: max_length=359 pattern=        - akm24_only: pattern=        - radius_server: max_length=35 pattern=        - nas_filter_rule: pattern=        - domain_name_stripping: pattern=        - mlo: pattern=        - local_standalone: pattern=        - local_standalone_nat: pattern=        - ip: pattern=        - dhcp_lease_time: min=300 max=8640000 pattern=        - local_standalone_dns: pattern=        - local_standalone_dns_ip: pattern=        - local_lan_partition: pattern=        - local_bridging: pattern=        - local_lan: pattern=        - local_authentication: pattern=        - usergroup: pattern=        - captive_portal: pattern=        - captive_network_assistant_bypass: pattern=        - portal_message_override_group: max_length=35 pattern=        - portal_message_overrides: pattern=        - portal_type: pattern=        - selected_usergroups: pattern=        - security_exempt_list: max_length=35 pattern=        - security_redirect_url: max_length=1023 pattern=        - auth_cert: max_length=35 pattern=        - auth_portal_addr: max_length=63 pattern=        - intra_vap_privacy: pattern=        - schedule: pattern=        - ldpc: pattern=        - high_efficiency: pattern=        - target_wake_time: pattern=        - port_macauth: pattern=        - port_macauth_timeout: min=60 max=65535 pattern=        - port_macauth_reauth_timeout: min=120 max=65535 pattern=        - bss_color_partial: pattern=        - mpsk_profile: max_length=35 pattern=        - split_tunneling: pattern=        - nac: pattern=        - nac_profile: max_length=35 pattern=        - vlanid: min=0 max=4094 pattern=        - vlan_auto: pattern=        - dynamic_vlan: pattern=        - captive_portal_fw_accounting: pattern=        - captive_portal_ac_name: max_length=35 pattern=        - captive_portal_auth_timeout: min=0 max=864000 pattern=        - multicast_rate: pattern=        - multicast_enhance: pattern=        - igmp_snooping: pattern=        - dhcp_address_enforcement: pattern=        - broadcast_suppression: pattern=        - ipv6_rules: pattern=        - me_disable_thresh: min=2 max=256 pattern=        - mu_mimo: pattern=        - probe_resp_suppression: pattern=        - probe_resp_threshold: max_length=7 pattern=        - radio_sensitivity: pattern=        - quarantine: pattern=        - radio_5g_threshold: max_length=7 pattern=        - radio_2g_threshold: max_length=7 pattern=        - vlan_name: pattern=        - vlan_pooling: pattern=        - vlan_pool: pattern=        - dhcp_option43_insertion: pattern=        - dhcp_option82_insertion: pattern=        - dhcp_option82_circuit_id_insertion: pattern=        - dhcp_option82_remote_id_insertion: pattern=        - ptk_rekey: pattern=        - ptk_rekey_intv: min=600 max=864000 pattern=        - gtk_rekey: pattern=        - gtk_rekey_intv: min=600 max=864000 pattern=        - eap_reauth: pattern=        - eap_reauth_intv: min=1800 max=864000 pattern=        - roaming_acct_interim_update: pattern=        - qos_profile: max_length=35 pattern=        - hotspot20_profile: max_length=35 pattern=        - access_control_list: max_length=35 pattern=        - primary_wag_profile: max_length=35 pattern=        - secondary_wag_profile: max_length=35 pattern=        - tunnel_echo_interval: min=1 max=65535 pattern=        - tunnel_fallback_interval: min=0 max=65535 pattern=        - rates_11a: pattern=        - rates_11bg: pattern=        - rates_11n_ss12: pattern=        - rates_11n_ss34: pattern=        - rates_11ac_mcs_map: max_length=63 pattern=        - rates_11ax_mcs_map: max_length=63 pattern=        - rates_11be_mcs_map: max_length=15 pattern=        - rates_11be_mcs_map_160: max_length=15 pattern=        - rates_11be_mcs_map_320: max_length=15 pattern=        - utm_profile: max_length=35 pattern=        - utm_status: pattern=        - utm_log: pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - antivirus_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - scan_botnet_connections: pattern=        - address_group: max_length=79 pattern=        - address_group_policy: pattern=        - sticky_client_remove: pattern=        - sticky_client_threshold_5g: max_length=7 pattern=        - sticky_client_threshold_2g: max_length=7 pattern=        - sticky_client_threshold_6g: max_length=7 pattern=        - bstm_rssi_disassoc_timer: min=1 max=2000 pattern=        - bstm_load_balancing_disassoc_timer: min=1 max=30 pattern=        - bstm_disassociation_imminent: pattern=        - beacon_advertising: pattern=        - osen: pattern=        - application_detection_engine: pattern=        - application_dscp_marking: pattern=        - application_report_intv: min=30 max=864000 pattern=        - l3_roaming: pattern=        - l3_roaming_mode: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=15, default="", description="Virtual AP name.")    
    pre_auth: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable pre-authentication, where supported by clients (default = enable).")    
    external_pre_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable pre-authentication with external APs not managed by the FortiGate (default = disable).")    
    mesh_backhaul: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable using this VAP as a WiFi mesh backhaul (default = disable). This entry is only available when security is set to a WPA type or open.")    
    atf_weight: int | None = Field(ge=0, le=100, default=20, description="Airtime weight in percentage (default = 20).")    
    max_clients: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of clients that can connect simultaneously to the VAP (default = 0, meaning no limitation).")    
    max_clients_ap: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of clients that can connect simultaneously to the VAP per AP radio (default = 0, meaning no limitation).")    
    ssid: str | None = Field(max_length=32, default="fortinet", description="IEEE 802.11 service set identifier (SSID) for the wireless interface. Users who wish to use the wireless network must configure their computers to access this SSID name.")    
    broadcast_ssid: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable broadcasting the SSID (default = enable).")    
    security: SecurityEnum | None = Field(default="wpa2-only-personal", description="Security mode for the wireless interface (default = wpa2-only-personal).")    
    pmf: Literal["disable", "enable", "optional"] | None = Field(default="disable", description="Protected Management Frames (PMF) support (default = disable).")    
    pmf_assoc_comeback_timeout: int | None = Field(ge=1, le=20, default=1, description="Protected Management Frames (PMF) comeback maximum timeout (1-20 sec).")    
    pmf_sa_query_retry_timeout: int | None = Field(ge=1, le=5, default=2, description="Protected Management Frames (PMF) SA query retry timeout interval (1 - 5 100s of msec).")    
    beacon_protection: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable beacon protection support (default = disable).")    
    okc: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable Opportunistic Key Caching (OKC) (default = enable).")    
    mbo: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable Multiband Operation (default = disable).")    
    gas_comeback_delay: int | None = Field(ge=100, le=10000, default=500, description="GAS comeback delay (0 or 100 - 10000 milliseconds, default = 500).")    
    gas_fragmentation_limit: int | None = Field(ge=512, le=4096, default=1024, description="GAS fragmentation limit (512 - 4096, default = 1024).")    
    mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = Field(default="prefer-not", description="MBO cell data connection preference (0, 1, or 255, default = 1).")    
    80211k: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable 802.11k assisted roaming (default = enable).")    
    80211v: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable 802.11v assisted roaming (default = enable).")    
    neighbor_report_dual_band: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable dual-band neighbor report (default = disable).")    
    fast_bss_transition: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable 802.11r Fast BSS Transition (FT) (default = disable).")    
    ft_mobility_domain: int | None = Field(ge=1, le=65535, default=1000, description="Mobility domain identifier in FT (1 - 65535, default = 1000).")    
    ft_r0_key_lifetime: int | None = Field(ge=1, le=65535, default=480, description="Lifetime of the PMK-R0 key in FT, 1-65535 minutes.")    
    ft_over_ds: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable FT over the Distribution System (DS).")    
    sae_groups: list[SaeGroups] = Field(default="", description="SAE-Groups.")    
    owe_groups: list[OweGroups] = Field(default="", description="OWE-Groups.")    
    owe_transition: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable OWE transition mode support.")    
    owe_transition_ssid: str | None = Field(max_length=32, default="", description="OWE transition mode peer SSID.")    
    additional_akms: list[AdditionalAkms] = Field(default="", description="Additional AKMs.")    
    eapol_key_retries: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2) (default = enable).")    
    tkip_counter_measure: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable TKIP counter measure.")    
    external_web: str | None = Field(max_length=1023, default=None, description="URL of external authentication web server.")    
    external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = Field(default="auto-detect", description="URL query parameter detection (default = auto-detect).")    
    external_logout: str | None = Field(max_length=127, default="", description="URL of external authentication logout server.")    
    mac_username_delimiter: MacUsernameDelimiterEnum | None = Field(default="hyphen", description="MAC authentication username delimiter (default = hyphen).")    
    mac_password_delimiter: MacPasswordDelimiterEnum | None = Field(default="hyphen", description="MAC authentication password delimiter (default = hyphen).")    
    mac_calling_station_delimiter: MacCallingStationDelimiterEnum | None = Field(default="hyphen", description="MAC calling station delimiter (default = hyphen).")    
    mac_called_station_delimiter: MacCalledStationDelimiterEnum | None = Field(default="hyphen", description="MAC called station delimiter (default = hyphen).")    
    mac_case: Literal["uppercase", "lowercase"] | None = Field(default="uppercase", description="MAC case (default = uppercase).")    
    called_station_id_type: Literal["mac", "ip", "apname"] | None = Field(default="mac", description="The format type of RADIUS attribute Called-Station-Id (default = mac).")    
    mac_auth_bypass: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable MAC authentication bypass.")    
    radius_mac_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable RADIUS-based MAC authentication of clients (default = disable).")    
    radius_mac_auth_server: str | None = Field(max_length=35, default="", description="RADIUS-based MAC authentication server.")  # datasource: ['user.radius.name']    
    radius_mac_auth_block_interval: int | None = Field(ge=30, le=864000, default=0, description="Don't send RADIUS MAC auth request again if the client has been rejected within specific interval (0 or 30 - 864000 seconds, default = 0, 0 to disable blocking).")    
    radius_mac_mpsk_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication (default = disable).")    
    radius_mac_mpsk_timeout: int | None = Field(ge=300, le=864000, default=86400, description="RADIUS MAC MPSK cache timeout interval (0 or 300 - 864000, default = 86400, 0 to disable caching).")    
    radius_mac_auth_usergroups: list[RadiusMacAuthUsergroups] = Field(default=None, description="Selective user groups that are permitted for RADIUS mac authentication.")    
    auth: Literal["radius", "usergroup"] | None = Field(default="", description="Authentication protocol.")    
    encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = Field(default="AES", description="Encryption protocol to use (only available when security is set to a WPA type).")    
    keyindex: int | None = Field(ge=1, le=4, default=1, description="WEP key index (1 - 4).")    
    key: Any = Field(max_length=128, default=None, description="WEP Key.")    
    passphrase: Any = Field(max_length=128, default=None, description="WPA pre-shared key (PSK) to be used to authenticate WiFi users.")    
    sae_password: Any = Field(max_length=128, default=None, description="WPA3 SAE password to be used to authenticate WiFi users.")    
    sae_h2e_only: Literal["enable", "disable"] | None = Field(default="disable", description="Use hash-to-element-only mechanism for PWE derivation (default = disable).")    
    sae_hnp_only: Literal["enable", "disable"] | None = Field(default="disable", description="Use hunting-and-pecking-only mechanism for PWE derivation (default = disable).")    
    sae_pk: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WPA3 SAE-PK (default = disable).")    
    sae_private_key: str | None = Field(max_length=359, default="", description="Private key used for WPA3 SAE-PK authentication.")    
    akm24_only: Literal["disable", "enable"] | None = Field(default="disable", description="WPA3 SAE using group-dependent hash only (default = disable).")    
    radius_server: str | None = Field(max_length=35, default="", description="RADIUS server to be used to authenticate WiFi users.")  # datasource: ['user.radius.name']    
    nas_filter_rule: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAS filter rule support (default = disable).")    
    domain_name_stripping: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable stripping domain name from identity (default = disable).")    
    mlo: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable WiFi7 Multi-Link-Operation (default = disable).")    
    local_standalone: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AP local standalone (default = disable).")    
    local_standalone_nat: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AP local standalone NAT mode.")    
    ip: Any = Field(default="0.0.0.0 0.0.0.0", description="IP address and subnet mask for the local standalone NAT subnet.")    
    dhcp_lease_time: int | None = Field(ge=300, le=8640000, default=2400, description="DHCP lease time in seconds for NAT IP address.")    
    local_standalone_dns: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AP local standalone DNS.")    
    local_standalone_dns_ip: list[LocalStandaloneDnsIp] = Field(default="", description="IPv4 addresses for the local standalone DNS.")    
    local_lan_partition: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable segregating client traffic to local LAN side (default = disable).")    
    local_bridging: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP (default = disable).")    
    local_lan: Literal["allow", "deny"] | None = Field(default="allow", description="Allow/deny traffic destined for a Class A, B, or C private IP address (default = allow).")    
    local_authentication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AP local authentication.")    
    usergroup: list[Usergroup] = Field(default=None, description="Firewall user group to be used to authenticate WiFi users.")    
    captive_portal: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable captive portal.")    
    captive_network_assistant_bypass: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Captive Network Assistant bypass.")    
    portal_message_override_group: str | None = Field(max_length=35, default="", description="Replacement message group for this VAP (only available when security is set to a captive portal type).")  # datasource: ['system.replacemsg-group.name']    
    portal_message_overrides: list[PortalMessageOverrides] = Field(default=None, description="Individual message overrides.")    
    portal_type: PortalTypeEnum | None = Field(default="auth", description="Captive portal functionality. Configure how the captive portal authenticates users and whether it includes a disclaimer.")    
    selected_usergroups: list[SelectedUsergroups] = Field(default=None, description="Selective user groups that are permitted to authenticate.")    
    security_exempt_list: str | None = Field(max_length=35, default="", description="Optional security exempt list for captive portal authentication.")  # datasource: ['user.security-exempt-list.name']    
    security_redirect_url: str | None = Field(max_length=1023, default=None, description="Optional URL for redirecting users after they pass captive portal authentication.")    
    auth_cert: str | None = Field(max_length=35, default="", description="HTTPS server certificate.")  # datasource: ['vpn.certificate.local.name']    
    auth_portal_addr: str | None = Field(max_length=63, default="", description="Address of captive portal.")    
    intra_vap_privacy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable blocking communication between clients on the same SSID (called intra-SSID privacy) (default = disable).")    
    schedule: list[Schedule] = Field(default=None, description="Firewall schedules for enabling this VAP on the FortiAP. This VAP will be enabled when at least one of the schedules is valid. Separate multiple schedule names with a space.")    
    ldpc: LdpcEnum | None = Field(default="rxtx", description="VAP low-density parity-check (LDPC) coding configuration.")    
    high_efficiency: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable 802.11ax high efficiency (default = enable).")    
    target_wake_time: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable 802.11ax target wake time (default = enable).")    
    port_macauth: Literal["disable", "radius", "address-group"] | None = Field(default="disable", description="Enable/disable LAN port MAC authentication (default = disable).")    
    port_macauth_timeout: int | None = Field(ge=60, le=65535, default=600, description="LAN port MAC authentication idle timeout value (default = 600 sec).")    
    port_macauth_reauth_timeout: int | None = Field(ge=120, le=65535, default=7200, description="LAN port MAC authentication re-authentication timeout value (default = 7200 sec).")    
    bss_color_partial: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable 802.11ax partial BSS color (default = enable).")    
    mpsk_profile: str | None = Field(max_length=35, default="", description="MPSK profile name.")  # datasource: ['wireless-controller.mpsk-profile.name']    
    split_tunneling: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable split tunneling (default = disable).")    
    nac: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable network access control.")    
    nac_profile: str | None = Field(max_length=35, default="", description="NAC profile name.")  # datasource: ['wireless-controller.nac-profile.name']    
    vlanid: int | None = Field(ge=0, le=4094, default=0, description="Optional VLAN ID.")    
    vlan_auto: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic management of SSID VLAN interface.")    
    dynamic_vlan: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dynamic VLAN assignment.")    
    captive_portal_fw_accounting: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable RADIUS accounting for captive portal firewall authentication session.")    
    captive_portal_ac_name: str | None = Field(max_length=35, default="", description="Local-bridging captive portal ac-name.")    
    captive_portal_auth_timeout: int | None = Field(ge=0, le=864000, default=0, description="Hard timeout - AP will always clear the session after timeout regardless of traffic (0 - 864000 sec, default = 0).")    
    multicast_rate: MulticastRateEnum | None = Field(default="0", description="Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0).")    
    multicast_enhance: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable converting multicast to unicast to improve performance (default = disable).")    
    igmp_snooping: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IGMP snooping.")    
    dhcp_address_enforcement: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DHCP address enforcement (default = disable).")    
    broadcast_suppression: list[BroadcastSuppression] = Field(default="dhcp-up dhcp-ucast arp-known", description="Optional suppression of broadcast messages. For example, you can keep DHCP messages, ARP broadcasts, and so on off of the wireless network.")    
    ipv6_rules: list[Ipv6Rules] = Field(default="drop-icmp6ra drop-icmp6rs drop-llmnr6 drop-icmp6mld2 drop-dhcp6s drop-dhcp6c ndp-proxy drop-ns-dad", description="Optional rules of IPv6 packets. For example, you can keep RA, RS and so on off of the wireless network.")    
    me_disable_thresh: int | None = Field(ge=2, le=256, default=32, description="Disable multicast enhancement when this many clients are receiving multicast traffic.")    
    mu_mimo: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Multi-user MIMO (default = enable).")    
    probe_resp_suppression: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable probe response suppression (to ignore weak signals) (default = disable).")    
    probe_resp_threshold: str | None = Field(max_length=7, default="-80", description="Minimum signal level/threshold in dBm required for the AP response to probe requests (-95 to -20, default = -80).")    
    radio_sensitivity: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable software radio sensitivity (to ignore weak signals) (default = disable).")    
    quarantine: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable station quarantine (default = disable).")    
    radio_5g_threshold: str | None = Field(max_length=7, default="-76", description="Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band(-95 to -20, default = -76).")    
    radio_2g_threshold: str | None = Field(max_length=7, default="-79", description="Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2.4G band (-95 to -20, default = -79).")    
    vlan_name: list[VlanName] = Field(default=None, description="Table for mapping VLAN name to VLAN ID.")    
    vlan_pooling: VlanPoolingEnum | None = Field(default="disable", description="Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools (default = disable). When set to wtp-group, VLAN pooling occurs with VLAN assignment by wtp-group.")    
    vlan_pool: list[VlanPool] = Field(default=None, description="VLAN pool.")    
    dhcp_option43_insertion: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable insertion of DHCP option 43 (default = enable).")    
    dhcp_option82_insertion: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DHCP option 82 insert (default = disable).")    
    dhcp_option82_circuit_id_insertion: DhcpOption82CircuitIdInsertionEnum | None = Field(default="disable", description="Enable/disable DHCP option 82 circuit-id insert (default = disable).")    
    dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = Field(default="disable", description="Enable/disable DHCP option 82 remote-id insert (default = disable).")    
    ptk_rekey: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PTK rekey for WPA-Enterprise security.")    
    ptk_rekey_intv: int | None = Field(ge=600, le=864000, default=86400, description="PTK rekey interval (600 - 864000 sec, default = 86400).")    
    gtk_rekey: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable GTK rekey for WPA security.")    
    gtk_rekey_intv: int | None = Field(ge=600, le=864000, default=86400, description="GTK rekey interval (600 - 864000 sec, default = 86400).")    
    eap_reauth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable EAP re-authentication for WPA-Enterprise security.")    
    eap_reauth_intv: int | None = Field(ge=1800, le=864000, default=86400, description="EAP re-authentication interval (1800 - 864000 sec, default = 86400).")    
    roaming_acct_interim_update: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable using accounting interim update instead of accounting start/stop on roaming for WPA-Enterprise security.")    
    qos_profile: str | None = Field(max_length=35, default="", description="Quality of service profile name.")  # datasource: ['wireless-controller.qos-profile.name']    
    hotspot20_profile: str | None = Field(max_length=35, default="", description="Hotspot 2.0 profile name.")  # datasource: ['wireless-controller.hotspot20.hs-profile.name']    
    access_control_list: str | None = Field(max_length=35, default="", description="Profile name for access-control-list.")  # datasource: ['wireless-controller.access-control-list.name']    
    primary_wag_profile: str | None = Field(max_length=35, default="", description="Primary wireless access gateway profile name.")  # datasource: ['wireless-controller.wag-profile.name']    
    secondary_wag_profile: str | None = Field(max_length=35, default="", description="Secondary wireless access gateway profile name.")  # datasource: ['wireless-controller.wag-profile.name']    
    tunnel_echo_interval: int | None = Field(ge=1, le=65535, default=300, description="The time interval to send echo to both primary and secondary tunnel peers (1 - 65535 sec, default = 300).")    
    tunnel_fallback_interval: int | None = Field(ge=0, le=65535, default=7200, description="The time interval for secondary tunnel to fall back to primary tunnel (0 - 65535 sec, default = 7200).")    
    rates_11a: list[Rates11A] = Field(default="", description="Allowed data rates for 802.11a.")    
    rates_11bg: list[Rates11Bg] = Field(default="", description="Allowed data rates for 802.11b/g.")    
    rates_11n_ss12: list[Rates11NSs12] = Field(default="", description="Allowed data rates for 802.11n with 1 or 2 spatial streams.")    
    rates_11n_ss34: list[Rates11NSs34] = Field(default="", description="Allowed data rates for 802.11n with 3 or 4 spatial streams.")    
    rates_11ac_mcs_map: str | None = Field(max_length=63, default="", description="Comma separated list of max supported VHT MCS for spatial streams 1 through 8.")    
    rates_11ax_mcs_map: str | None = Field(max_length=63, default="", description="Comma separated list of max supported HE MCS for spatial streams 1 through 8.")    
    rates_11be_mcs_map: str | None = Field(max_length=15, default="", description="Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 20MHz/40MHz/80MHz bandwidth.")    
    rates_11be_mcs_map_160: str | None = Field(max_length=15, default="", description="Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 160MHz bandwidth.")    
    rates_11be_mcs_map_320: str | None = Field(max_length=15, default="", description="Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 320MHz bandwidth.")    
    utm_profile: str | None = Field(max_length=35, default="", description="UTM profile name.")  # datasource: ['wireless-controller.utm-profile.name']    
    utm_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to add one or more security profiles (AV, IPS, etc.) to the VAP.")    
    utm_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable UTM logging.")    
    ips_sensor: str | None = Field(max_length=47, default="", description="IPS sensor name.")  # datasource: ['ips.sensor.name']    
    application_list: str | None = Field(max_length=47, default="", description="Application control list name.")  # datasource: ['application.list.name']    
    antivirus_profile: str | None = Field(max_length=47, default="", description="AntiVirus profile name.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile: str | None = Field(max_length=47, default="", description="WebFilter profile name.")  # datasource: ['webfilter.profile.name']    
    scan_botnet_connections: Literal["disable", "monitor", "block"] | None = Field(default="monitor", description="Block or monitor connections to Botnet servers or disable Botnet scanning.")    
    address_group: str | None = Field(max_length=79, default="", description="Firewall Address Group Name.")  # datasource: ['firewall.addrgrp.name']    
    address_group_policy: Literal["disable", "allow", "deny"] | None = Field(default="disable", description="Configure MAC address filtering policy for MAC addresses that are in the address-group.")    
    sticky_client_remove: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sticky client remove to maintain good signal level clients in SSID (default = disable).")    
    sticky_client_threshold_5g: str | None = Field(max_length=7, default="-76", description="Minimum signal level/threshold in dBm required for the 5G client to be serviced by the AP (-95 to -20, default = -76).")    
    sticky_client_threshold_2g: str | None = Field(max_length=7, default="-79", description="Minimum signal level/threshold in dBm required for the 2G client to be serviced by the AP (-95 to -20, default = -79).")    
    sticky_client_threshold_6g: str | None = Field(max_length=7, default="-76", description="Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP (-95 to -20, default = -76).")    
    bstm_rssi_disassoc_timer: int | None = Field(ge=1, le=2000, default=200, description="Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI (0 to 2000, default = 200).")    
    bstm_load_balancing_disassoc_timer: int | None = Field(ge=1, le=30, default=10, description="Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing (0 to 30, default = 10).")    
    bstm_disassociation_imminent: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable forcing of disassociation after the BSTM request timer has been reached (default = enable).")    
    beacon_advertising: list[BeaconAdvertising] = Field(default="", description="Fortinet beacon advertising IE data   (default = empty).")    
    osen: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable OSEN as part of key management (default = disable).")    
    application_detection_engine: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application detection engine (default = disable).")    
    application_dscp_marking: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application attribute based DSCP marking (default = disable).")    
    application_report_intv: int | None = Field(ge=30, le=864000, default=120, description="Application report interval (30 - 864000 sec, default = 120).")    
    l3_roaming: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable layer 3 roaming (default = disable).")    
    l3_roaming_mode: Literal["direct", "indirect"] | None = Field(default="direct", description="Select the way that layer 3 roaming traffic is passed (default = direct).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('radius_mac_auth_server')
    @classmethod
    def validate_radius_mac_auth_server(cls, v: Any) -> Any:
        """
        Validate radius_mac_auth_server field.
        
        Datasource: ['user.radius.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('radius_server')
    @classmethod
    def validate_radius_server(cls, v: Any) -> Any:
        """
        Validate radius_server field.
        
        Datasource: ['user.radius.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('portal_message_override_group')
    @classmethod
    def validate_portal_message_override_group(cls, v: Any) -> Any:
        """
        Validate portal_message_override_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('security_exempt_list')
    @classmethod
    def validate_security_exempt_list(cls, v: Any) -> Any:
        """
        Validate security_exempt_list field.
        
        Datasource: ['user.security-exempt-list.name']
        
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
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('mpsk_profile')
    @classmethod
    def validate_mpsk_profile(cls, v: Any) -> Any:
        """
        Validate mpsk_profile field.
        
        Datasource: ['wireless-controller.mpsk-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('nac_profile')
    @classmethod
    def validate_nac_profile(cls, v: Any) -> Any:
        """
        Validate nac_profile field.
        
        Datasource: ['wireless-controller.nac-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('qos_profile')
    @classmethod
    def validate_qos_profile(cls, v: Any) -> Any:
        """
        Validate qos_profile field.
        
        Datasource: ['wireless-controller.qos-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hotspot20_profile')
    @classmethod
    def validate_hotspot20_profile(cls, v: Any) -> Any:
        """
        Validate hotspot20_profile field.
        
        Datasource: ['wireless-controller.hotspot20.hs-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('access_control_list')
    @classmethod
    def validate_access_control_list(cls, v: Any) -> Any:
        """
        Validate access_control_list field.
        
        Datasource: ['wireless-controller.access-control-list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('primary_wag_profile')
    @classmethod
    def validate_primary_wag_profile(cls, v: Any) -> Any:
        """
        Validate primary_wag_profile field.
        
        Datasource: ['wireless-controller.wag-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('secondary_wag_profile')
    @classmethod
    def validate_secondary_wag_profile(cls, v: Any) -> Any:
        """
        Validate secondary_wag_profile field.
        
        Datasource: ['wireless-controller.wag-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('utm_profile')
    @classmethod
    def validate_utm_profile(cls, v: Any) -> Any:
        """
        Validate utm_profile field.
        
        Datasource: ['wireless-controller.utm-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_sensor')
    @classmethod
    def validate_ips_sensor(cls, v: Any) -> Any:
        """
        Validate ips_sensor field.
        
        Datasource: ['ips.sensor.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('application_list')
    @classmethod
    def validate_application_list(cls, v: Any) -> Any:
        """
        Validate application_list field.
        
        Datasource: ['application.list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('antivirus_profile')
    @classmethod
    def validate_antivirus_profile(cls, v: Any) -> Any:
        """
        Validate antivirus_profile field.
        
        Datasource: ['antivirus.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webfilter_profile')
    @classmethod
    def validate_webfilter_profile(cls, v: Any) -> Any:
        """
        Validate webfilter_profile field.
        
        Datasource: ['webfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('address_group')
    @classmethod
    def validate_address_group(cls, v: Any) -> Any:
        """
        Validate address_group field.
        
        Datasource: ['firewall.addrgrp.name']
        
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
    async def validate_radius_mac_auth_server_references(self, client: Any) -> list[str]:
        """
        Validate radius_mac_auth_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/radius        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     radius_mac_auth_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_radius_mac_auth_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "radius_mac_auth_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.radius.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Radius-Mac-Auth-Server '{value}' not found in "
                "user/radius"
            )        
        return errors    
    async def validate_radius_mac_auth_usergroups_references(self, client: Any) -> list[str]:
        """
        Validate radius_mac_auth_usergroups references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     radius_mac_auth_usergroups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_radius_mac_auth_usergroups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "radius_mac_auth_usergroups", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Radius-Mac-Auth-Usergroups '{value}' not found in "
                    "user/group"
                )        
        return errors    
    async def validate_radius_server_references(self, client: Any) -> list[str]:
        """
        Validate radius_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/radius        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     radius_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_radius_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "radius_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.radius.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Radius-Server '{value}' not found in "
                "user/radius"
            )        
        return errors    
    async def validate_usergroup_references(self, client: Any) -> list[str]:
        """
        Validate usergroup references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     usergroup=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_usergroup_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "usergroup", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Usergroup '{value}' not found in "
                    "user/group"
                )        
        return errors    
    async def validate_portal_message_override_group_references(self, client: Any) -> list[str]:
        """
        Validate portal_message_override_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/replacemsg-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     portal_message_override_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_portal_message_override_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "portal_message_override_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.replacemsg-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Portal-Message-Override-Group '{value}' not found in "
                "system/replacemsg-group"
            )        
        return errors    
    async def validate_selected_usergroups_references(self, client: Any) -> list[str]:
        """
        Validate selected_usergroups references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     selected_usergroups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_selected_usergroups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "selected_usergroups", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Selected-Usergroups '{value}' not found in "
                    "user/group"
                )        
        return errors    
    async def validate_security_exempt_list_references(self, client: Any) -> list[str]:
        """
        Validate security_exempt_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/security-exempt-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     security_exempt_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_security_exempt_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "security_exempt_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.security-exempt-list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Security-Exempt-List '{value}' not found in "
                "user/security-exempt-list"
            )        
        return errors    
    async def validate_auth_cert_references(self, client: Any) -> list[str]:
        """
        Validate auth_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     auth_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Cert '{value}' not found in "
                "vpn/certificate/local"
            )        
        return errors    
    async def validate_schedule_references(self, client: Any) -> list[str]:
        """
        Validate schedule references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/schedule/group        - firewall/schedule/recurring        - firewall/schedule/onetime        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     schedule=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_schedule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "schedule", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.schedule.group.exists(value):
                found = True
            elif await client.api.cmdb.firewall.schedule.recurring.exists(value):
                found = True
            elif await client.api.cmdb.firewall.schedule.onetime.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Schedule '{value}' not found in "
                    "firewall/schedule/group or firewall/schedule/recurring or firewall/schedule/onetime"
                )        
        return errors    
    async def validate_mpsk_profile_references(self, client: Any) -> list[str]:
        """
        Validate mpsk_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/mpsk-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     mpsk_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_mpsk_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "mpsk_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.mpsk-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Mpsk-Profile '{value}' not found in "
                "wireless-controller/mpsk-profile"
            )        
        return errors    
    async def validate_nac_profile_references(self, client: Any) -> list[str]:
        """
        Validate nac_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/nac-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     nac_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_nac_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "nac_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.nac-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Nac-Profile '{value}' not found in "
                "wireless-controller/nac-profile"
            )        
        return errors    
    async def validate_vlan_pool_references(self, client: Any) -> list[str]:
        """
        Validate vlan_pool references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/wtp-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     vlan_pool=[{"wtp-group": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vlan_pool_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "vlan_pool", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("wtp-group")
            else:
                value = getattr(item, "wtp-group", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.wireless-controller.wtp-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Vlan-Pool '{value}' not found in "
                    "wireless-controller/wtp-group"
                )        
        return errors    
    async def validate_qos_profile_references(self, client: Any) -> list[str]:
        """
        Validate qos_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/qos-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     qos_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_qos_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "qos_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.qos-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Qos-Profile '{value}' not found in "
                "wireless-controller/qos-profile"
            )        
        return errors    
    async def validate_hotspot20_profile_references(self, client: Any) -> list[str]:
        """
        Validate hotspot20_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/hs-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     hotspot20_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_hotspot20_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "hotspot20_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.hs-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Hotspot20-Profile '{value}' not found in "
                "wireless-controller/hotspot20/hs-profile"
            )        
        return errors    
    async def validate_access_control_list_references(self, client: Any) -> list[str]:
        """
        Validate access_control_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/access-control-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     access_control_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_access_control_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "access_control_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.access-control-list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Access-Control-List '{value}' not found in "
                "wireless-controller/access-control-list"
            )        
        return errors    
    async def validate_primary_wag_profile_references(self, client: Any) -> list[str]:
        """
        Validate primary_wag_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/wag-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     primary_wag_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_primary_wag_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "primary_wag_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.wag-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Primary-Wag-Profile '{value}' not found in "
                "wireless-controller/wag-profile"
            )        
        return errors    
    async def validate_secondary_wag_profile_references(self, client: Any) -> list[str]:
        """
        Validate secondary_wag_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/wag-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     secondary_wag_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_secondary_wag_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "secondary_wag_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.wag-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Secondary-Wag-Profile '{value}' not found in "
                "wireless-controller/wag-profile"
            )        
        return errors    
    async def validate_utm_profile_references(self, client: Any) -> list[str]:
        """
        Validate utm_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/utm-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     utm_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_utm_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "utm_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.utm-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Utm-Profile '{value}' not found in "
                "wireless-controller/utm-profile"
            )        
        return errors    
    async def validate_ips_sensor_references(self, client: Any) -> list[str]:
        """
        Validate ips_sensor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - ips/sensor        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ips_sensor", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.ips.sensor.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ips-Sensor '{value}' not found in "
                "ips/sensor"
            )        
        return errors    
    async def validate_application_list_references(self, client: Any) -> list[str]:
        """
        Validate application_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - application/list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     application_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_application_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "application_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.application.list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Application-List '{value}' not found in "
                "application/list"
            )        
        return errors    
    async def validate_antivirus_profile_references(self, client: Any) -> list[str]:
        """
        Validate antivirus_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - antivirus/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     antivirus_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_antivirus_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "antivirus_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.antivirus.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Antivirus-Profile '{value}' not found in "
                "antivirus/profile"
            )        
        return errors    
    async def validate_webfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate webfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - webfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     webfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "webfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.webfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Webfilter-Profile '{value}' not found in "
                "webfilter/profile"
            )        
        return errors    
    async def validate_address_group_references(self, client: Any) -> list[str]:
        """
        Validate address_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VapModel(
            ...     address_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_address_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.vap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "address_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Address-Group '{value}' not found in "
                "firewall/addrgrp"
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
        
        errors = await self.validate_radius_mac_auth_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_radius_mac_auth_usergroups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_radius_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_usergroup_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_portal_message_override_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_selected_usergroups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_security_exempt_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_schedule_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_mpsk_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_nac_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vlan_pool_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_qos_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_hotspot20_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_access_control_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_primary_wag_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_secondary_wag_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_utm_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_sensor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_application_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_antivirus_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_address_group_references(client)
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
    "VapModel",    "VapRadiusMacAuthUsergroups",    "VapUsergroup",    "VapPortalMessageOverrides",    "VapSelectedUsergroups",    "VapSchedule",    "VapVlanName",    "VapVlanPool",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.496166Z
# ============================================================================
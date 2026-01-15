from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class VapPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/vap payload fields.
    
    Configure Virtual Access Points (VAPs).
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.antivirus.profile.ProfileEndpoint` (via: antivirus-profile)
        - :class:`~.application.list.ListEndpoint` (via: application-list)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: address-group)
        - :class:`~.ips.sensor.SensorEndpoint` (via: ips-sensor)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: portal-message-override-group)
        - :class:`~.user.radius.RadiusEndpoint` (via: radius-mac-auth-server, radius-server)
        - :class:`~.user.security-exempt-list.SecurityExemptListEndpoint` (via: security-exempt-list)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: auth-cert)
        - :class:`~.webfilter.profile.ProfileEndpoint` (via: webfilter-profile)
        - :class:`~.wireless-controller.access-control-list.AccessControlListEndpoint` (via: access-control-list)
        - ... and 6 more dependencies

    **Usage:**
        payload: VapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Virtual AP name. | MaxLen: 15
    pre_auth: Literal["enable", "disable"]  # Enable/disable pre-authentication, where supported | Default: enable
    external_pre_auth: Literal["enable", "disable"]  # Enable/disable pre-authentication with external AP | Default: disable
    mesh_backhaul: Literal["enable", "disable"]  # Enable/disable using this VAP as a WiFi mesh backh | Default: disable
    atf_weight: int  # Airtime weight in percentage (default = 20). | Default: 20 | Min: 0 | Max: 100
    max_clients: int  # Maximum number of clients that can connect simulta | Default: 0 | Min: 0 | Max: 4294967295
    max_clients_ap: int  # Maximum number of clients that can connect simulta | Default: 0 | Min: 0 | Max: 4294967295
    ssid: str  # IEEE 802.11 service set identifier (SSID) for the | Default: fortinet | MaxLen: 32
    broadcast_ssid: Literal["enable", "disable"]  # Enable/disable broadcasting the SSID | Default: enable
    security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"]  # Security mode for the wireless interface | Default: wpa2-only-personal
    pmf: Literal["disable", "enable", "optional"]  # Protected Management Frames (PMF) support | Default: disable
    pmf_assoc_comeback_timeout: int  # Protected Management Frames (PMF) comeback maximum | Default: 1 | Min: 1 | Max: 20
    pmf_sa_query_retry_timeout: int  # Protected Management Frames (PMF) SA query retry t | Default: 2 | Min: 1 | Max: 5
    beacon_protection: Literal["disable", "enable"]  # Enable/disable beacon protection support | Default: disable
    okc: Literal["disable", "enable"]  # Enable/disable Opportunistic Key Caching (OKC) | Default: enable
    mbo: Literal["disable", "enable"]  # Enable/disable Multiband Operation | Default: disable
    gas_comeback_delay: int  # GAS comeback delay | Default: 500 | Min: 100 | Max: 10000
    gas_fragmentation_limit: int  # GAS fragmentation limit | Default: 1024 | Min: 512 | Max: 4096
    mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"]  # MBO cell data connection preference | Default: prefer-not
    x80211k: Literal["disable", "enable"]  # Enable/disable 802.11k assisted roaming | Default: enable
    x80211v: Literal["disable", "enable"]  # Enable/disable 802.11v assisted roaming | Default: enable
    neighbor_report_dual_band: Literal["disable", "enable"]  # Enable/disable dual-band neighbor report | Default: disable
    fast_bss_transition: Literal["disable", "enable"]  # Enable/disable 802.11r Fast BSS Transition (FT) | Default: disable
    ft_mobility_domain: int  # Mobility domain identifier in FT | Default: 1000 | Min: 1 | Max: 65535
    ft_r0_key_lifetime: int  # Lifetime of the PMK-R0 key in FT, 1-65535 minutes. | Default: 480 | Min: 1 | Max: 65535
    ft_over_ds: Literal["disable", "enable"]  # Enable/disable FT over the Distribution System | Default: disable
    sae_groups: Literal["19", "20", "21"]  # SAE-Groups.
    owe_groups: Literal["19", "20", "21"]  # OWE-Groups.
    owe_transition: Literal["disable", "enable"]  # Enable/disable OWE transition mode support. | Default: disable
    owe_transition_ssid: str  # OWE transition mode peer SSID. | MaxLen: 32
    additional_akms: Literal["akm6", "akm24"]  # Additional AKMs.
    eapol_key_retries: Literal["disable", "enable"]  # Enable/disable retransmission of EAPOL-Key frames | Default: enable
    tkip_counter_measure: Literal["enable", "disable"]  # Enable/disable TKIP counter measure. | Default: enable
    external_web: str  # URL of external authentication web server. | MaxLen: 1023
    external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"]  # URL query parameter detection | Default: auto-detect
    external_logout: str  # URL of external authentication logout server. | MaxLen: 127
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication username delimiter | Default: hyphen
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication password delimiter | Default: hyphen
    mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC calling station delimiter (default = hyphen). | Default: hyphen
    mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC called station delimiter (default = hyphen). | Default: hyphen
    mac_case: Literal["uppercase", "lowercase"]  # MAC case (default = uppercase). | Default: uppercase
    called_station_id_type: Literal["mac", "ip", "apname"]  # The format type of RADIUS attribute Called-Station | Default: mac
    mac_auth_bypass: Literal["enable", "disable"]  # Enable/disable MAC authentication bypass. | Default: disable
    radius_mac_auth: Literal["enable", "disable"]  # Enable/disable RADIUS-based MAC authentication of | Default: disable
    radius_mac_auth_server: str  # RADIUS-based MAC authentication server. | MaxLen: 35
    radius_mac_auth_block_interval: int  # Don't send RADIUS MAC auth request again if the cl | Default: 0 | Min: 30 | Max: 864000
    radius_mac_mpsk_auth: Literal["enable", "disable"]  # Enable/disable RADIUS-based MAC authentication of | Default: disable
    radius_mac_mpsk_timeout: int  # RADIUS MAC MPSK cache timeout interval | Default: 86400 | Min: 300 | Max: 864000
    radius_mac_auth_usergroups: list[dict[str, Any]]  # Selective user groups that are permitted for RADIU
    auth: Literal["radius", "usergroup"]  # Authentication protocol.
    encrypt: Literal["TKIP", "AES", "TKIP-AES"]  # Encryption protocol to use | Default: AES
    keyindex: int  # WEP key index (1 - 4). | Default: 1 | Min: 1 | Max: 4
    key: str  # WEP Key. | MaxLen: 128
    passphrase: str  # WPA pre-shared key (PSK) to be used to authenticat | MaxLen: 128
    sae_password: str  # WPA3 SAE password to be used to authenticate WiFi | MaxLen: 128
    sae_h2e_only: Literal["enable", "disable"]  # Use hash-to-element-only mechanism for PWE derivat | Default: disable
    sae_hnp_only: Literal["enable", "disable"]  # Use hunting-and-pecking-only mechanism for PWE der | Default: disable
    sae_pk: Literal["enable", "disable"]  # Enable/disable WPA3 SAE-PK (default = disable). | Default: disable
    sae_private_key: str  # Private key used for WPA3 SAE-PK authentication. | MaxLen: 359
    akm24_only: Literal["disable", "enable"]  # WPA3 SAE using group-dependent hash only | Default: disable
    radius_server: str  # RADIUS server to be used to authenticate WiFi user | MaxLen: 35
    nas_filter_rule: Literal["enable", "disable"]  # Enable/disable NAS filter rule support | Default: disable
    domain_name_stripping: Literal["disable", "enable"]  # Enable/disable stripping domain name from identity | Default: disable
    mlo: Literal["disable", "enable"]  # Enable/disable WiFi7 Multi-Link-Operation | Default: disable
    local_standalone: Literal["enable", "disable"]  # Enable/disable AP local standalone | Default: disable
    local_standalone_nat: Literal["enable", "disable"]  # Enable/disable AP local standalone NAT mode. | Default: disable
    ip: str  # IP address and subnet mask for the local standalon | Default: 0.0.0.0 0.0.0.0
    dhcp_lease_time: int  # DHCP lease time in seconds for NAT IP address. | Default: 2400 | Min: 300 | Max: 8640000
    local_standalone_dns: Literal["enable", "disable"]  # Enable/disable AP local standalone DNS. | Default: disable
    local_standalone_dns_ip: list[dict[str, Any]]  # IPv4 addresses for the local standalone DNS.
    local_lan_partition: Literal["enable", "disable"]  # Enable/disable segregating client traffic to local | Default: disable
    local_bridging: Literal["enable", "disable"]  # Enable/disable bridging of wireless and Ethernet i | Default: disable
    local_lan: Literal["allow", "deny"]  # Allow/deny traffic destined for a Class A, B, or C | Default: allow
    local_authentication: Literal["enable", "disable"]  # Enable/disable AP local authentication. | Default: disable
    usergroup: list[dict[str, Any]]  # Firewall user group to be used to authenticate WiF
    captive_portal: Literal["enable", "disable"]  # Enable/disable captive portal. | Default: disable
    captive_network_assistant_bypass: Literal["enable", "disable"]  # Enable/disable Captive Network Assistant bypass. | Default: disable
    portal_message_override_group: str  # Replacement message group for this VAP | MaxLen: 35
    portal_message_overrides: str  # Individual message overrides.
    portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"]  # Captive portal functionality. Configure how the ca | Default: auth
    selected_usergroups: list[dict[str, Any]]  # Selective user groups that are permitted to authen
    security_exempt_list: str  # Optional security exempt list for captive portal a | MaxLen: 35
    security_redirect_url: str  # Optional URL for redirecting users after they pass | MaxLen: 1023
    auth_cert: str  # HTTPS server certificate. | MaxLen: 35
    auth_portal_addr: str  # Address of captive portal. | MaxLen: 63
    intra_vap_privacy: Literal["enable", "disable"]  # Enable/disable blocking communication between clie | Default: disable
    schedule: list[dict[str, Any]]  # Firewall schedules for enabling this VAP on the Fo
    ldpc: Literal["disable", "rx", "tx", "rxtx"]  # VAP low-density parity-check (LDPC) coding configu | Default: rxtx
    high_efficiency: Literal["enable", "disable"]  # Enable/disable 802.11ax high efficiency | Default: enable
    target_wake_time: Literal["enable", "disable"]  # Enable/disable 802.11ax target wake time | Default: enable
    port_macauth: Literal["disable", "radius", "address-group"]  # Enable/disable LAN port MAC authentication | Default: disable
    port_macauth_timeout: int  # LAN port MAC authentication idle timeout value | Default: 600 | Min: 60 | Max: 65535
    port_macauth_reauth_timeout: int  # LAN port MAC authentication re-authentication time | Default: 7200 | Min: 120 | Max: 65535
    bss_color_partial: Literal["enable", "disable"]  # Enable/disable 802.11ax partial BSS color | Default: enable
    mpsk_profile: str  # MPSK profile name. | MaxLen: 35
    split_tunneling: Literal["enable", "disable"]  # Enable/disable split tunneling (default = disable) | Default: disable
    nac: Literal["enable", "disable"]  # Enable/disable network access control. | Default: disable
    nac_profile: str  # NAC profile name. | MaxLen: 35
    vlanid: int  # Optional VLAN ID. | Default: 0 | Min: 0 | Max: 4094
    vlan_auto: Literal["enable", "disable"]  # Enable/disable automatic management of SSID VLAN i | Default: disable
    dynamic_vlan: Literal["enable", "disable"]  # Enable/disable dynamic VLAN assignment. | Default: disable
    captive_portal_fw_accounting: Literal["enable", "disable"]  # Enable/disable RADIUS accounting for captive porta | Default: disable
    captive_portal_ac_name: str  # Local-bridging captive portal ac-name. | MaxLen: 35
    captive_portal_auth_timeout: int  # Hard timeout - AP will always clear the session af | Default: 0 | Min: 0 | Max: 864000
    multicast_rate: Literal["0", "6000", "12000", "24000"]  # Multicast rate | Default: 0
    multicast_enhance: Literal["enable", "disable"]  # Enable/disable converting multicast to unicast to | Default: disable
    igmp_snooping: Literal["enable", "disable"]  # Enable/disable IGMP snooping. | Default: disable
    dhcp_address_enforcement: Literal["enable", "disable"]  # Enable/disable DHCP address enforcement | Default: disable
    broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"]  # Optional suppression of broadcast messages. For ex | Default: dhcp-up dhcp-ucast arp-known
    ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"]  # Optional rules of IPv6 packets. For example, you c | Default: drop-icmp6ra drop-icmp6rs drop-llmnr6 drop-icmp6mld2 drop-dhcp6s drop-dhcp6c ndp-proxy drop-ns-dad
    me_disable_thresh: int  # Disable multicast enhancement when this many clien | Default: 32 | Min: 2 | Max: 256
    mu_mimo: Literal["enable", "disable"]  # Enable/disable Multi-user MIMO (default = enable). | Default: enable
    probe_resp_suppression: Literal["enable", "disable"]  # Enable/disable probe response suppression | Default: disable
    probe_resp_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -80 | MaxLen: 7
    radio_sensitivity: Literal["enable", "disable"]  # Enable/disable software radio sensitivity | Default: disable
    quarantine: Literal["enable", "disable"]  # Enable/disable station quarantine | Default: disable
    radio_5g_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -76 | MaxLen: 7
    radio_2g_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -79 | MaxLen: 7
    vlan_name: list[dict[str, Any]]  # Table for mapping VLAN name to VLAN ID.
    vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"]  # Enable/disable VLAN pooling, to allow grouping of | Default: disable
    vlan_pool: list[dict[str, Any]]  # VLAN pool.
    dhcp_option43_insertion: Literal["enable", "disable"]  # Enable/disable insertion of DHCP option 43 | Default: enable
    dhcp_option82_insertion: Literal["enable", "disable"]  # Enable/disable DHCP option 82 insert | Default: disable
    dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"]  # Enable/disable DHCP option 82 circuit-id insert | Default: disable
    dhcp_option82_remote_id_insertion: Literal["style-1", "disable"]  # Enable/disable DHCP option 82 remote-id insert | Default: disable
    ptk_rekey: Literal["enable", "disable"]  # Enable/disable PTK rekey for WPA-Enterprise securi | Default: disable
    ptk_rekey_intv: int  # PTK rekey interval | Default: 86400 | Min: 600 | Max: 864000
    gtk_rekey: Literal["enable", "disable"]  # Enable/disable GTK rekey for WPA security. | Default: disable
    gtk_rekey_intv: int  # GTK rekey interval | Default: 86400 | Min: 600 | Max: 864000
    eap_reauth: Literal["enable", "disable"]  # Enable/disable EAP re-authentication for WPA-Enter | Default: disable
    eap_reauth_intv: int  # EAP re-authentication interval | Default: 86400 | Min: 1800 | Max: 864000
    roaming_acct_interim_update: Literal["enable", "disable"]  # Enable/disable using accounting interim update ins | Default: disable
    qos_profile: str  # Quality of service profile name. | MaxLen: 35
    hotspot20_profile: str  # Hotspot 2.0 profile name. | MaxLen: 35
    access_control_list: str  # Profile name for access-control-list. | MaxLen: 35
    primary_wag_profile: str  # Primary wireless access gateway profile name. | MaxLen: 35
    secondary_wag_profile: str  # Secondary wireless access gateway profile name. | MaxLen: 35
    tunnel_echo_interval: int  # The time interval to send echo to both primary and | Default: 300 | Min: 1 | Max: 65535
    tunnel_fallback_interval: int  # The time interval for secondary tunnel to fall bac | Default: 7200 | Min: 0 | Max: 65535
    rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]  # Allowed data rates for 802.11a.
    rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]  # Allowed data rates for 802.11b/g.
    rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"]  # Allowed data rates for 802.11n with 1 or 2 spatial
    rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"]  # Allowed data rates for 802.11n with 3 or 4 spatial
    rates_11ac_mcs_map: str  # Comma separated list of max supported VHT MCS for | MaxLen: 63
    rates_11ax_mcs_map: str  # Comma separated list of max supported HE MCS for s | MaxLen: 63
    rates_11be_mcs_map: str  # Comma separated list of max nss that supports EHT- | MaxLen: 15
    rates_11be_mcs_map_160: str  # Comma separated list of max nss that supports EHT- | MaxLen: 15
    rates_11be_mcs_map_320: str  # Comma separated list of max nss that supports EHT- | MaxLen: 15
    utm_profile: str  # UTM profile name. | MaxLen: 35
    utm_status: Literal["enable", "disable"]  # Enable to add one or more security profiles | Default: disable
    utm_log: Literal["enable", "disable"]  # Enable/disable UTM logging. | Default: enable
    ips_sensor: str  # IPS sensor name. | MaxLen: 47
    application_list: str  # Application control list name. | MaxLen: 47
    antivirus_profile: str  # AntiVirus profile name. | MaxLen: 47
    webfilter_profile: str  # WebFilter profile name. | MaxLen: 47
    scan_botnet_connections: Literal["disable", "monitor", "block"]  # Block or monitor connections to Botnet servers or | Default: monitor
    address_group: str  # Firewall Address Group Name. | MaxLen: 79
    address_group_policy: Literal["disable", "allow", "deny"]  # Configure MAC address filtering policy for MAC add | Default: disable
    sticky_client_remove: Literal["enable", "disable"]  # Enable/disable sticky client remove to maintain go | Default: disable
    sticky_client_threshold_5g: str  # Minimum signal level/threshold in dBm required for | Default: -76 | MaxLen: 7
    sticky_client_threshold_2g: str  # Minimum signal level/threshold in dBm required for | Default: -79 | MaxLen: 7
    sticky_client_threshold_6g: str  # Minimum signal level/threshold in dBm required for | Default: -76 | MaxLen: 7
    bstm_rssi_disassoc_timer: int  # Time interval for client to voluntarily leave AP b | Default: 200 | Min: 1 | Max: 2000
    bstm_load_balancing_disassoc_timer: int  # Time interval for client to voluntarily leave AP b | Default: 10 | Min: 1 | Max: 30
    bstm_disassociation_imminent: Literal["enable", "disable"]  # Enable/disable forcing of disassociation after the | Default: enable
    beacon_advertising: Literal["name", "model", "serial-number"]  # Fortinet beacon advertising IE data
    osen: Literal["enable", "disable"]  # Enable/disable OSEN as part of key management | Default: disable
    application_detection_engine: Literal["enable", "disable"]  # Enable/disable application detection engine | Default: disable
    application_dscp_marking: Literal["enable", "disable"]  # Enable/disable application attribute based DSCP ma | Default: disable
    application_report_intv: int  # Application report interval | Default: 120 | Min: 30 | Max: 864000
    l3_roaming: Literal["enable", "disable"]  # Enable/disable layer 3 roaming (default = disable) | Default: disable
    l3_roaming_mode: Literal["direct", "indirect"]  # Select the way that layer 3 roaming traffic is pas | Default: direct

# Nested TypedDicts for table field children (dict mode)

class VapRadiusmacauthusergroupsItem(TypedDict):
    """Type hints for radius-mac-auth-usergroups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # User group name. | MaxLen: 79


class VapUsergroupItem(TypedDict):
    """Type hints for usergroup table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # User group name. | MaxLen: 79


class VapSelectedusergroupsItem(TypedDict):
    """Type hints for selected-usergroups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # User group name. | MaxLen: 79


class VapScheduleItem(TypedDict):
    """Type hints for schedule table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Schedule name. | MaxLen: 35


class VapVlannameItem(TypedDict):
    """Type hints for vlan-name table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # VLAN name. | MaxLen: 35
    vlan_id: int  # VLAN IDs (maximum 8 VLAN IDs). | Min: 0 | Max: 4094


class VapVlanpoolItem(TypedDict):
    """Type hints for vlan-pool table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4094
    wtp_group: str  # WTP group name. | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class VapRadiusmacauthusergroupsObject:
    """Typed object for radius-mac-auth-usergroups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User group name. | MaxLen: 79
    name: str
    
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


@final
class VapUsergroupObject:
    """Typed object for usergroup table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User group name. | MaxLen: 79
    name: str
    
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


@final
class VapSelectedusergroupsObject:
    """Typed object for selected-usergroups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User group name. | MaxLen: 79
    name: str
    
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


@final
class VapScheduleObject:
    """Typed object for schedule table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Schedule name. | MaxLen: 35
    name: str
    
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


@final
class VapVlannameObject:
    """Typed object for vlan-name table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name. | MaxLen: 35
    name: str
    # VLAN IDs (maximum 8 VLAN IDs). | Min: 0 | Max: 4094
    vlan_id: int
    
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


@final
class VapVlanpoolObject:
    """Typed object for vlan-pool table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4094
    id: int
    # WTP group name. | MaxLen: 35
    wtp_group: str
    
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
class VapResponse(TypedDict):
    """
    Type hints for wireless_controller/vap API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Virtual AP name. | MaxLen: 15
    pre_auth: Literal["enable", "disable"]  # Enable/disable pre-authentication, where supported | Default: enable
    external_pre_auth: Literal["enable", "disable"]  # Enable/disable pre-authentication with external AP | Default: disable
    mesh_backhaul: Literal["enable", "disable"]  # Enable/disable using this VAP as a WiFi mesh backh | Default: disable
    atf_weight: int  # Airtime weight in percentage (default = 20). | Default: 20 | Min: 0 | Max: 100
    max_clients: int  # Maximum number of clients that can connect simulta | Default: 0 | Min: 0 | Max: 4294967295
    max_clients_ap: int  # Maximum number of clients that can connect simulta | Default: 0 | Min: 0 | Max: 4294967295
    ssid: str  # IEEE 802.11 service set identifier (SSID) for the | Default: fortinet | MaxLen: 32
    broadcast_ssid: Literal["enable", "disable"]  # Enable/disable broadcasting the SSID | Default: enable
    security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"]  # Security mode for the wireless interface | Default: wpa2-only-personal
    pmf: Literal["disable", "enable", "optional"]  # Protected Management Frames (PMF) support | Default: disable
    pmf_assoc_comeback_timeout: int  # Protected Management Frames (PMF) comeback maximum | Default: 1 | Min: 1 | Max: 20
    pmf_sa_query_retry_timeout: int  # Protected Management Frames (PMF) SA query retry t | Default: 2 | Min: 1 | Max: 5
    beacon_protection: Literal["disable", "enable"]  # Enable/disable beacon protection support | Default: disable
    okc: Literal["disable", "enable"]  # Enable/disable Opportunistic Key Caching (OKC) | Default: enable
    mbo: Literal["disable", "enable"]  # Enable/disable Multiband Operation | Default: disable
    gas_comeback_delay: int  # GAS comeback delay | Default: 500 | Min: 100 | Max: 10000
    gas_fragmentation_limit: int  # GAS fragmentation limit | Default: 1024 | Min: 512 | Max: 4096
    mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"]  # MBO cell data connection preference | Default: prefer-not
    x80211k: Literal["disable", "enable"]  # Enable/disable 802.11k assisted roaming | Default: enable
    x80211v: Literal["disable", "enable"]  # Enable/disable 802.11v assisted roaming | Default: enable
    neighbor_report_dual_band: Literal["disable", "enable"]  # Enable/disable dual-band neighbor report | Default: disable
    fast_bss_transition: Literal["disable", "enable"]  # Enable/disable 802.11r Fast BSS Transition (FT) | Default: disable
    ft_mobility_domain: int  # Mobility domain identifier in FT | Default: 1000 | Min: 1 | Max: 65535
    ft_r0_key_lifetime: int  # Lifetime of the PMK-R0 key in FT, 1-65535 minutes. | Default: 480 | Min: 1 | Max: 65535
    ft_over_ds: Literal["disable", "enable"]  # Enable/disable FT over the Distribution System | Default: disable
    sae_groups: Literal["19", "20", "21"]  # SAE-Groups.
    owe_groups: Literal["19", "20", "21"]  # OWE-Groups.
    owe_transition: Literal["disable", "enable"]  # Enable/disable OWE transition mode support. | Default: disable
    owe_transition_ssid: str  # OWE transition mode peer SSID. | MaxLen: 32
    additional_akms: Literal["akm6", "akm24"]  # Additional AKMs.
    eapol_key_retries: Literal["disable", "enable"]  # Enable/disable retransmission of EAPOL-Key frames | Default: enable
    tkip_counter_measure: Literal["enable", "disable"]  # Enable/disable TKIP counter measure. | Default: enable
    external_web: str  # URL of external authentication web server. | MaxLen: 1023
    external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"]  # URL query parameter detection | Default: auto-detect
    external_logout: str  # URL of external authentication logout server. | MaxLen: 127
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication username delimiter | Default: hyphen
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC authentication password delimiter | Default: hyphen
    mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC calling station delimiter (default = hyphen). | Default: hyphen
    mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]  # MAC called station delimiter (default = hyphen). | Default: hyphen
    mac_case: Literal["uppercase", "lowercase"]  # MAC case (default = uppercase). | Default: uppercase
    called_station_id_type: Literal["mac", "ip", "apname"]  # The format type of RADIUS attribute Called-Station | Default: mac
    mac_auth_bypass: Literal["enable", "disable"]  # Enable/disable MAC authentication bypass. | Default: disable
    radius_mac_auth: Literal["enable", "disable"]  # Enable/disable RADIUS-based MAC authentication of | Default: disable
    radius_mac_auth_server: str  # RADIUS-based MAC authentication server. | MaxLen: 35
    radius_mac_auth_block_interval: int  # Don't send RADIUS MAC auth request again if the cl | Default: 0 | Min: 30 | Max: 864000
    radius_mac_mpsk_auth: Literal["enable", "disable"]  # Enable/disable RADIUS-based MAC authentication of | Default: disable
    radius_mac_mpsk_timeout: int  # RADIUS MAC MPSK cache timeout interval | Default: 86400 | Min: 300 | Max: 864000
    radius_mac_auth_usergroups: list[VapRadiusmacauthusergroupsItem]  # Selective user groups that are permitted for RADIU
    auth: Literal["radius", "usergroup"]  # Authentication protocol.
    encrypt: Literal["TKIP", "AES", "TKIP-AES"]  # Encryption protocol to use | Default: AES
    keyindex: int  # WEP key index (1 - 4). | Default: 1 | Min: 1 | Max: 4
    key: str  # WEP Key. | MaxLen: 128
    passphrase: str  # WPA pre-shared key (PSK) to be used to authenticat | MaxLen: 128
    sae_password: str  # WPA3 SAE password to be used to authenticate WiFi | MaxLen: 128
    sae_h2e_only: Literal["enable", "disable"]  # Use hash-to-element-only mechanism for PWE derivat | Default: disable
    sae_hnp_only: Literal["enable", "disable"]  # Use hunting-and-pecking-only mechanism for PWE der | Default: disable
    sae_pk: Literal["enable", "disable"]  # Enable/disable WPA3 SAE-PK (default = disable). | Default: disable
    sae_private_key: str  # Private key used for WPA3 SAE-PK authentication. | MaxLen: 359
    akm24_only: Literal["disable", "enable"]  # WPA3 SAE using group-dependent hash only | Default: disable
    radius_server: str  # RADIUS server to be used to authenticate WiFi user | MaxLen: 35
    nas_filter_rule: Literal["enable", "disable"]  # Enable/disable NAS filter rule support | Default: disable
    domain_name_stripping: Literal["disable", "enable"]  # Enable/disable stripping domain name from identity | Default: disable
    mlo: Literal["disable", "enable"]  # Enable/disable WiFi7 Multi-Link-Operation | Default: disable
    local_standalone: Literal["enable", "disable"]  # Enable/disable AP local standalone | Default: disable
    local_standalone_nat: Literal["enable", "disable"]  # Enable/disable AP local standalone NAT mode. | Default: disable
    ip: str  # IP address and subnet mask for the local standalon | Default: 0.0.0.0 0.0.0.0
    dhcp_lease_time: int  # DHCP lease time in seconds for NAT IP address. | Default: 2400 | Min: 300 | Max: 8640000
    local_standalone_dns: Literal["enable", "disable"]  # Enable/disable AP local standalone DNS. | Default: disable
    local_standalone_dns_ip: list[dict[str, Any]]  # IPv4 addresses for the local standalone DNS.
    local_lan_partition: Literal["enable", "disable"]  # Enable/disable segregating client traffic to local | Default: disable
    local_bridging: Literal["enable", "disable"]  # Enable/disable bridging of wireless and Ethernet i | Default: disable
    local_lan: Literal["allow", "deny"]  # Allow/deny traffic destined for a Class A, B, or C | Default: allow
    local_authentication: Literal["enable", "disable"]  # Enable/disable AP local authentication. | Default: disable
    usergroup: list[VapUsergroupItem]  # Firewall user group to be used to authenticate WiF
    captive_portal: Literal["enable", "disable"]  # Enable/disable captive portal. | Default: disable
    captive_network_assistant_bypass: Literal["enable", "disable"]  # Enable/disable Captive Network Assistant bypass. | Default: disable
    portal_message_override_group: str  # Replacement message group for this VAP | MaxLen: 35
    portal_message_overrides: str  # Individual message overrides.
    portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"]  # Captive portal functionality. Configure how the ca | Default: auth
    selected_usergroups: list[VapSelectedusergroupsItem]  # Selective user groups that are permitted to authen
    security_exempt_list: str  # Optional security exempt list for captive portal a | MaxLen: 35
    security_redirect_url: str  # Optional URL for redirecting users after they pass | MaxLen: 1023
    auth_cert: str  # HTTPS server certificate. | MaxLen: 35
    auth_portal_addr: str  # Address of captive portal. | MaxLen: 63
    intra_vap_privacy: Literal["enable", "disable"]  # Enable/disable blocking communication between clie | Default: disable
    schedule: list[VapScheduleItem]  # Firewall schedules for enabling this VAP on the Fo
    ldpc: Literal["disable", "rx", "tx", "rxtx"]  # VAP low-density parity-check (LDPC) coding configu | Default: rxtx
    high_efficiency: Literal["enable", "disable"]  # Enable/disable 802.11ax high efficiency | Default: enable
    target_wake_time: Literal["enable", "disable"]  # Enable/disable 802.11ax target wake time | Default: enable
    port_macauth: Literal["disable", "radius", "address-group"]  # Enable/disable LAN port MAC authentication | Default: disable
    port_macauth_timeout: int  # LAN port MAC authentication idle timeout value | Default: 600 | Min: 60 | Max: 65535
    port_macauth_reauth_timeout: int  # LAN port MAC authentication re-authentication time | Default: 7200 | Min: 120 | Max: 65535
    bss_color_partial: Literal["enable", "disable"]  # Enable/disable 802.11ax partial BSS color | Default: enable
    mpsk_profile: str  # MPSK profile name. | MaxLen: 35
    split_tunneling: Literal["enable", "disable"]  # Enable/disable split tunneling (default = disable) | Default: disable
    nac: Literal["enable", "disable"]  # Enable/disable network access control. | Default: disable
    nac_profile: str  # NAC profile name. | MaxLen: 35
    vlanid: int  # Optional VLAN ID. | Default: 0 | Min: 0 | Max: 4094
    vlan_auto: Literal["enable", "disable"]  # Enable/disable automatic management of SSID VLAN i | Default: disable
    dynamic_vlan: Literal["enable", "disable"]  # Enable/disable dynamic VLAN assignment. | Default: disable
    captive_portal_fw_accounting: Literal["enable", "disable"]  # Enable/disable RADIUS accounting for captive porta | Default: disable
    captive_portal_ac_name: str  # Local-bridging captive portal ac-name. | MaxLen: 35
    captive_portal_auth_timeout: int  # Hard timeout - AP will always clear the session af | Default: 0 | Min: 0 | Max: 864000
    multicast_rate: Literal["0", "6000", "12000", "24000"]  # Multicast rate | Default: 0
    multicast_enhance: Literal["enable", "disable"]  # Enable/disable converting multicast to unicast to | Default: disable
    igmp_snooping: Literal["enable", "disable"]  # Enable/disable IGMP snooping. | Default: disable
    dhcp_address_enforcement: Literal["enable", "disable"]  # Enable/disable DHCP address enforcement | Default: disable
    broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"]  # Optional suppression of broadcast messages. For ex | Default: dhcp-up dhcp-ucast arp-known
    ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"]  # Optional rules of IPv6 packets. For example, you c | Default: drop-icmp6ra drop-icmp6rs drop-llmnr6 drop-icmp6mld2 drop-dhcp6s drop-dhcp6c ndp-proxy drop-ns-dad
    me_disable_thresh: int  # Disable multicast enhancement when this many clien | Default: 32 | Min: 2 | Max: 256
    mu_mimo: Literal["enable", "disable"]  # Enable/disable Multi-user MIMO (default = enable). | Default: enable
    probe_resp_suppression: Literal["enable", "disable"]  # Enable/disable probe response suppression | Default: disable
    probe_resp_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -80 | MaxLen: 7
    radio_sensitivity: Literal["enable", "disable"]  # Enable/disable software radio sensitivity | Default: disable
    quarantine: Literal["enable", "disable"]  # Enable/disable station quarantine | Default: disable
    radio_5g_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -76 | MaxLen: 7
    radio_2g_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -79 | MaxLen: 7
    vlan_name: list[VapVlannameItem]  # Table for mapping VLAN name to VLAN ID.
    vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"]  # Enable/disable VLAN pooling, to allow grouping of | Default: disable
    vlan_pool: list[VapVlanpoolItem]  # VLAN pool.
    dhcp_option43_insertion: Literal["enable", "disable"]  # Enable/disable insertion of DHCP option 43 | Default: enable
    dhcp_option82_insertion: Literal["enable", "disable"]  # Enable/disable DHCP option 82 insert | Default: disable
    dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"]  # Enable/disable DHCP option 82 circuit-id insert | Default: disable
    dhcp_option82_remote_id_insertion: Literal["style-1", "disable"]  # Enable/disable DHCP option 82 remote-id insert | Default: disable
    ptk_rekey: Literal["enable", "disable"]  # Enable/disable PTK rekey for WPA-Enterprise securi | Default: disable
    ptk_rekey_intv: int  # PTK rekey interval | Default: 86400 | Min: 600 | Max: 864000
    gtk_rekey: Literal["enable", "disable"]  # Enable/disable GTK rekey for WPA security. | Default: disable
    gtk_rekey_intv: int  # GTK rekey interval | Default: 86400 | Min: 600 | Max: 864000
    eap_reauth: Literal["enable", "disable"]  # Enable/disable EAP re-authentication for WPA-Enter | Default: disable
    eap_reauth_intv: int  # EAP re-authentication interval | Default: 86400 | Min: 1800 | Max: 864000
    roaming_acct_interim_update: Literal["enable", "disable"]  # Enable/disable using accounting interim update ins | Default: disable
    qos_profile: str  # Quality of service profile name. | MaxLen: 35
    hotspot20_profile: str  # Hotspot 2.0 profile name. | MaxLen: 35
    access_control_list: str  # Profile name for access-control-list. | MaxLen: 35
    primary_wag_profile: str  # Primary wireless access gateway profile name. | MaxLen: 35
    secondary_wag_profile: str  # Secondary wireless access gateway profile name. | MaxLen: 35
    tunnel_echo_interval: int  # The time interval to send echo to both primary and | Default: 300 | Min: 1 | Max: 65535
    tunnel_fallback_interval: int  # The time interval for secondary tunnel to fall bac | Default: 7200 | Min: 0 | Max: 65535
    rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]  # Allowed data rates for 802.11a.
    rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]  # Allowed data rates for 802.11b/g.
    rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"]  # Allowed data rates for 802.11n with 1 or 2 spatial
    rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"]  # Allowed data rates for 802.11n with 3 or 4 spatial
    rates_11ac_mcs_map: str  # Comma separated list of max supported VHT MCS for | MaxLen: 63
    rates_11ax_mcs_map: str  # Comma separated list of max supported HE MCS for s | MaxLen: 63
    rates_11be_mcs_map: str  # Comma separated list of max nss that supports EHT- | MaxLen: 15
    rates_11be_mcs_map_160: str  # Comma separated list of max nss that supports EHT- | MaxLen: 15
    rates_11be_mcs_map_320: str  # Comma separated list of max nss that supports EHT- | MaxLen: 15
    utm_profile: str  # UTM profile name. | MaxLen: 35
    utm_status: Literal["enable", "disable"]  # Enable to add one or more security profiles | Default: disable
    utm_log: Literal["enable", "disable"]  # Enable/disable UTM logging. | Default: enable
    ips_sensor: str  # IPS sensor name. | MaxLen: 47
    application_list: str  # Application control list name. | MaxLen: 47
    antivirus_profile: str  # AntiVirus profile name. | MaxLen: 47
    webfilter_profile: str  # WebFilter profile name. | MaxLen: 47
    scan_botnet_connections: Literal["disable", "monitor", "block"]  # Block or monitor connections to Botnet servers or | Default: monitor
    address_group: str  # Firewall Address Group Name. | MaxLen: 79
    address_group_policy: Literal["disable", "allow", "deny"]  # Configure MAC address filtering policy for MAC add | Default: disable
    sticky_client_remove: Literal["enable", "disable"]  # Enable/disable sticky client remove to maintain go | Default: disable
    sticky_client_threshold_5g: str  # Minimum signal level/threshold in dBm required for | Default: -76 | MaxLen: 7
    sticky_client_threshold_2g: str  # Minimum signal level/threshold in dBm required for | Default: -79 | MaxLen: 7
    sticky_client_threshold_6g: str  # Minimum signal level/threshold in dBm required for | Default: -76 | MaxLen: 7
    bstm_rssi_disassoc_timer: int  # Time interval for client to voluntarily leave AP b | Default: 200 | Min: 1 | Max: 2000
    bstm_load_balancing_disassoc_timer: int  # Time interval for client to voluntarily leave AP b | Default: 10 | Min: 1 | Max: 30
    bstm_disassociation_imminent: Literal["enable", "disable"]  # Enable/disable forcing of disassociation after the | Default: enable
    beacon_advertising: Literal["name", "model", "serial-number"]  # Fortinet beacon advertising IE data
    osen: Literal["enable", "disable"]  # Enable/disable OSEN as part of key management | Default: disable
    application_detection_engine: Literal["enable", "disable"]  # Enable/disable application detection engine | Default: disable
    application_dscp_marking: Literal["enable", "disable"]  # Enable/disable application attribute based DSCP ma | Default: disable
    application_report_intv: int  # Application report interval | Default: 120 | Min: 30 | Max: 864000
    l3_roaming: Literal["enable", "disable"]  # Enable/disable layer 3 roaming (default = disable) | Default: disable
    l3_roaming_mode: Literal["direct", "indirect"]  # Select the way that layer 3 roaming traffic is pas | Default: direct


@final
class VapObject:
    """Typed FortiObject for wireless_controller/vap with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Virtual AP name. | MaxLen: 15
    name: str
    # Enable/disable pre-authentication, where supported by client | Default: enable
    pre_auth: Literal["enable", "disable"]
    # Enable/disable pre-authentication with external APs not mana | Default: disable
    external_pre_auth: Literal["enable", "disable"]
    # Enable/disable using this VAP as a WiFi mesh backhaul | Default: disable
    mesh_backhaul: Literal["enable", "disable"]
    # Airtime weight in percentage (default = 20). | Default: 20 | Min: 0 | Max: 100
    atf_weight: int
    # Maximum number of clients that can connect simultaneously to | Default: 0 | Min: 0 | Max: 4294967295
    max_clients: int
    # Maximum number of clients that can connect simultaneously to | Default: 0 | Min: 0 | Max: 4294967295
    max_clients_ap: int
    # IEEE 802.11 service set identifier (SSID) for the wireless i | Default: fortinet | MaxLen: 32
    ssid: str
    # Enable/disable broadcasting the SSID (default = enable). | Default: enable
    broadcast_ssid: Literal["enable", "disable"]
    # Security mode for the wireless interface | Default: wpa2-only-personal
    security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"]
    # Protected Management Frames (PMF) support | Default: disable
    pmf: Literal["disable", "enable", "optional"]
    # Protected Management Frames (PMF) comeback maximum timeout | Default: 1 | Min: 1 | Max: 20
    pmf_assoc_comeback_timeout: int
    # Protected Management Frames (PMF) SA query retry timeout int | Default: 2 | Min: 1 | Max: 5
    pmf_sa_query_retry_timeout: int
    # Enable/disable beacon protection support (default = disable) | Default: disable
    beacon_protection: Literal["disable", "enable"]
    # Enable/disable Opportunistic Key Caching (OKC) | Default: enable
    okc: Literal["disable", "enable"]
    # Enable/disable Multiband Operation (default = disable). | Default: disable
    mbo: Literal["disable", "enable"]
    # GAS comeback delay | Default: 500 | Min: 100 | Max: 10000
    gas_comeback_delay: int
    # GAS fragmentation limit (512 - 4096, default = 1024). | Default: 1024 | Min: 512 | Max: 4096
    gas_fragmentation_limit: int
    # MBO cell data connection preference | Default: prefer-not
    mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"]
    # Enable/disable 802.11k assisted roaming (default = enable). | Default: enable
    x80211k: Literal["disable", "enable"]
    # Enable/disable 802.11v assisted roaming (default = enable). | Default: enable
    x80211v: Literal["disable", "enable"]
    # Enable/disable dual-band neighbor report (default = disable) | Default: disable
    neighbor_report_dual_band: Literal["disable", "enable"]
    # Enable/disable 802.11r Fast BSS Transition (FT) | Default: disable
    fast_bss_transition: Literal["disable", "enable"]
    # Mobility domain identifier in FT (1 - 65535, default = 1000) | Default: 1000 | Min: 1 | Max: 65535
    ft_mobility_domain: int
    # Lifetime of the PMK-R0 key in FT, 1-65535 minutes. | Default: 480 | Min: 1 | Max: 65535
    ft_r0_key_lifetime: int
    # Enable/disable FT over the Distribution System (DS). | Default: disable
    ft_over_ds: Literal["disable", "enable"]
    # SAE-Groups.
    sae_groups: Literal["19", "20", "21"]
    # OWE-Groups.
    owe_groups: Literal["19", "20", "21"]
    # Enable/disable OWE transition mode support. | Default: disable
    owe_transition: Literal["disable", "enable"]
    # OWE transition mode peer SSID. | MaxLen: 32
    owe_transition_ssid: str
    # Additional AKMs.
    additional_akms: Literal["akm6", "akm24"]
    # Enable/disable retransmission of EAPOL-Key frames | Default: enable
    eapol_key_retries: Literal["disable", "enable"]
    # Enable/disable TKIP counter measure. | Default: enable
    tkip_counter_measure: Literal["enable", "disable"]
    # URL of external authentication web server. | MaxLen: 1023
    external_web: str
    # URL query parameter detection (default = auto-detect). | Default: auto-detect
    external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"]
    # URL of external authentication logout server. | MaxLen: 127
    external_logout: str
    # MAC authentication username delimiter (default = hyphen). | Default: hyphen
    mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC authentication password delimiter (default = hyphen). | Default: hyphen
    mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC calling station delimiter (default = hyphen). | Default: hyphen
    mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC called station delimiter (default = hyphen). | Default: hyphen
    mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"]
    # MAC case (default = uppercase). | Default: uppercase
    mac_case: Literal["uppercase", "lowercase"]
    # The format type of RADIUS attribute Called-Station-Id | Default: mac
    called_station_id_type: Literal["mac", "ip", "apname"]
    # Enable/disable MAC authentication bypass. | Default: disable
    mac_auth_bypass: Literal["enable", "disable"]
    # Enable/disable RADIUS-based MAC authentication of clients | Default: disable
    radius_mac_auth: Literal["enable", "disable"]
    # RADIUS-based MAC authentication server. | MaxLen: 35
    radius_mac_auth_server: str
    # Don't send RADIUS MAC auth request again if the client has b | Default: 0 | Min: 30 | Max: 864000
    radius_mac_auth_block_interval: int
    # Enable/disable RADIUS-based MAC authentication of clients fo | Default: disable
    radius_mac_mpsk_auth: Literal["enable", "disable"]
    # RADIUS MAC MPSK cache timeout interval | Default: 86400 | Min: 300 | Max: 864000
    radius_mac_mpsk_timeout: int
    # Selective user groups that are permitted for RADIUS mac auth
    radius_mac_auth_usergroups: list[VapRadiusmacauthusergroupsObject]
    # Authentication protocol.
    auth: Literal["radius", "usergroup"]
    # Encryption protocol to use | Default: AES
    encrypt: Literal["TKIP", "AES", "TKIP-AES"]
    # WEP key index (1 - 4). | Default: 1 | Min: 1 | Max: 4
    keyindex: int
    # WEP Key. | MaxLen: 128
    key: str
    # WPA pre-shared key (PSK) to be used to authenticate WiFi use | MaxLen: 128
    passphrase: str
    # WPA3 SAE password to be used to authenticate WiFi users. | MaxLen: 128
    sae_password: str
    # Use hash-to-element-only mechanism for PWE derivation | Default: disable
    sae_h2e_only: Literal["enable", "disable"]
    # Use hunting-and-pecking-only mechanism for PWE derivation | Default: disable
    sae_hnp_only: Literal["enable", "disable"]
    # Enable/disable WPA3 SAE-PK (default = disable). | Default: disable
    sae_pk: Literal["enable", "disable"]
    # Private key used for WPA3 SAE-PK authentication. | MaxLen: 359
    sae_private_key: str
    # WPA3 SAE using group-dependent hash only (default = disable) | Default: disable
    akm24_only: Literal["disable", "enable"]
    # RADIUS server to be used to authenticate WiFi users. | MaxLen: 35
    radius_server: str
    # Enable/disable NAS filter rule support (default = disable). | Default: disable
    nas_filter_rule: Literal["enable", "disable"]
    # Enable/disable stripping domain name from identity | Default: disable
    domain_name_stripping: Literal["disable", "enable"]
    # Enable/disable WiFi7 Multi-Link-Operation | Default: disable
    mlo: Literal["disable", "enable"]
    # Enable/disable AP local standalone (default = disable). | Default: disable
    local_standalone: Literal["enable", "disable"]
    # Enable/disable AP local standalone NAT mode. | Default: disable
    local_standalone_nat: Literal["enable", "disable"]
    # IP address and subnet mask for the local standalone NAT subn | Default: 0.0.0.0 0.0.0.0
    ip: str
    # DHCP lease time in seconds for NAT IP address. | Default: 2400 | Min: 300 | Max: 8640000
    dhcp_lease_time: int
    # Enable/disable AP local standalone DNS. | Default: disable
    local_standalone_dns: Literal["enable", "disable"]
    # IPv4 addresses for the local standalone DNS.
    local_standalone_dns_ip: list[dict[str, Any]]
    # Enable/disable segregating client traffic to local LAN side | Default: disable
    local_lan_partition: Literal["enable", "disable"]
    # Enable/disable bridging of wireless and Ethernet interfaces | Default: disable
    local_bridging: Literal["enable", "disable"]
    # Allow/deny traffic destined for a Class A, B, or C private I | Default: allow
    local_lan: Literal["allow", "deny"]
    # Enable/disable AP local authentication. | Default: disable
    local_authentication: Literal["enable", "disable"]
    # Firewall user group to be used to authenticate WiFi users.
    usergroup: list[VapUsergroupObject]
    # Enable/disable captive portal. | Default: disable
    captive_portal: Literal["enable", "disable"]
    # Enable/disable Captive Network Assistant bypass. | Default: disable
    captive_network_assistant_bypass: Literal["enable", "disable"]
    # Replacement message group for this VAP | MaxLen: 35
    portal_message_override_group: str
    # Individual message overrides.
    portal_message_overrides: str
    # Captive portal functionality. Configure how the captive port | Default: auth
    portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"]
    # Selective user groups that are permitted to authenticate.
    selected_usergroups: list[VapSelectedusergroupsObject]
    # Optional security exempt list for captive portal authenticat | MaxLen: 35
    security_exempt_list: str
    # Optional URL for redirecting users after they pass captive p | MaxLen: 1023
    security_redirect_url: str
    # HTTPS server certificate. | MaxLen: 35
    auth_cert: str
    # Address of captive portal. | MaxLen: 63
    auth_portal_addr: str
    # Enable/disable blocking communication between clients on the | Default: disable
    intra_vap_privacy: Literal["enable", "disable"]
    # Firewall schedules for enabling this VAP on the FortiAP. Thi
    schedule: list[VapScheduleObject]
    # VAP low-density parity-check (LDPC) coding configuration. | Default: rxtx
    ldpc: Literal["disable", "rx", "tx", "rxtx"]
    # Enable/disable 802.11ax high efficiency (default = enable). | Default: enable
    high_efficiency: Literal["enable", "disable"]
    # Enable/disable 802.11ax target wake time (default = enable). | Default: enable
    target_wake_time: Literal["enable", "disable"]
    # Enable/disable LAN port MAC authentication | Default: disable
    port_macauth: Literal["disable", "radius", "address-group"]
    # LAN port MAC authentication idle timeout value | Default: 600 | Min: 60 | Max: 65535
    port_macauth_timeout: int
    # LAN port MAC authentication re-authentication timeout value | Default: 7200 | Min: 120 | Max: 65535
    port_macauth_reauth_timeout: int
    # Enable/disable 802.11ax partial BSS color (default = enable) | Default: enable
    bss_color_partial: Literal["enable", "disable"]
    # MPSK profile name. | MaxLen: 35
    mpsk_profile: str
    # Enable/disable split tunneling (default = disable). | Default: disable
    split_tunneling: Literal["enable", "disable"]
    # Enable/disable network access control. | Default: disable
    nac: Literal["enable", "disable"]
    # NAC profile name. | MaxLen: 35
    nac_profile: str
    # Optional VLAN ID. | Default: 0 | Min: 0 | Max: 4094
    vlanid: int
    # Enable/disable automatic management of SSID VLAN interface. | Default: disable
    vlan_auto: Literal["enable", "disable"]
    # Enable/disable dynamic VLAN assignment. | Default: disable
    dynamic_vlan: Literal["enable", "disable"]
    # Enable/disable RADIUS accounting for captive portal firewall | Default: disable
    captive_portal_fw_accounting: Literal["enable", "disable"]
    # Local-bridging captive portal ac-name. | MaxLen: 35
    captive_portal_ac_name: str
    # Hard timeout - AP will always clear the session after timeou | Default: 0 | Min: 0 | Max: 864000
    captive_portal_auth_timeout: int
    # Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0). | Default: 0
    multicast_rate: Literal["0", "6000", "12000", "24000"]
    # Enable/disable converting multicast to unicast to improve pe | Default: disable
    multicast_enhance: Literal["enable", "disable"]
    # Enable/disable IGMP snooping. | Default: disable
    igmp_snooping: Literal["enable", "disable"]
    # Enable/disable DHCP address enforcement (default = disable). | Default: disable
    dhcp_address_enforcement: Literal["enable", "disable"]
    # Optional suppression of broadcast messages. For example, you | Default: dhcp-up dhcp-ucast arp-known
    broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"]
    # Optional rules of IPv6 packets. For example, you can keep RA | Default: drop-icmp6ra drop-icmp6rs drop-llmnr6 drop-icmp6mld2 drop-dhcp6s drop-dhcp6c ndp-proxy drop-ns-dad
    ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"]
    # Disable multicast enhancement when this many clients are rec | Default: 32 | Min: 2 | Max: 256
    me_disable_thresh: int
    # Enable/disable Multi-user MIMO (default = enable). | Default: enable
    mu_mimo: Literal["enable", "disable"]
    # Enable/disable probe response suppression | Default: disable
    probe_resp_suppression: Literal["enable", "disable"]
    # Minimum signal level/threshold in dBm required for the AP re | Default: -80 | MaxLen: 7
    probe_resp_threshold: str
    # Enable/disable software radio sensitivity | Default: disable
    radio_sensitivity: Literal["enable", "disable"]
    # Enable/disable station quarantine (default = disable). | Default: disable
    quarantine: Literal["enable", "disable"]
    # Minimum signal level/threshold in dBm required for the AP re | Default: -76 | MaxLen: 7
    radio_5g_threshold: str
    # Minimum signal level/threshold in dBm required for the AP re | Default: -79 | MaxLen: 7
    radio_2g_threshold: str
    # Table for mapping VLAN name to VLAN ID.
    vlan_name: list[VapVlannameObject]
    # Enable/disable VLAN pooling, to allow grouping of multiple w | Default: disable
    vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"]
    # VLAN pool.
    vlan_pool: list[VapVlanpoolObject]
    # Enable/disable insertion of DHCP option 43 | Default: enable
    dhcp_option43_insertion: Literal["enable", "disable"]
    # Enable/disable DHCP option 82 insert (default = disable). | Default: disable
    dhcp_option82_insertion: Literal["enable", "disable"]
    # Enable/disable DHCP option 82 circuit-id insert | Default: disable
    dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"]
    # Enable/disable DHCP option 82 remote-id insert | Default: disable
    dhcp_option82_remote_id_insertion: Literal["style-1", "disable"]
    # Enable/disable PTK rekey for WPA-Enterprise security. | Default: disable
    ptk_rekey: Literal["enable", "disable"]
    # PTK rekey interval (600 - 864000 sec, default = 86400). | Default: 86400 | Min: 600 | Max: 864000
    ptk_rekey_intv: int
    # Enable/disable GTK rekey for WPA security. | Default: disable
    gtk_rekey: Literal["enable", "disable"]
    # GTK rekey interval (600 - 864000 sec, default = 86400). | Default: 86400 | Min: 600 | Max: 864000
    gtk_rekey_intv: int
    # Enable/disable EAP re-authentication for WPA-Enterprise secu | Default: disable
    eap_reauth: Literal["enable", "disable"]
    # EAP re-authentication interval | Default: 86400 | Min: 1800 | Max: 864000
    eap_reauth_intv: int
    # Enable/disable using accounting interim update instead of ac | Default: disable
    roaming_acct_interim_update: Literal["enable", "disable"]
    # Quality of service profile name. | MaxLen: 35
    qos_profile: str
    # Hotspot 2.0 profile name. | MaxLen: 35
    hotspot20_profile: str
    # Profile name for access-control-list. | MaxLen: 35
    access_control_list: str
    # Primary wireless access gateway profile name. | MaxLen: 35
    primary_wag_profile: str
    # Secondary wireless access gateway profile name. | MaxLen: 35
    secondary_wag_profile: str
    # The time interval to send echo to both primary and secondary | Default: 300 | Min: 1 | Max: 65535
    tunnel_echo_interval: int
    # The time interval for secondary tunnel to fall back to prima | Default: 7200 | Min: 0 | Max: 65535
    tunnel_fallback_interval: int
    # Allowed data rates for 802.11a.
    rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]
    # Allowed data rates for 802.11b/g.
    rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"]
    # Allowed data rates for 802.11n with 1 or 2 spatial streams.
    rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"]
    # Allowed data rates for 802.11n with 3 or 4 spatial streams.
    rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"]
    # Comma separated list of max supported VHT MCS for spatial st | MaxLen: 63
    rates_11ac_mcs_map: str
    # Comma separated list of max supported HE MCS for spatial str | MaxLen: 63
    rates_11ax_mcs_map: str
    # Comma separated list of max nss that supports EHT-MCS 0-9, 1 | MaxLen: 15
    rates_11be_mcs_map: str
    # Comma separated list of max nss that supports EHT-MCS 0-9, 1 | MaxLen: 15
    rates_11be_mcs_map_160: str
    # Comma separated list of max nss that supports EHT-MCS 0-9, 1 | MaxLen: 15
    rates_11be_mcs_map_320: str
    # UTM profile name. | MaxLen: 35
    utm_profile: str
    # Enable to add one or more security profiles (AV, IPS, etc.) | Default: disable
    utm_status: Literal["enable", "disable"]
    # Enable/disable UTM logging. | Default: enable
    utm_log: Literal["enable", "disable"]
    # IPS sensor name. | MaxLen: 47
    ips_sensor: str
    # Application control list name. | MaxLen: 47
    application_list: str
    # AntiVirus profile name. | MaxLen: 47
    antivirus_profile: str
    # WebFilter profile name. | MaxLen: 47
    webfilter_profile: str
    # Block or monitor connections to Botnet servers or disable Bo | Default: monitor
    scan_botnet_connections: Literal["disable", "monitor", "block"]
    # Firewall Address Group Name. | MaxLen: 79
    address_group: str
    # Configure MAC address filtering policy for MAC addresses tha | Default: disable
    address_group_policy: Literal["disable", "allow", "deny"]
    # Enable/disable sticky client remove to maintain good signal | Default: disable
    sticky_client_remove: Literal["enable", "disable"]
    # Minimum signal level/threshold in dBm required for the 5G cl | Default: -76 | MaxLen: 7
    sticky_client_threshold_5g: str
    # Minimum signal level/threshold in dBm required for the 2G cl | Default: -79 | MaxLen: 7
    sticky_client_threshold_2g: str
    # Minimum signal level/threshold in dBm required for the 6G cl | Default: -76 | MaxLen: 7
    sticky_client_threshold_6g: str
    # Time interval for client to voluntarily leave AP before forc | Default: 200 | Min: 1 | Max: 2000
    bstm_rssi_disassoc_timer: int
    # Time interval for client to voluntarily leave AP before forc | Default: 10 | Min: 1 | Max: 30
    bstm_load_balancing_disassoc_timer: int
    # Enable/disable forcing of disassociation after the BSTM requ | Default: enable
    bstm_disassociation_imminent: Literal["enable", "disable"]
    # Fortinet beacon advertising IE data   (default = empty).
    beacon_advertising: Literal["name", "model", "serial-number"]
    # Enable/disable OSEN as part of key management | Default: disable
    osen: Literal["enable", "disable"]
    # Enable/disable application detection engine | Default: disable
    application_detection_engine: Literal["enable", "disable"]
    # Enable/disable application attribute based DSCP marking | Default: disable
    application_dscp_marking: Literal["enable", "disable"]
    # Application report interval (30 - 864000 sec, default = 120) | Default: 120 | Min: 30 | Max: 864000
    application_report_intv: int
    # Enable/disable layer 3 roaming (default = disable). | Default: disable
    l3_roaming: Literal["enable", "disable"]
    # Select the way that layer 3 roaming traffic is passed | Default: direct
    l3_roaming_mode: Literal["direct", "indirect"]
    
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
    def to_dict(self) -> VapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Vap:
    """
    Configure Virtual Access Points (VAPs).
    
    Path: wireless_controller/vap
    Category: cmdb
    Primary Key: name
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
    ) -> VapObject: ...
    
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
    ) -> VapObject: ...
    
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
    ) -> FortiObjectList[VapObject]: ...
    
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
    ) -> VapObject: ...
    
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
    ) -> VapObject: ...
    
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
    ) -> FortiObjectList[VapObject]: ...
    
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
    ) -> VapObject: ...
    
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
    ) -> VapObject: ...
    
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
    ) -> FortiObjectList[VapObject]: ...
    
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
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
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
    ) -> VapObject | list[VapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> VapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> VapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> VapObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: VapPayload | None = ...,
        name: str | None = ...,
        pre_auth: Literal["enable", "disable"] | None = ...,
        external_pre_auth: Literal["enable", "disable"] | None = ...,
        mesh_backhaul: Literal["enable", "disable"] | None = ...,
        atf_weight: int | None = ...,
        max_clients: int | None = ...,
        max_clients_ap: int | None = ...,
        ssid: str | None = ...,
        broadcast_ssid: Literal["enable", "disable"] | None = ...,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = ...,
        pmf: Literal["disable", "enable", "optional"] | None = ...,
        pmf_assoc_comeback_timeout: int | None = ...,
        pmf_sa_query_retry_timeout: int | None = ...,
        beacon_protection: Literal["disable", "enable"] | None = ...,
        okc: Literal["disable", "enable"] | None = ...,
        mbo: Literal["disable", "enable"] | None = ...,
        gas_comeback_delay: int | None = ...,
        gas_fragmentation_limit: int | None = ...,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = ...,
        x80211k: Literal["disable", "enable"] | None = ...,
        x80211v: Literal["disable", "enable"] | None = ...,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = ...,
        fast_bss_transition: Literal["disable", "enable"] | None = ...,
        ft_mobility_domain: int | None = ...,
        ft_r0_key_lifetime: int | None = ...,
        ft_over_ds: Literal["disable", "enable"] | None = ...,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = ...,
        owe_transition: Literal["disable", "enable"] | None = ...,
        owe_transition_ssid: str | None = ...,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = ...,
        eapol_key_retries: Literal["disable", "enable"] | None = ...,
        tkip_counter_measure: Literal["enable", "disable"] | None = ...,
        external_web: str | None = ...,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = ...,
        external_logout: str | None = ...,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = ...,
        mac_case: Literal["uppercase", "lowercase"] | None = ...,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = ...,
        mac_auth_bypass: Literal["enable", "disable"] | None = ...,
        radius_mac_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_auth_server: str | None = ...,
        radius_mac_auth_block_interval: int | None = ...,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = ...,
        radius_mac_mpsk_timeout: int | None = ...,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: Literal["radius", "usergroup"] | None = ...,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = ...,
        keyindex: int | None = ...,
        key: str | None = ...,
        passphrase: str | None = ...,
        sae_password: str | None = ...,
        sae_h2e_only: Literal["enable", "disable"] | None = ...,
        sae_hnp_only: Literal["enable", "disable"] | None = ...,
        sae_pk: Literal["enable", "disable"] | None = ...,
        sae_private_key: str | None = ...,
        akm24_only: Literal["disable", "enable"] | None = ...,
        radius_server: str | None = ...,
        nas_filter_rule: Literal["enable", "disable"] | None = ...,
        domain_name_stripping: Literal["disable", "enable"] | None = ...,
        mlo: Literal["disable", "enable"] | None = ...,
        local_standalone: Literal["enable", "disable"] | None = ...,
        local_standalone_nat: Literal["enable", "disable"] | None = ...,
        ip: str | None = ...,
        dhcp_lease_time: int | None = ...,
        local_standalone_dns: Literal["enable", "disable"] | None = ...,
        local_standalone_dns_ip: str | list[str] | None = ...,
        local_lan_partition: Literal["enable", "disable"] | None = ...,
        local_bridging: Literal["enable", "disable"] | None = ...,
        local_lan: Literal["allow", "deny"] | None = ...,
        local_authentication: Literal["enable", "disable"] | None = ...,
        usergroup: str | list[str] | list[dict[str, Any]] | None = ...,
        captive_portal: Literal["enable", "disable"] | None = ...,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = ...,
        portal_message_override_group: str | None = ...,
        portal_message_overrides: str | None = ...,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = ...,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = ...,
        security_exempt_list: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        intra_vap_privacy: Literal["enable", "disable"] | None = ...,
        schedule: str | list[str] | list[dict[str, Any]] | None = ...,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = ...,
        high_efficiency: Literal["enable", "disable"] | None = ...,
        target_wake_time: Literal["enable", "disable"] | None = ...,
        port_macauth: Literal["disable", "radius", "address-group"] | None = ...,
        port_macauth_timeout: int | None = ...,
        port_macauth_reauth_timeout: int | None = ...,
        bss_color_partial: Literal["enable", "disable"] | None = ...,
        mpsk_profile: str | None = ...,
        split_tunneling: Literal["enable", "disable"] | None = ...,
        nac: Literal["enable", "disable"] | None = ...,
        nac_profile: str | None = ...,
        vlanid: int | None = ...,
        vlan_auto: Literal["enable", "disable"] | None = ...,
        dynamic_vlan: Literal["enable", "disable"] | None = ...,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = ...,
        captive_portal_ac_name: str | None = ...,
        captive_portal_auth_timeout: int | None = ...,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = ...,
        multicast_enhance: Literal["enable", "disable"] | None = ...,
        igmp_snooping: Literal["enable", "disable"] | None = ...,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = ...,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = ...,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = ...,
        me_disable_thresh: int | None = ...,
        mu_mimo: Literal["enable", "disable"] | None = ...,
        probe_resp_suppression: Literal["enable", "disable"] | None = ...,
        probe_resp_threshold: str | None = ...,
        radio_sensitivity: Literal["enable", "disable"] | None = ...,
        quarantine: Literal["enable", "disable"] | None = ...,
        radio_5g_threshold: str | None = ...,
        radio_2g_threshold: str | None = ...,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = ...,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = ...,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = ...,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = ...,
        ptk_rekey: Literal["enable", "disable"] | None = ...,
        ptk_rekey_intv: int | None = ...,
        gtk_rekey: Literal["enable", "disable"] | None = ...,
        gtk_rekey_intv: int | None = ...,
        eap_reauth: Literal["enable", "disable"] | None = ...,
        eap_reauth_intv: int | None = ...,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = ...,
        qos_profile: str | None = ...,
        hotspot20_profile: str | None = ...,
        access_control_list: str | None = ...,
        primary_wag_profile: str | None = ...,
        secondary_wag_profile: str | None = ...,
        tunnel_echo_interval: int | None = ...,
        tunnel_fallback_interval: int | None = ...,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = ...,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = ...,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = ...,
        rates_11ac_mcs_map: str | None = ...,
        rates_11ax_mcs_map: str | None = ...,
        rates_11be_mcs_map: str | None = ...,
        rates_11be_mcs_map_160: str | None = ...,
        rates_11be_mcs_map_320: str | None = ...,
        utm_profile: str | None = ...,
        utm_status: Literal["enable", "disable"] | None = ...,
        utm_log: Literal["enable", "disable"] | None = ...,
        ips_sensor: str | None = ...,
        application_list: str | None = ...,
        antivirus_profile: str | None = ...,
        webfilter_profile: str | None = ...,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = ...,
        address_group: str | None = ...,
        address_group_policy: Literal["disable", "allow", "deny"] | None = ...,
        sticky_client_remove: Literal["enable", "disable"] | None = ...,
        sticky_client_threshold_5g: str | None = ...,
        sticky_client_threshold_2g: str | None = ...,
        sticky_client_threshold_6g: str | None = ...,
        bstm_rssi_disassoc_timer: int | None = ...,
        bstm_load_balancing_disassoc_timer: int | None = ...,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = ...,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = ...,
        osen: Literal["enable", "disable"] | None = ...,
        application_detection_engine: Literal["enable", "disable"] | None = ...,
        application_dscp_marking: Literal["enable", "disable"] | None = ...,
        application_report_intv: int | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        l3_roaming_mode: Literal["direct", "indirect"] | None = ...,
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
    "Vap",
    "VapPayload",
    "VapResponse",
    "VapObject",
]
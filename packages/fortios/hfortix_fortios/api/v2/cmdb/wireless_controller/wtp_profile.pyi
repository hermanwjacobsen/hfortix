from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WtpProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wtp_profile payload fields.
    
    Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.tacacs+.TacacsPlusEndpoint` (via: admin-auth-tacacs+)
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: apcfg-auto-cert-est-https-ca, apcfg-auto-cert-scep-https-ca)
        - :class:`~.wireless-controller.apcfg-profile.ApcfgProfileEndpoint` (via: apcfg-profile)
        - :class:`~.wireless-controller.ble-profile.BleProfileEndpoint` (via: ble-profile)
        - :class:`~.wireless-controller.bonjour-profile.BonjourProfileEndpoint` (via: bonjour-profile)
        - :class:`~.wireless-controller.lw-profile.LwProfileEndpoint` (via: lw-profile)
        - :class:`~.wireless-controller.syslog-profile.SyslogProfileEndpoint` (via: syslog-profile)
        - :class:`~.wireless-controller.vap.VapEndpoint` (via: apcfg-mesh-ssid)

    **Usage:**
        payload: WtpProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # WTP (or FortiAP or AP) profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    platform: str  # WTP, FortiAP, or AP platform.
    control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]  # Enable/disable CAPWAP control message data channel | Default: ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis
    bonjour_profile: str  # Bonjour profile name. | MaxLen: 35
    apcfg_profile: str  # AP local configuration profile name. | MaxLen: 35
    apcfg_mesh: Literal["enable", "disable"]  # Enable/disable AP local mesh configuration | Default: disable
    apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"]  # Mesh AP Type (default = ethernet). | Default: ethernet
    apcfg_mesh_ssid: str  #  Mesh SSID (default = none). | MaxLen: 15
    apcfg_mesh_eth_bridge: Literal["enable", "disable"]  # Enable/disable mesh ethernet bridge | Default: disable
    ble_profile: str  # Bluetooth Low Energy profile name. | MaxLen: 35
    lw_profile: str  # LoRaWAN profile name. | MaxLen: 35
    syslog_profile: str  # System log server configuration profile name. | MaxLen: 35
    wan_port_mode: Literal["wan-lan", "wan-only"]  # Enable/disable using a WAN port as a LAN port. | Default: wan-only
    lan: str  # WTP LAN port mapping.
    energy_efficient_ethernet: Literal["enable", "disable"]  # Enable/disable use of energy efficient Ethernet on | Default: disable
    led_state: Literal["enable", "disable"]  # Enable/disable use of LEDs on WTP | Default: enable
    led_schedules: list[dict[str, Any]]  # Recurring firewall schedules for illuminating LEDs
    dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"]  # WTP data channel DTLS policy | Default: clear-text
    dtls_in_kernel: Literal["enable", "disable"]  # Enable/disable data channel DTLS in kernel. | Default: disable
    max_clients: int  # Maximum number of stations (STAs) supported by the | Default: 0 | Min: 0 | Max: 4294967295
    handoff_rssi: int  # Minimum received signal strength indicator (RSSI) | Default: 25 | Min: 20 | Max: 30
    handoff_sta_thresh: int  # Threshold value for AP handoff. | Default: 0 | Min: 5 | Max: 60
    handoff_roaming: Literal["enable", "disable"]  # Enable/disable client load balancing during roamin | Default: enable
    deny_mac_list: list[dict[str, Any]]  # List of MAC addresses that are denied access to th
    ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]  # Country in which this WTP, FortiAP, or AP will ope | Default: --
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]  # Method(s) by which IP fragmentation is prevented f | Default: tcp-mss-adjust
    tun_mtu_uplink: int  # The maximum transmission unit (MTU) of uplink CAPW | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_downlink: int  # The MTU of downlink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    split_tunneling_acl_path: Literal["tunnel", "local"]  # Split tunneling ACL path is local/tunnel. | Default: local
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]  # Enable/disable automatically adding local subnetwo | Default: disable
    split_tunneling_acl: list[dict[str, Any]]  # Split tunneling ACL filter list.
    allowaccess: Literal["https", "ssh", "snmp"]  # Control management access to the managed WTP, Fort
    login_passwd_change: Literal["yes", "default", "no"]  # Change or reset the administrator password of a ma | Default: no
    login_passwd: str  # Set the managed WTP, FortiAP, or AP's administrato | MaxLen: 128
    lldp: Literal["enable", "disable"]  # Enable/disable Link Layer Discovery Protocol | Default: enable
    poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]  # Set the WTP, FortiAP, or AP's PoE mode. | Default: auto
    usb_port: Literal["enable", "disable"]  # Enable/disable USB port of the WTP | Default: enable
    frequency_handoff: Literal["enable", "disable"]  # Enable/disable frequency handoff of clients to oth | Default: disable
    ap_handoff: Literal["enable", "disable"]  # Enable/disable AP handoff of clients to other APs | Default: disable
    default_mesh_root: Literal["enable", "disable"]  # Configure default mesh root SSID when it is not in | Default: disable
    radio_1: str  # Configuration options for radio 1.
    radio_2: str  # Configuration options for radio 2.
    radio_3: str  # Configuration options for radio 3.
    radio_4: str  # Configuration options for radio 4.
    lbs: str  # Set various location based service (LBS) options.
    ext_info_enable: Literal["enable", "disable"]  # Enable/disable station/VAP/radio extension informa | Default: enable
    indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"]  # Set to allow indoor/outdoor-only channels under re | Default: platform-determined
    esl_ses_dongle: str  # ESL SES-imagotag dongle configuration.
    console_login: Literal["enable", "disable"]  # Enable/disable FortiAP console login access | Default: enable
    wan_port_auth: Literal["none", "802.1x"]  # Set WAN port authentication mode (default = none). | Default: none
    wan_port_auth_usrname: str  # Set WAN port 802.1x supplicant user name. | MaxLen: 63
    wan_port_auth_password: str  # Set WAN port 802.1x supplicant password. | MaxLen: 128
    wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]  # WAN port 802.1x supplicant EAP methods | Default: all
    wan_port_auth_macsec: Literal["enable", "disable"]  # Enable/disable WAN port 802.1x supplicant MACsec p | Default: disable
    apcfg_auto_cert: Literal["enable", "disable"]  # Enable/disable AP local auto cert configuration | Default: disable
    apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"]  # Certificate enrollment protocol (default = none) | Default: none
    apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]  # Cryptography algorithm: rsa-1024, rsa-1536, rsa-20 | Default: ec-secp256r1
    apcfg_auto_cert_est_server: str  # Address and port for EST server | MaxLen: 255
    apcfg_auto_cert_est_ca_id: str  # CA identifier of the CA server for signing via EST | MaxLen: 255
    apcfg_auto_cert_est_http_username: str  # HTTP Authentication username for signing via EST. | MaxLen: 63
    apcfg_auto_cert_est_http_password: str  # HTTP Authentication password for signing via EST. | MaxLen: 128
    apcfg_auto_cert_est_subject: str  # Subject e.g. "CN=User,DC=example,DC=COM" | Default: CN=FortiAP,DC=local,DC=COM | MaxLen: 127
    apcfg_auto_cert_est_subject_alt_name: str  # Subject alternative name | MaxLen: 127
    apcfg_auto_cert_auto_regen_days: int  # Number of days to wait before expiry of an updated | Default: 30 | Min: 0 | Max: 4294967295
    apcfg_auto_cert_est_https_ca: str  # PEM format https CA Certificate. | MaxLen: 79
    apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"]  # Key type (default = rsa) | Default: rsa
    apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"]  # Key size: 1024, 1536, 2048, 4096 (default 2048). | Default: 2048
    apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"]  # Elliptic curve name: secp256r1, secp384r1 and secp | Default: secp256r1
    apcfg_auto_cert_scep_sub_fully_dn: str  # Full DN of the subject | MaxLen: 255
    apcfg_auto_cert_scep_url: str  # SCEP server URL. | MaxLen: 255
    apcfg_auto_cert_scep_password: str  # SCEP server challenge password for auto-regenerati | MaxLen: 128
    apcfg_auto_cert_scep_ca_id: str  # CA identifier of the CA server for signing via SCE | MaxLen: 255
    apcfg_auto_cert_scep_subject_alt_name: str  # Subject alternative name | MaxLen: 127
    apcfg_auto_cert_scep_https_ca: str  # PEM format https CA Certificate. | MaxLen: 79
    unii_4_5ghz_band: Literal["enable", "disable"]  # Enable/disable UNII-4 5Ghz band channels | Default: disable
    admin_auth_tacacs_plus: str  # Remote authentication server for admin user. | MaxLen: 35
    admin_restrict_local: Literal["enable", "disable"]  # Enable/disable local admin authentication restrict | Default: disable

# Nested TypedDicts for table field children (dict mode)

class WtpProfileLedschedulesItem(TypedDict):
    """Type hints for led-schedules table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Schedule name. | MaxLen: 35


class WtpProfileDenymaclistItem(TypedDict):
    """Type hints for deny-mac-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    mac: str  # A WiFi device with this MAC address is denied acce | Default: 00:00:00:00:00:00


class WtpProfileSplittunnelingaclItem(TypedDict):
    """Type hints for split-tunneling-acl table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    dest_ip: str  # Destination IP and mask for the split-tunneling su | Default: 0.0.0.0 0.0.0.0


# Nested classes for table field children (object mode)

@final
class WtpProfileLedschedulesObject:
    """Typed object for led-schedules table items.
    
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
class WtpProfileDenymaclistObject:
    """Typed object for deny-mac-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # A WiFi device with this MAC address is denied access to this | Default: 00:00:00:00:00:00
    mac: str
    
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
class WtpProfileSplittunnelingaclObject:
    """Typed object for split-tunneling-acl table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Destination IP and mask for the split-tunneling subnet. | Default: 0.0.0.0 0.0.0.0
    dest_ip: str
    
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
class WtpProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/wtp_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # WTP (or FortiAP or AP) profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    platform: str  # WTP, FortiAP, or AP platform.
    control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]  # Enable/disable CAPWAP control message data channel | Default: ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis
    bonjour_profile: str  # Bonjour profile name. | MaxLen: 35
    apcfg_profile: str  # AP local configuration profile name. | MaxLen: 35
    apcfg_mesh: Literal["enable", "disable"]  # Enable/disable AP local mesh configuration | Default: disable
    apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"]  # Mesh AP Type (default = ethernet). | Default: ethernet
    apcfg_mesh_ssid: str  #  Mesh SSID (default = none). | MaxLen: 15
    apcfg_mesh_eth_bridge: Literal["enable", "disable"]  # Enable/disable mesh ethernet bridge | Default: disable
    ble_profile: str  # Bluetooth Low Energy profile name. | MaxLen: 35
    lw_profile: str  # LoRaWAN profile name. | MaxLen: 35
    syslog_profile: str  # System log server configuration profile name. | MaxLen: 35
    wan_port_mode: Literal["wan-lan", "wan-only"]  # Enable/disable using a WAN port as a LAN port. | Default: wan-only
    lan: str  # WTP LAN port mapping.
    energy_efficient_ethernet: Literal["enable", "disable"]  # Enable/disable use of energy efficient Ethernet on | Default: disable
    led_state: Literal["enable", "disable"]  # Enable/disable use of LEDs on WTP | Default: enable
    led_schedules: list[WtpProfileLedschedulesItem]  # Recurring firewall schedules for illuminating LEDs
    dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"]  # WTP data channel DTLS policy | Default: clear-text
    dtls_in_kernel: Literal["enable", "disable"]  # Enable/disable data channel DTLS in kernel. | Default: disable
    max_clients: int  # Maximum number of stations (STAs) supported by the | Default: 0 | Min: 0 | Max: 4294967295
    handoff_rssi: int  # Minimum received signal strength indicator (RSSI) | Default: 25 | Min: 20 | Max: 30
    handoff_sta_thresh: int  # Threshold value for AP handoff. | Default: 0 | Min: 5 | Max: 60
    handoff_roaming: Literal["enable", "disable"]  # Enable/disable client load balancing during roamin | Default: enable
    deny_mac_list: list[WtpProfileDenymaclistItem]  # List of MAC addresses that are denied access to th
    ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]  # Country in which this WTP, FortiAP, or AP will ope | Default: --
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]  # Method(s) by which IP fragmentation is prevented f | Default: tcp-mss-adjust
    tun_mtu_uplink: int  # The maximum transmission unit (MTU) of uplink CAPW | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_downlink: int  # The MTU of downlink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    split_tunneling_acl_path: Literal["tunnel", "local"]  # Split tunneling ACL path is local/tunnel. | Default: local
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]  # Enable/disable automatically adding local subnetwo | Default: disable
    split_tunneling_acl: list[WtpProfileSplittunnelingaclItem]  # Split tunneling ACL filter list.
    allowaccess: Literal["https", "ssh", "snmp"]  # Control management access to the managed WTP, Fort
    login_passwd_change: Literal["yes", "default", "no"]  # Change or reset the administrator password of a ma | Default: no
    login_passwd: str  # Set the managed WTP, FortiAP, or AP's administrato | MaxLen: 128
    lldp: Literal["enable", "disable"]  # Enable/disable Link Layer Discovery Protocol | Default: enable
    poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]  # Set the WTP, FortiAP, or AP's PoE mode. | Default: auto
    usb_port: Literal["enable", "disable"]  # Enable/disable USB port of the WTP | Default: enable
    frequency_handoff: Literal["enable", "disable"]  # Enable/disable frequency handoff of clients to oth | Default: disable
    ap_handoff: Literal["enable", "disable"]  # Enable/disable AP handoff of clients to other APs | Default: disable
    default_mesh_root: Literal["enable", "disable"]  # Configure default mesh root SSID when it is not in | Default: disable
    radio_1: str  # Configuration options for radio 1.
    radio_2: str  # Configuration options for radio 2.
    radio_3: str  # Configuration options for radio 3.
    radio_4: str  # Configuration options for radio 4.
    lbs: str  # Set various location based service (LBS) options.
    ext_info_enable: Literal["enable", "disable"]  # Enable/disable station/VAP/radio extension informa | Default: enable
    indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"]  # Set to allow indoor/outdoor-only channels under re | Default: platform-determined
    esl_ses_dongle: str  # ESL SES-imagotag dongle configuration.
    console_login: Literal["enable", "disable"]  # Enable/disable FortiAP console login access | Default: enable
    wan_port_auth: Literal["none", "802.1x"]  # Set WAN port authentication mode (default = none). | Default: none
    wan_port_auth_usrname: str  # Set WAN port 802.1x supplicant user name. | MaxLen: 63
    wan_port_auth_password: str  # Set WAN port 802.1x supplicant password. | MaxLen: 128
    wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]  # WAN port 802.1x supplicant EAP methods | Default: all
    wan_port_auth_macsec: Literal["enable", "disable"]  # Enable/disable WAN port 802.1x supplicant MACsec p | Default: disable
    apcfg_auto_cert: Literal["enable", "disable"]  # Enable/disable AP local auto cert configuration | Default: disable
    apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"]  # Certificate enrollment protocol (default = none) | Default: none
    apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]  # Cryptography algorithm: rsa-1024, rsa-1536, rsa-20 | Default: ec-secp256r1
    apcfg_auto_cert_est_server: str  # Address and port for EST server | MaxLen: 255
    apcfg_auto_cert_est_ca_id: str  # CA identifier of the CA server for signing via EST | MaxLen: 255
    apcfg_auto_cert_est_http_username: str  # HTTP Authentication username for signing via EST. | MaxLen: 63
    apcfg_auto_cert_est_http_password: str  # HTTP Authentication password for signing via EST. | MaxLen: 128
    apcfg_auto_cert_est_subject: str  # Subject e.g. "CN=User,DC=example,DC=COM" | Default: CN=FortiAP,DC=local,DC=COM | MaxLen: 127
    apcfg_auto_cert_est_subject_alt_name: str  # Subject alternative name | MaxLen: 127
    apcfg_auto_cert_auto_regen_days: int  # Number of days to wait before expiry of an updated | Default: 30 | Min: 0 | Max: 4294967295
    apcfg_auto_cert_est_https_ca: str  # PEM format https CA Certificate. | MaxLen: 79
    apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"]  # Key type (default = rsa) | Default: rsa
    apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"]  # Key size: 1024, 1536, 2048, 4096 (default 2048). | Default: 2048
    apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"]  # Elliptic curve name: secp256r1, secp384r1 and secp | Default: secp256r1
    apcfg_auto_cert_scep_sub_fully_dn: str  # Full DN of the subject | MaxLen: 255
    apcfg_auto_cert_scep_url: str  # SCEP server URL. | MaxLen: 255
    apcfg_auto_cert_scep_password: str  # SCEP server challenge password for auto-regenerati | MaxLen: 128
    apcfg_auto_cert_scep_ca_id: str  # CA identifier of the CA server for signing via SCE | MaxLen: 255
    apcfg_auto_cert_scep_subject_alt_name: str  # Subject alternative name | MaxLen: 127
    apcfg_auto_cert_scep_https_ca: str  # PEM format https CA Certificate. | MaxLen: 79
    unii_4_5ghz_band: Literal["enable", "disable"]  # Enable/disable UNII-4 5Ghz band channels | Default: disable
    admin_auth_tacacs_plus: str  # Remote authentication server for admin user. | MaxLen: 35
    admin_restrict_local: Literal["enable", "disable"]  # Enable/disable local admin authentication restrict | Default: disable


@final
class WtpProfileObject:
    """Typed FortiObject for wireless_controller/wtp_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WTP (or FortiAP or AP) profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # WTP, FortiAP, or AP platform.
    platform: str
    # Enable/disable CAPWAP control message data channel offload. | Default: ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis
    control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]
    # Bonjour profile name. | MaxLen: 35
    bonjour_profile: str
    # AP local configuration profile name. | MaxLen: 35
    apcfg_profile: str
    # Enable/disable AP local mesh configuration | Default: disable
    apcfg_mesh: Literal["enable", "disable"]
    # Mesh AP Type (default = ethernet). | Default: ethernet
    apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"]
    #  Mesh SSID (default = none). | MaxLen: 15
    apcfg_mesh_ssid: str
    # Enable/disable mesh ethernet bridge (default = disable). | Default: disable
    apcfg_mesh_eth_bridge: Literal["enable", "disable"]
    # Bluetooth Low Energy profile name. | MaxLen: 35
    ble_profile: str
    # LoRaWAN profile name. | MaxLen: 35
    lw_profile: str
    # System log server configuration profile name. | MaxLen: 35
    syslog_profile: str
    # Enable/disable using a WAN port as a LAN port. | Default: wan-only
    wan_port_mode: Literal["wan-lan", "wan-only"]
    # WTP LAN port mapping.
    lan: str
    # Enable/disable use of energy efficient Ethernet on WTP. | Default: disable
    energy_efficient_ethernet: Literal["enable", "disable"]
    # Enable/disable use of LEDs on WTP (default = enable). | Default: enable
    led_state: Literal["enable", "disable"]
    # Recurring firewall schedules for illuminating LEDs on the Fo
    led_schedules: list[WtpProfileLedschedulesObject]
    # WTP data channel DTLS policy (default = clear-text). | Default: clear-text
    dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"]
    # Enable/disable data channel DTLS in kernel. | Default: disable
    dtls_in_kernel: Literal["enable", "disable"]
    # Maximum number of stations (STAs) supported by the WTP | Default: 0 | Min: 0 | Max: 4294967295
    max_clients: int
    # Minimum received signal strength indicator (RSSI) value for | Default: 25 | Min: 20 | Max: 30
    handoff_rssi: int
    # Threshold value for AP handoff. | Default: 0 | Min: 5 | Max: 60
    handoff_sta_thresh: int
    # Enable/disable client load balancing during roaming to avoid | Default: enable
    handoff_roaming: Literal["enable", "disable"]
    # List of MAC addresses that are denied access to this WTP, Fo
    deny_mac_list: list[WtpProfileDenymaclistObject]
    # Country in which this WTP, FortiAP, or AP will operate | Default: --
    ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"]
    # Method(s) by which IP fragmentation is prevented for control | Default: tcp-mss-adjust
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]
    # The maximum transmission unit (MTU) of uplink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_uplink: int
    # The MTU of downlink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_downlink: int
    # Split tunneling ACL path is local/tunnel. | Default: local
    split_tunneling_acl_path: Literal["tunnel", "local"]
    # Enable/disable automatically adding local subnetwork of Fort | Default: disable
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    # Split tunneling ACL filter list.
    split_tunneling_acl: list[WtpProfileSplittunnelingaclObject]
    # Control management access to the managed WTP, FortiAP, or AP
    allowaccess: Literal["https", "ssh", "snmp"]
    # Change or reset the administrator password of a managed WTP, | Default: no
    login_passwd_change: Literal["yes", "default", "no"]
    # Set the managed WTP, FortiAP, or AP's administrator password | MaxLen: 128
    login_passwd: str
    # Enable/disable Link Layer Discovery Protocol (LLDP) for the | Default: enable
    lldp: Literal["enable", "disable"]
    # Set the WTP, FortiAP, or AP's PoE mode. | Default: auto
    poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"]
    # Enable/disable USB port of the WTP (default = enable). | Default: enable
    usb_port: Literal["enable", "disable"]
    # Enable/disable frequency handoff of clients to other channel | Default: disable
    frequency_handoff: Literal["enable", "disable"]
    # Enable/disable AP handoff of clients to other APs | Default: disable
    ap_handoff: Literal["enable", "disable"]
    # Configure default mesh root SSID when it is not included by | Default: disable
    default_mesh_root: Literal["enable", "disable"]
    # Configuration options for radio 1.
    radio_1: str
    # Configuration options for radio 2.
    radio_2: str
    # Configuration options for radio 3.
    radio_3: str
    # Configuration options for radio 4.
    radio_4: str
    # Set various location based service (LBS) options.
    lbs: str
    # Enable/disable station/VAP/radio extension information. | Default: enable
    ext_info_enable: Literal["enable", "disable"]
    # Set to allow indoor/outdoor-only channels under regulatory r | Default: platform-determined
    indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"]
    # ESL SES-imagotag dongle configuration.
    esl_ses_dongle: str
    # Enable/disable FortiAP console login access | Default: enable
    console_login: Literal["enable", "disable"]
    # Set WAN port authentication mode (default = none). | Default: none
    wan_port_auth: Literal["none", "802.1x"]
    # Set WAN port 802.1x supplicant user name. | MaxLen: 63
    wan_port_auth_usrname: str
    # Set WAN port 802.1x supplicant password. | MaxLen: 128
    wan_port_auth_password: str
    # WAN port 802.1x supplicant EAP methods (default = all). | Default: all
    wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]
    # Enable/disable WAN port 802.1x supplicant MACsec policy | Default: disable
    wan_port_auth_macsec: Literal["enable", "disable"]
    # Enable/disable AP local auto cert configuration | Default: disable
    apcfg_auto_cert: Literal["enable", "disable"]
    # Certificate enrollment protocol (default = none) | Default: none
    apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"]
    # Cryptography algorithm: rsa-1024, rsa-1536, rsa-2048, rsa-40 | Default: ec-secp256r1
    apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"]
    # Address and port for EST server | MaxLen: 255
    apcfg_auto_cert_est_server: str
    # CA identifier of the CA server for signing via EST. | MaxLen: 255
    apcfg_auto_cert_est_ca_id: str
    # HTTP Authentication username for signing via EST. | MaxLen: 63
    apcfg_auto_cert_est_http_username: str
    # HTTP Authentication password for signing via EST. | MaxLen: 128
    apcfg_auto_cert_est_http_password: str
    # Subject e.g. "CN=User,DC=example,DC=COM" | Default: CN=FortiAP,DC=local,DC=COM | MaxLen: 127
    apcfg_auto_cert_est_subject: str
    # Subject alternative name | MaxLen: 127
    apcfg_auto_cert_est_subject_alt_name: str
    # Number of days to wait before expiry of an updated local cer | Default: 30 | Min: 0 | Max: 4294967295
    apcfg_auto_cert_auto_regen_days: int
    # PEM format https CA Certificate. | MaxLen: 79
    apcfg_auto_cert_est_https_ca: str
    # Key type (default = rsa) | Default: rsa
    apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"]
    # Key size: 1024, 1536, 2048, 4096 (default 2048). | Default: 2048
    apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"]
    # Elliptic curve name: secp256r1, secp384r1 and secp521r1. | Default: secp256r1
    apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"]
    # Full DN of the subject | MaxLen: 255
    apcfg_auto_cert_scep_sub_fully_dn: str
    # SCEP server URL. | MaxLen: 255
    apcfg_auto_cert_scep_url: str
    # SCEP server challenge password for auto-regeneration. | MaxLen: 128
    apcfg_auto_cert_scep_password: str
    # CA identifier of the CA server for signing via SCEP. | MaxLen: 255
    apcfg_auto_cert_scep_ca_id: str
    # Subject alternative name | MaxLen: 127
    apcfg_auto_cert_scep_subject_alt_name: str
    # PEM format https CA Certificate. | MaxLen: 79
    apcfg_auto_cert_scep_https_ca: str
    # Enable/disable UNII-4 5Ghz band channels (default = disable) | Default: disable
    unii_4_5ghz_band: Literal["enable", "disable"]
    # Remote authentication server for admin user. | MaxLen: 35
    admin_auth_tacacs_plus: str
    # Enable/disable local admin authentication restriction when r | Default: disable
    admin_restrict_local: Literal["enable", "disable"]
    
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
    def to_dict(self) -> WtpProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class WtpProfile:
    """
    Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
    
    Path: wireless_controller/wtp_profile
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
    ) -> WtpProfileObject: ...
    
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
    ) -> WtpProfileObject: ...
    
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
    ) -> FortiObjectList[WtpProfileObject]: ...
    
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
    ) -> WtpProfileObject: ...
    
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
    ) -> WtpProfileObject: ...
    
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
    ) -> FortiObjectList[WtpProfileObject]: ...
    
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
    ) -> WtpProfileObject: ...
    
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
    ) -> WtpProfileObject: ...
    
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
    ) -> FortiObjectList[WtpProfileObject]: ...
    
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
    ) -> WtpProfileObject | list[WtpProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpProfileObject: ...
    
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
        payload_dict: WtpProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        platform: str | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        bonjour_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        apcfg_mesh: Literal["enable", "disable"] | None = ...,
        apcfg_mesh_ap_type: Literal["ethernet", "mesh", "auto"] | None = ...,
        apcfg_mesh_ssid: str | None = ...,
        apcfg_mesh_eth_bridge: Literal["enable", "disable"] | None = ...,
        ble_profile: str | None = ...,
        lw_profile: str | None = ...,
        syslog_profile: str | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        lan: str | None = ...,
        energy_efficient_ethernet: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        led_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        dtls_policy: Literal["clear-text", "dtls-enabled", "ipsec-vpn", "ipsec-sn-vpn"] | list[str] | None = ...,
        dtls_in_kernel: Literal["enable", "disable"] | None = ...,
        max_clients: int | None = ...,
        handoff_rssi: int | None = ...,
        handoff_sta_thresh: int | None = ...,
        handoff_roaming: Literal["enable", "disable"] | None = ...,
        deny_mac_list: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_country: Literal["--", "AF", "AL", "DZ", "AS", "AO", "AR", "AM", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BA", "BW", "BR", "BN", "BG", "BF", "KH", "CM", "KY", "CF", "TD", "CL", "CN", "CX", "CO", "CG", "CD", "CR", "HR", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "ET", "EE", "GF", "PF", "FO", "FJ", "FI", "FR", "GA", "GE", "GM", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GY", "HT", "HN", "HK", "HU", "IS", "IN", "ID", "IQ", "IE", "IM", "IL", "IT", "CI", "JM", "JO", "KZ", "KE", "KR", "KW", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT", "MX", "FM", "MD", "MC", "MN", "MA", "MZ", "MM", "NA", "NP", "NL", "AN", "AW", "NZ", "NI", "NE", "NG", "NO", "MP", "OM", "PK", "PW", "PA", "PG", "PY", "PE", "PH", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "KN", "LC", "MF", "PM", "VC", "SA", "SN", "RS", "ME", "SL", "SG", "SK", "SI", "SO", "ZA", "ES", "LK", "SR", "SZ", "SE", "CH", "TW", "TZ", "TH", "TL", "TG", "TT", "TN", "TR", "TM", "AE", "TC", "UG", "UA", "GB", "US", "PS", "UY", "UZ", "VU", "VE", "VN", "VI", "WF", "YE", "ZM", "ZW", "JP", "CA"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        lldp: Literal["enable", "disable"] | None = ...,
        poe_mode: Literal["auto", "8023af", "8023at", "power-adapter", "full", "high", "low"] | None = ...,
        usb_port: Literal["enable", "disable"] | None = ...,
        frequency_handoff: Literal["enable", "disable"] | None = ...,
        ap_handoff: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        lbs: str | None = ...,
        ext_info_enable: Literal["enable", "disable"] | None = ...,
        indoor_outdoor_deployment: Literal["platform-determined", "outdoor", "indoor"] | None = ...,
        esl_ses_dongle: str | None = ...,
        console_login: Literal["enable", "disable"] | None = ...,
        wan_port_auth: Literal["none", "802.1x"] | None = ...,
        wan_port_auth_usrname: str | None = ...,
        wan_port_auth_password: str | None = ...,
        wan_port_auth_methods: Literal["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"] | None = ...,
        wan_port_auth_macsec: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert: Literal["enable", "disable"] | None = ...,
        apcfg_auto_cert_enroll_protocol: Literal["none", "est", "scep"] | None = ...,
        apcfg_auto_cert_crypto_algo: Literal["rsa-1024", "rsa-1536", "rsa-2048", "rsa-4096", "ec-secp256r1", "ec-secp384r1", "ec-secp521r1"] | None = ...,
        apcfg_auto_cert_est_server: str | None = ...,
        apcfg_auto_cert_est_ca_id: str | None = ...,
        apcfg_auto_cert_est_http_username: str | None = ...,
        apcfg_auto_cert_est_http_password: str | None = ...,
        apcfg_auto_cert_est_subject: str | None = ...,
        apcfg_auto_cert_est_subject_alt_name: str | None = ...,
        apcfg_auto_cert_auto_regen_days: int | None = ...,
        apcfg_auto_cert_est_https_ca: str | None = ...,
        apcfg_auto_cert_scep_keytype: Literal["rsa", "ec"] | None = ...,
        apcfg_auto_cert_scep_keysize: Literal["1024", "1536", "2048", "4096"] | None = ...,
        apcfg_auto_cert_scep_ec_name: Literal["secp256r1", "secp384r1", "secp521r1"] | None = ...,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = ...,
        apcfg_auto_cert_scep_url: str | None = ...,
        apcfg_auto_cert_scep_password: str | None = ...,
        apcfg_auto_cert_scep_ca_id: str | None = ...,
        apcfg_auto_cert_scep_subject_alt_name: str | None = ...,
        apcfg_auto_cert_scep_https_ca: str | None = ...,
        unii_4_5ghz_band: Literal["enable", "disable"] | None = ...,
        admin_auth_tacacs_plus: str | None = ...,
        admin_restrict_local: Literal["enable", "disable"] | None = ...,
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
    "WtpProfile",
    "WtpProfilePayload",
    "WtpProfileResponse",
    "WtpProfileObject",
]
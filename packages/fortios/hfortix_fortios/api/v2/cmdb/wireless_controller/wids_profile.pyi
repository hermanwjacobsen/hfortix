from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WidsProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wids_profile payload fields.
    
    Configure wireless intrusion detection system (WIDS) profiles.
    
    **Usage:**
        payload: WidsProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # WIDS profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    sensor_mode: Literal["disable", "foreign", "both"]  # Scan nearby WiFi stations (default = disable). | Default: disable
    ap_scan: Literal["disable", "enable"]  # Enable/disable rogue AP detection. | Default: disable
    ap_scan_channel_list_2G_5G: list[dict[str, Any]]  # Selected ap scan channel list for 2.4G and 5G band
    ap_scan_channel_list_6G: list[dict[str, Any]]  # Selected ap scan channel list for 6G band.
    ap_bgscan_period: int  # Period between background scans | Default: 600 | Min: 10 | Max: 3600
    ap_bgscan_intv: int  # Period between successive channel scans | Default: 3 | Min: 1 | Max: 600
    ap_bgscan_duration: int  # Listen time on scanning a channel | Default: 30 | Min: 10 | Max: 1000
    ap_bgscan_idle: int  # Wait time for channel inactivity before scanning t | Default: 20 | Min: 0 | Max: 1000
    ap_bgscan_report_intv: int  # Period between background scan reports | Default: 30 | Min: 15 | Max: 600
    ap_bgscan_disable_schedules: list[dict[str, Any]]  # Firewall schedules for turning off FortiAP radio b
    ap_fgscan_report_intv: int  # Period between foreground scan reports | Default: 15 | Min: 15 | Max: 600
    ap_scan_passive: Literal["enable", "disable"]  # Enable/disable passive scanning. Enable means do n | Default: disable
    ap_scan_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -90 | MaxLen: 7
    ap_auto_suppress: Literal["enable", "disable"]  # Enable/disable on-wire rogue AP auto-suppression | Default: disable
    wireless_bridge: Literal["enable", "disable"]  # Enable/disable wireless bridge detection | Default: disable
    deauth_broadcast: Literal["enable", "disable"]  # Enable/disable broadcasting de-authentication dete | Default: disable
    null_ssid_probe_resp: Literal["enable", "disable"]  # Enable/disable null SSID probe response detection | Default: disable
    long_duration_attack: Literal["enable", "disable"]  # Enable/disable long duration attack detection base | Default: disable
    long_duration_thresh: int  # Threshold value for long duration attack detection | Default: 8200 | Min: 1000 | Max: 32767
    invalid_mac_oui: Literal["enable", "disable"]  # Enable/disable invalid MAC OUI detection. | Default: disable
    weak_wep_iv: Literal["enable", "disable"]  # Enable/disable weak WEP IV (Initialization Vector) | Default: disable
    auth_frame_flood: Literal["enable", "disable"]  # Enable/disable authentication frame flooding detec | Default: disable
    auth_flood_time: int  # Number of seconds after which a station is conside | Default: 10 | Min: 5 | Max: 120
    auth_flood_thresh: int  # The threshold value for authentication frame flood | Default: 30 | Min: 1 | Max: 100
    assoc_frame_flood: Literal["enable", "disable"]  # Enable/disable association frame flooding detectio | Default: disable
    assoc_flood_time: int  # Number of seconds after which a station is conside | Default: 10 | Min: 5 | Max: 120
    assoc_flood_thresh: int  # The threshold value for association frame flooding | Default: 30 | Min: 1 | Max: 100
    reassoc_flood: Literal["enable", "disable"]  # Enable/disable reassociation flood detection | Default: disable
    reassoc_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    reassoc_flood_thresh: int  # The threshold value for reassociation flood. | Default: 30 | Min: 1 | Max: 65100
    probe_flood: Literal["enable", "disable"]  # Enable/disable probe flood detection | Default: disable
    probe_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    probe_flood_thresh: int  # The threshold value for probe flood. | Default: 30 | Min: 1 | Max: 65100
    bcn_flood: Literal["enable", "disable"]  # Enable/disable bcn flood detection | Default: disable
    bcn_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    bcn_flood_thresh: int  # The threshold value for bcn flood. | Default: 15 | Min: 1 | Max: 65100
    rts_flood: Literal["enable", "disable"]  # Enable/disable rts flood detection | Default: disable
    rts_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    rts_flood_thresh: int  # The threshold value for rts flood. | Default: 30 | Min: 1 | Max: 65100
    cts_flood: Literal["enable", "disable"]  # Enable/disable cts flood detection | Default: disable
    cts_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    cts_flood_thresh: int  # The threshold value for cts flood. | Default: 30 | Min: 1 | Max: 65100
    client_flood: Literal["enable", "disable"]  # Enable/disable client flood detection | Default: disable
    client_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    client_flood_thresh: int  # The threshold value for client flood. | Default: 30 | Min: 1 | Max: 65100
    block_ack_flood: Literal["enable", "disable"]  # Enable/disable block_ack flood detection | Default: disable
    block_ack_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    block_ack_flood_thresh: int  # The threshold value for block_ack flood. | Default: 50 | Min: 1 | Max: 65100
    pspoll_flood: Literal["enable", "disable"]  # Enable/disable pspoll flood detection | Default: disable
    pspoll_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    pspoll_flood_thresh: int  # The threshold value for pspoll flood. | Default: 30 | Min: 1 | Max: 65100
    netstumbler: Literal["enable", "disable"]  # Enable/disable netstumbler detection | Default: disable
    netstumbler_time: int  # Detection Window Period. | Default: 30 | Min: 1 | Max: 120
    netstumbler_thresh: int  # The threshold value for netstumbler. | Default: 5 | Min: 1 | Max: 65100
    wellenreiter: Literal["enable", "disable"]  # Enable/disable wellenreiter detection | Default: disable
    wellenreiter_time: int  # Detection Window Period. | Default: 30 | Min: 1 | Max: 120
    wellenreiter_thresh: int  # The threshold value for wellenreiter. | Default: 5 | Min: 1 | Max: 65100
    spoofed_deauth: Literal["enable", "disable"]  # Enable/disable spoofed de-authentication attack de | Default: disable
    asleap_attack: Literal["enable", "disable"]  # Enable/disable asleap attack detection | Default: disable
    eapol_start_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Start flooding (to AP) detect | Default: disable
    eapol_start_thresh: int  # The threshold value for EAPOL-Start flooding in sp | Default: 10 | Min: 2 | Max: 100
    eapol_start_intv: int  # The detection interval for EAPOL-Start flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_logoff_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Logoff flooding (to AP) detec | Default: disable
    eapol_logoff_thresh: int  # The threshold value for EAPOL-Logoff flooding in s | Default: 10 | Min: 2 | Max: 100
    eapol_logoff_intv: int  # The detection interval for EAPOL-Logoff flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_succ_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Success flooding (to AP) dete | Default: disable
    eapol_succ_thresh: int  # The threshold value for EAPOL-Success flooding in | Default: 10 | Min: 2 | Max: 100
    eapol_succ_intv: int  # The detection interval for EAPOL-Success flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_fail_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Failure flooding (to AP) dete | Default: disable
    eapol_fail_thresh: int  # The threshold value for EAPOL-Failure flooding in | Default: 10 | Min: 2 | Max: 100
    eapol_fail_intv: int  # The detection interval for EAPOL-Failure flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_pre_succ_flood: Literal["enable", "disable"]  # Enable/disable premature EAPOL-Success flooding | Default: disable
    eapol_pre_succ_thresh: int  # The threshold value for premature EAPOL-Success fl | Default: 10 | Min: 2 | Max: 100
    eapol_pre_succ_intv: int  # The detection interval for premature EAPOL-Success | Default: 1 | Min: 1 | Max: 3600
    eapol_pre_fail_flood: Literal["enable", "disable"]  # Enable/disable premature EAPOL-Failure flooding | Default: disable
    eapol_pre_fail_thresh: int  # The threshold value for premature EAPOL-Failure fl | Default: 10 | Min: 2 | Max: 100
    eapol_pre_fail_intv: int  # The detection interval for premature EAPOL-Failure | Default: 1 | Min: 1 | Max: 3600
    deauth_unknown_src_thresh: int  # Threshold value per second to deauth unknown src f | Default: 10 | Min: 0 | Max: 65535
    windows_bridge: Literal["enable", "disable"]  # Enable/disable windows bridge detection | Default: disable
    disassoc_broadcast: Literal["enable", "disable"]  # Enable/disable broadcast dis-association detection | Default: disable
    ap_spoofing: Literal["enable", "disable"]  # Enable/disable AP spoofing detection | Default: disable
    chan_based_mitm: Literal["enable", "disable"]  # Enable/disable channel based mitm detection | Default: disable
    adhoc_valid_ssid: Literal["enable", "disable"]  # Enable/disable adhoc using valid SSID detection | Default: disable
    adhoc_network: Literal["enable", "disable"]  # Enable/disable adhoc network detection | Default: disable
    eapol_key_overflow: Literal["enable", "disable"]  # Enable/disable overflow EAPOL key detection | Default: disable
    ap_impersonation: Literal["enable", "disable"]  # Enable/disable AP impersonation detection | Default: disable
    invalid_addr_combination: Literal["enable", "disable"]  # Enable/disable invalid address combination detecti | Default: disable
    beacon_wrong_channel: Literal["enable", "disable"]  # Enable/disable beacon wrong channel detection | Default: disable
    ht_greenfield: Literal["enable", "disable"]  # Enable/disable HT greenfield detection | Default: disable
    overflow_ie: Literal["enable", "disable"]  # Enable/disable overflow IE detection | Default: disable
    malformed_ht_ie: Literal["enable", "disable"]  # Enable/disable malformed HT IE detection | Default: disable
    malformed_auth: Literal["enable", "disable"]  # Enable/disable malformed auth frame detection | Default: disable
    malformed_association: Literal["enable", "disable"]  # Enable/disable malformed association request detec | Default: disable
    ht_40mhz_intolerance: Literal["enable", "disable"]  # Enable/disable HT 40 MHz intolerance detection | Default: disable
    valid_ssid_misuse: Literal["enable", "disable"]  # Enable/disable valid SSID misuse detection | Default: disable
    valid_client_misassociation: Literal["enable", "disable"]  # Enable/disable valid client misassociation detecti | Default: disable
    hotspotter_attack: Literal["enable", "disable"]  # Enable/disable hotspotter attack detection | Default: disable
    pwsave_dos_attack: Literal["enable", "disable"]  # Enable/disable power save DOS attack detection | Default: disable
    omerta_attack: Literal["enable", "disable"]  # Enable/disable omerta attack detection | Default: disable
    disconnect_station: Literal["enable", "disable"]  # Enable/disable disconnect station detection | Default: disable
    unencrypted_valid: Literal["enable", "disable"]  # Enable/disable unencrypted valid detection | Default: disable
    fata_jack: Literal["enable", "disable"]  # Enable/disable FATA-Jack detection | Default: disable
    risky_encryption: Literal["enable", "disable"]  # Enable/disable Risky Encryption detection | Default: disable
    fuzzed_beacon: Literal["enable", "disable"]  # Enable/disable fuzzed beacon detection | Default: disable
    fuzzed_probe_request: Literal["enable", "disable"]  # Enable/disable fuzzed probe request detection | Default: disable
    fuzzed_probe_response: Literal["enable", "disable"]  # Enable/disable fuzzed probe response detection | Default: disable
    air_jack: Literal["enable", "disable"]  # Enable/disable AirJack detection | Default: disable
    wpa_ft_attack: Literal["enable", "disable"]  # Enable/disable WPA FT attack detection | Default: disable

# Nested TypedDicts for table field children (dict mode)

class WidsProfileApscanchannellist2g5gItem(TypedDict):
    """Type hints for ap-scan-channel-list-2G-5G table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    chan: str  # Channel number. | MaxLen: 3


class WidsProfileApscanchannellist6gItem(TypedDict):
    """Type hints for ap-scan-channel-list-6G table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    chan: str  # Channel 6g number. | MaxLen: 3


class WidsProfileApbgscandisableschedulesItem(TypedDict):
    """Type hints for ap-bgscan-disable-schedules table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Schedule name. | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class WidsProfileApscanchannellist2g5gObject:
    """Typed object for ap-scan-channel-list-2G-5G table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Channel number. | MaxLen: 3
    chan: str
    
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
class WidsProfileApscanchannellist6gObject:
    """Typed object for ap-scan-channel-list-6G table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Channel 6g number. | MaxLen: 3
    chan: str
    
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
class WidsProfileApbgscandisableschedulesObject:
    """Typed object for ap-bgscan-disable-schedules table items.
    
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



# Response TypedDict for GET returns (all fields present in API response)
class WidsProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/wids_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # WIDS profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    sensor_mode: Literal["disable", "foreign", "both"]  # Scan nearby WiFi stations (default = disable). | Default: disable
    ap_scan: Literal["disable", "enable"]  # Enable/disable rogue AP detection. | Default: disable
    ap_scan_channel_list_2G_5G: list[WidsProfileApscanchannellist2g5gItem]  # Selected ap scan channel list for 2.4G and 5G band
    ap_scan_channel_list_6G: list[WidsProfileApscanchannellist6gItem]  # Selected ap scan channel list for 6G band.
    ap_bgscan_period: int  # Period between background scans | Default: 600 | Min: 10 | Max: 3600
    ap_bgscan_intv: int  # Period between successive channel scans | Default: 3 | Min: 1 | Max: 600
    ap_bgscan_duration: int  # Listen time on scanning a channel | Default: 30 | Min: 10 | Max: 1000
    ap_bgscan_idle: int  # Wait time for channel inactivity before scanning t | Default: 20 | Min: 0 | Max: 1000
    ap_bgscan_report_intv: int  # Period between background scan reports | Default: 30 | Min: 15 | Max: 600
    ap_bgscan_disable_schedules: list[WidsProfileApbgscandisableschedulesItem]  # Firewall schedules for turning off FortiAP radio b
    ap_fgscan_report_intv: int  # Period between foreground scan reports | Default: 15 | Min: 15 | Max: 600
    ap_scan_passive: Literal["enable", "disable"]  # Enable/disable passive scanning. Enable means do n | Default: disable
    ap_scan_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -90 | MaxLen: 7
    ap_auto_suppress: Literal["enable", "disable"]  # Enable/disable on-wire rogue AP auto-suppression | Default: disable
    wireless_bridge: Literal["enable", "disable"]  # Enable/disable wireless bridge detection | Default: disable
    deauth_broadcast: Literal["enable", "disable"]  # Enable/disable broadcasting de-authentication dete | Default: disable
    null_ssid_probe_resp: Literal["enable", "disable"]  # Enable/disable null SSID probe response detection | Default: disable
    long_duration_attack: Literal["enable", "disable"]  # Enable/disable long duration attack detection base | Default: disable
    long_duration_thresh: int  # Threshold value for long duration attack detection | Default: 8200 | Min: 1000 | Max: 32767
    invalid_mac_oui: Literal["enable", "disable"]  # Enable/disable invalid MAC OUI detection. | Default: disable
    weak_wep_iv: Literal["enable", "disable"]  # Enable/disable weak WEP IV (Initialization Vector) | Default: disable
    auth_frame_flood: Literal["enable", "disable"]  # Enable/disable authentication frame flooding detec | Default: disable
    auth_flood_time: int  # Number of seconds after which a station is conside | Default: 10 | Min: 5 | Max: 120
    auth_flood_thresh: int  # The threshold value for authentication frame flood | Default: 30 | Min: 1 | Max: 100
    assoc_frame_flood: Literal["enable", "disable"]  # Enable/disable association frame flooding detectio | Default: disable
    assoc_flood_time: int  # Number of seconds after which a station is conside | Default: 10 | Min: 5 | Max: 120
    assoc_flood_thresh: int  # The threshold value for association frame flooding | Default: 30 | Min: 1 | Max: 100
    reassoc_flood: Literal["enable", "disable"]  # Enable/disable reassociation flood detection | Default: disable
    reassoc_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    reassoc_flood_thresh: int  # The threshold value for reassociation flood. | Default: 30 | Min: 1 | Max: 65100
    probe_flood: Literal["enable", "disable"]  # Enable/disable probe flood detection | Default: disable
    probe_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    probe_flood_thresh: int  # The threshold value for probe flood. | Default: 30 | Min: 1 | Max: 65100
    bcn_flood: Literal["enable", "disable"]  # Enable/disable bcn flood detection | Default: disable
    bcn_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    bcn_flood_thresh: int  # The threshold value for bcn flood. | Default: 15 | Min: 1 | Max: 65100
    rts_flood: Literal["enable", "disable"]  # Enable/disable rts flood detection | Default: disable
    rts_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    rts_flood_thresh: int  # The threshold value for rts flood. | Default: 30 | Min: 1 | Max: 65100
    cts_flood: Literal["enable", "disable"]  # Enable/disable cts flood detection | Default: disable
    cts_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    cts_flood_thresh: int  # The threshold value for cts flood. | Default: 30 | Min: 1 | Max: 65100
    client_flood: Literal["enable", "disable"]  # Enable/disable client flood detection | Default: disable
    client_flood_time: int  # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    client_flood_thresh: int  # The threshold value for client flood. | Default: 30 | Min: 1 | Max: 65100
    block_ack_flood: Literal["enable", "disable"]  # Enable/disable block_ack flood detection | Default: disable
    block_ack_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    block_ack_flood_thresh: int  # The threshold value for block_ack flood. | Default: 50 | Min: 1 | Max: 65100
    pspoll_flood: Literal["enable", "disable"]  # Enable/disable pspoll flood detection | Default: disable
    pspoll_flood_time: int  # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    pspoll_flood_thresh: int  # The threshold value for pspoll flood. | Default: 30 | Min: 1 | Max: 65100
    netstumbler: Literal["enable", "disable"]  # Enable/disable netstumbler detection | Default: disable
    netstumbler_time: int  # Detection Window Period. | Default: 30 | Min: 1 | Max: 120
    netstumbler_thresh: int  # The threshold value for netstumbler. | Default: 5 | Min: 1 | Max: 65100
    wellenreiter: Literal["enable", "disable"]  # Enable/disable wellenreiter detection | Default: disable
    wellenreiter_time: int  # Detection Window Period. | Default: 30 | Min: 1 | Max: 120
    wellenreiter_thresh: int  # The threshold value for wellenreiter. | Default: 5 | Min: 1 | Max: 65100
    spoofed_deauth: Literal["enable", "disable"]  # Enable/disable spoofed de-authentication attack de | Default: disable
    asleap_attack: Literal["enable", "disable"]  # Enable/disable asleap attack detection | Default: disable
    eapol_start_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Start flooding (to AP) detect | Default: disable
    eapol_start_thresh: int  # The threshold value for EAPOL-Start flooding in sp | Default: 10 | Min: 2 | Max: 100
    eapol_start_intv: int  # The detection interval for EAPOL-Start flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_logoff_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Logoff flooding (to AP) detec | Default: disable
    eapol_logoff_thresh: int  # The threshold value for EAPOL-Logoff flooding in s | Default: 10 | Min: 2 | Max: 100
    eapol_logoff_intv: int  # The detection interval for EAPOL-Logoff flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_succ_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Success flooding (to AP) dete | Default: disable
    eapol_succ_thresh: int  # The threshold value for EAPOL-Success flooding in | Default: 10 | Min: 2 | Max: 100
    eapol_succ_intv: int  # The detection interval for EAPOL-Success flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_fail_flood: Literal["enable", "disable"]  # Enable/disable EAPOL-Failure flooding (to AP) dete | Default: disable
    eapol_fail_thresh: int  # The threshold value for EAPOL-Failure flooding in | Default: 10 | Min: 2 | Max: 100
    eapol_fail_intv: int  # The detection interval for EAPOL-Failure flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_pre_succ_flood: Literal["enable", "disable"]  # Enable/disable premature EAPOL-Success flooding | Default: disable
    eapol_pre_succ_thresh: int  # The threshold value for premature EAPOL-Success fl | Default: 10 | Min: 2 | Max: 100
    eapol_pre_succ_intv: int  # The detection interval for premature EAPOL-Success | Default: 1 | Min: 1 | Max: 3600
    eapol_pre_fail_flood: Literal["enable", "disable"]  # Enable/disable premature EAPOL-Failure flooding | Default: disable
    eapol_pre_fail_thresh: int  # The threshold value for premature EAPOL-Failure fl | Default: 10 | Min: 2 | Max: 100
    eapol_pre_fail_intv: int  # The detection interval for premature EAPOL-Failure | Default: 1 | Min: 1 | Max: 3600
    deauth_unknown_src_thresh: int  # Threshold value per second to deauth unknown src f | Default: 10 | Min: 0 | Max: 65535
    windows_bridge: Literal["enable", "disable"]  # Enable/disable windows bridge detection | Default: disable
    disassoc_broadcast: Literal["enable", "disable"]  # Enable/disable broadcast dis-association detection | Default: disable
    ap_spoofing: Literal["enable", "disable"]  # Enable/disable AP spoofing detection | Default: disable
    chan_based_mitm: Literal["enable", "disable"]  # Enable/disable channel based mitm detection | Default: disable
    adhoc_valid_ssid: Literal["enable", "disable"]  # Enable/disable adhoc using valid SSID detection | Default: disable
    adhoc_network: Literal["enable", "disable"]  # Enable/disable adhoc network detection | Default: disable
    eapol_key_overflow: Literal["enable", "disable"]  # Enable/disable overflow EAPOL key detection | Default: disable
    ap_impersonation: Literal["enable", "disable"]  # Enable/disable AP impersonation detection | Default: disable
    invalid_addr_combination: Literal["enable", "disable"]  # Enable/disable invalid address combination detecti | Default: disable
    beacon_wrong_channel: Literal["enable", "disable"]  # Enable/disable beacon wrong channel detection | Default: disable
    ht_greenfield: Literal["enable", "disable"]  # Enable/disable HT greenfield detection | Default: disable
    overflow_ie: Literal["enable", "disable"]  # Enable/disable overflow IE detection | Default: disable
    malformed_ht_ie: Literal["enable", "disable"]  # Enable/disable malformed HT IE detection | Default: disable
    malformed_auth: Literal["enable", "disable"]  # Enable/disable malformed auth frame detection | Default: disable
    malformed_association: Literal["enable", "disable"]  # Enable/disable malformed association request detec | Default: disable
    ht_40mhz_intolerance: Literal["enable", "disable"]  # Enable/disable HT 40 MHz intolerance detection | Default: disable
    valid_ssid_misuse: Literal["enable", "disable"]  # Enable/disable valid SSID misuse detection | Default: disable
    valid_client_misassociation: Literal["enable", "disable"]  # Enable/disable valid client misassociation detecti | Default: disable
    hotspotter_attack: Literal["enable", "disable"]  # Enable/disable hotspotter attack detection | Default: disable
    pwsave_dos_attack: Literal["enable", "disable"]  # Enable/disable power save DOS attack detection | Default: disable
    omerta_attack: Literal["enable", "disable"]  # Enable/disable omerta attack detection | Default: disable
    disconnect_station: Literal["enable", "disable"]  # Enable/disable disconnect station detection | Default: disable
    unencrypted_valid: Literal["enable", "disable"]  # Enable/disable unencrypted valid detection | Default: disable
    fata_jack: Literal["enable", "disable"]  # Enable/disable FATA-Jack detection | Default: disable
    risky_encryption: Literal["enable", "disable"]  # Enable/disable Risky Encryption detection | Default: disable
    fuzzed_beacon: Literal["enable", "disable"]  # Enable/disable fuzzed beacon detection | Default: disable
    fuzzed_probe_request: Literal["enable", "disable"]  # Enable/disable fuzzed probe request detection | Default: disable
    fuzzed_probe_response: Literal["enable", "disable"]  # Enable/disable fuzzed probe response detection | Default: disable
    air_jack: Literal["enable", "disable"]  # Enable/disable AirJack detection | Default: disable
    wpa_ft_attack: Literal["enable", "disable"]  # Enable/disable WPA FT attack detection | Default: disable


@final
class WidsProfileObject:
    """Typed FortiObject for wireless_controller/wids_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WIDS profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 63
    comment: str
    # Scan nearby WiFi stations (default = disable). | Default: disable
    sensor_mode: Literal["disable", "foreign", "both"]
    # Enable/disable rogue AP detection. | Default: disable
    ap_scan: Literal["disable", "enable"]
    # Selected ap scan channel list for 2.4G and 5G bands.
    ap_scan_channel_list_2G_5G: list[WidsProfileApscanchannellist2g5gObject]
    # Selected ap scan channel list for 6G band.
    ap_scan_channel_list_6G: list[WidsProfileApscanchannellist6gObject]
    # Period between background scans | Default: 600 | Min: 10 | Max: 3600
    ap_bgscan_period: int
    # Period between successive channel scans | Default: 3 | Min: 1 | Max: 600
    ap_bgscan_intv: int
    # Listen time on scanning a channel | Default: 30 | Min: 10 | Max: 1000
    ap_bgscan_duration: int
    # Wait time for channel inactivity before scanning this channe | Default: 20 | Min: 0 | Max: 1000
    ap_bgscan_idle: int
    # Period between background scan reports | Default: 30 | Min: 15 | Max: 600
    ap_bgscan_report_intv: int
    # Firewall schedules for turning off FortiAP radio background
    ap_bgscan_disable_schedules: list[WidsProfileApbgscandisableschedulesObject]
    # Period between foreground scan reports | Default: 15 | Min: 15 | Max: 600
    ap_fgscan_report_intv: int
    # Enable/disable passive scanning. Enable means do not send pr | Default: disable
    ap_scan_passive: Literal["enable", "disable"]
    # Minimum signal level/threshold in dBm required for the AP to | Default: -90 | MaxLen: 7
    ap_scan_threshold: str
    # Enable/disable on-wire rogue AP auto-suppression | Default: disable
    ap_auto_suppress: Literal["enable", "disable"]
    # Enable/disable wireless bridge detection (default = disable) | Default: disable
    wireless_bridge: Literal["enable", "disable"]
    # Enable/disable broadcasting de-authentication detection | Default: disable
    deauth_broadcast: Literal["enable", "disable"]
    # Enable/disable null SSID probe response detection | Default: disable
    null_ssid_probe_resp: Literal["enable", "disable"]
    # Enable/disable long duration attack detection based on user | Default: disable
    long_duration_attack: Literal["enable", "disable"]
    # Threshold value for long duration attack detection | Default: 8200 | Min: 1000 | Max: 32767
    long_duration_thresh: int
    # Enable/disable invalid MAC OUI detection. | Default: disable
    invalid_mac_oui: Literal["enable", "disable"]
    # Enable/disable weak WEP IV (Initialization Vector) detection | Default: disable
    weak_wep_iv: Literal["enable", "disable"]
    # Enable/disable authentication frame flooding detection | Default: disable
    auth_frame_flood: Literal["enable", "disable"]
    # Number of seconds after which a station is considered not co | Default: 10 | Min: 5 | Max: 120
    auth_flood_time: int
    # The threshold value for authentication frame flooding. | Default: 30 | Min: 1 | Max: 100
    auth_flood_thresh: int
    # Enable/disable association frame flooding detection | Default: disable
    assoc_frame_flood: Literal["enable", "disable"]
    # Number of seconds after which a station is considered not co | Default: 10 | Min: 5 | Max: 120
    assoc_flood_time: int
    # The threshold value for association frame flooding. | Default: 30 | Min: 1 | Max: 100
    assoc_flood_thresh: int
    # Enable/disable reassociation flood detection | Default: disable
    reassoc_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    reassoc_flood_time: int
    # The threshold value for reassociation flood. | Default: 30 | Min: 1 | Max: 65100
    reassoc_flood_thresh: int
    # Enable/disable probe flood detection (default = disable). | Default: disable
    probe_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    probe_flood_time: int
    # The threshold value for probe flood. | Default: 30 | Min: 1 | Max: 65100
    probe_flood_thresh: int
    # Enable/disable bcn flood detection (default = disable). | Default: disable
    bcn_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    bcn_flood_time: int
    # The threshold value for bcn flood. | Default: 15 | Min: 1 | Max: 65100
    bcn_flood_thresh: int
    # Enable/disable rts flood detection (default = disable). | Default: disable
    rts_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    rts_flood_time: int
    # The threshold value for rts flood. | Default: 30 | Min: 1 | Max: 65100
    rts_flood_thresh: int
    # Enable/disable cts flood detection (default = disable). | Default: disable
    cts_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    cts_flood_time: int
    # The threshold value for cts flood. | Default: 30 | Min: 1 | Max: 65100
    cts_flood_thresh: int
    # Enable/disable client flood detection (default = disable). | Default: disable
    client_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 10 | Min: 1 | Max: 120
    client_flood_time: int
    # The threshold value for client flood. | Default: 30 | Min: 1 | Max: 65100
    client_flood_thresh: int
    # Enable/disable block_ack flood detection (default = disable) | Default: disable
    block_ack_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    block_ack_flood_time: int
    # The threshold value for block_ack flood. | Default: 50 | Min: 1 | Max: 65100
    block_ack_flood_thresh: int
    # Enable/disable pspoll flood detection (default = disable). | Default: disable
    pspoll_flood: Literal["enable", "disable"]
    # Detection Window Period. | Default: 1 | Min: 1 | Max: 120
    pspoll_flood_time: int
    # The threshold value for pspoll flood. | Default: 30 | Min: 1 | Max: 65100
    pspoll_flood_thresh: int
    # Enable/disable netstumbler detection (default = disable). | Default: disable
    netstumbler: Literal["enable", "disable"]
    # Detection Window Period. | Default: 30 | Min: 1 | Max: 120
    netstumbler_time: int
    # The threshold value for netstumbler. | Default: 5 | Min: 1 | Max: 65100
    netstumbler_thresh: int
    # Enable/disable wellenreiter detection (default = disable). | Default: disable
    wellenreiter: Literal["enable", "disable"]
    # Detection Window Period. | Default: 30 | Min: 1 | Max: 120
    wellenreiter_time: int
    # The threshold value for wellenreiter. | Default: 5 | Min: 1 | Max: 65100
    wellenreiter_thresh: int
    # Enable/disable spoofed de-authentication attack detection | Default: disable
    spoofed_deauth: Literal["enable", "disable"]
    # Enable/disable asleap attack detection (default = disable). | Default: disable
    asleap_attack: Literal["enable", "disable"]
    # Enable/disable EAPOL-Start flooding (to AP) detection | Default: disable
    eapol_start_flood: Literal["enable", "disable"]
    # The threshold value for EAPOL-Start flooding in specified in | Default: 10 | Min: 2 | Max: 100
    eapol_start_thresh: int
    # The detection interval for EAPOL-Start flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_start_intv: int
    # Enable/disable EAPOL-Logoff flooding (to AP) detection | Default: disable
    eapol_logoff_flood: Literal["enable", "disable"]
    # The threshold value for EAPOL-Logoff flooding in specified i | Default: 10 | Min: 2 | Max: 100
    eapol_logoff_thresh: int
    # The detection interval for EAPOL-Logoff flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_logoff_intv: int
    # Enable/disable EAPOL-Success flooding (to AP) detection | Default: disable
    eapol_succ_flood: Literal["enable", "disable"]
    # The threshold value for EAPOL-Success flooding in specified | Default: 10 | Min: 2 | Max: 100
    eapol_succ_thresh: int
    # The detection interval for EAPOL-Success flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_succ_intv: int
    # Enable/disable EAPOL-Failure flooding (to AP) detection | Default: disable
    eapol_fail_flood: Literal["enable", "disable"]
    # The threshold value for EAPOL-Failure flooding in specified | Default: 10 | Min: 2 | Max: 100
    eapol_fail_thresh: int
    # The detection interval for EAPOL-Failure flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_fail_intv: int
    # Enable/disable premature EAPOL-Success flooding (to STA) det | Default: disable
    eapol_pre_succ_flood: Literal["enable", "disable"]
    # The threshold value for premature EAPOL-Success flooding in | Default: 10 | Min: 2 | Max: 100
    eapol_pre_succ_thresh: int
    # The detection interval for premature EAPOL-Success flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_pre_succ_intv: int
    # Enable/disable premature EAPOL-Failure flooding (to STA) det | Default: disable
    eapol_pre_fail_flood: Literal["enable", "disable"]
    # The threshold value for premature EAPOL-Failure flooding in | Default: 10 | Min: 2 | Max: 100
    eapol_pre_fail_thresh: int
    # The detection interval for premature EAPOL-Failure flooding | Default: 1 | Min: 1 | Max: 3600
    eapol_pre_fail_intv: int
    # Threshold value per second to deauth unknown src for DoS att | Default: 10 | Min: 0 | Max: 65535
    deauth_unknown_src_thresh: int
    # Enable/disable windows bridge detection (default = disable). | Default: disable
    windows_bridge: Literal["enable", "disable"]
    # Enable/disable broadcast dis-association detection | Default: disable
    disassoc_broadcast: Literal["enable", "disable"]
    # Enable/disable AP spoofing detection (default = disable). | Default: disable
    ap_spoofing: Literal["enable", "disable"]
    # Enable/disable channel based mitm detection | Default: disable
    chan_based_mitm: Literal["enable", "disable"]
    # Enable/disable adhoc using valid SSID detection | Default: disable
    adhoc_valid_ssid: Literal["enable", "disable"]
    # Enable/disable adhoc network detection (default = disable). | Default: disable
    adhoc_network: Literal["enable", "disable"]
    # Enable/disable overflow EAPOL key detection | Default: disable
    eapol_key_overflow: Literal["enable", "disable"]
    # Enable/disable AP impersonation detection | Default: disable
    ap_impersonation: Literal["enable", "disable"]
    # Enable/disable invalid address combination detection | Default: disable
    invalid_addr_combination: Literal["enable", "disable"]
    # Enable/disable beacon wrong channel detection | Default: disable
    beacon_wrong_channel: Literal["enable", "disable"]
    # Enable/disable HT greenfield detection (default = disable). | Default: disable
    ht_greenfield: Literal["enable", "disable"]
    # Enable/disable overflow IE detection (default = disable). | Default: disable
    overflow_ie: Literal["enable", "disable"]
    # Enable/disable malformed HT IE detection (default = disable) | Default: disable
    malformed_ht_ie: Literal["enable", "disable"]
    # Enable/disable malformed auth frame detection | Default: disable
    malformed_auth: Literal["enable", "disable"]
    # Enable/disable malformed association request detection | Default: disable
    malformed_association: Literal["enable", "disable"]
    # Enable/disable HT 40 MHz intolerance detection | Default: disable
    ht_40mhz_intolerance: Literal["enable", "disable"]
    # Enable/disable valid SSID misuse detection | Default: disable
    valid_ssid_misuse: Literal["enable", "disable"]
    # Enable/disable valid client misassociation detection | Default: disable
    valid_client_misassociation: Literal["enable", "disable"]
    # Enable/disable hotspotter attack detection | Default: disable
    hotspotter_attack: Literal["enable", "disable"]
    # Enable/disable power save DOS attack detection | Default: disable
    pwsave_dos_attack: Literal["enable", "disable"]
    # Enable/disable omerta attack detection (default = disable). | Default: disable
    omerta_attack: Literal["enable", "disable"]
    # Enable/disable disconnect station detection | Default: disable
    disconnect_station: Literal["enable", "disable"]
    # Enable/disable unencrypted valid detection | Default: disable
    unencrypted_valid: Literal["enable", "disable"]
    # Enable/disable FATA-Jack detection (default = disable). | Default: disable
    fata_jack: Literal["enable", "disable"]
    # Enable/disable Risky Encryption detection | Default: disable
    risky_encryption: Literal["enable", "disable"]
    # Enable/disable fuzzed beacon detection (default = disable). | Default: disable
    fuzzed_beacon: Literal["enable", "disable"]
    # Enable/disable fuzzed probe request detection | Default: disable
    fuzzed_probe_request: Literal["enable", "disable"]
    # Enable/disable fuzzed probe response detection | Default: disable
    fuzzed_probe_response: Literal["enable", "disable"]
    # Enable/disable AirJack detection (default = disable). | Default: disable
    air_jack: Literal["enable", "disable"]
    # Enable/disable WPA FT attack detection (default = disable). | Default: disable
    wpa_ft_attack: Literal["enable", "disable"]
    
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
    def to_dict(self) -> WidsProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class WidsProfile:
    """
    Configure wireless intrusion detection system (WIDS) profiles.
    
    Path: wireless_controller/wids_profile
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
    ) -> WidsProfileObject: ...
    
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
    ) -> WidsProfileObject: ...
    
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
    ) -> FortiObjectList[WidsProfileObject]: ...
    
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
    ) -> WidsProfileObject: ...
    
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
    ) -> WidsProfileObject: ...
    
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
    ) -> FortiObjectList[WidsProfileObject]: ...
    
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
    ) -> WidsProfileObject: ...
    
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
    ) -> WidsProfileObject: ...
    
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
    ) -> FortiObjectList[WidsProfileObject]: ...
    
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
    ) -> WidsProfileObject | list[WidsProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> WidsProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> WidsProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WidsProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: WidsProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        sensor_mode: Literal["disable", "foreign", "both"] | None = ...,
        ap_scan: Literal["disable", "enable"] | None = ...,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_bgscan_period: int | None = ...,
        ap_bgscan_intv: int | None = ...,
        ap_bgscan_duration: int | None = ...,
        ap_bgscan_idle: int | None = ...,
        ap_bgscan_report_intv: int | None = ...,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = ...,
        ap_fgscan_report_intv: int | None = ...,
        ap_scan_passive: Literal["enable", "disable"] | None = ...,
        ap_scan_threshold: str | None = ...,
        ap_auto_suppress: Literal["enable", "disable"] | None = ...,
        wireless_bridge: Literal["enable", "disable"] | None = ...,
        deauth_broadcast: Literal["enable", "disable"] | None = ...,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = ...,
        long_duration_attack: Literal["enable", "disable"] | None = ...,
        long_duration_thresh: int | None = ...,
        invalid_mac_oui: Literal["enable", "disable"] | None = ...,
        weak_wep_iv: Literal["enable", "disable"] | None = ...,
        auth_frame_flood: Literal["enable", "disable"] | None = ...,
        auth_flood_time: int | None = ...,
        auth_flood_thresh: int | None = ...,
        assoc_frame_flood: Literal["enable", "disable"] | None = ...,
        assoc_flood_time: int | None = ...,
        assoc_flood_thresh: int | None = ...,
        reassoc_flood: Literal["enable", "disable"] | None = ...,
        reassoc_flood_time: int | None = ...,
        reassoc_flood_thresh: int | None = ...,
        probe_flood: Literal["enable", "disable"] | None = ...,
        probe_flood_time: int | None = ...,
        probe_flood_thresh: int | None = ...,
        bcn_flood: Literal["enable", "disable"] | None = ...,
        bcn_flood_time: int | None = ...,
        bcn_flood_thresh: int | None = ...,
        rts_flood: Literal["enable", "disable"] | None = ...,
        rts_flood_time: int | None = ...,
        rts_flood_thresh: int | None = ...,
        cts_flood: Literal["enable", "disable"] | None = ...,
        cts_flood_time: int | None = ...,
        cts_flood_thresh: int | None = ...,
        client_flood: Literal["enable", "disable"] | None = ...,
        client_flood_time: int | None = ...,
        client_flood_thresh: int | None = ...,
        block_ack_flood: Literal["enable", "disable"] | None = ...,
        block_ack_flood_time: int | None = ...,
        block_ack_flood_thresh: int | None = ...,
        pspoll_flood: Literal["enable", "disable"] | None = ...,
        pspoll_flood_time: int | None = ...,
        pspoll_flood_thresh: int | None = ...,
        netstumbler: Literal["enable", "disable"] | None = ...,
        netstumbler_time: int | None = ...,
        netstumbler_thresh: int | None = ...,
        wellenreiter: Literal["enable", "disable"] | None = ...,
        wellenreiter_time: int | None = ...,
        wellenreiter_thresh: int | None = ...,
        spoofed_deauth: Literal["enable", "disable"] | None = ...,
        asleap_attack: Literal["enable", "disable"] | None = ...,
        eapol_start_flood: Literal["enable", "disable"] | None = ...,
        eapol_start_thresh: int | None = ...,
        eapol_start_intv: int | None = ...,
        eapol_logoff_flood: Literal["enable", "disable"] | None = ...,
        eapol_logoff_thresh: int | None = ...,
        eapol_logoff_intv: int | None = ...,
        eapol_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_succ_thresh: int | None = ...,
        eapol_succ_intv: int | None = ...,
        eapol_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_fail_thresh: int | None = ...,
        eapol_fail_intv: int | None = ...,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_succ_thresh: int | None = ...,
        eapol_pre_succ_intv: int | None = ...,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = ...,
        eapol_pre_fail_thresh: int | None = ...,
        eapol_pre_fail_intv: int | None = ...,
        deauth_unknown_src_thresh: int | None = ...,
        windows_bridge: Literal["enable", "disable"] | None = ...,
        disassoc_broadcast: Literal["enable", "disable"] | None = ...,
        ap_spoofing: Literal["enable", "disable"] | None = ...,
        chan_based_mitm: Literal["enable", "disable"] | None = ...,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = ...,
        adhoc_network: Literal["enable", "disable"] | None = ...,
        eapol_key_overflow: Literal["enable", "disable"] | None = ...,
        ap_impersonation: Literal["enable", "disable"] | None = ...,
        invalid_addr_combination: Literal["enable", "disable"] | None = ...,
        beacon_wrong_channel: Literal["enable", "disable"] | None = ...,
        ht_greenfield: Literal["enable", "disable"] | None = ...,
        overflow_ie: Literal["enable", "disable"] | None = ...,
        malformed_ht_ie: Literal["enable", "disable"] | None = ...,
        malformed_auth: Literal["enable", "disable"] | None = ...,
        malformed_association: Literal["enable", "disable"] | None = ...,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = ...,
        valid_ssid_misuse: Literal["enable", "disable"] | None = ...,
        valid_client_misassociation: Literal["enable", "disable"] | None = ...,
        hotspotter_attack: Literal["enable", "disable"] | None = ...,
        pwsave_dos_attack: Literal["enable", "disable"] | None = ...,
        omerta_attack: Literal["enable", "disable"] | None = ...,
        disconnect_station: Literal["enable", "disable"] | None = ...,
        unencrypted_valid: Literal["enable", "disable"] | None = ...,
        fata_jack: Literal["enable", "disable"] | None = ...,
        risky_encryption: Literal["enable", "disable"] | None = ...,
        fuzzed_beacon: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_request: Literal["enable", "disable"] | None = ...,
        fuzzed_probe_response: Literal["enable", "disable"] | None = ...,
        air_jack: Literal["enable", "disable"] | None = ...,
        wpa_ft_attack: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
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
    "WidsProfile",
    "WidsProfilePayload",
    "WidsProfileResponse",
    "WidsProfileObject",
]
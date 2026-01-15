from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/global_ payload fields.
    
    Configure wireless controller global settings.
    
    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name of the wireless controller. | MaxLen: 35
    location: str  # Description of the location of the wireless contro | MaxLen: 35
    acd_process_count: int  # Configure the number cw_acd daemons for multi-core | Default: 0 | Min: 0 | Max: 255
    wpad_process_count: int  # Wpad daemon process count for multi-core CPU suppo | Default: 0 | Min: 0 | Max: 255
    image_download: Literal["enable", "disable"]  # Enable/disable WTP image download at join time. | Default: enable
    rolling_wtp_upgrade: Literal["enable", "disable"]  # Enable/disable rolling WTP upgrade | Default: disable
    rolling_wtp_upgrade_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -80 | MaxLen: 7
    max_retransmit: int  # Maximum number of tunnel packet retransmissions | Default: 3 | Min: 0 | Max: 64
    control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]  # Configure CAPWAP control message data channel offl | Default: ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis
    data_ethernet_II: Literal["enable", "disable"]  # Configure the wireless controller to use Ethernet | Default: enable
    link_aggregation: Literal["enable", "disable"]  # Enable/disable calculating the CAPWAP transmit has | Default: disable
    mesh_eth_type: int  # Mesh Ethernet identifier included in backhaul pack | Default: 8755 | Min: 0 | Max: 65535
    fiapp_eth_type: int  # Ethernet type for Fortinet Inter-Access Point Prot | Default: 5252 | Min: 0 | Max: 65535
    discovery_mc_addr: str  # Multicast IP address for AP discovery | Default: 224.0.1.140
    discovery_mc_addr6: str  # Multicast IPv6 address for AP discovery | Default: ff02::18c
    max_clients: int  # Maximum number of clients that can connect simulta | Default: 0 | Min: 0 | Max: 4294967295
    rogue_scan_mac_adjacency: int  # Maximum numerical difference between an AP's Ether | Default: 7 | Min: 0 | Max: 31
    ipsec_base_ip: str  # Base IP address for IPsec VPN tunnels between the | Default: 169.254.0.1
    wtp_share: Literal["enable", "disable"]  # Enable/disable sharing of WTPs between VDOMs. | Default: disable
    tunnel_mode: Literal["compatible", "strict"]  # Compatible/strict tunnel mode. | Default: compatible
    nac_interval: int  # Interval in seconds between two WiFi network acces | Default: 120 | Min: 10 | Max: 600
    ap_log_server: Literal["enable", "disable"]  # Enable/disable configuring FortiGate to redirect w | Default: disable
    ap_log_server_ip: str  # IP address that FortiGate or FortiAPs send log mes | Default: 0.0.0.0
    ap_log_server_port: int  # Port that FortiGate or FortiAPs send log messages | Default: 0 | Min: 0 | Max: 65535
    max_sta_offline: int  # Maximum number of station offline stored on the co | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_offline_ip2mac: int  # Maximum number of station offline ip2mac stored on | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_cap: int  # Maximum number of station cap stored on the contro | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_cap_wtp: int  # Maximum number of station cap's wtp info stored on | Default: 8 | Min: 1 | Max: 8
    max_rogue_ap: int  # Maximum number of rogue APs stored on the controll | Default: 0 | Min: 0 | Max: 4294967295
    max_rogue_ap_wtp: int  # Maximum number of rogue AP's wtp info stored on th | Default: 16 | Min: 1 | Max: 16
    max_rogue_sta: int  # Maximum number of rogue stations stored on the con | Default: 0 | Min: 0 | Max: 4294967295
    max_wids_entry: int  # Maximum number of wids entries stored on the contr | Default: 0 | Min: 0 | Max: 4294967295
    max_ble_device: int  # Maximum number of BLE devices stored on the contro | Default: 0 | Min: 0 | Max: 4294967295

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class GlobalResponse(TypedDict):
    """
    Type hints for wireless_controller/global_ API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name of the wireless controller. | MaxLen: 35
    location: str  # Description of the location of the wireless contro | MaxLen: 35
    acd_process_count: int  # Configure the number cw_acd daemons for multi-core | Default: 0 | Min: 0 | Max: 255
    wpad_process_count: int  # Wpad daemon process count for multi-core CPU suppo | Default: 0 | Min: 0 | Max: 255
    image_download: Literal["enable", "disable"]  # Enable/disable WTP image download at join time. | Default: enable
    rolling_wtp_upgrade: Literal["enable", "disable"]  # Enable/disable rolling WTP upgrade | Default: disable
    rolling_wtp_upgrade_threshold: str  # Minimum signal level/threshold in dBm required for | Default: -80 | MaxLen: 7
    max_retransmit: int  # Maximum number of tunnel packet retransmissions | Default: 3 | Min: 0 | Max: 64
    control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]  # Configure CAPWAP control message data channel offl | Default: ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis
    data_ethernet_II: Literal["enable", "disable"]  # Configure the wireless controller to use Ethernet | Default: enable
    link_aggregation: Literal["enable", "disable"]  # Enable/disable calculating the CAPWAP transmit has | Default: disable
    mesh_eth_type: int  # Mesh Ethernet identifier included in backhaul pack | Default: 8755 | Min: 0 | Max: 65535
    fiapp_eth_type: int  # Ethernet type for Fortinet Inter-Access Point Prot | Default: 5252 | Min: 0 | Max: 65535
    discovery_mc_addr: str  # Multicast IP address for AP discovery | Default: 224.0.1.140
    discovery_mc_addr6: str  # Multicast IPv6 address for AP discovery | Default: ff02::18c
    max_clients: int  # Maximum number of clients that can connect simulta | Default: 0 | Min: 0 | Max: 4294967295
    rogue_scan_mac_adjacency: int  # Maximum numerical difference between an AP's Ether | Default: 7 | Min: 0 | Max: 31
    ipsec_base_ip: str  # Base IP address for IPsec VPN tunnels between the | Default: 169.254.0.1
    wtp_share: Literal["enable", "disable"]  # Enable/disable sharing of WTPs between VDOMs. | Default: disable
    tunnel_mode: Literal["compatible", "strict"]  # Compatible/strict tunnel mode. | Default: compatible
    nac_interval: int  # Interval in seconds between two WiFi network acces | Default: 120 | Min: 10 | Max: 600
    ap_log_server: Literal["enable", "disable"]  # Enable/disable configuring FortiGate to redirect w | Default: disable
    ap_log_server_ip: str  # IP address that FortiGate or FortiAPs send log mes | Default: 0.0.0.0
    ap_log_server_port: int  # Port that FortiGate or FortiAPs send log messages | Default: 0 | Min: 0 | Max: 65535
    max_sta_offline: int  # Maximum number of station offline stored on the co | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_offline_ip2mac: int  # Maximum number of station offline ip2mac stored on | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_cap: int  # Maximum number of station cap stored on the contro | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_cap_wtp: int  # Maximum number of station cap's wtp info stored on | Default: 8 | Min: 1 | Max: 8
    max_rogue_ap: int  # Maximum number of rogue APs stored on the controll | Default: 0 | Min: 0 | Max: 4294967295
    max_rogue_ap_wtp: int  # Maximum number of rogue AP's wtp info stored on th | Default: 16 | Min: 1 | Max: 16
    max_rogue_sta: int  # Maximum number of rogue stations stored on the con | Default: 0 | Min: 0 | Max: 4294967295
    max_wids_entry: int  # Maximum number of wids entries stored on the contr | Default: 0 | Min: 0 | Max: 4294967295
    max_ble_device: int  # Maximum number of BLE devices stored on the contro | Default: 0 | Min: 0 | Max: 4294967295


@final
class GlobalObject:
    """Typed FortiObject for wireless_controller/global_ with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name of the wireless controller. | MaxLen: 35
    name: str
    # Description of the location of the wireless controller. | MaxLen: 35
    location: str
    # Configure the number cw_acd daemons for multi-core CPU suppo | Default: 0 | Min: 0 | Max: 255
    acd_process_count: int
    # Wpad daemon process count for multi-core CPU support. | Default: 0 | Min: 0 | Max: 255
    wpad_process_count: int
    # Enable/disable WTP image download at join time. | Default: enable
    image_download: Literal["enable", "disable"]
    # Enable/disable rolling WTP upgrade (default = disable). | Default: disable
    rolling_wtp_upgrade: Literal["enable", "disable"]
    # Minimum signal level/threshold in dBm required for the manag | Default: -80 | MaxLen: 7
    rolling_wtp_upgrade_threshold: str
    # Maximum number of tunnel packet retransmissions | Default: 3 | Min: 0 | Max: 64
    max_retransmit: int
    # Configure CAPWAP control message data channel offload. | Default: ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis
    control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"]
    # Configure the wireless controller to use Ethernet II or 802. | Default: enable
    data_ethernet_II: Literal["enable", "disable"]
    # Enable/disable calculating the CAPWAP transmit hash to load | Default: disable
    link_aggregation: Literal["enable", "disable"]
    # Mesh Ethernet identifier included in backhaul packets | Default: 8755 | Min: 0 | Max: 65535
    mesh_eth_type: int
    # Ethernet type for Fortinet Inter-Access Point Protocol | Default: 5252 | Min: 0 | Max: 65535
    fiapp_eth_type: int
    # Multicast IP address for AP discovery | Default: 224.0.1.140
    discovery_mc_addr: str
    # Multicast IPv6 address for AP discovery | Default: ff02::18c
    discovery_mc_addr6: str
    # Maximum number of clients that can connect simultaneously | Default: 0 | Min: 0 | Max: 4294967295
    max_clients: int
    # Maximum numerical difference between an AP's Ethernet and wi | Default: 7 | Min: 0 | Max: 31
    rogue_scan_mac_adjacency: int
    # Base IP address for IPsec VPN tunnels between the access poi | Default: 169.254.0.1
    ipsec_base_ip: str
    # Enable/disable sharing of WTPs between VDOMs. | Default: disable
    wtp_share: Literal["enable", "disable"]
    # Compatible/strict tunnel mode. | Default: compatible
    tunnel_mode: Literal["compatible", "strict"]
    # Interval in seconds between two WiFi network access control | Default: 120 | Min: 10 | Max: 600
    nac_interval: int
    # Enable/disable configuring FortiGate to redirect wireless ev | Default: disable
    ap_log_server: Literal["enable", "disable"]
    # IP address that FortiGate or FortiAPs send log messages to. | Default: 0.0.0.0
    ap_log_server_ip: str
    # Port that FortiGate or FortiAPs send log messages to. | Default: 0 | Min: 0 | Max: 65535
    ap_log_server_port: int
    # Maximum number of station offline stored on the controller | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_offline: int
    # Maximum number of station offline ip2mac stored on the contr | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_offline_ip2mac: int
    # Maximum number of station cap stored on the controller | Default: 0 | Min: 0 | Max: 4294967295
    max_sta_cap: int
    # Maximum number of station cap's wtp info stored on the contr | Default: 8 | Min: 1 | Max: 8
    max_sta_cap_wtp: int
    # Maximum number of rogue APs stored on the controller | Default: 0 | Min: 0 | Max: 4294967295
    max_rogue_ap: int
    # Maximum number of rogue AP's wtp info stored on the controll | Default: 16 | Min: 1 | Max: 16
    max_rogue_ap_wtp: int
    # Maximum number of rogue stations stored on the controller | Default: 0 | Min: 0 | Max: 4294967295
    max_rogue_sta: int
    # Maximum number of wids entries stored on the controller | Default: 0 | Min: 0 | Max: 4294967295
    max_wids_entry: int
    # Maximum number of BLE devices stored on the controller | Default: 0 | Min: 0 | Max: 4294967295
    max_ble_device: int
    
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
    Configure wireless controller global settings.
    
    Path: wireless_controller/global_
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        discovery_mc_addr6: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        discovery_mc_addr6: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        discovery_mc_addr6: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        discovery_mc_addr6: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        discovery_mc_addr6: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GlobalPayload | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        acd_process_count: int | None = ...,
        wpad_process_count: int | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade: Literal["enable", "disable"] | None = ...,
        rolling_wtp_upgrade_threshold: str | None = ...,
        max_retransmit: int | None = ...,
        control_message_offload: Literal["ebp-frame", "aeroscout-tag", "ap-list", "sta-list", "sta-cap-list", "stats", "aeroscout-mu", "sta-health", "spectral-analysis"] | list[str] | None = ...,
        data_ethernet_II: Literal["enable", "disable"] | None = ...,
        link_aggregation: Literal["enable", "disable"] | None = ...,
        mesh_eth_type: int | None = ...,
        fiapp_eth_type: int | None = ...,
        discovery_mc_addr: str | None = ...,
        discovery_mc_addr6: str | None = ...,
        max_clients: int | None = ...,
        rogue_scan_mac_adjacency: int | None = ...,
        ipsec_base_ip: str | None = ...,
        wtp_share: Literal["enable", "disable"] | None = ...,
        tunnel_mode: Literal["compatible", "strict"] | None = ...,
        nac_interval: int | None = ...,
        ap_log_server: Literal["enable", "disable"] | None = ...,
        ap_log_server_ip: str | None = ...,
        ap_log_server_port: int | None = ...,
        max_sta_offline: int | None = ...,
        max_sta_offline_ip2mac: int | None = ...,
        max_sta_cap: int | None = ...,
        max_sta_cap_wtp: int | None = ...,
        max_rogue_ap: int | None = ...,
        max_rogue_ap_wtp: int | None = ...,
        max_rogue_sta: int | None = ...,
        max_wids_entry: int | None = ...,
        max_ble_device: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
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
    "Global",
    "GlobalPayload",
    "GlobalResponse",
    "GlobalObject",
]
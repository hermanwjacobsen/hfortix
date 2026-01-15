from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WtpPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wtp payload fields.
    
    Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.wireless-controller.apcfg-profile.ApcfgProfileEndpoint` (via: apcfg-profile)
        - :class:`~.wireless-controller.bonjour-profile.BonjourProfileEndpoint` (via: bonjour-profile)
        - :class:`~.wireless-controller.region.RegionEndpoint` (via: region)
        - :class:`~.wireless-controller.wtp-profile.WtpProfileEndpoint` (via: wtp-profile)

    **Usage:**
        payload: WtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    wtp_id: str  # WTP ID. | MaxLen: 35
    index: int  # Index (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    admin: Literal["discovered", "disable", "enable"]  # Configure how the FortiGate operating as a wireles | Default: enable
    name: str  # WTP, AP or FortiAP configuration name. | MaxLen: 35
    location: str  # Field for describing the physical location of the | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    region: str  # Region name WTP is associated with. | MaxLen: 35
    region_x: str  # Relative horizontal region coordinate | Default: 0 | MaxLen: 15
    region_y: str  # Relative vertical region coordinate | Default: 0 | MaxLen: 15
    firmware_provision: str  # Firmware version to provision to this FortiAP on b | MaxLen: 35
    firmware_provision_latest: Literal["disable", "once"]  # Enable/disable one-time automatic provisioning of | Default: disable
    wtp_profile: str  # WTP profile name to apply to this WTP, AP or Forti | MaxLen: 35
    apcfg_profile: str  # AP local configuration profile name. | MaxLen: 35
    bonjour_profile: str  # Bonjour profile name. | MaxLen: 35
    ble_major_id: int  # Override BLE Major ID. | Default: 0 | Min: 0 | Max: 65535
    ble_minor_id: int  # Override BLE Minor ID. | Default: 0 | Min: 0 | Max: 65535
    override_led_state: Literal["enable", "disable"]  # Enable to override the profile LED state setting f | Default: disable
    led_state: Literal["enable", "disable"]  # Enable to allow the FortiAPs LEDs to light. Disabl | Default: enable
    override_wan_port_mode: Literal["enable", "disable"]  # Enable/disable overriding the wan-port-mode in the | Default: disable
    wan_port_mode: Literal["wan-lan", "wan-only"]  # Enable/disable using the FortiAP WAN port as a LAN | Default: wan-only
    override_ip_fragment: Literal["enable", "disable"]  # Enable/disable overriding the WTP profile IP fragm | Default: disable
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]  # Method(s) by which IP fragmentation is prevented f | Default: tcp-mss-adjust
    tun_mtu_uplink: int  # The maximum transmission unit (MTU) of uplink CAPW | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_downlink: int  # The MTU of downlink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    override_split_tunnel: Literal["enable", "disable"]  # Enable/disable overriding the WTP profile split tu | Default: disable
    split_tunneling_acl_path: Literal["tunnel", "local"]  # Split tunneling ACL path is local/tunnel. | Default: local
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]  # Enable/disable automatically adding local subnetwo | Default: disable
    split_tunneling_acl: list[dict[str, Any]]  # Split tunneling ACL filter list.
    override_lan: Literal["enable", "disable"]  # Enable to override the WTP profile LAN port settin | Default: disable
    lan: str  # WTP LAN port mapping.
    override_allowaccess: Literal["enable", "disable"]  # Enable to override the WTP profile management acce | Default: disable
    allowaccess: Literal["https", "ssh", "snmp"]  # Control management access to the managed WTP, Fort
    override_login_passwd_change: Literal["enable", "disable"]  # Enable to override the WTP profile login-password | Default: disable
    login_passwd_change: Literal["yes", "default", "no"]  # Change or reset the administrator password of a ma | Default: no
    login_passwd: str  # Set the managed WTP, FortiAP, or AP's administrato | MaxLen: 128
    override_default_mesh_root: Literal["enable", "disable"]  # Enable to override the WTP profile default mesh ro | Default: disable
    default_mesh_root: Literal["enable", "disable"]  # Configure default mesh root SSID when it is not in | Default: disable
    radio_1: str  # Configuration options for radio 1.
    radio_2: str  # Configuration options for radio 2.
    radio_3: str  # Configuration options for radio 3.
    radio_4: str  # Configuration options for radio 4.
    image_download: Literal["enable", "disable"]  # Enable/disable WTP image download. | Default: enable
    mesh_bridge_enable: Literal["default", "enable", "disable"]  # Enable/disable mesh Ethernet bridge when WTP is co | Default: default
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # Purdue Level of this WTP. | Default: 3
    coordinate_latitude: str  # WTP latitude coordinate. | MaxLen: 19
    coordinate_longitude: str  # WTP longitude coordinate. | MaxLen: 19

# Nested TypedDicts for table field children (dict mode)

class WtpSplittunnelingaclItem(TypedDict):
    """Type hints for split-tunneling-acl table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    dest_ip: str  # Destination IP and mask for the split-tunneling su | Default: 0.0.0.0 0.0.0.0


# Nested classes for table field children (object mode)

@final
class WtpSplittunnelingaclObject:
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
class WtpResponse(TypedDict):
    """
    Type hints for wireless_controller/wtp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    wtp_id: str  # WTP ID. | MaxLen: 35
    index: int  # Index (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    admin: Literal["discovered", "disable", "enable"]  # Configure how the FortiGate operating as a wireles | Default: enable
    name: str  # WTP, AP or FortiAP configuration name. | MaxLen: 35
    location: str  # Field for describing the physical location of the | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    region: str  # Region name WTP is associated with. | MaxLen: 35
    region_x: str  # Relative horizontal region coordinate | Default: 0 | MaxLen: 15
    region_y: str  # Relative vertical region coordinate | Default: 0 | MaxLen: 15
    firmware_provision: str  # Firmware version to provision to this FortiAP on b | MaxLen: 35
    firmware_provision_latest: Literal["disable", "once"]  # Enable/disable one-time automatic provisioning of | Default: disable
    wtp_profile: str  # WTP profile name to apply to this WTP, AP or Forti | MaxLen: 35
    apcfg_profile: str  # AP local configuration profile name. | MaxLen: 35
    bonjour_profile: str  # Bonjour profile name. | MaxLen: 35
    ble_major_id: int  # Override BLE Major ID. | Default: 0 | Min: 0 | Max: 65535
    ble_minor_id: int  # Override BLE Minor ID. | Default: 0 | Min: 0 | Max: 65535
    override_led_state: Literal["enable", "disable"]  # Enable to override the profile LED state setting f | Default: disable
    led_state: Literal["enable", "disable"]  # Enable to allow the FortiAPs LEDs to light. Disabl | Default: enable
    override_wan_port_mode: Literal["enable", "disable"]  # Enable/disable overriding the wan-port-mode in the | Default: disable
    wan_port_mode: Literal["wan-lan", "wan-only"]  # Enable/disable using the FortiAP WAN port as a LAN | Default: wan-only
    override_ip_fragment: Literal["enable", "disable"]  # Enable/disable overriding the WTP profile IP fragm | Default: disable
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]  # Method(s) by which IP fragmentation is prevented f | Default: tcp-mss-adjust
    tun_mtu_uplink: int  # The maximum transmission unit (MTU) of uplink CAPW | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_downlink: int  # The MTU of downlink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    override_split_tunnel: Literal["enable", "disable"]  # Enable/disable overriding the WTP profile split tu | Default: disable
    split_tunneling_acl_path: Literal["tunnel", "local"]  # Split tunneling ACL path is local/tunnel. | Default: local
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]  # Enable/disable automatically adding local subnetwo | Default: disable
    split_tunneling_acl: list[WtpSplittunnelingaclItem]  # Split tunneling ACL filter list.
    override_lan: Literal["enable", "disable"]  # Enable to override the WTP profile LAN port settin | Default: disable
    lan: str  # WTP LAN port mapping.
    override_allowaccess: Literal["enable", "disable"]  # Enable to override the WTP profile management acce | Default: disable
    allowaccess: Literal["https", "ssh", "snmp"]  # Control management access to the managed WTP, Fort
    override_login_passwd_change: Literal["enable", "disable"]  # Enable to override the WTP profile login-password | Default: disable
    login_passwd_change: Literal["yes", "default", "no"]  # Change or reset the administrator password of a ma | Default: no
    login_passwd: str  # Set the managed WTP, FortiAP, or AP's administrato | MaxLen: 128
    override_default_mesh_root: Literal["enable", "disable"]  # Enable to override the WTP profile default mesh ro | Default: disable
    default_mesh_root: Literal["enable", "disable"]  # Configure default mesh root SSID when it is not in | Default: disable
    radio_1: str  # Configuration options for radio 1.
    radio_2: str  # Configuration options for radio 2.
    radio_3: str  # Configuration options for radio 3.
    radio_4: str  # Configuration options for radio 4.
    image_download: Literal["enable", "disable"]  # Enable/disable WTP image download. | Default: enable
    mesh_bridge_enable: Literal["default", "enable", "disable"]  # Enable/disable mesh Ethernet bridge when WTP is co | Default: default
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # Purdue Level of this WTP. | Default: 3
    coordinate_latitude: str  # WTP latitude coordinate. | MaxLen: 19
    coordinate_longitude: str  # WTP longitude coordinate. | MaxLen: 19


@final
class WtpObject:
    """Typed FortiObject for wireless_controller/wtp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WTP ID. | MaxLen: 35
    wtp_id: str
    # Index (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    index: int
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Configure how the FortiGate operating as a wireless controll | Default: enable
    admin: Literal["discovered", "disable", "enable"]
    # WTP, AP or FortiAP configuration name. | MaxLen: 35
    name: str
    # Field for describing the physical location of the WTP, AP or | MaxLen: 35
    location: str
    # Comment. | MaxLen: 255
    comment: str
    # Region name WTP is associated with. | MaxLen: 35
    region: str
    # Relative horizontal region coordinate (between 0 and 1). | Default: 0 | MaxLen: 15
    region_x: str
    # Relative vertical region coordinate (between 0 and 1). | Default: 0 | MaxLen: 15
    region_y: str
    # Firmware version to provision to this FortiAP on bootup | MaxLen: 35
    firmware_provision: str
    # Enable/disable one-time automatic provisioning of the latest | Default: disable
    firmware_provision_latest: Literal["disable", "once"]
    # WTP profile name to apply to this WTP, AP or FortiAP. | MaxLen: 35
    wtp_profile: str
    # AP local configuration profile name. | MaxLen: 35
    apcfg_profile: str
    # Bonjour profile name. | MaxLen: 35
    bonjour_profile: str
    # Override BLE Major ID. | Default: 0 | Min: 0 | Max: 65535
    ble_major_id: int
    # Override BLE Minor ID. | Default: 0 | Min: 0 | Max: 65535
    ble_minor_id: int
    # Enable to override the profile LED state setting for this Fo | Default: disable
    override_led_state: Literal["enable", "disable"]
    # Enable to allow the FortiAPs LEDs to light. Disable to keep | Default: enable
    led_state: Literal["enable", "disable"]
    # Enable/disable overriding the wan-port-mode in the WTP profi | Default: disable
    override_wan_port_mode: Literal["enable", "disable"]
    # Enable/disable using the FortiAP WAN port as a LAN port. | Default: wan-only
    wan_port_mode: Literal["wan-lan", "wan-only"]
    # Enable/disable overriding the WTP profile IP fragment preven | Default: disable
    override_ip_fragment: Literal["enable", "disable"]
    # Method(s) by which IP fragmentation is prevented for control | Default: tcp-mss-adjust
    ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"]
    # The maximum transmission unit (MTU) of uplink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_uplink: int
    # The MTU of downlink CAPWAP tunnel | Default: 0 | Min: 576 | Max: 1500
    tun_mtu_downlink: int
    # Enable/disable overriding the WTP profile split tunneling se | Default: disable
    override_split_tunnel: Literal["enable", "disable"]
    # Split tunneling ACL path is local/tunnel. | Default: local
    split_tunneling_acl_path: Literal["tunnel", "local"]
    # Enable/disable automatically adding local subnetwork of Fort | Default: disable
    split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"]
    # Split tunneling ACL filter list.
    split_tunneling_acl: list[WtpSplittunnelingaclObject]
    # Enable to override the WTP profile LAN port setting. | Default: disable
    override_lan: Literal["enable", "disable"]
    # WTP LAN port mapping.
    lan: str
    # Enable to override the WTP profile management access configu | Default: disable
    override_allowaccess: Literal["enable", "disable"]
    # Control management access to the managed WTP, FortiAP, or AP
    allowaccess: Literal["https", "ssh", "snmp"]
    # Enable to override the WTP profile login-password | Default: disable
    override_login_passwd_change: Literal["enable", "disable"]
    # Change or reset the administrator password of a managed WTP, | Default: no
    login_passwd_change: Literal["yes", "default", "no"]
    # Set the managed WTP, FortiAP, or AP's administrator password | MaxLen: 128
    login_passwd: str
    # Enable to override the WTP profile default mesh root SSID se | Default: disable
    override_default_mesh_root: Literal["enable", "disable"]
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
    # Enable/disable WTP image download. | Default: enable
    image_download: Literal["enable", "disable"]
    # Enable/disable mesh Ethernet bridge when WTP is configured a | Default: default
    mesh_bridge_enable: Literal["default", "enable", "disable"]
    # Purdue Level of this WTP. | Default: 3
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # WTP latitude coordinate. | MaxLen: 19
    coordinate_latitude: str
    # WTP longitude coordinate. | MaxLen: 19
    coordinate_longitude: str
    
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
    def to_dict(self) -> WtpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Wtp:
    """
    Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
    
    Path: wireless_controller/wtp
    Category: cmdb
    Primary Key: wtp-id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        wtp_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        wtp_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        wtp_id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[WtpObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        wtp_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        wtp_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
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
    ) -> FortiObjectList[WtpObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        wtp_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        wtp_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
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
    ) -> FortiObjectList[WtpObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        wtp_id: str | None = ...,
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
        wtp_id: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject | list[WtpObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WtpObject: ...
    
    @overload
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        wtp_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        wtp_id: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: WtpPayload | None = ...,
        wtp_id: str | None = ...,
        index: int | None = ...,
        uuid: str | None = ...,
        admin: Literal["discovered", "disable", "enable"] | None = ...,
        name: str | None = ...,
        location: str | None = ...,
        comment: str | None = ...,
        region: str | None = ...,
        region_x: str | None = ...,
        region_y: str | None = ...,
        firmware_provision: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        wtp_profile: str | None = ...,
        apcfg_profile: str | None = ...,
        bonjour_profile: str | None = ...,
        ble_major_id: int | None = ...,
        ble_minor_id: int | None = ...,
        override_led_state: Literal["enable", "disable"] | None = ...,
        led_state: Literal["enable", "disable"] | None = ...,
        override_wan_port_mode: Literal["enable", "disable"] | None = ...,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = ...,
        override_ip_fragment: Literal["enable", "disable"] | None = ...,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = ...,
        tun_mtu_uplink: int | None = ...,
        tun_mtu_downlink: int | None = ...,
        override_split_tunnel: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = ...,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = ...,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = ...,
        override_lan: Literal["enable", "disable"] | None = ...,
        lan: str | None = ...,
        override_allowaccess: Literal["enable", "disable"] | None = ...,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = ...,
        override_login_passwd_change: Literal["enable", "disable"] | None = ...,
        login_passwd_change: Literal["yes", "default", "no"] | None = ...,
        login_passwd: str | None = ...,
        override_default_mesh_root: Literal["enable", "disable"] | None = ...,
        default_mesh_root: Literal["enable", "disable"] | None = ...,
        radio_1: str | None = ...,
        radio_2: str | None = ...,
        radio_3: str | None = ...,
        radio_4: str | None = ...,
        image_download: Literal["enable", "disable"] | None = ...,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        coordinate_latitude: str | None = ...,
        coordinate_longitude: str | None = ...,
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
    "Wtp",
    "WtpPayload",
    "WtpResponse",
    "WtpObject",
]
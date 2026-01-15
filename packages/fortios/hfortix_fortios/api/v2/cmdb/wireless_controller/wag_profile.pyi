from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WagProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/wag_profile payload fields.
    
    Configure wireless access gateway (WAG) profiles used for tunnels on AP.
    
    **Usage:**
        payload: WagProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Tunnel profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    tunnel_type: Literal["l2tpv3", "gre"]  # Tunnel type. | Default: l2tpv3
    wag_ip: str  # IP Address of the wireless access gateway. | Default: 0.0.0.0
    wag_port: int  # UDP port of the wireless access gateway. | Default: 1701 | Min: 0 | Max: 65535
    ping_interval: int  # Interval between two tunnel monitoring echo packet | Default: 1 | Min: 1 | Max: 65535
    ping_number: int  # Number of the tunnel monitoring echo packets | Default: 5 | Min: 1 | Max: 65535
    return_packet_timeout: int  # Window of time for the return packets from the tun | Default: 160 | Min: 1 | Max: 65535
    dhcp_ip_addr: str  # IP address of the monitoring DHCP request packet s | Default: 0.0.0.0

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class WagProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/wag_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Tunnel profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    tunnel_type: Literal["l2tpv3", "gre"]  # Tunnel type. | Default: l2tpv3
    wag_ip: str  # IP Address of the wireless access gateway. | Default: 0.0.0.0
    wag_port: int  # UDP port of the wireless access gateway. | Default: 1701 | Min: 0 | Max: 65535
    ping_interval: int  # Interval between two tunnel monitoring echo packet | Default: 1 | Min: 1 | Max: 65535
    ping_number: int  # Number of the tunnel monitoring echo packets | Default: 5 | Min: 1 | Max: 65535
    return_packet_timeout: int  # Window of time for the return packets from the tun | Default: 160 | Min: 1 | Max: 65535
    dhcp_ip_addr: str  # IP address of the monitoring DHCP request packet s | Default: 0.0.0.0


@final
class WagProfileObject:
    """Typed FortiObject for wireless_controller/wag_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Tunnel profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Tunnel type. | Default: l2tpv3
    tunnel_type: Literal["l2tpv3", "gre"]
    # IP Address of the wireless access gateway. | Default: 0.0.0.0
    wag_ip: str
    # UDP port of the wireless access gateway. | Default: 1701 | Min: 0 | Max: 65535
    wag_port: int
    # Interval between two tunnel monitoring echo packets | Default: 1 | Min: 1 | Max: 65535
    ping_interval: int
    # Number of the tunnel monitoring echo packets | Default: 5 | Min: 1 | Max: 65535
    ping_number: int
    # Window of time for the return packets from the tunnel's remo | Default: 160 | Min: 1 | Max: 65535
    return_packet_timeout: int
    # IP address of the monitoring DHCP request packet sent throug | Default: 0.0.0.0
    dhcp_ip_addr: str
    
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
    def to_dict(self) -> WagProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class WagProfile:
    """
    Configure wireless access gateway (WAG) profiles used for tunnels on AP.
    
    Path: wireless_controller/wag_profile
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
    ) -> WagProfileObject: ...
    
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
    ) -> WagProfileObject: ...
    
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
    ) -> FortiObjectList[WagProfileObject]: ...
    
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
    ) -> WagProfileObject: ...
    
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
    ) -> WagProfileObject: ...
    
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
    ) -> FortiObjectList[WagProfileObject]: ...
    
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
    ) -> WagProfileObject: ...
    
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
    ) -> WagProfileObject: ...
    
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
    ) -> FortiObjectList[WagProfileObject]: ...
    
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
    ) -> WagProfileObject | list[WagProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WagProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WagProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WagProfileObject: ...
    
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
        payload_dict: WagProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        tunnel_type: Literal["l2tpv3", "gre"] | None = ...,
        wag_ip: str | None = ...,
        wag_port: int | None = ...,
        ping_interval: int | None = ...,
        ping_number: int | None = ...,
        return_packet_timeout: int | None = ...,
        dhcp_ip_addr: str | None = ...,
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
    "WagProfile",
    "WagProfilePayload",
    "WagProfileResponse",
    "WagProfileObject",
]
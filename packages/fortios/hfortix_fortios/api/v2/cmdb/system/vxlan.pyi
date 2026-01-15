from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class VxlanPayload(TypedDict, total=False):
    """
    Type hints for system/vxlan payload fields.
    
    Configure VXLAN devices.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.evpn.EvpnEndpoint` (via: evpn-id)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: VxlanPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # VXLAN device or interface name. Must be a unique i | MaxLen: 15
    interface: str  # Outgoing interface for VXLAN encapsulated traffic. | MaxLen: 15
    vni: int  # VXLAN network ID. | Default: 0 | Min: 1 | Max: 16777215
    ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"]  # IP version to use for the VXLAN interface and so f | Default: ipv4-unicast
    remote_ip: list[dict[str, Any]]  # IPv4 address of the VXLAN interface on the device
    local_ip: str  # IPv4 address to use as the source address for egre | Default: 0.0.0.0
    remote_ip6: list[dict[str, Any]]  # IPv6 IP address of the VXLAN interface on the devi
    local_ip6: str  # IPv6 address to use as the source address for egre | Default: ::
    dstport: int  # VXLAN destination port (1 - 65535, default = 4789) | Default: 4789 | Min: 1 | Max: 65535
    multicast_ttl: int  # VXLAN multicast TTL (1-255, default = 0). | Default: 0 | Min: 1 | Max: 255
    evpn_id: int  # EVPN instance. | Default: 0 | Min: 1 | Max: 65535
    learn_from_traffic: Literal["enable", "disable"]  # Enable/disable VXLAN MAC learning from traffic. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class VxlanRemoteipItem(TypedDict):
    """Type hints for remote-ip table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip: str  # IPv4 address. | MaxLen: 15


class VxlanRemoteip6Item(TypedDict):
    """Type hints for remote-ip6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip6: str  # IPv6 address. | MaxLen: 45


# Nested classes for table field children (object mode)

@final
class VxlanRemoteipObject:
    """Typed object for remote-ip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv4 address. | MaxLen: 15
    ip: str
    
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
class VxlanRemoteip6Object:
    """Typed object for remote-ip6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 address. | MaxLen: 45
    ip6: str
    
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
class VxlanResponse(TypedDict):
    """
    Type hints for system/vxlan API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # VXLAN device or interface name. Must be a unique i | MaxLen: 15
    interface: str  # Outgoing interface for VXLAN encapsulated traffic. | MaxLen: 15
    vni: int  # VXLAN network ID. | Default: 0 | Min: 1 | Max: 16777215
    ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"]  # IP version to use for the VXLAN interface and so f | Default: ipv4-unicast
    remote_ip: list[VxlanRemoteipItem]  # IPv4 address of the VXLAN interface on the device
    local_ip: str  # IPv4 address to use as the source address for egre | Default: 0.0.0.0
    remote_ip6: list[VxlanRemoteip6Item]  # IPv6 IP address of the VXLAN interface on the devi
    local_ip6: str  # IPv6 address to use as the source address for egre | Default: ::
    dstport: int  # VXLAN destination port (1 - 65535, default = 4789) | Default: 4789 | Min: 1 | Max: 65535
    multicast_ttl: int  # VXLAN multicast TTL (1-255, default = 0). | Default: 0 | Min: 1 | Max: 255
    evpn_id: int  # EVPN instance. | Default: 0 | Min: 1 | Max: 65535
    learn_from_traffic: Literal["enable", "disable"]  # Enable/disable VXLAN MAC learning from traffic. | Default: disable


@final
class VxlanObject:
    """Typed FortiObject for system/vxlan with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VXLAN device or interface name. Must be a unique interface n | MaxLen: 15
    name: str
    # Outgoing interface for VXLAN encapsulated traffic. | MaxLen: 15
    interface: str
    # VXLAN network ID. | Default: 0 | Min: 1 | Max: 16777215
    vni: int
    # IP version to use for the VXLAN interface and so for communi | Default: ipv4-unicast
    ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"]
    # IPv4 address of the VXLAN interface on the device at the rem
    remote_ip: list[VxlanRemoteipObject]
    # IPv4 address to use as the source address for egress VXLAN p | Default: 0.0.0.0
    local_ip: str
    # IPv6 IP address of the VXLAN interface on the device at the
    remote_ip6: list[VxlanRemoteip6Object]
    # IPv6 address to use as the source address for egress VXLAN p | Default: ::
    local_ip6: str
    # VXLAN destination port (1 - 65535, default = 4789). | Default: 4789 | Min: 1 | Max: 65535
    dstport: int
    # VXLAN multicast TTL (1-255, default = 0). | Default: 0 | Min: 1 | Max: 255
    multicast_ttl: int
    # EVPN instance. | Default: 0 | Min: 1 | Max: 65535
    evpn_id: int
    # Enable/disable VXLAN MAC learning from traffic. | Default: disable
    learn_from_traffic: Literal["enable", "disable"]
    
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
    def to_dict(self) -> VxlanPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Vxlan:
    """
    Configure VXLAN devices.
    
    Path: system/vxlan
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
    ) -> VxlanObject: ...
    
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
    ) -> VxlanObject: ...
    
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
    ) -> FortiObjectList[VxlanObject]: ...
    
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
    ) -> VxlanObject: ...
    
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
    ) -> VxlanObject: ...
    
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
    ) -> FortiObjectList[VxlanObject]: ...
    
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
    ) -> VxlanObject: ...
    
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
    ) -> VxlanObject: ...
    
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
    ) -> FortiObjectList[VxlanObject]: ...
    
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
    ) -> VxlanObject | list[VxlanObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> VxlanObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> VxlanObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> VxlanObject: ...
    
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
        payload_dict: VxlanPayload | None = ...,
        name: str | None = ...,
        interface: str | None = ...,
        vni: int | None = ...,
        ip_version: Literal["ipv4-unicast", "ipv6-unicast", "ipv4-multicast", "ipv6-multicast"] | None = ...,
        remote_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip: str | None = ...,
        remote_ip6: str | list[str] | list[dict[str, Any]] | None = ...,
        local_ip6: str | None = ...,
        dstport: int | None = ...,
        multicast_ttl: int | None = ...,
        evpn_id: int | None = ...,
        learn_from_traffic: Literal["enable", "disable"] | None = ...,
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
    "Vxlan",
    "VxlanPayload",
    "VxlanResponse",
    "VxlanObject",
]
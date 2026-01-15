from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class MulticastPayload(TypedDict, total=False):
    """
    Type hints for router/multicast payload fields.
    
    Configure router multicast.
    
    **Usage:**
        payload: MulticastPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    route_threshold: int  # Generate warnings when the number of multicast rou | Min: 1 | Max: 2147483647
    route_limit: int  # Maximum number of multicast routes. | Default: 2147483647 | Min: 1 | Max: 2147483647
    multicast_routing: Literal["enable", "disable"]  # Enable/disable IP multicast routing. | Default: disable
    pim_sm_global: str  # PIM sparse-mode global settings.
    pim_sm_global_vrf: list[dict[str, Any]]  # per-VRF PIM sparse-mode global settings.
    interface: list[dict[str, Any]]  # PIM interfaces.

# Nested TypedDicts for table field children (dict mode)

class MulticastPimsmglobalvrfItem(TypedDict):
    """Type hints for pim-sm-global-vrf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vrf: int  # VRF ID. | Default: 0 | Min: 1 | Max: 511
    bsr_candidate: Literal["enable", "disable"]  # Enable/disable allowing this router to become a bo | Default: disable
    bsr_interface: str  # Interface to advertise as candidate BSR. | MaxLen: 15
    bsr_priority: int  # BSR priority (0 - 255, default = 0). | Default: 0 | Min: 0 | Max: 255
    bsr_hash: int  # BSR hash length (0 - 32, default = 10). | Default: 10 | Min: 0 | Max: 32
    bsr_allow_quick_refresh: Literal["enable", "disable"]  # Enable/disable accept BSR quick refresh packets fr | Default: disable
    cisco_crp_prefix: Literal["enable", "disable"]  # Enable/disable making candidate RP compatible with | Default: disable
    rp_address: str  # Statically configure RP addresses.


class MulticastInterfaceItem(TypedDict):
    """Type hints for interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 15
    ttl_threshold: int  # Minimum TTL of multicast packets that will be forw | Default: 1 | Min: 1 | Max: 255
    pim_mode: Literal["sparse-mode", "dense-mode"]  # PIM operation mode. | Default: sparse-mode
    passive: Literal["enable", "disable"]  # Enable/disable listening to IGMP but not participa | Default: disable
    bfd: Literal["enable", "disable"]  # Enable/disable Protocol Independent Multicast | Default: disable
    neighbour_filter: str  # Routers acknowledged as neighbor routers. | MaxLen: 35
    hello_interval: int  # Interval between sending PIM hello messages | Default: 30 | Min: 1 | Max: 65535
    hello_holdtime: int  # Time before old neighbor information expires | Default: 105 | Min: 1 | Max: 65535
    cisco_exclude_genid: Literal["enable", "disable"]  # Exclude GenID from hello packets | Default: disable
    dr_priority: int  # DR election priority. | Default: 1 | Min: 1 | Max: 4294967295
    propagation_delay: int  # Delay flooding packets on this interface | Default: 500 | Min: 100 | Max: 5000
    state_refresh_interval: int  # Interval between sending state-refresh packets | Default: 60 | Min: 1 | Max: 100
    rp_candidate: Literal["enable", "disable"]  # Enable/disable compete to become RP in elections. | Default: disable
    rp_candidate_group: str  # Multicast groups managed by this RP. | MaxLen: 35
    rp_candidate_priority: int  # Router's priority as RP. | Default: 192 | Min: 0 | Max: 255
    rp_candidate_interval: int  # RP candidate advertisement interval | Default: 60 | Min: 1 | Max: 16383
    multicast_flow: str  # Acceptable source for multicast group. | MaxLen: 35
    static_group: str  # Statically set multicast groups to forward out. | MaxLen: 35
    rpf_nbr_fail_back: Literal["enable", "disable"]  # Enable/disable fail back for RPF neighbor query. | Default: disable
    rpf_nbr_fail_back_filter: str  # Filter for fail back RPF neighbors. | MaxLen: 35
    join_group: str  # Join multicast groups.
    igmp: str  # IGMP configuration options.


# Nested classes for table field children (object mode)

@final
class MulticastPimsmglobalvrfObject:
    """Typed object for pim-sm-global-vrf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VRF ID. | Default: 0 | Min: 1 | Max: 511
    vrf: int
    # Enable/disable allowing this router to become a bootstrap ro | Default: disable
    bsr_candidate: Literal["enable", "disable"]
    # Interface to advertise as candidate BSR. | MaxLen: 15
    bsr_interface: str
    # BSR priority (0 - 255, default = 0). | Default: 0 | Min: 0 | Max: 255
    bsr_priority: int
    # BSR hash length (0 - 32, default = 10). | Default: 10 | Min: 0 | Max: 32
    bsr_hash: int
    # Enable/disable accept BSR quick refresh packets from neighbo | Default: disable
    bsr_allow_quick_refresh: Literal["enable", "disable"]
    # Enable/disable making candidate RP compatible with old Cisco | Default: disable
    cisco_crp_prefix: Literal["enable", "disable"]
    # Statically configure RP addresses.
    rp_address: str
    
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
class MulticastInterfaceObject:
    """Typed object for interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 15
    name: str
    # Minimum TTL of multicast packets that will be forwarded | Default: 1 | Min: 1 | Max: 255
    ttl_threshold: int
    # PIM operation mode. | Default: sparse-mode
    pim_mode: Literal["sparse-mode", "dense-mode"]
    # Enable/disable listening to IGMP but not participating in PI | Default: disable
    passive: Literal["enable", "disable"]
    # Enable/disable Protocol Independent Multicast (PIM) Bidirect | Default: disable
    bfd: Literal["enable", "disable"]
    # Routers acknowledged as neighbor routers. | MaxLen: 35
    neighbour_filter: str
    # Interval between sending PIM hello messages | Default: 30 | Min: 1 | Max: 65535
    hello_interval: int
    # Time before old neighbor information expires | Default: 105 | Min: 1 | Max: 65535
    hello_holdtime: int
    # Exclude GenID from hello packets | Default: disable
    cisco_exclude_genid: Literal["enable", "disable"]
    # DR election priority. | Default: 1 | Min: 1 | Max: 4294967295
    dr_priority: int
    # Delay flooding packets on this interface | Default: 500 | Min: 100 | Max: 5000
    propagation_delay: int
    # Interval between sending state-refresh packets | Default: 60 | Min: 1 | Max: 100
    state_refresh_interval: int
    # Enable/disable compete to become RP in elections. | Default: disable
    rp_candidate: Literal["enable", "disable"]
    # Multicast groups managed by this RP. | MaxLen: 35
    rp_candidate_group: str
    # Router's priority as RP. | Default: 192 | Min: 0 | Max: 255
    rp_candidate_priority: int
    # RP candidate advertisement interval | Default: 60 | Min: 1 | Max: 16383
    rp_candidate_interval: int
    # Acceptable source for multicast group. | MaxLen: 35
    multicast_flow: str
    # Statically set multicast groups to forward out. | MaxLen: 35
    static_group: str
    # Enable/disable fail back for RPF neighbor query. | Default: disable
    rpf_nbr_fail_back: Literal["enable", "disable"]
    # Filter for fail back RPF neighbors. | MaxLen: 35
    rpf_nbr_fail_back_filter: str
    # Join multicast groups.
    join_group: str
    # IGMP configuration options.
    igmp: str
    
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
class MulticastResponse(TypedDict):
    """
    Type hints for router/multicast API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    route_threshold: int  # Generate warnings when the number of multicast rou | Min: 1 | Max: 2147483647
    route_limit: int  # Maximum number of multicast routes. | Default: 2147483647 | Min: 1 | Max: 2147483647
    multicast_routing: Literal["enable", "disable"]  # Enable/disable IP multicast routing. | Default: disable
    pim_sm_global: str  # PIM sparse-mode global settings.
    pim_sm_global_vrf: list[MulticastPimsmglobalvrfItem]  # per-VRF PIM sparse-mode global settings.
    interface: list[MulticastInterfaceItem]  # PIM interfaces.


@final
class MulticastObject:
    """Typed FortiObject for router/multicast with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Generate warnings when the number of multicast routes exceed | Min: 1 | Max: 2147483647
    route_threshold: int
    # Maximum number of multicast routes. | Default: 2147483647 | Min: 1 | Max: 2147483647
    route_limit: int
    # Enable/disable IP multicast routing. | Default: disable
    multicast_routing: Literal["enable", "disable"]
    # PIM sparse-mode global settings.
    pim_sm_global: str
    # per-VRF PIM sparse-mode global settings.
    pim_sm_global_vrf: list[MulticastPimsmglobalvrfObject]
    # PIM interfaces.
    interface: list[MulticastInterfaceObject]
    
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
    def to_dict(self) -> MulticastPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Multicast:
    """
    Configure router multicast.
    
    Path: router/multicast
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject: ...
    
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
    ) -> MulticastObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MulticastObject: ...
    
    @overload
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: MulticastPayload | None = ...,
        route_threshold: int | None = ...,
        route_limit: int | None = ...,
        multicast_routing: Literal["enable", "disable"] | None = ...,
        pim_sm_global: str | None = ...,
        pim_sm_global_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Multicast",
    "MulticastPayload",
    "MulticastResponse",
    "MulticastObject",
]
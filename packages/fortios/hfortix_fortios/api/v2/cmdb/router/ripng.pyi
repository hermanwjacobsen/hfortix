from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RipngPayload(TypedDict, total=False):
    """
    Type hints for router/ripng payload fields.
    
    Configure RIPng.
    
    **Usage:**
        payload: RipngPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    default_information_originate: Literal["enable", "disable"]  # Enable/disable generation of default route. | Default: disable
    default_metric: int  # Default metric. | Default: 1 | Min: 1 | Max: 16
    max_out_metric: int  # Maximum metric allowed to output | Default: 0 | Min: 0 | Max: 15
    distance: list[dict[str, Any]]  # Distance.
    distribute_list: list[dict[str, Any]]  # Distribute list.
    neighbor: list[dict[str, Any]]  # Neighbor.
    network: list[dict[str, Any]]  # Network.
    aggregate_address: list[dict[str, Any]]  # Aggregate address.
    offset_list: list[dict[str, Any]]  # Offset list.
    passive_interface: list[dict[str, Any]]  # Passive interface configuration.
    redistribute: list[dict[str, Any]]  # Redistribute configuration.
    update_timer: int  # Update timer in seconds. | Default: 30 | Min: 5 | Max: 2147483647
    timeout_timer: int  # Timeout timer in seconds. | Default: 180 | Min: 5 | Max: 2147483647
    garbage_timer: int  # Garbage timer in seconds. | Default: 120 | Min: 5 | Max: 2147483647
    interface: list[dict[str, Any]]  # RIPng interface configuration.

# Nested TypedDicts for table field children (dict mode)

class RipngDistanceItem(TypedDict):
    """Type hints for distance table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Distance ID. | Default: 0 | Min: 0 | Max: 4294967295
    distance: int  # Distance (1 - 255). | Default: 0 | Min: 1 | Max: 255
    prefix6: str  # Distance prefix6. | Default: ::/0
    access_list6: str  # Access list for route destination. | MaxLen: 35


class RipngDistributelistItem(TypedDict):
    """Type hints for distribute-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Distribute list ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Status. | Default: disable
    direction: Literal["in", "out"]  # Distribute list direction. | Default: out
    listname: str  # Distribute access/prefix list name. | MaxLen: 35
    interface: str  # Distribute list interface name. | MaxLen: 15


class RipngNeighborItem(TypedDict):
    """Type hints for neighbor table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Neighbor entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    ip6: str  # IPv6 link-local address. | Default: ::
    interface: str  # Interface name. | MaxLen: 15


class RipngNetworkItem(TypedDict):
    """Type hints for network table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Network IPv6 link-local prefix. | Default: ::/0


class RipngAggregateaddressItem(TypedDict):
    """Type hints for aggregate-address table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Aggregate address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix6: str  # Aggregate address prefix. | Default: ::/0


class RipngOffsetlistItem(TypedDict):
    """Type hints for offset-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Offset-list ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Status. | Default: enable
    direction: Literal["in", "out"]  # Offset list direction. | Default: out
    access_list6: str  # IPv6 access list name. | MaxLen: 35
    offset: int  # Offset. | Default: 0 | Min: 1 | Max: 16
    interface: str  # Interface name. | MaxLen: 15


class RipngPassiveinterfaceItem(TypedDict):
    """Type hints for passive-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Passive interface name. | MaxLen: 79


class RipngRedistributeItem(TypedDict):
    """Type hints for redistribute table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Redistribute name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Status. | Default: disable
    metric: int  # Redistribute metric setting. | Default: 0 | Min: 1 | Max: 16
    routemap: str  # Route map name. | MaxLen: 35


class RipngInterfaceItem(TypedDict):
    """Type hints for interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 35
    split_horizon_status: Literal["enable", "disable"]  # Enable/disable split horizon. | Default: enable
    split_horizon: Literal["poisoned", "regular"]  # Enable/disable split horizon. | Default: poisoned
    flags: int  # Flags. | Default: 8 | Min: 0 | Max: 255


# Nested classes for table field children (object mode)

@final
class RipngDistanceObject:
    """Typed object for distance table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distance ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Distance (1 - 255). | Default: 0 | Min: 1 | Max: 255
    distance: int
    # Distance prefix6. | Default: ::/0
    prefix6: str
    # Access list for route destination. | MaxLen: 35
    access_list6: str
    
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
class RipngDistributelistObject:
    """Typed object for distribute-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Distribute list direction. | Default: out
    direction: Literal["in", "out"]
    # Distribute access/prefix list name. | MaxLen: 35
    listname: str
    # Distribute list interface name. | MaxLen: 15
    interface: str
    
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
class RipngNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IPv6 link-local address. | Default: ::
    ip6: str
    # Interface name. | MaxLen: 15
    interface: str
    
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
class RipngNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Network IPv6 link-local prefix. | Default: ::/0
    prefix: str
    
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
class RipngAggregateaddressObject:
    """Typed object for aggregate-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Aggregate address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Aggregate address prefix. | Default: ::/0
    prefix6: str
    
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
class RipngOffsetlistObject:
    """Typed object for offset-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Offset-list ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Status. | Default: enable
    status: Literal["enable", "disable"]
    # Offset list direction. | Default: out
    direction: Literal["in", "out"]
    # IPv6 access list name. | MaxLen: 35
    access_list6: str
    # Offset. | Default: 0 | Min: 1 | Max: 16
    offset: int
    # Interface name. | MaxLen: 15
    interface: str
    
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
class RipngPassiveinterfaceObject:
    """Typed object for passive-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Passive interface name. | MaxLen: 79
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
class RipngRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Redistribute name. | MaxLen: 35
    name: str
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Redistribute metric setting. | Default: 0 | Min: 1 | Max: 16
    metric: int
    # Route map name. | MaxLen: 35
    routemap: str
    
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
class RipngInterfaceObject:
    """Typed object for interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 35
    name: str
    # Enable/disable split horizon. | Default: enable
    split_horizon_status: Literal["enable", "disable"]
    # Enable/disable split horizon. | Default: poisoned
    split_horizon: Literal["poisoned", "regular"]
    # Flags. | Default: 8 | Min: 0 | Max: 255
    flags: int
    
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
class RipngResponse(TypedDict):
    """
    Type hints for router/ripng API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    default_information_originate: Literal["enable", "disable"]  # Enable/disable generation of default route. | Default: disable
    default_metric: int  # Default metric. | Default: 1 | Min: 1 | Max: 16
    max_out_metric: int  # Maximum metric allowed to output | Default: 0 | Min: 0 | Max: 15
    distance: list[RipngDistanceItem]  # Distance.
    distribute_list: list[RipngDistributelistItem]  # Distribute list.
    neighbor: list[RipngNeighborItem]  # Neighbor.
    network: list[RipngNetworkItem]  # Network.
    aggregate_address: list[RipngAggregateaddressItem]  # Aggregate address.
    offset_list: list[RipngOffsetlistItem]  # Offset list.
    passive_interface: list[RipngPassiveinterfaceItem]  # Passive interface configuration.
    redistribute: list[RipngRedistributeItem]  # Redistribute configuration.
    update_timer: int  # Update timer in seconds. | Default: 30 | Min: 5 | Max: 2147483647
    timeout_timer: int  # Timeout timer in seconds. | Default: 180 | Min: 5 | Max: 2147483647
    garbage_timer: int  # Garbage timer in seconds. | Default: 120 | Min: 5 | Max: 2147483647
    interface: list[RipngInterfaceItem]  # RIPng interface configuration.


@final
class RipngObject:
    """Typed FortiObject for router/ripng with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable generation of default route. | Default: disable
    default_information_originate: Literal["enable", "disable"]
    # Default metric. | Default: 1 | Min: 1 | Max: 16
    default_metric: int
    # Maximum metric allowed to output(0 means 'not set'). | Default: 0 | Min: 0 | Max: 15
    max_out_metric: int
    # Distance.
    distance: list[RipngDistanceObject]
    # Distribute list.
    distribute_list: list[RipngDistributelistObject]
    # Neighbor.
    neighbor: list[RipngNeighborObject]
    # Network.
    network: list[RipngNetworkObject]
    # Aggregate address.
    aggregate_address: list[RipngAggregateaddressObject]
    # Offset list.
    offset_list: list[RipngOffsetlistObject]
    # Passive interface configuration.
    passive_interface: list[RipngPassiveinterfaceObject]
    # Redistribute configuration.
    redistribute: list[RipngRedistributeObject]
    # Update timer in seconds. | Default: 30 | Min: 5 | Max: 2147483647
    update_timer: int
    # Timeout timer in seconds. | Default: 180 | Min: 5 | Max: 2147483647
    timeout_timer: int
    # Garbage timer in seconds. | Default: 120 | Min: 5 | Max: 2147483647
    garbage_timer: int
    # RIPng interface configuration.
    interface: list[RipngInterfaceObject]
    
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
    def to_dict(self) -> RipngPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ripng:
    """
    Configure RIPng.
    
    Path: router/ripng
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject: ...
    
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
    ) -> RipngObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RipngObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
        interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
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
        payload_dict: RipngPayload | None = ...,
        default_information_originate: Literal["enable", "disable"] | None = ...,
        default_metric: int | None = ...,
        max_out_metric: int | None = ...,
        distance: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        offset_list: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        update_timer: int | None = ...,
        timeout_timer: int | None = ...,
        garbage_timer: int | None = ...,
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
    "Ripng",
    "RipngPayload",
    "RipngResponse",
    "RipngObject",
]
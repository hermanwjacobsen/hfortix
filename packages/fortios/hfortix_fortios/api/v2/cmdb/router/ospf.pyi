from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class OspfPayload(TypedDict, total=False):
    """
    Type hints for router/ospf payload fields.
    
    Configure OSPF.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.access-list.AccessListEndpoint` (via: distribute-list-in)
        - :class:`~.router.prefix-list.PrefixListEndpoint` (via: distribute-list-in)
        - :class:`~.router.route-map.RouteMapEndpoint` (via: default-information-route-map, distribute-route-map-in)

    **Usage:**
        payload: OspfPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    abr_type: Literal["cisco", "ibm", "shortcut", "standard"]  # Area border router type. | Default: standard
    auto_cost_ref_bandwidth: int  # Reference bandwidth in terms of megabits per secon | Default: 1000 | Min: 1 | Max: 1000000
    distance_external: int  # Administrative external distance. | Default: 110 | Min: 1 | Max: 255
    distance_inter_area: int  # Administrative inter-area distance. | Default: 110 | Min: 1 | Max: 255
    distance_intra_area: int  # Administrative intra-area distance. | Default: 110 | Min: 1 | Max: 255
    database_overflow: Literal["enable", "disable"]  # Enable/disable database overflow. | Default: disable
    database_overflow_max_lsas: int  # Database overflow maximum LSAs. | Default: 10000 | Min: 0 | Max: 4294967295
    database_overflow_time_to_recover: int  # Database overflow time to recover (sec). | Default: 300 | Min: 0 | Max: 65535
    default_information_originate: Literal["enable", "always", "disable"]  # Enable/disable generation of default route. | Default: disable
    default_information_metric: int  # Default information metric. | Default: 10 | Min: 1 | Max: 16777214
    default_information_metric_type: Literal["1", "2"]  # Default information metric type. | Default: 2
    default_information_route_map: str  # Default information route map. | MaxLen: 35
    default_metric: int  # Default metric of redistribute routes. | Default: 10 | Min: 1 | Max: 16777214
    distance: int  # Distance of the route. | Default: 110 | Min: 1 | Max: 255
    lsa_refresh_interval: int  # The minimal OSPF LSA update time interval | Default: 5 | Min: 0 | Max: 5
    rfc1583_compatible: Literal["enable", "disable"]  # Enable/disable RFC1583 compatibility. | Default: disable
    router_id: str  # Router ID. | Default: 0.0.0.0
    spf_timers: str  # SPF calculation frequency.
    bfd: Literal["enable", "disable"]  # Bidirectional Forwarding Detection (BFD). | Default: disable
    log_neighbour_changes: Literal["enable", "disable"]  # Log of OSPF neighbor changes. | Default: enable
    distribute_list_in: str  # Filter incoming routes. | MaxLen: 35
    distribute_route_map_in: str  # Filter incoming external routes by route-map. | MaxLen: 35
    restart_mode: Literal["none", "lls", "graceful-restart"]  # OSPF restart mode (graceful or LLS). | Default: none
    restart_period: int  # Graceful restart period. | Default: 120 | Min: 1 | Max: 3600
    restart_on_topology_change: Literal["enable", "disable"]  # Enable/disable continuing graceful restart upon to | Default: disable
    area: list[dict[str, Any]]  # OSPF area configuration.
    ospf_interface: list[dict[str, Any]]  # OSPF interface configuration.
    network: list[dict[str, Any]]  # OSPF network configuration.
    neighbor: list[dict[str, Any]]  # OSPF neighbor configuration are used when OSPF run
    passive_interface: list[dict[str, Any]]  # Passive interface configuration.
    summary_address: list[dict[str, Any]]  # IP address summary configuration.
    distribute_list: list[dict[str, Any]]  # Distribute list configuration.
    redistribute: list[dict[str, Any]]  # Redistribute configuration.

# Nested TypedDicts for table field children (dict mode)

class OspfAreaItem(TypedDict):
    """Type hints for area table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: str  # Area entry IP address. | Default: 0.0.0.0
    shortcut: Literal["disable", "enable", "default"]  # Enable/disable shortcut option. | Default: disable
    authentication: Literal["none", "text", "message-digest"]  # Authentication type. | Default: none
    default_cost: int  # Summary default cost of stub or NSSA area. | Default: 10 | Min: 0 | Max: 4294967295
    nssa_translator_role: Literal["candidate", "never", "always"]  # NSSA translator role type. | Default: candidate
    stub_type: Literal["no-summary", "summary"]  # Stub summary setting. | Default: summary
    type: Literal["regular", "nssa", "stub"]  # Area type setting. | Default: regular
    nssa_default_information_originate: Literal["enable", "always", "disable"]  # Redistribute, advertise, or do not originate Type- | Default: disable
    nssa_default_information_originate_metric: int  # OSPF default metric. | Default: 10 | Min: 0 | Max: 16777214
    nssa_default_information_originate_metric_type: Literal["1", "2"]  # OSPF metric type for default routes. | Default: 2
    nssa_redistribution: Literal["enable", "disable"]  # Enable/disable redistribute into NSSA area. | Default: enable
    comments: str  # Comment. | MaxLen: 255
    range: str  # OSPF area range configuration.
    virtual_link: str  # OSPF virtual link configuration.
    filter_list: str  # OSPF area filter-list configuration.


class OspfOspfinterfaceItem(TypedDict):
    """Type hints for ospf-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface entry name. | MaxLen: 35
    comments: str  # Comment. | MaxLen: 255
    interface: str  # Configuration interface name. | MaxLen: 15
    ip: str  # IP address. | Default: 0.0.0.0
    linkdown_fast_failover: Literal["enable", "disable"]  # Enable/disable fast link failover. | Default: disable
    authentication: Literal["none", "text", "message-digest"]  # Authentication type. | Default: none
    authentication_key: str  # Authentication key. | MaxLen: 8
    keychain: str  # Message-digest key-chain name. | MaxLen: 35
    prefix_length: int  # Prefix length. | Default: 0 | Min: 0 | Max: 32
    retransmit_interval: int  # Retransmit interval. | Default: 5 | Min: 1 | Max: 65535
    transmit_delay: int  # Transmit delay. | Default: 1 | Min: 1 | Max: 65535
    cost: int  # Cost of the interface, value range from 0 to 65535 | Default: 0 | Min: 0 | Max: 65535
    priority: int  # Priority. | Default: 1 | Min: 0 | Max: 255
    dead_interval: int  # Dead interval. | Default: 0 | Min: 0 | Max: 65535
    hello_interval: int  # Hello interval. | Default: 0 | Min: 0 | Max: 65535
    hello_multiplier: int  # Number of hello packets within dead interval. | Default: 0 | Min: 3 | Max: 10
    database_filter_out: Literal["enable", "disable"]  # Enable/disable control of flooding out LSAs. | Default: disable
    mtu: int  # MTU for database description packets. | Default: 0 | Min: 576 | Max: 65535
    mtu_ignore: Literal["enable", "disable"]  # Enable/disable ignore MTU. | Default: disable
    network_type: Literal["broadcast", "non-broadcast", "point-to-point", "point-to-multipoint", "point-to-multipoint-non-broadcast"]  # Network type. | Default: broadcast
    bfd: Literal["global", "enable", "disable"]  # Bidirectional Forwarding Detection (BFD). | Default: global
    status: Literal["disable", "enable"]  # Enable/disable status. | Default: enable
    resync_timeout: int  # Graceful restart neighbor resynchronization timeou | Default: 40 | Min: 1 | Max: 3600
    md5_keys: str  # MD5 key.


class OspfNetworkItem(TypedDict):
    """Type hints for network table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Prefix. | Default: 0.0.0.0 0.0.0.0
    area: str  # Attach the network to area. | Default: 0.0.0.0
    comments: str  # Comment. | MaxLen: 255


class OspfNeighborItem(TypedDict):
    """Type hints for neighbor table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Neighbor entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    ip: str  # Interface IP address of the neighbor. | Default: 0.0.0.0
    poll_interval: int  # Poll interval time in seconds. | Default: 10 | Min: 1 | Max: 65535
    cost: int  # Cost of the interface, value range from 0 to 65535 | Default: 0 | Min: 0 | Max: 65535
    priority: int  # Priority. | Default: 1 | Min: 0 | Max: 255


class OspfPassiveinterfaceItem(TypedDict):
    """Type hints for passive-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Passive interface name. | MaxLen: 79


class OspfSummaryaddressItem(TypedDict):
    """Type hints for summary-address table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Summary address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Prefix. | Default: 0.0.0.0 0.0.0.0
    tag: int  # Tag value. | Default: 0 | Min: 0 | Max: 4294967295
    advertise: Literal["disable", "enable"]  # Enable/disable advertise status. | Default: enable


class OspfDistributelistItem(TypedDict):
    """Type hints for distribute-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Distribute list entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    access_list: str  # Access list name. | MaxLen: 35
    protocol: Literal["connected", "static", "rip"]  # Protocol type. | Default: connected


class OspfRedistributeItem(TypedDict):
    """Type hints for redistribute table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Redistribute name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Status. | Default: disable
    metric: int  # Redistribute metric setting. | Default: 0 | Min: 0 | Max: 16777214
    routemap: str  # Route map name. | MaxLen: 35
    metric_type: Literal["1", "2"]  # Metric type. | Default: 2
    tag: int  # Tag value. | Default: 0 | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class OspfAreaObject:
    """Typed object for area table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Area entry IP address. | Default: 0.0.0.0
    id: str
    # Enable/disable shortcut option. | Default: disable
    shortcut: Literal["disable", "enable", "default"]
    # Authentication type. | Default: none
    authentication: Literal["none", "text", "message-digest"]
    # Summary default cost of stub or NSSA area. | Default: 10 | Min: 0 | Max: 4294967295
    default_cost: int
    # NSSA translator role type. | Default: candidate
    nssa_translator_role: Literal["candidate", "never", "always"]
    # Stub summary setting. | Default: summary
    stub_type: Literal["no-summary", "summary"]
    # Area type setting. | Default: regular
    type: Literal["regular", "nssa", "stub"]
    # Redistribute, advertise, or do not originate Type-7 default | Default: disable
    nssa_default_information_originate: Literal["enable", "always", "disable"]
    # OSPF default metric. | Default: 10 | Min: 0 | Max: 16777214
    nssa_default_information_originate_metric: int
    # OSPF metric type for default routes. | Default: 2
    nssa_default_information_originate_metric_type: Literal["1", "2"]
    # Enable/disable redistribute into NSSA area. | Default: enable
    nssa_redistribution: Literal["enable", "disable"]
    # Comment. | MaxLen: 255
    comments: str
    # OSPF area range configuration.
    range: str
    # OSPF virtual link configuration.
    virtual_link: str
    # OSPF area filter-list configuration.
    filter_list: str
    
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
class OspfOspfinterfaceObject:
    """Typed object for ospf-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface entry name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comments: str
    # Configuration interface name. | MaxLen: 15
    interface: str
    # IP address. | Default: 0.0.0.0
    ip: str
    # Enable/disable fast link failover. | Default: disable
    linkdown_fast_failover: Literal["enable", "disable"]
    # Authentication type. | Default: none
    authentication: Literal["none", "text", "message-digest"]
    # Authentication key. | MaxLen: 8
    authentication_key: str
    # Message-digest key-chain name. | MaxLen: 35
    keychain: str
    # Prefix length. | Default: 0 | Min: 0 | Max: 32
    prefix_length: int
    # Retransmit interval. | Default: 5 | Min: 1 | Max: 65535
    retransmit_interval: int
    # Transmit delay. | Default: 1 | Min: 1 | Max: 65535
    transmit_delay: int
    # Cost of the interface, value range from 0 to 65535, 0 means | Default: 0 | Min: 0 | Max: 65535
    cost: int
    # Priority. | Default: 1 | Min: 0 | Max: 255
    priority: int
    # Dead interval. | Default: 0 | Min: 0 | Max: 65535
    dead_interval: int
    # Hello interval. | Default: 0 | Min: 0 | Max: 65535
    hello_interval: int
    # Number of hello packets within dead interval. | Default: 0 | Min: 3 | Max: 10
    hello_multiplier: int
    # Enable/disable control of flooding out LSAs. | Default: disable
    database_filter_out: Literal["enable", "disable"]
    # MTU for database description packets. | Default: 0 | Min: 576 | Max: 65535
    mtu: int
    # Enable/disable ignore MTU. | Default: disable
    mtu_ignore: Literal["enable", "disable"]
    # Network type. | Default: broadcast
    network_type: Literal["broadcast", "non-broadcast", "point-to-point", "point-to-multipoint", "point-to-multipoint-non-broadcast"]
    # Bidirectional Forwarding Detection (BFD). | Default: global
    bfd: Literal["global", "enable", "disable"]
    # Enable/disable status. | Default: enable
    status: Literal["disable", "enable"]
    # Graceful restart neighbor resynchronization timeout. | Default: 40 | Min: 1 | Max: 3600
    resync_timeout: int
    # MD5 key.
    md5_keys: str
    
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
class OspfNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Network entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Attach the network to area. | Default: 0.0.0.0
    area: str
    # Comment. | MaxLen: 255
    comments: str
    
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
class OspfNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Interface IP address of the neighbor. | Default: 0.0.0.0
    ip: str
    # Poll interval time in seconds. | Default: 10 | Min: 1 | Max: 65535
    poll_interval: int
    # Cost of the interface, value range from 0 to 65535, 0 means | Default: 0 | Min: 0 | Max: 65535
    cost: int
    # Priority. | Default: 1 | Min: 0 | Max: 255
    priority: int
    
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
class OspfPassiveinterfaceObject:
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
class OspfSummaryaddressObject:
    """Typed object for summary-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Summary address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Tag value. | Default: 0 | Min: 0 | Max: 4294967295
    tag: int
    # Enable/disable advertise status. | Default: enable
    advertise: Literal["disable", "enable"]
    
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
class OspfDistributelistObject:
    """Typed object for distribute-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Access list name. | MaxLen: 35
    access_list: str
    # Protocol type. | Default: connected
    protocol: Literal["connected", "static", "rip"]
    
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
class OspfRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Redistribute name. | MaxLen: 35
    name: str
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Redistribute metric setting. | Default: 0 | Min: 0 | Max: 16777214
    metric: int
    # Route map name. | MaxLen: 35
    routemap: str
    # Metric type. | Default: 2
    metric_type: Literal["1", "2"]
    # Tag value. | Default: 0 | Min: 0 | Max: 4294967295
    tag: int
    
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
class OspfResponse(TypedDict):
    """
    Type hints for router/ospf API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    abr_type: Literal["cisco", "ibm", "shortcut", "standard"]  # Area border router type. | Default: standard
    auto_cost_ref_bandwidth: int  # Reference bandwidth in terms of megabits per secon | Default: 1000 | Min: 1 | Max: 1000000
    distance_external: int  # Administrative external distance. | Default: 110 | Min: 1 | Max: 255
    distance_inter_area: int  # Administrative inter-area distance. | Default: 110 | Min: 1 | Max: 255
    distance_intra_area: int  # Administrative intra-area distance. | Default: 110 | Min: 1 | Max: 255
    database_overflow: Literal["enable", "disable"]  # Enable/disable database overflow. | Default: disable
    database_overflow_max_lsas: int  # Database overflow maximum LSAs. | Default: 10000 | Min: 0 | Max: 4294967295
    database_overflow_time_to_recover: int  # Database overflow time to recover (sec). | Default: 300 | Min: 0 | Max: 65535
    default_information_originate: Literal["enable", "always", "disable"]  # Enable/disable generation of default route. | Default: disable
    default_information_metric: int  # Default information metric. | Default: 10 | Min: 1 | Max: 16777214
    default_information_metric_type: Literal["1", "2"]  # Default information metric type. | Default: 2
    default_information_route_map: str  # Default information route map. | MaxLen: 35
    default_metric: int  # Default metric of redistribute routes. | Default: 10 | Min: 1 | Max: 16777214
    distance: int  # Distance of the route. | Default: 110 | Min: 1 | Max: 255
    lsa_refresh_interval: int  # The minimal OSPF LSA update time interval | Default: 5 | Min: 0 | Max: 5
    rfc1583_compatible: Literal["enable", "disable"]  # Enable/disable RFC1583 compatibility. | Default: disable
    router_id: str  # Router ID. | Default: 0.0.0.0
    spf_timers: str  # SPF calculation frequency.
    bfd: Literal["enable", "disable"]  # Bidirectional Forwarding Detection (BFD). | Default: disable
    log_neighbour_changes: Literal["enable", "disable"]  # Log of OSPF neighbor changes. | Default: enable
    distribute_list_in: str  # Filter incoming routes. | MaxLen: 35
    distribute_route_map_in: str  # Filter incoming external routes by route-map. | MaxLen: 35
    restart_mode: Literal["none", "lls", "graceful-restart"]  # OSPF restart mode (graceful or LLS). | Default: none
    restart_period: int  # Graceful restart period. | Default: 120 | Min: 1 | Max: 3600
    restart_on_topology_change: Literal["enable", "disable"]  # Enable/disable continuing graceful restart upon to | Default: disable
    area: list[OspfAreaItem]  # OSPF area configuration.
    ospf_interface: list[OspfOspfinterfaceItem]  # OSPF interface configuration.
    network: list[OspfNetworkItem]  # OSPF network configuration.
    neighbor: list[OspfNeighborItem]  # OSPF neighbor configuration are used when OSPF run
    passive_interface: list[OspfPassiveinterfaceItem]  # Passive interface configuration.
    summary_address: list[OspfSummaryaddressItem]  # IP address summary configuration.
    distribute_list: list[OspfDistributelistItem]  # Distribute list configuration.
    redistribute: list[OspfRedistributeItem]  # Redistribute configuration.


@final
class OspfObject:
    """Typed FortiObject for router/ospf with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Area border router type. | Default: standard
    abr_type: Literal["cisco", "ibm", "shortcut", "standard"]
    # Reference bandwidth in terms of megabits per second. | Default: 1000 | Min: 1 | Max: 1000000
    auto_cost_ref_bandwidth: int
    # Administrative external distance. | Default: 110 | Min: 1 | Max: 255
    distance_external: int
    # Administrative inter-area distance. | Default: 110 | Min: 1 | Max: 255
    distance_inter_area: int
    # Administrative intra-area distance. | Default: 110 | Min: 1 | Max: 255
    distance_intra_area: int
    # Enable/disable database overflow. | Default: disable
    database_overflow: Literal["enable", "disable"]
    # Database overflow maximum LSAs. | Default: 10000 | Min: 0 | Max: 4294967295
    database_overflow_max_lsas: int
    # Database overflow time to recover (sec). | Default: 300 | Min: 0 | Max: 65535
    database_overflow_time_to_recover: int
    # Enable/disable generation of default route. | Default: disable
    default_information_originate: Literal["enable", "always", "disable"]
    # Default information metric. | Default: 10 | Min: 1 | Max: 16777214
    default_information_metric: int
    # Default information metric type. | Default: 2
    default_information_metric_type: Literal["1", "2"]
    # Default information route map. | MaxLen: 35
    default_information_route_map: str
    # Default metric of redistribute routes. | Default: 10 | Min: 1 | Max: 16777214
    default_metric: int
    # Distance of the route. | Default: 110 | Min: 1 | Max: 255
    distance: int
    # The minimal OSPF LSA update time interval | Default: 5 | Min: 0 | Max: 5
    lsa_refresh_interval: int
    # Enable/disable RFC1583 compatibility. | Default: disable
    rfc1583_compatible: Literal["enable", "disable"]
    # Router ID. | Default: 0.0.0.0
    router_id: str
    # SPF calculation frequency.
    spf_timers: str
    # Bidirectional Forwarding Detection (BFD). | Default: disable
    bfd: Literal["enable", "disable"]
    # Log of OSPF neighbor changes. | Default: enable
    log_neighbour_changes: Literal["enable", "disable"]
    # Filter incoming routes. | MaxLen: 35
    distribute_list_in: str
    # Filter incoming external routes by route-map. | MaxLen: 35
    distribute_route_map_in: str
    # OSPF restart mode (graceful or LLS). | Default: none
    restart_mode: Literal["none", "lls", "graceful-restart"]
    # Graceful restart period. | Default: 120 | Min: 1 | Max: 3600
    restart_period: int
    # Enable/disable continuing graceful restart upon topology cha | Default: disable
    restart_on_topology_change: Literal["enable", "disable"]
    # OSPF area configuration.
    area: list[OspfAreaObject]
    # OSPF interface configuration.
    ospf_interface: list[OspfOspfinterfaceObject]
    # OSPF network configuration.
    network: list[OspfNetworkObject]
    # OSPF neighbor configuration are used when OSPF runs on non-b
    neighbor: list[OspfNeighborObject]
    # Passive interface configuration.
    passive_interface: list[OspfPassiveinterfaceObject]
    # IP address summary configuration.
    summary_address: list[OspfSummaryaddressObject]
    # Distribute list configuration.
    distribute_list: list[OspfDistributelistObject]
    # Redistribute configuration.
    redistribute: list[OspfRedistributeObject]
    
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
    def to_dict(self) -> OspfPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ospf:
    """
    Configure OSPF.
    
    Path: router/ospf
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject: ...
    
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
    ) -> OspfObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> OspfObject: ...
    
    @overload
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: OspfPayload | None = ...,
        abr_type: Literal["cisco", "ibm", "shortcut", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        distance_external: int | None = ...,
        distance_inter_area: int | None = ...,
        distance_intra_area: int | None = ...,
        database_overflow: Literal["enable", "disable"] | None = ...,
        database_overflow_max_lsas: int | None = ...,
        database_overflow_time_to_recover: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        distance: int | None = ...,
        lsa_refresh_interval: int | None = ...,
        rfc1583_compatible: Literal["enable", "disable"] | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        distribute_list_in: str | None = ...,
        distribute_route_map_in: str | None = ...,
        restart_mode: Literal["none", "lls", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        distribute_list: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ospf",
    "OspfPayload",
    "OspfResponse",
    "OspfObject",
]
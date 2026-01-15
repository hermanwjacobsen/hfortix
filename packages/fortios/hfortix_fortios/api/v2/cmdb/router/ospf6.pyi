from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Ospf6Payload(TypedDict, total=False):
    """
    Type hints for router/ospf6 payload fields.
    
    Configure IPv6 OSPF.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.route-map.RouteMapEndpoint` (via: default-information-route-map)

    **Usage:**
        payload: Ospf6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    abr_type: Literal["cisco", "ibm", "standard"]  # Area border router type. | Default: standard
    auto_cost_ref_bandwidth: int  # Reference bandwidth in terms of megabits per secon | Default: 1000 | Min: 1 | Max: 1000000
    default_information_originate: Literal["enable", "always", "disable"]  # Enable/disable generation of default route. | Default: disable
    log_neighbour_changes: Literal["enable", "disable"]  # Log OSPFv3 neighbor changes. | Default: enable
    default_information_metric: int  # Default information metric. | Default: 10 | Min: 1 | Max: 16777214
    default_information_metric_type: Literal["1", "2"]  # Default information metric type. | Default: 2
    default_information_route_map: str  # Default information route map. | MaxLen: 35
    default_metric: int  # Default metric of redistribute routes. | Default: 10 | Min: 1 | Max: 16777214
    router_id: str  # A.B.C.D, in IPv4 address format. | Default: 0.0.0.0
    spf_timers: str  # SPF calculation frequency.
    bfd: Literal["enable", "disable"]  # Enable/disable Bidirectional Forwarding Detection | Default: disable
    restart_mode: Literal["none", "graceful-restart"]  # OSPFv3 restart mode (graceful or none). | Default: none
    restart_period: int  # Graceful restart period in seconds. | Default: 120 | Min: 1 | Max: 3600
    restart_on_topology_change: Literal["enable", "disable"]  # Enable/disable continuing graceful restart upon to | Default: disable
    area: list[dict[str, Any]]  # OSPF6 area configuration.
    ospf6_interface: list[dict[str, Any]]  # OSPF6 interface configuration.
    redistribute: list[dict[str, Any]]  # Redistribute configuration.
    passive_interface: list[dict[str, Any]]  # Passive interface configuration.
    summary_address: list[dict[str, Any]]  # IPv6 address summary configuration.

# Nested TypedDicts for table field children (dict mode)

class Ospf6AreaItem(TypedDict):
    """Type hints for area table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: str  # Area entry IP address. | Default: 0.0.0.0
    default_cost: int  # Summary default cost of stub or NSSA area. | Default: 10 | Min: 0 | Max: 16777215
    nssa_translator_role: Literal["candidate", "never", "always"]  # NSSA translator role type. | Default: candidate
    stub_type: Literal["no-summary", "summary"]  # Stub summary setting. | Default: summary
    type: Literal["regular", "nssa", "stub"]  # Area type setting. | Default: regular
    nssa_default_information_originate: Literal["enable", "disable"]  # Enable/disable originate type 7 default into NSSA | Default: disable
    nssa_default_information_originate_metric: int  # OSPFv3 default metric. | Default: 10 | Min: 0 | Max: 16777214
    nssa_default_information_originate_metric_type: Literal["1", "2"]  # OSPFv3 metric type for default routes. | Default: 2
    nssa_redistribution: Literal["enable", "disable"]  # Enable/disable redistribute into NSSA area. | Default: enable
    authentication: Literal["none", "ah", "esp"]  # Authentication mode. | Default: none
    key_rollover_interval: int  # Key roll-over interval. | Default: 300 | Min: 300 | Max: 216000
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]  # Authentication algorithm. | Default: md5
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]  # Encryption algorithm. | Default: null
    ipsec_keys: str  # IPsec authentication and encryption keys.
    range: str  # OSPF6 area range configuration.
    virtual_link: str  # OSPF6 virtual link configuration.


class Ospf6Ospf6interfaceItem(TypedDict):
    """Type hints for ospf6-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface entry name. | MaxLen: 35
    area_id: str  # A.B.C.D, in IPv4 address format. | Default: 0.0.0.0
    interface: str  # Configuration interface name. | MaxLen: 15
    retransmit_interval: int  # Retransmit interval. | Default: 5 | Min: 1 | Max: 65535
    transmit_delay: int  # Transmit delay. | Default: 1 | Min: 1 | Max: 65535
    cost: int  # Cost of the interface, value range from 0 to 65535 | Default: 0 | Min: 0 | Max: 65535
    priority: int  # Priority. | Default: 1 | Min: 0 | Max: 255
    dead_interval: int  # Dead interval. | Default: 0 | Min: 1 | Max: 65535
    hello_interval: int  # Hello interval. | Default: 0 | Min: 1 | Max: 65535
    status: Literal["disable", "enable"]  # Enable/disable OSPF6 routing on this interface. | Default: enable
    network_type: Literal["broadcast", "point-to-point", "non-broadcast", "point-to-multipoint", "point-to-multipoint-non-broadcast"]  # Network type. | Default: broadcast
    bfd: Literal["global", "enable", "disable"]  # Enable/disable Bidirectional Forwarding Detection | Default: global
    mtu: int  # MTU for OSPFv3 packets. | Default: 0 | Min: 576 | Max: 65535
    mtu_ignore: Literal["enable", "disable"]  # Enable/disable ignoring MTU field in DBD packets. | Default: disable
    authentication: Literal["none", "ah", "esp", "area"]  # Authentication mode. | Default: area
    key_rollover_interval: int  # Key roll-over interval. | Default: 300 | Min: 300 | Max: 216000
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]  # Authentication algorithm. | Default: md5
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]  # Encryption algorithm. | Default: null
    ipsec_keys: str  # IPsec authentication and encryption keys.
    neighbor: str  # OSPFv3 neighbors are used when OSPFv3 runs on non-


class Ospf6RedistributeItem(TypedDict):
    """Type hints for redistribute table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Redistribute name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Status. | Default: disable
    metric: int  # Redistribute metric setting. | Default: 0 | Min: 0 | Max: 16777214
    routemap: str  # Route map name. | MaxLen: 35
    metric_type: Literal["1", "2"]  # Metric type. | Default: 2


class Ospf6PassiveinterfaceItem(TypedDict):
    """Type hints for passive-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Passive interface name. | MaxLen: 79


class Ospf6SummaryaddressItem(TypedDict):
    """Type hints for summary-address table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Summary address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix6: str  # IPv6 prefix. | Default: ::/0
    advertise: Literal["disable", "enable"]  # Enable/disable advertise status. | Default: enable
    tag: int  # Tag value. | Default: 0 | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class Ospf6AreaObject:
    """Typed object for area table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Area entry IP address. | Default: 0.0.0.0
    id: str
    # Summary default cost of stub or NSSA area. | Default: 10 | Min: 0 | Max: 16777215
    default_cost: int
    # NSSA translator role type. | Default: candidate
    nssa_translator_role: Literal["candidate", "never", "always"]
    # Stub summary setting. | Default: summary
    stub_type: Literal["no-summary", "summary"]
    # Area type setting. | Default: regular
    type: Literal["regular", "nssa", "stub"]
    # Enable/disable originate type 7 default into NSSA area. | Default: disable
    nssa_default_information_originate: Literal["enable", "disable"]
    # OSPFv3 default metric. | Default: 10 | Min: 0 | Max: 16777214
    nssa_default_information_originate_metric: int
    # OSPFv3 metric type for default routes. | Default: 2
    nssa_default_information_originate_metric_type: Literal["1", "2"]
    # Enable/disable redistribute into NSSA area. | Default: enable
    nssa_redistribution: Literal["enable", "disable"]
    # Authentication mode. | Default: none
    authentication: Literal["none", "ah", "esp"]
    # Key roll-over interval. | Default: 300 | Min: 300 | Max: 216000
    key_rollover_interval: int
    # Authentication algorithm. | Default: md5
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]
    # Encryption algorithm. | Default: null
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]
    # IPsec authentication and encryption keys.
    ipsec_keys: str
    # OSPF6 area range configuration.
    range: str
    # OSPF6 virtual link configuration.
    virtual_link: str
    
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
class Ospf6Ospf6interfaceObject:
    """Typed object for ospf6-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface entry name. | MaxLen: 35
    name: str
    # A.B.C.D, in IPv4 address format. | Default: 0.0.0.0
    area_id: str
    # Configuration interface name. | MaxLen: 15
    interface: str
    # Retransmit interval. | Default: 5 | Min: 1 | Max: 65535
    retransmit_interval: int
    # Transmit delay. | Default: 1 | Min: 1 | Max: 65535
    transmit_delay: int
    # Cost of the interface, value range from 0 to 65535, 0 means | Default: 0 | Min: 0 | Max: 65535
    cost: int
    # Priority. | Default: 1 | Min: 0 | Max: 255
    priority: int
    # Dead interval. | Default: 0 | Min: 1 | Max: 65535
    dead_interval: int
    # Hello interval. | Default: 0 | Min: 1 | Max: 65535
    hello_interval: int
    # Enable/disable OSPF6 routing on this interface. | Default: enable
    status: Literal["disable", "enable"]
    # Network type. | Default: broadcast
    network_type: Literal["broadcast", "point-to-point", "non-broadcast", "point-to-multipoint", "point-to-multipoint-non-broadcast"]
    # Enable/disable Bidirectional Forwarding Detection (BFD). | Default: global
    bfd: Literal["global", "enable", "disable"]
    # MTU for OSPFv3 packets. | Default: 0 | Min: 576 | Max: 65535
    mtu: int
    # Enable/disable ignoring MTU field in DBD packets. | Default: disable
    mtu_ignore: Literal["enable", "disable"]
    # Authentication mode. | Default: area
    authentication: Literal["none", "ah", "esp", "area"]
    # Key roll-over interval. | Default: 300 | Min: 300 | Max: 216000
    key_rollover_interval: int
    # Authentication algorithm. | Default: md5
    ipsec_auth_alg: Literal["md5", "sha1", "sha256", "sha384", "sha512"]
    # Encryption algorithm. | Default: null
    ipsec_enc_alg: Literal["null", "des", "3des", "aes128", "aes192", "aes256"]
    # IPsec authentication and encryption keys.
    ipsec_keys: str
    # OSPFv3 neighbors are used when OSPFv3 runs on non-broadcast
    neighbor: str
    
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
class Ospf6RedistributeObject:
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
class Ospf6PassiveinterfaceObject:
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
class Ospf6SummaryaddressObject:
    """Typed object for summary-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Summary address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IPv6 prefix. | Default: ::/0
    prefix6: str
    # Enable/disable advertise status. | Default: enable
    advertise: Literal["disable", "enable"]
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
class Ospf6Response(TypedDict):
    """
    Type hints for router/ospf6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    abr_type: Literal["cisco", "ibm", "standard"]  # Area border router type. | Default: standard
    auto_cost_ref_bandwidth: int  # Reference bandwidth in terms of megabits per secon | Default: 1000 | Min: 1 | Max: 1000000
    default_information_originate: Literal["enable", "always", "disable"]  # Enable/disable generation of default route. | Default: disable
    log_neighbour_changes: Literal["enable", "disable"]  # Log OSPFv3 neighbor changes. | Default: enable
    default_information_metric: int  # Default information metric. | Default: 10 | Min: 1 | Max: 16777214
    default_information_metric_type: Literal["1", "2"]  # Default information metric type. | Default: 2
    default_information_route_map: str  # Default information route map. | MaxLen: 35
    default_metric: int  # Default metric of redistribute routes. | Default: 10 | Min: 1 | Max: 16777214
    router_id: str  # A.B.C.D, in IPv4 address format. | Default: 0.0.0.0
    spf_timers: str  # SPF calculation frequency.
    bfd: Literal["enable", "disable"]  # Enable/disable Bidirectional Forwarding Detection | Default: disable
    restart_mode: Literal["none", "graceful-restart"]  # OSPFv3 restart mode (graceful or none). | Default: none
    restart_period: int  # Graceful restart period in seconds. | Default: 120 | Min: 1 | Max: 3600
    restart_on_topology_change: Literal["enable", "disable"]  # Enable/disable continuing graceful restart upon to | Default: disable
    area: list[Ospf6AreaItem]  # OSPF6 area configuration.
    ospf6_interface: list[Ospf6Ospf6interfaceItem]  # OSPF6 interface configuration.
    redistribute: list[Ospf6RedistributeItem]  # Redistribute configuration.
    passive_interface: list[Ospf6PassiveinterfaceItem]  # Passive interface configuration.
    summary_address: list[Ospf6SummaryaddressItem]  # IPv6 address summary configuration.


@final
class Ospf6Object:
    """Typed FortiObject for router/ospf6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Area border router type. | Default: standard
    abr_type: Literal["cisco", "ibm", "standard"]
    # Reference bandwidth in terms of megabits per second. | Default: 1000 | Min: 1 | Max: 1000000
    auto_cost_ref_bandwidth: int
    # Enable/disable generation of default route. | Default: disable
    default_information_originate: Literal["enable", "always", "disable"]
    # Log OSPFv3 neighbor changes. | Default: enable
    log_neighbour_changes: Literal["enable", "disable"]
    # Default information metric. | Default: 10 | Min: 1 | Max: 16777214
    default_information_metric: int
    # Default information metric type. | Default: 2
    default_information_metric_type: Literal["1", "2"]
    # Default information route map. | MaxLen: 35
    default_information_route_map: str
    # Default metric of redistribute routes. | Default: 10 | Min: 1 | Max: 16777214
    default_metric: int
    # A.B.C.D, in IPv4 address format. | Default: 0.0.0.0
    router_id: str
    # SPF calculation frequency.
    spf_timers: str
    # Enable/disable Bidirectional Forwarding Detection (BFD). | Default: disable
    bfd: Literal["enable", "disable"]
    # OSPFv3 restart mode (graceful or none). | Default: none
    restart_mode: Literal["none", "graceful-restart"]
    # Graceful restart period in seconds. | Default: 120 | Min: 1 | Max: 3600
    restart_period: int
    # Enable/disable continuing graceful restart upon topology cha | Default: disable
    restart_on_topology_change: Literal["enable", "disable"]
    # OSPF6 area configuration.
    area: list[Ospf6AreaObject]
    # OSPF6 interface configuration.
    ospf6_interface: list[Ospf6Ospf6interfaceObject]
    # Redistribute configuration.
    redistribute: list[Ospf6RedistributeObject]
    # Passive interface configuration.
    passive_interface: list[Ospf6PassiveinterfaceObject]
    # IPv6 address summary configuration.
    summary_address: list[Ospf6SummaryaddressObject]
    
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
    def to_dict(self) -> Ospf6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ospf6:
    """
    Configure IPv6 OSPF.
    
    Path: router/ospf6
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object: ...
    
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
    ) -> Ospf6Object | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Ospf6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: Ospf6Payload | None = ...,
        abr_type: Literal["cisco", "ibm", "standard"] | None = ...,
        auto_cost_ref_bandwidth: int | None = ...,
        default_information_originate: Literal["enable", "always", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        default_information_metric: int | None = ...,
        default_information_metric_type: Literal["1", "2"] | None = ...,
        default_information_route_map: str | None = ...,
        default_metric: int | None = ...,
        router_id: str | None = ...,
        spf_timers: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        restart_mode: Literal["none", "graceful-restart"] | None = ...,
        restart_period: int | None = ...,
        restart_on_topology_change: Literal["enable", "disable"] | None = ...,
        area: str | list[str] | list[dict[str, Any]] | None = ...,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ospf6",
    "Ospf6Payload",
    "Ospf6Response",
    "Ospf6Object",
]
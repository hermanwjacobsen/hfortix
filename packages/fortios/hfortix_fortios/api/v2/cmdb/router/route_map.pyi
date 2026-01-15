from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RouteMapPayload(TypedDict, total=False):
    """
    Type hints for router/route_map payload fields.
    
    Configure route maps.
    
    **Usage:**
        payload: RouteMapPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    comments: str  # Optional comments. | MaxLen: 127
    rule: list[dict[str, Any]]  # Rule.

# Nested TypedDicts for table field children (dict mode)

class RouteMapRuleItem(TypedDict):
    """Type hints for rule table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Rule ID. | Default: 0 | Min: 0 | Max: 4294967295
    action: Literal["permit", "deny"]  # Action. | Default: permit
    match_as_path: str  # Match BGP AS path list. | MaxLen: 35
    match_community: str  # Match BGP community list. | MaxLen: 35
    match_extcommunity: str  # Match BGP extended community list. | MaxLen: 35
    match_community_exact: Literal["enable", "disable"]  # Enable/disable exact matching of communities. | Default: disable
    match_extcommunity_exact: Literal["enable", "disable"]  # Enable/disable exact matching of extended communit | Default: disable
    match_origin: Literal["none", "egp", "igp", "incomplete"]  # Match BGP origin code. | Default: none
    match_interface: str  # Match interface configuration. | MaxLen: 15
    match_ip_address: str  # Match IP address permitted by access-list or prefi | MaxLen: 35
    match_ip6_address: str  # Match IPv6 address permitted by access-list6 or pr | MaxLen: 35
    match_ip_nexthop: str  # Match next hop IP address passed by access-list or | MaxLen: 35
    match_ip6_nexthop: str  # Match next hop IPv6 address passed by access-list6 | MaxLen: 35
    match_metric: int  # Match metric for redistribute routes. | Min: 0 | Max: 4294967295
    match_route_type: Literal["external-type1", "external-type2", "none"]  # Match route type.
    match_tag: int  # Match tag. | Min: 0 | Max: 4294967295
    match_vrf: int  # Match VRF ID. | Min: 0 | Max: 511
    match_suppress: Literal["enable", "disable"]  # Enable/disable matching of suppressed original nei | Default: disable
    set_aggregator_as: int  # BGP aggregator AS. | Default: 0 | Min: 0 | Max: 4294967295
    set_aggregator_ip: str  # BGP aggregator IP. | Default: 0.0.0.0
    set_aspath_action: Literal["prepend", "replace"]  # Specify preferred action of set-aspath. | Default: prepend
    set_aspath: str  # Prepend BGP AS path attribute.
    set_atomic_aggregate: Literal["enable", "disable"]  # Enable/disable BGP atomic aggregate attribute. | Default: disable
    set_community_delete: str  # Delete communities matching community list. | MaxLen: 35
    set_community: str  # BGP community attribute.
    set_community_additive: Literal["enable", "disable"]  # Enable/disable adding set-community to existing co | Default: disable
    set_dampening_reachability_half_life: int  # Reachability half-life time for the penalty | Default: 0 | Min: 0 | Max: 45
    set_dampening_reuse: int  # Value to start reusing a route | Default: 0 | Min: 0 | Max: 20000
    set_dampening_suppress: int  # Value to start suppressing a route | Default: 0 | Min: 0 | Max: 20000
    set_dampening_max_suppress: int  # Maximum duration to suppress a route | Default: 0 | Min: 0 | Max: 255
    set_dampening_unreachability_half_life: int  # Unreachability Half-life time for the penalty | Default: 0 | Min: 0 | Max: 45
    set_extcommunity_rt: str  # Route Target extended community.
    set_extcommunity_soo: str  # Site-of-Origin extended community.
    set_ip_nexthop: str  # IP address of next hop.
    set_ip_prefsrc: str  # IP address of preferred source.
    set_vpnv4_nexthop: str  # IP address of VPNv4 next-hop.
    set_ip6_nexthop: str  # IPv6 global address of next hop.
    set_ip6_nexthop_local: str  # IPv6 local address of next hop.
    set_vpnv6_nexthop: str  # IPv6 global address of VPNv6 next-hop.
    set_vpnv6_nexthop_local: str  # IPv6 link-local address of VPNv6 next-hop.
    set_local_preference: int  # BGP local preference path attribute. | Min: 0 | Max: 4294967295
    set_metric: int  # Metric value. | Min: 0 | Max: 4294967295
    set_metric_type: Literal["external-type1", "external-type2", "none"]  # Metric type.
    set_originator_id: str  # BGP originator ID attribute.
    set_origin: Literal["none", "egp", "igp", "incomplete"]  # BGP origin code. | Default: none
    set_tag: int  # Tag value. | Min: 0 | Max: 4294967295
    set_weight: int  # BGP weight for routing table. | Min: 0 | Max: 4294967295
    set_route_tag: int  # Route tag for routing table. | Min: 0 | Max: 4294967295
    set_priority: int  # Priority for routing table. | Min: 1 | Max: 65535


# Nested classes for table field children (object mode)

@final
class RouteMapRuleObject:
    """Typed object for rule table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Rule ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Action. | Default: permit
    action: Literal["permit", "deny"]
    # Match BGP AS path list. | MaxLen: 35
    match_as_path: str
    # Match BGP community list. | MaxLen: 35
    match_community: str
    # Match BGP extended community list. | MaxLen: 35
    match_extcommunity: str
    # Enable/disable exact matching of communities. | Default: disable
    match_community_exact: Literal["enable", "disable"]
    # Enable/disable exact matching of extended communities. | Default: disable
    match_extcommunity_exact: Literal["enable", "disable"]
    # Match BGP origin code. | Default: none
    match_origin: Literal["none", "egp", "igp", "incomplete"]
    # Match interface configuration. | MaxLen: 15
    match_interface: str
    # Match IP address permitted by access-list or prefix-list. | MaxLen: 35
    match_ip_address: str
    # Match IPv6 address permitted by access-list6 or prefix-list6 | MaxLen: 35
    match_ip6_address: str
    # Match next hop IP address passed by access-list or prefix-li | MaxLen: 35
    match_ip_nexthop: str
    # Match next hop IPv6 address passed by access-list6 or prefix | MaxLen: 35
    match_ip6_nexthop: str
    # Match metric for redistribute routes. | Min: 0 | Max: 4294967295
    match_metric: int
    # Match route type.
    match_route_type: Literal["external-type1", "external-type2", "none"]
    # Match tag. | Min: 0 | Max: 4294967295
    match_tag: int
    # Match VRF ID. | Min: 0 | Max: 511
    match_vrf: int
    # Enable/disable matching of suppressed original neighbor. | Default: disable
    match_suppress: Literal["enable", "disable"]
    # BGP aggregator AS. | Default: 0 | Min: 0 | Max: 4294967295
    set_aggregator_as: int
    # BGP aggregator IP. | Default: 0.0.0.0
    set_aggregator_ip: str
    # Specify preferred action of set-aspath. | Default: prepend
    set_aspath_action: Literal["prepend", "replace"]
    # Prepend BGP AS path attribute.
    set_aspath: str
    # Enable/disable BGP atomic aggregate attribute. | Default: disable
    set_atomic_aggregate: Literal["enable", "disable"]
    # Delete communities matching community list. | MaxLen: 35
    set_community_delete: str
    # BGP community attribute.
    set_community: str
    # Enable/disable adding set-community to existing community. | Default: disable
    set_community_additive: Literal["enable", "disable"]
    # Reachability half-life time for the penalty | Default: 0 | Min: 0 | Max: 45
    set_dampening_reachability_half_life: int
    # Value to start reusing a route (1 - 20000, 0 = unset). | Default: 0 | Min: 0 | Max: 20000
    set_dampening_reuse: int
    # Value to start suppressing a route (1 - 20000, 0 = unset). | Default: 0 | Min: 0 | Max: 20000
    set_dampening_suppress: int
    # Maximum duration to suppress a route | Default: 0 | Min: 0 | Max: 255
    set_dampening_max_suppress: int
    # Unreachability Half-life time for the penalty | Default: 0 | Min: 0 | Max: 45
    set_dampening_unreachability_half_life: int
    # Route Target extended community.
    set_extcommunity_rt: str
    # Site-of-Origin extended community.
    set_extcommunity_soo: str
    # IP address of next hop.
    set_ip_nexthop: str
    # IP address of preferred source.
    set_ip_prefsrc: str
    # IP address of VPNv4 next-hop.
    set_vpnv4_nexthop: str
    # IPv6 global address of next hop.
    set_ip6_nexthop: str
    # IPv6 local address of next hop.
    set_ip6_nexthop_local: str
    # IPv6 global address of VPNv6 next-hop.
    set_vpnv6_nexthop: str
    # IPv6 link-local address of VPNv6 next-hop.
    set_vpnv6_nexthop_local: str
    # BGP local preference path attribute. | Min: 0 | Max: 4294967295
    set_local_preference: int
    # Metric value. | Min: 0 | Max: 4294967295
    set_metric: int
    # Metric type.
    set_metric_type: Literal["external-type1", "external-type2", "none"]
    # BGP originator ID attribute.
    set_originator_id: str
    # BGP origin code. | Default: none
    set_origin: Literal["none", "egp", "igp", "incomplete"]
    # Tag value. | Min: 0 | Max: 4294967295
    set_tag: int
    # BGP weight for routing table. | Min: 0 | Max: 4294967295
    set_weight: int
    # Route tag for routing table. | Min: 0 | Max: 4294967295
    set_route_tag: int
    # Priority for routing table. | Min: 1 | Max: 65535
    set_priority: int
    
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
class RouteMapResponse(TypedDict):
    """
    Type hints for router/route_map API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    comments: str  # Optional comments. | MaxLen: 127
    rule: list[RouteMapRuleItem]  # Rule.


@final
class RouteMapObject:
    """Typed FortiObject for router/route_map with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Optional comments. | MaxLen: 127
    comments: str
    # Rule.
    rule: list[RouteMapRuleObject]
    
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
    def to_dict(self) -> RouteMapPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class RouteMap:
    """
    Configure route maps.
    
    Path: router/route_map
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
    ) -> RouteMapObject: ...
    
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
    ) -> RouteMapObject: ...
    
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
    ) -> FortiObjectList[RouteMapObject]: ...
    
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
    ) -> RouteMapObject: ...
    
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
    ) -> RouteMapObject: ...
    
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
    ) -> FortiObjectList[RouteMapObject]: ...
    
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
    ) -> RouteMapObject: ...
    
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
    ) -> RouteMapObject: ...
    
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
    ) -> FortiObjectList[RouteMapObject]: ...
    
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
    ) -> RouteMapObject | list[RouteMapObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RouteMapObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RouteMapObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> RouteMapObject: ...
    
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
        payload_dict: RouteMapPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "RouteMap",
    "RouteMapPayload",
    "RouteMapResponse",
    "RouteMapObject",
]
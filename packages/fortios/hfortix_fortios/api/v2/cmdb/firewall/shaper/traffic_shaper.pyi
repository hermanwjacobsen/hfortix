from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class TrafficShaperPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaper/traffic_shaper payload fields.
    
    Configure shared traffic shaper.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.traffic-class.TrafficClassEndpoint` (via: exceed-class-id)

    **Usage:**
        payload: TrafficShaperPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Traffic shaper name. | MaxLen: 35
    guaranteed_bandwidth: int  # Amount of bandwidth guaranteed for this shaper | Default: 0 | Min: 0 | Max: 80000000
    maximum_bandwidth: int  # Upper bandwidth limit enforced by this shaper | Default: 0 | Min: 0 | Max: 80000000
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]  # Unit of measurement for guaranteed and maximum ban | Default: kbps
    priority: Literal["low", "medium", "high"]  # Higher priority traffic is more likely to be forwa | Default: high
    per_policy: Literal["disable", "enable"]  # Enable/disable applying a separate shaper for each | Default: disable
    diffserv: Literal["enable", "disable"]  # Enable/disable changing the DiffServ setting appli | Default: disable
    diffservcode: str  # DiffServ setting to be applied to traffic accepted
    dscp_marking_method: Literal["multi-stage", "static"]  # Select DSCP marking method. | Default: static
    exceed_bandwidth: int  # Exceed bandwidth used for DSCP/VLAN CoS multi-stag | Default: 0 | Min: 0 | Max: 80000000
    exceed_dscp: str  # DSCP mark for traffic in guaranteed-bandwidth and
    maximum_dscp: str  # DSCP mark for traffic in exceed-bandwidth and maxi
    cos_marking: Literal["enable", "disable"]  # Enable/disable VLAN CoS marking. | Default: disable
    cos_marking_method: Literal["multi-stage", "static"]  # Select VLAN CoS marking method. | Default: static
    cos: str  # VLAN CoS mark.
    exceed_cos: str  # VLAN CoS mark for traffic in
    maximum_cos: str  # VLAN CoS mark for traffic in
    overhead: int  # Per-packet size overhead used in rate computations | Default: 0 | Min: 0 | Max: 100
    exceed_class_id: int  # Class ID for traffic in guaranteed-bandwidth and m | Default: 0 | Min: 0 | Max: 4294967295

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class TrafficShaperResponse(TypedDict):
    """
    Type hints for firewall/shaper/traffic_shaper API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Traffic shaper name. | MaxLen: 35
    guaranteed_bandwidth: int  # Amount of bandwidth guaranteed for this shaper | Default: 0 | Min: 0 | Max: 80000000
    maximum_bandwidth: int  # Upper bandwidth limit enforced by this shaper | Default: 0 | Min: 0 | Max: 80000000
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]  # Unit of measurement for guaranteed and maximum ban | Default: kbps
    priority: Literal["low", "medium", "high"]  # Higher priority traffic is more likely to be forwa | Default: high
    per_policy: Literal["disable", "enable"]  # Enable/disable applying a separate shaper for each | Default: disable
    diffserv: Literal["enable", "disable"]  # Enable/disable changing the DiffServ setting appli | Default: disable
    diffservcode: str  # DiffServ setting to be applied to traffic accepted
    dscp_marking_method: Literal["multi-stage", "static"]  # Select DSCP marking method. | Default: static
    exceed_bandwidth: int  # Exceed bandwidth used for DSCP/VLAN CoS multi-stag | Default: 0 | Min: 0 | Max: 80000000
    exceed_dscp: str  # DSCP mark for traffic in guaranteed-bandwidth and
    maximum_dscp: str  # DSCP mark for traffic in exceed-bandwidth and maxi
    cos_marking: Literal["enable", "disable"]  # Enable/disable VLAN CoS marking. | Default: disable
    cos_marking_method: Literal["multi-stage", "static"]  # Select VLAN CoS marking method. | Default: static
    cos: str  # VLAN CoS mark.
    exceed_cos: str  # VLAN CoS mark for traffic in
    maximum_cos: str  # VLAN CoS mark for traffic in
    overhead: int  # Per-packet size overhead used in rate computations | Default: 0 | Min: 0 | Max: 100
    exceed_class_id: int  # Class ID for traffic in guaranteed-bandwidth and m | Default: 0 | Min: 0 | Max: 4294967295


@final
class TrafficShaperObject:
    """Typed FortiObject for firewall/shaper/traffic_shaper with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Traffic shaper name. | MaxLen: 35
    name: str
    # Amount of bandwidth guaranteed for this shaper | Default: 0 | Min: 0 | Max: 80000000
    guaranteed_bandwidth: int
    # Upper bandwidth limit enforced by this shaper (0 - 80000000) | Default: 0 | Min: 0 | Max: 80000000
    maximum_bandwidth: int
    # Unit of measurement for guaranteed and maximum bandwidth for | Default: kbps
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]
    # Higher priority traffic is more likely to be forwarded witho | Default: high
    priority: Literal["low", "medium", "high"]
    # Enable/disable applying a separate shaper for each policy. F | Default: disable
    per_policy: Literal["disable", "enable"]
    # Enable/disable changing the DiffServ setting applied to traf | Default: disable
    diffserv: Literal["enable", "disable"]
    # DiffServ setting to be applied to traffic accepted by this s
    diffservcode: str
    # Select DSCP marking method. | Default: static
    dscp_marking_method: Literal["multi-stage", "static"]
    # Exceed bandwidth used for DSCP/VLAN CoS multi-stage marking. | Default: 0 | Min: 0 | Max: 80000000
    exceed_bandwidth: int
    # DSCP mark for traffic in guaranteed-bandwidth and exceed-ban
    exceed_dscp: str
    # DSCP mark for traffic in exceed-bandwidth and maximum-bandwi
    maximum_dscp: str
    # Enable/disable VLAN CoS marking. | Default: disable
    cos_marking: Literal["enable", "disable"]
    # Select VLAN CoS marking method. | Default: static
    cos_marking_method: Literal["multi-stage", "static"]
    # VLAN CoS mark.
    cos: str
    # VLAN CoS mark for traffic in
    exceed_cos: str
    # VLAN CoS mark for traffic in
    maximum_cos: str
    # Per-packet size overhead used in rate computations. | Default: 0 | Min: 0 | Max: 100
    overhead: int
    # Class ID for traffic in guaranteed-bandwidth and maximum-ban | Default: 0 | Min: 0 | Max: 4294967295
    exceed_class_id: int
    
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
    def to_dict(self) -> TrafficShaperPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TrafficShaper:
    """
    Configure shared traffic shaper.
    
    Path: firewall/shaper/traffic_shaper
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
    ) -> TrafficShaperObject: ...
    
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
    ) -> TrafficShaperObject: ...
    
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
    ) -> list[TrafficShaperObject]: ...
    
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
    ) -> TrafficShaperObject: ...
    
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
    ) -> TrafficShaperObject: ...
    
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
    ) -> list[TrafficShaperObject]: ...
    
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
    ) -> TrafficShaperObject: ...
    
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
    ) -> TrafficShaperObject: ...
    
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
    ) -> list[TrafficShaperObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> TrafficShaperObject | list[TrafficShaperObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> TrafficShaperObject: ...
    
    @overload
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> TrafficShaperObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> TrafficShaperObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
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
        payload_dict: TrafficShaperPayload | None = ...,
        name: str | None = ...,
        guaranteed_bandwidth: int | None = ...,
        maximum_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        per_policy: Literal["disable", "enable"] | None = ...,
        diffserv: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        dscp_marking_method: Literal["multi-stage", "static"] | None = ...,
        exceed_bandwidth: int | None = ...,
        exceed_dscp: str | None = ...,
        maximum_dscp: str | None = ...,
        cos_marking: Literal["enable", "disable"] | None = ...,
        cos_marking_method: Literal["multi-stage", "static"] | None = ...,
        cos: str | None = ...,
        exceed_cos: str | None = ...,
        maximum_cos: str | None = ...,
        overhead: int | None = ...,
        exceed_class_id: int | None = ...,
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
    "TrafficShaper",
    "TrafficShaperPayload",
    "TrafficShaperResponse",
    "TrafficShaperObject",
]
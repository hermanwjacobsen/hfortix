from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class H2qpWanMetricPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/hotspot20/h2qp_wan_metric payload fields.
    
    Configure WAN metrics.
    
    **Usage:**
        payload: H2qpWanMetricPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # WAN metric name. | MaxLen: 35
    link_status: Literal["up", "down", "in-test"]  # Link status. | Default: up
    symmetric_wan_link: Literal["symmetric", "asymmetric"]  # WAN link symmetry. | Default: asymmetric
    link_at_capacity: Literal["enable", "disable"]  # Link at capacity. | Default: disable
    uplink_speed: int  # Uplink speed (in kilobits/s). | Default: 2400 | Min: 0 | Max: 4294967295
    downlink_speed: int  # Downlink speed (in kilobits/s). | Default: 2400 | Min: 0 | Max: 4294967295
    uplink_load: int  # Uplink load. | Default: 0 | Min: 0 | Max: 255
    downlink_load: int  # Downlink load. | Default: 0 | Min: 0 | Max: 255
    load_measurement_duration: int  # Load measurement duration (in tenths of a second). | Default: 0 | Min: 0 | Max: 65535

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class H2qpWanMetricResponse(TypedDict):
    """
    Type hints for wireless_controller/hotspot20/h2qp_wan_metric API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # WAN metric name. | MaxLen: 35
    link_status: Literal["up", "down", "in-test"]  # Link status. | Default: up
    symmetric_wan_link: Literal["symmetric", "asymmetric"]  # WAN link symmetry. | Default: asymmetric
    link_at_capacity: Literal["enable", "disable"]  # Link at capacity. | Default: disable
    uplink_speed: int  # Uplink speed (in kilobits/s). | Default: 2400 | Min: 0 | Max: 4294967295
    downlink_speed: int  # Downlink speed (in kilobits/s). | Default: 2400 | Min: 0 | Max: 4294967295
    uplink_load: int  # Uplink load. | Default: 0 | Min: 0 | Max: 255
    downlink_load: int  # Downlink load. | Default: 0 | Min: 0 | Max: 255
    load_measurement_duration: int  # Load measurement duration (in tenths of a second). | Default: 0 | Min: 0 | Max: 65535


@final
class H2qpWanMetricObject:
    """Typed FortiObject for wireless_controller/hotspot20/h2qp_wan_metric with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WAN metric name. | MaxLen: 35
    name: str
    # Link status. | Default: up
    link_status: Literal["up", "down", "in-test"]
    # WAN link symmetry. | Default: asymmetric
    symmetric_wan_link: Literal["symmetric", "asymmetric"]
    # Link at capacity. | Default: disable
    link_at_capacity: Literal["enable", "disable"]
    # Uplink speed (in kilobits/s). | Default: 2400 | Min: 0 | Max: 4294967295
    uplink_speed: int
    # Downlink speed (in kilobits/s). | Default: 2400 | Min: 0 | Max: 4294967295
    downlink_speed: int
    # Uplink load. | Default: 0 | Min: 0 | Max: 255
    uplink_load: int
    # Downlink load. | Default: 0 | Min: 0 | Max: 255
    downlink_load: int
    # Load measurement duration (in tenths of a second). | Default: 0 | Min: 0 | Max: 65535
    load_measurement_duration: int
    
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
    def to_dict(self) -> H2qpWanMetricPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class H2qpWanMetric:
    """
    Configure WAN metrics.
    
    Path: wireless_controller/hotspot20/h2qp_wan_metric
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> list[H2qpWanMetricObject]: ...
    
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> list[H2qpWanMetricObject]: ...
    
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> H2qpWanMetricObject: ...
    
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
    ) -> list[H2qpWanMetricObject]: ...
    
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
    ) -> H2qpWanMetricObject | list[H2qpWanMetricObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> H2qpWanMetricObject: ...
    
    @overload
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> H2qpWanMetricObject: ...
    
    @overload
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
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
    ) -> H2qpWanMetricObject: ...
    
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
        payload_dict: H2qpWanMetricPayload | None = ...,
        name: str | None = ...,
        link_status: Literal["up", "down", "in-test"] | None = ...,
        symmetric_wan_link: Literal["symmetric", "asymmetric"] | None = ...,
        link_at_capacity: Literal["enable", "disable"] | None = ...,
        uplink_speed: int | None = ...,
        downlink_speed: int | None = ...,
        uplink_load: int | None = ...,
        downlink_load: int | None = ...,
        load_measurement_duration: int | None = ...,
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
    "H2qpWanMetric",
    "H2qpWanMetricPayload",
    "H2qpWanMetricResponse",
    "H2qpWanMetricObject",
]
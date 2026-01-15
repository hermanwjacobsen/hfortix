from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ShapingProfilePayload(TypedDict, total=False):
    """
    Type hints for firewall/shaping_profile payload fields.
    
    Configure shaping profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.traffic-class.TrafficClassEndpoint` (via: default-class-id)

    **Usage:**
        payload: ShapingProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    profile_name: str  # Shaping profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 1023
    type: Literal["policing", "queuing"]  # Select shaping profile type: policing / queuing. | Default: policing
    npu_offloading: Literal["disable", "enable"]  # Enable/disable NPU offloading. | Default: enable
    default_class_id: int  # Default class ID to handle unclassified packets | Default: 0 | Min: 0 | Max: 4294967295
    shaping_entries: list[dict[str, Any]]  # Define shaping entries of this shaping profile.

# Nested TypedDicts for table field children (dict mode)

class ShapingProfileShapingentriesItem(TypedDict):
    """Type hints for shaping-entries table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID number. | Default: 0 | Min: 0 | Max: 4294967295
    class_id: int  # Class ID. | Default: 0 | Min: 0 | Max: 4294967295
    priority: Literal["top", "critical", "high", "medium", "low"]  # Priority. | Default: high
    guaranteed_bandwidth_percentage: int  # Guaranteed bandwidth in percentage. | Default: 0 | Min: 0 | Max: 100
    maximum_bandwidth_percentage: int  # Maximum bandwidth in percentage. | Default: 1 | Min: 1 | Max: 100
    limit: int  # Hard limit on the real queue size in packets. | Default: 100 | Min: 5 | Max: 10000
    burst_in_msec: int  # Number of bytes that can be burst at maximum-bandw | Default: 0 | Min: 0 | Max: 2000
    cburst_in_msec: int  # Number of bytes that can be burst as fast as the i | Default: 0 | Min: 0 | Max: 2000
    red_probability: int  # Maximum probability (in percentage) for RED markin | Default: 0 | Min: 0 | Max: 20
    min: int  # Average queue size in packets at which RED drop be | Default: 83 | Min: 3 | Max: 3000
    max: int  # Average queue size in packets at which RED drop pr | Default: 250 | Min: 3 | Max: 3000


# Nested classes for table field children (object mode)

@final
class ShapingProfileShapingentriesObject:
    """Typed object for shaping-entries table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID number. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Class ID. | Default: 0 | Min: 0 | Max: 4294967295
    class_id: int
    # Priority. | Default: high
    priority: Literal["top", "critical", "high", "medium", "low"]
    # Guaranteed bandwidth in percentage. | Default: 0 | Min: 0 | Max: 100
    guaranteed_bandwidth_percentage: int
    # Maximum bandwidth in percentage. | Default: 1 | Min: 1 | Max: 100
    maximum_bandwidth_percentage: int
    # Hard limit on the real queue size in packets. | Default: 100 | Min: 5 | Max: 10000
    limit: int
    # Number of bytes that can be burst at maximum-bandwidth speed | Default: 0 | Min: 0 | Max: 2000
    burst_in_msec: int
    # Number of bytes that can be burst as fast as the interface c | Default: 0 | Min: 0 | Max: 2000
    cburst_in_msec: int
    # Maximum probability (in percentage) for RED marking. | Default: 0 | Min: 0 | Max: 20
    red_probability: int
    # Average queue size in packets at which RED drop becomes a po | Default: 83 | Min: 3 | Max: 3000
    min: int
    # Average queue size in packets at which RED drop probability | Default: 250 | Min: 3 | Max: 3000
    max: int
    
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
class ShapingProfileResponse(TypedDict):
    """
    Type hints for firewall/shaping_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    profile_name: str  # Shaping profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 1023
    type: Literal["policing", "queuing"]  # Select shaping profile type: policing / queuing. | Default: policing
    npu_offloading: Literal["disable", "enable"]  # Enable/disable NPU offloading. | Default: enable
    default_class_id: int  # Default class ID to handle unclassified packets | Default: 0 | Min: 0 | Max: 4294967295
    shaping_entries: list[ShapingProfileShapingentriesItem]  # Define shaping entries of this shaping profile.


@final
class ShapingProfileObject:
    """Typed FortiObject for firewall/shaping_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Shaping profile name. | MaxLen: 35
    profile_name: str
    # Comment. | MaxLen: 1023
    comment: str
    # Select shaping profile type: policing / queuing. | Default: policing
    type: Literal["policing", "queuing"]
    # Enable/disable NPU offloading. | Default: enable
    npu_offloading: Literal["disable", "enable"]
    # Default class ID to handle unclassified packets | Default: 0 | Min: 0 | Max: 4294967295
    default_class_id: int
    # Define shaping entries of this shaping profile.
    shaping_entries: list[ShapingProfileShapingentriesObject]
    
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
    def to_dict(self) -> ShapingProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ShapingProfile:
    """
    Configure shaping profiles.
    
    Path: firewall/shaping_profile
    Category: cmdb
    Primary Key: profile-name
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        profile_name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        profile_name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        profile_name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ShapingProfileObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        profile_name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        profile_name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
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
    ) -> FortiObjectList[ShapingProfileObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        profile_name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        profile_name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
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
    ) -> FortiObjectList[ShapingProfileObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        profile_name: str | None = ...,
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
        profile_name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject | list[ShapingProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ShapingProfileObject: ...
    
    @overload
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        profile_name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        profile_name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ShapingProfilePayload | None = ...,
        profile_name: str | None = ...,
        comment: str | None = ...,
        type: Literal["policing", "queuing"] | None = ...,
        npu_offloading: Literal["disable", "enable"] | None = ...,
        default_class_id: int | None = ...,
        shaping_entries: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ShapingProfile",
    "ShapingProfilePayload",
    "ShapingProfileResponse",
    "ShapingProfileObject",
]
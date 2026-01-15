from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class QueuePolicyPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/qos/queue_policy payload fields.
    
    Configure FortiSwitch QoS egress queue policy.
    
    **Usage:**
        payload: QueuePolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # QoS policy name. | MaxLen: 63
    schedule: Literal["strict", "round-robin", "weighted"]  # COS queue scheduling. | Default: round-robin
    rate_by: Literal["kbps", "percent"]  # COS queue rate by kbps or percent. | Default: kbps
    cos_queue: list[dict[str, Any]]  # COS queue configuration.

# Nested TypedDicts for table field children (dict mode)

class QueuePolicyCosqueueItem(TypedDict):
    """Type hints for cos-queue table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Cos queue ID. | MaxLen: 63
    description: str  # Description of the COS queue. | MaxLen: 63
    min_rate: int  # Minimum rate (0 - 4294967295 kbps, 0 to disable). | Default: 0 | Min: 0 | Max: 4294967295
    max_rate: int  # Maximum rate (0 - 4294967295 kbps, 0 to disable). | Default: 0 | Min: 0 | Max: 4294967295
    min_rate_percent: int  # Minimum rate (% of link speed). | Default: 0 | Min: 0 | Max: 4294967295
    max_rate_percent: int  # Maximum rate (% of link speed). | Default: 0 | Min: 0 | Max: 4294967295
    drop_policy: Literal["taildrop", "weighted-random-early-detection"]  # COS queue drop policy. | Default: taildrop
    ecn: Literal["disable", "enable"]  # Enable/disable ECN packet marking to drop eligible | Default: disable
    weight: int  # Weight of weighted round robin scheduling. | Default: 1 | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class QueuePolicyCosqueueObject:
    """Typed object for cos-queue table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Cos queue ID. | MaxLen: 63
    name: str
    # Description of the COS queue. | MaxLen: 63
    description: str
    # Minimum rate (0 - 4294967295 kbps, 0 to disable). | Default: 0 | Min: 0 | Max: 4294967295
    min_rate: int
    # Maximum rate (0 - 4294967295 kbps, 0 to disable). | Default: 0 | Min: 0 | Max: 4294967295
    max_rate: int
    # Minimum rate (% of link speed). | Default: 0 | Min: 0 | Max: 4294967295
    min_rate_percent: int
    # Maximum rate (% of link speed). | Default: 0 | Min: 0 | Max: 4294967295
    max_rate_percent: int
    # COS queue drop policy. | Default: taildrop
    drop_policy: Literal["taildrop", "weighted-random-early-detection"]
    # Enable/disable ECN packet marking to drop eligible packets. | Default: disable
    ecn: Literal["disable", "enable"]
    # Weight of weighted round robin scheduling. | Default: 1 | Min: 0 | Max: 4294967295
    weight: int
    
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
class QueuePolicyResponse(TypedDict):
    """
    Type hints for switch_controller/qos/queue_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # QoS policy name. | MaxLen: 63
    schedule: Literal["strict", "round-robin", "weighted"]  # COS queue scheduling. | Default: round-robin
    rate_by: Literal["kbps", "percent"]  # COS queue rate by kbps or percent. | Default: kbps
    cos_queue: list[QueuePolicyCosqueueItem]  # COS queue configuration.


@final
class QueuePolicyObject:
    """Typed FortiObject for switch_controller/qos/queue_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # QoS policy name. | MaxLen: 63
    name: str
    # COS queue scheduling. | Default: round-robin
    schedule: Literal["strict", "round-robin", "weighted"]
    # COS queue rate by kbps or percent. | Default: kbps
    rate_by: Literal["kbps", "percent"]
    # COS queue configuration.
    cos_queue: list[QueuePolicyCosqueueObject]
    
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
    def to_dict(self) -> QueuePolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class QueuePolicy:
    """
    Configure FortiSwitch QoS egress queue policy.
    
    Path: switch_controller/qos/queue_policy
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
    ) -> QueuePolicyObject: ...
    
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
    ) -> QueuePolicyObject: ...
    
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
    ) -> FortiObjectList[QueuePolicyObject]: ...
    
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
    ) -> QueuePolicyObject: ...
    
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
    ) -> QueuePolicyObject: ...
    
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
    ) -> FortiObjectList[QueuePolicyObject]: ...
    
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
    ) -> QueuePolicyObject: ...
    
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
    ) -> QueuePolicyObject: ...
    
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
    ) -> FortiObjectList[QueuePolicyObject]: ...
    
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
    ) -> QueuePolicyObject | list[QueuePolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> QueuePolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> QueuePolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> QueuePolicyObject: ...
    
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
        payload_dict: QueuePolicyPayload | None = ...,
        name: str | None = ...,
        schedule: Literal["strict", "round-robin", "weighted"] | None = ...,
        rate_by: Literal["kbps", "percent"] | None = ...,
        cos_queue: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "QueuePolicy",
    "QueuePolicyPayload",
    "QueuePolicyResponse",
    "QueuePolicyObject",
]
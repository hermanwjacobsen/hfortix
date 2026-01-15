from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class TosBasedPriorityPayload(TypedDict, total=False):
    """
    Type hints for system/tos_based_priority payload fields.
    
    Configure Type of Service (ToS) based priority table to set network traffic priorities.
    
    **Usage:**
        payload: TosBasedPriorityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # Item ID. | Default: 0 | Min: 0 | Max: 4294967295
    tos: int  # Value of the ToS byte in the IP datagram header | Default: 0 | Min: 0 | Max: 15
    priority: Literal["low", "medium", "high"]  # ToS based priority level to low, medium or high | Default: high

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class TosBasedPriorityResponse(TypedDict):
    """
    Type hints for system/tos_based_priority API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # Item ID. | Default: 0 | Min: 0 | Max: 4294967295
    tos: int  # Value of the ToS byte in the IP datagram header | Default: 0 | Min: 0 | Max: 15
    priority: Literal["low", "medium", "high"]  # ToS based priority level to low, medium or high | Default: high


@final
class TosBasedPriorityObject:
    """Typed FortiObject for system/tos_based_priority with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Item ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Value of the ToS byte in the IP datagram header | Default: 0 | Min: 0 | Max: 15
    tos: int
    # ToS based priority level to low, medium or high | Default: high
    priority: Literal["low", "medium", "high"]
    
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
    def to_dict(self) -> TosBasedPriorityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TosBasedPriority:
    """
    Configure Type of Service (ToS) based priority table to set network traffic priorities.
    
    Path: system/tos_based_priority
    Category: cmdb
    Primary Key: id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[TosBasedPriorityObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
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
    ) -> FortiObjectList[TosBasedPriorityObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
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
    ) -> FortiObjectList[TosBasedPriorityObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject | list[TosBasedPriorityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> TosBasedPriorityObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: TosBasedPriorityPayload | None = ...,
        id: int | None = ...,
        tos: int | None = ...,
        priority: Literal["low", "medium", "high"] | None = ...,
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
    "TosBasedPriority",
    "TosBasedPriorityPayload",
    "TosBasedPriorityResponse",
    "TosBasedPriorityObject",
]
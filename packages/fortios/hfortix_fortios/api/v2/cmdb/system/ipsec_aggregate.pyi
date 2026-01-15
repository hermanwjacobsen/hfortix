from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class IpsecAggregatePayload(TypedDict, total=False):
    """
    Type hints for system/ipsec_aggregate payload fields.
    
    Configure an aggregate of IPsec tunnels.
    
    **Usage:**
        payload: IpsecAggregatePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPsec aggregate name. | MaxLen: 15
    member: list[dict[str, Any]]  # Member tunnels of the aggregate.
    algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"]  # Frame distribution algorithm. | Default: round-robin

# Nested TypedDicts for table field children (dict mode)

class IpsecAggregateMemberItem(TypedDict):
    """Type hints for member table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    tunnel_name: str  # Tunnel name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class IpsecAggregateMemberObject:
    """Typed object for member table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Tunnel name. | MaxLen: 79
    tunnel_name: str
    
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
class IpsecAggregateResponse(TypedDict):
    """
    Type hints for system/ipsec_aggregate API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPsec aggregate name. | MaxLen: 15
    member: list[IpsecAggregateMemberItem]  # Member tunnels of the aggregate.
    algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"]  # Frame distribution algorithm. | Default: round-robin


@final
class IpsecAggregateObject:
    """Typed FortiObject for system/ipsec_aggregate with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPsec aggregate name. | MaxLen: 15
    name: str
    # Member tunnels of the aggregate.
    member: list[IpsecAggregateMemberObject]
    # Frame distribution algorithm. | Default: round-robin
    algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"]
    
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
    def to_dict(self) -> IpsecAggregatePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class IpsecAggregate:
    """
    Configure an aggregate of IPsec tunnels.
    
    Path: system/ipsec_aggregate
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
    ) -> IpsecAggregateObject: ...
    
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
    ) -> IpsecAggregateObject: ...
    
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
    ) -> FortiObjectList[IpsecAggregateObject]: ...
    
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
    ) -> IpsecAggregateObject: ...
    
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
    ) -> IpsecAggregateObject: ...
    
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
    ) -> FortiObjectList[IpsecAggregateObject]: ...
    
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
    ) -> IpsecAggregateObject: ...
    
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
    ) -> IpsecAggregateObject: ...
    
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
    ) -> FortiObjectList[IpsecAggregateObject]: ...
    
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
    ) -> IpsecAggregateObject | list[IpsecAggregateObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> IpsecAggregateObject: ...
    
    @overload
    def post(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> IpsecAggregateObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> IpsecAggregateObject: ...
    
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
        payload_dict: IpsecAggregatePayload | None = ...,
        name: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        algorithm: Literal["L3", "L4", "round-robin", "redundant", "weighted-round-robin"] | None = ...,
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
    "IpsecAggregate",
    "IpsecAggregatePayload",
    "IpsecAggregateResponse",
    "IpsecAggregateObject",
]
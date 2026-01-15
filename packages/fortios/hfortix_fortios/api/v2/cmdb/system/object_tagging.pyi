from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ObjectTaggingPayload(TypedDict, total=False):
    """
    Type hints for system/object_tagging payload fields.
    
    Configure object tagging.
    
    **Usage:**
        payload: ObjectTaggingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    category: str  # Tag Category. | MaxLen: 63
    address: Literal["disable", "mandatory", "optional"]  # Address. | Default: optional
    device: Literal["disable", "mandatory", "optional"]  # Device. | Default: optional
    interface: Literal["disable", "mandatory", "optional"]  # Interface. | Default: optional
    multiple: Literal["enable", "disable"]  # Allow multiple tag selection. | Default: enable
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    tags: list[dict[str, Any]]  # Tags.

# Nested TypedDicts for table field children (dict mode)

class ObjectTaggingTagsItem(TypedDict):
    """Type hints for tags table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Tag name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class ObjectTaggingTagsObject:
    """Typed object for tags table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Tag name. | MaxLen: 79
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



# Response TypedDict for GET returns (all fields present in API response)
class ObjectTaggingResponse(TypedDict):
    """
    Type hints for system/object_tagging API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    category: str  # Tag Category. | MaxLen: 63
    address: Literal["disable", "mandatory", "optional"]  # Address. | Default: optional
    device: Literal["disable", "mandatory", "optional"]  # Device. | Default: optional
    interface: Literal["disable", "mandatory", "optional"]  # Interface. | Default: optional
    multiple: Literal["enable", "disable"]  # Allow multiple tag selection. | Default: enable
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    tags: list[ObjectTaggingTagsItem]  # Tags.


@final
class ObjectTaggingObject:
    """Typed FortiObject for system/object_tagging with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Tag Category. | MaxLen: 63
    category: str
    # Address. | Default: optional
    address: Literal["disable", "mandatory", "optional"]
    # Device. | Default: optional
    device: Literal["disable", "mandatory", "optional"]
    # Interface. | Default: optional
    interface: Literal["disable", "mandatory", "optional"]
    # Allow multiple tag selection. | Default: enable
    multiple: Literal["enable", "disable"]
    # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    color: int
    # Tags.
    tags: list[ObjectTaggingTagsObject]
    
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
    def to_dict(self) -> ObjectTaggingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ObjectTagging:
    """
    Configure object tagging.
    
    Path: system/object_tagging
    Category: cmdb
    Primary Key: category
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        category: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        category: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        category: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[ObjectTaggingObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        category: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        category: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
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
    ) -> FortiObjectList[ObjectTaggingObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        category: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        category: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
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
    ) -> FortiObjectList[ObjectTaggingObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        category: str | None = ...,
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
        category: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject | list[ObjectTaggingObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ObjectTaggingObject: ...
    
    @overload
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        category: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        category: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ObjectTaggingPayload | None = ...,
        category: str | None = ...,
        address: Literal["disable", "mandatory", "optional"] | None = ...,
        device: Literal["disable", "mandatory", "optional"] | None = ...,
        interface: Literal["disable", "mandatory", "optional"] | None = ...,
        multiple: Literal["enable", "disable"] | None = ...,
        color: int | None = ...,
        tags: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ObjectTagging",
    "ObjectTaggingPayload",
    "ObjectTaggingResponse",
    "ObjectTaggingObject",
]
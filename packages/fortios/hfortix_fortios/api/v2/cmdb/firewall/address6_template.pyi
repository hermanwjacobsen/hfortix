from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Address6TemplatePayload(TypedDict, total=False):
    """
    Type hints for firewall/address6_template payload fields.
    
    Configure IPv6 address templates.
    
    **Usage:**
        payload: Address6TemplatePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPv6 address template name. | MaxLen: 63
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    ip6: str  # IPv6 address prefix. | Default: ::/0
    subnet_segment_count: int  # Number of IPv6 subnet segments. | Default: 0 | Min: 1 | Max: 6
    subnet_segment: list[dict[str, Any]]  # IPv6 subnet segments.
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class Address6TemplateSubnetsegmentItem(TypedDict):
    """Type hints for subnet-segment table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Subnet segment ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Subnet segment name. | MaxLen: 63
    bits: int  # Number of bits. | Default: 0 | Min: 1 | Max: 16
    exclusive: Literal["enable", "disable"]  # Enable/disable exclusive value. | Default: disable
    values: str  # Subnet segment values.


# Nested classes for table field children (object mode)

@final
class Address6TemplateSubnetsegmentObject:
    """Typed object for subnet-segment table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Subnet segment ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Subnet segment name. | MaxLen: 63
    name: str
    # Number of bits. | Default: 0 | Min: 1 | Max: 16
    bits: int
    # Enable/disable exclusive value. | Default: disable
    exclusive: Literal["enable", "disable"]
    # Subnet segment values.
    values: str
    
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
class Address6TemplateResponse(TypedDict):
    """
    Type hints for firewall/address6_template API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPv6 address template name. | MaxLen: 63
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    ip6: str  # IPv6 address prefix. | Default: ::/0
    subnet_segment_count: int  # Number of IPv6 subnet segments. | Default: 0 | Min: 1 | Max: 6
    subnet_segment: list[Address6TemplateSubnetsegmentItem]  # IPv6 subnet segments.
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable


@final
class Address6TemplateObject:
    """Typed FortiObject for firewall/address6_template with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPv6 address template name. | MaxLen: 63
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # IPv6 address prefix. | Default: ::/0
    ip6: str
    # Number of IPv6 subnet segments. | Default: 0 | Min: 1 | Max: 6
    subnet_segment_count: int
    # IPv6 subnet segments.
    subnet_segment: list[Address6TemplateSubnetsegmentObject]
    # Security Fabric global object setting. | Default: disable
    fabric_object: Literal["enable", "disable"]
    
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
    def to_dict(self) -> Address6TemplatePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Address6Template:
    """
    Configure IPv6 address templates.
    
    Path: firewall/address6_template
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
    ) -> Address6TemplateObject: ...
    
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
    ) -> Address6TemplateObject: ...
    
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
    ) -> FortiObjectList[Address6TemplateObject]: ...
    
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
    ) -> Address6TemplateObject: ...
    
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
    ) -> Address6TemplateObject: ...
    
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
    ) -> FortiObjectList[Address6TemplateObject]: ...
    
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
    ) -> Address6TemplateObject: ...
    
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
    ) -> Address6TemplateObject: ...
    
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
    ) -> FortiObjectList[Address6TemplateObject]: ...
    
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
    ) -> Address6TemplateObject | list[Address6TemplateObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Address6TemplateObject: ...
    
    @overload
    def post(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Address6TemplateObject: ...
    
    @overload
    def put(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Address6TemplateObject: ...
    
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
        payload_dict: Address6TemplatePayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        ip6: str | None = ...,
        subnet_segment_count: int | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Address6Template",
    "Address6TemplatePayload",
    "Address6TemplateResponse",
    "Address6TemplateObject",
]
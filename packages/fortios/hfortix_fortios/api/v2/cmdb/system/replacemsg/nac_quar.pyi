from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class NacQuarPayload(TypedDict, total=False):
    """
    Type hints for system/replacemsg/nac_quar payload fields.
    
    Replacement messages.
    
    **Usage:**
        payload: NacQuarPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class NacQuarResponse(TypedDict):
    """
    Type hints for system/replacemsg/nac_quar API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


@final
class NacQuarObject:
    """Typed FortiObject for system/replacemsg/nac_quar with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
    def to_dict(self) -> NacQuarPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class NacQuar:
    """
    Replacement messages.
    
    Path: system/replacemsg/nac_quar
    Category: cmdb
    Primary Key: msg-type
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        msg_type: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        msg_type: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        msg_type: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[NacQuarObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        msg_type: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        msg_type: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
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
    ) -> FortiObjectList[NacQuarObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        msg_type: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        msg_type: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
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
    ) -> FortiObjectList[NacQuarObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        msg_type: str | None = ...,
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
        msg_type: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject | list[NacQuarObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
    @overload
    def post(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        msg_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> NacQuarObject: ...
    
    @overload
    def delete(
        self,
        msg_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        msg_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        msg_type: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        msg_type: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: NacQuarPayload | None = ...,
        msg_type: str | None = ...,
        buffer: str | None = ...,
        header: Literal["none", "http", "8bit"] | None = ...,
        format: Literal["none", "text", "html"] | None = ...,
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
    "NacQuar",
    "NacQuarPayload",
    "NacQuarResponse",
    "NacQuarObject",
]
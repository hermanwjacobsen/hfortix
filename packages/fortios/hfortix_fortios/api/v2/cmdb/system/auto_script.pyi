from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AutoScriptPayload(TypedDict, total=False):
    """
    Type hints for system/auto_script payload fields.
    
    Configure auto script.
    
    **Usage:**
        payload: AutoScriptPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Auto script name. | MaxLen: 35
    interval: int  # Repeat interval in seconds. | Default: 0 | Min: 0 | Max: 31557600
    repeat: int  # Number of times to repeat this script | Default: 1 | Min: 0 | Max: 65535
    start: Literal["manual", "auto"]  # Script starting mode. | Default: manual
    script: str  # List of FortiOS CLI commands to repeat. | MaxLen: 1023
    output_size: int  # Number of megabytes to limit script output to | Default: 10 | Min: 10 | Max: 1024
    timeout: int  # Maximum running time for this script in seconds | Default: 0 | Min: 0 | Max: 300

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class AutoScriptResponse(TypedDict):
    """
    Type hints for system/auto_script API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Auto script name. | MaxLen: 35
    interval: int  # Repeat interval in seconds. | Default: 0 | Min: 0 | Max: 31557600
    repeat: int  # Number of times to repeat this script | Default: 1 | Min: 0 | Max: 65535
    start: Literal["manual", "auto"]  # Script starting mode. | Default: manual
    script: str  # List of FortiOS CLI commands to repeat. | MaxLen: 1023
    output_size: int  # Number of megabytes to limit script output to | Default: 10 | Min: 10 | Max: 1024
    timeout: int  # Maximum running time for this script in seconds | Default: 0 | Min: 0 | Max: 300


@final
class AutoScriptObject:
    """Typed FortiObject for system/auto_script with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Auto script name. | MaxLen: 35
    name: str
    # Repeat interval in seconds. | Default: 0 | Min: 0 | Max: 31557600
    interval: int
    # Number of times to repeat this script (0 = infinite). | Default: 1 | Min: 0 | Max: 65535
    repeat: int
    # Script starting mode. | Default: manual
    start: Literal["manual", "auto"]
    # List of FortiOS CLI commands to repeat. | MaxLen: 1023
    script: str
    # Number of megabytes to limit script output to | Default: 10 | Min: 10 | Max: 1024
    output_size: int
    # Maximum running time for this script in seconds | Default: 0 | Min: 0 | Max: 300
    timeout: int
    
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
    def to_dict(self) -> AutoScriptPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AutoScript:
    """
    Configure auto script.
    
    Path: system/auto_script
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
    ) -> AutoScriptObject: ...
    
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
    ) -> AutoScriptObject: ...
    
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
    ) -> FortiObjectList[AutoScriptObject]: ...
    
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
    ) -> AutoScriptObject: ...
    
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
    ) -> AutoScriptObject: ...
    
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
    ) -> FortiObjectList[AutoScriptObject]: ...
    
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
    ) -> AutoScriptObject: ...
    
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
    ) -> AutoScriptObject: ...
    
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
    ) -> FortiObjectList[AutoScriptObject]: ...
    
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
    ) -> AutoScriptObject | list[AutoScriptObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutoScriptObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutoScriptObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutoScriptObject: ...
    
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
        payload_dict: AutoScriptPayload | None = ...,
        name: str | None = ...,
        interval: int | None = ...,
        repeat: int | None = ...,
        start: Literal["manual", "auto"] | None = ...,
        script: str | None = ...,
        output_size: int | None = ...,
        timeout: int | None = ...,
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
    "AutoScript",
    "AutoScriptPayload",
    "AutoScriptResponse",
    "AutoScriptObject",
]
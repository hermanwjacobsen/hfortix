from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FortigatePayload(TypedDict, total=False):
    """
    Type hints for extension_controller/fortigate payload fields.
    
    FortiGate controller configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.extension-controller.fortigate-profile.FortigateProfileEndpoint` (via: profile)

    **Usage:**
        payload: FortigatePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # FortiGate entry name. | MaxLen: 19
    id: str  # FortiGate serial number. | MaxLen: 19
    authorized: Literal["discovered", "disable", "enable"]  # Enable/disable FortiGate administration. | Default: discovered
    hostname: str  # FortiGate hostname. | MaxLen: 31
    description: str  # Description. | MaxLen: 255
    vdom: int  # VDOM. | Default: 0 | Min: 0 | Max: 4294967295
    device_id: int  # Device ID. | Default: 1026 | Min: 0 | Max: 4294967295
    profile: str  # FortiGate profile configuration. | MaxLen: 31

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class FortigateResponse(TypedDict):
    """
    Type hints for extension_controller/fortigate API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # FortiGate entry name. | MaxLen: 19
    id: str  # FortiGate serial number. | MaxLen: 19
    authorized: Literal["discovered", "disable", "enable"]  # Enable/disable FortiGate administration. | Default: discovered
    hostname: str  # FortiGate hostname. | MaxLen: 31
    description: str  # Description. | MaxLen: 255
    vdom: int  # VDOM. | Default: 0 | Min: 0 | Max: 4294967295
    device_id: int  # Device ID. | Default: 1026 | Min: 0 | Max: 4294967295
    profile: str  # FortiGate profile configuration. | MaxLen: 31


@final
class FortigateObject:
    """Typed FortiObject for extension_controller/fortigate with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # FortiGate entry name. | MaxLen: 19
    name: str
    # FortiGate serial number. | MaxLen: 19
    id: str
    # Enable/disable FortiGate administration. | Default: discovered
    authorized: Literal["discovered", "disable", "enable"]
    # FortiGate hostname. | MaxLen: 31
    hostname: str
    # Description. | MaxLen: 255
    description: str
    # VDOM. | Default: 0 | Min: 0 | Max: 4294967295
    vdom: int
    # Device ID. | Default: 1026 | Min: 0 | Max: 4294967295
    device_id: int
    # FortiGate profile configuration. | MaxLen: 31
    profile: str
    
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
    def to_dict(self) -> FortigatePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Fortigate:
    """
    FortiGate controller configuration.
    
    Path: extension_controller/fortigate
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
    ) -> FortigateObject: ...
    
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
    ) -> FortigateObject: ...
    
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
    ) -> FortiObjectList[FortigateObject]: ...
    
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
    ) -> FortigateObject: ...
    
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
    ) -> FortigateObject: ...
    
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
    ) -> FortiObjectList[FortigateObject]: ...
    
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
    ) -> FortigateObject: ...
    
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
    ) -> FortigateObject: ...
    
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
    ) -> FortiObjectList[FortigateObject]: ...
    
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
    ) -> FortigateObject | list[FortigateObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortigateObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortigateObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortigateObject: ...
    
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
        payload_dict: FortigatePayload | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        authorized: Literal["discovered", "disable", "enable"] | None = ...,
        hostname: str | None = ...,
        description: str | None = ...,
        device_id: int | None = ...,
        profile: str | None = ...,
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
    "Fortigate",
    "FortigatePayload",
    "FortigateResponse",
    "FortigateObject",
]
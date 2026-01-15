from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ApStatusPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/ap_status payload fields.
    
    Configure access point status (rogue | accepted | suppressed).
    
    **Usage:**
        payload: ApStatusPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # AP ID. | Default: 0 | Min: 0 | Max: 4294967295
    bssid: str  # Access Point's (AP's) BSSID. | Default: 00:00:00:00:00:00
    ssid: str  # Access Point's (AP's) SSID. | MaxLen: 32
    status: Literal["rogue", "accepted", "suppressed"]  # Access Point's (AP's) status: rogue, accepted, or | Default: rogue

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ApStatusResponse(TypedDict):
    """
    Type hints for wireless_controller/ap_status API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # AP ID. | Default: 0 | Min: 0 | Max: 4294967295
    bssid: str  # Access Point's (AP's) BSSID. | Default: 00:00:00:00:00:00
    ssid: str  # Access Point's (AP's) SSID. | MaxLen: 32
    status: Literal["rogue", "accepted", "suppressed"]  # Access Point's (AP's) status: rogue, accepted, or | Default: rogue


@final
class ApStatusObject:
    """Typed FortiObject for wireless_controller/ap_status with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # AP ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Access Point's (AP's) BSSID. | Default: 00:00:00:00:00:00
    bssid: str
    # Access Point's (AP's) SSID. | MaxLen: 32
    ssid: str
    # Access Point's (AP's) status: rogue, accepted, or suppressed | Default: rogue
    status: Literal["rogue", "accepted", "suppressed"]
    
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
    def to_dict(self) -> ApStatusPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ApStatus:
    """
    Configure access point status (rogue | accepted | suppressed).
    
    Path: wireless_controller/ap_status
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
    ) -> ApStatusObject: ...
    
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
    ) -> ApStatusObject: ...
    
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
    ) -> FortiObjectList[ApStatusObject]: ...
    
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
    ) -> ApStatusObject: ...
    
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
    ) -> ApStatusObject: ...
    
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
    ) -> FortiObjectList[ApStatusObject]: ...
    
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
    ) -> ApStatusObject: ...
    
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
    ) -> ApStatusObject: ...
    
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
    ) -> FortiObjectList[ApStatusObject]: ...
    
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
    ) -> ApStatusObject | list[ApStatusObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ApStatusObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ApStatusObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ApStatusObject: ...
    
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
        payload_dict: ApStatusPayload | None = ...,
        id: int | None = ...,
        bssid: str | None = ...,
        ssid: str | None = ...,
        status: Literal["rogue", "accepted", "suppressed"] | None = ...,
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
    "ApStatus",
    "ApStatusPayload",
    "ApStatusResponse",
    "ApStatusObject",
]
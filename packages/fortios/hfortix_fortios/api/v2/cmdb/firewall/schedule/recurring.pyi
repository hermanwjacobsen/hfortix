from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RecurringPayload(TypedDict, total=False):
    """
    Type hints for firewall/schedule/recurring payload fields.
    
    Recurring schedule configuration.
    
    **Usage:**
        payload: RecurringPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Recurring schedule name. | MaxLen: 31
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    start: str  # Time of day to start the schedule, format hh:mm.
    end: str  # Time of day to end the schedule, format hh:mm.
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"]  # One or more days of the week on which the schedule | Default: none
    label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"]  # Configure a window during the time of day in which | Default: none
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class RecurringResponse(TypedDict):
    """
    Type hints for firewall/schedule/recurring API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Recurring schedule name. | MaxLen: 31
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    start: str  # Time of day to start the schedule, format hh:mm.
    end: str  # Time of day to end the schedule, format hh:mm.
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"]  # One or more days of the week on which the schedule | Default: none
    label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"]  # Configure a window during the time of day in which | Default: none
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable


@final
class RecurringObject:
    """Typed FortiObject for firewall/schedule/recurring with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Recurring schedule name. | MaxLen: 31
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Time of day to start the schedule, format hh:mm.
    start: str
    # Time of day to end the schedule, format hh:mm.
    end: str
    # One or more days of the week on which the schedule is valid. | Default: none
    day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"]
    # Configure a window during the time of day in which the sched | Default: none
    label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"]
    # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    color: int
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
    def to_dict(self) -> RecurringPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Recurring:
    """
    Recurring schedule configuration.
    
    Path: firewall/schedule/recurring
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
    ) -> RecurringObject: ...
    
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
    ) -> RecurringObject: ...
    
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
    ) -> FortiObjectList[RecurringObject]: ...
    
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
    ) -> RecurringObject: ...
    
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
    ) -> RecurringObject: ...
    
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
    ) -> FortiObjectList[RecurringObject]: ...
    
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
    ) -> RecurringObject: ...
    
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
    ) -> RecurringObject: ...
    
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
    ) -> FortiObjectList[RecurringObject]: ...
    
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
    ) -> RecurringObject | list[RecurringObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RecurringObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RecurringObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> RecurringObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: RecurringPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        start: str | None = ...,
        end: str | None = ...,
        day: Literal["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "none"] | list[str] | None = ...,
        label_day: Literal["none", "over-night", "early-morning", "morning", "midday", "afternoon", "evening", "night", "late-night"] | None = ...,
        color: int | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Recurring",
    "RecurringPayload",
    "RecurringResponse",
    "RecurringObject",
]
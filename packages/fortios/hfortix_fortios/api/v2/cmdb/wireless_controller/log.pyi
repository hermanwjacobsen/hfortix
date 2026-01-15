from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LogPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/log payload fields.
    
    Configure wireless controller event log filters.
    
    **Usage:**
        payload: LogPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable wireless event logging. | Default: enable
    addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log address group message | Default: notification
    ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log BLE detection message | Default: notification
    clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log client load balancing | Default: notification
    dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log DHCP starvation event | Default: notification
    led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log LED schedule event me | Default: notification
    radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log radio event message. | Default: notification
    rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log rogue AP event messag | Default: notification
    sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log station event message | Default: notification
    sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log station locate messag | Default: notification
    wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log WIDS message. | Default: notification
    wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log WTP event message. | Default: notification
    wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log FAP fips event messag | Default: notification

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class LogResponse(TypedDict):
    """
    Type hints for wireless_controller/log API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable wireless event logging. | Default: enable
    addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log address group message | Default: notification
    ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log BLE detection message | Default: notification
    clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log client load balancing | Default: notification
    dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log DHCP starvation event | Default: notification
    led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log LED schedule event me | Default: notification
    radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log radio event message. | Default: notification
    rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log rogue AP event messag | Default: notification
    sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log station event message | Default: notification
    sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log station locate messag | Default: notification
    wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log WIDS message. | Default: notification
    wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log WTP event message. | Default: notification
    wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Lowest severity level to log FAP fips event messag | Default: notification


@final
class LogObject:
    """Typed FortiObject for wireless_controller/log with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable wireless event logging. | Default: enable
    status: Literal["enable", "disable"]
    # Lowest severity level to log address group message. | Default: notification
    addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log BLE detection message. | Default: notification
    ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log client load balancing message. | Default: notification
    clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log DHCP starvation event message. | Default: notification
    dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log LED schedule event message. | Default: notification
    led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log radio event message. | Default: notification
    radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log rogue AP event message. | Default: notification
    rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log station event message. | Default: notification
    sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log station locate message. | Default: notification
    sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log WIDS message. | Default: notification
    wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log WTP event message. | Default: notification
    wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Lowest severity level to log FAP fips event message. | Default: notification
    wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    
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
    def to_dict(self) -> LogPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Log:
    """
    Configure wireless controller event log filters.
    
    Path: wireless_controller/log
    Category: cmdb
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> LogObject: ...
    
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
    ) -> dict[str, Any] | FortiObject: ...
    
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
    ) -> LogObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> LogObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: LogPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        addrgrp_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        ble_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        clb_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        dhcp_starv_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        led_sched_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        radio_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        rogue_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        sta_locate_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wids_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
        wtp_fips_event_log: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = ...,
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
    "Log",
    "LogPayload",
    "LogResponse",
    "LogObject",
]
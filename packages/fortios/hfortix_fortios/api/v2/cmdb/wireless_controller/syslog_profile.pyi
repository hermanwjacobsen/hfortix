from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SyslogProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/syslog_profile payload fields.
    
    Configure Wireless Termination Points (WTP) system log server profile.
    
    **Usage:**
        payload: SyslogProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # WTP system log server profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    server_status: Literal["enable", "disable"]  # Enable/disable FortiAP units to send log messages | Default: enable
    server: str  # Syslog server CN domain name or IP address. | MaxLen: 63
    server_port: int  # Port number of syslog server that FortiAP units se | Default: 514 | Min: 0 | Max: 65535
    server_type: Literal["standard", "fortianalyzer"]  # Configure syslog server type (default = standard). | Default: standard
    log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"]  # Lowest level of log messages that FortiAP units se | Default: information

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SyslogProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/syslog_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # WTP system log server profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    server_status: Literal["enable", "disable"]  # Enable/disable FortiAP units to send log messages | Default: enable
    server: str  # Syslog server CN domain name or IP address. | MaxLen: 63
    server_port: int  # Port number of syslog server that FortiAP units se | Default: 514 | Min: 0 | Max: 65535
    server_type: Literal["standard", "fortianalyzer"]  # Configure syslog server type (default = standard). | Default: standard
    log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"]  # Lowest level of log messages that FortiAP units se | Default: information


@final
class SyslogProfileObject:
    """Typed FortiObject for wireless_controller/syslog_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # WTP system log server profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Enable/disable FortiAP units to send log messages to a syslo | Default: enable
    server_status: Literal["enable", "disable"]
    # Syslog server CN domain name or IP address. | MaxLen: 63
    server: str
    # Port number of syslog server that FortiAP units send log mes | Default: 514 | Min: 0 | Max: 65535
    server_port: int
    # Configure syslog server type (default = standard). | Default: standard
    server_type: Literal["standard", "fortianalyzer"]
    # Lowest level of log messages that FortiAP units send to this | Default: information
    log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"]
    
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
    def to_dict(self) -> SyslogProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SyslogProfile:
    """
    Configure Wireless Termination Points (WTP) system log server profile.
    
    Path: wireless_controller/syslog_profile
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
    ) -> SyslogProfileObject: ...
    
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
    ) -> SyslogProfileObject: ...
    
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
    ) -> FortiObjectList[SyslogProfileObject]: ...
    
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
    ) -> SyslogProfileObject: ...
    
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
    ) -> SyslogProfileObject: ...
    
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
    ) -> FortiObjectList[SyslogProfileObject]: ...
    
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
    ) -> SyslogProfileObject: ...
    
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
    ) -> SyslogProfileObject: ...
    
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
    ) -> FortiObjectList[SyslogProfileObject]: ...
    
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
    ) -> SyslogProfileObject | list[SyslogProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SyslogProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SyslogProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SyslogProfileObject: ...
    
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
        payload_dict: SyslogProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        server_status: Literal["enable", "disable"] | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_type: Literal["standard", "fortianalyzer"] | None = ...,
        log_level: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debugging"] | None = ...,
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
    "SyslogProfile",
    "SyslogProfilePayload",
    "SyslogProfileResponse",
    "SyslogProfileObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SysinfoPayload(TypedDict, total=False):
    """
    Type hints for system/snmp/sysinfo payload fields.
    
    SNMP system info configuration.
    
    **Usage:**
        payload: SysinfoPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable SNMP. | Default: disable
    engine_id_type: Literal["text", "hex", "mac"]  # Local SNMP engineID type (text/hex/mac). | Default: text
    engine_id: str  # Local SNMP engineID string (maximum 27 characters) | MaxLen: 54
    description: str  # System description. | MaxLen: 255
    contact_info: str  # Contact information. | MaxLen: 255
    location: str  # System location. | MaxLen: 255
    trap_high_cpu_threshold: int  # CPU usage when trap is sent. | Default: 80 | Min: 1 | Max: 100
    trap_low_memory_threshold: int  # Memory usage when trap is sent. | Default: 80 | Min: 1 | Max: 100
    trap_log_full_threshold: int  # Log disk usage when trap is sent. | Default: 90 | Min: 1 | Max: 100
    trap_free_memory_threshold: int  # Free memory usage when trap is sent. | Default: 5 | Min: 1 | Max: 100
    trap_freeable_memory_threshold: int  # Freeable memory usage when trap is sent. | Default: 60 | Min: 1 | Max: 100
    append_index: Literal["enable", "disable"]  # Enable/disable allowance of appending vdom or inte | Default: disable
    non_mgmt_vdom_query: Literal["enable", "disable"]  # Enable/disable allowance of SNMPv3 query from non- | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SysinfoResponse(TypedDict):
    """
    Type hints for system/snmp/sysinfo API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable SNMP. | Default: disable
    engine_id_type: Literal["text", "hex", "mac"]  # Local SNMP engineID type (text/hex/mac). | Default: text
    engine_id: str  # Local SNMP engineID string (maximum 27 characters) | MaxLen: 54
    description: str  # System description. | MaxLen: 255
    contact_info: str  # Contact information. | MaxLen: 255
    location: str  # System location. | MaxLen: 255
    trap_high_cpu_threshold: int  # CPU usage when trap is sent. | Default: 80 | Min: 1 | Max: 100
    trap_low_memory_threshold: int  # Memory usage when trap is sent. | Default: 80 | Min: 1 | Max: 100
    trap_log_full_threshold: int  # Log disk usage when trap is sent. | Default: 90 | Min: 1 | Max: 100
    trap_free_memory_threshold: int  # Free memory usage when trap is sent. | Default: 5 | Min: 1 | Max: 100
    trap_freeable_memory_threshold: int  # Freeable memory usage when trap is sent. | Default: 60 | Min: 1 | Max: 100
    append_index: Literal["enable", "disable"]  # Enable/disable allowance of appending vdom or inte | Default: disable
    non_mgmt_vdom_query: Literal["enable", "disable"]  # Enable/disable allowance of SNMPv3 query from non- | Default: disable


@final
class SysinfoObject:
    """Typed FortiObject for system/snmp/sysinfo with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable SNMP. | Default: disable
    status: Literal["enable", "disable"]
    # Local SNMP engineID type (text/hex/mac). | Default: text
    engine_id_type: Literal["text", "hex", "mac"]
    # Local SNMP engineID string (maximum 27 characters). | MaxLen: 54
    engine_id: str
    # System description. | MaxLen: 255
    description: str
    # Contact information. | MaxLen: 255
    contact_info: str
    # System location. | MaxLen: 255
    location: str
    # CPU usage when trap is sent. | Default: 80 | Min: 1 | Max: 100
    trap_high_cpu_threshold: int
    # Memory usage when trap is sent. | Default: 80 | Min: 1 | Max: 100
    trap_low_memory_threshold: int
    # Log disk usage when trap is sent. | Default: 90 | Min: 1 | Max: 100
    trap_log_full_threshold: int
    # Free memory usage when trap is sent. | Default: 5 | Min: 1 | Max: 100
    trap_free_memory_threshold: int
    # Freeable memory usage when trap is sent. | Default: 60 | Min: 1 | Max: 100
    trap_freeable_memory_threshold: int
    # Enable/disable allowance of appending vdom or interface inde | Default: disable
    append_index: Literal["enable", "disable"]
    # Enable/disable allowance of SNMPv3 query from non-management | Default: disable
    non_mgmt_vdom_query: Literal["enable", "disable"]
    
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
    def to_dict(self) -> SysinfoPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Sysinfo:
    """
    SNMP system info configuration.
    
    Path: system/snmp/sysinfo
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject: ...
    
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
    ) -> SysinfoObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SysinfoObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SysinfoPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        engine_id_type: Literal["text", "hex", "mac"] | None = ...,
        engine_id: str | None = ...,
        description: str | None = ...,
        contact_info: str | None = ...,
        location: str | None = ...,
        trap_high_cpu_threshold: int | None = ...,
        trap_low_memory_threshold: int | None = ...,
        trap_log_full_threshold: int | None = ...,
        trap_free_memory_threshold: int | None = ...,
        trap_freeable_memory_threshold: int | None = ...,
        append_index: Literal["enable", "disable"] | None = ...,
        non_mgmt_vdom_query: Literal["enable", "disable"] | None = ...,
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
    "Sysinfo",
    "SysinfoPayload",
    "SysinfoResponse",
    "SysinfoObject",
]
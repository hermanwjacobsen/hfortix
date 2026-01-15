from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SystemPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/system payload fields.
    
    Configure system-wide switch controller settings.
    
    **Usage:**
        payload: SystemPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    parallel_process_override: Literal["disable", "enable"]  # Enable/disable parallel process override. | Default: disable
    parallel_process: int  # Maximum number of parallel processes. | Default: 1 | Min: 1 | Max: 24
    data_sync_interval: int  # Time interval between collection of switch data | Default: 60 | Min: 30 | Max: 1800
    iot_weight_threshold: int  # MAC entry's confidence value. Value is re-queried | Default: 1 | Min: 0 | Max: 255
    iot_scan_interval: int  # IoT scan interval | Default: 60 | Min: 2 | Max: 10080
    iot_holdoff: int  # MAC entry's creation time. Time must be greater th | Default: 5 | Min: 0 | Max: 10080
    iot_mac_idle: int  # MAC entry's idle time. MAC entry is removed after | Default: 1440 | Min: 0 | Max: 10080
    nac_periodic_interval: int  # Periodic time interval to run NAC engine | Default: 60 | Min: 5 | Max: 180
    dynamic_periodic_interval: int  # Periodic time interval to run Dynamic port policy | Default: 60 | Min: 5 | Max: 180
    tunnel_mode: Literal["compatible", "moderate", "strict"]  # Compatible/strict tunnel mode. | Default: compatible
    caputp_echo_interval: int  # Echo interval for the caputp echo requests from sw | Default: 30 | Min: 8 | Max: 600
    caputp_max_retransmit: int  # Maximum retransmission count for the caputp tunnel | Default: 5 | Min: 0 | Max: 64

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SystemResponse(TypedDict):
    """
    Type hints for switch_controller/system API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    parallel_process_override: Literal["disable", "enable"]  # Enable/disable parallel process override. | Default: disable
    parallel_process: int  # Maximum number of parallel processes. | Default: 1 | Min: 1 | Max: 24
    data_sync_interval: int  # Time interval between collection of switch data | Default: 60 | Min: 30 | Max: 1800
    iot_weight_threshold: int  # MAC entry's confidence value. Value is re-queried | Default: 1 | Min: 0 | Max: 255
    iot_scan_interval: int  # IoT scan interval | Default: 60 | Min: 2 | Max: 10080
    iot_holdoff: int  # MAC entry's creation time. Time must be greater th | Default: 5 | Min: 0 | Max: 10080
    iot_mac_idle: int  # MAC entry's idle time. MAC entry is removed after | Default: 1440 | Min: 0 | Max: 10080
    nac_periodic_interval: int  # Periodic time interval to run NAC engine | Default: 60 | Min: 5 | Max: 180
    dynamic_periodic_interval: int  # Periodic time interval to run Dynamic port policy | Default: 60 | Min: 5 | Max: 180
    tunnel_mode: Literal["compatible", "moderate", "strict"]  # Compatible/strict tunnel mode. | Default: compatible
    caputp_echo_interval: int  # Echo interval for the caputp echo requests from sw | Default: 30 | Min: 8 | Max: 600
    caputp_max_retransmit: int  # Maximum retransmission count for the caputp tunnel | Default: 5 | Min: 0 | Max: 64


@final
class SystemObject:
    """Typed FortiObject for switch_controller/system with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable parallel process override. | Default: disable
    parallel_process_override: Literal["disable", "enable"]
    # Maximum number of parallel processes. | Default: 1 | Min: 1 | Max: 24
    parallel_process: int
    # Time interval between collection of switch data | Default: 60 | Min: 30 | Max: 1800
    data_sync_interval: int
    # MAC entry's confidence value. Value is re-queried when below | Default: 1 | Min: 0 | Max: 255
    iot_weight_threshold: int
    # IoT scan interval | Default: 60 | Min: 2 | Max: 10080
    iot_scan_interval: int
    # MAC entry's creation time. Time must be greater than this va | Default: 5 | Min: 0 | Max: 10080
    iot_holdoff: int
    # MAC entry's idle time. MAC entry is removed after this value | Default: 1440 | Min: 0 | Max: 10080
    iot_mac_idle: int
    # Periodic time interval to run NAC engine | Default: 60 | Min: 5 | Max: 180
    nac_periodic_interval: int
    # Periodic time interval to run Dynamic port policy engine | Default: 60 | Min: 5 | Max: 180
    dynamic_periodic_interval: int
    # Compatible/strict tunnel mode. | Default: compatible
    tunnel_mode: Literal["compatible", "moderate", "strict"]
    # Echo interval for the caputp echo requests from swtp. | Default: 30 | Min: 8 | Max: 600
    caputp_echo_interval: int
    # Maximum retransmission count for the caputp tunnel packets. | Default: 5 | Min: 0 | Max: 64
    caputp_max_retransmit: int
    
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
    def to_dict(self) -> SystemPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class System:
    """
    Configure system-wide switch controller settings.
    
    Path: switch_controller/system
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject: ...
    
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
    ) -> SystemObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> SystemObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SystemPayload | None = ...,
        parallel_process_override: Literal["disable", "enable"] | None = ...,
        parallel_process: int | None = ...,
        data_sync_interval: int | None = ...,
        iot_weight_threshold: int | None = ...,
        iot_scan_interval: int | None = ...,
        iot_holdoff: int | None = ...,
        iot_mac_idle: int | None = ...,
        nac_periodic_interval: int | None = ...,
        dynamic_periodic_interval: int | None = ...,
        tunnel_mode: Literal["compatible", "moderate", "strict"] | None = ...,
        caputp_echo_interval: int | None = ...,
        caputp_max_retransmit: int | None = ...,
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
    "System",
    "SystemPayload",
    "SystemResponse",
    "SystemObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class InterControllerPayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/inter_controller payload fields.
    
    Configure inter wireless controller operation.
    
    **Usage:**
        payload: InterControllerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    inter_controller_mode: Literal["disable", "l2-roaming", "1+1"]  # Configure inter-controller mode | Default: disable
    l3_roaming: Literal["enable", "disable"]  # Enable/disable layer 3 roaming (default = disable) | Default: disable
    inter_controller_key: str  # Secret key for inter-controller communications. | MaxLen: 127
    inter_controller_pri: Literal["primary", "secondary"]  # Configure inter-controller's priority | Default: primary
    fast_failover_max: int  # Maximum number of retransmissions for fast failove | Default: 10 | Min: 3 | Max: 64
    fast_failover_wait: int  # Minimum wait time before an AP transitions from se | Default: 10 | Min: 10 | Max: 86400
    inter_controller_peer: list[dict[str, Any]]  # Fast failover peer wireless controller list.

# Nested TypedDicts for table field children (dict mode)

class InterControllerIntercontrollerpeerItem(TypedDict):
    """Type hints for inter-controller-peer table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    peer_ip: str  # Peer wireless controller's IP address. | Default: 0.0.0.0
    peer_port: int  # Port used by the wireless controller's for inter-c | Default: 5246 | Min: 1024 | Max: 49150
    peer_priority: Literal["primary", "secondary"]  # Peer wireless controller's priority | Default: primary


# Nested classes for table field children (object mode)

@final
class InterControllerIntercontrollerpeerObject:
    """Typed object for inter-controller-peer table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Peer wireless controller's IP address. | Default: 0.0.0.0
    peer_ip: str
    # Port used by the wireless controller's for inter-controller | Default: 5246 | Min: 1024 | Max: 49150
    peer_port: int
    # Peer wireless controller's priority | Default: primary
    peer_priority: Literal["primary", "secondary"]
    
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
class InterControllerResponse(TypedDict):
    """
    Type hints for wireless_controller/inter_controller API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    inter_controller_mode: Literal["disable", "l2-roaming", "1+1"]  # Configure inter-controller mode | Default: disable
    l3_roaming: Literal["enable", "disable"]  # Enable/disable layer 3 roaming (default = disable) | Default: disable
    inter_controller_key: str  # Secret key for inter-controller communications. | MaxLen: 127
    inter_controller_pri: Literal["primary", "secondary"]  # Configure inter-controller's priority | Default: primary
    fast_failover_max: int  # Maximum number of retransmissions for fast failove | Default: 10 | Min: 3 | Max: 64
    fast_failover_wait: int  # Minimum wait time before an AP transitions from se | Default: 10 | Min: 10 | Max: 86400
    inter_controller_peer: list[InterControllerIntercontrollerpeerItem]  # Fast failover peer wireless controller list.


@final
class InterControllerObject:
    """Typed FortiObject for wireless_controller/inter_controller with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Configure inter-controller mode | Default: disable
    inter_controller_mode: Literal["disable", "l2-roaming", "1+1"]
    # Enable/disable layer 3 roaming (default = disable). | Default: disable
    l3_roaming: Literal["enable", "disable"]
    # Secret key for inter-controller communications. | MaxLen: 127
    inter_controller_key: str
    # Configure inter-controller's priority | Default: primary
    inter_controller_pri: Literal["primary", "secondary"]
    # Maximum number of retransmissions for fast failover HA messa | Default: 10 | Min: 3 | Max: 64
    fast_failover_max: int
    # Minimum wait time before an AP transitions from secondary co | Default: 10 | Min: 10 | Max: 86400
    fast_failover_wait: int
    # Fast failover peer wireless controller list.
    inter_controller_peer: list[InterControllerIntercontrollerpeerObject]
    
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
    def to_dict(self) -> InterControllerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class InterController:
    """
    Configure inter wireless controller operation.
    
    Path: wireless_controller/inter_controller
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject: ...
    
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
    ) -> InterControllerObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> InterControllerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InterControllerPayload | None = ...,
        inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = ...,
        l3_roaming: Literal["enable", "disable"] | None = ...,
        inter_controller_key: str | None = ...,
        inter_controller_pri: Literal["primary", "secondary"] | None = ...,
        fast_failover_max: int | None = ...,
        fast_failover_wait: int | None = ...,
        inter_controller_peer: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "InterController",
    "InterControllerPayload",
    "InterControllerResponse",
    "InterControllerObject",
]
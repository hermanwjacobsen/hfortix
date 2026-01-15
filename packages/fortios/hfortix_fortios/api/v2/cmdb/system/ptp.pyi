from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class PtpPayload(TypedDict, total=False):
    """
    Type hints for system/ptp payload fields.
    
    Configure system PTP information.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: PtpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable setting the FortiGate system time b | Default: disable
    mode: Literal["multicast", "hybrid"]  # Multicast transmission or hybrid transmission. | Default: multicast
    delay_mechanism: Literal["E2E", "P2P"]  # End to end delay detection or peer to peer delay d | Default: E2E
    request_interval: int  # The delay request value is the logarithmic mean in | Default: 1 | Min: 1 | Max: 6
    interface: str  # PTP client will reply through this interface. | MaxLen: 15
    server_mode: Literal["enable", "disable"]  # Enable/disable FortiGate PTP server mode. Your For | Default: disable
    server_interface: list[dict[str, Any]]  # FortiGate interface(s) with PTP server mode enable

# Nested TypedDicts for table field children (dict mode)

class PtpServerinterfaceItem(TypedDict):
    """Type hints for server-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    server_interface_name: str  # Interface name. | MaxLen: 15
    delay_mechanism: Literal["E2E", "P2P"]  # End to end delay detection or peer to peer delay d | Default: E2E


# Nested classes for table field children (object mode)

@final
class PtpServerinterfaceObject:
    """Typed object for server-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Interface name. | MaxLen: 15
    server_interface_name: str
    # End to end delay detection or peer to peer delay detection. | Default: E2E
    delay_mechanism: Literal["E2E", "P2P"]
    
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
class PtpResponse(TypedDict):
    """
    Type hints for system/ptp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable setting the FortiGate system time b | Default: disable
    mode: Literal["multicast", "hybrid"]  # Multicast transmission or hybrid transmission. | Default: multicast
    delay_mechanism: Literal["E2E", "P2P"]  # End to end delay detection or peer to peer delay d | Default: E2E
    request_interval: int  # The delay request value is the logarithmic mean in | Default: 1 | Min: 1 | Max: 6
    interface: str  # PTP client will reply through this interface. | MaxLen: 15
    server_mode: Literal["enable", "disable"]  # Enable/disable FortiGate PTP server mode. Your For | Default: disable
    server_interface: list[PtpServerinterfaceItem]  # FortiGate interface(s) with PTP server mode enable


@final
class PtpObject:
    """Typed FortiObject for system/ptp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable setting the FortiGate system time by synchron | Default: disable
    status: Literal["enable", "disable"]
    # Multicast transmission or hybrid transmission. | Default: multicast
    mode: Literal["multicast", "hybrid"]
    # End to end delay detection or peer to peer delay detection. | Default: E2E
    delay_mechanism: Literal["E2E", "P2P"]
    # The delay request value is the logarithmic mean interval in | Default: 1 | Min: 1 | Max: 6
    request_interval: int
    # PTP client will reply through this interface. | MaxLen: 15
    interface: str
    # Enable/disable FortiGate PTP server mode. Your FortiGate bec | Default: disable
    server_mode: Literal["enable", "disable"]
    # FortiGate interface(s) with PTP server mode enabled. Devices
    server_interface: list[PtpServerinterfaceObject]
    
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
    def to_dict(self) -> PtpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ptp:
    """
    Configure system PTP information.
    
    Path: system/ptp
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject: ...
    
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
    ) -> PtpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> PtpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: PtpPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        mode: Literal["multicast", "hybrid"] | None = ...,
        delay_mechanism: Literal["E2E", "P2P"] | None = ...,
        request_interval: int | None = ...,
        interface: str | None = ...,
        server_mode: Literal["enable", "disable"] | None = ...,
        server_interface: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Ptp",
    "PtpPayload",
    "PtpResponse",
    "PtpObject",
]
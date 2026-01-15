from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class TrafficSnifferPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/traffic_sniffer payload fields.
    
    Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
    
    **Usage:**
        payload: TrafficSnifferPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    mode: Literal["erspan-auto", "rspan", "none"]  # Configure traffic sniffer mode. | Default: erspan-auto
    erspan_ip: str  # Configure ERSPAN collector IP address. | Default: 0.0.0.0
    target_mac: list[dict[str, Any]]  # Sniffer MACs to filter.
    target_ip: list[dict[str, Any]]  # Sniffer IPs to filter.
    target_port: list[dict[str, Any]]  # Sniffer ports to filter.

# Nested TypedDicts for table field children (dict mode)

class TrafficSnifferTargetmacItem(TypedDict):
    """Type hints for target-mac table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    mac: str  # Sniffer MAC. | Default: 00:00:00:00:00:00
    description: str  # Description for the sniffer MAC. | MaxLen: 63


class TrafficSnifferTargetipItem(TypedDict):
    """Type hints for target-ip table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip: str  # Sniffer IP. | Default: 0.0.0.0
    description: str  # Description for the sniffer IP. | MaxLen: 63


class TrafficSnifferTargetportItem(TypedDict):
    """Type hints for target-port table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    switch_id: str  # Managed-switch ID. | MaxLen: 35
    description: str  # Description for the sniffer port entry. | MaxLen: 63
    in_ports: str  # Configure source ingress port interfaces.
    out_ports: str  # Configure source egress port interfaces.


# Nested classes for table field children (object mode)

@final
class TrafficSnifferTargetmacObject:
    """Typed object for target-mac table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Sniffer MAC. | Default: 00:00:00:00:00:00
    mac: str
    # Description for the sniffer MAC. | MaxLen: 63
    description: str
    
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


@final
class TrafficSnifferTargetipObject:
    """Typed object for target-ip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Sniffer IP. | Default: 0.0.0.0
    ip: str
    # Description for the sniffer IP. | MaxLen: 63
    description: str
    
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


@final
class TrafficSnifferTargetportObject:
    """Typed object for target-port table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Managed-switch ID. | MaxLen: 35
    switch_id: str
    # Description for the sniffer port entry. | MaxLen: 63
    description: str
    # Configure source ingress port interfaces.
    in_ports: str
    # Configure source egress port interfaces.
    out_ports: str
    
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
class TrafficSnifferResponse(TypedDict):
    """
    Type hints for switch_controller/traffic_sniffer API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    mode: Literal["erspan-auto", "rspan", "none"]  # Configure traffic sniffer mode. | Default: erspan-auto
    erspan_ip: str  # Configure ERSPAN collector IP address. | Default: 0.0.0.0
    target_mac: list[TrafficSnifferTargetmacItem]  # Sniffer MACs to filter.
    target_ip: list[TrafficSnifferTargetipItem]  # Sniffer IPs to filter.
    target_port: list[TrafficSnifferTargetportItem]  # Sniffer ports to filter.


@final
class TrafficSnifferObject:
    """Typed FortiObject for switch_controller/traffic_sniffer with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Configure traffic sniffer mode. | Default: erspan-auto
    mode: Literal["erspan-auto", "rspan", "none"]
    # Configure ERSPAN collector IP address. | Default: 0.0.0.0
    erspan_ip: str
    # Sniffer MACs to filter.
    target_mac: list[TrafficSnifferTargetmacObject]
    # Sniffer IPs to filter.
    target_ip: list[TrafficSnifferTargetipObject]
    # Sniffer ports to filter.
    target_port: list[TrafficSnifferTargetportObject]
    
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
    def to_dict(self) -> TrafficSnifferPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class TrafficSniffer:
    """
    Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
    
    Path: switch_controller/traffic_sniffer
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject: ...
    
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
    ) -> TrafficSnifferObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> TrafficSnifferObject: ...
    
    @overload
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: TrafficSnifferPayload | None = ...,
        mode: Literal["erspan-auto", "rspan", "none"] | None = ...,
        erspan_ip: str | None = ...,
        target_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        target_ip: str | list[str] | list[dict[str, Any]] | None = ...,
        target_port: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "TrafficSniffer",
    "TrafficSnifferPayload",
    "TrafficSnifferResponse",
    "TrafficSnifferObject",
]
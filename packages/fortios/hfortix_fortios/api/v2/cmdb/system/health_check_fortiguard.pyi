from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class HealthCheckFortiguardPayload(TypedDict, total=False):
    """
    Type hints for system/health_check_fortiguard payload fields.
    
    SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
    
    **Usage:**
        payload: HealthCheckFortiguardPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Status check or predefined health-check targets na | MaxLen: 35
    server: str  # Status check or predefined health-check domain nam | MaxLen: 127
    obsolete: int  # Indicates whether Health Check service can be used | Default: 0 | Min: 0 | Max: 255
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]  # Protocol name. | Default: ping

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class HealthCheckFortiguardResponse(TypedDict):
    """
    Type hints for system/health_check_fortiguard API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Status check or predefined health-check targets na | MaxLen: 35
    server: str  # Status check or predefined health-check domain nam | MaxLen: 127
    obsolete: int  # Indicates whether Health Check service can be used | Default: 0 | Min: 0 | Max: 255
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]  # Protocol name. | Default: ping


@final
class HealthCheckFortiguardObject:
    """Typed FortiObject for system/health_check_fortiguard with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Status check or predefined health-check targets name. | MaxLen: 35
    name: str
    # Status check or predefined health-check domain name. | MaxLen: 127
    server: str
    # Indicates whether Health Check service can be used. | Default: 0 | Min: 0 | Max: 255
    obsolete: int
    # Protocol name. | Default: ping
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]
    
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
    def to_dict(self) -> HealthCheckFortiguardPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HealthCheckFortiguard:
    """
    SD-WAN status checking or health checking. Identify a server predefine by FortiGuard and determine how SD-WAN verifies that FGT can communicate with it.
    
    Path: system/health_check_fortiguard
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
    ) -> HealthCheckFortiguardObject: ...
    
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
    ) -> HealthCheckFortiguardObject: ...
    
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
    ) -> FortiObjectList[HealthCheckFortiguardObject]: ...
    
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
    ) -> HealthCheckFortiguardObject: ...
    
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
    ) -> HealthCheckFortiguardObject: ...
    
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
    ) -> FortiObjectList[HealthCheckFortiguardObject]: ...
    
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
    ) -> HealthCheckFortiguardObject: ...
    
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
    ) -> HealthCheckFortiguardObject: ...
    
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
    ) -> FortiObjectList[HealthCheckFortiguardObject]: ...
    
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
    ) -> HealthCheckFortiguardObject | list[HealthCheckFortiguardObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> HealthCheckFortiguardObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> HealthCheckFortiguardObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> HealthCheckFortiguardObject: ...
    
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
        payload_dict: HealthCheckFortiguardPayload | None = ...,
        name: str | None = ...,
        server: str | None = ...,
        obsolete: int | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"] | None = ...,
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
    "HealthCheckFortiguard",
    "HealthCheckFortiguardPayload",
    "HealthCheckFortiguardResponse",
    "HealthCheckFortiguardObject",
]
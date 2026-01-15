from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WispPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/wisp payload fields.
    
    Configure Websense Integrated Services Protocol (WISP) servers.
    
    **Usage:**
        payload: WispPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Server name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    outgoing_ip: str  # WISP outgoing IP address. | Default: 0.0.0.0
    server_ip: str  # WISP server IP address. | Default: 0.0.0.0
    server_port: int  # WISP server port (1 - 65535, default = 15868). | Default: 15868 | Min: 1 | Max: 65535
    max_connections: int  # Maximum number of web proxy WISP connections | Default: 64 | Min: 4 | Max: 4096
    timeout: int  # Period of time before WISP requests time out | Default: 5 | Min: 1 | Max: 15

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class WispResponse(TypedDict):
    """
    Type hints for web_proxy/wisp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Server name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    outgoing_ip: str  # WISP outgoing IP address. | Default: 0.0.0.0
    server_ip: str  # WISP server IP address. | Default: 0.0.0.0
    server_port: int  # WISP server port (1 - 65535, default = 15868). | Default: 15868 | Min: 1 | Max: 65535
    max_connections: int  # Maximum number of web proxy WISP connections | Default: 64 | Min: 4 | Max: 4096
    timeout: int  # Period of time before WISP requests time out | Default: 5 | Min: 1 | Max: 15


@final
class WispObject:
    """Typed FortiObject for web_proxy/wisp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Server name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # WISP outgoing IP address. | Default: 0.0.0.0
    outgoing_ip: str
    # WISP server IP address. | Default: 0.0.0.0
    server_ip: str
    # WISP server port (1 - 65535, default = 15868). | Default: 15868 | Min: 1 | Max: 65535
    server_port: int
    # Maximum number of web proxy WISP connections | Default: 64 | Min: 4 | Max: 4096
    max_connections: int
    # Period of time before WISP requests time out | Default: 5 | Min: 1 | Max: 15
    timeout: int
    
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
    def to_dict(self) -> WispPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Wisp:
    """
    Configure Websense Integrated Services Protocol (WISP) servers.
    
    Path: web_proxy/wisp
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
    ) -> WispObject: ...
    
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
    ) -> WispObject: ...
    
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
    ) -> FortiObjectList[WispObject]: ...
    
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
    ) -> WispObject: ...
    
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
    ) -> WispObject: ...
    
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
    ) -> FortiObjectList[WispObject]: ...
    
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
    ) -> WispObject: ...
    
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
    ) -> WispObject: ...
    
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
    ) -> FortiObjectList[WispObject]: ...
    
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
    ) -> WispObject | list[WispObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> WispObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> WispObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WispObject: ...
    
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
        payload_dict: WispPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        outgoing_ip: str | None = ...,
        server_ip: str | None = ...,
        server_port: int | None = ...,
        max_connections: int | None = ...,
        timeout: int | None = ...,
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
    "Wisp",
    "WispPayload",
    "WispResponse",
    "WispObject",
]
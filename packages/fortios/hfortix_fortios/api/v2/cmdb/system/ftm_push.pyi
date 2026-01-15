from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FtmPushPayload(TypedDict, total=False):
    """
    Type hints for system/ftm_push payload fields.
    
    Configure FortiToken Mobile push services.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: server-cert)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: FtmPushPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    proxy: Literal["enable", "disable"]  # Enable/disable communication to the proxy server i | Default: enable
    interface: str  # Interface of FortiToken Mobile push services serve | MaxLen: 35
    server: str  # IPv4 address or domain name of FortiToken Mobile p | MaxLen: 127
    server_port: int  # Port to communicate with FortiToken Mobile push se | Default: 4433 | Min: 1 | Max: 65535
    server_cert: str  # Name of the server certificate to be used for SSL. | Default: Fortinet_GUI_Server | MaxLen: 35
    server_ip: str  # IPv4 address of FortiToken Mobile push services se | Default: 0.0.0.0
    status: Literal["enable", "disable"]  # Enable/disable the use of FortiToken Mobile push s | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class FtmPushResponse(TypedDict):
    """
    Type hints for system/ftm_push API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    proxy: Literal["enable", "disable"]  # Enable/disable communication to the proxy server i | Default: enable
    interface: str  # Interface of FortiToken Mobile push services serve | MaxLen: 35
    server: str  # IPv4 address or domain name of FortiToken Mobile p | MaxLen: 127
    server_port: int  # Port to communicate with FortiToken Mobile push se | Default: 4433 | Min: 1 | Max: 65535
    server_cert: str  # Name of the server certificate to be used for SSL. | Default: Fortinet_GUI_Server | MaxLen: 35
    server_ip: str  # IPv4 address of FortiToken Mobile push services se | Default: 0.0.0.0
    status: Literal["enable", "disable"]  # Enable/disable the use of FortiToken Mobile push s | Default: disable


@final
class FtmPushObject:
    """Typed FortiObject for system/ftm_push with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable communication to the proxy server in FortiGua | Default: enable
    proxy: Literal["enable", "disable"]
    # Interface of FortiToken Mobile push services server. | MaxLen: 35
    interface: str
    # IPv4 address or domain name of FortiToken Mobile push servic | MaxLen: 127
    server: str
    # Port to communicate with FortiToken Mobile push services ser | Default: 4433 | Min: 1 | Max: 65535
    server_port: int
    # Name of the server certificate to be used for SSL. | Default: Fortinet_GUI_Server | MaxLen: 35
    server_cert: str
    # IPv4 address of FortiToken Mobile push services server | Default: 0.0.0.0
    server_ip: str
    # Enable/disable the use of FortiToken Mobile push services. | Default: disable
    status: Literal["enable", "disable"]
    
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
    def to_dict(self) -> FtmPushPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FtmPush:
    """
    Configure FortiToken Mobile push services.
    
    Path: system/ftm_push
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject: ...
    
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
    ) -> FtmPushObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtmPushObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FtmPushPayload | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        interface: str | None = ...,
        server: str | None = ...,
        server_port: int | None = ...,
        server_cert: str | None = ...,
        server_ip: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
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
    "FtmPush",
    "FtmPushPayload",
    "FtmPushResponse",
    "FtmPushObject",
]
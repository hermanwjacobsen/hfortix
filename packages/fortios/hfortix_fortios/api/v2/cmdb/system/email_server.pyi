from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class EmailServerPayload(TypedDict, total=False):
    """
    Type hints for system/email_server payload fields.
    
    Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)

    **Usage:**
        payload: EmailServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    type: Literal["custom"]  # Use FortiGuard Message service or custom email ser | Default: custom
    server: str  # SMTP server IP address or hostname. | MaxLen: 63
    port: int  # SMTP server port. | Default: 25 | Min: 1 | Max: 65535
    source_ip: str  # SMTP server IPv4 source IP. | Default: 0.0.0.0
    source_ip6: str  # SMTP server IPv6 source IP. | Default: ::
    authenticate: Literal["enable", "disable"]  # Enable/disable authentication. | Default: disable
    validate_server: Literal["enable", "disable"]  # Enable/disable validation of server certificate. | Default: disable
    username: str  # SMTP server user name for authentication. | MaxLen: 255
    password: str  # SMTP server user password for authentication. | MaxLen: 128
    security: Literal["none", "starttls", "smtps"]  # Connection security used by the email server. | Default: none
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class EmailServerResponse(TypedDict):
    """
    Type hints for system/email_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    type: Literal["custom"]  # Use FortiGuard Message service or custom email ser | Default: custom
    server: str  # SMTP server IP address or hostname. | MaxLen: 63
    port: int  # SMTP server port. | Default: 25 | Min: 1 | Max: 65535
    source_ip: str  # SMTP server IPv4 source IP. | Default: 0.0.0.0
    source_ip6: str  # SMTP server IPv6 source IP. | Default: ::
    authenticate: Literal["enable", "disable"]  # Enable/disable authentication. | Default: disable
    validate_server: Literal["enable", "disable"]  # Enable/disable validation of server certificate. | Default: disable
    username: str  # SMTP server user name for authentication. | MaxLen: 255
    password: str  # SMTP server user password for authentication. | MaxLen: 128
    security: Literal["none", "starttls", "smtps"]  # Connection security used by the email server. | Default: none
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class EmailServerObject:
    """Typed FortiObject for system/email_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Use FortiGuard Message service or custom email server. | Default: custom
    type: Literal["custom"]
    # SMTP server IP address or hostname. | MaxLen: 63
    server: str
    # SMTP server port. | Default: 25 | Min: 1 | Max: 65535
    port: int
    # SMTP server IPv4 source IP. | Default: 0.0.0.0
    source_ip: str
    # SMTP server IPv6 source IP. | Default: ::
    source_ip6: str
    # Enable/disable authentication. | Default: disable
    authenticate: Literal["enable", "disable"]
    # Enable/disable validation of server certificate. | Default: disable
    validate_server: Literal["enable", "disable"]
    # SMTP server user name for authentication. | MaxLen: 255
    username: str
    # SMTP server user password for authentication. | MaxLen: 128
    password: str
    # Connection security used by the email server. | Default: none
    security: Literal["none", "starttls", "smtps"]
    # Minimum supported protocol version for SSL/TLS connections | Default: default
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
    def to_dict(self) -> EmailServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class EmailServer:
    """
    Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.
    
    Path: system/email_server
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject: ...
    
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
    ) -> EmailServerObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> EmailServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: EmailServerPayload | None = ...,
        type: Literal["custom"] | None = ...,
        server: str | None = ...,
        port: int | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        authenticate: Literal["enable", "disable"] | None = ...,
        validate_server: Literal["enable", "disable"] | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        security: Literal["none", "starttls", "smtps"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "EmailServer",
    "EmailServerPayload",
    "EmailServerResponse",
    "EmailServerObject",
]
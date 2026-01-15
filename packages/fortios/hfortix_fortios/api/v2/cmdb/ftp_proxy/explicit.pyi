from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ExplicitPayload(TypedDict, total=False):
    """
    Type hints for ftp_proxy/explicit payload fields.
    
    Configure explicit FTP proxy settings.
    
    **Usage:**
        payload: ExplicitPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable the explicit FTP proxy. | Default: disable
    incoming_port: str  # Accept incoming FTP requests on one or more ports.
    incoming_ip: str  # Accept incoming FTP requests from this IP address. | Default: 0.0.0.0
    outgoing_ip: list[dict[str, Any]]  # Outgoing FTP requests will leave from this IP addr
    sec_default_action: Literal["accept", "deny"]  # Accept or deny explicit FTP proxy sessions when no | Default: deny
    server_data_mode: Literal["client", "passive"]  # Determine mode of data session on FTP server side. | Default: client
    ssl: Literal["enable", "disable"]  # Enable/disable the explicit FTPS proxy. | Default: disable
    ssl_cert: list[dict[str, Any]]  # List of certificate names to use for SSL connectio
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE- | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Relative strength of encryption algorithms accepte | Default: high

# Nested TypedDicts for table field children (dict mode)

class ExplicitSslcertItem(TypedDict):
    """Type hints for ssl-cert table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate list. | Default: Fortinet_SSL | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class ExplicitSslcertObject:
    """Typed object for ssl-cert table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate list. | Default: Fortinet_SSL | MaxLen: 79
    name: str
    
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
class ExplicitResponse(TypedDict):
    """
    Type hints for ftp_proxy/explicit API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable the explicit FTP proxy. | Default: disable
    incoming_port: str  # Accept incoming FTP requests on one or more ports.
    incoming_ip: str  # Accept incoming FTP requests from this IP address. | Default: 0.0.0.0
    outgoing_ip: list[dict[str, Any]]  # Outgoing FTP requests will leave from this IP addr
    sec_default_action: Literal["accept", "deny"]  # Accept or deny explicit FTP proxy sessions when no | Default: deny
    server_data_mode: Literal["client", "passive"]  # Determine mode of data session on FTP server side. | Default: client
    ssl: Literal["enable", "disable"]  # Enable/disable the explicit FTPS proxy. | Default: disable
    ssl_cert: list[ExplicitSslcertItem]  # List of certificate names to use for SSL connectio
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE- | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Relative strength of encryption algorithms accepte | Default: high


@final
class ExplicitObject:
    """Typed FortiObject for ftp_proxy/explicit with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable the explicit FTP proxy. | Default: disable
    status: Literal["enable", "disable"]
    # Accept incoming FTP requests on one or more ports.
    incoming_port: str
    # Accept incoming FTP requests from this IP address. An interf | Default: 0.0.0.0
    incoming_ip: str
    # Outgoing FTP requests will leave from this IP address. An in
    outgoing_ip: list[dict[str, Any]]
    # Accept or deny explicit FTP proxy sessions when no FTP proxy | Default: deny
    sec_default_action: Literal["accept", "deny"]
    # Determine mode of data session on FTP server side. | Default: client
    server_data_mode: Literal["client", "passive"]
    # Enable/disable the explicit FTPS proxy. | Default: disable
    ssl: Literal["enable", "disable"]
    # List of certificate names to use for SSL connections to this
    ssl_cert: list[ExplicitSslcertObject]
    # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti | Default: 2048
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    # Relative strength of encryption algorithms accepted in negot | Default: high
    ssl_algorithm: Literal["high", "medium", "low"]
    
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
    def to_dict(self) -> ExplicitPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Explicit:
    """
    Configure explicit FTP proxy settings.
    
    Path: ftp_proxy/explicit
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
    ) -> ExplicitObject: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> ExplicitObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ExplicitObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ExplicitPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        incoming_port: str | None = ...,
        incoming_ip: str | None = ...,
        outgoing_ip: str | list[str] | None = ...,
        sec_default_action: Literal["accept", "deny"] | None = ...,
        server_data_mode: Literal["client", "passive"] | None = ...,
        ssl: Literal["enable", "disable"] | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
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
    "Explicit",
    "ExplicitPayload",
    "ExplicitResponse",
    "ExplicitObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SslServerPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl_server payload fields.
    
    Configure SSL servers.
    
    **Usage:**
        payload: SslServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Server name. | MaxLen: 35
    ip: str  # IPv4 address of the SSL server. | Default: 0.0.0.0
    port: int  # Server service port (1 - 65535, default = 443). | Default: 443 | Min: 1 | Max: 65535
    ssl_mode: Literal["half", "full"]  # SSL/TLS mode for encryption and decryption of traf | Default: full
    add_header_x_forwarded_proto: Literal["enable", "disable"]  # Enable/disable adding an X-Forwarded-Proto header | Default: enable
    mapped_port: int  # Mapped server service port | Default: 80 | Min: 1 | Max: 65535
    ssl_cert: list[dict[str, Any]]  # List of certificate names to use for SSL connectio
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE- | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Relative strength of encryption algorithms accepte | Default: high
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]  # Allow or block client renegotiation by server. | Default: allow
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version to negotiate. | Default: tls-1.1
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version to negotiate. | Default: tls-1.3
    ssl_send_empty_frags: Literal["enable", "disable"]  # Enable/disable sending empty fragments to avoid at | Default: enable
    url_rewrite: Literal["enable", "disable"]  # Enable/disable rewriting the URL. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class SslServerSslcertItem(TypedDict):
    """Type hints for ssl-cert table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate list. | Default: Fortinet_SSL | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class SslServerSslcertObject:
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
class SslServerResponse(TypedDict):
    """
    Type hints for firewall/ssl_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Server name. | MaxLen: 35
    ip: str  # IPv4 address of the SSL server. | Default: 0.0.0.0
    port: int  # Server service port (1 - 65535, default = 443). | Default: 443 | Min: 1 | Max: 65535
    ssl_mode: Literal["half", "full"]  # SSL/TLS mode for encryption and decryption of traf | Default: full
    add_header_x_forwarded_proto: Literal["enable", "disable"]  # Enable/disable adding an X-Forwarded-Proto header | Default: enable
    mapped_port: int  # Mapped server service port | Default: 80 | Min: 1 | Max: 65535
    ssl_cert: list[SslServerSslcertItem]  # List of certificate names to use for SSL connectio
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]  # Bit-size of Diffie-Hellman (DH) prime used in DHE- | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Relative strength of encryption algorithms accepte | Default: high
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]  # Allow or block client renegotiation by server. | Default: allow
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version to negotiate. | Default: tls-1.1
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version to negotiate. | Default: tls-1.3
    ssl_send_empty_frags: Literal["enable", "disable"]  # Enable/disable sending empty fragments to avoid at | Default: enable
    url_rewrite: Literal["enable", "disable"]  # Enable/disable rewriting the URL. | Default: disable


@final
class SslServerObject:
    """Typed FortiObject for firewall/ssl_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Server name. | MaxLen: 35
    name: str
    # IPv4 address of the SSL server. | Default: 0.0.0.0
    ip: str
    # Server service port (1 - 65535, default = 443). | Default: 443 | Min: 1 | Max: 65535
    port: int
    # SSL/TLS mode for encryption and decryption of traffic. | Default: full
    ssl_mode: Literal["half", "full"]
    # Enable/disable adding an X-Forwarded-Proto header to forward | Default: enable
    add_header_x_forwarded_proto: Literal["enable", "disable"]
    # Mapped server service port (1 - 65535, default = 80). | Default: 80 | Min: 1 | Max: 65535
    mapped_port: int
    # List of certificate names to use for SSL connections to this
    ssl_cert: list[SslServerSslcertObject]
    # Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negoti | Default: 2048
    ssl_dh_bits: Literal["768", "1024", "1536", "2048"]
    # Relative strength of encryption algorithms accepted in negot | Default: high
    ssl_algorithm: Literal["high", "medium", "low"]
    # Allow or block client renegotiation by server. | Default: allow
    ssl_client_renegotiation: Literal["allow", "deny", "secure"]
    # Lowest SSL/TLS version to negotiate. | Default: tls-1.1
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version to negotiate. | Default: tls-1.3
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Enable/disable sending empty fragments to avoid attack on CB | Default: enable
    ssl_send_empty_frags: Literal["enable", "disable"]
    # Enable/disable rewriting the URL. | Default: disable
    url_rewrite: Literal["enable", "disable"]
    
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
    def to_dict(self) -> SslServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SslServer:
    """
    Configure SSL servers.
    
    Path: firewall/ssl_server
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
    ) -> SslServerObject: ...
    
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
    ) -> SslServerObject: ...
    
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
    ) -> list[SslServerObject]: ...
    
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
    ) -> SslServerObject: ...
    
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
    ) -> SslServerObject: ...
    
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
    ) -> list[SslServerObject]: ...
    
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
    ) -> SslServerObject: ...
    
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
    ) -> SslServerObject: ...
    
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
    ) -> list[SslServerObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> SslServerObject | list[SslServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SslServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SslServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SslServerObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
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
        payload_dict: SslServerPayload | None = ...,
        name: str | None = ...,
        ip: str | None = ...,
        port: int | None = ...,
        ssl_mode: Literal["half", "full"] | None = ...,
        add_header_x_forwarded_proto: Literal["enable", "disable"] | None = ...,
        mapped_port: int | None = ...,
        ssl_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048"] | None = ...,
        ssl_algorithm: Literal["high", "medium", "low"] | None = ...,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = ...,
        ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = ...,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = ...,
        url_rewrite: Literal["enable", "disable"] | None = ...,
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
    "SslServer",
    "SslServerPayload",
    "SslServerResponse",
    "SslServerObject",
]
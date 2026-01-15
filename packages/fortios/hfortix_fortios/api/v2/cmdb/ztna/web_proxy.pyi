from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WebProxyPayload(TypedDict, total=False):
    """
    Type hints for ztna/web_proxy payload fields.
    
    Configure ZTNA web-proxy.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.access-proxy-virtual-host.AccessProxyVirtualHostEndpoint` (via: auth-virtual-host, host)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.vip.VipEndpoint` (via: vip)
        - :class:`~.firewall.vip6.Vip6Endpoint` (via: vip6)

    **Usage:**
        payload: WebProxyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # ZTNA proxy name. | MaxLen: 79
    vip: str  # Virtual IP name. | MaxLen: 79
    host: str  # Virtual or real host name. | MaxLen: 79
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    log_blocked_traffic: Literal["disable", "enable"]  # Enable/disable logging of blocked traffic. | Default: enable
    auth_portal: Literal["disable", "enable"]  # Enable/disable authentication portal. | Default: disable
    auth_virtual_host: str  # Virtual host for authentication portal. | MaxLen: 79
    vip6: str  # Virtual IPv6 name. | MaxLen: 79
    svr_pool_multiplex: Literal["enable", "disable"]  # Enable/disable server pool multiplexing | Default: disable
    svr_pool_ttl: int  # Time-to-live in the server pool for idle connectio | Default: 15 | Min: 0 | Max: 2147483647
    svr_pool_server_max_request: int  # Maximum number of requests that servers in the ser | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_concurrent_request: int  # Maximum number of concurrent requests that servers | Default: 0 | Min: 0 | Max: 2147483647
    api_gateway: list[dict[str, Any]]  # Set IPv4 API Gateway.
    api_gateway6: list[dict[str, Any]]  # Set IPv6 API Gateway.

# Nested TypedDicts for table field children (dict mode)

class WebProxyApigatewayItem(TypedDict):
    """Type hints for api-gateway table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    url_map: str  # URL pattern to match. | Default: / | MaxLen: 511
    service: Literal["http", "https"]  # Service. | Default: https
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]  # Method used to distribute sessions to real servers | Default: static
    url_map_type: Literal["sub-string", "wildcard", "regex"]  # Type of url-map. | Default: sub-string
    h2_support: Literal["enable", "disable"]  # HTTP2 support, default=Enable. | Default: enable
    h3_support: Literal["enable", "disable"]  # HTTP3/QUIC support, default=Disable. | Default: disable
    quic: str  # QUIC setting.
    realservers: str  # Select the real servers that this Access Proxy wil
    persistence: Literal["none", "http-cookie"]  # Configure how to make sure that clients connect to | Default: none
    http_cookie_domain_from_host: Literal["disable", "enable"]  # Enable/disable use of HTTP cookie domain from host | Default: disable
    http_cookie_domain: str  # Domain that HTTP cookie persistence should apply t | MaxLen: 35
    http_cookie_path: str  # Limit HTTP cookie persistence to the specified pat | MaxLen: 35
    http_cookie_generation: int  # Generation of HTTP cookie to be accepted. Changing | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_age: int  # Time in minutes that client web browsers should ke | Default: 60 | Min: 0 | Max: 525600
    http_cookie_share: Literal["disable", "same-ip"]  # Control sharing of cookies across API Gateway. Use | Default: same-ip
    https_cookie_secure: Literal["disable", "enable"]  # Enable/disable verification that inserted HTTPS co | Default: disable
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Permitted encryption algorithms for the server sid | Default: high
    ssl_cipher_suites: str  # SSL/TLS cipher suites to offer to a server, ordere
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version acceptable from a server. | Default: tls-1.1
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version acceptable from a server. | Default: tls-1.3
    ssl_renegotiation: Literal["enable", "disable"]  # Enable/disable secure renegotiation to comply with | Default: enable


class WebProxyApigateway6Item(TypedDict):
    """Type hints for api-gateway6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    url_map: str  # URL pattern to match. | Default: / | MaxLen: 511
    service: Literal["http", "https"]  # Service. | Default: https
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]  # Method used to distribute sessions to real servers | Default: static
    url_map_type: Literal["sub-string", "wildcard", "regex"]  # Type of url-map. | Default: sub-string
    h2_support: Literal["enable", "disable"]  # HTTP2 support, default=Enable. | Default: enable
    h3_support: Literal["enable", "disable"]  # HTTP3/QUIC support, default=Disable. | Default: disable
    quic: str  # QUIC setting.
    realservers: str  # Select the real servers that this Access Proxy wil
    persistence: Literal["none", "http-cookie"]  # Configure how to make sure that clients connect to | Default: none
    http_cookie_domain_from_host: Literal["disable", "enable"]  # Enable/disable use of HTTP cookie domain from host | Default: disable
    http_cookie_domain: str  # Domain that HTTP cookie persistence should apply t | MaxLen: 35
    http_cookie_path: str  # Limit HTTP cookie persistence to the specified pat | MaxLen: 35
    http_cookie_generation: int  # Generation of HTTP cookie to be accepted. Changing | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_age: int  # Time in minutes that client web browsers should ke | Default: 60 | Min: 0 | Max: 525600
    http_cookie_share: Literal["disable", "same-ip"]  # Control sharing of cookies across API Gateway. Use | Default: same-ip
    https_cookie_secure: Literal["disable", "enable"]  # Enable/disable verification that inserted HTTPS co | Default: disable
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Permitted encryption algorithms for the server sid | Default: high
    ssl_cipher_suites: str  # SSL/TLS cipher suites to offer to a server, ordere
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version acceptable from a server. | Default: tls-1.1
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version acceptable from a server. | Default: tls-1.3
    ssl_renegotiation: Literal["enable", "disable"]  # Enable/disable secure renegotiation to comply with | Default: enable


# Nested classes for table field children (object mode)

@final
class WebProxyApigatewayObject:
    """Typed object for api-gateway table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # URL pattern to match. | Default: / | MaxLen: 511
    url_map: str
    # Service. | Default: https
    service: Literal["http", "https"]
    # Method used to distribute sessions to real servers. | Default: static
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    # Type of url-map. | Default: sub-string
    url_map_type: Literal["sub-string", "wildcard", "regex"]
    # HTTP2 support, default=Enable. | Default: enable
    h2_support: Literal["enable", "disable"]
    # HTTP3/QUIC support, default=Disable. | Default: disable
    h3_support: Literal["enable", "disable"]
    # QUIC setting.
    quic: str
    # Select the real servers that this Access Proxy will distribu
    realservers: str
    # Configure how to make sure that clients connect to the same | Default: none
    persistence: Literal["none", "http-cookie"]
    # Enable/disable use of HTTP cookie domain from host field in | Default: disable
    http_cookie_domain_from_host: Literal["disable", "enable"]
    # Domain that HTTP cookie persistence should apply to. | MaxLen: 35
    http_cookie_domain: str
    # Limit HTTP cookie persistence to the specified path. | MaxLen: 35
    http_cookie_path: str
    # Generation of HTTP cookie to be accepted. Changing invalidat | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_generation: int
    # Time in minutes that client web browsers should keep a cooki | Default: 60 | Min: 0 | Max: 525600
    http_cookie_age: int
    # Control sharing of cookies across API Gateway. Use of same-i | Default: same-ip
    http_cookie_share: Literal["disable", "same-ip"]
    # Enable/disable verification that inserted HTTPS cookies are | Default: disable
    https_cookie_secure: Literal["disable", "enable"]
    # Number of bits to use in the Diffie-Hellman exchange for RSA | Default: 2048
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    # Permitted encryption algorithms for the server side of SSL f | Default: high
    ssl_algorithm: Literal["high", "medium", "low"]
    # SSL/TLS cipher suites to offer to a server, ordered by prior
    ssl_cipher_suites: str
    # Lowest SSL/TLS version acceptable from a server. | Default: tls-1.1
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version acceptable from a server. | Default: tls-1.3
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Enable/disable secure renegotiation to comply with RFC 5746. | Default: enable
    ssl_renegotiation: Literal["enable", "disable"]
    
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
class WebProxyApigateway6Object:
    """Typed object for api-gateway6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # URL pattern to match. | Default: / | MaxLen: 511
    url_map: str
    # Service. | Default: https
    service: Literal["http", "https"]
    # Method used to distribute sessions to real servers. | Default: static
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    # Type of url-map. | Default: sub-string
    url_map_type: Literal["sub-string", "wildcard", "regex"]
    # HTTP2 support, default=Enable. | Default: enable
    h2_support: Literal["enable", "disable"]
    # HTTP3/QUIC support, default=Disable. | Default: disable
    h3_support: Literal["enable", "disable"]
    # QUIC setting.
    quic: str
    # Select the real servers that this Access Proxy will distribu
    realservers: str
    # Configure how to make sure that clients connect to the same | Default: none
    persistence: Literal["none", "http-cookie"]
    # Enable/disable use of HTTP cookie domain from host field in | Default: disable
    http_cookie_domain_from_host: Literal["disable", "enable"]
    # Domain that HTTP cookie persistence should apply to. | MaxLen: 35
    http_cookie_domain: str
    # Limit HTTP cookie persistence to the specified path. | MaxLen: 35
    http_cookie_path: str
    # Generation of HTTP cookie to be accepted. Changing invalidat | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_generation: int
    # Time in minutes that client web browsers should keep a cooki | Default: 60 | Min: 0 | Max: 525600
    http_cookie_age: int
    # Control sharing of cookies across API Gateway. Use of same-i | Default: same-ip
    http_cookie_share: Literal["disable", "same-ip"]
    # Enable/disable verification that inserted HTTPS cookies are | Default: disable
    https_cookie_secure: Literal["disable", "enable"]
    # Number of bits to use in the Diffie-Hellman exchange for RSA | Default: 2048
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]
    # Permitted encryption algorithms for the server side of SSL f | Default: high
    ssl_algorithm: Literal["high", "medium", "low"]
    # SSL/TLS cipher suites to offer to a server, ordered by prior
    ssl_cipher_suites: str
    # Lowest SSL/TLS version acceptable from a server. | Default: tls-1.1
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Highest SSL/TLS version acceptable from a server. | Default: tls-1.3
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]
    # Enable/disable secure renegotiation to comply with RFC 5746. | Default: enable
    ssl_renegotiation: Literal["enable", "disable"]
    
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
class WebProxyResponse(TypedDict):
    """
    Type hints for ztna/web_proxy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # ZTNA proxy name. | MaxLen: 79
    vip: str  # Virtual IP name. | MaxLen: 79
    host: str  # Virtual or real host name. | MaxLen: 79
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    log_blocked_traffic: Literal["disable", "enable"]  # Enable/disable logging of blocked traffic. | Default: enable
    auth_portal: Literal["disable", "enable"]  # Enable/disable authentication portal. | Default: disable
    auth_virtual_host: str  # Virtual host for authentication portal. | MaxLen: 79
    vip6: str  # Virtual IPv6 name. | MaxLen: 79
    svr_pool_multiplex: Literal["enable", "disable"]  # Enable/disable server pool multiplexing | Default: disable
    svr_pool_ttl: int  # Time-to-live in the server pool for idle connectio | Default: 15 | Min: 0 | Max: 2147483647
    svr_pool_server_max_request: int  # Maximum number of requests that servers in the ser | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_concurrent_request: int  # Maximum number of concurrent requests that servers | Default: 0 | Min: 0 | Max: 2147483647
    api_gateway: list[WebProxyApigatewayItem]  # Set IPv4 API Gateway.
    api_gateway6: list[WebProxyApigateway6Item]  # Set IPv6 API Gateway.


@final
class WebProxyObject:
    """Typed FortiObject for ztna/web_proxy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ZTNA proxy name. | MaxLen: 79
    name: str
    # Virtual IP name. | MaxLen: 79
    vip: str
    # Virtual or real host name. | MaxLen: 79
    host: str
    # Decrypted traffic mirror. | MaxLen: 35
    decrypted_traffic_mirror: str
    # Enable/disable logging of blocked traffic. | Default: enable
    log_blocked_traffic: Literal["disable", "enable"]
    # Enable/disable authentication portal. | Default: disable
    auth_portal: Literal["disable", "enable"]
    # Virtual host for authentication portal. | MaxLen: 79
    auth_virtual_host: str
    # Virtual IPv6 name. | MaxLen: 79
    vip6: str
    # Enable/disable server pool multiplexing (default = disable). | Default: disable
    svr_pool_multiplex: Literal["enable", "disable"]
    # Time-to-live in the server pool for idle connections to serv | Default: 15 | Min: 0 | Max: 2147483647
    svr_pool_ttl: int
    # Maximum number of requests that servers in the server pool h | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_request: int
    # Maximum number of concurrent requests that servers in the se | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_concurrent_request: int
    # Set IPv4 API Gateway.
    api_gateway: list[WebProxyApigatewayObject]
    # Set IPv6 API Gateway.
    api_gateway6: list[WebProxyApigateway6Object]
    
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
    def to_dict(self) -> WebProxyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class WebProxy:
    """
    Configure ZTNA web-proxy.
    
    Path: ztna/web_proxy
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
    ) -> WebProxyObject: ...
    
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
    ) -> WebProxyObject: ...
    
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
    ) -> list[WebProxyObject]: ...
    
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
    ) -> WebProxyObject: ...
    
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
    ) -> WebProxyObject: ...
    
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
    ) -> list[WebProxyObject]: ...
    
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
    ) -> WebProxyObject: ...
    
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
    ) -> WebProxyObject: ...
    
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
    ) -> list[WebProxyObject]: ...
    
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
    ) -> WebProxyObject | list[WebProxyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> WebProxyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> WebProxyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> WebProxyObject: ...
    
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
        payload_dict: WebProxyPayload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        host: str | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        log_blocked_traffic: Literal["disable", "enable"] | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        vip6: str | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "WebProxy",
    "WebProxyPayload",
    "WebProxyResponse",
    "WebProxyObject",
]
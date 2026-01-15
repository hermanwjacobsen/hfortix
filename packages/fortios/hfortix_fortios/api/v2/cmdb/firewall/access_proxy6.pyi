from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AccessProxy6Payload(TypedDict, total=False):
    """
    Type hints for firewall/access_proxy6 payload fields.
    
    Configure IPv6 access proxy.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.access-proxy-virtual-host.AccessProxyVirtualHostEndpoint` (via: auth-virtual-host)
        - :class:`~.firewall.decrypted-traffic-mirror.DecryptedTrafficMirrorEndpoint` (via: decrypted-traffic-mirror)
        - :class:`~.firewall.vip6.Vip6Endpoint` (via: vip)

    **Usage:**
        payload: AccessProxy6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Access Proxy name. | MaxLen: 79
    vip: str  # Virtual IP name. | MaxLen: 79
    auth_portal: Literal["disable", "enable"]  # Enable/disable authentication portal. | Default: disable
    auth_virtual_host: str  # Virtual host for authentication portal. | MaxLen: 79
    log_blocked_traffic: Literal["enable", "disable"]  # Enable/disable logging of blocked traffic. | Default: enable
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]  # Enable/disable adding vhost/domain to dnsdb for zt | Default: disable
    svr_pool_multiplex: Literal["enable", "disable"]  # Enable/disable server pool multiplexing | Default: disable
    svr_pool_ttl: int  # Time-to-live in the server pool for idle connectio | Default: 15 | Min: 0 | Max: 2147483647
    svr_pool_server_max_request: int  # Maximum number of requests that servers in server | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_concurrent_request: int  # Maximum number of concurrent requests that servers | Default: 0 | Min: 0 | Max: 2147483647
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    api_gateway: list[dict[str, Any]]  # Set IPv4 API Gateway.
    api_gateway6: list[dict[str, Any]]  # Set IPv6 API Gateway.

# Nested TypedDicts for table field children (dict mode)

class AccessProxy6ApigatewayItem(TypedDict):
    """Type hints for api-gateway table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    url_map: str  # URL pattern to match. | Default: / | MaxLen: 511
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]  # Service. | Default: https
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]  # Method used to distribute sessions to real servers | Default: static
    virtual_host: str  # Virtual host. | MaxLen: 79
    url_map_type: Literal["sub-string", "wildcard", "regex"]  # Type of url-map. | Default: sub-string
    h2_support: Literal["enable", "disable"]  # HTTP2 support, default=Enable. | Default: enable
    h3_support: Literal["enable", "disable"]  # HTTP3/QUIC support, default=Disable. | Default: disable
    quic: str  # QUIC setting.
    realservers: str  # Select the real servers that this Access Proxy wil
    application: str  # SaaS application controlled by this Access Proxy.
    persistence: Literal["none", "http-cookie"]  # Configure how to make sure that clients connect to | Default: none
    http_cookie_domain_from_host: Literal["disable", "enable"]  # Enable/disable use of HTTP cookie domain from host | Default: disable
    http_cookie_domain: str  # Domain that HTTP cookie persistence should apply t | MaxLen: 35
    http_cookie_path: str  # Limit HTTP cookie persistence to the specified pat | MaxLen: 35
    http_cookie_generation: int  # Generation of HTTP cookie to be accepted. Changing | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_age: int  # Time in minutes that client web browsers should ke | Default: 60 | Min: 0 | Max: 525600
    http_cookie_share: Literal["disable", "same-ip"]  # Control sharing of cookies across API Gateway. Use | Default: same-ip
    https_cookie_secure: Literal["disable", "enable"]  # Enable/disable verification that inserted HTTPS co | Default: disable
    saml_server: str  # SAML service provider configuration for VIP authen | MaxLen: 35
    saml_redirect: Literal["disable", "enable"]  # Enable/disable SAML redirection after successful a | Default: enable
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Permitted encryption algorithms for the server sid | Default: high
    ssl_cipher_suites: str  # SSL/TLS cipher suites to offer to a server, ordere
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version acceptable from a server. | Default: tls-1.1
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version acceptable from a server. | Default: tls-1.3
    ssl_renegotiation: Literal["enable", "disable"]  # Enable/disable secure renegotiation to comply with | Default: enable
    ssl_vpn_web_portal: str  # Agentless VPN web portal. | MaxLen: 35


class AccessProxy6Apigateway6Item(TypedDict):
    """Type hints for api-gateway6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    url_map: str  # URL pattern to match. | Default: / | MaxLen: 511
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]  # Service. | Default: https
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]  # Method used to distribute sessions to real servers | Default: static
    virtual_host: str  # Virtual host. | MaxLen: 79
    url_map_type: Literal["sub-string", "wildcard", "regex"]  # Type of url-map. | Default: sub-string
    h2_support: Literal["enable", "disable"]  # HTTP2 support, default=Enable. | Default: enable
    h3_support: Literal["enable", "disable"]  # HTTP3/QUIC support, default=Disable. | Default: disable
    quic: str  # QUIC setting.
    realservers: str  # Select the real servers that this Access Proxy wil
    application: str  # SaaS application controlled by this Access Proxy.
    persistence: Literal["none", "http-cookie"]  # Configure how to make sure that clients connect to | Default: none
    http_cookie_domain_from_host: Literal["disable", "enable"]  # Enable/disable use of HTTP cookie domain from host | Default: disable
    http_cookie_domain: str  # Domain that HTTP cookie persistence should apply t | MaxLen: 35
    http_cookie_path: str  # Limit HTTP cookie persistence to the specified pat | MaxLen: 35
    http_cookie_generation: int  # Generation of HTTP cookie to be accepted. Changing | Default: 0 | Min: 0 | Max: 4294967295
    http_cookie_age: int  # Time in minutes that client web browsers should ke | Default: 60 | Min: 0 | Max: 525600
    http_cookie_share: Literal["disable", "same-ip"]  # Control sharing of cookies across API Gateway. Use | Default: same-ip
    https_cookie_secure: Literal["disable", "enable"]  # Enable/disable verification that inserted HTTPS co | Default: disable
    saml_server: str  # SAML service provider configuration for VIP authen | MaxLen: 35
    saml_redirect: Literal["disable", "enable"]  # Enable/disable SAML redirection after successful a | Default: enable
    ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"]  # Number of bits to use in the Diffie-Hellman exchan | Default: 2048
    ssl_algorithm: Literal["high", "medium", "low"]  # Permitted encryption algorithms for the server sid | Default: high
    ssl_cipher_suites: str  # SSL/TLS cipher suites to offer to a server, ordere
    ssl_min_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Lowest SSL/TLS version acceptable from a server. | Default: tls-1.1
    ssl_max_version: Literal["tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"]  # Highest SSL/TLS version acceptable from a server. | Default: tls-1.3
    ssl_renegotiation: Literal["enable", "disable"]  # Enable/disable secure renegotiation to comply with | Default: enable
    ssl_vpn_web_portal: str  # Agentless VPN web portal. | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class AccessProxy6ApigatewayObject:
    """Typed object for api-gateway table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # URL pattern to match. | Default: / | MaxLen: 511
    url_map: str
    # Service. | Default: https
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]
    # Method used to distribute sessions to real servers. | Default: static
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    # Virtual host. | MaxLen: 79
    virtual_host: str
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
    # SaaS application controlled by this Access Proxy.
    application: str
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
    # SAML service provider configuration for VIP authentication. | MaxLen: 35
    saml_server: str
    # Enable/disable SAML redirection after successful authenticat | Default: enable
    saml_redirect: Literal["disable", "enable"]
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
    # Agentless VPN web portal. | MaxLen: 35
    ssl_vpn_web_portal: str
    
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
class AccessProxy6Apigateway6Object:
    """Typed object for api-gateway6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # API Gateway ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # URL pattern to match. | Default: / | MaxLen: 511
    url_map: str
    # Service. | Default: https
    service: Literal["http", "https", "tcp-forwarding", "samlsp", "web-portal", "saas"]
    # Method used to distribute sessions to real servers. | Default: static
    ldb_method: Literal["static", "round-robin", "weighted", "first-alive", "http-host"]
    # Virtual host. | MaxLen: 79
    virtual_host: str
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
    # SaaS application controlled by this Access Proxy.
    application: str
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
    # SAML service provider configuration for VIP authentication. | MaxLen: 35
    saml_server: str
    # Enable/disable SAML redirection after successful authenticat | Default: enable
    saml_redirect: Literal["disable", "enable"]
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
    # Agentless VPN web portal. | MaxLen: 35
    ssl_vpn_web_portal: str
    
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
class AccessProxy6Response(TypedDict):
    """
    Type hints for firewall/access_proxy6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Access Proxy name. | MaxLen: 79
    vip: str  # Virtual IP name. | MaxLen: 79
    auth_portal: Literal["disable", "enable"]  # Enable/disable authentication portal. | Default: disable
    auth_virtual_host: str  # Virtual host for authentication portal. | MaxLen: 79
    log_blocked_traffic: Literal["enable", "disable"]  # Enable/disable logging of blocked traffic. | Default: enable
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]  # Enable/disable adding vhost/domain to dnsdb for zt | Default: disable
    svr_pool_multiplex: Literal["enable", "disable"]  # Enable/disable server pool multiplexing | Default: disable
    svr_pool_ttl: int  # Time-to-live in the server pool for idle connectio | Default: 15 | Min: 0 | Max: 2147483647
    svr_pool_server_max_request: int  # Maximum number of requests that servers in server | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_concurrent_request: int  # Maximum number of concurrent requests that servers | Default: 0 | Min: 0 | Max: 2147483647
    decrypted_traffic_mirror: str  # Decrypted traffic mirror. | MaxLen: 35
    api_gateway: list[AccessProxy6ApigatewayItem]  # Set IPv4 API Gateway.
    api_gateway6: list[AccessProxy6Apigateway6Item]  # Set IPv6 API Gateway.


@final
class AccessProxy6Object:
    """Typed FortiObject for firewall/access_proxy6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Access Proxy name. | MaxLen: 79
    name: str
    # Virtual IP name. | MaxLen: 79
    vip: str
    # Enable/disable authentication portal. | Default: disable
    auth_portal: Literal["disable", "enable"]
    # Virtual host for authentication portal. | MaxLen: 79
    auth_virtual_host: str
    # Enable/disable logging of blocked traffic. | Default: enable
    log_blocked_traffic: Literal["enable", "disable"]
    # Enable/disable adding vhost/domain to dnsdb for ztna dox tun | Default: disable
    add_vhost_domain_to_dnsdb: Literal["enable", "disable"]
    # Enable/disable server pool multiplexing (default = disable). | Default: disable
    svr_pool_multiplex: Literal["enable", "disable"]
    # Time-to-live in the server pool for idle connections to serv | Default: 15 | Min: 0 | Max: 2147483647
    svr_pool_ttl: int
    # Maximum number of requests that servers in server pool handl | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_request: int
    # Maximum number of concurrent requests that servers in server | Default: 0 | Min: 0 | Max: 2147483647
    svr_pool_server_max_concurrent_request: int
    # Decrypted traffic mirror. | MaxLen: 35
    decrypted_traffic_mirror: str
    # Set IPv4 API Gateway.
    api_gateway: list[AccessProxy6ApigatewayObject]
    # Set IPv6 API Gateway.
    api_gateway6: list[AccessProxy6Apigateway6Object]
    
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
    def to_dict(self) -> AccessProxy6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AccessProxy6:
    """
    Configure IPv6 access proxy.
    
    Path: firewall/access_proxy6
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> FortiObjectList[AccessProxy6Object]: ...
    
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> FortiObjectList[AccessProxy6Object]: ...
    
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> AccessProxy6Object: ...
    
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
    ) -> FortiObjectList[AccessProxy6Object]: ...
    
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
    ) -> AccessProxy6Object | list[AccessProxy6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccessProxy6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccessProxy6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AccessProxy6Object: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AccessProxy6Payload | None = ...,
        name: str | None = ...,
        vip: str | None = ...,
        auth_portal: Literal["disable", "enable"] | None = ...,
        auth_virtual_host: str | None = ...,
        log_blocked_traffic: Literal["enable", "disable"] | None = ...,
        add_vhost_domain_to_dnsdb: Literal["enable", "disable"] | None = ...,
        svr_pool_multiplex: Literal["enable", "disable"] | None = ...,
        svr_pool_ttl: int | None = ...,
        svr_pool_server_max_request: int | None = ...,
        svr_pool_server_max_concurrent_request: int | None = ...,
        decrypted_traffic_mirror: str | None = ...,
        api_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        api_gateway6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "AccessProxy6",
    "AccessProxy6Payload",
    "AccessProxy6Response",
    "AccessProxy6Object",
]
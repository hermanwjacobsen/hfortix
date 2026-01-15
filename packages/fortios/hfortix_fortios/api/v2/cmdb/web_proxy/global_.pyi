from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class GlobalPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/global_ payload fields.
    
    Configure Web proxy global settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.hsm-local.HsmLocalEndpoint` (via: ssl-ca-cert)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: ssl-ca-cert, ssl-cert)
        - :class:`~.web-proxy.profile.ProfileEndpoint` (via: webproxy-profile)

    **Usage:**
        payload: GlobalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ssl_cert: str  # SSL certificate for SSL interception. | Default: Fortinet_Factory | MaxLen: 35
    ssl_ca_cert: str  # SSL CA certificate for SSL interception. | Default: Fortinet_CA_SSL | MaxLen: 35
    fast_policy_match: Literal["enable", "disable"]  # Enable/disable fast matching algorithm for explici | Default: enable
    ldap_user_cache: Literal["enable", "disable"]  # Enable/disable LDAP user cache for explicit and tr | Default: disable
    proxy_fqdn: str  # Fully Qualified Domain Name of the explicit web pr | Default: default.fqdn | MaxLen: 255
    max_request_length: int  # Maximum length of HTTP request line | Default: 8 | Min: 2 | Max: 64
    max_message_length: int  # Maximum length of HTTP message, not including body | Default: 32 | Min: 16 | Max: 256
    http2_client_window_size: int  # HTTP/2 client initial window size in bytes | Default: 1048576 | Min: 65535 | Max: 2147483647
    http2_server_window_size: int  # HTTP/2 server initial window size in bytes | Default: 1048576 | Min: 65535 | Max: 2147483647
    auth_sign_timeout: int  # Proxy auth query sign timeout in seconds | Default: 120 | Min: 30 | Max: 3600
    strict_web_check: Literal["enable", "disable"]  # Enable/disable strict web checking to block web si | Default: disable
    forward_proxy_auth: Literal["enable", "disable"]  # Enable/disable forwarding proxy authentication hea | Default: disable
    forward_server_affinity_timeout: int  # Period of time before the source IP's traffic is n | Default: 30 | Min: 6 | Max: 60
    max_waf_body_cache_length: int  # Maximum length of HTTP messages processed by Web A | Default: 1 | Min: 1 | Max: 1024
    webproxy_profile: str  # Name of the web proxy profile to apply when explic | MaxLen: 63
    learn_client_ip: Literal["enable", "disable"]  # Enable/disable learning the client's IP address fr | Default: disable
    always_learn_client_ip: Literal["enable", "disable"]  # Enable/disable learning the client's IP address fr | Default: disable
    learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"]  # Learn client IP address from the specified headers
    learn_client_ip_srcaddr: list[dict[str, Any]]  # Source address name
    learn_client_ip_srcaddr6: list[dict[str, Any]]  # IPv6 Source address name
    src_affinity_exempt_addr: list[dict[str, Any]]  # IPv4 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr6: list[dict[str, Any]]  # IPv6 source addresses to exempt proxy affinity.
    policy_partial_match: Literal["enable", "disable"]  # Enable/disable policy partial matching. | Default: enable
    log_policy_pending: Literal["enable", "disable"]  # Enable/disable logging sessions that are pending o | Default: disable
    log_forward_server: Literal["enable", "disable"]  # Enable/disable forward server name logging in forw | Default: disable
    log_app_id: Literal["enable", "disable"]  # Enable/disable always log application type in traf | Default: disable
    proxy_transparent_cert_inspection: Literal["enable", "disable"]  # Enable/disable transparent proxy certificate inspe | Default: disable
    request_obs_fold: Literal["replace-with-sp", "block", "keep"]  # Action when HTTP/1.x request header contains obs-f | Default: keep

# Nested TypedDicts for table field children (dict mode)

class GlobalLearnclientipsrcaddrItem(TypedDict):
    """Type hints for learn-client-ip-srcaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class GlobalLearnclientipsrcaddr6Item(TypedDict):
    """Type hints for learn-client-ip-srcaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class GlobalLearnclientipsrcaddrObject:
    """Typed object for learn-client-ip-srcaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
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


@final
class GlobalLearnclientipsrcaddr6Object:
    """Typed object for learn-client-ip-srcaddr6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
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
class GlobalResponse(TypedDict):
    """
    Type hints for web_proxy/global_ API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ssl_cert: str  # SSL certificate for SSL interception. | Default: Fortinet_Factory | MaxLen: 35
    ssl_ca_cert: str  # SSL CA certificate for SSL interception. | Default: Fortinet_CA_SSL | MaxLen: 35
    fast_policy_match: Literal["enable", "disable"]  # Enable/disable fast matching algorithm for explici | Default: enable
    ldap_user_cache: Literal["enable", "disable"]  # Enable/disable LDAP user cache for explicit and tr | Default: disable
    proxy_fqdn: str  # Fully Qualified Domain Name of the explicit web pr | Default: default.fqdn | MaxLen: 255
    max_request_length: int  # Maximum length of HTTP request line | Default: 8 | Min: 2 | Max: 64
    max_message_length: int  # Maximum length of HTTP message, not including body | Default: 32 | Min: 16 | Max: 256
    http2_client_window_size: int  # HTTP/2 client initial window size in bytes | Default: 1048576 | Min: 65535 | Max: 2147483647
    http2_server_window_size: int  # HTTP/2 server initial window size in bytes | Default: 1048576 | Min: 65535 | Max: 2147483647
    auth_sign_timeout: int  # Proxy auth query sign timeout in seconds | Default: 120 | Min: 30 | Max: 3600
    strict_web_check: Literal["enable", "disable"]  # Enable/disable strict web checking to block web si | Default: disable
    forward_proxy_auth: Literal["enable", "disable"]  # Enable/disable forwarding proxy authentication hea | Default: disable
    forward_server_affinity_timeout: int  # Period of time before the source IP's traffic is n | Default: 30 | Min: 6 | Max: 60
    max_waf_body_cache_length: int  # Maximum length of HTTP messages processed by Web A | Default: 1 | Min: 1 | Max: 1024
    webproxy_profile: str  # Name of the web proxy profile to apply when explic | MaxLen: 63
    learn_client_ip: Literal["enable", "disable"]  # Enable/disable learning the client's IP address fr | Default: disable
    always_learn_client_ip: Literal["enable", "disable"]  # Enable/disable learning the client's IP address fr | Default: disable
    learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"]  # Learn client IP address from the specified headers
    learn_client_ip_srcaddr: list[GlobalLearnclientipsrcaddrItem]  # Source address name
    learn_client_ip_srcaddr6: list[GlobalLearnclientipsrcaddr6Item]  # IPv6 Source address name
    src_affinity_exempt_addr: list[dict[str, Any]]  # IPv4 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr6: list[dict[str, Any]]  # IPv6 source addresses to exempt proxy affinity.
    policy_partial_match: Literal["enable", "disable"]  # Enable/disable policy partial matching. | Default: enable
    log_policy_pending: Literal["enable", "disable"]  # Enable/disable logging sessions that are pending o | Default: disable
    log_forward_server: Literal["enable", "disable"]  # Enable/disable forward server name logging in forw | Default: disable
    log_app_id: Literal["enable", "disable"]  # Enable/disable always log application type in traf | Default: disable
    proxy_transparent_cert_inspection: Literal["enable", "disable"]  # Enable/disable transparent proxy certificate inspe | Default: disable
    request_obs_fold: Literal["replace-with-sp", "block", "keep"]  # Action when HTTP/1.x request header contains obs-f | Default: keep


@final
class GlobalObject:
    """Typed FortiObject for web_proxy/global_ with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SSL certificate for SSL interception. | Default: Fortinet_Factory | MaxLen: 35
    ssl_cert: str
    # SSL CA certificate for SSL interception. | Default: Fortinet_CA_SSL | MaxLen: 35
    ssl_ca_cert: str
    # Enable/disable fast matching algorithm for explicit and tran | Default: enable
    fast_policy_match: Literal["enable", "disable"]
    # Enable/disable LDAP user cache for explicit and transparent | Default: disable
    ldap_user_cache: Literal["enable", "disable"]
    # Fully Qualified Domain Name of the explicit web proxy | Default: default.fqdn | MaxLen: 255
    proxy_fqdn: str
    # Maximum length of HTTP request line | Default: 8 | Min: 2 | Max: 64
    max_request_length: int
    # Maximum length of HTTP message, not including body | Default: 32 | Min: 16 | Max: 256
    max_message_length: int
    # HTTP/2 client initial window size in bytes | Default: 1048576 | Min: 65535 | Max: 2147483647
    http2_client_window_size: int
    # HTTP/2 server initial window size in bytes | Default: 1048576 | Min: 65535 | Max: 2147483647
    http2_server_window_size: int
    # Proxy auth query sign timeout in seconds | Default: 120 | Min: 30 | Max: 3600
    auth_sign_timeout: int
    # Enable/disable strict web checking to block web sites that s | Default: disable
    strict_web_check: Literal["enable", "disable"]
    # Enable/disable forwarding proxy authentication headers. | Default: disable
    forward_proxy_auth: Literal["enable", "disable"]
    # Period of time before the source IP's traffic is no longer a | Default: 30 | Min: 6 | Max: 60
    forward_server_affinity_timeout: int
    # Maximum length of HTTP messages processed by Web Application | Default: 1 | Min: 1 | Max: 1024
    max_waf_body_cache_length: int
    # Name of the web proxy profile to apply when explicit proxy t | MaxLen: 63
    webproxy_profile: str
    # Enable/disable learning the client's IP address from headers | Default: disable
    learn_client_ip: Literal["enable", "disable"]
    # Enable/disable learning the client's IP address from headers | Default: disable
    always_learn_client_ip: Literal["enable", "disable"]
    # Learn client IP address from the specified headers.
    learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"]
    # Source address name (srcaddr or srcaddr6 must be set).
    learn_client_ip_srcaddr: list[GlobalLearnclientipsrcaddrObject]
    # IPv6 Source address name (srcaddr or srcaddr6 must be set).
    learn_client_ip_srcaddr6: list[GlobalLearnclientipsrcaddr6Object]
    # IPv4 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr: list[dict[str, Any]]
    # IPv6 source addresses to exempt proxy affinity.
    src_affinity_exempt_addr6: list[dict[str, Any]]
    # Enable/disable policy partial matching. | Default: enable
    policy_partial_match: Literal["enable", "disable"]
    # Enable/disable logging sessions that are pending on policy m | Default: disable
    log_policy_pending: Literal["enable", "disable"]
    # Enable/disable forward server name logging in forward traffi | Default: disable
    log_forward_server: Literal["enable", "disable"]
    # Enable/disable always log application type in traffic log. | Default: disable
    log_app_id: Literal["enable", "disable"]
    # Enable/disable transparent proxy certificate inspection. | Default: disable
    proxy_transparent_cert_inspection: Literal["enable", "disable"]
    # Action when HTTP/1.x request header contains obs-fold | Default: keep
    request_obs_fold: Literal["replace-with-sp", "block", "keep"]
    
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
    def to_dict(self) -> GlobalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Global:
    """
    Configure Web proxy global settings.
    
    Path: web_proxy/global_
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject: ...
    
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
    ) -> GlobalObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> GlobalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: GlobalPayload | None = ...,
        ssl_cert: str | None = ...,
        ssl_ca_cert: str | None = ...,
        fast_policy_match: Literal["enable", "disable"] | None = ...,
        ldap_user_cache: Literal["enable", "disable"] | None = ...,
        proxy_fqdn: str | None = ...,
        max_request_length: int | None = ...,
        max_message_length: int | None = ...,
        http2_client_window_size: int | None = ...,
        http2_server_window_size: int | None = ...,
        auth_sign_timeout: int | None = ...,
        strict_web_check: Literal["enable", "disable"] | None = ...,
        forward_proxy_auth: Literal["enable", "disable"] | None = ...,
        forward_server_affinity_timeout: int | None = ...,
        max_waf_body_cache_length: int | None = ...,
        webproxy_profile: str | None = ...,
        learn_client_ip: Literal["enable", "disable"] | None = ...,
        always_learn_client_ip: Literal["enable", "disable"] | None = ...,
        learn_client_ip_from_header: Literal["true-client-ip", "x-real-ip", "x-forwarded-for"] | list[str] | None = ...,
        learn_client_ip_srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        learn_client_ip_srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        src_affinity_exempt_addr: str | list[str] | None = ...,
        src_affinity_exempt_addr6: str | list[str] | None = ...,
        policy_partial_match: Literal["enable", "disable"] | None = ...,
        log_policy_pending: Literal["enable", "disable"] | None = ...,
        log_forward_server: Literal["enable", "disable"] | None = ...,
        log_app_id: Literal["enable", "disable"] | None = ...,
        proxy_transparent_cert_inspection: Literal["enable", "disable"] | None = ...,
        request_obs_fold: Literal["replace-with-sp", "block", "keep"] | None = ...,
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
    "Global",
    "GlobalPayload",
    "GlobalResponse",
    "GlobalObject",
]
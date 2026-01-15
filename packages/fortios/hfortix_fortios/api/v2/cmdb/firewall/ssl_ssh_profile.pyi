from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SslSshProfilePayload(TypedDict, total=False):
    """
    Type hints for firewall/ssl_ssh_profile payload fields.
    
    Configure SSL/SSH protocol options.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.hsm-local.HsmLocalEndpoint` (via: caname, untrusted-caname)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: caname, untrusted-caname)

    **Usage:**
        payload: SslSshProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 47
    comment: str  # Optional comments. | MaxLen: 255
    ssl: str  # Configure SSL options.
    https: str  # Configure HTTPS options.
    ftps: str  # Configure FTPS options.
    imaps: str  # Configure IMAPS options.
    pop3s: str  # Configure POP3S options.
    smtps: str  # Configure SMTPS options.
    ssh: str  # Configure SSH options.
    dot: str  # Configure DNS over TLS options.
    allowlist: Literal["enable", "disable"]  # Enable/disable exempting servers by FortiGuard all | Default: disable
    block_blocklisted_certificates: Literal["disable", "enable"]  # Enable/disable blocking SSL-based botnet communica | Default: enable
    ssl_exempt: list[dict[str, Any]]  # Servers to exempt from SSL inspection.
    ech_outer_sni: list[dict[str, Any]]  # ClientHelloOuter SNIs to be blocked.
    server_cert_mode: Literal["re-sign", "replace"]  # Re-sign or replace the server's certificate. | Default: re-sign
    use_ssl_server: Literal["disable", "enable"]  # Enable/disable the use of SSL server table for SSL | Default: disable
    caname: str  # CA certificate used by SSL Inspection. | Default: Fortinet_CA_SSL | MaxLen: 35
    untrusted_caname: str  # Untrusted CA certificate used by SSL Inspection. | Default: Fortinet_CA_Untrusted | MaxLen: 35
    server_cert: list[dict[str, Any]]  # Certificate used by SSL Inspection to replace serv
    ssl_server: list[dict[str, Any]]  # SSL server settings used for client certificate re
    ssl_exemption_ip_rating: Literal["enable", "disable"]  # Enable/disable IP based URL rating. | Default: enable
    ssl_exemption_log: Literal["disable", "enable"]  # Enable/disable logging of SSL exemptions. | Default: disable
    ssl_anomaly_log: Literal["disable", "enable"]  # Enable/disable logging of SSL anomalies. | Default: enable
    ssl_negotiation_log: Literal["disable", "enable"]  # Enable/disable logging of SSL negotiation events. | Default: enable
    ssl_server_cert_log: Literal["disable", "enable"]  # Enable/disable logging of server certificate infor | Default: disable
    ssl_handshake_log: Literal["disable", "enable"]  # Enable/disable logging of TLS handshakes. | Default: disable
    rpc_over_https: Literal["enable", "disable"]  # Enable/disable inspection of RPC over HTTPS. | Default: disable
    mapi_over_https: Literal["enable", "disable"]  # Enable/disable inspection of MAPI over HTTPS. | Default: disable
    supported_alpn: Literal["http1-1", "http2", "all", "none"]  # Configure ALPN option. | Default: all

# Nested TypedDicts for table field children (dict mode)

class SslSshProfileSslexemptItem(TypedDict):
    """Type hints for ssl-exempt table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID number. | Default: 0 | Min: 0 | Max: 512
    type: Literal["fortiguard-category", "address", "address6", "wildcard-fqdn", "regex"]  # Type of address object (IPv4 or IPv6) or FortiGuar | Default: fortiguard-category
    fortiguard_category: int  # FortiGuard category ID. | Default: 0 | Min: 0 | Max: 255
    address: str  # IPv4 address object. | MaxLen: 79
    address6: str  # IPv6 address object. | MaxLen: 79
    wildcard_fqdn: str  # Exempt servers by wildcard FQDN. | MaxLen: 79
    regex: str  # Exempt servers by regular expression. | MaxLen: 255


class SslSshProfileEchoutersniItem(TypedDict):
    """Type hints for ech-outer-sni table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # ClientHelloOuter SNI name. | MaxLen: 79
    sni: str  # ClientHelloOuter SNI to be blocked. | MaxLen: 255


class SslSshProfileServercertItem(TypedDict):
    """Type hints for server-cert table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate list. | Default: Fortinet_SSL | MaxLen: 79


class SslSshProfileSslserverItem(TypedDict):
    """Type hints for ssl-server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # SSL server ID. | Default: 0 | Min: 0 | Max: 4294967295
    ip: str  # IPv4 address of the SSL server. | Default: 0.0.0.0
    https_client_certificate: Literal["bypass", "inspect", "block"]  # Action based on received client certificate during | Default: bypass
    smtps_client_certificate: Literal["bypass", "inspect", "block"]  # Action based on received client certificate during | Default: bypass
    pop3s_client_certificate: Literal["bypass", "inspect", "block"]  # Action based on received client certificate during | Default: bypass
    imaps_client_certificate: Literal["bypass", "inspect", "block"]  # Action based on received client certificate during | Default: bypass
    ftps_client_certificate: Literal["bypass", "inspect", "block"]  # Action based on received client certificate during | Default: bypass
    ssl_other_client_certificate: Literal["bypass", "inspect", "block"]  # Action based on received client certificate during | Default: bypass


# Nested classes for table field children (object mode)

@final
class SslSshProfileSslexemptObject:
    """Typed object for ssl-exempt table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID number. | Default: 0 | Min: 0 | Max: 512
    id: int
    # Type of address object (IPv4 or IPv6) or FortiGuard category | Default: fortiguard-category
    type: Literal["fortiguard-category", "address", "address6", "wildcard-fqdn", "regex"]
    # FortiGuard category ID. | Default: 0 | Min: 0 | Max: 255
    fortiguard_category: int
    # IPv4 address object. | MaxLen: 79
    address: str
    # IPv6 address object. | MaxLen: 79
    address6: str
    # Exempt servers by wildcard FQDN. | MaxLen: 79
    wildcard_fqdn: str
    # Exempt servers by regular expression. | MaxLen: 255
    regex: str
    
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
class SslSshProfileEchoutersniObject:
    """Typed object for ech-outer-sni table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ClientHelloOuter SNI name. | MaxLen: 79
    name: str
    # ClientHelloOuter SNI to be blocked. | MaxLen: 255
    sni: str
    
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
class SslSshProfileServercertObject:
    """Typed object for server-cert table items.
    
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


@final
class SslSshProfileSslserverObject:
    """Typed object for ssl-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SSL server ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IPv4 address of the SSL server. | Default: 0.0.0.0
    ip: str
    # Action based on received client certificate during the HTTPS | Default: bypass
    https_client_certificate: Literal["bypass", "inspect", "block"]
    # Action based on received client certificate during the SMTPS | Default: bypass
    smtps_client_certificate: Literal["bypass", "inspect", "block"]
    # Action based on received client certificate during the POP3S | Default: bypass
    pop3s_client_certificate: Literal["bypass", "inspect", "block"]
    # Action based on received client certificate during the IMAPS | Default: bypass
    imaps_client_certificate: Literal["bypass", "inspect", "block"]
    # Action based on received client certificate during the FTPS | Default: bypass
    ftps_client_certificate: Literal["bypass", "inspect", "block"]
    # Action based on received client certificate during an SSL pr | Default: bypass
    ssl_other_client_certificate: Literal["bypass", "inspect", "block"]
    
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
class SslSshProfileResponse(TypedDict):
    """
    Type hints for firewall/ssl_ssh_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 47
    comment: str  # Optional comments. | MaxLen: 255
    ssl: str  # Configure SSL options.
    https: str  # Configure HTTPS options.
    ftps: str  # Configure FTPS options.
    imaps: str  # Configure IMAPS options.
    pop3s: str  # Configure POP3S options.
    smtps: str  # Configure SMTPS options.
    ssh: str  # Configure SSH options.
    dot: str  # Configure DNS over TLS options.
    allowlist: Literal["enable", "disable"]  # Enable/disable exempting servers by FortiGuard all | Default: disable
    block_blocklisted_certificates: Literal["disable", "enable"]  # Enable/disable blocking SSL-based botnet communica | Default: enable
    ssl_exempt: list[SslSshProfileSslexemptItem]  # Servers to exempt from SSL inspection.
    ech_outer_sni: list[SslSshProfileEchoutersniItem]  # ClientHelloOuter SNIs to be blocked.
    server_cert_mode: Literal["re-sign", "replace"]  # Re-sign or replace the server's certificate. | Default: re-sign
    use_ssl_server: Literal["disable", "enable"]  # Enable/disable the use of SSL server table for SSL | Default: disable
    caname: str  # CA certificate used by SSL Inspection. | Default: Fortinet_CA_SSL | MaxLen: 35
    untrusted_caname: str  # Untrusted CA certificate used by SSL Inspection. | Default: Fortinet_CA_Untrusted | MaxLen: 35
    server_cert: list[SslSshProfileServercertItem]  # Certificate used by SSL Inspection to replace serv
    ssl_server: list[SslSshProfileSslserverItem]  # SSL server settings used for client certificate re
    ssl_exemption_ip_rating: Literal["enable", "disable"]  # Enable/disable IP based URL rating. | Default: enable
    ssl_exemption_log: Literal["disable", "enable"]  # Enable/disable logging of SSL exemptions. | Default: disable
    ssl_anomaly_log: Literal["disable", "enable"]  # Enable/disable logging of SSL anomalies. | Default: enable
    ssl_negotiation_log: Literal["disable", "enable"]  # Enable/disable logging of SSL negotiation events. | Default: enable
    ssl_server_cert_log: Literal["disable", "enable"]  # Enable/disable logging of server certificate infor | Default: disable
    ssl_handshake_log: Literal["disable", "enable"]  # Enable/disable logging of TLS handshakes. | Default: disable
    rpc_over_https: Literal["enable", "disable"]  # Enable/disable inspection of RPC over HTTPS. | Default: disable
    mapi_over_https: Literal["enable", "disable"]  # Enable/disable inspection of MAPI over HTTPS. | Default: disable
    supported_alpn: Literal["http1-1", "http2", "all", "none"]  # Configure ALPN option. | Default: all


@final
class SslSshProfileObject:
    """Typed FortiObject for firewall/ssl_ssh_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 47
    name: str
    # Optional comments. | MaxLen: 255
    comment: str
    # Configure SSL options.
    ssl: str
    # Configure HTTPS options.
    https: str
    # Configure FTPS options.
    ftps: str
    # Configure IMAPS options.
    imaps: str
    # Configure POP3S options.
    pop3s: str
    # Configure SMTPS options.
    smtps: str
    # Configure SSH options.
    ssh: str
    # Configure DNS over TLS options.
    dot: str
    # Enable/disable exempting servers by FortiGuard allowlist. | Default: disable
    allowlist: Literal["enable", "disable"]
    # Enable/disable blocking SSL-based botnet communication by Fo | Default: enable
    block_blocklisted_certificates: Literal["disable", "enable"]
    # Servers to exempt from SSL inspection.
    ssl_exempt: list[SslSshProfileSslexemptObject]
    # ClientHelloOuter SNIs to be blocked.
    ech_outer_sni: list[SslSshProfileEchoutersniObject]
    # Re-sign or replace the server's certificate. | Default: re-sign
    server_cert_mode: Literal["re-sign", "replace"]
    # Enable/disable the use of SSL server table for SSL offloadin | Default: disable
    use_ssl_server: Literal["disable", "enable"]
    # CA certificate used by SSL Inspection. | Default: Fortinet_CA_SSL | MaxLen: 35
    caname: str
    # Untrusted CA certificate used by SSL Inspection. | Default: Fortinet_CA_Untrusted | MaxLen: 35
    untrusted_caname: str
    # Certificate used by SSL Inspection to replace server certifi
    server_cert: list[SslSshProfileServercertObject]
    # SSL server settings used for client certificate request.
    ssl_server: list[SslSshProfileSslserverObject]
    # Enable/disable IP based URL rating. | Default: enable
    ssl_exemption_ip_rating: Literal["enable", "disable"]
    # Enable/disable logging of SSL exemptions. | Default: disable
    ssl_exemption_log: Literal["disable", "enable"]
    # Enable/disable logging of SSL anomalies. | Default: enable
    ssl_anomaly_log: Literal["disable", "enable"]
    # Enable/disable logging of SSL negotiation events. | Default: enable
    ssl_negotiation_log: Literal["disable", "enable"]
    # Enable/disable logging of server certificate information. | Default: disable
    ssl_server_cert_log: Literal["disable", "enable"]
    # Enable/disable logging of TLS handshakes. | Default: disable
    ssl_handshake_log: Literal["disable", "enable"]
    # Enable/disable inspection of RPC over HTTPS. | Default: disable
    rpc_over_https: Literal["enable", "disable"]
    # Enable/disable inspection of MAPI over HTTPS. | Default: disable
    mapi_over_https: Literal["enable", "disable"]
    # Configure ALPN option. | Default: all
    supported_alpn: Literal["http1-1", "http2", "all", "none"]
    
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
    def to_dict(self) -> SslSshProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SslSshProfile:
    """
    Configure SSL/SSH protocol options.
    
    Path: firewall/ssl_ssh_profile
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> FortiObjectList[SslSshProfileObject]: ...
    
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> FortiObjectList[SslSshProfileObject]: ...
    
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> SslSshProfileObject: ...
    
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
    ) -> FortiObjectList[SslSshProfileObject]: ...
    
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
    ) -> SslSshProfileObject | list[SslSshProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SslSshProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SslSshProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SslSshProfileObject: ...
    
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
        payload_dict: SslSshProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        ssl: str | None = ...,
        https: str | None = ...,
        ftps: str | None = ...,
        imaps: str | None = ...,
        pop3s: str | None = ...,
        smtps: str | None = ...,
        ssh: str | None = ...,
        dot: str | None = ...,
        allowlist: Literal["enable", "disable"] | None = ...,
        block_blocklisted_certificates: Literal["disable", "enable"] | None = ...,
        ssl_exempt: str | list[str] | list[dict[str, Any]] | None = ...,
        ech_outer_sni: str | list[str] | list[dict[str, Any]] | None = ...,
        server_cert_mode: Literal["re-sign", "replace"] | None = ...,
        use_ssl_server: Literal["disable", "enable"] | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        server_cert: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_server: str | list[str] | list[dict[str, Any]] | None = ...,
        ssl_exemption_ip_rating: Literal["enable", "disable"] | None = ...,
        ssl_exemption_log: Literal["disable", "enable"] | None = ...,
        ssl_anomaly_log: Literal["disable", "enable"] | None = ...,
        ssl_negotiation_log: Literal["disable", "enable"] | None = ...,
        ssl_server_cert_log: Literal["disable", "enable"] | None = ...,
        ssl_handshake_log: Literal["disable", "enable"] | None = ...,
        rpc_over_https: Literal["enable", "disable"] | None = ...,
        mapi_over_https: Literal["enable", "disable"] | None = ...,
        supported_alpn: Literal["http1-1", "http2", "all", "none"] | None = ...,
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
    "SslSshProfile",
    "SslSshProfilePayload",
    "SslSshProfileResponse",
    "SslSshProfileObject",
]
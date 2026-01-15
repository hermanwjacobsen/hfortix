from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for user/setting payload fields.
    
    Configure user authentication setting.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.user.password-policy.PasswordPolicyEndpoint` (via: default-user-password-policy)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: auth-ca-cert, auth-cert)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    auth_type: Literal["http", "https", "ftp", "telnet"]  # Supported firewall policy authentication protocols | Default: http https ftp telnet
    auth_cert: str  # HTTPS server certificate for policy authentication | MaxLen: 35
    auth_ca_cert: str  # HTTPS CA certificate for policy authentication. | MaxLen: 35
    auth_secure_http: Literal["enable", "disable"]  # Enable/disable redirecting HTTP user authenticatio | Default: disable
    auth_http_basic: Literal["enable", "disable"]  # Enable/disable use of HTTP basic authentication fo | Default: disable
    auth_ssl_allow_renegotiation: Literal["enable", "disable"]  # Allow/forbid SSL re-negotiation for HTTPS authenti | Default: disable
    auth_src_mac: Literal["enable", "disable"]  # Enable/disable source MAC for user identity. | Default: enable
    auth_on_demand: Literal["always", "implicitly"]  # Always/implicitly trigger firewall authentication | Default: implicitly
    auth_timeout: int  # Time in minutes before the firewall user authentic | Default: 5 | Min: 1 | Max: 1440
    auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"]  # Control if authenticated users have to login again | Default: idle-timeout
    auth_portal_timeout: int  # Time in minutes before captive portal user have to | Default: 3 | Min: 1 | Max: 30
    radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"]  # Set the RADIUS session timeout to a hard timeout o | Default: hard-timeout
    auth_blackout_time: int  # Time in seconds an IP address is denied access aft | Default: 0 | Min: 0 | Max: 3600
    auth_invalid_max: int  # Maximum number of failed authentication attempts b | Default: 5 | Min: 1 | Max: 100
    auth_lockout_threshold: int  # Maximum number of failed login attempts before log | Default: 3 | Min: 1 | Max: 10
    auth_lockout_duration: int  # Lockout period in seconds after too many login fai | Default: 0 | Min: 0 | Max: 4294967295
    per_policy_disclaimer: Literal["enable", "disable"]  # Enable/disable per policy disclaimer. | Default: disable
    auth_ports: list[dict[str, Any]]  # Set up non-standard ports for authentication with
    auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"]  # Maximum supported protocol version for SSL/TLS con
    auth_ssl_sigalgs: Literal["no-rsa-pss", "all"]  # Set signature algorithms related to HTTPS authenti | Default: all
    default_user_password_policy: str  # Default password policy to apply to all local user | MaxLen: 35
    cors: Literal["disable", "enable"]  # Enable/disable allowed origins white list for CORS | Default: disable
    cors_allowed_origins: list[dict[str, Any]]  # Allowed origins white list for CORS.

# Nested TypedDicts for table field children (dict mode)

class SettingAuthportsItem(TypedDict):
    """Type hints for auth-ports table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    type: Literal["http", "https", "ftp", "telnet"]  # Service type. | Default: http
    port: int  # Non-standard port for firewall user authentication | Default: 1024 | Min: 1 | Max: 65535


class SettingCorsallowedoriginsItem(TypedDict):
    """Type hints for cors-allowed-origins table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Allowed origin for CORS. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class SettingAuthportsObject:
    """Typed object for auth-ports table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Service type. | Default: http
    type: Literal["http", "https", "ftp", "telnet"]
    # Non-standard port for firewall user authentication. | Default: 1024 | Min: 1 | Max: 65535
    port: int
    
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
class SettingCorsallowedoriginsObject:
    """Typed object for cors-allowed-origins table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Allowed origin for CORS. | MaxLen: 79
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
class SettingResponse(TypedDict):
    """
    Type hints for user/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    auth_type: Literal["http", "https", "ftp", "telnet"]  # Supported firewall policy authentication protocols | Default: http https ftp telnet
    auth_cert: str  # HTTPS server certificate for policy authentication | MaxLen: 35
    auth_ca_cert: str  # HTTPS CA certificate for policy authentication. | MaxLen: 35
    auth_secure_http: Literal["enable", "disable"]  # Enable/disable redirecting HTTP user authenticatio | Default: disable
    auth_http_basic: Literal["enable", "disable"]  # Enable/disable use of HTTP basic authentication fo | Default: disable
    auth_ssl_allow_renegotiation: Literal["enable", "disable"]  # Allow/forbid SSL re-negotiation for HTTPS authenti | Default: disable
    auth_src_mac: Literal["enable", "disable"]  # Enable/disable source MAC for user identity. | Default: enable
    auth_on_demand: Literal["always", "implicitly"]  # Always/implicitly trigger firewall authentication | Default: implicitly
    auth_timeout: int  # Time in minutes before the firewall user authentic | Default: 5 | Min: 1 | Max: 1440
    auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"]  # Control if authenticated users have to login again | Default: idle-timeout
    auth_portal_timeout: int  # Time in minutes before captive portal user have to | Default: 3 | Min: 1 | Max: 30
    radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"]  # Set the RADIUS session timeout to a hard timeout o | Default: hard-timeout
    auth_blackout_time: int  # Time in seconds an IP address is denied access aft | Default: 0 | Min: 0 | Max: 3600
    auth_invalid_max: int  # Maximum number of failed authentication attempts b | Default: 5 | Min: 1 | Max: 100
    auth_lockout_threshold: int  # Maximum number of failed login attempts before log | Default: 3 | Min: 1 | Max: 10
    auth_lockout_duration: int  # Lockout period in seconds after too many login fai | Default: 0 | Min: 0 | Max: 4294967295
    per_policy_disclaimer: Literal["enable", "disable"]  # Enable/disable per policy disclaimer. | Default: disable
    auth_ports: list[SettingAuthportsItem]  # Set up non-standard ports for authentication with
    auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"]  # Maximum supported protocol version for SSL/TLS con
    auth_ssl_sigalgs: Literal["no-rsa-pss", "all"]  # Set signature algorithms related to HTTPS authenti | Default: all
    default_user_password_policy: str  # Default password policy to apply to all local user | MaxLen: 35
    cors: Literal["disable", "enable"]  # Enable/disable allowed origins white list for CORS | Default: disable
    cors_allowed_origins: list[SettingCorsallowedoriginsItem]  # Allowed origins white list for CORS.


@final
class SettingObject:
    """Typed FortiObject for user/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Supported firewall policy authentication protocols/methods. | Default: http https ftp telnet
    auth_type: Literal["http", "https", "ftp", "telnet"]
    # HTTPS server certificate for policy authentication. | MaxLen: 35
    auth_cert: str
    # HTTPS CA certificate for policy authentication. | MaxLen: 35
    auth_ca_cert: str
    # Enable/disable redirecting HTTP user authentication to more | Default: disable
    auth_secure_http: Literal["enable", "disable"]
    # Enable/disable use of HTTP basic authentication for identity | Default: disable
    auth_http_basic: Literal["enable", "disable"]
    # Allow/forbid SSL re-negotiation for HTTPS authentication. | Default: disable
    auth_ssl_allow_renegotiation: Literal["enable", "disable"]
    # Enable/disable source MAC for user identity. | Default: enable
    auth_src_mac: Literal["enable", "disable"]
    # Always/implicitly trigger firewall authentication on demand. | Default: implicitly
    auth_on_demand: Literal["always", "implicitly"]
    # Time in minutes before the firewall user authentication time | Default: 5 | Min: 1 | Max: 1440
    auth_timeout: int
    # Control if authenticated users have to login again after a h | Default: idle-timeout
    auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"]
    # Time in minutes before captive portal user have to re-authen | Default: 3 | Min: 1 | Max: 30
    auth_portal_timeout: int
    # Set the RADIUS session timeout to a hard timeout or to ignor | Default: hard-timeout
    radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"]
    # Time in seconds an IP address is denied access after failing | Default: 0 | Min: 0 | Max: 3600
    auth_blackout_time: int
    # Maximum number of failed authentication attempts before the | Default: 5 | Min: 1 | Max: 100
    auth_invalid_max: int
    # Maximum number of failed login attempts before login lockout | Default: 3 | Min: 1 | Max: 10
    auth_lockout_threshold: int
    # Lockout period in seconds after too many login failures. | Default: 0 | Min: 0 | Max: 4294967295
    auth_lockout_duration: int
    # Enable/disable per policy disclaimer. | Default: disable
    per_policy_disclaimer: Literal["enable", "disable"]
    # Set up non-standard ports for authentication with HTTP, HTTP
    auth_ports: list[SettingAuthportsObject]
    # Minimum supported protocol version for SSL/TLS connections | Default: default
    auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Maximum supported protocol version for SSL/TLS connections
    auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"]
    # Set signature algorithms related to HTTPS authentication | Default: all
    auth_ssl_sigalgs: Literal["no-rsa-pss", "all"]
    # Default password policy to apply to all local users unless o | MaxLen: 35
    default_user_password_policy: str
    # Enable/disable allowed origins white list for CORS. | Default: disable
    cors: Literal["disable", "enable"]
    # Allowed origins white list for CORS.
    cors_allowed_origins: list[SettingCorsallowedoriginsObject]
    
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
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Setting:
    """
    Configure user authentication setting.
    
    Path: user/setting
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingPayload | None = ...,
        auth_type: Literal["http", "https", "ftp", "telnet"] | list[str] | None = ...,
        auth_cert: str | None = ...,
        auth_ca_cert: str | None = ...,
        auth_secure_http: Literal["enable", "disable"] | None = ...,
        auth_http_basic: Literal["enable", "disable"] | None = ...,
        auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = ...,
        auth_src_mac: Literal["enable", "disable"] | None = ...,
        auth_on_demand: Literal["always", "implicitly"] | None = ...,
        auth_timeout: int | None = ...,
        auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = ...,
        auth_portal_timeout: int | None = ...,
        radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = ...,
        auth_blackout_time: int | None = ...,
        auth_invalid_max: int | None = ...,
        auth_lockout_threshold: int | None = ...,
        auth_lockout_duration: int | None = ...,
        per_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        auth_ports: str | list[str] | list[dict[str, Any]] | None = ...,
        auth_ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        auth_ssl_max_proto_version: Literal["sslv3", "tlsv1", "tlsv1-1", "tlsv1-2", "tlsv1-3"] | None = ...,
        auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = ...,
        default_user_password_policy: str | None = ...,
        cors: Literal["disable", "enable"] | None = ...,
        cors_allowed_origins: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingResponse",
    "SettingObject",
]
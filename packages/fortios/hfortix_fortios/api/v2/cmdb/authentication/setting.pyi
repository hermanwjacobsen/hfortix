from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for authentication/setting payload fields.
    
    Configure authentication setting.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.authentication.scheme.SchemeEndpoint` (via: active-auth-scheme, sso-auth-scheme)
        - :class:`~.firewall.address.AddressEndpoint` (via: captive-portal, cert-captive-portal)
        - :class:`~.firewall.address6.Address6Endpoint` (via: captive-portal6)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    active_auth_scheme: str  # Active authentication method (scheme name). | MaxLen: 35
    sso_auth_scheme: str  # Single-Sign-On authentication method (scheme name) | MaxLen: 35
    update_time: str  # Time of the last update.
    persistent_cookie: Literal["enable", "disable"]  # Enable/disable persistent cookie on web portal aut | Default: enable
    ip_auth_cookie: Literal["enable", "disable"]  # Enable/disable persistent cookie on IP based web p | Default: disable
    cookie_max_age: int  # Persistent web portal cookie maximum age in minute | Default: 480 | Min: 30 | Max: 10080
    cookie_refresh_div: int  # Refresh rate divider of persistent web portal cook | Default: 2 | Min: 2 | Max: 4
    captive_portal_type: Literal["fqdn", "ip"]  # Captive portal type. | Default: fqdn
    captive_portal_ip: str  # Captive portal IP address. | Default: 0.0.0.0
    captive_portal_ip6: str  # Captive portal IPv6 address. | Default: ::
    captive_portal: str  # Captive portal host name. | MaxLen: 255
    captive_portal6: str  # IPv6 captive portal host name. | MaxLen: 255
    cert_auth: Literal["enable", "disable"]  # Enable/disable redirecting certificate authenticat | Default: disable
    cert_captive_portal: str  # Certificate captive portal host name. | MaxLen: 255
    cert_captive_portal_ip: str  # Certificate captive portal IP address. | Default: 0.0.0.0
    cert_captive_portal_port: int  # Certificate captive portal port number | Default: 7832 | Min: 1 | Max: 65535
    captive_portal_port: int  # Captive portal port number | Default: 7830 | Min: 1 | Max: 65535
    auth_https: Literal["enable", "disable"]  # Enable/disable redirecting HTTP user authenticatio | Default: enable
    captive_portal_ssl_port: int  # Captive portal SSL port number | Default: 7831 | Min: 1 | Max: 65535
    user_cert_ca: list[dict[str, Any]]  # CA certificate used for client certificate verific
    dev_range: list[dict[str, Any]]  # Address range for the IP based device query.

# Nested TypedDicts for table field children (dict mode)

class SettingUsercertcaItem(TypedDict):
    """Type hints for user-cert-ca table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # CA certificate list. | MaxLen: 79


class SettingDevrangeItem(TypedDict):
    """Type hints for dev-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class SettingUsercertcaObject:
    """Typed object for user-cert-ca table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # CA certificate list. | MaxLen: 79
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
class SettingDevrangeObject:
    """Typed object for dev-range table items.
    
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
class SettingResponse(TypedDict):
    """
    Type hints for authentication/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    active_auth_scheme: str  # Active authentication method (scheme name). | MaxLen: 35
    sso_auth_scheme: str  # Single-Sign-On authentication method (scheme name) | MaxLen: 35
    update_time: str  # Time of the last update.
    persistent_cookie: Literal["enable", "disable"]  # Enable/disable persistent cookie on web portal aut | Default: enable
    ip_auth_cookie: Literal["enable", "disable"]  # Enable/disable persistent cookie on IP based web p | Default: disable
    cookie_max_age: int  # Persistent web portal cookie maximum age in minute | Default: 480 | Min: 30 | Max: 10080
    cookie_refresh_div: int  # Refresh rate divider of persistent web portal cook | Default: 2 | Min: 2 | Max: 4
    captive_portal_type: Literal["fqdn", "ip"]  # Captive portal type. | Default: fqdn
    captive_portal_ip: str  # Captive portal IP address. | Default: 0.0.0.0
    captive_portal_ip6: str  # Captive portal IPv6 address. | Default: ::
    captive_portal: str  # Captive portal host name. | MaxLen: 255
    captive_portal6: str  # IPv6 captive portal host name. | MaxLen: 255
    cert_auth: Literal["enable", "disable"]  # Enable/disable redirecting certificate authenticat | Default: disable
    cert_captive_portal: str  # Certificate captive portal host name. | MaxLen: 255
    cert_captive_portal_ip: str  # Certificate captive portal IP address. | Default: 0.0.0.0
    cert_captive_portal_port: int  # Certificate captive portal port number | Default: 7832 | Min: 1 | Max: 65535
    captive_portal_port: int  # Captive portal port number | Default: 7830 | Min: 1 | Max: 65535
    auth_https: Literal["enable", "disable"]  # Enable/disable redirecting HTTP user authenticatio | Default: enable
    captive_portal_ssl_port: int  # Captive portal SSL port number | Default: 7831 | Min: 1 | Max: 65535
    user_cert_ca: list[SettingUsercertcaItem]  # CA certificate used for client certificate verific
    dev_range: list[SettingDevrangeItem]  # Address range for the IP based device query.


@final
class SettingObject:
    """Typed FortiObject for authentication/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Active authentication method (scheme name). | MaxLen: 35
    active_auth_scheme: str
    # Single-Sign-On authentication method (scheme name). | MaxLen: 35
    sso_auth_scheme: str
    # Time of the last update.
    update_time: str
    # Enable/disable persistent cookie on web portal authenticatio | Default: enable
    persistent_cookie: Literal["enable", "disable"]
    # Enable/disable persistent cookie on IP based web portal auth | Default: disable
    ip_auth_cookie: Literal["enable", "disable"]
    # Persistent web portal cookie maximum age in minutes | Default: 480 | Min: 30 | Max: 10080
    cookie_max_age: int
    # Refresh rate divider of persistent web portal cookie | Default: 2 | Min: 2 | Max: 4
    cookie_refresh_div: int
    # Captive portal type. | Default: fqdn
    captive_portal_type: Literal["fqdn", "ip"]
    # Captive portal IP address. | Default: 0.0.0.0
    captive_portal_ip: str
    # Captive portal IPv6 address. | Default: ::
    captive_portal_ip6: str
    # Captive portal host name. | MaxLen: 255
    captive_portal: str
    # IPv6 captive portal host name. | MaxLen: 255
    captive_portal6: str
    # Enable/disable redirecting certificate authentication to HTT | Default: disable
    cert_auth: Literal["enable", "disable"]
    # Certificate captive portal host name. | MaxLen: 255
    cert_captive_portal: str
    # Certificate captive portal IP address. | Default: 0.0.0.0
    cert_captive_portal_ip: str
    # Certificate captive portal port number | Default: 7832 | Min: 1 | Max: 65535
    cert_captive_portal_port: int
    # Captive portal port number (1 - 65535, default = 7830). | Default: 7830 | Min: 1 | Max: 65535
    captive_portal_port: int
    # Enable/disable redirecting HTTP user authentication to HTTPS | Default: enable
    auth_https: Literal["enable", "disable"]
    # Captive portal SSL port number (1 - 65535, default = 7831). | Default: 7831 | Min: 1 | Max: 65535
    captive_portal_ssl_port: int
    # CA certificate used for client certificate verification.
    user_cert_ca: list[SettingUsercertcaObject]
    # Address range for the IP based device query.
    dev_range: list[SettingDevrangeObject]
    
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
    Configure authentication setting.
    
    Path: authentication/setting
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
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
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
        active_auth_scheme: str | None = ...,
        sso_auth_scheme: str | None = ...,
        update_time: str | None = ...,
        persistent_cookie: Literal["enable", "disable"] | None = ...,
        ip_auth_cookie: Literal["enable", "disable"] | None = ...,
        cookie_max_age: int | None = ...,
        cookie_refresh_div: int | None = ...,
        captive_portal_type: Literal["fqdn", "ip"] | None = ...,
        captive_portal_ip: str | None = ...,
        captive_portal_ip6: str | None = ...,
        captive_portal: str | None = ...,
        captive_portal6: str | None = ...,
        cert_auth: Literal["enable", "disable"] | None = ...,
        cert_captive_portal: str | None = ...,
        cert_captive_portal_ip: str | None = ...,
        cert_captive_portal_port: int | None = ...,
        captive_portal_port: int | None = ...,
        auth_https: Literal["enable", "disable"] | None = ...,
        captive_portal_ssl_port: int | None = ...,
        user_cert_ca: str | list[str] | list[dict[str, Any]] | None = ...,
        dev_range: str | list[str] | list[dict[str, Any]] | None = ...,
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
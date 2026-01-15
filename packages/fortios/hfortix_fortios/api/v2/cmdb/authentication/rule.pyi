from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class RulePayload(TypedDict, total=False):
    """
    Type hints for authentication/rule payload fields.
    
    Configure Authentication Rules.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.authentication.scheme.SchemeEndpoint` (via: active-auth-method, sso-auth-method)

    **Usage:**
        payload: RulePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Authentication rule name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this authentication rule. | Default: enable
    protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"]  # Authentication is required for the selected protoc | Default: http
    srcintf: list[dict[str, Any]]  # Incoming (ingress) interface.
    srcaddr: list[dict[str, Any]]  # Authentication is required for the selected IPv4 s
    dstaddr: list[dict[str, Any]]  # Select an IPv4 destination address from available
    srcaddr6: list[dict[str, Any]]  # Authentication is required for the selected IPv6 s
    dstaddr6: list[dict[str, Any]]  # Select an IPv6 destination address from available
    ip_based: Literal["enable", "disable"]  # Enable/disable IP-based authentication. When enabl | Default: enable
    active_auth_method: str  # Select an active authentication method. | MaxLen: 35
    sso_auth_method: str  # Select a single-sign on (SSO) authentication metho | MaxLen: 35
    web_auth_cookie: Literal["enable", "disable"]  # Enable/disable Web authentication cookies | Default: disable
    cors_stateful: Literal["enable", "disable"]  # Enable/disable allowance of CORS access | Default: disable
    cors_depth: int  # Depth to allow CORS access (default = 3). | Default: 3 | Min: 1 | Max: 8
    cert_auth_cookie: Literal["enable", "disable"]  # Enable/disable to use device certificate as authen | Default: enable
    transaction_based: Literal["enable", "disable"]  # Enable/disable transaction based authentication | Default: disable
    web_portal: Literal["enable", "disable"]  # Enable/disable web portal for proxy transparent po | Default: enable
    comments: str  # Comment. | MaxLen: 1023
    session_logout: Literal["enable", "disable"]  # Enable/disable logout of a user from the current s | Default: disable

# Nested TypedDicts for table field children (dict mode)

class RuleSrcintfItem(TypedDict):
    """Type hints for srcintf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 79


class RuleSrcaddrItem(TypedDict):
    """Type hints for srcaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class RuleDstaddrItem(TypedDict):
    """Type hints for dstaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class RuleSrcaddr6Item(TypedDict):
    """Type hints for srcaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


class RuleDstaddr6Item(TypedDict):
    """Type hints for dstaddr6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class RuleSrcintfObject:
    """Typed object for srcintf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 79
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
class RuleSrcaddrObject:
    """Typed object for srcaddr table items.
    
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
class RuleDstaddrObject:
    """Typed object for dstaddr table items.
    
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
class RuleSrcaddr6Object:
    """Typed object for srcaddr6 table items.
    
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
class RuleDstaddr6Object:
    """Typed object for dstaddr6 table items.
    
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
class RuleResponse(TypedDict):
    """
    Type hints for authentication/rule API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Authentication rule name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this authentication rule. | Default: enable
    protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"]  # Authentication is required for the selected protoc | Default: http
    srcintf: list[RuleSrcintfItem]  # Incoming (ingress) interface.
    srcaddr: list[RuleSrcaddrItem]  # Authentication is required for the selected IPv4 s
    dstaddr: list[RuleDstaddrItem]  # Select an IPv4 destination address from available
    srcaddr6: list[RuleSrcaddr6Item]  # Authentication is required for the selected IPv6 s
    dstaddr6: list[RuleDstaddr6Item]  # Select an IPv6 destination address from available
    ip_based: Literal["enable", "disable"]  # Enable/disable IP-based authentication. When enabl | Default: enable
    active_auth_method: str  # Select an active authentication method. | MaxLen: 35
    sso_auth_method: str  # Select a single-sign on (SSO) authentication metho | MaxLen: 35
    web_auth_cookie: Literal["enable", "disable"]  # Enable/disable Web authentication cookies | Default: disable
    cors_stateful: Literal["enable", "disable"]  # Enable/disable allowance of CORS access | Default: disable
    cors_depth: int  # Depth to allow CORS access (default = 3). | Default: 3 | Min: 1 | Max: 8
    cert_auth_cookie: Literal["enable", "disable"]  # Enable/disable to use device certificate as authen | Default: enable
    transaction_based: Literal["enable", "disable"]  # Enable/disable transaction based authentication | Default: disable
    web_portal: Literal["enable", "disable"]  # Enable/disable web portal for proxy transparent po | Default: enable
    comments: str  # Comment. | MaxLen: 1023
    session_logout: Literal["enable", "disable"]  # Enable/disable logout of a user from the current s | Default: disable


@final
class RuleObject:
    """Typed FortiObject for authentication/rule with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Authentication rule name. | MaxLen: 35
    name: str
    # Enable/disable this authentication rule. | Default: enable
    status: Literal["enable", "disable"]
    # Authentication is required for the selected protocol | Default: http
    protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"]
    # Incoming (ingress) interface.
    srcintf: list[RuleSrcintfObject]
    # Authentication is required for the selected IPv4 source addr
    srcaddr: list[RuleSrcaddrObject]
    # Select an IPv4 destination address from available options. R
    dstaddr: list[RuleDstaddrObject]
    # Authentication is required for the selected IPv6 source addr
    srcaddr6: list[RuleSrcaddr6Object]
    # Select an IPv6 destination address from available options. R
    dstaddr6: list[RuleDstaddr6Object]
    # Enable/disable IP-based authentication. When enabled, previo | Default: enable
    ip_based: Literal["enable", "disable"]
    # Select an active authentication method. | MaxLen: 35
    active_auth_method: str
    # Select a single-sign on (SSO) authentication method. | MaxLen: 35
    sso_auth_method: str
    # Enable/disable Web authentication cookies | Default: disable
    web_auth_cookie: Literal["enable", "disable"]
    # Enable/disable allowance of CORS access (default = disable). | Default: disable
    cors_stateful: Literal["enable", "disable"]
    # Depth to allow CORS access (default = 3). | Default: 3 | Min: 1 | Max: 8
    cors_depth: int
    # Enable/disable to use device certificate as authentication c | Default: enable
    cert_auth_cookie: Literal["enable", "disable"]
    # Enable/disable transaction based authentication | Default: disable
    transaction_based: Literal["enable", "disable"]
    # Enable/disable web portal for proxy transparent policy | Default: enable
    web_portal: Literal["enable", "disable"]
    # Comment. | MaxLen: 1023
    comments: str
    # Enable/disable logout of a user from the current session. | Default: disable
    session_logout: Literal["enable", "disable"]
    
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
    def to_dict(self) -> RulePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Rule:
    """
    Configure Authentication Rules.
    
    Path: authentication/rule
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
    ) -> RuleObject: ...
    
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
    ) -> RuleObject: ...
    
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
    ) -> FortiObjectList[RuleObject]: ...
    
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
    ) -> RuleObject: ...
    
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
    ) -> RuleObject: ...
    
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
    ) -> FortiObjectList[RuleObject]: ...
    
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
    ) -> RuleObject: ...
    
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
    ) -> RuleObject: ...
    
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
    ) -> FortiObjectList[RuleObject]: ...
    
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
    ) -> RuleObject | list[RuleObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RuleObject: ...
    
    @overload
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> RuleObject: ...
    
    @overload
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> RuleObject: ...
    
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
        payload_dict: RulePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        protocol: Literal["http", "ftp", "socks", "ssh", "ztna-portal"] | None = ...,
        srcintf: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_based: Literal["enable", "disable"] | None = ...,
        active_auth_method: str | None = ...,
        sso_auth_method: str | None = ...,
        web_auth_cookie: Literal["enable", "disable"] | None = ...,
        cors_stateful: Literal["enable", "disable"] | None = ...,
        cors_depth: int | None = ...,
        cert_auth_cookie: Literal["enable", "disable"] | None = ...,
        transaction_based: Literal["enable", "disable"] | None = ...,
        web_portal: Literal["enable", "disable"] | None = ...,
        comments: str | None = ...,
        session_logout: Literal["enable", "disable"] | None = ...,
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
    "Rule",
    "RulePayload",
    "RuleResponse",
    "RuleObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ProxyAddressPayload(TypedDict, total=False):
    """
    Type hints for firewall/proxy_address payload fields.
    
    Configure web proxy address.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: host)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: host)
        - :class:`~.firewall.proxy-address.ProxyAddressEndpoint` (via: host)
        - :class:`~.firewall.vip.VipEndpoint` (via: host)
        - :class:`~.firewall.vipgrp.VipgrpEndpoint` (via: host)

    **Usage:**
        payload: ProxyAddressPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Address name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"]  # Proxy address type. | Default: url
    host: str  # Address object for the host. | MaxLen: 79
    host_regex: str  # Host name as a regular expression. | MaxLen: 255
    path: str  # URL path as a regular expression. | MaxLen: 255
    query: str  # Match the query part of the URL as a regular expre | MaxLen: 255
    referrer: Literal["enable", "disable"]  # Enable/disable use of referrer field in the HTTP h | Default: disable
    category: list[dict[str, Any]]  # FortiGuard category ID.
    method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"]  # HTTP request methods to be used.
    ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"]  # Names of browsers to be used as user agent.
    ua_min_ver: str  # Minimum version of the user agent specified in dot | MaxLen: 63
    ua_max_ver: str  # Maximum version of the user agent specified in dot | MaxLen: 63
    header_name: str  # Name of HTTP header. | MaxLen: 79
    header: str  # HTTP header name as a regular expression. | MaxLen: 255
    case_sensitivity: Literal["disable", "enable"]  # Enable to make the pattern case sensitive. | Default: disable
    header_group: list[dict[str, Any]]  # HTTP header group.
    color: int  # Integer value to determine the color of the icon i | Default: 0 | Min: 0 | Max: 32
    tagging: list[dict[str, Any]]  # Config object tagging.
    comment: str  # Optional comments. | MaxLen: 255
    application: list[dict[str, Any]]  # SaaS application.

# Nested TypedDicts for table field children (dict mode)

class ProxyAddressCategoryItem(TypedDict):
    """Type hints for category table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # FortiGuard category ID. | Default: 0 | Min: 0 | Max: 4294967295


class ProxyAddressHeadergroupItem(TypedDict):
    """Type hints for header-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    header_name: str  # HTTP header. | MaxLen: 79
    header: str  # HTTP header regular expression. | MaxLen: 255
    case_sensitivity: Literal["disable", "enable"]  # Case sensitivity in pattern. | Default: disable


class ProxyAddressTaggingItem(TypedDict):
    """Type hints for tagging table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Tagging entry name. | MaxLen: 63
    category: str  # Tag category. | MaxLen: 63
    tags: str  # Tags.


class ProxyAddressApplicationItem(TypedDict):
    """Type hints for application table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # SaaS application name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class ProxyAddressCategoryObject:
    """Typed object for category table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FortiGuard category ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    
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
class ProxyAddressHeadergroupObject:
    """Typed object for header-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # HTTP header. | MaxLen: 79
    header_name: str
    # HTTP header regular expression. | MaxLen: 255
    header: str
    # Case sensitivity in pattern. | Default: disable
    case_sensitivity: Literal["disable", "enable"]
    
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
class ProxyAddressTaggingObject:
    """Typed object for tagging table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Tagging entry name. | MaxLen: 63
    name: str
    # Tag category. | MaxLen: 63
    category: str
    # Tags.
    tags: str
    
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
class ProxyAddressApplicationObject:
    """Typed object for application table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SaaS application name. | MaxLen: 79
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
class ProxyAddressResponse(TypedDict):
    """
    Type hints for firewall/proxy_address API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Address name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"]  # Proxy address type. | Default: url
    host: str  # Address object for the host. | MaxLen: 79
    host_regex: str  # Host name as a regular expression. | MaxLen: 255
    path: str  # URL path as a regular expression. | MaxLen: 255
    query: str  # Match the query part of the URL as a regular expre | MaxLen: 255
    referrer: Literal["enable", "disable"]  # Enable/disable use of referrer field in the HTTP h | Default: disable
    category: list[ProxyAddressCategoryItem]  # FortiGuard category ID.
    method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"]  # HTTP request methods to be used.
    ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"]  # Names of browsers to be used as user agent.
    ua_min_ver: str  # Minimum version of the user agent specified in dot | MaxLen: 63
    ua_max_ver: str  # Maximum version of the user agent specified in dot | MaxLen: 63
    header_name: str  # Name of HTTP header. | MaxLen: 79
    header: str  # HTTP header name as a regular expression. | MaxLen: 255
    case_sensitivity: Literal["disable", "enable"]  # Enable to make the pattern case sensitive. | Default: disable
    header_group: list[ProxyAddressHeadergroupItem]  # HTTP header group.
    color: int  # Integer value to determine the color of the icon i | Default: 0 | Min: 0 | Max: 32
    tagging: list[ProxyAddressTaggingItem]  # Config object tagging.
    comment: str  # Optional comments. | MaxLen: 255
    application: list[ProxyAddressApplicationItem]  # SaaS application.


@final
class ProxyAddressObject:
    """Typed FortiObject for firewall/proxy_address with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Proxy address type. | Default: url
    type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"]
    # Address object for the host. | MaxLen: 79
    host: str
    # Host name as a regular expression. | MaxLen: 255
    host_regex: str
    # URL path as a regular expression. | MaxLen: 255
    path: str
    # Match the query part of the URL as a regular expression. | MaxLen: 255
    query: str
    # Enable/disable use of referrer field in the HTTP header to m | Default: disable
    referrer: Literal["enable", "disable"]
    # FortiGuard category ID.
    category: list[ProxyAddressCategoryObject]
    # HTTP request methods to be used.
    method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"]
    # Names of browsers to be used as user agent.
    ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"]
    # Minimum version of the user agent specified in dotted notati | MaxLen: 63
    ua_min_ver: str
    # Maximum version of the user agent specified in dotted notati | MaxLen: 63
    ua_max_ver: str
    # Name of HTTP header. | MaxLen: 79
    header_name: str
    # HTTP header name as a regular expression. | MaxLen: 255
    header: str
    # Enable to make the pattern case sensitive. | Default: disable
    case_sensitivity: Literal["disable", "enable"]
    # HTTP header group.
    header_group: list[ProxyAddressHeadergroupObject]
    # Integer value to determine the color of the icon in the GUI | Default: 0 | Min: 0 | Max: 32
    color: int
    # Config object tagging.
    tagging: list[ProxyAddressTaggingObject]
    # Optional comments. | MaxLen: 255
    comment: str
    # SaaS application.
    application: list[ProxyAddressApplicationObject]
    
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
    def to_dict(self) -> ProxyAddressPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ProxyAddress:
    """
    Configure web proxy address.
    
    Path: firewall/proxy_address
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
    ) -> ProxyAddressObject: ...
    
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
    ) -> ProxyAddressObject: ...
    
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
    ) -> FortiObjectList[ProxyAddressObject]: ...
    
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
    ) -> ProxyAddressObject: ...
    
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
    ) -> ProxyAddressObject: ...
    
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
    ) -> FortiObjectList[ProxyAddressObject]: ...
    
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
    ) -> ProxyAddressObject: ...
    
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
    ) -> ProxyAddressObject: ...
    
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
    ) -> FortiObjectList[ProxyAddressObject]: ...
    
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
    ) -> ProxyAddressObject | list[ProxyAddressObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProxyAddressObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProxyAddressObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProxyAddressObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProxyAddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["host-regex", "url", "category", "method", "ua", "header", "src-advanced", "dst-advanced", "saas"] | None = ...,
        host: str | None = ...,
        host_regex: str | None = ...,
        path: str | None = ...,
        query: str | None = ...,
        referrer: Literal["enable", "disable"] | None = ...,
        category: str | list[str] | list[dict[str, Any]] | None = ...,
        method: Literal["get", "post", "put", "head", "connect", "trace", "options", "delete", "update", "patch", "other"] | list[str] | None = ...,
        ua: Literal["chrome", "ms", "firefox", "safari", "ie", "edge", "other"] | list[str] | None = ...,
        ua_min_ver: str | None = ...,
        ua_max_ver: str | None = ...,
        header_name: str | None = ...,
        header: str | None = ...,
        case_sensitivity: Literal["disable", "enable"] | None = ...,
        header_group: str | list[str] | list[dict[str, Any]] | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ProxyAddress",
    "ProxyAddressPayload",
    "ProxyAddressResponse",
    "ProxyAddressObject",
]
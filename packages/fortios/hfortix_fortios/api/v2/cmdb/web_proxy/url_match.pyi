from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class UrlMatchPayload(TypedDict, total=False):
    """
    Type hints for web_proxy/url_match payload fields.
    
    Exempt URLs from web proxy forwarding, caching and fast-fallback.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.web-proxy.fast-fallback.FastFallbackEndpoint` (via: fast-fallback)
        - :class:`~.web-proxy.forward-server.ForwardServerEndpoint` (via: forward-server)
        - :class:`~.web-proxy.forward-server-group.ForwardServerGroupEndpoint` (via: forward-server)

    **Usage:**
        payload: UrlMatchPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Configure a name for the URL to be exempted. | MaxLen: 63
    status: Literal["enable", "disable"]  # Enable/disable exempting the URLs matching the URL | Default: enable
    url_pattern: str  # URL pattern to be exempted from web proxy forwardi | MaxLen: 511
    forward_server: str  # Forward server name. | MaxLen: 63
    fast_fallback: str  # Fast fallback configuration entry name. | MaxLen: 63
    cache_exemption: Literal["enable", "disable"]  # Enable/disable exempting this URL pattern from cac | Default: disable
    comment: str  # Comment. | MaxLen: 255

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class UrlMatchResponse(TypedDict):
    """
    Type hints for web_proxy/url_match API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Configure a name for the URL to be exempted. | MaxLen: 63
    status: Literal["enable", "disable"]  # Enable/disable exempting the URLs matching the URL | Default: enable
    url_pattern: str  # URL pattern to be exempted from web proxy forwardi | MaxLen: 511
    forward_server: str  # Forward server name. | MaxLen: 63
    fast_fallback: str  # Fast fallback configuration entry name. | MaxLen: 63
    cache_exemption: Literal["enable", "disable"]  # Enable/disable exempting this URL pattern from cac | Default: disable
    comment: str  # Comment. | MaxLen: 255


@final
class UrlMatchObject:
    """Typed FortiObject for web_proxy/url_match with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Configure a name for the URL to be exempted. | MaxLen: 63
    name: str
    # Enable/disable exempting the URLs matching the URL pattern f | Default: enable
    status: Literal["enable", "disable"]
    # URL pattern to be exempted from web proxy forwarding, cachin | MaxLen: 511
    url_pattern: str
    # Forward server name. | MaxLen: 63
    forward_server: str
    # Fast fallback configuration entry name. | MaxLen: 63
    fast_fallback: str
    # Enable/disable exempting this URL pattern from caching. | Default: disable
    cache_exemption: Literal["enable", "disable"]
    # Comment. | MaxLen: 255
    comment: str
    
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
    def to_dict(self) -> UrlMatchPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class UrlMatch:
    """
    Exempt URLs from web proxy forwarding, caching and fast-fallback.
    
    Path: web_proxy/url_match
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
    ) -> UrlMatchObject: ...
    
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
    ) -> UrlMatchObject: ...
    
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
    ) -> FortiObjectList[UrlMatchObject]: ...
    
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
    ) -> UrlMatchObject: ...
    
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
    ) -> UrlMatchObject: ...
    
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
    ) -> FortiObjectList[UrlMatchObject]: ...
    
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
    ) -> UrlMatchObject: ...
    
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
    ) -> UrlMatchObject: ...
    
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
    ) -> FortiObjectList[UrlMatchObject]: ...
    
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
    ) -> UrlMatchObject | list[UrlMatchObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> UrlMatchObject: ...
    
    @overload
    def post(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> UrlMatchObject: ...
    
    @overload
    def put(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> UrlMatchObject: ...
    
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
        payload_dict: UrlMatchPayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        url_pattern: str | None = ...,
        forward_server: str | None = ...,
        fast_fallback: str | None = ...,
        cache_exemption: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
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
    "UrlMatch",
    "UrlMatchPayload",
    "UrlMatchResponse",
    "UrlMatchObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SearchEnginePayload(TypedDict, total=False):
    """
    Type hints for webfilter/search_engine payload fields.
    
    Configure web filter search engines.
    
    **Usage:**
        payload: SearchEnginePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Search engine name. | MaxLen: 35
    hostname: str  # Hostname (regular expression). | MaxLen: 127
    url: str  # URL (regular expression). | MaxLen: 127
    query: str  # Code used to prefix a query | MaxLen: 15
    safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"]  # Safe search method. You can disable safe search, a | Default: disable
    charset: Literal["utf-8", "gb2312"]  # Search engine charset. | Default: utf-8
    safesearch_str: str  # Safe search parameter used in the URL in URL mode. | MaxLen: 255

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SearchEngineResponse(TypedDict):
    """
    Type hints for webfilter/search_engine API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Search engine name. | MaxLen: 35
    hostname: str  # Hostname (regular expression). | MaxLen: 127
    url: str  # URL (regular expression). | MaxLen: 127
    query: str  # Code used to prefix a query | MaxLen: 15
    safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"]  # Safe search method. You can disable safe search, a | Default: disable
    charset: Literal["utf-8", "gb2312"]  # Search engine charset. | Default: utf-8
    safesearch_str: str  # Safe search parameter used in the URL in URL mode. | MaxLen: 255


@final
class SearchEngineObject:
    """Typed FortiObject for webfilter/search_engine with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Search engine name. | MaxLen: 35
    name: str
    # Hostname (regular expression). | MaxLen: 127
    hostname: str
    # URL (regular expression). | MaxLen: 127
    url: str
    # Code used to prefix a query | MaxLen: 15
    query: str
    # Safe search method. You can disable safe search, add the saf | Default: disable
    safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"]
    # Search engine charset. | Default: utf-8
    charset: Literal["utf-8", "gb2312"]
    # Safe search parameter used in the URL in URL mode. In transl | MaxLen: 255
    safesearch_str: str
    
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
    def to_dict(self) -> SearchEnginePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SearchEngine:
    """
    Configure web filter search engines.
    
    Path: webfilter/search_engine
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
    ) -> SearchEngineObject: ...
    
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
    ) -> SearchEngineObject: ...
    
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
    ) -> FortiObjectList[SearchEngineObject]: ...
    
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
    ) -> SearchEngineObject: ...
    
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
    ) -> SearchEngineObject: ...
    
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
    ) -> FortiObjectList[SearchEngineObject]: ...
    
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
    ) -> SearchEngineObject: ...
    
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
    ) -> SearchEngineObject: ...
    
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
    ) -> FortiObjectList[SearchEngineObject]: ...
    
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
    ) -> SearchEngineObject | list[SearchEngineObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SearchEngineObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SearchEngineObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SearchEngineObject: ...
    
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
        payload_dict: SearchEnginePayload | None = ...,
        name: str | None = ...,
        hostname: str | None = ...,
        url: str | None = ...,
        query: str | None = ...,
        safesearch: Literal["disable", "url", "header", "translate", "yt-pattern", "yt-scan", "yt-video", "yt-channel"] | None = ...,
        charset: Literal["utf-8", "gb2312"] | None = ...,
        safesearch_str: str | None = ...,
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
    "SearchEngine",
    "SearchEnginePayload",
    "SearchEngineResponse",
    "SearchEngineObject",
]
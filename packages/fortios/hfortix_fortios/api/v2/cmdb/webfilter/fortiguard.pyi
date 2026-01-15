from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FortiguardPayload(TypedDict, total=False):
    """
    Type hints for webfilter/fortiguard payload fields.
    
    Configure FortiGuard Web Filter service.
    
    **Usage:**
        payload: FortiguardPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    cache_mode: Literal["ttl", "db-ver"]  # Cache entry expiration mode. | Default: ttl
    cache_prefix_match: Literal["enable", "disable"]  # Enable/disable prefix matching in the cache. | Default: enable
    cache_mem_permille: int  # Maximum permille of available memory allocated to | Default: 1 | Min: 1 | Max: 150
    ovrd_auth_port_http: int  # Port to use for FortiGuard Web Filter HTTP overrid | Default: 8008 | Min: 0 | Max: 65535
    ovrd_auth_port_https: int  # Port to use for FortiGuard Web Filter HTTPS overri | Default: 8010 | Min: 0 | Max: 65535
    ovrd_auth_port_https_flow: int  # Port to use for FortiGuard Web Filter HTTPS overri | Default: 8015 | Min: 0 | Max: 65535
    ovrd_auth_port_warning: int  # Port to use for FortiGuard Web Filter Warning over | Default: 8020 | Min: 0 | Max: 65535
    ovrd_auth_https: Literal["enable", "disable"]  # Enable/disable use of HTTPS for override authentic | Default: enable
    warn_auth_https: Literal["enable", "disable"]  # Enable/disable use of HTTPS for warning and authen | Default: enable
    close_ports: Literal["enable", "disable"]  # Close ports used for HTTP/HTTPS override authentic | Default: disable
    request_packet_size_limit: int  # Limit size of URL request packets sent to FortiGua | Default: 0 | Min: 576 | Max: 10000
    embed_image: Literal["enable", "disable"]  # Enable/disable embedding images into replacement m | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class FortiguardResponse(TypedDict):
    """
    Type hints for webfilter/fortiguard API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    cache_mode: Literal["ttl", "db-ver"]  # Cache entry expiration mode. | Default: ttl
    cache_prefix_match: Literal["enable", "disable"]  # Enable/disable prefix matching in the cache. | Default: enable
    cache_mem_permille: int  # Maximum permille of available memory allocated to | Default: 1 | Min: 1 | Max: 150
    ovrd_auth_port_http: int  # Port to use for FortiGuard Web Filter HTTP overrid | Default: 8008 | Min: 0 | Max: 65535
    ovrd_auth_port_https: int  # Port to use for FortiGuard Web Filter HTTPS overri | Default: 8010 | Min: 0 | Max: 65535
    ovrd_auth_port_https_flow: int  # Port to use for FortiGuard Web Filter HTTPS overri | Default: 8015 | Min: 0 | Max: 65535
    ovrd_auth_port_warning: int  # Port to use for FortiGuard Web Filter Warning over | Default: 8020 | Min: 0 | Max: 65535
    ovrd_auth_https: Literal["enable", "disable"]  # Enable/disable use of HTTPS for override authentic | Default: enable
    warn_auth_https: Literal["enable", "disable"]  # Enable/disable use of HTTPS for warning and authen | Default: enable
    close_ports: Literal["enable", "disable"]  # Close ports used for HTTP/HTTPS override authentic | Default: disable
    request_packet_size_limit: int  # Limit size of URL request packets sent to FortiGua | Default: 0 | Min: 576 | Max: 10000
    embed_image: Literal["enable", "disable"]  # Enable/disable embedding images into replacement m | Default: enable


@final
class FortiguardObject:
    """Typed FortiObject for webfilter/fortiguard with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Cache entry expiration mode. | Default: ttl
    cache_mode: Literal["ttl", "db-ver"]
    # Enable/disable prefix matching in the cache. | Default: enable
    cache_prefix_match: Literal["enable", "disable"]
    # Maximum permille of available memory allocated to caching | Default: 1 | Min: 1 | Max: 150
    cache_mem_permille: int
    # Port to use for FortiGuard Web Filter HTTP override authenti | Default: 8008 | Min: 0 | Max: 65535
    ovrd_auth_port_http: int
    # Port to use for FortiGuard Web Filter HTTPS override authent | Default: 8010 | Min: 0 | Max: 65535
    ovrd_auth_port_https: int
    # Port to use for FortiGuard Web Filter HTTPS override authent | Default: 8015 | Min: 0 | Max: 65535
    ovrd_auth_port_https_flow: int
    # Port to use for FortiGuard Web Filter Warning override authe | Default: 8020 | Min: 0 | Max: 65535
    ovrd_auth_port_warning: int
    # Enable/disable use of HTTPS for override authentication. | Default: enable
    ovrd_auth_https: Literal["enable", "disable"]
    # Enable/disable use of HTTPS for warning and authentication. | Default: enable
    warn_auth_https: Literal["enable", "disable"]
    # Close ports used for HTTP/HTTPS override authentication and | Default: disable
    close_ports: Literal["enable", "disable"]
    # Limit size of URL request packets sent to FortiGuard server | Default: 0 | Min: 576 | Max: 10000
    request_packet_size_limit: int
    # Enable/disable embedding images into replacement messages | Default: enable
    embed_image: Literal["enable", "disable"]
    
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
    def to_dict(self) -> FortiguardPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Fortiguard:
    """
    Configure FortiGuard Web Filter service.
    
    Path: webfilter/fortiguard
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
    ) -> FortiguardObject: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> FortiguardObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> FortiguardObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
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
        payload_dict: FortiguardPayload | None = ...,
        cache_mode: Literal["ttl", "db-ver"] | None = ...,
        cache_prefix_match: Literal["enable", "disable"] | None = ...,
        cache_mem_permille: int | None = ...,
        ovrd_auth_port_http: int | None = ...,
        ovrd_auth_port_https: int | None = ...,
        ovrd_auth_port_https_flow: int | None = ...,
        ovrd_auth_port_warning: int | None = ...,
        ovrd_auth_https: Literal["enable", "disable"] | None = ...,
        warn_auth_https: Literal["enable", "disable"] | None = ...,
        close_ports: Literal["enable", "disable"] | None = ...,
        request_packet_size_limit: int | None = ...,
        embed_image: Literal["enable", "disable"] | None = ...,
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
    "Fortiguard",
    "FortiguardPayload",
    "FortiguardResponse",
    "FortiguardObject",
]
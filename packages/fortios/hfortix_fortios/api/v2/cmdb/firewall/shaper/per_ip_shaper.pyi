from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class PerIpShaperPayload(TypedDict, total=False):
    """
    Type hints for firewall/shaper/per_ip_shaper payload fields.
    
    Configure per-IP traffic shaper.
    
    **Usage:**
        payload: PerIpShaperPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Traffic shaper name. | MaxLen: 35
    max_bandwidth: int  # Upper bandwidth limit enforced by this shaper | Default: 0 | Min: 0 | Max: 80000000
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]  # Unit of measurement for maximum bandwidth for this | Default: kbps
    max_concurrent_session: int  # Maximum number of concurrent sessions allowed by t | Default: 0 | Min: 0 | Max: 2097000
    max_concurrent_tcp_session: int  # Maximum number of concurrent TCP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    max_concurrent_udp_session: int  # Maximum number of concurrent UDP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    diffserv_forward: Literal["enable", "disable"]  # Enable/disable changing the Forward (original) Dif | Default: disable
    diffserv_reverse: Literal["enable", "disable"]  # Enable/disable changing the Reverse (reply) DiffSe | Default: disable
    diffservcode_forward: str  # Forward (original) DiffServ setting to be applied
    diffservcode_rev: str  # Reverse (reply) DiffServ setting to be applied to

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class PerIpShaperResponse(TypedDict):
    """
    Type hints for firewall/shaper/per_ip_shaper API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Traffic shaper name. | MaxLen: 35
    max_bandwidth: int  # Upper bandwidth limit enforced by this shaper | Default: 0 | Min: 0 | Max: 80000000
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]  # Unit of measurement for maximum bandwidth for this | Default: kbps
    max_concurrent_session: int  # Maximum number of concurrent sessions allowed by t | Default: 0 | Min: 0 | Max: 2097000
    max_concurrent_tcp_session: int  # Maximum number of concurrent TCP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    max_concurrent_udp_session: int  # Maximum number of concurrent UDP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    diffserv_forward: Literal["enable", "disable"]  # Enable/disable changing the Forward (original) Dif | Default: disable
    diffserv_reverse: Literal["enable", "disable"]  # Enable/disable changing the Reverse (reply) DiffSe | Default: disable
    diffservcode_forward: str  # Forward (original) DiffServ setting to be applied
    diffservcode_rev: str  # Reverse (reply) DiffServ setting to be applied to


@final
class PerIpShaperObject:
    """Typed FortiObject for firewall/shaper/per_ip_shaper with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Traffic shaper name. | MaxLen: 35
    name: str
    # Upper bandwidth limit enforced by this shaper (0 - 80000000) | Default: 0 | Min: 0 | Max: 80000000
    max_bandwidth: int
    # Unit of measurement for maximum bandwidth for this shaper | Default: kbps
    bandwidth_unit: Literal["kbps", "mbps", "gbps"]
    # Maximum number of concurrent sessions allowed by this shaper | Default: 0 | Min: 0 | Max: 2097000
    max_concurrent_session: int
    # Maximum number of concurrent TCP sessions allowed by this sh | Default: 0 | Min: 0 | Max: 2097000
    max_concurrent_tcp_session: int
    # Maximum number of concurrent UDP sessions allowed by this sh | Default: 0 | Min: 0 | Max: 2097000
    max_concurrent_udp_session: int
    # Enable/disable changing the Forward (original) DiffServ sett | Default: disable
    diffserv_forward: Literal["enable", "disable"]
    # Enable/disable changing the Reverse (reply) DiffServ setting | Default: disable
    diffserv_reverse: Literal["enable", "disable"]
    # Forward (original) DiffServ setting to be applied to traffic
    diffservcode_forward: str
    # Reverse (reply) DiffServ setting to be applied to traffic ac
    diffservcode_rev: str
    
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
    def to_dict(self) -> PerIpShaperPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class PerIpShaper:
    """
    Configure per-IP traffic shaper.
    
    Path: firewall/shaper/per_ip_shaper
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
    ) -> PerIpShaperObject: ...
    
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
    ) -> PerIpShaperObject: ...
    
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
    ) -> list[PerIpShaperObject]: ...
    
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
    ) -> PerIpShaperObject: ...
    
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
    ) -> PerIpShaperObject: ...
    
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
    ) -> list[PerIpShaperObject]: ...
    
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
    ) -> PerIpShaperObject: ...
    
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
    ) -> PerIpShaperObject: ...
    
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
    ) -> list[PerIpShaperObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject | list[PerIpShaperObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    @overload
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PerIpShaperObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
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
        payload_dict: PerIpShaperPayload | None = ...,
        name: str | None = ...,
        max_bandwidth: int | None = ...,
        bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = ...,
        max_concurrent_session: int | None = ...,
        max_concurrent_tcp_session: int | None = ...,
        max_concurrent_udp_session: int | None = ...,
        diffserv_forward: Literal["enable", "disable"] | None = ...,
        diffserv_reverse: Literal["enable", "disable"] | None = ...,
        diffservcode_forward: str | None = ...,
        diffservcode_rev: str | None = ...,
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
    "PerIpShaper",
    "PerIpShaperPayload",
    "PerIpShaperResponse",
    "PerIpShaperObject",
]
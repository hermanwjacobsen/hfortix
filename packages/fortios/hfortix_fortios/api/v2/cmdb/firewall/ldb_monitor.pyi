from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LdbMonitorPayload(TypedDict, total=False):
    """
    Type hints for firewall/ldb_monitor payload fields.
    
    Configure server load balancing health monitors.
    
    **Usage:**
        payload: LdbMonitorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Monitor name. | MaxLen: 35
    type: Literal["ping", "tcp", "http", "https", "dns"]  # Select the Monitor type used by the health check m
    interval: int  # Time between health checks | Default: 10 | Min: 5 | Max: 65535
    timeout: int  # Time to wait to receive response to a health check | Default: 2 | Min: 1 | Max: 255
    retry: int  # Number health check attempts before the server is | Default: 3 | Min: 1 | Max: 255
    port: int  # Service port used to perform the health check. If | Default: 0 | Min: 0 | Max: 65535
    src_ip: str  # Source IP for ldb-monitor. | Default: 0.0.0.0
    http_get: str  # Request URI used to send a GET request to check th | MaxLen: 255
    http_match: str  # String to match the value expected in response to | MaxLen: 255
    http_max_redirects: int  # The maximum number of HTTP redirects to be allowed | Default: 0 | Min: 0 | Max: 5
    dns_protocol: Literal["udp", "tcp"]  # Select the protocol used by the DNS health check m | Default: udp
    dns_request_domain: str  # Fully qualified domain name to resolve for the DNS | MaxLen: 255
    dns_match_ip: str  # Response IP expected from DNS server. | Default: 0.0.0.0

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class LdbMonitorResponse(TypedDict):
    """
    Type hints for firewall/ldb_monitor API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Monitor name. | MaxLen: 35
    type: Literal["ping", "tcp", "http", "https", "dns"]  # Select the Monitor type used by the health check m
    interval: int  # Time between health checks | Default: 10 | Min: 5 | Max: 65535
    timeout: int  # Time to wait to receive response to a health check | Default: 2 | Min: 1 | Max: 255
    retry: int  # Number health check attempts before the server is | Default: 3 | Min: 1 | Max: 255
    port: int  # Service port used to perform the health check. If | Default: 0 | Min: 0 | Max: 65535
    src_ip: str  # Source IP for ldb-monitor. | Default: 0.0.0.0
    http_get: str  # Request URI used to send a GET request to check th | MaxLen: 255
    http_match: str  # String to match the value expected in response to | MaxLen: 255
    http_max_redirects: int  # The maximum number of HTTP redirects to be allowed | Default: 0 | Min: 0 | Max: 5
    dns_protocol: Literal["udp", "tcp"]  # Select the protocol used by the DNS health check m | Default: udp
    dns_request_domain: str  # Fully qualified domain name to resolve for the DNS | MaxLen: 255
    dns_match_ip: str  # Response IP expected from DNS server. | Default: 0.0.0.0


@final
class LdbMonitorObject:
    """Typed FortiObject for firewall/ldb_monitor with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Monitor name. | MaxLen: 35
    name: str
    # Select the Monitor type used by the health check monitor to
    type: Literal["ping", "tcp", "http", "https", "dns"]
    # Time between health checks (5 - 65535 sec, default = 10). | Default: 10 | Min: 5 | Max: 65535
    interval: int
    # Time to wait to receive response to a health check from a se | Default: 2 | Min: 1 | Max: 255
    timeout: int
    # Number health check attempts before the server is considered | Default: 3 | Min: 1 | Max: 255
    retry: int
    # Service port used to perform the health check. If 0, health | Default: 0 | Min: 0 | Max: 65535
    port: int
    # Source IP for ldb-monitor. | Default: 0.0.0.0
    src_ip: str
    # Request URI used to send a GET request to check the health o | MaxLen: 255
    http_get: str
    # String to match the value expected in response to an HTTP-GE | MaxLen: 255
    http_match: str
    # The maximum number of HTTP redirects to be allowed | Default: 0 | Min: 0 | Max: 5
    http_max_redirects: int
    # Select the protocol used by the DNS health check monitor to | Default: udp
    dns_protocol: Literal["udp", "tcp"]
    # Fully qualified domain name to resolve for the DNS probe. | MaxLen: 255
    dns_request_domain: str
    # Response IP expected from DNS server. | Default: 0.0.0.0
    dns_match_ip: str
    
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
    def to_dict(self) -> LdbMonitorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LdbMonitor:
    """
    Configure server load balancing health monitors.
    
    Path: firewall/ldb_monitor
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
    ) -> LdbMonitorObject: ...
    
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
    ) -> LdbMonitorObject: ...
    
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
    ) -> list[LdbMonitorObject]: ...
    
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
    ) -> LdbMonitorObject: ...
    
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
    ) -> LdbMonitorObject: ...
    
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
    ) -> list[LdbMonitorObject]: ...
    
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
    ) -> LdbMonitorObject: ...
    
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
    ) -> LdbMonitorObject: ...
    
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
    ) -> list[LdbMonitorObject]: ...
    
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
    ) -> LdbMonitorObject | list[LdbMonitorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> LdbMonitorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> LdbMonitorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
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
    ) -> LdbMonitorObject: ...
    
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
        payload_dict: LdbMonitorPayload | None = ...,
        name: str | None = ...,
        type: Literal["ping", "tcp", "http", "https", "dns"] | None = ...,
        interval: int | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        port: int | None = ...,
        src_ip: str | None = ...,
        http_get: str | None = ...,
        http_match: str | None = ...,
        http_max_redirects: int | None = ...,
        dns_protocol: Literal["udp", "tcp"] | None = ...,
        dns_request_domain: str | None = ...,
        dns_match_ip: str | None = ...,
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
    "LdbMonitor",
    "LdbMonitorPayload",
    "LdbMonitorResponse",
    "LdbMonitorObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WccpPayload(TypedDict, total=False):
    """
    Type hints for system/wccp payload fields.
    
    Configure WCCP.
    
    **Usage:**
        payload: WccpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    service_id: str  # Service ID. | MaxLen: 3
    router_id: str  # IP address known to all cache engines. If all cach | Default: 0.0.0.0
    cache_id: str  # IP address known to all routers. If the addresses | Default: 0.0.0.0
    group_address: str  # IP multicast address used by the cache routers. Fo | Default: 0.0.0.0
    server_list: list[dict[str, Any]]  # IP addresses and netmasks for up to four cache ser
    router_list: list[dict[str, Any]]  # IP addresses of one or more WCCP routers.
    ports_defined: Literal["source", "destination"]  # Match method.
    server_type: Literal["forward", "proxy"]  # Cache server type. | Default: forward
    ports: list[dict[str, Any]]  # Service ports.
    authentication: Literal["enable", "disable"]  # Enable/disable MD5 authentication. | Default: disable
    password: str  # Password for MD5 authentication. | MaxLen: 128
    forward_method: Literal["GRE", "L2", "any"]  # Method used to forward traffic to the cache server | Default: GRE
    cache_engine_method: Literal["GRE", "L2"]  # Method used to forward traffic to the routers or t | Default: GRE
    service_type: Literal["auto", "standard", "dynamic"]  # WCCP service type used by the cache server for log | Default: auto
    primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"]  # Hash method. | Default: dst-ip
    priority: int  # Service priority. | Default: 0 | Min: 0 | Max: 255
    protocol: int  # Service protocol. | Default: 0 | Min: 0 | Max: 255
    assignment_weight: int  # Assignment of hash weight/ratio for the WCCP cache | Default: 0 | Min: 0 | Max: 255
    assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"]  # Assignment bucket format for the WCCP cache engine | Default: cisco-implementation
    return_method: Literal["GRE", "L2", "any"]  # Method used to decline a redirected packet and ret | Default: GRE
    assignment_method: Literal["HASH", "MASK", "any"]  # Hash key assignment preference. | Default: HASH
    assignment_srcaddr_mask: str  # Assignment source address mask. | Default: 0.0.23.65
    assignment_dstaddr_mask: str  # Assignment destination address mask. | Default: 0.0.0.0

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class WccpResponse(TypedDict):
    """
    Type hints for system/wccp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    service_id: str  # Service ID. | MaxLen: 3
    router_id: str  # IP address known to all cache engines. If all cach | Default: 0.0.0.0
    cache_id: str  # IP address known to all routers. If the addresses | Default: 0.0.0.0
    group_address: str  # IP multicast address used by the cache routers. Fo | Default: 0.0.0.0
    server_list: list[dict[str, Any]]  # IP addresses and netmasks for up to four cache ser
    router_list: list[dict[str, Any]]  # IP addresses of one or more WCCP routers.
    ports_defined: Literal["source", "destination"]  # Match method.
    server_type: Literal["forward", "proxy"]  # Cache server type. | Default: forward
    ports: list[dict[str, Any]]  # Service ports.
    authentication: Literal["enable", "disable"]  # Enable/disable MD5 authentication. | Default: disable
    password: str  # Password for MD5 authentication. | MaxLen: 128
    forward_method: Literal["GRE", "L2", "any"]  # Method used to forward traffic to the cache server | Default: GRE
    cache_engine_method: Literal["GRE", "L2"]  # Method used to forward traffic to the routers or t | Default: GRE
    service_type: Literal["auto", "standard", "dynamic"]  # WCCP service type used by the cache server for log | Default: auto
    primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"]  # Hash method. | Default: dst-ip
    priority: int  # Service priority. | Default: 0 | Min: 0 | Max: 255
    protocol: int  # Service protocol. | Default: 0 | Min: 0 | Max: 255
    assignment_weight: int  # Assignment of hash weight/ratio for the WCCP cache | Default: 0 | Min: 0 | Max: 255
    assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"]  # Assignment bucket format for the WCCP cache engine | Default: cisco-implementation
    return_method: Literal["GRE", "L2", "any"]  # Method used to decline a redirected packet and ret | Default: GRE
    assignment_method: Literal["HASH", "MASK", "any"]  # Hash key assignment preference. | Default: HASH
    assignment_srcaddr_mask: str  # Assignment source address mask. | Default: 0.0.23.65
    assignment_dstaddr_mask: str  # Assignment destination address mask. | Default: 0.0.0.0


@final
class WccpObject:
    """Typed FortiObject for system/wccp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Service ID. | MaxLen: 3
    service_id: str
    # IP address known to all cache engines. If all cache engines | Default: 0.0.0.0
    router_id: str
    # IP address known to all routers. If the addresses are the sa | Default: 0.0.0.0
    cache_id: str
    # IP multicast address used by the cache routers. For the Fort | Default: 0.0.0.0
    group_address: str
    # IP addresses and netmasks for up to four cache servers.
    server_list: list[dict[str, Any]]
    # IP addresses of one or more WCCP routers.
    router_list: list[dict[str, Any]]
    # Match method.
    ports_defined: Literal["source", "destination"]
    # Cache server type. | Default: forward
    server_type: Literal["forward", "proxy"]
    # Service ports.
    ports: list[dict[str, Any]]
    # Enable/disable MD5 authentication. | Default: disable
    authentication: Literal["enable", "disable"]
    # Password for MD5 authentication. | MaxLen: 128
    password: str
    # Method used to forward traffic to the cache servers. | Default: GRE
    forward_method: Literal["GRE", "L2", "any"]
    # Method used to forward traffic to the routers or to return t | Default: GRE
    cache_engine_method: Literal["GRE", "L2"]
    # WCCP service type used by the cache server for logical inter | Default: auto
    service_type: Literal["auto", "standard", "dynamic"]
    # Hash method. | Default: dst-ip
    primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"]
    # Service priority. | Default: 0 | Min: 0 | Max: 255
    priority: int
    # Service protocol. | Default: 0 | Min: 0 | Max: 255
    protocol: int
    # Assignment of hash weight/ratio for the WCCP cache engine. | Default: 0 | Min: 0 | Max: 255
    assignment_weight: int
    # Assignment bucket format for the WCCP cache engine. | Default: cisco-implementation
    assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"]
    # Method used to decline a redirected packet and return it to | Default: GRE
    return_method: Literal["GRE", "L2", "any"]
    # Hash key assignment preference. | Default: HASH
    assignment_method: Literal["HASH", "MASK", "any"]
    # Assignment source address mask. | Default: 0.0.23.65
    assignment_srcaddr_mask: str
    # Assignment destination address mask. | Default: 0.0.0.0
    assignment_dstaddr_mask: str
    
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
    def to_dict(self) -> WccpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Wccp:
    """
    Configure WCCP.
    
    Path: system/wccp
    Category: cmdb
    Primary Key: service-id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        service_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        service_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        service_id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[WccpObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        service_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        service_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
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
    ) -> FortiObjectList[WccpObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        service_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        service_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
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
    ) -> FortiObjectList[WccpObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        service_id: str | None = ...,
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
        service_id: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject | list[WccpObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WccpObject: ...
    
    @overload
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        service_id: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        service_id: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: WccpPayload | None = ...,
        service_id: str | None = ...,
        router_id: str | None = ...,
        cache_id: str | None = ...,
        group_address: str | None = ...,
        server_list: str | list[str] | None = ...,
        router_list: str | list[str] | None = ...,
        ports_defined: Literal["source", "destination"] | None = ...,
        server_type: Literal["forward", "proxy"] | None = ...,
        ports: str | list[str] | None = ...,
        authentication: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        forward_method: Literal["GRE", "L2", "any"] | None = ...,
        cache_engine_method: Literal["GRE", "L2"] | None = ...,
        service_type: Literal["auto", "standard", "dynamic"] | None = ...,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = ...,
        priority: int | None = ...,
        protocol: int | None = ...,
        assignment_weight: int | None = ...,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = ...,
        return_method: Literal["GRE", "L2", "any"] | None = ...,
        assignment_method: Literal["HASH", "MASK", "any"] | None = ...,
        assignment_srcaddr_mask: str | None = ...,
        assignment_dstaddr_mask: str | None = ...,
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
    "Wccp",
    "WccpPayload",
    "WccpResponse",
    "WccpObject",
]
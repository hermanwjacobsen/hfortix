from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class PcpServerPayload(TypedDict, total=False):
    """
    Type hints for system/pcp_server payload fields.
    
    Configure PCP server information.
    
    **Usage:**
        payload: PcpServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable PCP server. | Default: disable
    pools: list[dict[str, Any]]  # Configure PCP pools.

# Nested TypedDicts for table field children (dict mode)

class PcpServerPoolsItem(TypedDict):
    """Type hints for pools table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # PCP pool name. | MaxLen: 79
    description: str  # Description. | MaxLen: 127
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    client_subnet: str  # Subnets from which PCP requests are accepted.
    ext_intf: str  # External interface name. | MaxLen: 35
    arp_reply: Literal["disable", "enable"]  # Enable to respond to ARP requests for external IP | Default: enable
    extip: str  # IP address or address range on the external interf
    extport: str  # Incoming port number range that you want to map to
    minimal_lifetime: int  # Minimal lifetime of a PCP mapping in seconds | Default: 120 | Min: 60 | Max: 300
    maximal_lifetime: int  # Maximal lifetime of a PCP mapping in seconds | Default: 86400 | Min: 3600 | Max: 604800
    client_mapping_limit: int  # Mapping limit per client | Default: 0 | Min: 0 | Max: 65535
    mapping_filter_limit: int  # Filter limit per mapping (0 - 5, default = 1). | Default: 1 | Min: 0 | Max: 5
    allow_opcode: Literal["map", "peer", "announce"]  # Allowed PCP opcode. | Default: map peer announce
    third_party: Literal["allow", "disallow"]  # Allow/disallow third party option. | Default: disallow
    third_party_subnet: str  # Subnets from which third party requests are accept
    multicast_announcement: Literal["enable", "disable"]  # Enable/disable multicast announcements. | Default: enable
    announcement_count: int  # Number of multicast announcements. | Default: 3 | Min: 3 | Max: 10
    intl_intf: str  # Internal interface name.
    recycle_delay: int  # Minimum delay (in seconds) the PCP Server will wai | Default: 0 | Min: 0 | Max: 3600


# Nested classes for table field children (object mode)

@final
class PcpServerPoolsObject:
    """Typed object for pools table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # PCP pool name. | MaxLen: 79
    name: str
    # Description. | MaxLen: 127
    description: str
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Subnets from which PCP requests are accepted.
    client_subnet: str
    # External interface name. | MaxLen: 35
    ext_intf: str
    # Enable to respond to ARP requests for external IP | Default: enable
    arp_reply: Literal["disable", "enable"]
    # IP address or address range on the external interface that y
    extip: str
    # Incoming port number range that you want to map to a port nu
    extport: str
    # Minimal lifetime of a PCP mapping in seconds | Default: 120 | Min: 60 | Max: 300
    minimal_lifetime: int
    # Maximal lifetime of a PCP mapping in seconds | Default: 86400 | Min: 3600 | Max: 604800
    maximal_lifetime: int
    # Mapping limit per client | Default: 0 | Min: 0 | Max: 65535
    client_mapping_limit: int
    # Filter limit per mapping (0 - 5, default = 1). | Default: 1 | Min: 0 | Max: 5
    mapping_filter_limit: int
    # Allowed PCP opcode. | Default: map peer announce
    allow_opcode: Literal["map", "peer", "announce"]
    # Allow/disallow third party option. | Default: disallow
    third_party: Literal["allow", "disallow"]
    # Subnets from which third party requests are accepted.
    third_party_subnet: str
    # Enable/disable multicast announcements. | Default: enable
    multicast_announcement: Literal["enable", "disable"]
    # Number of multicast announcements. | Default: 3 | Min: 3 | Max: 10
    announcement_count: int
    # Internal interface name.
    intl_intf: str
    # Minimum delay (in seconds) the PCP Server will wait before r | Default: 0 | Min: 0 | Max: 3600
    recycle_delay: int
    
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
class PcpServerResponse(TypedDict):
    """
    Type hints for system/pcp_server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable PCP server. | Default: disable
    pools: list[PcpServerPoolsItem]  # Configure PCP pools.


@final
class PcpServerObject:
    """Typed FortiObject for system/pcp_server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable PCP server. | Default: disable
    status: Literal["enable", "disable"]
    # Configure PCP pools.
    pools: list[PcpServerPoolsObject]
    
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
    def to_dict(self) -> PcpServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class PcpServer:
    """
    Configure PCP server information.
    
    Path: system/pcp_server
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject: ...
    
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
    ) -> PcpServerObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: PcpServerPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> PcpServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: PcpServerPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: PcpServerPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: PcpServerPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: PcpServerPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: PcpServerPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        pools: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "PcpServer",
    "PcpServerPayload",
    "PcpServerResponse",
    "PcpServerObject",
]
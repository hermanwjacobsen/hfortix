from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SnmpCommunityPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/snmp_community payload fields.
    
    Configure FortiSwitch SNMP v1/v2c communities globally.
    
    **Usage:**
        payload: SnmpCommunityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # SNMP community ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # SNMP community name. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable this SNMP community. | Default: enable
    hosts: list[dict[str, Any]]  # Configure IPv4 SNMP managers (hosts).
    query_v1_status: Literal["disable", "enable"]  # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_port: int  # SNMP v1 query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v2c_status: Literal["disable", "enable"]  # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_port: int  # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    trap_v1_status: Literal["disable", "enable"]  # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v1_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_status: Literal["disable", "enable"]  # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]  # SNMP notifications (traps) to send. | Default: cpu-high mem-low log-full intf-ip ent-conf-change l2mac

# Nested TypedDicts for table field children (dict mode)

class SnmpCommunityHostsItem(TypedDict):
    """Type hints for hosts table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Host entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    ip: str  # IPv4 address of the SNMP manager (host).


# Nested classes for table field children (object mode)

@final
class SnmpCommunityHostsObject:
    """Typed object for hosts table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Host entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IPv4 address of the SNMP manager (host).
    ip: str
    
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
class SnmpCommunityResponse(TypedDict):
    """
    Type hints for switch_controller/snmp_community API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # SNMP community ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # SNMP community name. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable this SNMP community. | Default: enable
    hosts: list[SnmpCommunityHostsItem]  # Configure IPv4 SNMP managers (hosts).
    query_v1_status: Literal["disable", "enable"]  # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_port: int  # SNMP v1 query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v2c_status: Literal["disable", "enable"]  # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_port: int  # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    trap_v1_status: Literal["disable", "enable"]  # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v1_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_status: Literal["disable", "enable"]  # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]  # SNMP notifications (traps) to send. | Default: cpu-high mem-low log-full intf-ip ent-conf-change l2mac


@final
class SnmpCommunityObject:
    """Typed FortiObject for switch_controller/snmp_community with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # SNMP community ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # SNMP community name. | MaxLen: 35
    name: str
    # Enable/disable this SNMP community. | Default: enable
    status: Literal["disable", "enable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: list[SnmpCommunityHostsObject]
    # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_status: Literal["disable", "enable"]
    # SNMP v1 query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v1_port: int
    # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_status: Literal["disable", "enable"]
    # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v2c_port: int
    # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v1_lport: int
    # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v1_rport: int
    # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_lport: int
    # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_rport: int
    # SNMP notifications (traps) to send. | Default: cpu-high mem-low log-full intf-ip ent-conf-change l2mac
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]
    
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
    def to_dict(self) -> SnmpCommunityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class SnmpCommunity:
    """
    Configure FortiSwitch SNMP v1/v2c communities globally.
    
    Path: switch_controller/snmp_community
    Category: cmdb
    Primary Key: id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[SnmpCommunityObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
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
    ) -> FortiObjectList[SnmpCommunityObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        id: int,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
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
    ) -> FortiObjectList[SnmpCommunityObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        id: int | None = ...,
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
        id: int | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject | list[SnmpCommunityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> SnmpCommunityObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SnmpCommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["disable", "enable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["disable", "enable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["disable", "enable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["disable", "enable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"] | list[str] | None = ...,
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
    "SnmpCommunity",
    "SnmpCommunityPayload",
    "SnmpCommunityResponse",
    "SnmpCommunityObject",
]
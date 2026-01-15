from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CommunityPayload(TypedDict, total=False):
    """
    Type hints for system/snmp/community payload fields.
    
    SNMP community configuration.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.snmp.mib-view.MibViewEndpoint` (via: mib-view)

    **Usage:**
        payload: CommunityPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # Community ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Community name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this SNMP community. | Default: enable
    hosts: list[dict[str, Any]]  # Configure IPv4 SNMP managers (hosts).
    hosts6: list[dict[str, Any]]  # Configure IPv6 SNMP managers.
    query_v1_status: Literal["enable", "disable"]  # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_port: int  # SNMP v1 query port (default = 161). | Default: 161 | Min: 1 | Max: 65535
    query_v2c_status: Literal["enable", "disable"]  # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_port: int  # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    trap_v1_status: Literal["enable", "disable"]  # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_lport: int  # SNMP v1 trap local port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v1_rport: int  # SNMP v1 trap remote port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v2c_status: Literal["enable", "disable"]  # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v2c_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]  # SNMP trap events. | Default: cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open faz-disconnect faz wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down load-balance-real-server-down per-cpu-high dhcp pool-usage ippool interface ospf-nbr-state-change ospf-virtnbr-state-change bfd
    mib_view: str  # SNMP access control MIB view. | MaxLen: 32
    vdoms: list[dict[str, Any]]  # SNMP access control VDOMs.

# Nested TypedDicts for table field children (dict mode)

class CommunityHostsItem(TypedDict):
    """Type hints for hosts table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Host entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    source_ip: str  # Source IPv4 address for SNMP traps. | Default: 0.0.0.0
    ip: str  # IPv4 address of the SNMP manager (host).
    ha_direct: Literal["enable", "disable"]  # Enable/disable direct management of HA cluster mem | Default: disable
    host_type: Literal["any", "query", "trap"]  # Control whether the SNMP manager sends SNMP querie | Default: any
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


class CommunityHosts6Item(TypedDict):
    """Type hints for hosts6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Host6 entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    source_ipv6: str  # Source IPv6 address for SNMP traps. | Default: ::
    ipv6: str  # SNMP manager IPv6 address prefix. | Default: ::/0
    ha_direct: Literal["enable", "disable"]  # Enable/disable direct management of HA cluster mem | Default: disable
    host_type: Literal["any", "query", "trap"]  # Control whether the SNMP manager sends SNMP querie | Default: any
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


class CommunityVdomsItem(TypedDict):
    """Type hints for vdoms table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # VDOM name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class CommunityHostsObject:
    """Typed object for hosts table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Host entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Source IPv4 address for SNMP traps. | Default: 0.0.0.0
    source_ip: str
    # IPv4 address of the SNMP manager (host).
    ip: str
    # Enable/disable direct management of HA cluster members. | Default: disable
    ha_direct: Literal["enable", "disable"]
    # Control whether the SNMP manager sends SNMP queries, receive | Default: any
    host_type: Literal["any", "query", "trap"]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
class CommunityHosts6Object:
    """Typed object for hosts6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Host6 entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Source IPv6 address for SNMP traps. | Default: ::
    source_ipv6: str
    # SNMP manager IPv6 address prefix. | Default: ::/0
    ipv6: str
    # Enable/disable direct management of HA cluster members. | Default: disable
    ha_direct: Literal["enable", "disable"]
    # Control whether the SNMP manager sends SNMP queries, receive | Default: any
    host_type: Literal["any", "query", "trap"]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
class CommunityVdomsObject:
    """Typed object for vdoms table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VDOM name. | MaxLen: 79
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
class CommunityResponse(TypedDict):
    """
    Type hints for system/snmp/community API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # Community ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Community name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this SNMP community. | Default: enable
    hosts: list[CommunityHostsItem]  # Configure IPv4 SNMP managers (hosts).
    hosts6: list[CommunityHosts6Item]  # Configure IPv6 SNMP managers.
    query_v1_status: Literal["enable", "disable"]  # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_port: int  # SNMP v1 query port (default = 161). | Default: 161 | Min: 1 | Max: 65535
    query_v2c_status: Literal["enable", "disable"]  # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_port: int  # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    trap_v1_status: Literal["enable", "disable"]  # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_lport: int  # SNMP v1 trap local port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v1_rport: int  # SNMP v1 trap remote port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v2c_status: Literal["enable", "disable"]  # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v2c_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]  # SNMP trap events. | Default: cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open faz-disconnect faz wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down load-balance-real-server-down per-cpu-high dhcp pool-usage ippool interface ospf-nbr-state-change ospf-virtnbr-state-change bfd
    mib_view: str  # SNMP access control MIB view. | MaxLen: 32
    vdoms: list[CommunityVdomsItem]  # SNMP access control VDOMs.


@final
class CommunityObject:
    """Typed FortiObject for system/snmp/community with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Community ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Community name. | MaxLen: 35
    name: str
    # Enable/disable this SNMP community. | Default: enable
    status: Literal["enable", "disable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: list[CommunityHostsObject]
    # Configure IPv6 SNMP managers.
    hosts6: list[CommunityHosts6Object]
    # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_status: Literal["enable", "disable"]
    # SNMP v1 query port (default = 161). | Default: 161 | Min: 1 | Max: 65535
    query_v1_port: int
    # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_status: Literal["enable", "disable"]
    # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v2c_port: int
    # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_status: Literal["enable", "disable"]
    # SNMP v1 trap local port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v1_lport: int
    # SNMP v1 trap remote port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v1_rport: int
    # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_status: Literal["enable", "disable"]
    # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v2c_lport: int
    # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 1 | Max: 65535
    trap_v2c_rport: int
    # SNMP trap events. | Default: cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open faz-disconnect faz wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down load-balance-real-server-down per-cpu-high dhcp pool-usage ippool interface ospf-nbr-state-change ospf-virtnbr-state-change bfd
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"]
    # SNMP access control MIB view. | MaxLen: 32
    mib_view: str
    # SNMP access control VDOMs.
    vdoms: list[CommunityVdomsObject]
    
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
    def to_dict(self) -> CommunityPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Community:
    """
    SNMP community configuration.
    
    Path: system/snmp/community
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
    ) -> CommunityObject: ...
    
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
    ) -> CommunityObject: ...
    
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
    ) -> FortiObjectList[CommunityObject]: ...
    
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
    ) -> CommunityObject: ...
    
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
    ) -> CommunityObject: ...
    
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
    ) -> FortiObjectList[CommunityObject]: ...
    
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
    ) -> CommunityObject: ...
    
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
    ) -> CommunityObject: ...
    
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
    ) -> FortiObjectList[CommunityObject]: ...
    
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
    ) -> CommunityObject | list[CommunityObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> CommunityObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> CommunityObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> CommunityObject: ...
    
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        id: int,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: CommunityPayload | None = ...,
        id: int | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        hosts: str | list[str] | list[dict[str, Any]] | None = ...,
        hosts6: str | list[str] | list[dict[str, Any]] | None = ...,
        query_v1_status: Literal["enable", "disable"] | None = ...,
        query_v1_port: int | None = ...,
        query_v2c_status: Literal["enable", "disable"] | None = ...,
        query_v2c_port: int | None = ...,
        trap_v1_status: Literal["enable", "disable"] | None = ...,
        trap_v1_lport: int | None = ...,
        trap_v1_rport: int | None = ...,
        trap_v2c_status: Literal["enable", "disable"] | None = ...,
        trap_v2c_lport: int | None = ...,
        trap_v2c_rport: int | None = ...,
        events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "vpn-tun-up", "vpn-tun-down", "ha-switch", "ha-hb-failure", "ips-signature", "ips-anomaly", "av-virus", "av-oversize", "av-pattern", "av-fragmented", "fm-if-change", "fm-conf-change", "bgp-established", "bgp-backward-transition", "ha-member-up", "ha-member-down", "ent-conf-change", "av-conserve", "av-bypass", "av-oversize-passed", "av-oversize-blocked", "ips-pkg-update", "ips-fail-open", "faz-disconnect", "faz", "wc-ap-up", "wc-ap-down", "fswctl-session-up", "fswctl-session-down", "load-balance-real-server-down", "device-new", "per-cpu-high", "dhcp", "pool-usage", "ippool", "interface", "ospf-nbr-state-change", "ospf-virtnbr-state-change", "bfd"] | list[str] | None = ...,
        mib_view: str | None = ...,
        vdoms: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Community",
    "CommunityPayload",
    "CommunityResponse",
    "CommunityObject",
]
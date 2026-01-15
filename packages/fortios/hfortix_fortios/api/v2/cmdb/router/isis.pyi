from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class IsisPayload(TypedDict, total=False):
    """
    Type hints for router/isis payload fields.
    
    Configure IS-IS.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.access-list.AccessListEndpoint` (via: redistribute-l1-list, redistribute-l2-list)
        - :class:`~.router.access-list6.AccessList6Endpoint` (via: redistribute6-l1-list, redistribute6-l2-list)
        - :class:`~.router.key-chain.KeyChainEndpoint` (via: auth-keychain-l1, auth-keychain-l2)

    **Usage:**
        payload: IsisPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    is_type: Literal["level-1-2", "level-1", "level-2-only"]  # IS type. | Default: level-1-2
    adv_passive_only: Literal["enable", "disable"]  # Enable/disable IS-IS advertisement of passive inte | Default: disable
    adv_passive_only6: Literal["enable", "disable"]  # Enable/disable IPv6 IS-IS advertisement of passive | Default: disable
    auth_mode_l1: Literal["password", "md5"]  # Level 1 authentication mode. | Default: password
    auth_mode_l2: Literal["password", "md5"]  # Level 2 authentication mode. | Default: password
    auth_password_l1: str  # Authentication password for level 1 PDUs. | MaxLen: 128
    auth_password_l2: str  # Authentication password for level 2 PDUs. | MaxLen: 128
    auth_keychain_l1: str  # Authentication key-chain for level 1 PDUs. | MaxLen: 35
    auth_keychain_l2: str  # Authentication key-chain for level 2 PDUs. | MaxLen: 35
    auth_sendonly_l1: Literal["enable", "disable"]  # Enable/disable level 1 authentication send-only. | Default: disable
    auth_sendonly_l2: Literal["enable", "disable"]  # Enable/disable level 2 authentication send-only. | Default: disable
    ignore_lsp_errors: Literal["enable", "disable"]  # Enable/disable ignoring of LSP errors with bad che | Default: disable
    lsp_gen_interval_l1: int  # Minimum interval for level 1 LSP regenerating. | Default: 30 | Min: 1 | Max: 120
    lsp_gen_interval_l2: int  # Minimum interval for level 2 LSP regenerating. | Default: 30 | Min: 1 | Max: 120
    lsp_refresh_interval: int  # LSP refresh time in seconds. | Default: 900 | Min: 1 | Max: 65535
    max_lsp_lifetime: int  # Maximum LSP lifetime in seconds. | Default: 1200 | Min: 350 | Max: 65535
    spf_interval_exp_l1: str  # Level 1 SPF calculation delay.
    spf_interval_exp_l2: str  # Level 2 SPF calculation delay.
    dynamic_hostname: Literal["enable", "disable"]  # Enable/disable dynamic hostname. | Default: disable
    adjacency_check: Literal["enable", "disable"]  # Enable/disable adjacency check. | Default: disable
    adjacency_check6: Literal["enable", "disable"]  # Enable/disable IPv6 adjacency check. | Default: disable
    overload_bit: Literal["enable", "disable"]  # Enable/disable signal other routers not to use us | Default: disable
    overload_bit_suppress: Literal["external", "interlevel"]  # Suppress overload-bit for the specific prefixes.
    overload_bit_on_startup: int  # Overload-bit only temporarily after reboot. | Default: 0 | Min: 5 | Max: 86400
    default_originate: Literal["enable", "disable"]  # Enable/disable distribution of default route infor | Default: disable
    default_originate6: Literal["enable", "disable"]  # Enable/disable distribution of default IPv6 route | Default: disable
    metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"]  # Use old-style (ISO 10589) or new-style packet form | Default: narrow
    redistribute_l1: Literal["enable", "disable"]  # Enable/disable redistribution of level 1 routes in | Default: disable
    redistribute_l1_list: str  # Access-list for route redistribution from l1 to l2 | MaxLen: 35
    redistribute_l2: Literal["enable", "disable"]  # Enable/disable redistribution of level 2 routes in | Default: disable
    redistribute_l2_list: str  # Access-list for route redistribution from l2 to l1 | MaxLen: 35
    redistribute6_l1: Literal["enable", "disable"]  # Enable/disable redistribution of level 1 IPv6 rout | Default: disable
    redistribute6_l1_list: str  # Access-list for IPv6 route redistribution from l1 | MaxLen: 35
    redistribute6_l2: Literal["enable", "disable"]  # Enable/disable redistribution of level 2 IPv6 rout | Default: disable
    redistribute6_l2_list: str  # Access-list for IPv6 route redistribution from l2 | MaxLen: 35
    isis_net: list[dict[str, Any]]  # IS-IS net configuration.
    isis_interface: list[dict[str, Any]]  # IS-IS interface configuration.
    summary_address: list[dict[str, Any]]  # IS-IS summary addresses.
    summary_address6: list[dict[str, Any]]  # IS-IS IPv6 summary address.
    redistribute: list[dict[str, Any]]  # IS-IS redistribute protocols.
    redistribute6: list[dict[str, Any]]  # IS-IS IPv6 redistribution for routing protocols.

# Nested TypedDicts for table field children (dict mode)

class IsisIsisnetItem(TypedDict):
    """Type hints for isis-net table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ISIS network ID. | Default: 0 | Min: 0 | Max: 4294967295
    net: str  # IS-IS networks (format = xx.xxxx.  .xxxx.xx.).


class IsisIsisinterfaceItem(TypedDict):
    """Type hints for isis-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # IS-IS interface name. | MaxLen: 15
    status: Literal["enable", "disable"]  # Enable/disable interface for IS-IS. | Default: disable
    status6: Literal["enable", "disable"]  # Enable/disable IPv6 interface for IS-IS. | Default: disable
    network_type: Literal["broadcast", "point-to-point", "loopback"]  # IS-IS interface's network type.
    circuit_type: Literal["level-1-2", "level-1", "level-2"]  # IS-IS interface's circuit type. | Default: level-1-2
    csnp_interval_l1: int  # Level 1 CSNP interval. | Default: 10 | Min: 1 | Max: 65535
    csnp_interval_l2: int  # Level 2 CSNP interval. | Default: 10 | Min: 1 | Max: 65535
    hello_interval_l1: int  # Level 1 hello interval. | Default: 10 | Min: 0 | Max: 65535
    hello_interval_l2: int  # Level 2 hello interval. | Default: 10 | Min: 0 | Max: 65535
    hello_multiplier_l1: int  # Level 1 multiplier for Hello holding time. | Default: 3 | Min: 2 | Max: 100
    hello_multiplier_l2: int  # Level 2 multiplier for Hello holding time. | Default: 3 | Min: 2 | Max: 100
    hello_padding: Literal["enable", "disable"]  # Enable/disable padding to IS-IS hello packets. | Default: enable
    lsp_interval: int  # LSP transmission interval (milliseconds). | Default: 33 | Min: 1 | Max: 4294967295
    lsp_retransmit_interval: int  # LSP retransmission interval (sec). | Default: 5 | Min: 1 | Max: 65535
    metric_l1: int  # Level 1 metric for interface. | Default: 10 | Min: 1 | Max: 63
    metric_l2: int  # Level 2 metric for interface. | Default: 10 | Min: 1 | Max: 63
    wide_metric_l1: int  # Level 1 wide metric for interface. | Default: 10 | Min: 1 | Max: 16777214
    wide_metric_l2: int  # Level 2 wide metric for interface. | Default: 10 | Min: 1 | Max: 16777214
    auth_password_l1: str  # Authentication password for level 1 PDUs. | MaxLen: 128
    auth_password_l2: str  # Authentication password for level 2 PDUs. | MaxLen: 128
    auth_keychain_l1: str  # Authentication key-chain for level 1 PDUs. | MaxLen: 35
    auth_keychain_l2: str  # Authentication key-chain for level 2 PDUs. | MaxLen: 35
    auth_send_only_l1: Literal["enable", "disable"]  # Enable/disable authentication send-only for level | Default: disable
    auth_send_only_l2: Literal["enable", "disable"]  # Enable/disable authentication send-only for level | Default: disable
    auth_mode_l1: Literal["md5", "password"]  # Level 1 authentication mode. | Default: password
    auth_mode_l2: Literal["md5", "password"]  # Level 2 authentication mode. | Default: password
    priority_l1: int  # Level 1 priority. | Default: 64 | Min: 0 | Max: 127
    priority_l2: int  # Level 2 priority. | Default: 64 | Min: 0 | Max: 127
    mesh_group: Literal["enable", "disable"]  # Enable/disable IS-IS mesh group. | Default: disable
    mesh_group_id: int  # Mesh group ID <0-4294967295>, 0: mesh-group blocke | Default: 0 | Min: 0 | Max: 4294967295


class IsisSummaryaddressItem(TypedDict):
    """Type hints for summary-address table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Summary address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Prefix. | Default: 0.0.0.0 0.0.0.0
    level: Literal["level-1-2", "level-1", "level-2"]  # Level. | Default: level-2


class IsisSummaryaddress6Item(TypedDict):
    """Type hints for summary-address6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Prefix entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix6: str  # IPv6 prefix. | Default: ::/0
    level: Literal["level-1-2", "level-1", "level-2"]  # Level. | Default: level-2


class IsisRedistributeItem(TypedDict):
    """Type hints for redistribute table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    protocol: str  # Protocol name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Status. | Default: disable
    metric: int  # Metric. | Default: 0 | Min: 0 | Max: 4261412864
    metric_type: Literal["external", "internal"]  # Metric type. | Default: internal
    level: Literal["level-1-2", "level-1", "level-2"]  # Level. | Default: level-2
    routemap: str  # Route map name. | MaxLen: 35


class IsisRedistribute6Item(TypedDict):
    """Type hints for redistribute6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    protocol: str  # Protocol name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable redistribution. | Default: disable
    metric: int  # Metric. | Default: 0 | Min: 0 | Max: 4261412864
    metric_type: Literal["external", "internal"]  # Metric type. | Default: internal
    level: Literal["level-1-2", "level-1", "level-2"]  # Level. | Default: level-2
    routemap: str  # Route map name. | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class IsisIsisnetObject:
    """Typed object for isis-net table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ISIS network ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IS-IS networks (format = xx.xxxx.  .xxxx.xx.).
    net: str
    
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
class IsisIsisinterfaceObject:
    """Typed object for isis-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IS-IS interface name. | MaxLen: 15
    name: str
    # Enable/disable interface for IS-IS. | Default: disable
    status: Literal["enable", "disable"]
    # Enable/disable IPv6 interface for IS-IS. | Default: disable
    status6: Literal["enable", "disable"]
    # IS-IS interface's network type.
    network_type: Literal["broadcast", "point-to-point", "loopback"]
    # IS-IS interface's circuit type. | Default: level-1-2
    circuit_type: Literal["level-1-2", "level-1", "level-2"]
    # Level 1 CSNP interval. | Default: 10 | Min: 1 | Max: 65535
    csnp_interval_l1: int
    # Level 2 CSNP interval. | Default: 10 | Min: 1 | Max: 65535
    csnp_interval_l2: int
    # Level 1 hello interval. | Default: 10 | Min: 0 | Max: 65535
    hello_interval_l1: int
    # Level 2 hello interval. | Default: 10 | Min: 0 | Max: 65535
    hello_interval_l2: int
    # Level 1 multiplier for Hello holding time. | Default: 3 | Min: 2 | Max: 100
    hello_multiplier_l1: int
    # Level 2 multiplier for Hello holding time. | Default: 3 | Min: 2 | Max: 100
    hello_multiplier_l2: int
    # Enable/disable padding to IS-IS hello packets. | Default: enable
    hello_padding: Literal["enable", "disable"]
    # LSP transmission interval (milliseconds). | Default: 33 | Min: 1 | Max: 4294967295
    lsp_interval: int
    # LSP retransmission interval (sec). | Default: 5 | Min: 1 | Max: 65535
    lsp_retransmit_interval: int
    # Level 1 metric for interface. | Default: 10 | Min: 1 | Max: 63
    metric_l1: int
    # Level 2 metric for interface. | Default: 10 | Min: 1 | Max: 63
    metric_l2: int
    # Level 1 wide metric for interface. | Default: 10 | Min: 1 | Max: 16777214
    wide_metric_l1: int
    # Level 2 wide metric for interface. | Default: 10 | Min: 1 | Max: 16777214
    wide_metric_l2: int
    # Authentication password for level 1 PDUs. | MaxLen: 128
    auth_password_l1: str
    # Authentication password for level 2 PDUs. | MaxLen: 128
    auth_password_l2: str
    # Authentication key-chain for level 1 PDUs. | MaxLen: 35
    auth_keychain_l1: str
    # Authentication key-chain for level 2 PDUs. | MaxLen: 35
    auth_keychain_l2: str
    # Enable/disable authentication send-only for level 1 PDUs. | Default: disable
    auth_send_only_l1: Literal["enable", "disable"]
    # Enable/disable authentication send-only for level 2 PDUs. | Default: disable
    auth_send_only_l2: Literal["enable", "disable"]
    # Level 1 authentication mode. | Default: password
    auth_mode_l1: Literal["md5", "password"]
    # Level 2 authentication mode. | Default: password
    auth_mode_l2: Literal["md5", "password"]
    # Level 1 priority. | Default: 64 | Min: 0 | Max: 127
    priority_l1: int
    # Level 2 priority. | Default: 64 | Min: 0 | Max: 127
    priority_l2: int
    # Enable/disable IS-IS mesh group. | Default: disable
    mesh_group: Literal["enable", "disable"]
    # Mesh group ID <0-4294967295>, 0: mesh-group blocked. | Default: 0 | Min: 0 | Max: 4294967295
    mesh_group_id: int
    
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
class IsisSummaryaddressObject:
    """Typed object for summary-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Summary address entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Level. | Default: level-2
    level: Literal["level-1-2", "level-1", "level-2"]
    
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
class IsisSummaryaddress6Object:
    """Typed object for summary-address6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Prefix entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IPv6 prefix. | Default: ::/0
    prefix6: str
    # Level. | Default: level-2
    level: Literal["level-1-2", "level-1", "level-2"]
    
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
class IsisRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Protocol name. | MaxLen: 35
    protocol: str
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Metric. | Default: 0 | Min: 0 | Max: 4261412864
    metric: int
    # Metric type. | Default: internal
    metric_type: Literal["external", "internal"]
    # Level. | Default: level-2
    level: Literal["level-1-2", "level-1", "level-2"]
    # Route map name. | MaxLen: 35
    routemap: str
    
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
class IsisRedistribute6Object:
    """Typed object for redistribute6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Protocol name. | MaxLen: 35
    protocol: str
    # Enable/disable redistribution. | Default: disable
    status: Literal["enable", "disable"]
    # Metric. | Default: 0 | Min: 0 | Max: 4261412864
    metric: int
    # Metric type. | Default: internal
    metric_type: Literal["external", "internal"]
    # Level. | Default: level-2
    level: Literal["level-1-2", "level-1", "level-2"]
    # Route map name. | MaxLen: 35
    routemap: str
    
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
class IsisResponse(TypedDict):
    """
    Type hints for router/isis API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    is_type: Literal["level-1-2", "level-1", "level-2-only"]  # IS type. | Default: level-1-2
    adv_passive_only: Literal["enable", "disable"]  # Enable/disable IS-IS advertisement of passive inte | Default: disable
    adv_passive_only6: Literal["enable", "disable"]  # Enable/disable IPv6 IS-IS advertisement of passive | Default: disable
    auth_mode_l1: Literal["password", "md5"]  # Level 1 authentication mode. | Default: password
    auth_mode_l2: Literal["password", "md5"]  # Level 2 authentication mode. | Default: password
    auth_password_l1: str  # Authentication password for level 1 PDUs. | MaxLen: 128
    auth_password_l2: str  # Authentication password for level 2 PDUs. | MaxLen: 128
    auth_keychain_l1: str  # Authentication key-chain for level 1 PDUs. | MaxLen: 35
    auth_keychain_l2: str  # Authentication key-chain for level 2 PDUs. | MaxLen: 35
    auth_sendonly_l1: Literal["enable", "disable"]  # Enable/disable level 1 authentication send-only. | Default: disable
    auth_sendonly_l2: Literal["enable", "disable"]  # Enable/disable level 2 authentication send-only. | Default: disable
    ignore_lsp_errors: Literal["enable", "disable"]  # Enable/disable ignoring of LSP errors with bad che | Default: disable
    lsp_gen_interval_l1: int  # Minimum interval for level 1 LSP regenerating. | Default: 30 | Min: 1 | Max: 120
    lsp_gen_interval_l2: int  # Minimum interval for level 2 LSP regenerating. | Default: 30 | Min: 1 | Max: 120
    lsp_refresh_interval: int  # LSP refresh time in seconds. | Default: 900 | Min: 1 | Max: 65535
    max_lsp_lifetime: int  # Maximum LSP lifetime in seconds. | Default: 1200 | Min: 350 | Max: 65535
    spf_interval_exp_l1: str  # Level 1 SPF calculation delay.
    spf_interval_exp_l2: str  # Level 2 SPF calculation delay.
    dynamic_hostname: Literal["enable", "disable"]  # Enable/disable dynamic hostname. | Default: disable
    adjacency_check: Literal["enable", "disable"]  # Enable/disable adjacency check. | Default: disable
    adjacency_check6: Literal["enable", "disable"]  # Enable/disable IPv6 adjacency check. | Default: disable
    overload_bit: Literal["enable", "disable"]  # Enable/disable signal other routers not to use us | Default: disable
    overload_bit_suppress: Literal["external", "interlevel"]  # Suppress overload-bit for the specific prefixes.
    overload_bit_on_startup: int  # Overload-bit only temporarily after reboot. | Default: 0 | Min: 5 | Max: 86400
    default_originate: Literal["enable", "disable"]  # Enable/disable distribution of default route infor | Default: disable
    default_originate6: Literal["enable", "disable"]  # Enable/disable distribution of default IPv6 route | Default: disable
    metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"]  # Use old-style (ISO 10589) or new-style packet form | Default: narrow
    redistribute_l1: Literal["enable", "disable"]  # Enable/disable redistribution of level 1 routes in | Default: disable
    redistribute_l1_list: str  # Access-list for route redistribution from l1 to l2 | MaxLen: 35
    redistribute_l2: Literal["enable", "disable"]  # Enable/disable redistribution of level 2 routes in | Default: disable
    redistribute_l2_list: str  # Access-list for route redistribution from l2 to l1 | MaxLen: 35
    redistribute6_l1: Literal["enable", "disable"]  # Enable/disable redistribution of level 1 IPv6 rout | Default: disable
    redistribute6_l1_list: str  # Access-list for IPv6 route redistribution from l1 | MaxLen: 35
    redistribute6_l2: Literal["enable", "disable"]  # Enable/disable redistribution of level 2 IPv6 rout | Default: disable
    redistribute6_l2_list: str  # Access-list for IPv6 route redistribution from l2 | MaxLen: 35
    isis_net: list[IsisIsisnetItem]  # IS-IS net configuration.
    isis_interface: list[IsisIsisinterfaceItem]  # IS-IS interface configuration.
    summary_address: list[IsisSummaryaddressItem]  # IS-IS summary addresses.
    summary_address6: list[IsisSummaryaddress6Item]  # IS-IS IPv6 summary address.
    redistribute: list[IsisRedistributeItem]  # IS-IS redistribute protocols.
    redistribute6: list[IsisRedistribute6Item]  # IS-IS IPv6 redistribution for routing protocols.


@final
class IsisObject:
    """Typed FortiObject for router/isis with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IS type. | Default: level-1-2
    is_type: Literal["level-1-2", "level-1", "level-2-only"]
    # Enable/disable IS-IS advertisement of passive interfaces onl | Default: disable
    adv_passive_only: Literal["enable", "disable"]
    # Enable/disable IPv6 IS-IS advertisement of passive interface | Default: disable
    adv_passive_only6: Literal["enable", "disable"]
    # Level 1 authentication mode. | Default: password
    auth_mode_l1: Literal["password", "md5"]
    # Level 2 authentication mode. | Default: password
    auth_mode_l2: Literal["password", "md5"]
    # Authentication password for level 1 PDUs. | MaxLen: 128
    auth_password_l1: str
    # Authentication password for level 2 PDUs. | MaxLen: 128
    auth_password_l2: str
    # Authentication key-chain for level 1 PDUs. | MaxLen: 35
    auth_keychain_l1: str
    # Authentication key-chain for level 2 PDUs. | MaxLen: 35
    auth_keychain_l2: str
    # Enable/disable level 1 authentication send-only. | Default: disable
    auth_sendonly_l1: Literal["enable", "disable"]
    # Enable/disable level 2 authentication send-only. | Default: disable
    auth_sendonly_l2: Literal["enable", "disable"]
    # Enable/disable ignoring of LSP errors with bad checksums. | Default: disable
    ignore_lsp_errors: Literal["enable", "disable"]
    # Minimum interval for level 1 LSP regenerating. | Default: 30 | Min: 1 | Max: 120
    lsp_gen_interval_l1: int
    # Minimum interval for level 2 LSP regenerating. | Default: 30 | Min: 1 | Max: 120
    lsp_gen_interval_l2: int
    # LSP refresh time in seconds. | Default: 900 | Min: 1 | Max: 65535
    lsp_refresh_interval: int
    # Maximum LSP lifetime in seconds. | Default: 1200 | Min: 350 | Max: 65535
    max_lsp_lifetime: int
    # Level 1 SPF calculation delay.
    spf_interval_exp_l1: str
    # Level 2 SPF calculation delay.
    spf_interval_exp_l2: str
    # Enable/disable dynamic hostname. | Default: disable
    dynamic_hostname: Literal["enable", "disable"]
    # Enable/disable adjacency check. | Default: disable
    adjacency_check: Literal["enable", "disable"]
    # Enable/disable IPv6 adjacency check. | Default: disable
    adjacency_check6: Literal["enable", "disable"]
    # Enable/disable signal other routers not to use us in SPF. | Default: disable
    overload_bit: Literal["enable", "disable"]
    # Suppress overload-bit for the specific prefixes.
    overload_bit_suppress: Literal["external", "interlevel"]
    # Overload-bit only temporarily after reboot. | Default: 0 | Min: 5 | Max: 86400
    overload_bit_on_startup: int
    # Enable/disable distribution of default route information. | Default: disable
    default_originate: Literal["enable", "disable"]
    # Enable/disable distribution of default IPv6 route informatio | Default: disable
    default_originate6: Literal["enable", "disable"]
    # Use old-style (ISO 10589) or new-style packet formats. | Default: narrow
    metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"]
    # Enable/disable redistribution of level 1 routes into level 2 | Default: disable
    redistribute_l1: Literal["enable", "disable"]
    # Access-list for route redistribution from l1 to l2. | MaxLen: 35
    redistribute_l1_list: str
    # Enable/disable redistribution of level 2 routes into level 1 | Default: disable
    redistribute_l2: Literal["enable", "disable"]
    # Access-list for route redistribution from l2 to l1. | MaxLen: 35
    redistribute_l2_list: str
    # Enable/disable redistribution of level 1 IPv6 routes into le | Default: disable
    redistribute6_l1: Literal["enable", "disable"]
    # Access-list for IPv6 route redistribution from l1 to l2. | MaxLen: 35
    redistribute6_l1_list: str
    # Enable/disable redistribution of level 2 IPv6 routes into le | Default: disable
    redistribute6_l2: Literal["enable", "disable"]
    # Access-list for IPv6 route redistribution from l2 to l1. | MaxLen: 35
    redistribute6_l2_list: str
    # IS-IS net configuration.
    isis_net: list[IsisIsisnetObject]
    # IS-IS interface configuration.
    isis_interface: list[IsisIsisinterfaceObject]
    # IS-IS summary addresses.
    summary_address: list[IsisSummaryaddressObject]
    # IS-IS IPv6 summary address.
    summary_address6: list[IsisSummaryaddress6Object]
    # IS-IS redistribute protocols.
    redistribute: list[IsisRedistributeObject]
    # IS-IS IPv6 redistribution for routing protocols.
    redistribute6: list[IsisRedistribute6Object]
    
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
    def to_dict(self) -> IsisPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Isis:
    """
    Configure IS-IS.
    
    Path: router/isis
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject: ...
    
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
    ) -> IsisObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> IsisObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
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
        payload_dict: IsisPayload | None = ...,
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = ...,
        adv_passive_only: Literal["enable", "disable"] | None = ...,
        adv_passive_only6: Literal["enable", "disable"] | None = ...,
        auth_mode_l1: Literal["password", "md5"] | None = ...,
        auth_mode_l2: Literal["password", "md5"] | None = ...,
        auth_password_l1: str | None = ...,
        auth_password_l2: str | None = ...,
        auth_keychain_l1: str | None = ...,
        auth_keychain_l2: str | None = ...,
        auth_sendonly_l1: Literal["enable", "disable"] | None = ...,
        auth_sendonly_l2: Literal["enable", "disable"] | None = ...,
        ignore_lsp_errors: Literal["enable", "disable"] | None = ...,
        lsp_gen_interval_l1: int | None = ...,
        lsp_gen_interval_l2: int | None = ...,
        lsp_refresh_interval: int | None = ...,
        max_lsp_lifetime: int | None = ...,
        spf_interval_exp_l1: str | None = ...,
        spf_interval_exp_l2: str | None = ...,
        dynamic_hostname: Literal["enable", "disable"] | None = ...,
        adjacency_check: Literal["enable", "disable"] | None = ...,
        adjacency_check6: Literal["enable", "disable"] | None = ...,
        overload_bit: Literal["enable", "disable"] | None = ...,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = ...,
        overload_bit_on_startup: int | None = ...,
        default_originate: Literal["enable", "disable"] | None = ...,
        default_originate6: Literal["enable", "disable"] | None = ...,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = ...,
        redistribute_l1: Literal["enable", "disable"] | None = ...,
        redistribute_l1_list: str | None = ...,
        redistribute_l2: Literal["enable", "disable"] | None = ...,
        redistribute_l2_list: str | None = ...,
        redistribute6_l1: Literal["enable", "disable"] | None = ...,
        redistribute6_l1_list: str | None = ...,
        redistribute6_l2: Literal["enable", "disable"] | None = ...,
        redistribute6_l2_list: str | None = ...,
        isis_net: str | list[str] | list[dict[str, Any]] | None = ...,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address: str | list[str] | list[dict[str, Any]] | None = ...,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Isis",
    "IsisPayload",
    "IsisResponse",
    "IsisObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FabricVpnPayload(TypedDict, total=False):
    """
    Type hints for system/fabric_vpn payload fields.
    
    Setup for self orchestrated fabric auto discovery VPN.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.fabric-vpn.advertised-subnets.AdvertisedSubnetsEndpoint` (via: loopback-advertised-subnet)
        - :class:`~.system.interface.InterfaceEndpoint` (via: loopback-interface)
        - :class:`~.system.sdwan.health-check.HealthCheckEndpoint` (via: health-checks)
        - :class:`~.system.sdwan.zone.ZoneEndpoint` (via: sdwan-zone)

    **Usage:**
        payload: FabricVpnPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable Fabric VPN. | Default: disable
    sync_mode: Literal["enable", "disable"]  # Setting synchronized by fabric or manual. | Default: enable
    branch_name: str  # Branch name. | MaxLen: 35
    policy_rule: Literal["health-check", "manual", "auto"]  # Policy creation rule. | Default: health-check
    vpn_role: Literal["hub", "spoke"]  # Fabric VPN role. | Default: hub
    overlays: list[dict[str, Any]]  # Local overlay interfaces table.
    advertised_subnets: list[dict[str, Any]]  # Local advertised subnets.
    loopback_address_block: str  # IPv4 address and subnet mask for hub's loopback ad | Default: 0.0.0.0 0.0.0.0
    loopback_interface: str  # Loopback interface. | MaxLen: 15
    loopback_advertised_subnet: int  # Loopback advertised subnet reference. | Default: 0 | Min: 0 | Max: 4294967295
    psksecret: str  # Pre-shared secret for ADVPN.
    bgp_as: str  # BGP Router AS number, asplain/asdot/asdot+ format.
    sdwan_zone: str  # Reference to created SD-WAN zone. | MaxLen: 35
    health_checks: list[dict[str, Any]]  # Underlying health checks. | MaxLen: 35

# Nested TypedDicts for table field children (dict mode)

class FabricVpnOverlaysItem(TypedDict):
    """Type hints for overlays table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Overlay name. | MaxLen: 79
    ipsec_network_id: int  # VPN gateway network ID. | Default: 0 | Min: 0 | Max: 255
    overlay_tunnel_block: str  # IPv4 address and subnet mask for the overlay tunne | Default: 0.0.0.0 0.0.0.0
    remote_gw: str  # IP address of the hub gateway (Set by hub). | Default: 0.0.0.0
    interface: str  # Underlying interface name. | MaxLen: 15
    bgp_neighbor: str  # Underlying BGP neighbor entry. | MaxLen: 45
    overlay_policy: int  # The overlay policy to allow ADVPN thru traffic. | Default: 0 | Min: 0 | Max: 4294967295
    bgp_network: int  # Underlying BGP network. | Default: 0 | Min: 0 | Max: 4294967295
    route_policy: int  # Underlying router policy. | Default: 0 | Min: 0 | Max: 4294967295
    bgp_neighbor_group: str  # Underlying BGP neighbor group entry. | MaxLen: 45
    bgp_neighbor_range: int  # Underlying BGP neighbor range entry. | Default: 0 | Min: 0 | Max: 4294967295
    ipsec_phase1: str  # IPsec interface. | MaxLen: 35
    sdwan_member: int  # Reference to SD-WAN member entry. | Default: 0 | Min: 0 | Max: 4294967295


class FabricVpnAdvertisedsubnetsItem(TypedDict):
    """Type hints for advertised-subnets table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967294
    prefix: str  # Network prefix. | Default: 0.0.0.0 0.0.0.0
    access: Literal["inbound", "bidirectional"]  # Access policy direction. | Default: inbound
    bgp_network: int  # Underlying BGP network. | Default: 0 | Min: 0 | Max: 4294967295
    firewall_address: str  # Underlying firewall address. | MaxLen: 79
    policies: int  # Underlying policies. | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class FabricVpnOverlaysObject:
    """Typed object for overlays table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Overlay name. | MaxLen: 79
    name: str
    # VPN gateway network ID. | Default: 0 | Min: 0 | Max: 255
    ipsec_network_id: int
    # IPv4 address and subnet mask for the overlay tunnel , syntax | Default: 0.0.0.0 0.0.0.0
    overlay_tunnel_block: str
    # IP address of the hub gateway (Set by hub). | Default: 0.0.0.0
    remote_gw: str
    # Underlying interface name. | MaxLen: 15
    interface: str
    # Underlying BGP neighbor entry. | MaxLen: 45
    bgp_neighbor: str
    # The overlay policy to allow ADVPN thru traffic. | Default: 0 | Min: 0 | Max: 4294967295
    overlay_policy: int
    # Underlying BGP network. | Default: 0 | Min: 0 | Max: 4294967295
    bgp_network: int
    # Underlying router policy. | Default: 0 | Min: 0 | Max: 4294967295
    route_policy: int
    # Underlying BGP neighbor group entry. | MaxLen: 45
    bgp_neighbor_group: str
    # Underlying BGP neighbor range entry. | Default: 0 | Min: 0 | Max: 4294967295
    bgp_neighbor_range: int
    # IPsec interface. | MaxLen: 35
    ipsec_phase1: str
    # Reference to SD-WAN member entry. | Default: 0 | Min: 0 | Max: 4294967295
    sdwan_member: int
    
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
class FabricVpnAdvertisedsubnetsObject:
    """Typed object for advertised-subnets table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967294
    id: int
    # Network prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Access policy direction. | Default: inbound
    access: Literal["inbound", "bidirectional"]
    # Underlying BGP network. | Default: 0 | Min: 0 | Max: 4294967295
    bgp_network: int
    # Underlying firewall address. | MaxLen: 79
    firewall_address: str
    # Underlying policies. | Min: 0 | Max: 4294967295
    policies: int
    
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
class FabricVpnResponse(TypedDict):
    """
    Type hints for system/fabric_vpn API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable Fabric VPN. | Default: disable
    sync_mode: Literal["enable", "disable"]  # Setting synchronized by fabric or manual. | Default: enable
    branch_name: str  # Branch name. | MaxLen: 35
    policy_rule: Literal["health-check", "manual", "auto"]  # Policy creation rule. | Default: health-check
    vpn_role: Literal["hub", "spoke"]  # Fabric VPN role. | Default: hub
    overlays: list[FabricVpnOverlaysItem]  # Local overlay interfaces table.
    advertised_subnets: list[FabricVpnAdvertisedsubnetsItem]  # Local advertised subnets.
    loopback_address_block: str  # IPv4 address and subnet mask for hub's loopback ad | Default: 0.0.0.0 0.0.0.0
    loopback_interface: str  # Loopback interface. | MaxLen: 15
    loopback_advertised_subnet: int  # Loopback advertised subnet reference. | Default: 0 | Min: 0 | Max: 4294967295
    psksecret: str  # Pre-shared secret for ADVPN.
    bgp_as: str  # BGP Router AS number, asplain/asdot/asdot+ format.
    sdwan_zone: str  # Reference to created SD-WAN zone. | MaxLen: 35
    health_checks: list[dict[str, Any]]  # Underlying health checks. | MaxLen: 35


@final
class FabricVpnObject:
    """Typed FortiObject for system/fabric_vpn with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable Fabric VPN. | Default: disable
    status: Literal["enable", "disable"]
    # Setting synchronized by fabric or manual. | Default: enable
    sync_mode: Literal["enable", "disable"]
    # Branch name. | MaxLen: 35
    branch_name: str
    # Policy creation rule. | Default: health-check
    policy_rule: Literal["health-check", "manual", "auto"]
    # Fabric VPN role. | Default: hub
    vpn_role: Literal["hub", "spoke"]
    # Local overlay interfaces table.
    overlays: list[FabricVpnOverlaysObject]
    # Local advertised subnets.
    advertised_subnets: list[FabricVpnAdvertisedsubnetsObject]
    # IPv4 address and subnet mask for hub's loopback address, syn | Default: 0.0.0.0 0.0.0.0
    loopback_address_block: str
    # Loopback interface. | MaxLen: 15
    loopback_interface: str
    # Loopback advertised subnet reference. | Default: 0 | Min: 0 | Max: 4294967295
    loopback_advertised_subnet: int
    # Pre-shared secret for ADVPN.
    psksecret: str
    # BGP Router AS number, asplain/asdot/asdot+ format.
    bgp_as: str
    # Reference to created SD-WAN zone. | MaxLen: 35
    sdwan_zone: str
    # Underlying health checks. | MaxLen: 35
    health_checks: list[dict[str, Any]]
    
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
    def to_dict(self) -> FabricVpnPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FabricVpn:
    """
    Setup for self orchestrated fabric auto discovery VPN.
    
    Path: system/fabric_vpn
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject: ...
    
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
    ) -> FabricVpnObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FabricVpnObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FabricVpnPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sync_mode: Literal["enable", "disable"] | None = ...,
        branch_name: str | None = ...,
        policy_rule: Literal["health-check", "manual", "auto"] | None = ...,
        vpn_role: Literal["hub", "spoke"] | None = ...,
        overlays: str | list[str] | list[dict[str, Any]] | None = ...,
        advertised_subnets: str | list[str] | list[dict[str, Any]] | None = ...,
        loopback_address_block: str | None = ...,
        loopback_interface: str | None = ...,
        loopback_advertised_subnet: int | None = ...,
        psksecret: str | None = ...,
        bgp_as: str | None = ...,
        sdwan_zone: str | None = ...,
        health_checks: str | list[str] | None = ...,
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
    "FabricVpn",
    "FabricVpnPayload",
    "FabricVpnResponse",
    "FabricVpnObject",
]
from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ResourceLimitsPayload(TypedDict, total=False):
    """
    Type hints for system/resource_limits payload fields.
    
    Configure resource limits.
    
    **Usage:**
        payload: ResourceLimitsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    session: int  # Maximum number of sessions. | Min: 0 | Max: 4294967295
    ipsec_phase1: int  # Maximum number of VPN IPsec phase1 tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase2: int  # Maximum number of VPN IPsec phase2 tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase1_interface: int  # Maximum number of VPN IPsec phase1 interface tunne | Min: 0 | Max: 4294967295
    ipsec_phase2_interface: int  # Maximum number of VPN IPsec phase2 interface tunne | Min: 0 | Max: 4294967295
    dialup_tunnel: int  # Maximum number of dial-up tunnels. | Min: 0 | Max: 4294967295
    firewall_policy: int  # Maximum number of firewall policies | Min: 0 | Max: 4294967295
    firewall_address: int  # Maximum number of firewall addresses | Min: 0 | Max: 4294967295
    firewall_addrgrp: int  # Maximum number of firewall address groups | Min: 0 | Max: 4294967295
    custom_service: int  # Maximum number of firewall custom services. | Min: 0 | Max: 4294967295
    service_group: int  # Maximum number of firewall service groups. | Min: 0 | Max: 4294967295
    onetime_schedule: int  # Maximum number of firewall one-time schedules. | Min: 0 | Max: 4294967295
    recurring_schedule: int  # Maximum number of firewall recurring schedules. | Min: 0 | Max: 4294967295
    user: int  # Maximum number of local users. | Min: 0 | Max: 4294967295
    user_group: int  # Maximum number of user groups. | Min: 0 | Max: 4294967295
    sslvpn: int  # Maximum number of Agentless VPN. | Min: 0 | Max: 4294967295
    proxy: int  # Maximum number of concurrent proxy users. | Min: 0 | Max: 4294967295
    log_disk_quota: int  # Log disk quota in megabytes (MB). | Default: 0 | Min: 0 | Max: 4294967295

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ResourceLimitsResponse(TypedDict):
    """
    Type hints for system/resource_limits API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    session: int  # Maximum number of sessions. | Min: 0 | Max: 4294967295
    ipsec_phase1: int  # Maximum number of VPN IPsec phase1 tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase2: int  # Maximum number of VPN IPsec phase2 tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase1_interface: int  # Maximum number of VPN IPsec phase1 interface tunne | Min: 0 | Max: 4294967295
    ipsec_phase2_interface: int  # Maximum number of VPN IPsec phase2 interface tunne | Min: 0 | Max: 4294967295
    dialup_tunnel: int  # Maximum number of dial-up tunnels. | Min: 0 | Max: 4294967295
    firewall_policy: int  # Maximum number of firewall policies | Min: 0 | Max: 4294967295
    firewall_address: int  # Maximum number of firewall addresses | Min: 0 | Max: 4294967295
    firewall_addrgrp: int  # Maximum number of firewall address groups | Min: 0 | Max: 4294967295
    custom_service: int  # Maximum number of firewall custom services. | Min: 0 | Max: 4294967295
    service_group: int  # Maximum number of firewall service groups. | Min: 0 | Max: 4294967295
    onetime_schedule: int  # Maximum number of firewall one-time schedules. | Min: 0 | Max: 4294967295
    recurring_schedule: int  # Maximum number of firewall recurring schedules. | Min: 0 | Max: 4294967295
    user: int  # Maximum number of local users. | Min: 0 | Max: 4294967295
    user_group: int  # Maximum number of user groups. | Min: 0 | Max: 4294967295
    sslvpn: int  # Maximum number of Agentless VPN. | Min: 0 | Max: 4294967295
    proxy: int  # Maximum number of concurrent proxy users. | Min: 0 | Max: 4294967295
    log_disk_quota: int  # Log disk quota in megabytes (MB). | Default: 0 | Min: 0 | Max: 4294967295


@final
class ResourceLimitsObject:
    """Typed FortiObject for system/resource_limits with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Maximum number of sessions. | Min: 0 | Max: 4294967295
    session: int
    # Maximum number of VPN IPsec phase1 tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase1: int
    # Maximum number of VPN IPsec phase2 tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase2: int
    # Maximum number of VPN IPsec phase1 interface tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase1_interface: int
    # Maximum number of VPN IPsec phase2 interface tunnels. | Min: 0 | Max: 4294967295
    ipsec_phase2_interface: int
    # Maximum number of dial-up tunnels. | Min: 0 | Max: 4294967295
    dialup_tunnel: int
    # Maximum number of firewall policies | Min: 0 | Max: 4294967295
    firewall_policy: int
    # Maximum number of firewall addresses (IPv4, IPv6, multicast) | Min: 0 | Max: 4294967295
    firewall_address: int
    # Maximum number of firewall address groups (IPv4, IPv6). | Min: 0 | Max: 4294967295
    firewall_addrgrp: int
    # Maximum number of firewall custom services. | Min: 0 | Max: 4294967295
    custom_service: int
    # Maximum number of firewall service groups. | Min: 0 | Max: 4294967295
    service_group: int
    # Maximum number of firewall one-time schedules. | Min: 0 | Max: 4294967295
    onetime_schedule: int
    # Maximum number of firewall recurring schedules. | Min: 0 | Max: 4294967295
    recurring_schedule: int
    # Maximum number of local users. | Min: 0 | Max: 4294967295
    user: int
    # Maximum number of user groups. | Min: 0 | Max: 4294967295
    user_group: int
    # Maximum number of Agentless VPN. | Min: 0 | Max: 4294967295
    sslvpn: int
    # Maximum number of concurrent proxy users. | Min: 0 | Max: 4294967295
    proxy: int
    # Log disk quota in megabytes (MB). | Default: 0 | Min: 0 | Max: 4294967295
    log_disk_quota: int
    
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
    def to_dict(self) -> ResourceLimitsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ResourceLimits:
    """
    Configure resource limits.
    
    Path: system/resource_limits
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject: ...
    
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
    ) -> ResourceLimitsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ResourceLimitsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ResourceLimitsPayload | None = ...,
        session: int | None = ...,
        ipsec_phase1: int | None = ...,
        ipsec_phase2: int | None = ...,
        ipsec_phase1_interface: int | None = ...,
        ipsec_phase2_interface: int | None = ...,
        dialup_tunnel: int | None = ...,
        firewall_policy: int | None = ...,
        firewall_address: int | None = ...,
        firewall_addrgrp: int | None = ...,
        custom_service: int | None = ...,
        service_group: int | None = ...,
        onetime_schedule: int | None = ...,
        recurring_schedule: int | None = ...,
        user: int | None = ...,
        user_group: int | None = ...,
        sslvpn: int | None = ...,
        proxy: int | None = ...,
        log_disk_quota: int | None = ...,
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
    "ResourceLimits",
    "ResourceLimitsPayload",
    "ResourceLimitsResponse",
    "ResourceLimitsObject",
]
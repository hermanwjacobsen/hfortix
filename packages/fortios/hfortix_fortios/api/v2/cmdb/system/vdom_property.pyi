from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class VdomPropertyPayload(TypedDict, total=False):
    """
    Type hints for system/vdom_property payload fields.
    
    Configure VDOM property.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.vdom.VdomEndpoint` (via: name)

    **Usage:**
        payload: VdomPropertyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # VDOM name. | MaxLen: 31
    description: str  # Description. | MaxLen: 127
    snmp_index: int  # Permanent SNMP Index of the virtual domain | Default: 0 | Min: 1 | Max: 2147483647
    session: list[dict[str, Any]]  # Maximum guaranteed number of sessions.
    ipsec_phase1: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase 1 tun
    ipsec_phase2: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase 2 tun
    ipsec_phase1_interface: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase1 inte
    ipsec_phase2_interface: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase2 inte
    dialup_tunnel: list[dict[str, Any]]  # Maximum guaranteed number of dial-up tunnels.
    firewall_policy: list[dict[str, Any]]  # Maximum guaranteed number of firewall policies
    firewall_address: list[dict[str, Any]]  # Maximum guaranteed number of firewall addresses
    firewall_addrgrp: list[dict[str, Any]]  # Maximum guaranteed number of firewall address grou
    custom_service: list[dict[str, Any]]  # Maximum guaranteed number of firewall custom servi
    service_group: list[dict[str, Any]]  # Maximum guaranteed number of firewall service grou
    onetime_schedule: list[dict[str, Any]]  # Maximum guaranteed number of firewall one-time sch
    recurring_schedule: list[dict[str, Any]]  # Maximum guaranteed number of firewall recurring sc
    user: list[dict[str, Any]]  # Maximum guaranteed number of local users.
    user_group: list[dict[str, Any]]  # Maximum guaranteed number of user groups.
    sslvpn: list[dict[str, Any]]  # Maximum guaranteed number of Agentless VPNs.
    proxy: list[dict[str, Any]]  # Maximum guaranteed number of concurrent proxy user
    log_disk_quota: list[dict[str, Any]]  # Log disk quota in megabytes (MB). Range depends on

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class VdomPropertyResponse(TypedDict):
    """
    Type hints for system/vdom_property API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # VDOM name. | MaxLen: 31
    description: str  # Description. | MaxLen: 127
    snmp_index: int  # Permanent SNMP Index of the virtual domain | Default: 0 | Min: 1 | Max: 2147483647
    session: list[dict[str, Any]]  # Maximum guaranteed number of sessions.
    ipsec_phase1: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase 1 tun
    ipsec_phase2: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase 2 tun
    ipsec_phase1_interface: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase1 inte
    ipsec_phase2_interface: list[dict[str, Any]]  # Maximum guaranteed number of VPN IPsec phase2 inte
    dialup_tunnel: list[dict[str, Any]]  # Maximum guaranteed number of dial-up tunnels.
    firewall_policy: list[dict[str, Any]]  # Maximum guaranteed number of firewall policies
    firewall_address: list[dict[str, Any]]  # Maximum guaranteed number of firewall addresses
    firewall_addrgrp: list[dict[str, Any]]  # Maximum guaranteed number of firewall address grou
    custom_service: list[dict[str, Any]]  # Maximum guaranteed number of firewall custom servi
    service_group: list[dict[str, Any]]  # Maximum guaranteed number of firewall service grou
    onetime_schedule: list[dict[str, Any]]  # Maximum guaranteed number of firewall one-time sch
    recurring_schedule: list[dict[str, Any]]  # Maximum guaranteed number of firewall recurring sc
    user: list[dict[str, Any]]  # Maximum guaranteed number of local users.
    user_group: list[dict[str, Any]]  # Maximum guaranteed number of user groups.
    sslvpn: list[dict[str, Any]]  # Maximum guaranteed number of Agentless VPNs.
    proxy: list[dict[str, Any]]  # Maximum guaranteed number of concurrent proxy user
    log_disk_quota: list[dict[str, Any]]  # Log disk quota in megabytes (MB). Range depends on


@final
class VdomPropertyObject:
    """Typed FortiObject for system/vdom_property with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VDOM name. | MaxLen: 31
    name: str
    # Description. | MaxLen: 127
    description: str
    # Permanent SNMP Index of the virtual domain (1 - 2147483647). | Default: 0 | Min: 1 | Max: 2147483647
    snmp_index: int
    # Maximum guaranteed number of sessions.
    session: list[dict[str, Any]]
    # Maximum guaranteed number of VPN IPsec phase 1 tunnels.
    ipsec_phase1: list[dict[str, Any]]
    # Maximum guaranteed number of VPN IPsec phase 2 tunnels.
    ipsec_phase2: list[dict[str, Any]]
    # Maximum guaranteed number of VPN IPsec phase1 interface tunn
    ipsec_phase1_interface: list[dict[str, Any]]
    # Maximum guaranteed number of VPN IPsec phase2 interface tunn
    ipsec_phase2_interface: list[dict[str, Any]]
    # Maximum guaranteed number of dial-up tunnels.
    dialup_tunnel: list[dict[str, Any]]
    # Maximum guaranteed number of firewall policies
    firewall_policy: list[dict[str, Any]]
    # Maximum guaranteed number of firewall addresses
    firewall_address: list[dict[str, Any]]
    # Maximum guaranteed number of firewall address groups
    firewall_addrgrp: list[dict[str, Any]]
    # Maximum guaranteed number of firewall custom services.
    custom_service: list[dict[str, Any]]
    # Maximum guaranteed number of firewall service groups.
    service_group: list[dict[str, Any]]
    # Maximum guaranteed number of firewall one-time schedules..
    onetime_schedule: list[dict[str, Any]]
    # Maximum guaranteed number of firewall recurring schedules.
    recurring_schedule: list[dict[str, Any]]
    # Maximum guaranteed number of local users.
    user: list[dict[str, Any]]
    # Maximum guaranteed number of user groups.
    user_group: list[dict[str, Any]]
    # Maximum guaranteed number of Agentless VPNs.
    sslvpn: list[dict[str, Any]]
    # Maximum guaranteed number of concurrent proxy users.
    proxy: list[dict[str, Any]]
    # Log disk quota in megabytes (MB). Range depends on how much
    log_disk_quota: list[dict[str, Any]]
    
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
    def to_dict(self) -> VdomPropertyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class VdomProperty:
    """
    Configure VDOM property.
    
    Path: system/vdom_property
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> list[VdomPropertyObject]: ...
    
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> list[VdomPropertyObject]: ...
    
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> VdomPropertyObject: ...
    
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
    ) -> list[VdomPropertyObject]: ...
    
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
    ) -> VdomPropertyObject | list[VdomPropertyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VdomPropertyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> VdomPropertyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
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
    ) -> VdomPropertyObject: ...
    
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
        payload_dict: VdomPropertyPayload | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        snmp_index: int | None = ...,
        session: str | list[str] | None = ...,
        ipsec_phase1: str | list[str] | None = ...,
        ipsec_phase2: str | list[str] | None = ...,
        ipsec_phase1_interface: str | list[str] | None = ...,
        ipsec_phase2_interface: str | list[str] | None = ...,
        dialup_tunnel: str | list[str] | None = ...,
        firewall_policy: str | list[str] | None = ...,
        firewall_address: str | list[str] | None = ...,
        firewall_addrgrp: str | list[str] | None = ...,
        custom_service: str | list[str] | None = ...,
        service_group: str | list[str] | None = ...,
        onetime_schedule: str | list[str] | None = ...,
        recurring_schedule: str | list[str] | None = ...,
        user: str | list[str] | None = ...,
        user_group: str | list[str] | None = ...,
        sslvpn: str | list[str] | None = ...,
        proxy: str | list[str] | None = ...,
        log_disk_quota: str | list[str] | None = ...,
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
    "VdomProperty",
    "VdomPropertyPayload",
    "VdomPropertyResponse",
    "VdomPropertyObject",
]
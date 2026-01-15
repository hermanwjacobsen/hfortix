from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class IppoolPayload(TypedDict, total=False):
    """
    Type hints for firewall/ippool payload fields.
    
    Configure IPv4 IP pools.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: arp-intf, associated-interface)

    **Usage:**
        payload: IppoolPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IP pool name. | MaxLen: 79
    type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"]  # IP pool type: overload, one-to-one, fixed-port-ran | Default: overload
    startip: str  # First IPv4 address (inclusive) in the range for th | Default: 0.0.0.0
    endip: str  # Final IPv4 address (inclusive) in the range for th | Default: 0.0.0.0
    startport: int  # First port number (inclusive) in the range for the | Default: 5117 | Min: 1024 | Max: 65535
    endport: int  # Final port number (inclusive) in the range for the | Default: 65533 | Min: 1024 | Max: 65535
    source_startip: str  # First IPv4 address (inclusive) in the range of the | Default: 0.0.0.0
    source_endip: str  # Final IPv4 address (inclusive) in the range of the | Default: 0.0.0.0
    block_size: int  # Number of addresses in a block | Default: 128 | Min: 64 | Max: 4096
    port_per_user: int  # Number of port for each user | Default: 0 | Min: 32 | Max: 60417
    num_blocks_per_user: int  # Number of addresses blocks that can be used by a u | Default: 8 | Min: 1 | Max: 128
    pba_timeout: int  # Port block allocation timeout (seconds). | Default: 30 | Min: 3 | Max: 86400
    pba_interim_log: int  # Port block allocation interim logging interval | Default: 0 | Min: 600 | Max: 86400
    permit_any_host: Literal["disable", "enable"]  # Enable/disable fullcone NAT. Accept UDP packets fr | Default: disable
    arp_reply: Literal["disable", "enable"]  # Enable/disable replying to ARP requests when an IP | Default: enable
    arp_intf: str  # Select an interface from available options that wi | MaxLen: 15
    associated_interface: str  # Associated interface name. | MaxLen: 15
    comments: str  # Comment. | MaxLen: 255
    nat64: Literal["disable", "enable"]  # Enable/disable NAT64. | Default: disable
    add_nat64_route: Literal["disable", "enable"]  # Enable/disable adding NAT64 route. | Default: enable
    source_prefix6: str  # Source IPv6 network to be translated | Default: ::/0
    client_prefix_length: int  # Subnet length of a single deterministic NAT64 clie | Default: 64 | Min: 1 | Max: 128
    tcp_session_quota: int  # Maximum number of concurrent TCP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    udp_session_quota: int  # Maximum number of concurrent UDP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    icmp_session_quota: int  # Maximum number of concurrent ICMP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    privileged_port_use_pba: Literal["disable", "enable"]  # Enable/disable selection of the external port from | Default: disable
    subnet_broadcast_in_ippool: Literal["disable"]  # Enable/disable inclusion of the subnetwork address

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class IppoolResponse(TypedDict):
    """
    Type hints for firewall/ippool API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IP pool name. | MaxLen: 79
    type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"]  # IP pool type: overload, one-to-one, fixed-port-ran | Default: overload
    startip: str  # First IPv4 address (inclusive) in the range for th | Default: 0.0.0.0
    endip: str  # Final IPv4 address (inclusive) in the range for th | Default: 0.0.0.0
    startport: int  # First port number (inclusive) in the range for the | Default: 5117 | Min: 1024 | Max: 65535
    endport: int  # Final port number (inclusive) in the range for the | Default: 65533 | Min: 1024 | Max: 65535
    source_startip: str  # First IPv4 address (inclusive) in the range of the | Default: 0.0.0.0
    source_endip: str  # Final IPv4 address (inclusive) in the range of the | Default: 0.0.0.0
    block_size: int  # Number of addresses in a block | Default: 128 | Min: 64 | Max: 4096
    port_per_user: int  # Number of port for each user | Default: 0 | Min: 32 | Max: 60417
    num_blocks_per_user: int  # Number of addresses blocks that can be used by a u | Default: 8 | Min: 1 | Max: 128
    pba_timeout: int  # Port block allocation timeout (seconds). | Default: 30 | Min: 3 | Max: 86400
    pba_interim_log: int  # Port block allocation interim logging interval | Default: 0 | Min: 600 | Max: 86400
    permit_any_host: Literal["disable", "enable"]  # Enable/disable fullcone NAT. Accept UDP packets fr | Default: disable
    arp_reply: Literal["disable", "enable"]  # Enable/disable replying to ARP requests when an IP | Default: enable
    arp_intf: str  # Select an interface from available options that wi | MaxLen: 15
    associated_interface: str  # Associated interface name. | MaxLen: 15
    comments: str  # Comment. | MaxLen: 255
    nat64: Literal["disable", "enable"]  # Enable/disable NAT64. | Default: disable
    add_nat64_route: Literal["disable", "enable"]  # Enable/disable adding NAT64 route. | Default: enable
    source_prefix6: str  # Source IPv6 network to be translated | Default: ::/0
    client_prefix_length: int  # Subnet length of a single deterministic NAT64 clie | Default: 64 | Min: 1 | Max: 128
    tcp_session_quota: int  # Maximum number of concurrent TCP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    udp_session_quota: int  # Maximum number of concurrent UDP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    icmp_session_quota: int  # Maximum number of concurrent ICMP sessions allowed | Default: 0 | Min: 0 | Max: 2097000
    privileged_port_use_pba: Literal["disable", "enable"]  # Enable/disable selection of the external port from | Default: disable
    subnet_broadcast_in_ippool: Literal["disable"]  # Enable/disable inclusion of the subnetwork address


@final
class IppoolObject:
    """Typed FortiObject for firewall/ippool with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IP pool name. | MaxLen: 79
    name: str
    # IP pool type: overload, one-to-one, fixed-port-range, port-b | Default: overload
    type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"]
    # First IPv4 address (inclusive) in the range for the address | Default: 0.0.0.0
    startip: str
    # Final IPv4 address (inclusive) in the range for the address | Default: 0.0.0.0
    endip: str
    # First port number (inclusive) in the range for the address p | Default: 5117 | Min: 1024 | Max: 65535
    startport: int
    # Final port number (inclusive) in the range for the address p | Default: 65533 | Min: 1024 | Max: 65535
    endport: int
    # First IPv4 address (inclusive) in the range of the source ad | Default: 0.0.0.0
    source_startip: str
    # Final IPv4 address (inclusive) in the range of the source ad | Default: 0.0.0.0
    source_endip: str
    # Number of addresses in a block (64 - 4096, default = 128). | Default: 128 | Min: 64 | Max: 4096
    block_size: int
    # Number of port for each user | Default: 0 | Min: 32 | Max: 60417
    port_per_user: int
    # Number of addresses blocks that can be used by a user | Default: 8 | Min: 1 | Max: 128
    num_blocks_per_user: int
    # Port block allocation timeout (seconds). | Default: 30 | Min: 3 | Max: 86400
    pba_timeout: int
    # Port block allocation interim logging interval | Default: 0 | Min: 600 | Max: 86400
    pba_interim_log: int
    # Enable/disable fullcone NAT. Accept UDP packets from any hos | Default: disable
    permit_any_host: Literal["disable", "enable"]
    # Enable/disable replying to ARP requests when an IP Pool is a | Default: enable
    arp_reply: Literal["disable", "enable"]
    # Select an interface from available options that will reply t | MaxLen: 15
    arp_intf: str
    # Associated interface name. | MaxLen: 15
    associated_interface: str
    # Comment. | MaxLen: 255
    comments: str
    # Enable/disable NAT64. | Default: disable
    nat64: Literal["disable", "enable"]
    # Enable/disable adding NAT64 route. | Default: enable
    add_nat64_route: Literal["disable", "enable"]
    # Source IPv6 network to be translated | Default: ::/0
    source_prefix6: str
    # Subnet length of a single deterministic NAT64 client | Default: 64 | Min: 1 | Max: 128
    client_prefix_length: int
    # Maximum number of concurrent TCP sessions allowed per client | Default: 0 | Min: 0 | Max: 2097000
    tcp_session_quota: int
    # Maximum number of concurrent UDP sessions allowed per client | Default: 0 | Min: 0 | Max: 2097000
    udp_session_quota: int
    # Maximum number of concurrent ICMP sessions allowed per clien | Default: 0 | Min: 0 | Max: 2097000
    icmp_session_quota: int
    # Enable/disable selection of the external port from the port | Default: disable
    privileged_port_use_pba: Literal["disable", "enable"]
    # Enable/disable inclusion of the subnetwork address and broad
    subnet_broadcast_in_ippool: Literal["disable"]
    
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
    def to_dict(self) -> IppoolPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Ippool:
    """
    Configure IPv4 IP pools.
    
    Path: firewall/ippool
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
    ) -> IppoolObject: ...
    
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
    ) -> IppoolObject: ...
    
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
    ) -> list[IppoolObject]: ...
    
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
    ) -> IppoolObject: ...
    
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
    ) -> IppoolObject: ...
    
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
    ) -> list[IppoolObject]: ...
    
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
    ) -> IppoolObject: ...
    
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
    ) -> IppoolObject: ...
    
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
    ) -> list[IppoolObject]: ...
    
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
    ) -> IppoolObject | list[IppoolObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> IppoolObject: ...
    
    @overload
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> IppoolObject: ...
    
    @overload
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
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
    ) -> IppoolObject: ...
    
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
        payload_dict: IppoolPayload | None = ...,
        name: str | None = ...,
        type: Literal["overload", "one-to-one", "fixed-port-range", "port-block-allocation"] | None = ...,
        startip: str | None = ...,
        endip: str | None = ...,
        startport: int | None = ...,
        endport: int | None = ...,
        source_startip: str | None = ...,
        source_endip: str | None = ...,
        block_size: int | None = ...,
        port_per_user: int | None = ...,
        num_blocks_per_user: int | None = ...,
        pba_timeout: int | None = ...,
        pba_interim_log: int | None = ...,
        permit_any_host: Literal["disable", "enable"] | None = ...,
        arp_reply: Literal["disable", "enable"] | None = ...,
        arp_intf: str | None = ...,
        associated_interface: str | None = ...,
        comments: str | None = ...,
        nat64: Literal["disable", "enable"] | None = ...,
        add_nat64_route: Literal["disable", "enable"] | None = ...,
        source_prefix6: str | None = ...,
        client_prefix_length: int | None = ...,
        tcp_session_quota: int | None = ...,
        udp_session_quota: int | None = ...,
        icmp_session_quota: int | None = ...,
        privileged_port_use_pba: Literal["disable", "enable"] | None = ...,
        subnet_broadcast_in_ippool: Literal["disable"] | None = ...,
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
    "Ippool",
    "IppoolPayload",
    "IppoolResponse",
    "IppoolObject",
]
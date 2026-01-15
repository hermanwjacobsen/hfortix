from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ServerPayload(TypedDict, total=False):
    """
    Type hints for system/dhcp6/server payload fields.
    
    Configure DHCPv6 servers.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, upstream-interface)

    **Usage:**
        payload: ServerPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["disable", "enable"]  # Enable/disable this DHCPv6 configuration. | Default: enable
    rapid_commit: Literal["disable", "enable"]  # Enable/disable allow/disallow rapid commit. | Default: disable
    lease_time: int  # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 300 | Max: 8640000
    dns_service: Literal["delegated", "default", "specify"]  # Options for assigning DNS servers to DHCPv6 client | Default: specify
    dns_search_list: Literal["delegated", "specify"]  # DNS search list options. | Default: specify
    dns_server1: str  # DNS server 1. | Default: ::
    dns_server2: str  # DNS server 2. | Default: ::
    dns_server3: str  # DNS server 3. | Default: ::
    dns_server4: str  # DNS server 4. | Default: ::
    domain: str  # Domain name suffix for the IP addresses that the D | MaxLen: 35
    subnet: str  # Subnet or subnet-id if the IP mode is delegated. | Default: ::/0
    interface: str  # DHCP server can assign IP configurations to client | MaxLen: 15
    delegated_prefix_route: Literal["disable", "enable"]  # Enable/disable automatically adding of routing for | Default: disable
    options: list[dict[str, Any]]  # DHCPv6 options.
    upstream_interface: str  # Interface name from where delegated information is | MaxLen: 15
    delegated_prefix_iaid: int  # IAID of obtained delegated-prefix from the upstrea | Default: 0 | Min: 0 | Max: 4294967295
    ip_mode: Literal["range", "delegated"]  # Method used to assign client IP. | Default: range
    prefix_mode: Literal["dhcp6", "ra"]  # Assigning a prefix from a DHCPv6 client or RA. | Default: dhcp6
    prefix_range: list[dict[str, Any]]  # DHCP prefix configuration.
    ip_range: list[dict[str, Any]]  # DHCP IP range configuration.

# Nested TypedDicts for table field children (dict mode)

class ServerOptionsItem(TypedDict):
    """Type hints for options table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    code: int  # DHCPv6 option code. | Default: 0 | Min: 0 | Max: 255
    type: Literal["hex", "string", "ip6", "fqdn"]  # DHCPv6 option type. | Default: hex
    value: str  # DHCPv6 option value | MaxLen: 312
    ip6: str  # DHCP option IP6s.
    vci_match: Literal["disable", "enable"]  # Enable/disable vendor class option matching. When | Default: disable
    vci_string: str  # One or more VCI strings in quotes separated by spa


class ServerPrefixrangeItem(TypedDict):
    """Type hints for prefix-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    start_prefix: str  # Start of prefix range. | Default: ::
    end_prefix: str  # End of prefix range. | Default: ::
    prefix_length: int  # Prefix length. | Default: 0 | Min: 1 | Max: 128


class ServerIprangeItem(TypedDict):
    """Type hints for ip-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    start_ip: str  # Start of IP range. | Default: ::
    end_ip: str  # End of IP range. | Default: ::
    vci_match: Literal["disable", "enable"]  # Enable/disable vendor class option matching. When | Default: disable
    vci_string: str  # One or more VCI strings in quotes separated by spa


# Nested classes for table field children (object mode)

@final
class ServerOptionsObject:
    """Typed object for options table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # DHCPv6 option code. | Default: 0 | Min: 0 | Max: 255
    code: int
    # DHCPv6 option type. | Default: hex
    type: Literal["hex", "string", "ip6", "fqdn"]
    # DHCPv6 option value (hexadecimal value must be even). | MaxLen: 312
    value: str
    # DHCP option IP6s.
    ip6: str
    # Enable/disable vendor class option matching. When enabled on | Default: disable
    vci_match: Literal["disable", "enable"]
    # One or more VCI strings in quotes separated by spaces.
    vci_string: str
    
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
class ServerPrefixrangeObject:
    """Typed object for prefix-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Start of prefix range. | Default: ::
    start_prefix: str
    # End of prefix range. | Default: ::
    end_prefix: str
    # Prefix length. | Default: 0 | Min: 1 | Max: 128
    prefix_length: int
    
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
class ServerIprangeObject:
    """Typed object for ip-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Start of IP range. | Default: ::
    start_ip: str
    # End of IP range. | Default: ::
    end_ip: str
    # Enable/disable vendor class option matching. When enabled on | Default: disable
    vci_match: Literal["disable", "enable"]
    # One or more VCI strings in quotes separated by spaces.
    vci_string: str
    
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
class ServerResponse(TypedDict):
    """
    Type hints for system/dhcp6/server API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["disable", "enable"]  # Enable/disable this DHCPv6 configuration. | Default: enable
    rapid_commit: Literal["disable", "enable"]  # Enable/disable allow/disallow rapid commit. | Default: disable
    lease_time: int  # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 300 | Max: 8640000
    dns_service: Literal["delegated", "default", "specify"]  # Options for assigning DNS servers to DHCPv6 client | Default: specify
    dns_search_list: Literal["delegated", "specify"]  # DNS search list options. | Default: specify
    dns_server1: str  # DNS server 1. | Default: ::
    dns_server2: str  # DNS server 2. | Default: ::
    dns_server3: str  # DNS server 3. | Default: ::
    dns_server4: str  # DNS server 4. | Default: ::
    domain: str  # Domain name suffix for the IP addresses that the D | MaxLen: 35
    subnet: str  # Subnet or subnet-id if the IP mode is delegated. | Default: ::/0
    interface: str  # DHCP server can assign IP configurations to client | MaxLen: 15
    delegated_prefix_route: Literal["disable", "enable"]  # Enable/disable automatically adding of routing for | Default: disable
    options: list[ServerOptionsItem]  # DHCPv6 options.
    upstream_interface: str  # Interface name from where delegated information is | MaxLen: 15
    delegated_prefix_iaid: int  # IAID of obtained delegated-prefix from the upstrea | Default: 0 | Min: 0 | Max: 4294967295
    ip_mode: Literal["range", "delegated"]  # Method used to assign client IP. | Default: range
    prefix_mode: Literal["dhcp6", "ra"]  # Assigning a prefix from a DHCPv6 client or RA. | Default: dhcp6
    prefix_range: list[ServerPrefixrangeItem]  # DHCP prefix configuration.
    ip_range: list[ServerIprangeItem]  # DHCP IP range configuration.


@final
class ServerObject:
    """Typed FortiObject for system/dhcp6/server with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Enable/disable this DHCPv6 configuration. | Default: enable
    status: Literal["disable", "enable"]
    # Enable/disable allow/disallow rapid commit. | Default: disable
    rapid_commit: Literal["disable", "enable"]
    # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 300 | Max: 8640000
    lease_time: int
    # Options for assigning DNS servers to DHCPv6 clients. | Default: specify
    dns_service: Literal["delegated", "default", "specify"]
    # DNS search list options. | Default: specify
    dns_search_list: Literal["delegated", "specify"]
    # DNS server 1. | Default: ::
    dns_server1: str
    # DNS server 2. | Default: ::
    dns_server2: str
    # DNS server 3. | Default: ::
    dns_server3: str
    # DNS server 4. | Default: ::
    dns_server4: str
    # Domain name suffix for the IP addresses that the DHCP server | MaxLen: 35
    domain: str
    # Subnet or subnet-id if the IP mode is delegated. | Default: ::/0
    subnet: str
    # DHCP server can assign IP configurations to clients connecte | MaxLen: 15
    interface: str
    # Enable/disable automatically adding of routing for delegated | Default: disable
    delegated_prefix_route: Literal["disable", "enable"]
    # DHCPv6 options.
    options: list[ServerOptionsObject]
    # Interface name from where delegated information is provided. | MaxLen: 15
    upstream_interface: str
    # IAID of obtained delegated-prefix from the upstream interfac | Default: 0 | Min: 0 | Max: 4294967295
    delegated_prefix_iaid: int
    # Method used to assign client IP. | Default: range
    ip_mode: Literal["range", "delegated"]
    # Assigning a prefix from a DHCPv6 client or RA. | Default: dhcp6
    prefix_mode: Literal["dhcp6", "ra"]
    # DHCP prefix configuration.
    prefix_range: list[ServerPrefixrangeObject]
    # DHCP IP range configuration.
    ip_range: list[ServerIprangeObject]
    
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
    def to_dict(self) -> ServerPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Server:
    """
    Configure DHCPv6 servers.
    
    Path: system/dhcp6/server
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
    ) -> ServerObject: ...
    
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
    ) -> ServerObject: ...
    
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
    ) -> FortiObjectList[ServerObject]: ...
    
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
    ) -> ServerObject: ...
    
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
    ) -> ServerObject: ...
    
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
    ) -> FortiObjectList[ServerObject]: ...
    
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
    ) -> ServerObject: ...
    
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
    ) -> ServerObject: ...
    
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
    ) -> FortiObjectList[ServerObject]: ...
    
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
    ) -> ServerObject | list[ServerObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ServerObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ServerObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        id: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ServerObject: ...
    
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
        payload_dict: ServerPayload | None = ...,
        id: int | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        rapid_commit: Literal["disable", "enable"] | None = ...,
        lease_time: int | None = ...,
        dns_service: Literal["delegated", "default", "specify"] | None = ...,
        dns_search_list: Literal["delegated", "specify"] | None = ...,
        dns_server1: str | None = ...,
        dns_server2: str | None = ...,
        dns_server3: str | None = ...,
        dns_server4: str | None = ...,
        domain: str | None = ...,
        subnet: str | None = ...,
        interface: str | None = ...,
        delegated_prefix_route: Literal["disable", "enable"] | None = ...,
        options: str | list[str] | list[dict[str, Any]] | None = ...,
        upstream_interface: str | None = ...,
        delegated_prefix_iaid: int | None = ...,
        ip_mode: Literal["range", "delegated"] | None = ...,
        prefix_mode: Literal["dhcp6", "ra"] | None = ...,
        prefix_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_range: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Server",
    "ServerPayload",
    "ServerResponse",
    "ServerObject",
]
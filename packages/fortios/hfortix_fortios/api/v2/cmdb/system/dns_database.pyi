from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class DnsDatabasePayload(TypedDict, total=False):
    """
    Type hints for system/dns_database payload fields.
    
    Configure DNS databases.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)

    **Usage:**
        payload: DnsDatabasePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Zone name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this DNS zone. | Default: enable
    domain: str  # Domain name. | MaxLen: 255
    allow_transfer: list[dict[str, Any]]  # DNS zone transfer IP address list.
    type: Literal["primary", "secondary"]  # Zone type | Default: primary
    view: Literal["shadow", "public", "shadow-ztna", "proxy"]  # Zone view | Default: shadow
    ip_primary: str  # IP address of primary DNS server. Entries in this | Default: 0.0.0.0
    primary_name: str  # Domain name of the default DNS server for this zon | Default: dns | MaxLen: 255
    contact: str  # Email address of the administrator for this zone. | Default: host | MaxLen: 255
    ttl: int  # Default time-to-live value for the entries of this | Default: 86400 | Min: 0 | Max: 2147483647
    authoritative: Literal["enable", "disable"]  # Enable/disable authoritative zone. | Default: enable
    forwarder: list[dict[str, Any]]  # DNS zone forwarder IP address list.
    forwarder6: str  # Forwarder IPv6 address. | Default: ::
    source_ip: str  # Source IP for forwarding to DNS server. | Default: 0.0.0.0
    source_ip6: str  # IPv6 source IP address for forwarding to DNS serve | Default: ::
    source_ip_interface: str  # IP address of the specified interface as the sourc | MaxLen: 15
    rr_max: int  # Maximum number of resource records | Default: 16384 | Min: 10 | Max: 65536
    dns_entry: list[dict[str, Any]]  # DNS entry.
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511

# Nested TypedDicts for table field children (dict mode)

class DnsDatabaseDnsentryItem(TypedDict):
    """Type hints for dns-entry table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # DNS entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    status: Literal["enable", "disable"]  # Enable/disable resource record status. | Default: enable
    type: Literal["A", "NS", "CNAME", "MX", "AAAA", "PTR", "PTR_V6"]  # Resource record type. | Default: A
    ttl: int  # Time-to-live for this entry | Default: 0 | Min: 0 | Max: 2147483647
    preference: int  # DNS entry preference | Default: 10 | Min: 0 | Max: 65535
    ip: str  # IPv4 address of the host. | Default: 0.0.0.0
    ipv6: str  # IPv6 address of the host. | Default: ::
    hostname: str  # Name of the host. | MaxLen: 255
    canonical_name: str  # Canonical name of the host. | MaxLen: 255


# Nested classes for table field children (object mode)

@final
class DnsDatabaseDnsentryObject:
    """Typed object for dns-entry table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DNS entry ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Enable/disable resource record status. | Default: enable
    status: Literal["enable", "disable"]
    # Resource record type. | Default: A
    type: Literal["A", "NS", "CNAME", "MX", "AAAA", "PTR", "PTR_V6"]
    # Time-to-live for this entry | Default: 0 | Min: 0 | Max: 2147483647
    ttl: int
    # DNS entry preference | Default: 10 | Min: 0 | Max: 65535
    preference: int
    # IPv4 address of the host. | Default: 0.0.0.0
    ip: str
    # IPv6 address of the host. | Default: ::
    ipv6: str
    # Name of the host. | MaxLen: 255
    hostname: str
    # Canonical name of the host. | MaxLen: 255
    canonical_name: str
    
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
class DnsDatabaseResponse(TypedDict):
    """
    Type hints for system/dns_database API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Zone name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable this DNS zone. | Default: enable
    domain: str  # Domain name. | MaxLen: 255
    allow_transfer: list[dict[str, Any]]  # DNS zone transfer IP address list.
    type: Literal["primary", "secondary"]  # Zone type | Default: primary
    view: Literal["shadow", "public", "shadow-ztna", "proxy"]  # Zone view | Default: shadow
    ip_primary: str  # IP address of primary DNS server. Entries in this | Default: 0.0.0.0
    primary_name: str  # Domain name of the default DNS server for this zon | Default: dns | MaxLen: 255
    contact: str  # Email address of the administrator for this zone. | Default: host | MaxLen: 255
    ttl: int  # Default time-to-live value for the entries of this | Default: 86400 | Min: 0 | Max: 2147483647
    authoritative: Literal["enable", "disable"]  # Enable/disable authoritative zone. | Default: enable
    forwarder: list[dict[str, Any]]  # DNS zone forwarder IP address list.
    forwarder6: str  # Forwarder IPv6 address. | Default: ::
    source_ip: str  # Source IP for forwarding to DNS server. | Default: 0.0.0.0
    source_ip6: str  # IPv6 source IP address for forwarding to DNS serve | Default: ::
    source_ip_interface: str  # IP address of the specified interface as the sourc | MaxLen: 15
    rr_max: int  # Maximum number of resource records | Default: 16384 | Min: 10 | Max: 65536
    dns_entry: list[DnsDatabaseDnsentryItem]  # DNS entry.
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511


@final
class DnsDatabaseObject:
    """Typed FortiObject for system/dns_database with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Zone name. | MaxLen: 35
    name: str
    # Enable/disable this DNS zone. | Default: enable
    status: Literal["enable", "disable"]
    # Domain name. | MaxLen: 255
    domain: str
    # DNS zone transfer IP address list.
    allow_transfer: list[dict[str, Any]]
    # Zone type | Default: primary
    type: Literal["primary", "secondary"]
    # Zone view | Default: shadow
    view: Literal["shadow", "public", "shadow-ztna", "proxy"]
    # IP address of primary DNS server. Entries in this primary DN | Default: 0.0.0.0
    ip_primary: str
    # Domain name of the default DNS server for this zone. | Default: dns | MaxLen: 255
    primary_name: str
    # Email address of the administrator for this zone. You can sp | Default: host | MaxLen: 255
    contact: str
    # Default time-to-live value for the entries of this DNS zone | Default: 86400 | Min: 0 | Max: 2147483647
    ttl: int
    # Enable/disable authoritative zone. | Default: enable
    authoritative: Literal["enable", "disable"]
    # DNS zone forwarder IP address list.
    forwarder: list[dict[str, Any]]
    # Forwarder IPv6 address. | Default: ::
    forwarder6: str
    # Source IP for forwarding to DNS server. | Default: 0.0.0.0
    source_ip: str
    # IPv6 source IP address for forwarding to DNS server. | Default: ::
    source_ip6: str
    # IP address of the specified interface as the source IP addre | MaxLen: 15
    source_ip_interface: str
    # Maximum number of resource records | Default: 16384 | Min: 10 | Max: 65536
    rr_max: int
    # DNS entry.
    dns_entry: list[DnsDatabaseDnsentryObject]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    
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
    def to_dict(self) -> DnsDatabasePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class DnsDatabase:
    """
    Configure DNS databases.
    
    Path: system/dns_database
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> FortiObjectList[DnsDatabaseObject]: ...
    
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> FortiObjectList[DnsDatabaseObject]: ...
    
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> DnsDatabaseObject: ...
    
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
    ) -> FortiObjectList[DnsDatabaseObject]: ...
    
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
    ) -> DnsDatabaseObject | list[DnsDatabaseObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> DnsDatabaseObject: ...
    
    @overload
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> DnsDatabaseObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> DnsDatabaseObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: DnsDatabasePayload | None = ...,
        name: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        domain: str | None = ...,
        allow_transfer: str | list[str] | None = ...,
        type: Literal["primary", "secondary"] | None = ...,
        view: Literal["shadow", "public", "shadow-ztna", "proxy"] | None = ...,
        ip_primary: str | None = ...,
        primary_name: str | None = ...,
        contact: str | None = ...,
        ttl: int | None = ...,
        authoritative: Literal["enable", "disable"] | None = ...,
        forwarder: str | list[str] | None = ...,
        forwarder6: str | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        source_ip_interface: str | None = ...,
        rr_max: int | None = ...,
        dns_entry: str | list[str] | list[dict[str, Any]] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
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
    "DnsDatabase",
    "DnsDatabasePayload",
    "DnsDatabaseResponse",
    "DnsDatabaseObject",
]
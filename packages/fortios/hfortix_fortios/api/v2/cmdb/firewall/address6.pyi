from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Address6Payload(TypedDict, total=False):
    """
    Type hints for firewall/address6 payload fields.
    
    Configure IPv6 firewall addresses.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address6-template.Address6TemplateEndpoint` (via: template)
        - :class:`~.system.sdn-connector.SdnConnectorEndpoint` (via: sdn)

    **Usage:**
        payload: Address6Payload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Address name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"]  # Type of IPv6 address object (default = ipprefix). | Default: ipprefix
    route_tag: int  # route-tag address. | Default: 0 | Min: 1 | Max: 4294967295
    macaddr: list[dict[str, Any]]  # Multiple MAC address ranges.
    sdn: str  # SDN. | MaxLen: 35
    ip6: str  # IPv6 address prefix | Default: ::/0
    wildcard: str  # IPv6 address and wildcard netmask. | Default: :: ::
    start_ip: str  # First IP address (inclusive) in the range for the | Default: ::
    end_ip: str  # Final IP address (inclusive) in the range for the | Default: ::
    fqdn: str  # Fully qualified domain name. | MaxLen: 255
    country: str  # IPv6 addresses associated to a specific country. | MaxLen: 2
    cache_ttl: int  # Minimal TTL of individual IPv6 addresses in FQDN c | Default: 0 | Min: 0 | Max: 86400
    color: int  # Integer value to determine the color of the icon i | Default: 0 | Min: 0 | Max: 32
    obj_id: str  # Object ID for NSX. | MaxLen: 255
    tagging: list[dict[str, Any]]  # Config object tagging.
    comment: str  # Comment. | MaxLen: 255
    template: str  # IPv6 address template. | MaxLen: 63
    subnet_segment: list[dict[str, Any]]  # IPv6 subnet segments.
    host_type: Literal["any", "specific"]  # Host type. | Default: any
    host: str  # Host Address. | Default: ::
    tenant: str  # Tenant. | MaxLen: 35
    epg_name: str  # Endpoint group name. | MaxLen: 255
    sdn_tag: str  # SDN Tag. | MaxLen: 15
    filter: str  # Match criteria filter. | MaxLen: 2047
    list: list[dict[str, Any]]  # IP address list.
    sdn_addr_type: Literal["private", "public", "all"]  # Type of addresses to collect. | Default: private
    passive_fqdn_learning: Literal["disable", "enable"]  # Enable/disable passive learning of FQDNs.  When en | Default: enable
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class Address6MacaddrItem(TypedDict):
    """Type hints for macaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    macaddr: str  # MAC address ranges <start>[-<end>] separated by sp | MaxLen: 127


class Address6TaggingItem(TypedDict):
    """Type hints for tagging table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Tagging entry name. | MaxLen: 63
    category: str  # Tag category. | MaxLen: 63
    tags: str  # Tags.


class Address6SubnetsegmentItem(TypedDict):
    """Type hints for subnet-segment table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Name. | MaxLen: 63
    type: Literal["any", "specific"]  # Subnet segment type. | Default: any
    value: str  # Subnet segment value. | MaxLen: 35


class Address6ListItem(TypedDict):
    """Type hints for list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip: str  # IP. | MaxLen: 89


# Nested classes for table field children (object mode)

@final
class Address6MacaddrObject:
    """Typed object for macaddr table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # MAC address ranges <start>[-<end>] separated by space. | MaxLen: 127
    macaddr: str
    
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
class Address6TaggingObject:
    """Typed object for tagging table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Tagging entry name. | MaxLen: 63
    name: str
    # Tag category. | MaxLen: 63
    category: str
    # Tags.
    tags: str
    
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
class Address6SubnetsegmentObject:
    """Typed object for subnet-segment table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Name. | MaxLen: 63
    name: str
    # Subnet segment type. | Default: any
    type: Literal["any", "specific"]
    # Subnet segment value. | MaxLen: 35
    value: str
    
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
class Address6ListObject:
    """Typed object for list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP. | MaxLen: 89
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
class Address6Response(TypedDict):
    """
    Type hints for firewall/address6 API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Address name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"]  # Type of IPv6 address object (default = ipprefix). | Default: ipprefix
    route_tag: int  # route-tag address. | Default: 0 | Min: 1 | Max: 4294967295
    macaddr: list[Address6MacaddrItem]  # Multiple MAC address ranges.
    sdn: str  # SDN. | MaxLen: 35
    ip6: str  # IPv6 address prefix | Default: ::/0
    wildcard: str  # IPv6 address and wildcard netmask. | Default: :: ::
    start_ip: str  # First IP address (inclusive) in the range for the | Default: ::
    end_ip: str  # Final IP address (inclusive) in the range for the | Default: ::
    fqdn: str  # Fully qualified domain name. | MaxLen: 255
    country: str  # IPv6 addresses associated to a specific country. | MaxLen: 2
    cache_ttl: int  # Minimal TTL of individual IPv6 addresses in FQDN c | Default: 0 | Min: 0 | Max: 86400
    color: int  # Integer value to determine the color of the icon i | Default: 0 | Min: 0 | Max: 32
    obj_id: str  # Object ID for NSX. | MaxLen: 255
    tagging: list[Address6TaggingItem]  # Config object tagging.
    comment: str  # Comment. | MaxLen: 255
    template: str  # IPv6 address template. | MaxLen: 63
    subnet_segment: list[Address6SubnetsegmentItem]  # IPv6 subnet segments.
    host_type: Literal["any", "specific"]  # Host type. | Default: any
    host: str  # Host Address. | Default: ::
    tenant: str  # Tenant. | MaxLen: 35
    epg_name: str  # Endpoint group name. | MaxLen: 255
    sdn_tag: str  # SDN Tag. | MaxLen: 15
    filter: str  # Match criteria filter. | MaxLen: 2047
    list: list[Address6ListItem]  # IP address list.
    sdn_addr_type: Literal["private", "public", "all"]  # Type of addresses to collect. | Default: private
    passive_fqdn_learning: Literal["disable", "enable"]  # Enable/disable passive learning of FQDNs.  When en | Default: enable
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable


@final
class Address6Object:
    """Typed FortiObject for firewall/address6 with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Type of IPv6 address object (default = ipprefix). | Default: ipprefix
    type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"]
    # route-tag address. | Default: 0 | Min: 1 | Max: 4294967295
    route_tag: int
    # Multiple MAC address ranges.
    macaddr: list[Address6MacaddrObject]
    # SDN. | MaxLen: 35
    sdn: str
    # IPv6 address prefix | Default: ::/0
    ip6: str
    # IPv6 address and wildcard netmask. | Default: :: ::
    wildcard: str
    # First IP address (inclusive) in the range for the address | Default: ::
    start_ip: str
    # Final IP address (inclusive) in the range for the address | Default: ::
    end_ip: str
    # Fully qualified domain name. | MaxLen: 255
    fqdn: str
    # IPv6 addresses associated to a specific country. | MaxLen: 2
    country: str
    # Minimal TTL of individual IPv6 addresses in FQDN cache. | Default: 0 | Min: 0 | Max: 86400
    cache_ttl: int
    # Integer value to determine the color of the icon in the GUI | Default: 0 | Min: 0 | Max: 32
    color: int
    # Object ID for NSX. | MaxLen: 255
    obj_id: str
    # Config object tagging.
    tagging: list[Address6TaggingObject]
    # Comment. | MaxLen: 255
    comment: str
    # IPv6 address template. | MaxLen: 63
    template: str
    # IPv6 subnet segments.
    subnet_segment: list[Address6SubnetsegmentObject]
    # Host type. | Default: any
    host_type: Literal["any", "specific"]
    # Host Address. | Default: ::
    host: str
    # Tenant. | MaxLen: 35
    tenant: str
    # Endpoint group name. | MaxLen: 255
    epg_name: str
    # SDN Tag. | MaxLen: 15
    sdn_tag: str
    # Match criteria filter. | MaxLen: 2047
    filter: str
    # IP address list.
    list: list[Address6ListObject]
    # Type of addresses to collect. | Default: private
    sdn_addr_type: Literal["private", "public", "all"]
    # Enable/disable passive learning of FQDNs.  When enabled, the | Default: enable
    passive_fqdn_learning: Literal["disable", "enable"]
    # Security Fabric global object setting. | Default: disable
    fabric_object: Literal["enable", "disable"]
    
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
    def to_dict(self) -> Address6Payload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Address6:
    """
    Configure IPv6 firewall addresses.
    
    Path: firewall/address6
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
    ) -> Address6Object: ...
    
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
    ) -> Address6Object: ...
    
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
    ) -> FortiObjectList[Address6Object]: ...
    
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
    ) -> Address6Object: ...
    
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
    ) -> Address6Object: ...
    
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
    ) -> FortiObjectList[Address6Object]: ...
    
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
    ) -> Address6Object: ...
    
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
    ) -> Address6Object: ...
    
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
    ) -> FortiObjectList[Address6Object]: ...
    
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
    ) -> Address6Object | list[Address6Object] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Address6Object: ...
    
    @overload
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Address6Object: ...
    
    @overload
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Address6Object: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: Address6Payload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        type: Literal["ipprefix", "iprange", "fqdn", "geography", "dynamic", "template", "mac", "route-tag", "wildcard"] | None = ...,
        route_tag: int | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn: str | None = ...,
        ip6: str | None = ...,
        wildcard: str | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        cache_ttl: int | None = ...,
        color: int | None = ...,
        obj_id: str | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        comment: str | None = ...,
        template: str | None = ...,
        subnet_segment: str | list[str] | list[dict[str, Any]] | None = ...,
        host_type: Literal["any", "specific"] | None = ...,
        host: str | None = ...,
        tenant: str | None = ...,
        epg_name: str | None = ...,
        sdn_tag: str | None = ...,
        filter: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Address6",
    "Address6Payload",
    "Address6Response",
    "Address6Object",
]
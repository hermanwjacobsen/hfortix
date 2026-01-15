from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AddressPayload(TypedDict, total=False):
    """
    Type hints for firewall/address payload fields.
    
    Configure IPv4 addresses.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: associated-interface, interface)
        - :class:`~.system.sdn-connector.SdnConnectorEndpoint` (via: sdn)
        - :class:`~.system.zone.ZoneEndpoint` (via: associated-interface)

    **Usage:**
        payload: AddressPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Address name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    subnet: str  # IP address and subnet mask of address. | Default: 0.0.0.0 0.0.0.0
    type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"]  # Type of address. | Default: ipmask
    route_tag: int  # route-tag address. | Default: 0 | Min: 1 | Max: 4294967295
    sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"]  # Sub-type of address. | Default: sdn
    clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"]  # SPT (System Posture Token) value. | Default: unknown
    macaddr: list[dict[str, Any]]  # Multiple MAC address ranges.
    start_ip: str  # First IP address (inclusive) in the range for the | Default: 0.0.0.0
    end_ip: str  # Final IP address (inclusive) in the range for the | Default: 0.0.0.0
    fqdn: str  # Fully Qualified Domain Name address. | MaxLen: 255
    country: str  # IP addresses associated to a specific country. | MaxLen: 2
    wildcard_fqdn: str  # Fully Qualified Domain Name with wildcard characte | MaxLen: 255
    cache_ttl: int  # Defines the minimal TTL of individual IP addresses | Default: 0 | Min: 0 | Max: 86400
    wildcard: str  # IP address and wildcard netmask. | Default: 0.0.0.0 0.0.0.0
    sdn: str  # SDN. | MaxLen: 35
    fsso_group: list[dict[str, Any]]  # FSSO group(s).
    sso_attribute_value: list[dict[str, Any]]  # RADIUS attributes value.
    interface: str  # Name of interface whose IP address is to be used. | MaxLen: 35
    tenant: str  # Tenant. | MaxLen: 35
    organization: str  # Organization domain name | MaxLen: 35
    epg_name: str  # Endpoint group name. | MaxLen: 255
    subnet_name: str  # Subnet name. | MaxLen: 255
    sdn_tag: str  # SDN Tag. | MaxLen: 15
    policy_group: str  # Policy group name. | MaxLen: 15
    obj_tag: str  # Tag of dynamic address object. | MaxLen: 255
    obj_type: Literal["ip", "mac"]  # Object type. | Default: ip
    tag_detection_level: str  # Tag detection level of dynamic address object. | MaxLen: 15
    tag_type: str  # Tag type of dynamic address object. | MaxLen: 63
    hw_vendor: str  # Dynamic address matching hardware vendor. | MaxLen: 35
    hw_model: str  # Dynamic address matching hardware model. | MaxLen: 35
    os: str  # Dynamic address matching operating system. | MaxLen: 35
    sw_version: str  # Dynamic address matching software version. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    associated_interface: str  # Network interface associated with address. | MaxLen: 35
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    filter: str  # Match criteria filter. | MaxLen: 2047
    sdn_addr_type: Literal["private", "public", "all"]  # Type of addresses to collect. | Default: private
    node_ip_only: Literal["enable", "disable"]  # Enable/disable collection of node addresses only i | Default: disable
    obj_id: str  # Object ID for NSX. | MaxLen: 255
    list: list[dict[str, Any]]  # IP address list.
    tagging: list[dict[str, Any]]  # Config object tagging.
    allow_routing: Literal["enable", "disable"]  # Enable/disable use of this address in routing conf | Default: disable
    passive_fqdn_learning: Literal["disable", "enable"]  # Enable/disable passive learning of FQDNs.  When en | Default: enable
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class AddressMacaddrItem(TypedDict):
    """Type hints for macaddr table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    macaddr: str  # MAC address ranges <start>[-<end>] separated by sp | MaxLen: 127


class AddressFssogroupItem(TypedDict):
    """Type hints for fsso-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # FSSO group name. | MaxLen: 511


class AddressSsoattributevalueItem(TypedDict):
    """Type hints for sso-attribute-value table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # RADIUS attribute value. | MaxLen: 511


class AddressListItem(TypedDict):
    """Type hints for list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip: str  # IP. | MaxLen: 35


class AddressTaggingItem(TypedDict):
    """Type hints for tagging table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Tagging entry name. | MaxLen: 63
    category: str  # Tag category. | MaxLen: 63
    tags: str  # Tags.


# Nested classes for table field children (object mode)

@final
class AddressMacaddrObject:
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
class AddressFssogroupObject:
    """Typed object for fsso-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # FSSO group name. | MaxLen: 511
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


@final
class AddressSsoattributevalueObject:
    """Typed object for sso-attribute-value table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # RADIUS attribute value. | MaxLen: 511
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


@final
class AddressListObject:
    """Typed object for list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP. | MaxLen: 35
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


@final
class AddressTaggingObject:
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



# Response TypedDict for GET returns (all fields present in API response)
class AddressResponse(TypedDict):
    """
    Type hints for firewall/address API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Address name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    subnet: str  # IP address and subnet mask of address. | Default: 0.0.0.0 0.0.0.0
    type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"]  # Type of address. | Default: ipmask
    route_tag: int  # route-tag address. | Default: 0 | Min: 1 | Max: 4294967295
    sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"]  # Sub-type of address. | Default: sdn
    clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"]  # SPT (System Posture Token) value. | Default: unknown
    macaddr: list[AddressMacaddrItem]  # Multiple MAC address ranges.
    start_ip: str  # First IP address (inclusive) in the range for the | Default: 0.0.0.0
    end_ip: str  # Final IP address (inclusive) in the range for the | Default: 0.0.0.0
    fqdn: str  # Fully Qualified Domain Name address. | MaxLen: 255
    country: str  # IP addresses associated to a specific country. | MaxLen: 2
    wildcard_fqdn: str  # Fully Qualified Domain Name with wildcard characte | MaxLen: 255
    cache_ttl: int  # Defines the minimal TTL of individual IP addresses | Default: 0 | Min: 0 | Max: 86400
    wildcard: str  # IP address and wildcard netmask. | Default: 0.0.0.0 0.0.0.0
    sdn: str  # SDN. | MaxLen: 35
    fsso_group: list[AddressFssogroupItem]  # FSSO group(s).
    sso_attribute_value: list[AddressSsoattributevalueItem]  # RADIUS attributes value.
    interface: str  # Name of interface whose IP address is to be used. | MaxLen: 35
    tenant: str  # Tenant. | MaxLen: 35
    organization: str  # Organization domain name | MaxLen: 35
    epg_name: str  # Endpoint group name. | MaxLen: 255
    subnet_name: str  # Subnet name. | MaxLen: 255
    sdn_tag: str  # SDN Tag. | MaxLen: 15
    policy_group: str  # Policy group name. | MaxLen: 15
    obj_tag: str  # Tag of dynamic address object. | MaxLen: 255
    obj_type: Literal["ip", "mac"]  # Object type. | Default: ip
    tag_detection_level: str  # Tag detection level of dynamic address object. | MaxLen: 15
    tag_type: str  # Tag type of dynamic address object. | MaxLen: 63
    hw_vendor: str  # Dynamic address matching hardware vendor. | MaxLen: 35
    hw_model: str  # Dynamic address matching hardware model. | MaxLen: 35
    os: str  # Dynamic address matching operating system. | MaxLen: 35
    sw_version: str  # Dynamic address matching software version. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    associated_interface: str  # Network interface associated with address. | MaxLen: 35
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    filter: str  # Match criteria filter. | MaxLen: 2047
    sdn_addr_type: Literal["private", "public", "all"]  # Type of addresses to collect. | Default: private
    node_ip_only: Literal["enable", "disable"]  # Enable/disable collection of node addresses only i | Default: disable
    obj_id: str  # Object ID for NSX. | MaxLen: 255
    list: list[AddressListItem]  # IP address list.
    tagging: list[AddressTaggingItem]  # Config object tagging.
    allow_routing: Literal["enable", "disable"]  # Enable/disable use of this address in routing conf | Default: disable
    passive_fqdn_learning: Literal["disable", "enable"]  # Enable/disable passive learning of FQDNs.  When en | Default: enable
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable


@final
class AddressObject:
    """Typed FortiObject for firewall/address with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # IP address and subnet mask of address. | Default: 0.0.0.0 0.0.0.0
    subnet: str
    # Type of address. | Default: ipmask
    type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"]
    # route-tag address. | Default: 0 | Min: 1 | Max: 4294967295
    route_tag: int
    # Sub-type of address. | Default: sdn
    sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"]
    # SPT (System Posture Token) value. | Default: unknown
    clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"]
    # Multiple MAC address ranges.
    macaddr: list[AddressMacaddrObject]
    # First IP address (inclusive) in the range for the address. | Default: 0.0.0.0
    start_ip: str
    # Final IP address (inclusive) in the range for the address. | Default: 0.0.0.0
    end_ip: str
    # Fully Qualified Domain Name address. | MaxLen: 255
    fqdn: str
    # IP addresses associated to a specific country. | MaxLen: 2
    country: str
    # Fully Qualified Domain Name with wildcard characters. | MaxLen: 255
    wildcard_fqdn: str
    # Defines the minimal TTL of individual IP addresses in FQDN c | Default: 0 | Min: 0 | Max: 86400
    cache_ttl: int
    # IP address and wildcard netmask. | Default: 0.0.0.0 0.0.0.0
    wildcard: str
    # SDN. | MaxLen: 35
    sdn: str
    # FSSO group(s).
    fsso_group: list[AddressFssogroupObject]
    # RADIUS attributes value.
    sso_attribute_value: list[AddressSsoattributevalueObject]
    # Name of interface whose IP address is to be used. | MaxLen: 35
    interface: str
    # Tenant. | MaxLen: 35
    tenant: str
    # Organization domain name (Syntax: organization/domain). | MaxLen: 35
    organization: str
    # Endpoint group name. | MaxLen: 255
    epg_name: str
    # Subnet name. | MaxLen: 255
    subnet_name: str
    # SDN Tag. | MaxLen: 15
    sdn_tag: str
    # Policy group name. | MaxLen: 15
    policy_group: str
    # Tag of dynamic address object. | MaxLen: 255
    obj_tag: str
    # Object type. | Default: ip
    obj_type: Literal["ip", "mac"]
    # Tag detection level of dynamic address object. | MaxLen: 15
    tag_detection_level: str
    # Tag type of dynamic address object. | MaxLen: 63
    tag_type: str
    # Dynamic address matching hardware vendor. | MaxLen: 35
    hw_vendor: str
    # Dynamic address matching hardware model. | MaxLen: 35
    hw_model: str
    # Dynamic address matching operating system. | MaxLen: 35
    os: str
    # Dynamic address matching software version. | MaxLen: 35
    sw_version: str
    # Comment. | MaxLen: 255
    comment: str
    # Network interface associated with address. | MaxLen: 35
    associated_interface: str
    # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    color: int
    # Match criteria filter. | MaxLen: 2047
    filter: str
    # Type of addresses to collect. | Default: private
    sdn_addr_type: Literal["private", "public", "all"]
    # Enable/disable collection of node addresses only in Kubernet | Default: disable
    node_ip_only: Literal["enable", "disable"]
    # Object ID for NSX. | MaxLen: 255
    obj_id: str
    # IP address list.
    list: list[AddressListObject]
    # Config object tagging.
    tagging: list[AddressTaggingObject]
    # Enable/disable use of this address in routing configurations | Default: disable
    allow_routing: Literal["enable", "disable"]
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
    def to_dict(self) -> AddressPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Address:
    """
    Configure IPv4 addresses.
    
    Path: firewall/address
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
    ) -> AddressObject: ...
    
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
    ) -> AddressObject: ...
    
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
    ) -> FortiObjectList[AddressObject]: ...
    
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
    ) -> AddressObject: ...
    
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
    ) -> AddressObject: ...
    
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
    ) -> FortiObjectList[AddressObject]: ...
    
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
    ) -> AddressObject: ...
    
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
    ) -> AddressObject: ...
    
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
    ) -> FortiObjectList[AddressObject]: ...
    
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
    ) -> AddressObject | list[AddressObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AddressObject: ...
    
    @overload
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> AddressObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AddressObject: ...
    
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
        payload_dict: AddressPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        subnet: str | None = ...,
        type: Literal["ipmask", "iprange", "fqdn", "geography", "wildcard", "dynamic", "interface-subnet", "mac", "route-tag"] | None = ...,
        route_tag: int | None = ...,
        sub_type: Literal["sdn", "clearpass-spt", "fsso", "rsso", "ems-tag", "fortivoice-tag", "fortinac-tag", "swc-tag", "device-identification", "external-resource", "obsolete"] | None = ...,
        clearpass_spt: Literal["unknown", "healthy", "quarantine", "checkup", "transient", "infected"] | None = ...,
        macaddr: str | list[str] | list[dict[str, Any]] | None = ...,
        start_ip: str | None = ...,
        end_ip: str | None = ...,
        fqdn: str | None = ...,
        country: str | None = ...,
        wildcard_fqdn: str | None = ...,
        cache_ttl: int | None = ...,
        wildcard: str | None = ...,
        sdn: str | None = ...,
        fsso_group: str | list[str] | list[dict[str, Any]] | None = ...,
        sso_attribute_value: str | list[str] | list[dict[str, Any]] | None = ...,
        interface: str | None = ...,
        tenant: str | None = ...,
        organization: str | None = ...,
        epg_name: str | None = ...,
        subnet_name: str | None = ...,
        sdn_tag: str | None = ...,
        policy_group: str | None = ...,
        obj_tag: str | None = ...,
        obj_type: Literal["ip", "mac"] | None = ...,
        tag_detection_level: str | None = ...,
        tag_type: str | None = ...,
        hw_vendor: str | None = ...,
        hw_model: str | None = ...,
        os: str | None = ...,
        sw_version: str | None = ...,
        comment: str | None = ...,
        associated_interface: str | None = ...,
        color: int | None = ...,
        filter: str | None = ...,
        sdn_addr_type: Literal["private", "public", "all"] | None = ...,
        node_ip_only: Literal["enable", "disable"] | None = ...,
        obj_id: str | None = ...,
        list: str | list[str] | list[dict[str, Any]] | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        allow_routing: Literal["enable", "disable"] | None = ...,
        passive_fqdn_learning: Literal["disable", "enable"] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
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
    "Address",
    "AddressPayload",
    "AddressResponse",
    "AddressObject",
]
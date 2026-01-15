from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class DnsPayload(TypedDict, total=False):
    """
    Type hints for system/dns payload fields.
    
    Configure DNS.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.local.LocalEndpoint` (via: ssl-certificate)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface, source-ip-interface)

    **Usage:**
        payload: DnsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    primary: str  # Primary DNS server IP address. | Default: 0.0.0.0
    secondary: str  # Secondary DNS server IP address. | Default: 0.0.0.0
    protocol: Literal["cleartext", "dot", "doh"]  # DNS transport protocols. | Default: cleartext
    ssl_certificate: str  # Name of local certificate for SSL connections. | Default: Fortinet_Factory | MaxLen: 35
    server_hostname: list[dict[str, Any]]  # DNS server host name list.
    domain: list[dict[str, Any]]  # Search suffix list for hostname lookup.
    ip6_primary: str  # Primary DNS server IPv6 address. | Default: ::
    ip6_secondary: str  # Secondary DNS server IPv6 address. | Default: ::
    timeout: int  # DNS query timeout interval in seconds (1 - 10). | Default: 5 | Min: 1 | Max: 10
    retry: int  # Number of times to retry (0 - 5). | Default: 2 | Min: 0 | Max: 5
    dns_cache_limit: int  # Maximum number of records in the DNS cache. | Default: 5000 | Min: 0 | Max: 4294967295
    dns_cache_ttl: int  # Duration in seconds that the DNS cache retains inf | Default: 1800 | Min: 60 | Max: 86400
    cache_notfound_responses: Literal["disable", "enable"]  # Enable/disable response from the DNS server when a | Default: disable
    source_ip: str  # IP address used by the DNS server as its source IP | Default: 0.0.0.0
    source_ip_interface: str  # IP address of the specified interface as the sourc | MaxLen: 15
    root_servers: list[dict[str, Any]]  # Configure up to two preferred servers that serve t
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    server_select_method: Literal["least-rtt", "failover"]  # Specify how configured servers are prioritized. | Default: least-rtt
    alt_primary: str  # Alternate primary DNS server. This is not used as | Default: 0.0.0.0
    alt_secondary: str  # Alternate secondary DNS server. This is not used a | Default: 0.0.0.0
    log: Literal["disable", "error", "all"]  # Local DNS log setting. | Default: disable
    fqdn_cache_ttl: int  # FQDN cache time to live in seconds | Default: 0 | Min: 0 | Max: 86400
    fqdn_max_refresh: int  # FQDN cache maximum refresh time in seconds | Default: 3600 | Min: 3600 | Max: 86400
    fqdn_min_refresh: int  # FQDN cache minimum refresh time in seconds | Default: 60 | Min: 10 | Max: 3600
    hostname_ttl: int  # TTL of hostname table entries (60 - 86400). | Default: 86400 | Min: 60 | Max: 86400
    hostname_limit: int  # Limit of the number of hostname table entries | Default: 5000 | Min: 0 | Max: 50000

# Nested TypedDicts for table field children (dict mode)

class DnsServerhostnameItem(TypedDict):
    """Type hints for server-hostname table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    hostname: str  # DNS server host name list separated by space | MaxLen: 127


class DnsDomainItem(TypedDict):
    """Type hints for domain table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    domain: str  # DNS search domain list separated by space | MaxLen: 127


# Nested classes for table field children (object mode)

@final
class DnsServerhostnameObject:
    """Typed object for server-hostname table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DNS server host name list separated by space | MaxLen: 127
    hostname: str
    
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
class DnsDomainObject:
    """Typed object for domain table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DNS search domain list separated by space | MaxLen: 127
    domain: str
    
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
class DnsResponse(TypedDict):
    """
    Type hints for system/dns API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    primary: str  # Primary DNS server IP address. | Default: 0.0.0.0
    secondary: str  # Secondary DNS server IP address. | Default: 0.0.0.0
    protocol: Literal["cleartext", "dot", "doh"]  # DNS transport protocols. | Default: cleartext
    ssl_certificate: str  # Name of local certificate for SSL connections. | Default: Fortinet_Factory | MaxLen: 35
    server_hostname: list[DnsServerhostnameItem]  # DNS server host name list.
    domain: list[DnsDomainItem]  # Search suffix list for hostname lookup.
    ip6_primary: str  # Primary DNS server IPv6 address. | Default: ::
    ip6_secondary: str  # Secondary DNS server IPv6 address. | Default: ::
    timeout: int  # DNS query timeout interval in seconds (1 - 10). | Default: 5 | Min: 1 | Max: 10
    retry: int  # Number of times to retry (0 - 5). | Default: 2 | Min: 0 | Max: 5
    dns_cache_limit: int  # Maximum number of records in the DNS cache. | Default: 5000 | Min: 0 | Max: 4294967295
    dns_cache_ttl: int  # Duration in seconds that the DNS cache retains inf | Default: 1800 | Min: 60 | Max: 86400
    cache_notfound_responses: Literal["disable", "enable"]  # Enable/disable response from the DNS server when a | Default: disable
    source_ip: str  # IP address used by the DNS server as its source IP | Default: 0.0.0.0
    source_ip_interface: str  # IP address of the specified interface as the sourc | MaxLen: 15
    root_servers: list[dict[str, Any]]  # Configure up to two preferred servers that serve t
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    server_select_method: Literal["least-rtt", "failover"]  # Specify how configured servers are prioritized. | Default: least-rtt
    alt_primary: str  # Alternate primary DNS server. This is not used as | Default: 0.0.0.0
    alt_secondary: str  # Alternate secondary DNS server. This is not used a | Default: 0.0.0.0
    log: Literal["disable", "error", "all"]  # Local DNS log setting. | Default: disable
    fqdn_cache_ttl: int  # FQDN cache time to live in seconds | Default: 0 | Min: 0 | Max: 86400
    fqdn_max_refresh: int  # FQDN cache maximum refresh time in seconds | Default: 3600 | Min: 3600 | Max: 86400
    fqdn_min_refresh: int  # FQDN cache minimum refresh time in seconds | Default: 60 | Min: 10 | Max: 3600
    hostname_ttl: int  # TTL of hostname table entries (60 - 86400). | Default: 86400 | Min: 60 | Max: 86400
    hostname_limit: int  # Limit of the number of hostname table entries | Default: 5000 | Min: 0 | Max: 50000


@final
class DnsObject:
    """Typed FortiObject for system/dns with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Primary DNS server IP address. | Default: 0.0.0.0
    primary: str
    # Secondary DNS server IP address. | Default: 0.0.0.0
    secondary: str
    # DNS transport protocols. | Default: cleartext
    protocol: Literal["cleartext", "dot", "doh"]
    # Name of local certificate for SSL connections. | Default: Fortinet_Factory | MaxLen: 35
    ssl_certificate: str
    # DNS server host name list.
    server_hostname: list[DnsServerhostnameObject]
    # Search suffix list for hostname lookup.
    domain: list[DnsDomainObject]
    # Primary DNS server IPv6 address. | Default: ::
    ip6_primary: str
    # Secondary DNS server IPv6 address. | Default: ::
    ip6_secondary: str
    # DNS query timeout interval in seconds (1 - 10). | Default: 5 | Min: 1 | Max: 10
    timeout: int
    # Number of times to retry (0 - 5). | Default: 2 | Min: 0 | Max: 5
    retry: int
    # Maximum number of records in the DNS cache. | Default: 5000 | Min: 0 | Max: 4294967295
    dns_cache_limit: int
    # Duration in seconds that the DNS cache retains information. | Default: 1800 | Min: 60 | Max: 86400
    dns_cache_ttl: int
    # Enable/disable response from the DNS server when a record is | Default: disable
    cache_notfound_responses: Literal["disable", "enable"]
    # IP address used by the DNS server as its source IP. | Default: 0.0.0.0
    source_ip: str
    # IP address of the specified interface as the source IP addre | MaxLen: 15
    source_ip_interface: str
    # Configure up to two preferred servers that serve the DNS roo
    root_servers: list[dict[str, Any]]
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    # Specify how configured servers are prioritized. | Default: least-rtt
    server_select_method: Literal["least-rtt", "failover"]
    # Alternate primary DNS server. This is not used as a failover | Default: 0.0.0.0
    alt_primary: str
    # Alternate secondary DNS server. This is not used as a failov | Default: 0.0.0.0
    alt_secondary: str
    # Local DNS log setting. | Default: disable
    log: Literal["disable", "error", "all"]
    # FQDN cache time to live in seconds (0 - 86400, default = 0). | Default: 0 | Min: 0 | Max: 86400
    fqdn_cache_ttl: int
    # FQDN cache maximum refresh time in seconds | Default: 3600 | Min: 3600 | Max: 86400
    fqdn_max_refresh: int
    # FQDN cache minimum refresh time in seconds | Default: 60 | Min: 10 | Max: 3600
    fqdn_min_refresh: int
    # TTL of hostname table entries (60 - 86400). | Default: 86400 | Min: 60 | Max: 86400
    hostname_ttl: int
    # Limit of the number of hostname table entries (0 - 50000). | Default: 5000 | Min: 0 | Max: 50000
    hostname_limit: int
    
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
    def to_dict(self) -> DnsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Dns:
    """
    Configure DNS.
    
    Path: system/dns
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject: ...
    
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
    ) -> DnsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> DnsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: DnsPayload | None = ...,
        primary: str | None = ...,
        secondary: str | None = ...,
        protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        ssl_certificate: str | None = ...,
        server_hostname: str | list[str] | list[dict[str, Any]] | None = ...,
        domain: str | list[str] | list[dict[str, Any]] | None = ...,
        ip6_primary: str | None = ...,
        ip6_secondary: str | None = ...,
        timeout: int | None = ...,
        retry: int | None = ...,
        dns_cache_limit: int | None = ...,
        dns_cache_ttl: int | None = ...,
        cache_notfound_responses: Literal["disable", "enable"] | None = ...,
        source_ip: str | None = ...,
        source_ip_interface: str | None = ...,
        root_servers: str | list[str] | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        server_select_method: Literal["least-rtt", "failover"] | None = ...,
        alt_primary: str | None = ...,
        alt_secondary: str | None = ...,
        log: Literal["disable", "error", "all"] | None = ...,
        fqdn_cache_ttl: int | None = ...,
        fqdn_max_refresh: int | None = ...,
        fqdn_min_refresh: int | None = ...,
        hostname_ttl: int | None = ...,
        hostname_limit: int | None = ...,
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
    "Dns",
    "DnsPayload",
    "DnsResponse",
    "DnsObject",
]
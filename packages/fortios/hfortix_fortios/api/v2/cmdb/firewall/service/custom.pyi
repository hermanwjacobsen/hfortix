from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class CustomPayload(TypedDict, total=False):
    """
    Type hints for firewall/service/custom payload fields.
    
    Configure custom services.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.service.category.CategoryEndpoint` (via: category)

    **Usage:**
        payload: CustomPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Custom service name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    proxy: Literal["enable", "disable"]  # Enable/disable web proxy service. | Default: disable
    category: str  # Service category. | MaxLen: 63
    protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"]  # Protocol type based on IANA numbers. | Default: TCP/UDP/UDP-Lite/SCTP
    helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"]  # Helper name. | Default: auto
    iprange: str  # Start and end of the IP range associated with serv
    fqdn: str  # Fully qualified domain name. | MaxLen: 255
    protocol_number: int  # IP protocol number. | Default: 0 | Min: 0 | Max: 254
    icmptype: int  # ICMP type. | Min: 0 | Max: 4294967295
    icmpcode: int  # ICMP code. | Min: 0 | Max: 255
    tcp_portrange: str  # Multiple TCP port ranges.
    udp_portrange: str  # Multiple UDP port ranges.
    udplite_portrange: str  # Multiple UDP-Lite port ranges.
    sctp_portrange: str  # Multiple SCTP port ranges.
    tcp_halfclose_timer: int  # Wait time to close a TCP session waiting for an un | Default: 0 | Min: 0 | Max: 86400
    tcp_halfopen_timer: int  # Wait time to close a TCP session waiting for an un | Default: 0 | Min: 0 | Max: 86400
    tcp_timewait_timer: int  # Set the length of the TCP TIME-WAIT state in secon | Default: 0 | Min: 0 | Max: 300
    tcp_rst_timer: int  # Set the length of the TCP CLOSE state in seconds | Default: 0 | Min: 5 | Max: 300
    udp_idle_timer: int  # Number of seconds before an idle UDP/UDP-Lite conn | Default: 0 | Min: 0 | Max: 86400
    session_ttl: str  # Session TTL (300 - 2764800, 0 = default).
    check_reset_range: Literal["disable", "strict", "default"]  # Configure the type of ICMP error message verificat | Default: default
    comment: str  # Comment. | MaxLen: 255
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    app_service_type: Literal["disable", "app-id", "app-category"]  # Application service type. | Default: disable
    app_category: list[dict[str, Any]]  # Application category ID.
    application: list[dict[str, Any]]  # Application ID.
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable

# Nested TypedDicts for table field children (dict mode)

class CustomAppcategoryItem(TypedDict):
    """Type hints for app-category table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Application category id. | Default: 0 | Min: 0 | Max: 4294967295


class CustomApplicationItem(TypedDict):
    """Type hints for application table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Application id. | Default: 0 | Min: 0 | Max: 4294967295


# Nested classes for table field children (object mode)

@final
class CustomAppcategoryObject:
    """Typed object for app-category table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Application category id. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    
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
class CustomApplicationObject:
    """Typed object for application table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Application id. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    
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
class CustomResponse(TypedDict):
    """
    Type hints for firewall/service/custom API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Custom service name. | MaxLen: 79
    uuid: str  # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    proxy: Literal["enable", "disable"]  # Enable/disable web proxy service. | Default: disable
    category: str  # Service category. | MaxLen: 63
    protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"]  # Protocol type based on IANA numbers. | Default: TCP/UDP/UDP-Lite/SCTP
    helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"]  # Helper name. | Default: auto
    iprange: str  # Start and end of the IP range associated with serv
    fqdn: str  # Fully qualified domain name. | MaxLen: 255
    protocol_number: int  # IP protocol number. | Default: 0 | Min: 0 | Max: 254
    icmptype: int  # ICMP type. | Min: 0 | Max: 4294967295
    icmpcode: int  # ICMP code. | Min: 0 | Max: 255
    tcp_portrange: str  # Multiple TCP port ranges.
    udp_portrange: str  # Multiple UDP port ranges.
    udplite_portrange: str  # Multiple UDP-Lite port ranges.
    sctp_portrange: str  # Multiple SCTP port ranges.
    tcp_halfclose_timer: int  # Wait time to close a TCP session waiting for an un | Default: 0 | Min: 0 | Max: 86400
    tcp_halfopen_timer: int  # Wait time to close a TCP session waiting for an un | Default: 0 | Min: 0 | Max: 86400
    tcp_timewait_timer: int  # Set the length of the TCP TIME-WAIT state in secon | Default: 0 | Min: 0 | Max: 300
    tcp_rst_timer: int  # Set the length of the TCP CLOSE state in seconds | Default: 0 | Min: 5 | Max: 300
    udp_idle_timer: int  # Number of seconds before an idle UDP/UDP-Lite conn | Default: 0 | Min: 0 | Max: 86400
    session_ttl: str  # Session TTL (300 - 2764800, 0 = default).
    check_reset_range: Literal["disable", "strict", "default"]  # Configure the type of ICMP error message verificat | Default: default
    comment: str  # Comment. | MaxLen: 255
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    app_service_type: Literal["disable", "app-id", "app-category"]  # Application service type. | Default: disable
    app_category: list[CustomAppcategoryItem]  # Application category ID.
    application: list[CustomApplicationItem]  # Application ID.
    fabric_object: Literal["enable", "disable"]  # Security Fabric global object setting. | Default: disable


@final
class CustomObject:
    """Typed FortiObject for firewall/service/custom with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Custom service name. | MaxLen: 79
    name: str
    # Universally Unique Identifier | Default: 00000000-0000-0000-0000-000000000000
    uuid: str
    # Enable/disable web proxy service. | Default: disable
    proxy: Literal["enable", "disable"]
    # Service category. | MaxLen: 63
    category: str
    # Protocol type based on IANA numbers. | Default: TCP/UDP/UDP-Lite/SCTP
    protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"]
    # Helper name. | Default: auto
    helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"]
    # Start and end of the IP range associated with service.
    iprange: str
    # Fully qualified domain name. | MaxLen: 255
    fqdn: str
    # IP protocol number. | Default: 0 | Min: 0 | Max: 254
    protocol_number: int
    # ICMP type. | Min: 0 | Max: 4294967295
    icmptype: int
    # ICMP code. | Min: 0 | Max: 255
    icmpcode: int
    # Multiple TCP port ranges.
    tcp_portrange: str
    # Multiple UDP port ranges.
    udp_portrange: str
    # Multiple UDP-Lite port ranges.
    udplite_portrange: str
    # Multiple SCTP port ranges.
    sctp_portrange: str
    # Wait time to close a TCP session waiting for an unanswered F | Default: 0 | Min: 0 | Max: 86400
    tcp_halfclose_timer: int
    # Wait time to close a TCP session waiting for an unanswered o | Default: 0 | Min: 0 | Max: 86400
    tcp_halfopen_timer: int
    # Set the length of the TCP TIME-WAIT state in seconds | Default: 0 | Min: 0 | Max: 300
    tcp_timewait_timer: int
    # Set the length of the TCP CLOSE state in seconds | Default: 0 | Min: 5 | Max: 300
    tcp_rst_timer: int
    # Number of seconds before an idle UDP/UDP-Lite connection tim | Default: 0 | Min: 0 | Max: 86400
    udp_idle_timer: int
    # Session TTL (300 - 2764800, 0 = default).
    session_ttl: str
    # Configure the type of ICMP error message verification. | Default: default
    check_reset_range: Literal["disable", "strict", "default"]
    # Comment. | MaxLen: 255
    comment: str
    # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    color: int
    # Application service type. | Default: disable
    app_service_type: Literal["disable", "app-id", "app-category"]
    # Application category ID.
    app_category: list[CustomAppcategoryObject]
    # Application ID.
    application: list[CustomApplicationObject]
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
    def to_dict(self) -> CustomPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Custom:
    """
    Configure custom services.
    
    Path: firewall/service/custom
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
    ) -> CustomObject: ...
    
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
    ) -> CustomObject: ...
    
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
    ) -> FortiObjectList[CustomObject]: ...
    
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
    ) -> CustomObject: ...
    
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
    ) -> CustomObject: ...
    
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
    ) -> FortiObjectList[CustomObject]: ...
    
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
    ) -> CustomObject: ...
    
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
    ) -> CustomObject: ...
    
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
    ) -> FortiObjectList[CustomObject]: ...
    
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
    ) -> CustomObject | list[CustomObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        fabric_object: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> CustomObject: ...
    
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
        payload_dict: CustomPayload | None = ...,
        name: str | None = ...,
        uuid: str | None = ...,
        proxy: Literal["enable", "disable"] | None = ...,
        category: str | None = ...,
        protocol: Literal["TCP/UDP/UDP-Lite/SCTP", "ICMP", "ICMP6", "IP", "HTTP", "FTP", "CONNECT", "SOCKS-TCP", "SOCKS-UDP", "ALL"] | None = ...,
        helper: Literal["auto", "disable", "ftp", "tftp", "ras", "h323", "tns", "mms", "sip", "pptp", "rtsp", "dns-udp", "dns-tcp", "pmap", "rsh", "dcerpc", "mgcp"] | None = ...,
        iprange: str | None = ...,
        fqdn: str | None = ...,
        protocol_number: int | None = ...,
        icmptype: int | None = ...,
        icmpcode: int | None = ...,
        tcp_portrange: str | None = ...,
        udp_portrange: str | None = ...,
        udplite_portrange: str | None = ...,
        sctp_portrange: str | None = ...,
        tcp_halfclose_timer: int | None = ...,
        tcp_halfopen_timer: int | None = ...,
        tcp_timewait_timer: int | None = ...,
        tcp_rst_timer: int | None = ...,
        udp_idle_timer: int | None = ...,
        session_ttl: str | None = ...,
        check_reset_range: Literal["disable", "strict", "default"] | None = ...,
        comment: str | None = ...,
        color: int | None = ...,
        app_service_type: Literal["disable", "app-id", "app-category"] | None = ...,
        app_category: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Custom",
    "CustomPayload",
    "CustomResponse",
    "CustomObject",
]
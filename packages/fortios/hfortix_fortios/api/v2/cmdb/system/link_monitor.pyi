from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LinkMonitorPayload(TypedDict, total=False):
    """
    Type hints for system/link_monitor payload fields.
    
    Configure Link Health Monitor.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.traffic-class.TrafficClassEndpoint` (via: class-id)
        - :class:`~.system.interface.InterfaceEndpoint` (via: srcintf)

    **Usage:**
        payload: LinkMonitorPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Link monitor name. | MaxLen: 35
    addr_mode: Literal["ipv4", "ipv6"]  # Address mode (IPv4 or IPv6). | Default: ipv4
    srcintf: str  # Interface that receives the traffic to be monitore | MaxLen: 15
    server_config: Literal["default", "individual"]  # Mode of server configuration. | Default: default
    server_type: Literal["static", "dynamic"]  # Server type (static or dynamic). | Default: static
    server: list[dict[str, Any]]  # IP address of the server(s) to be monitored.
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"]  # Protocols used to monitor the server. | Default: ping
    port: int  # Port number of the traffic to be used to monitor t | Default: 0 | Min: 1 | Max: 65535
    gateway_ip: str  # Gateway IP address used to probe the server. | Default: 0.0.0.0
    gateway_ip6: str  # Gateway IPv6 address used to probe the server. | Default: ::
    route: list[dict[str, Any]]  # Subnet to monitor.
    source_ip: str  # Source IP address used in packet to the server. | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address used in packet to the server. | Default: ::
    http_get: str  # If you are monitoring an HTML server you can send | Default: / | MaxLen: 1024
    http_agent: str  # String in the http-agent field in the HTTP header. | Default: Chrome/ Safari/ | MaxLen: 1024
    http_match: str  # String that you expect to see in the HTTP-GET requ | MaxLen: 1024
    interval: int  # Detection interval in milliseconds | Default: 500 | Min: 20 | Max: 3600000
    probe_timeout: int  # Time to wait before a probe packet is considered l | Default: 500 | Min: 20 | Max: 5000
    failtime: int  # Number of retry attempts before the server is cons | Default: 5 | Min: 1 | Max: 3600
    recoverytime: int  # Number of successful responses received before ser | Default: 5 | Min: 1 | Max: 3600
    probe_count: int  # Number of most recent probes that should be used t | Default: 30 | Min: 5 | Max: 30
    security_mode: Literal["none", "authentication"]  # Twamp controller security mode. | Default: none
    password: str  # TWAMP controller password in authentication mode. | MaxLen: 128
    packet_size: int  # Packet size of a TWAMP test session | Default: 124 | Min: 0 | Max: 65535
    ha_priority: int  # HA election priority (1 - 50). | Default: 1 | Min: 1 | Max: 50
    fail_weight: int  # Threshold weight to trigger link failure alert. | Default: 0 | Min: 0 | Max: 255
    update_cascade_interface: Literal["enable", "disable"]  # Enable/disable update cascade interface. | Default: enable
    update_static_route: Literal["enable", "disable"]  # Enable/disable updating the static route. | Default: enable
    update_policy_route: Literal["enable", "disable"]  # Enable/disable updating the policy route. | Default: enable
    status: Literal["enable", "disable"]  # Enable/disable this link monitor. | Default: enable
    diffservcode: str  # Differentiated services code point (DSCP) in the I
    class_id: int  # Traffic class ID. | Default: 0 | Min: 0 | Max: 4294967295
    service_detection: Literal["enable", "disable"]  # Only use monitor to read quality values. If enable | Default: disable
    server_list: list[dict[str, Any]]  # Servers for link-monitor to monitor.

# Nested TypedDicts for table field children (dict mode)

class LinkMonitorServerItem(TypedDict):
    """Type hints for server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    address: str  # Server address. | MaxLen: 79


class LinkMonitorRouteItem(TypedDict):
    """Type hints for route table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    subnet: str  # IP and netmask (x.x.x.x/y). | MaxLen: 79


class LinkMonitorServerlistItem(TypedDict):
    """Type hints for server-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Server ID. | Default: 0 | Min: 1 | Max: 32
    dst: str  # IP address of the server to be monitored. | MaxLen: 64
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"]  # Protocols used to monitor the server. | Default: ping
    port: int  # Port number of the traffic to be used to monitor t | Default: 0 | Min: 1 | Max: 65535
    weight: int  # Weight of the monitor to this dst (0 - 255). | Default: 0 | Min: 0 | Max: 255


# Nested classes for table field children (object mode)

@final
class LinkMonitorServerObject:
    """Typed object for server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Server address. | MaxLen: 79
    address: str
    
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
class LinkMonitorRouteObject:
    """Typed object for route table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP and netmask (x.x.x.x/y). | MaxLen: 79
    subnet: str
    
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
class LinkMonitorServerlistObject:
    """Typed object for server-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Server ID. | Default: 0 | Min: 1 | Max: 32
    id: int
    # IP address of the server to be monitored. | MaxLen: 64
    dst: str
    # Protocols used to monitor the server. | Default: ping
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"]
    # Port number of the traffic to be used to monitor the server. | Default: 0 | Min: 1 | Max: 65535
    port: int
    # Weight of the monitor to this dst (0 - 255). | Default: 0 | Min: 0 | Max: 255
    weight: int
    
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
class LinkMonitorResponse(TypedDict):
    """
    Type hints for system/link_monitor API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Link monitor name. | MaxLen: 35
    addr_mode: Literal["ipv4", "ipv6"]  # Address mode (IPv4 or IPv6). | Default: ipv4
    srcintf: str  # Interface that receives the traffic to be monitore | MaxLen: 15
    server_config: Literal["default", "individual"]  # Mode of server configuration. | Default: default
    server_type: Literal["static", "dynamic"]  # Server type (static or dynamic). | Default: static
    server: list[LinkMonitorServerItem]  # IP address of the server(s) to be monitored.
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"]  # Protocols used to monitor the server. | Default: ping
    port: int  # Port number of the traffic to be used to monitor t | Default: 0 | Min: 1 | Max: 65535
    gateway_ip: str  # Gateway IP address used to probe the server. | Default: 0.0.0.0
    gateway_ip6: str  # Gateway IPv6 address used to probe the server. | Default: ::
    route: list[LinkMonitorRouteItem]  # Subnet to monitor.
    source_ip: str  # Source IP address used in packet to the server. | Default: 0.0.0.0
    source_ip6: str  # Source IPv6 address used in packet to the server. | Default: ::
    http_get: str  # If you are monitoring an HTML server you can send | Default: / | MaxLen: 1024
    http_agent: str  # String in the http-agent field in the HTTP header. | Default: Chrome/ Safari/ | MaxLen: 1024
    http_match: str  # String that you expect to see in the HTTP-GET requ | MaxLen: 1024
    interval: int  # Detection interval in milliseconds | Default: 500 | Min: 20 | Max: 3600000
    probe_timeout: int  # Time to wait before a probe packet is considered l | Default: 500 | Min: 20 | Max: 5000
    failtime: int  # Number of retry attempts before the server is cons | Default: 5 | Min: 1 | Max: 3600
    recoverytime: int  # Number of successful responses received before ser | Default: 5 | Min: 1 | Max: 3600
    probe_count: int  # Number of most recent probes that should be used t | Default: 30 | Min: 5 | Max: 30
    security_mode: Literal["none", "authentication"]  # Twamp controller security mode. | Default: none
    password: str  # TWAMP controller password in authentication mode. | MaxLen: 128
    packet_size: int  # Packet size of a TWAMP test session | Default: 124 | Min: 0 | Max: 65535
    ha_priority: int  # HA election priority (1 - 50). | Default: 1 | Min: 1 | Max: 50
    fail_weight: int  # Threshold weight to trigger link failure alert. | Default: 0 | Min: 0 | Max: 255
    update_cascade_interface: Literal["enable", "disable"]  # Enable/disable update cascade interface. | Default: enable
    update_static_route: Literal["enable", "disable"]  # Enable/disable updating the static route. | Default: enable
    update_policy_route: Literal["enable", "disable"]  # Enable/disable updating the policy route. | Default: enable
    status: Literal["enable", "disable"]  # Enable/disable this link monitor. | Default: enable
    diffservcode: str  # Differentiated services code point (DSCP) in the I
    class_id: int  # Traffic class ID. | Default: 0 | Min: 0 | Max: 4294967295
    service_detection: Literal["enable", "disable"]  # Only use monitor to read quality values. If enable | Default: disable
    server_list: list[LinkMonitorServerlistItem]  # Servers for link-monitor to monitor.


@final
class LinkMonitorObject:
    """Typed FortiObject for system/link_monitor with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Link monitor name. | MaxLen: 35
    name: str
    # Address mode (IPv4 or IPv6). | Default: ipv4
    addr_mode: Literal["ipv4", "ipv6"]
    # Interface that receives the traffic to be monitored. | MaxLen: 15
    srcintf: str
    # Mode of server configuration. | Default: default
    server_config: Literal["default", "individual"]
    # Server type (static or dynamic). | Default: static
    server_type: Literal["static", "dynamic"]
    # IP address of the server(s) to be monitored.
    server: list[LinkMonitorServerObject]
    # Protocols used to monitor the server. | Default: ping
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"]
    # Port number of the traffic to be used to monitor the server. | Default: 0 | Min: 1 | Max: 65535
    port: int
    # Gateway IP address used to probe the server. | Default: 0.0.0.0
    gateway_ip: str
    # Gateway IPv6 address used to probe the server. | Default: ::
    gateway_ip6: str
    # Subnet to monitor.
    route: list[LinkMonitorRouteObject]
    # Source IP address used in packet to the server. | Default: 0.0.0.0
    source_ip: str
    # Source IPv6 address used in packet to the server. | Default: ::
    source_ip6: str
    # If you are monitoring an HTML server you can send an HTTP-GE | Default: / | MaxLen: 1024
    http_get: str
    # String in the http-agent field in the HTTP header. | Default: Chrome/ Safari/ | MaxLen: 1024
    http_agent: str
    # String that you expect to see in the HTTP-GET requests of th | MaxLen: 1024
    http_match: str
    # Detection interval in milliseconds | Default: 500 | Min: 20 | Max: 3600000
    interval: int
    # Time to wait before a probe packet is considered lost | Default: 500 | Min: 20 | Max: 5000
    probe_timeout: int
    # Number of retry attempts before the server is considered dow | Default: 5 | Min: 1 | Max: 3600
    failtime: int
    # Number of successful responses received before server is con | Default: 5 | Min: 1 | Max: 3600
    recoverytime: int
    # Number of most recent probes that should be used to calculat | Default: 30 | Min: 5 | Max: 30
    probe_count: int
    # Twamp controller security mode. | Default: none
    security_mode: Literal["none", "authentication"]
    # TWAMP controller password in authentication mode. | MaxLen: 128
    password: str
    # Packet size of a TWAMP test session (124/158 - 1024). | Default: 124 | Min: 0 | Max: 65535
    packet_size: int
    # HA election priority (1 - 50). | Default: 1 | Min: 1 | Max: 50
    ha_priority: int
    # Threshold weight to trigger link failure alert. | Default: 0 | Min: 0 | Max: 255
    fail_weight: int
    # Enable/disable update cascade interface. | Default: enable
    update_cascade_interface: Literal["enable", "disable"]
    # Enable/disable updating the static route. | Default: enable
    update_static_route: Literal["enable", "disable"]
    # Enable/disable updating the policy route. | Default: enable
    update_policy_route: Literal["enable", "disable"]
    # Enable/disable this link monitor. | Default: enable
    status: Literal["enable", "disable"]
    # Differentiated services code point (DSCP) in the IP header o
    diffservcode: str
    # Traffic class ID. | Default: 0 | Min: 0 | Max: 4294967295
    class_id: int
    # Only use monitor to read quality values. If enabled, static | Default: disable
    service_detection: Literal["enable", "disable"]
    # Servers for link-monitor to monitor.
    server_list: list[LinkMonitorServerlistObject]
    
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
    def to_dict(self) -> LinkMonitorPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LinkMonitor:
    """
    Configure Link Health Monitor.
    
    Path: system/link_monitor
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
    ) -> LinkMonitorObject: ...
    
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
    ) -> LinkMonitorObject: ...
    
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
    ) -> FortiObjectList[LinkMonitorObject]: ...
    
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
    ) -> LinkMonitorObject: ...
    
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
    ) -> LinkMonitorObject: ...
    
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
    ) -> FortiObjectList[LinkMonitorObject]: ...
    
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
    ) -> LinkMonitorObject: ...
    
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
    ) -> LinkMonitorObject: ...
    
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
    ) -> FortiObjectList[LinkMonitorObject]: ...
    
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
    ) -> LinkMonitorObject | list[LinkMonitorObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> LinkMonitorObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> LinkMonitorObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LinkMonitorObject: ...
    
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
        payload_dict: LinkMonitorPayload | None = ...,
        name: str | None = ...,
        addr_mode: Literal["ipv4", "ipv6"] | None = ...,
        srcintf: str | None = ...,
        server_config: Literal["default", "individual"] | None = ...,
        server_type: Literal["static", "dynamic"] | None = ...,
        server: str | list[str] | list[dict[str, Any]] | None = ...,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = ...,
        port: int | None = ...,
        gateway_ip: str | None = ...,
        gateway_ip6: str | None = ...,
        route: str | list[str] | list[dict[str, Any]] | None = ...,
        source_ip: str | None = ...,
        source_ip6: str | None = ...,
        http_get: str | None = ...,
        http_agent: str | None = ...,
        http_match: str | None = ...,
        interval: int | None = ...,
        probe_timeout: int | None = ...,
        failtime: int | None = ...,
        recoverytime: int | None = ...,
        probe_count: int | None = ...,
        security_mode: Literal["none", "authentication"] | None = ...,
        password: str | None = ...,
        packet_size: int | None = ...,
        ha_priority: int | None = ...,
        fail_weight: int | None = ...,
        update_cascade_interface: Literal["enable", "disable"] | None = ...,
        update_static_route: Literal["enable", "disable"] | None = ...,
        update_policy_route: Literal["enable", "disable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        diffservcode: str | None = ...,
        class_id: int | None = ...,
        service_detection: Literal["enable", "disable"] | None = ...,
        server_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "LinkMonitor",
    "LinkMonitorPayload",
    "LinkMonitorResponse",
    "LinkMonitorObject",
]
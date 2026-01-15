from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SdwanPayload(TypedDict, total=False):
    """
    Type hints for system/sdwan payload fields.
    
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    **Usage:**
        payload: SdwanPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["disable", "enable"]  # Enable/disable SD-WAN. | Default: disable
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]  # Algorithm or mode to use for load balancing Intern | Default: source-ip-based
    speedtest_bypass_routing: Literal["disable", "enable"]  # Enable/disable bypass routing when speedtest on a | Default: disable
    duplication_max_num: int  # Maximum number of interface members a packet is du | Default: 2 | Min: 2 | Max: 4
    duplication_max_discrepancy: int  # Maximum discrepancy between two packets for dedupl | Default: 250 | Min: 250 | Max: 1000
    neighbor_hold_down: Literal["enable", "disable"]  # Enable/disable hold switching from the secondary n | Default: disable
    neighbor_hold_down_time: int  # Waiting period in seconds when switching from the | Default: 0 | Min: 0 | Max: 10000000
    app_perf_log_period: int  # Time interval in seconds that application performa | Default: 0 | Min: 0 | Max: 3600
    neighbor_hold_boot_time: int  # Waiting period in seconds when switching from the | Default: 0 | Min: 0 | Max: 10000000
    fail_detect: Literal["enable", "disable"]  # Enable/disable SD-WAN Internet connection status c | Default: disable
    fail_alert_interfaces: list[dict[str, Any]]  # Physical interfaces that will be alerted.
    zone: list[dict[str, Any]]  # Configure SD-WAN zones.
    members: list[dict[str, Any]]  # FortiGate interfaces added to the SD-WAN.
    health_check: list[dict[str, Any]]  # SD-WAN status checking or health checking. Identif
    service: list[dict[str, Any]]  # Create SD-WAN rules (also called services) to cont
    neighbor: list[dict[str, Any]]  # Create SD-WAN neighbor from BGP neighbor table to
    duplication: list[dict[str, Any]]  # Create SD-WAN duplication rule.

# Nested TypedDicts for table field children (dict mode)

class SdwanFailalertinterfacesItem(TypedDict):
    """Type hints for fail-alert-interfaces table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Physical interface name. | MaxLen: 79


class SdwanZoneItem(TypedDict):
    """Type hints for zone table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Zone name. | MaxLen: 35
    advpn_select: Literal["enable", "disable"]  # Enable/disable selection of ADVPN based on SDWAN i | Default: disable
    advpn_health_check: str  # Health check for ADVPN local overlay link quality. | MaxLen: 35
    service_sla_tie_break: Literal["cfg-order", "fib-best-match", "priority", "input-device"]  # Method of selecting member if more than one meets | Default: cfg-order
    minimum_sla_meet_members: int  # Minimum number of members which meet SLA when the | Default: 1 | Min: 1 | Max: 255


class SdwanMembersItem(TypedDict):
    """Type hints for members table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    seq_num: int  # Sequence number(1-512). | Default: 0 | Min: 0 | Max: 512
    interface: str  # Interface name. | MaxLen: 15
    zone: str  # Zone name. | Default: virtual-wan-link | MaxLen: 35
    gateway: str  # The default gateway for this interface. Usually th | Default: 0.0.0.0
    preferred_source: str  # Preferred source of route for this member. | Default: 0.0.0.0
    source: str  # Source IP address used in the health-check packet | Default: 0.0.0.0
    gateway6: str  # IPv6 gateway. | Default: ::
    source6: str  # Source IPv6 address used in the health-check packe | Default: ::
    cost: int  # Cost of this interface for services in SLA mode | Default: 0 | Min: 0 | Max: 4294967295
    weight: int  # Weight of this interface for weighted load balanci | Default: 1 | Min: 1 | Max: 255
    priority: int  # Priority of the interface for IPv4 | Default: 1 | Min: 1 | Max: 65535
    priority6: int  # Priority of the interface for IPv6 | Default: 1024 | Min: 1 | Max: 65535
    priority_in_sla: int  # Preferred priority of routes to this member when t | Default: 0 | Min: 0 | Max: 65535
    priority_out_sla: int  # Preferred priority of routes to this member when t | Default: 0 | Min: 0 | Max: 65535
    spillover_threshold: int  # Egress spillover threshold for this interface | Default: 0 | Min: 0 | Max: 16776000
    ingress_spillover_threshold: int  # Ingress spillover threshold for this interface | Default: 0 | Min: 0 | Max: 16776000
    volume_ratio: int  # Measured volume ratio | Default: 1 | Min: 1 | Max: 255
    status: Literal["disable", "enable"]  # Enable/disable this interface in the SD-WAN. | Default: enable
    transport_group: int  # Measured transport group (0 - 255). | Default: 0 | Min: 0 | Max: 255
    comment: str  # Comments. | MaxLen: 255


class SdwanHealthcheckItem(TypedDict):
    """Type hints for health-check table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Status check or health check name. | MaxLen: 35
    fortiguard: Literal["disable", "enable"]  # Enable/disable use of FortiGuard predefined server | Default: disable
    fortiguard_name: str  # Predefined health-check target name. | MaxLen: 35
    probe_packets: Literal["disable", "enable"]  # Enable/disable transmission of probe packets. | Default: enable
    addr_mode: Literal["ipv4", "ipv6"]  # Address mode (IPv4 or IPv6). | Default: ipv4
    system_dns: Literal["disable", "enable"]  # Enable/disable system DNS as the probe server. | Default: disable
    server: str  # IP address or FQDN name of the server. | MaxLen: 79
    detect_mode: Literal["active", "passive", "prefer-passive", "remote", "agent-based"]  # The mode determining how to detect the server. | Default: active
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]  # Protocol used to determine if the FortiGate can co | Default: ping
    port: int  # Port number used to communicate with the server ov | Default: 0 | Min: 0 | Max: 65535
    quality_measured_method: Literal["half-open", "half-close"]  # Method to measure the quality of tcp-connect. | Default: half-open
    security_mode: Literal["none", "authentication"]  # Twamp controller security mode. | Default: none
    user: str  # The user name to access probe server. | MaxLen: 64
    password: str  # TWAMP controller password in authentication mode. | MaxLen: 128
    packet_size: int  # Packet size of a TWAMP test session. | Default: 124 | Min: 0 | Max: 65535
    ha_priority: int  # HA election priority (1 - 50). | Default: 1 | Min: 1 | Max: 50
    ftp_mode: Literal["passive", "port"]  # FTP mode. | Default: passive
    ftp_file: str  # Full path and file name on the FTP server to downl | MaxLen: 254
    http_get: str  # URL used to communicate with the server if the pro | Default: / | MaxLen: 1024
    http_agent: str  # String in the http-agent field in the HTTP header. | Default: Chrome/ Safari/ | MaxLen: 1024
    http_match: str  # Response string expected from the server if the pr | MaxLen: 1024
    dns_request_domain: str  # Fully qualified domain name to resolve for the DNS | Default: www.example.com | MaxLen: 255
    dns_match_ip: str  # Response IP expected from DNS server if the protoc | Default: 0.0.0.0
    interval: int  # Status check interval in milliseconds, or the time | Default: 500 | Min: 20 | Max: 3600000
    probe_timeout: int  # Time to wait before a probe packet is considered l | Default: 500 | Min: 20 | Max: 3600000
    agent_probe_timeout: int  # Time to wait before a probe packet is considered l | Default: 60000 | Min: 5000 | Max: 3600000
    remote_probe_timeout: int  # Time to wait before a probe packet is considered l | Default: 5000 | Min: 20 | Max: 3600000
    failtime: int  # Number of failures before server is considered los | Default: 5 | Min: 1 | Max: 3600
    recoverytime: int  # Number of successful responses received before ser | Default: 5 | Min: 1 | Max: 3600
    probe_count: int  # Number of most recent probes that should be used t | Default: 30 | Min: 5 | Max: 30
    diffservcode: str  # Differentiated services code point (DSCP) in the I
    update_cascade_interface: Literal["enable", "disable"]  # Enable/disable update cascade interface. | Default: enable
    update_static_route: Literal["enable", "disable"]  # Enable/disable updating the static route. | Default: enable
    update_bgp_route: Literal["enable", "disable"]  # Enable/disable updating the BGP route. | Default: disable
    embed_measured_health: Literal["enable", "disable"]  # Enable/disable embedding measured health informati | Default: disable
    sla_id_redistribute: int  # Select the ID from the SLA sub-table. The selected | Default: 0 | Min: 0 | Max: 32
    sla_fail_log_period: int  # Time interval in seconds that SLA fail log message | Default: 0 | Min: 0 | Max: 3600
    sla_pass_log_period: int  # Time interval in seconds that SLA pass log message | Default: 0 | Min: 0 | Max: 3600
    threshold_warning_packetloss: int  # Warning threshold for packet loss | Default: 0 | Min: 0 | Max: 100
    threshold_alert_packetloss: int  # Alert threshold for packet loss | Default: 0 | Min: 0 | Max: 100
    threshold_warning_latency: int  # Warning threshold for latency (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    threshold_alert_latency: int  # Alert threshold for latency (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    threshold_warning_jitter: int  # Warning threshold for jitter (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    threshold_alert_jitter: int  # Alert threshold for jitter (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    vrf: int  # Virtual Routing Forwarding ID. | Default: 0 | Min: 0 | Max: 511
    source: str  # Source IP address used in the health-check packet | Default: 0.0.0.0
    source6: str  # Source IPv6 address used in the health-check packe | Default: ::
    members: str  # Member sequence number list.
    mos_codec: Literal["g711", "g722", "g729"]  # Codec to use for MOS calculation (default = g711). | Default: g711
    class_id: int  # Traffic class ID. | Default: 0 | Min: 0 | Max: 4294967295
    packet_loss_weight: int  # Coefficient of packet-loss in the formula of custo | Default: 0 | Min: 0 | Max: 10000000
    latency_weight: int  # Coefficient of latency in the formula of custom-pr | Default: 0 | Min: 0 | Max: 10000000
    jitter_weight: int  # Coefficient of jitter in the formula of custom-pro | Default: 0 | Min: 0 | Max: 10000000
    bandwidth_weight: int  # Coefficient of reciprocal of available bidirection | Default: 0 | Min: 0 | Max: 10000000
    sla: str  # Service level agreement (SLA).


class SdwanServiceItem(TypedDict):
    """Type hints for service table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # SD-WAN rule ID (1 - 4000). | Default: 0 | Min: 1 | Max: 4000
    name: str  # SD-WAN rule name. | MaxLen: 35
    addr_mode: Literal["ipv4", "ipv6"]  # Address mode (IPv4 or IPv6). | Default: ipv4
    load_balance: Literal["enable", "disable"]  # Enable/disable load-balance. | Default: disable
    input_device: str  # Source interface name.
    input_device_negate: Literal["enable", "disable"]  # Enable/disable negation of input device match. | Default: disable
    input_zone: str  # Source input-zone name.
    mode: Literal["auto", "manual", "priority", "sla"]  # Control how the SD-WAN rule sets the priority of i | Default: manual
    zone_mode: Literal["enable", "disable"]  # Enable/disable zone mode. | Default: disable
    minimum_sla_meet_members: int  # Minimum number of members which meet SLA. | Default: 0 | Min: 0 | Max: 255
    hash_mode: Literal["round-robin", "source-ip-based", "source-dest-ip-based", "inbandwidth", "outbandwidth", "bibandwidth"]  # Hash algorithm for selected priority members for l | Default: round-robin
    shortcut_priority: Literal["enable", "disable", "auto"]  # High priority of ADVPN shortcut for this service. | Default: auto
    role: Literal["standalone", "primary", "secondary"]  # Service role to work with neighbor. | Default: standalone
    standalone_action: Literal["enable", "disable"]  # Enable/disable service when selected neighbor role | Default: disable
    quality_link: int  # Quality grade. | Default: 0 | Min: 0 | Max: 255
    tos: str  # Type of service bit pattern.
    tos_mask: str  # Type of service evaluated bits.
    protocol: int  # Protocol number. | Default: 0 | Min: 0 | Max: 255
    start_port: int  # Start destination port number. | Default: 1 | Min: 0 | Max: 65535
    end_port: int  # End destination port number. | Default: 65535 | Min: 0 | Max: 65535
    start_src_port: int  # Start source port number. | Default: 1 | Min: 0 | Max: 65535
    end_src_port: int  # End source port number. | Default: 65535 | Min: 0 | Max: 65535
    dst: str  # Destination address name.
    dst_negate: Literal["enable", "disable"]  # Enable/disable negation of destination address mat | Default: disable
    src: str  # Source address name.
    dst6: str  # Destination address6 name.
    src6: str  # Source address6 name.
    src_negate: Literal["enable", "disable"]  # Enable/disable negation of source address match. | Default: disable
    users: str  # User name.
    groups: str  # User groups.
    internet_service: Literal["enable", "disable"]  # Enable/disable use of Internet service for applica | Default: disable
    internet_service_custom: str  # Custom Internet service name list.
    internet_service_custom_group: str  # Custom Internet Service group list.
    internet_service_fortiguard: str  # FortiGuard Internet service name list.
    internet_service_name: str  # Internet service name list.
    internet_service_group: str  # Internet Service group list.
    internet_service_app_ctrl: str  # Application control based Internet Service ID list
    internet_service_app_ctrl_group: str  # Application control based Internet Service group l
    internet_service_app_ctrl_category: str  # IDs of one or more application control categories.
    health_check: str  # Health check list.
    link_cost_factor: Literal["latency", "jitter", "packet-loss", "inbandwidth", "outbandwidth", "bibandwidth", "custom-profile-1"]  # Link cost factor. | Default: latency
    packet_loss_weight: int  # Coefficient of packet-loss in the formula of custo | Default: 0 | Min: 0 | Max: 10000000
    latency_weight: int  # Coefficient of latency in the formula of custom-pr | Default: 0 | Min: 0 | Max: 10000000
    jitter_weight: int  # Coefficient of jitter in the formula of custom-pro | Default: 0 | Min: 0 | Max: 10000000
    bandwidth_weight: int  # Coefficient of reciprocal of available bidirection | Default: 0 | Min: 0 | Max: 10000000
    link_cost_threshold: int  # Percentage threshold change of link cost values th | Default: 10 | Min: 0 | Max: 10000000
    hold_down_time: int  # Waiting period in seconds when switching from the | Default: 0 | Min: 0 | Max: 10000000
    sla_stickiness: Literal["enable", "disable"]  # Enable/disable SLA stickiness (default = disable). | Default: disable
    dscp_forward: Literal["enable", "disable"]  # Enable/disable forward traffic DSCP tag. | Default: disable
    dscp_reverse: Literal["enable", "disable"]  # Enable/disable reverse traffic DSCP tag. | Default: disable
    dscp_forward_tag: str  # Forward traffic DSCP tag.
    dscp_reverse_tag: str  # Reverse traffic DSCP tag.
    sla: str  # Service level agreement (SLA).
    priority_members: str  # Member sequence number list.
    priority_zone: str  # Priority zone name list.
    status: Literal["enable", "disable"]  # Enable/disable SD-WAN service. | Default: enable
    gateway: Literal["enable", "disable"]  # Enable/disable SD-WAN service gateway. | Default: disable
    default: Literal["enable", "disable"]  # Enable/disable use of SD-WAN as default service. | Default: disable
    sla_compare_method: Literal["order", "number"]  # Method to compare SLA value for SLA mode. | Default: order
    fib_best_match_force: Literal["disable", "enable"]  # Enable/disable force using fib-best-match oif as o | Default: disable
    tie_break: Literal["zone", "cfg-order", "fib-best-match", "priority", "input-device"]  # Method of selecting member if more than one meets | Default: zone
    use_shortcut_sla: Literal["enable", "disable"]  # Enable/disable use of ADVPN shortcut for quality c | Default: enable
    passive_measurement: Literal["enable", "disable"]  # Enable/disable passive measurement based on the se | Default: disable
    agent_exclusive: Literal["enable", "disable"]  # Set/unset the service as agent use exclusively. | Default: disable
    shortcut: Literal["enable", "disable"]  # Enable/disable shortcut for this service. | Default: enable
    comment: str  # Comments. | MaxLen: 255


class SdwanNeighborItem(TypedDict):
    """Type hints for neighbor table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip: str  # IP/IPv6 address of neighbor or neighbor-group name | MaxLen: 45
    member: str  # Member sequence number list.
    service_id: int  # SD-WAN service ID to work with the neighbor. | Default: 0 | Min: 0 | Max: 4294967295
    minimum_sla_meet_members: int  # Minimum number of members which meet SLA when the | Default: 1 | Min: 1 | Max: 255
    mode: Literal["sla", "speedtest"]  # What metric to select the neighbor. | Default: sla
    role: Literal["standalone", "primary", "secondary"]  # Role of neighbor. | Default: standalone
    route_metric: Literal["preferable", "priority"]  # Route-metric of neighbor. | Default: preferable
    health_check: str  # SD-WAN health-check name. | MaxLen: 35
    sla_id: int  # SLA ID. | Default: 0 | Min: 0 | Max: 4294967295


class SdwanDuplicationItem(TypedDict):
    """Type hints for duplication table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Duplication rule ID (1 - 255). | Default: 0 | Min: 1 | Max: 255
    service_id: str  # SD-WAN service rule ID list.
    srcaddr: str  # Source address or address group names.
    dstaddr: str  # Destination address or address group names.
    srcaddr6: str  # Source address6 or address6 group names.
    dstaddr6: str  # Destination address6 or address6 group names.
    srcintf: str  # Incoming (ingress) interfaces or zones.
    dstintf: str  # Outgoing (egress) interfaces or zones.
    service: str  # Service and service group name.
    packet_duplication: Literal["disable", "force", "on-demand"]  # Configure packet duplication method. | Default: disable
    sla_match_service: Literal["enable", "disable"]  # Enable/disable packet duplication matching health- | Default: disable
    packet_de_duplication: Literal["enable", "disable"]  # Enable/disable discarding of packets that have bee | Default: disable


# Nested classes for table field children (object mode)

@final
class SdwanFailalertinterfacesObject:
    """Typed object for fail-alert-interfaces table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Physical interface name. | MaxLen: 79
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
class SdwanZoneObject:
    """Typed object for zone table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Zone name. | MaxLen: 35
    name: str
    # Enable/disable selection of ADVPN based on SDWAN information | Default: disable
    advpn_select: Literal["enable", "disable"]
    # Health check for ADVPN local overlay link quality. | MaxLen: 35
    advpn_health_check: str
    # Method of selecting member if more than one meets the SLA. | Default: cfg-order
    service_sla_tie_break: Literal["cfg-order", "fib-best-match", "priority", "input-device"]
    # Minimum number of members which meet SLA when the neighbor i | Default: 1 | Min: 1 | Max: 255
    minimum_sla_meet_members: int
    
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
class SdwanMembersObject:
    """Typed object for members table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Sequence number(1-512). | Default: 0 | Min: 0 | Max: 512
    seq_num: int
    # Interface name. | MaxLen: 15
    interface: str
    # Zone name. | Default: virtual-wan-link | MaxLen: 35
    zone: str
    # The default gateway for this interface. Usually the default | Default: 0.0.0.0
    gateway: str
    # Preferred source of route for this member. | Default: 0.0.0.0
    preferred_source: str
    # Source IP address used in the health-check packet to the ser | Default: 0.0.0.0
    source: str
    # IPv6 gateway. | Default: ::
    gateway6: str
    # Source IPv6 address used in the health-check packet to the s | Default: ::
    source6: str
    # Cost of this interface for services in SLA mode | Default: 0 | Min: 0 | Max: 4294967295
    cost: int
    # Weight of this interface for weighted load balancing. | Default: 1 | Min: 1 | Max: 255
    weight: int
    # Priority of the interface for IPv4 (1 - 65535, default = 1). | Default: 1 | Min: 1 | Max: 65535
    priority: int
    # Priority of the interface for IPv6 | Default: 1024 | Min: 1 | Max: 65535
    priority6: int
    # Preferred priority of routes to this member when this member | Default: 0 | Min: 0 | Max: 65535
    priority_in_sla: int
    # Preferred priority of routes to this member when this member | Default: 0 | Min: 0 | Max: 65535
    priority_out_sla: int
    # Egress spillover threshold for this interface | Default: 0 | Min: 0 | Max: 16776000
    spillover_threshold: int
    # Ingress spillover threshold for this interface | Default: 0 | Min: 0 | Max: 16776000
    ingress_spillover_threshold: int
    # Measured volume ratio | Default: 1 | Min: 1 | Max: 255
    volume_ratio: int
    # Enable/disable this interface in the SD-WAN. | Default: enable
    status: Literal["disable", "enable"]
    # Measured transport group (0 - 255). | Default: 0 | Min: 0 | Max: 255
    transport_group: int
    # Comments. | MaxLen: 255
    comment: str
    
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
class SdwanHealthcheckObject:
    """Typed object for health-check table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Status check or health check name. | MaxLen: 35
    name: str
    # Enable/disable use of FortiGuard predefined server. | Default: disable
    fortiguard: Literal["disable", "enable"]
    # Predefined health-check target name. | MaxLen: 35
    fortiguard_name: str
    # Enable/disable transmission of probe packets. | Default: enable
    probe_packets: Literal["disable", "enable"]
    # Address mode (IPv4 or IPv6). | Default: ipv4
    addr_mode: Literal["ipv4", "ipv6"]
    # Enable/disable system DNS as the probe server. | Default: disable
    system_dns: Literal["disable", "enable"]
    # IP address or FQDN name of the server. | MaxLen: 79
    server: str
    # The mode determining how to detect the server. | Default: active
    detect_mode: Literal["active", "passive", "prefer-passive", "remote", "agent-based"]
    # Protocol used to determine if the FortiGate can communicate | Default: ping
    protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp", "dns", "tcp-connect", "ftp"]
    # Port number used to communicate with the server over the sel | Default: 0 | Min: 0 | Max: 65535
    port: int
    # Method to measure the quality of tcp-connect. | Default: half-open
    quality_measured_method: Literal["half-open", "half-close"]
    # Twamp controller security mode. | Default: none
    security_mode: Literal["none", "authentication"]
    # The user name to access probe server. | MaxLen: 64
    user: str
    # TWAMP controller password in authentication mode. | MaxLen: 128
    password: str
    # Packet size of a TWAMP test session. (124/158 - 1024) | Default: 124 | Min: 0 | Max: 65535
    packet_size: int
    # HA election priority (1 - 50). | Default: 1 | Min: 1 | Max: 50
    ha_priority: int
    # FTP mode. | Default: passive
    ftp_mode: Literal["passive", "port"]
    # Full path and file name on the FTP server to download for FT | MaxLen: 254
    ftp_file: str
    # URL used to communicate with the server if the protocol if t | Default: / | MaxLen: 1024
    http_get: str
    # String in the http-agent field in the HTTP header. | Default: Chrome/ Safari/ | MaxLen: 1024
    http_agent: str
    # Response string expected from the server if the protocol is | MaxLen: 1024
    http_match: str
    # Fully qualified domain name to resolve for the DNS probe. | Default: www.example.com | MaxLen: 255
    dns_request_domain: str
    # Response IP expected from DNS server if the protocol is DNS. | Default: 0.0.0.0
    dns_match_ip: str
    # Status check interval in milliseconds, or the time between a | Default: 500 | Min: 20 | Max: 3600000
    interval: int
    # Time to wait before a probe packet is considered lost | Default: 500 | Min: 20 | Max: 3600000
    probe_timeout: int
    # Time to wait before a probe packet is considered lost when d | Default: 60000 | Min: 5000 | Max: 3600000
    agent_probe_timeout: int
    # Time to wait before a probe packet is considered lost when d | Default: 5000 | Min: 20 | Max: 3600000
    remote_probe_timeout: int
    # Number of failures before server is considered lost | Default: 5 | Min: 1 | Max: 3600
    failtime: int
    # Number of successful responses received before server is con | Default: 5 | Min: 1 | Max: 3600
    recoverytime: int
    # Number of most recent probes that should be used to calculat | Default: 30 | Min: 5 | Max: 30
    probe_count: int
    # Differentiated services code point (DSCP) in the IP header o
    diffservcode: str
    # Enable/disable update cascade interface. | Default: enable
    update_cascade_interface: Literal["enable", "disable"]
    # Enable/disable updating the static route. | Default: enable
    update_static_route: Literal["enable", "disable"]
    # Enable/disable updating the BGP route. | Default: disable
    update_bgp_route: Literal["enable", "disable"]
    # Enable/disable embedding measured health information. | Default: disable
    embed_measured_health: Literal["enable", "disable"]
    # Select the ID from the SLA sub-table. The selected SLA's pri | Default: 0 | Min: 0 | Max: 32
    sla_id_redistribute: int
    # Time interval in seconds that SLA fail log messages will be | Default: 0 | Min: 0 | Max: 3600
    sla_fail_log_period: int
    # Time interval in seconds that SLA pass log messages will be | Default: 0 | Min: 0 | Max: 3600
    sla_pass_log_period: int
    # Warning threshold for packet loss (percentage, default = 0). | Default: 0 | Min: 0 | Max: 100
    threshold_warning_packetloss: int
    # Alert threshold for packet loss (percentage, default = 0). | Default: 0 | Min: 0 | Max: 100
    threshold_alert_packetloss: int
    # Warning threshold for latency (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    threshold_warning_latency: int
    # Alert threshold for latency (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    threshold_alert_latency: int
    # Warning threshold for jitter (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    threshold_warning_jitter: int
    # Alert threshold for jitter (ms, default = 0). | Default: 0 | Min: 0 | Max: 4294967295
    threshold_alert_jitter: int
    # Virtual Routing Forwarding ID. | Default: 0 | Min: 0 | Max: 511
    vrf: int
    # Source IP address used in the health-check packet to the ser | Default: 0.0.0.0
    source: str
    # Source IPv6 address used in the health-check packet to serve | Default: ::
    source6: str
    # Member sequence number list.
    members: str
    # Codec to use for MOS calculation (default = g711). | Default: g711
    mos_codec: Literal["g711", "g722", "g729"]
    # Traffic class ID. | Default: 0 | Min: 0 | Max: 4294967295
    class_id: int
    # Coefficient of packet-loss in the formula of custom-profile- | Default: 0 | Min: 0 | Max: 10000000
    packet_loss_weight: int
    # Coefficient of latency in the formula of custom-profile-1. | Default: 0 | Min: 0 | Max: 10000000
    latency_weight: int
    # Coefficient of jitter in the formula of custom-profile-1. | Default: 0 | Min: 0 | Max: 10000000
    jitter_weight: int
    # Coefficient of reciprocal of available bidirectional bandwid | Default: 0 | Min: 0 | Max: 10000000
    bandwidth_weight: int
    # Service level agreement (SLA).
    sla: str
    
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
class SdwanServiceObject:
    """Typed object for service table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SD-WAN rule ID (1 - 4000). | Default: 0 | Min: 1 | Max: 4000
    id: int
    # SD-WAN rule name. | MaxLen: 35
    name: str
    # Address mode (IPv4 or IPv6). | Default: ipv4
    addr_mode: Literal["ipv4", "ipv6"]
    # Enable/disable load-balance. | Default: disable
    load_balance: Literal["enable", "disable"]
    # Source interface name.
    input_device: str
    # Enable/disable negation of input device match. | Default: disable
    input_device_negate: Literal["enable", "disable"]
    # Source input-zone name.
    input_zone: str
    # Control how the SD-WAN rule sets the priority of interfaces | Default: manual
    mode: Literal["auto", "manual", "priority", "sla"]
    # Enable/disable zone mode. | Default: disable
    zone_mode: Literal["enable", "disable"]
    # Minimum number of members which meet SLA. | Default: 0 | Min: 0 | Max: 255
    minimum_sla_meet_members: int
    # Hash algorithm for selected priority members for load balanc | Default: round-robin
    hash_mode: Literal["round-robin", "source-ip-based", "source-dest-ip-based", "inbandwidth", "outbandwidth", "bibandwidth"]
    # High priority of ADVPN shortcut for this service. | Default: auto
    shortcut_priority: Literal["enable", "disable", "auto"]
    # Service role to work with neighbor. | Default: standalone
    role: Literal["standalone", "primary", "secondary"]
    # Enable/disable service when selected neighbor role is standa | Default: disable
    standalone_action: Literal["enable", "disable"]
    # Quality grade. | Default: 0 | Min: 0 | Max: 255
    quality_link: int
    # Type of service bit pattern.
    tos: str
    # Type of service evaluated bits.
    tos_mask: str
    # Protocol number. | Default: 0 | Min: 0 | Max: 255
    protocol: int
    # Start destination port number. | Default: 1 | Min: 0 | Max: 65535
    start_port: int
    # End destination port number. | Default: 65535 | Min: 0 | Max: 65535
    end_port: int
    # Start source port number. | Default: 1 | Min: 0 | Max: 65535
    start_src_port: int
    # End source port number. | Default: 65535 | Min: 0 | Max: 65535
    end_src_port: int
    # Destination address name.
    dst: str
    # Enable/disable negation of destination address match. | Default: disable
    dst_negate: Literal["enable", "disable"]
    # Source address name.
    src: str
    # Destination address6 name.
    dst6: str
    # Source address6 name.
    src6: str
    # Enable/disable negation of source address match. | Default: disable
    src_negate: Literal["enable", "disable"]
    # User name.
    users: str
    # User groups.
    groups: str
    # Enable/disable use of Internet service for application-based | Default: disable
    internet_service: Literal["enable", "disable"]
    # Custom Internet service name list.
    internet_service_custom: str
    # Custom Internet Service group list.
    internet_service_custom_group: str
    # FortiGuard Internet service name list.
    internet_service_fortiguard: str
    # Internet service name list.
    internet_service_name: str
    # Internet Service group list.
    internet_service_group: str
    # Application control based Internet Service ID list.
    internet_service_app_ctrl: str
    # Application control based Internet Service group list.
    internet_service_app_ctrl_group: str
    # IDs of one or more application control categories.
    internet_service_app_ctrl_category: str
    # Health check list.
    health_check: str
    # Link cost factor. | Default: latency
    link_cost_factor: Literal["latency", "jitter", "packet-loss", "inbandwidth", "outbandwidth", "bibandwidth", "custom-profile-1"]
    # Coefficient of packet-loss in the formula of custom-profile- | Default: 0 | Min: 0 | Max: 10000000
    packet_loss_weight: int
    # Coefficient of latency in the formula of custom-profile-1. | Default: 0 | Min: 0 | Max: 10000000
    latency_weight: int
    # Coefficient of jitter in the formula of custom-profile-1. | Default: 0 | Min: 0 | Max: 10000000
    jitter_weight: int
    # Coefficient of reciprocal of available bidirectional bandwid | Default: 0 | Min: 0 | Max: 10000000
    bandwidth_weight: int
    # Percentage threshold change of link cost values that will re | Default: 10 | Min: 0 | Max: 10000000
    link_cost_threshold: int
    # Waiting period in seconds when switching from the back-up me | Default: 0 | Min: 0 | Max: 10000000
    hold_down_time: int
    # Enable/disable SLA stickiness (default = disable). | Default: disable
    sla_stickiness: Literal["enable", "disable"]
    # Enable/disable forward traffic DSCP tag. | Default: disable
    dscp_forward: Literal["enable", "disable"]
    # Enable/disable reverse traffic DSCP tag. | Default: disable
    dscp_reverse: Literal["enable", "disable"]
    # Forward traffic DSCP tag.
    dscp_forward_tag: str
    # Reverse traffic DSCP tag.
    dscp_reverse_tag: str
    # Service level agreement (SLA).
    sla: str
    # Member sequence number list.
    priority_members: str
    # Priority zone name list.
    priority_zone: str
    # Enable/disable SD-WAN service. | Default: enable
    status: Literal["enable", "disable"]
    # Enable/disable SD-WAN service gateway. | Default: disable
    gateway: Literal["enable", "disable"]
    # Enable/disable use of SD-WAN as default service. | Default: disable
    default: Literal["enable", "disable"]
    # Method to compare SLA value for SLA mode. | Default: order
    sla_compare_method: Literal["order", "number"]
    # Enable/disable force using fib-best-match oif as outgoing in | Default: disable
    fib_best_match_force: Literal["disable", "enable"]
    # Method of selecting member if more than one meets the SLA. | Default: zone
    tie_break: Literal["zone", "cfg-order", "fib-best-match", "priority", "input-device"]
    # Enable/disable use of ADVPN shortcut for quality comparison. | Default: enable
    use_shortcut_sla: Literal["enable", "disable"]
    # Enable/disable passive measurement based on the service crit | Default: disable
    passive_measurement: Literal["enable", "disable"]
    # Set/unset the service as agent use exclusively. | Default: disable
    agent_exclusive: Literal["enable", "disable"]
    # Enable/disable shortcut for this service. | Default: enable
    shortcut: Literal["enable", "disable"]
    # Comments. | MaxLen: 255
    comment: str
    
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
class SdwanNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP/IPv6 address of neighbor or neighbor-group name. | MaxLen: 45
    ip: str
    # Member sequence number list.
    member: str
    # SD-WAN service ID to work with the neighbor. | Default: 0 | Min: 0 | Max: 4294967295
    service_id: int
    # Minimum number of members which meet SLA when the neighbor i | Default: 1 | Min: 1 | Max: 255
    minimum_sla_meet_members: int
    # What metric to select the neighbor. | Default: sla
    mode: Literal["sla", "speedtest"]
    # Role of neighbor. | Default: standalone
    role: Literal["standalone", "primary", "secondary"]
    # Route-metric of neighbor. | Default: preferable
    route_metric: Literal["preferable", "priority"]
    # SD-WAN health-check name. | MaxLen: 35
    health_check: str
    # SLA ID. | Default: 0 | Min: 0 | Max: 4294967295
    sla_id: int
    
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
class SdwanDuplicationObject:
    """Typed object for duplication table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Duplication rule ID (1 - 255). | Default: 0 | Min: 1 | Max: 255
    id: int
    # SD-WAN service rule ID list.
    service_id: str
    # Source address or address group names.
    srcaddr: str
    # Destination address or address group names.
    dstaddr: str
    # Source address6 or address6 group names.
    srcaddr6: str
    # Destination address6 or address6 group names.
    dstaddr6: str
    # Incoming (ingress) interfaces or zones.
    srcintf: str
    # Outgoing (egress) interfaces or zones.
    dstintf: str
    # Service and service group name.
    service: str
    # Configure packet duplication method. | Default: disable
    packet_duplication: Literal["disable", "force", "on-demand"]
    # Enable/disable packet duplication matching health-check SLAs | Default: disable
    sla_match_service: Literal["enable", "disable"]
    # Enable/disable discarding of packets that have been duplicat | Default: disable
    packet_de_duplication: Literal["enable", "disable"]
    
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
class SdwanResponse(TypedDict):
    """
    Type hints for system/sdwan API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["disable", "enable"]  # Enable/disable SD-WAN. | Default: disable
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]  # Algorithm or mode to use for load balancing Intern | Default: source-ip-based
    speedtest_bypass_routing: Literal["disable", "enable"]  # Enable/disable bypass routing when speedtest on a | Default: disable
    duplication_max_num: int  # Maximum number of interface members a packet is du | Default: 2 | Min: 2 | Max: 4
    duplication_max_discrepancy: int  # Maximum discrepancy between two packets for dedupl | Default: 250 | Min: 250 | Max: 1000
    neighbor_hold_down: Literal["enable", "disable"]  # Enable/disable hold switching from the secondary n | Default: disable
    neighbor_hold_down_time: int  # Waiting period in seconds when switching from the | Default: 0 | Min: 0 | Max: 10000000
    app_perf_log_period: int  # Time interval in seconds that application performa | Default: 0 | Min: 0 | Max: 3600
    neighbor_hold_boot_time: int  # Waiting period in seconds when switching from the | Default: 0 | Min: 0 | Max: 10000000
    fail_detect: Literal["enable", "disable"]  # Enable/disable SD-WAN Internet connection status c | Default: disable
    fail_alert_interfaces: list[SdwanFailalertinterfacesItem]  # Physical interfaces that will be alerted.
    zone: list[SdwanZoneItem]  # Configure SD-WAN zones.
    members: list[SdwanMembersItem]  # FortiGate interfaces added to the SD-WAN.
    health_check: list[SdwanHealthcheckItem]  # SD-WAN status checking or health checking. Identif
    service: list[SdwanServiceItem]  # Create SD-WAN rules (also called services) to cont
    neighbor: list[SdwanNeighborItem]  # Create SD-WAN neighbor from BGP neighbor table to
    duplication: list[SdwanDuplicationItem]  # Create SD-WAN duplication rule.


@final
class SdwanObject:
    """Typed FortiObject for system/sdwan with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable SD-WAN. | Default: disable
    status: Literal["disable", "enable"]
    # Algorithm or mode to use for load balancing Internet traffic | Default: source-ip-based
    load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"]
    # Enable/disable bypass routing when speedtest on a SD-WAN mem | Default: disable
    speedtest_bypass_routing: Literal["disable", "enable"]
    # Maximum number of interface members a packet is duplicated i | Default: 2 | Min: 2 | Max: 4
    duplication_max_num: int
    # Maximum discrepancy between two packets for deduplication in | Default: 250 | Min: 250 | Max: 1000
    duplication_max_discrepancy: int
    # Enable/disable hold switching from the secondary neighbor to | Default: disable
    neighbor_hold_down: Literal["enable", "disable"]
    # Waiting period in seconds when switching from the secondary | Default: 0 | Min: 0 | Max: 10000000
    neighbor_hold_down_time: int
    # Time interval in seconds that application performance logs a | Default: 0 | Min: 0 | Max: 3600
    app_perf_log_period: int
    # Waiting period in seconds when switching from the primary ne | Default: 0 | Min: 0 | Max: 10000000
    neighbor_hold_boot_time: int
    # Enable/disable SD-WAN Internet connection status checking | Default: disable
    fail_detect: Literal["enable", "disable"]
    # Physical interfaces that will be alerted.
    fail_alert_interfaces: list[SdwanFailalertinterfacesObject]
    # Configure SD-WAN zones.
    zone: list[SdwanZoneObject]
    # FortiGate interfaces added to the SD-WAN.
    members: list[SdwanMembersObject]
    # SD-WAN status checking or health checking. Identify a server
    health_check: list[SdwanHealthcheckObject]
    # Create SD-WAN rules (also called services) to control how se
    service: list[SdwanServiceObject]
    # Create SD-WAN neighbor from BGP neighbor table to control ro
    neighbor: list[SdwanNeighborObject]
    # Create SD-WAN duplication rule.
    duplication: list[SdwanDuplicationObject]
    
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
    def to_dict(self) -> SdwanPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Sdwan:
    """
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    Path: system/sdwan
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject: ...
    
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
    ) -> SdwanObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> SdwanObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SdwanPayload | None = ...,
        status: Literal["disable", "enable"] | None = ...,
        load_balance_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based", "measured-volume-based"] | None = ...,
        speedtest_bypass_routing: Literal["disable", "enable"] | None = ...,
        duplication_max_num: int | None = ...,
        duplication_max_discrepancy: int | None = ...,
        neighbor_hold_down: Literal["enable", "disable"] | None = ...,
        neighbor_hold_down_time: int | None = ...,
        app_perf_log_period: int | None = ...,
        neighbor_hold_boot_time: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        zone: str | list[str] | list[dict[str, Any]] | None = ...,
        members: str | list[str] | list[dict[str, Any]] | None = ...,
        health_check: str | list[str] | list[dict[str, Any]] | None = ...,
        service: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        duplication: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Sdwan",
    "SdwanPayload",
    "SdwanResponse",
    "SdwanObject",
]
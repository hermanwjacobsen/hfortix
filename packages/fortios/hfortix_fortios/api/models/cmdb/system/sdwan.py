"""
Pydantic Models for CMDB - system/sdwan

Runtime validation models for system/sdwan configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SdwanFailAlertInterfaces(BaseModel):
    """
    Child table model for fail-alert-interfaces.
    
    Physical interfaces that will be alerted.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Physical interface name.")  # datasource: ['system.interface.name']
class SdwanZone(BaseModel):
    """
    Child table model for zone.
    
    Configure SD-WAN zones.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Zone name.")    
    advpn_select: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable selection of ADVPN based on SDWAN information.")    
    advpn_health_check: str | None = Field(max_length=35, default="", description="Health check for ADVPN local overlay link quality.")  # datasource: ['system.sdwan.health-check.name']    
    service_sla_tie_break: ServiceSlaTieBreakEnum | None = Field(default="cfg-order", description="Method of selecting member if more than one meets the SLA.")    
    minimum_sla_meet_members: int | None = Field(ge=1, le=255, default=1, description="Minimum number of members which meet SLA when the neighbor is preferred.")
class SdwanMembers(BaseModel):
    """
    Child table model for members.
    
    FortiGate interfaces added to the SD-WAN.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    seq_num: int | None = Field(ge=0, le=512, default=0, description="Sequence number(1-512).")    
    interface: str | None = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    zone: str | None = Field(max_length=35, default="virtual-wan-link", description="Zone name.")  # datasource: ['system.sdwan.zone.name']    
    gateway: str | None = Field(default="0.0.0.0", description="The default gateway for this interface. Usually the default gateway of the Internet service provider that this interface is connected to.")    
    preferred_source: str | None = Field(default="0.0.0.0", description="Preferred source of route for this member.")    
    source: str | None = Field(default="0.0.0.0", description="Source IP address used in the health-check packet to the server.")    
    gateway6: str | None = Field(default="::", description="IPv6 gateway.")    
    source6: str | None = Field(default="::", description="Source IPv6 address used in the health-check packet to the server.")    
    cost: int | None = Field(ge=0, le=4294967295, default=0, description="Cost of this interface for services in SLA mode (0 - 4294967295, default = 0).")    
    weight: int | None = Field(ge=1, le=255, default=1, description="Weight of this interface for weighted load balancing. (1 - 255) More traffic is directed to interfaces with higher weights.")    
    priority: int | None = Field(ge=1, le=65535, default=1, description="Priority of the interface for IPv4 (1 - 65535, default = 1). Used for SD-WAN rules or priority rules.")    
    priority6: int | None = Field(ge=1, le=65535, default=1024, description="Priority of the interface for IPv6 (1 - 65535, default = 1024). Used for SD-WAN rules or priority rules.")    
    priority_in_sla: int | None = Field(ge=0, le=65535, default=0, description="Preferred priority of routes to this member when this member is in-sla (0 - 65535, default = 0).")    
    priority_out_sla: int | None = Field(ge=0, le=65535, default=0, description="Preferred priority of routes to this member when this member is out-of-sla (0 - 65535, default = 0).")    
    spillover_threshold: int | None = Field(ge=0, le=16776000, default=0, description="Egress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN.")    
    ingress_spillover_threshold: int | None = Field(ge=0, le=16776000, default=0, description="Ingress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new sessions spill over to other interfaces in the SD-WAN.")    
    volume_ratio: int | None = Field(ge=1, le=255, default=1, description="Measured volume ratio (this value / sum of all values = percentage of link volume, 1 - 255).")    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable this interface in the SD-WAN.")    
    transport_group: int | None = Field(ge=0, le=255, default=0, description="Measured transport group (0 - 255).")    
    comment: str | None = Field(max_length=255, default=None, description="Comments.")
class SdwanHealthCheck(BaseModel):
    """
    Child table model for health-check.
    
    SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Status check or health check name.")    
    fortiguard: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of FortiGuard predefined server.")    
    fortiguard_name: str | None = Field(max_length=35, default="", description="Predefined health-check target name.")  # datasource: ['system.health-check-fortiguard.name']    
    probe_packets: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable transmission of probe packets.")    
    addr_mode: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address mode (IPv4 or IPv6).")    
    system_dns: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable system DNS as the probe server.")    
    server: list[Server] = Field(max_length=79, default="", description="IP address or FQDN name of the server.")    
    detect_mode: DetectModeEnum | None = Field(default="active", description="The mode determining how to detect the server.")    
    protocol: ProtocolEnum | None = Field(default="ping", description="Protocol used to determine if the FortiGate can communicate with the server.")    
    port: int | None = Field(ge=0, le=65535, default=0, description="Port number used to communicate with the server over the selected protocol (0 - 65535, default = 0, auto select. http, tcp-connect: 80, udp-echo, tcp-echo: 7, dns: 53, ftp: 21, twamp: 862).")    
    quality_measured_method: Literal["half-open", "half-close"] | None = Field(default="half-open", description="Method to measure the quality of tcp-connect.")    
    security_mode: Literal["none", "authentication"] | None = Field(default="none", description="Twamp controller security mode.")    
    user: str | None = Field(max_length=64, default="", description="The user name to access probe server.")    
    password: Any = Field(max_length=128, default=None, description="TWAMP controller password in authentication mode.")    
    packet_size: int | None = Field(ge=0, le=65535, default=124, description="Packet size of a TWAMP test session. (124/158 - 1024)")    
    ha_priority: int | None = Field(ge=1, le=50, default=1, description="HA election priority (1 - 50).")    
    ftp_mode: Literal["passive", "port"] | None = Field(default="passive", description="FTP mode.")    
    ftp_file: str | None = Field(max_length=254, default="", description="Full path and file name on the FTP server to download for FTP health-check to probe.")    
    http_get: str | None = Field(max_length=1024, default="/", description="URL used to communicate with the server if the protocol if the protocol is HTTP.")    
    http_agent: str | None = Field(max_length=1024, default="Chrome/ Safari/", description="String in the http-agent field in the HTTP header.")    
    http_match: str | None = Field(max_length=1024, default="", description="Response string expected from the server if the protocol is HTTP.")    
    dns_request_domain: str | None = Field(max_length=255, default="www.example.com", description="Fully qualified domain name to resolve for the DNS probe.")    
    dns_match_ip: str | None = Field(default="0.0.0.0", description="Response IP expected from DNS server if the protocol is DNS.")    
    interval: int | None = Field(ge=20, le=3600000, default=500, description="Status check interval in milliseconds, or the time between attempting to connect to the server (20 - 3600*1000 msec, default = 500).")    
    probe_timeout: int | None = Field(ge=20, le=3600000, default=500, description="Time to wait before a probe packet is considered lost (20 - 3600*1000 msec, default = 500).")    
    agent_probe_timeout: int | None = Field(ge=5000, le=3600000, default=60000, description="Time to wait before a probe packet is considered lost when detect-mode is agent (5000 - 3600*1000 msec, default = 60000).")    
    remote_probe_timeout: int | None = Field(ge=20, le=3600000, default=5000, description="Time to wait before a probe packet is considered lost when detect-mode is remote (20 - 3600*1000 msec, default = 5000).")    
    failtime: int | None = Field(ge=1, le=3600, default=5, description="Number of failures before server is considered lost (1 - 3600, default = 5).")    
    recoverytime: int | None = Field(ge=1, le=3600, default=5, description="Number of successful responses received before server is considered recovered (1 - 3600, default = 5).")    
    probe_count: int | None = Field(ge=5, le=30, default=30, description="Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).")    
    diffservcode: str | None = Field(default="", description="Differentiated services code point (DSCP) in the IP header of the probe packet.")    
    update_cascade_interface: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable update cascade interface.")    
    update_static_route: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable updating the static route.")    
    update_bgp_route: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable updating the BGP route.")    
    embed_measured_health: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable embedding measured health information.")    
    sla_id_redistribute: int | None = Field(ge=0, le=32, default=0, description="Select the ID from the SLA sub-table. The selected SLA's priority value will be distributed into the routing table (0 - 32, default = 0).")    
    sla_fail_log_period: int | None = Field(ge=0, le=3600, default=0, description="Time interval in seconds that SLA fail log messages will be generated (0 - 3600, default = 0).")    
    sla_pass_log_period: int | None = Field(ge=0, le=3600, default=0, description="Time interval in seconds that SLA pass log messages will be generated (0 - 3600, default = 0).")    
    threshold_warning_packetloss: int | None = Field(ge=0, le=100, default=0, description="Warning threshold for packet loss (percentage, default = 0).")    
    threshold_alert_packetloss: int | None = Field(ge=0, le=100, default=0, description="Alert threshold for packet loss (percentage, default = 0).")    
    threshold_warning_latency: int | None = Field(ge=0, le=4294967295, default=0, description="Warning threshold for latency (ms, default = 0).")    
    threshold_alert_latency: int | None = Field(ge=0, le=4294967295, default=0, description="Alert threshold for latency (ms, default = 0).")    
    threshold_warning_jitter: int | None = Field(ge=0, le=4294967295, default=0, description="Warning threshold for jitter (ms, default = 0).")    
    threshold_alert_jitter: int | None = Field(ge=0, le=4294967295, default=0, description="Alert threshold for jitter (ms, default = 0).")    
    vrf: int | None = Field(ge=0, le=511, default=0, description="Virtual Routing Forwarding ID.")    
    source: str | None = Field(default="0.0.0.0", description="Source IP address used in the health-check packet to the server.")    
    source6: str | None = Field(default="::", description="Source IPv6 address used in the health-check packet to server.")    
    members: list[Members] = Field(default=None, description="Member sequence number list.")    
    mos_codec: Literal["g711", "g722", "g729"] | None = Field(default="g711", description="Codec to use for MOS calculation (default = g711).")    
    class_id: int | None = Field(ge=0, le=4294967295, default=0, description="Traffic class ID.")  # datasource: ['firewall.traffic-class.class-id']    
    packet_loss_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of packet-loss in the formula of custom-profile-1.")    
    latency_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of latency in the formula of custom-profile-1.")    
    jitter_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of jitter in the formula of custom-profile-1.")    
    bandwidth_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.")    
    sla: list[Sla] = Field(default=None, description="Service level agreement (SLA).")
class SdwanService(BaseModel):
    """
    Child table model for service.
    
    Create SD-WAN rules (also called services) to control how sessions are distributed to interfaces in the SD-WAN.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=4000, default=0, description="SD-WAN rule ID (1 - 4000).")    
    name: str | None = Field(max_length=35, default="", description="SD-WAN rule name.")    
    addr_mode: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address mode (IPv4 or IPv6).")    
    load_balance: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable load-balance.")    
    input_device: list[InputDevice] = Field(default=None, description="Source interface name.")    
    input_device_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable negation of input device match.")    
    input_zone: list[InputZone] = Field(default=None, description="Source input-zone name.")    
    mode: ModeEnum | None = Field(default="manual", description="Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN.")    
    zone_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable zone mode.")    
    minimum_sla_meet_members: int | None = Field(ge=0, le=255, default=0, description="Minimum number of members which meet SLA.")    
    hash_mode: HashModeEnum | None = Field(default="round-robin", description="Hash algorithm for selected priority members for load balance mode.")    
    shortcut_priority: Literal["enable", "disable", "auto"] | None = Field(default="auto", description="High priority of ADVPN shortcut for this service.")    
    role: Literal["standalone", "primary", "secondary"] | None = Field(default="standalone", description="Service role to work with neighbor.")    
    standalone_action: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable service when selected neighbor role is standalone while service role is not standalone.")    
    quality_link: int | None = Field(ge=0, le=255, default=0, description="Quality grade.")    
    tos: str | None = Field(default="", description="Type of service bit pattern.")    
    tos_mask: str | None = Field(default="", description="Type of service evaluated bits.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Protocol number.")    
    start_port: int | None = Field(ge=0, le=65535, default=1, description="Start destination port number.")    
    end_port: int | None = Field(ge=0, le=65535, default=65535, description="End destination port number.")    
    start_src_port: int | None = Field(ge=0, le=65535, default=1, description="Start source port number.")    
    end_src_port: int | None = Field(ge=0, le=65535, default=65535, description="End source port number.")    
    dst: list[Dst] = Field(default=None, description="Destination address name.")    
    dst_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable negation of destination address match.")    
    src: list[Src] = Field(default=None, description="Source address name.")    
    dst6: list[Dst6] = Field(default=None, description="Destination address6 name.")    
    src6: list[Src6] = Field(default=None, description="Source address6 name.")    
    src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable negation of source address match.")    
    users: list[Users] = Field(default=None, description="User name.")    
    groups: list[Groups] = Field(default=None, description="User groups.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet service for application-based load balancing.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet service name list.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group list.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet service name list.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet service name list.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group list.")    
    internet_service_app_ctrl: list[InternetServiceAppCtrl] = Field(default=None, description="Application control based Internet Service ID list.")    
    internet_service_app_ctrl_group: list[InternetServiceAppCtrlGroup] = Field(default=None, description="Application control based Internet Service group list.")    
    internet_service_app_ctrl_category: list[InternetServiceAppCtrlCategory] = Field(default=None, description="IDs of one or more application control categories.")    
    health_check: list[HealthCheck] = Field(default=None, description="Health check list.")    
    link_cost_factor: LinkCostFactorEnum | None = Field(default="latency", description="Link cost factor.")    
    packet_loss_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of packet-loss in the formula of custom-profile-1.")    
    latency_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of latency in the formula of custom-profile-1.")    
    jitter_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of jitter in the formula of custom-profile-1.")    
    bandwidth_weight: int | None = Field(ge=0, le=10000000, default=0, description="Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.")    
    link_cost_threshold: int | None = Field(ge=0, le=10000000, default=10, description="Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).")    
    hold_down_time: int | None = Field(ge=0, le=10000000, default=0, description="Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).")    
    sla_stickiness: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SLA stickiness (default = disable).")    
    dscp_forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable forward traffic DSCP tag.")    
    dscp_reverse: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable reverse traffic DSCP tag.")    
    dscp_forward_tag: str | None = Field(default="", description="Forward traffic DSCP tag.")    
    dscp_reverse_tag: str | None = Field(default="", description="Reverse traffic DSCP tag.")    
    sla: list[Sla] = Field(default=None, description="Service level agreement (SLA).")    
    priority_members: list[PriorityMembers] = Field(default=None, description="Member sequence number list.")    
    priority_zone: list[PriorityZone] = Field(default=None, description="Priority zone name list.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SD-WAN service.")    
    gateway: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SD-WAN service gateway.")    
    default: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of SD-WAN as default service.")    
    sla_compare_method: Literal["order", "number"] | None = Field(default="order", description="Method to compare SLA value for SLA mode.")    
    fib_best_match_force: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable force using fib-best-match oif as outgoing interface.")    
    tie_break: TieBreakEnum | None = Field(default="zone", description="Method of selecting member if more than one meets the SLA.")    
    use_shortcut_sla: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of ADVPN shortcut for quality comparison.")    
    passive_measurement: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable passive measurement based on the service criteria.")    
    agent_exclusive: Literal["enable", "disable"] | None = Field(default="disable", description="Set/unset the service as agent use exclusively.")    
    shortcut: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable shortcut for this service.")    
    comment: str | None = Field(max_length=255, default=None, description="Comments.")
class SdwanNeighbor(BaseModel):
    """
    Child table model for neighbor.
    
    Create SD-WAN neighbor from BGP neighbor table to control route advertisements according to SLA status.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip: str = Field(max_length=45, default="", description="IP/IPv6 address of neighbor or neighbor-group name.")  # datasource: ['router.bgp.neighbor-group.name', 'router.bgp.neighbor.ip']    
    member: list[Member] = Field(default=None, description="Member sequence number list.")    
    service_id: int | None = Field(ge=0, le=4294967295, default=0, description="SD-WAN service ID to work with the neighbor.")  # datasource: ['system.sdwan.service.id']    
    minimum_sla_meet_members: int | None = Field(ge=1, le=255, default=1, description="Minimum number of members which meet SLA when the neighbor is preferred.")    
    mode: Literal["sla", "speedtest"] | None = Field(default="sla", description="What metric to select the neighbor.")    
    role: Literal["standalone", "primary", "secondary"] | None = Field(default="standalone", description="Role of neighbor.")    
    route_metric: Literal["preferable", "priority"] | None = Field(default="preferable", description="Route-metric of neighbor.")    
    health_check: str | None = Field(max_length=35, default="", description="SD-WAN health-check name.")  # datasource: ['system.sdwan.health-check.name']    
    sla_id: int | None = Field(ge=0, le=4294967295, default=0, description="SLA ID.")
class SdwanDuplication(BaseModel):
    """
    Child table model for duplication.
    
    Create SD-WAN duplication rule.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=255, default=0, description="Duplication rule ID (1 - 255).")    
    service_id: list[ServiceId] = Field(default=None, description="SD-WAN service rule ID list.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source address or address group names.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination address or address group names.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Source address6 or address6 group names.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="Destination address6 or address6 group names.")    
    srcintf: list[Srcintf] = Field(default=None, description="Incoming (ingress) interfaces or zones.")    
    dstintf: list[Dstintf] = Field(default=None, description="Outgoing (egress) interfaces or zones.")    
    service: list[Service] = Field(default=None, description="Service and service group name.")    
    packet_duplication: Literal["disable", "force", "on-demand"] | None = Field(default="disable", description="Configure packet duplication method.")    
    sla_match_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable packet duplication matching health-check SLAs in service rule.")    
    packet_de_duplication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable discarding of packets that have been duplicated.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SdwanLoad_balance_modeEnum(str, Enum):
    """Allowed values for load_balance_mode field."""
    SOURCE_IP_BASED = "source-ip-based"    WEIGHT_BASED = "weight-based"    USAGE_BASED = "usage-based"    SOURCE_DEST_IP_BASED = "source-dest-ip-based"    MEASURED_VOLUME_BASED = "measured-volume-based"

# ============================================================================
# Main Model
# ============================================================================

class SdwanModel(BaseModel):
    """
    Pydantic model for system/sdwan configuration.
    
    Configure redundant Internet connections with multiple outbound links and health-check profiles.
    
    Validation Rules:        - status: pattern=        - load_balance_mode: pattern=        - speedtest_bypass_routing: pattern=        - duplication_max_num: min=2 max=4 pattern=        - duplication_max_discrepancy: min=250 max=1000 pattern=        - neighbor_hold_down: pattern=        - neighbor_hold_down_time: min=0 max=10000000 pattern=        - app_perf_log_period: min=0 max=3600 pattern=        - neighbor_hold_boot_time: min=0 max=10000000 pattern=        - fail_detect: pattern=        - fail_alert_interfaces: pattern=        - zone: pattern=        - members: pattern=        - health_check: pattern=        - service: pattern=        - neighbor: pattern=        - duplication: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable SD-WAN.")    
    load_balance_mode: LoadBalanceModeEnum | None = Field(default="source-ip-based", description="Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.")    
    speedtest_bypass_routing: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bypass routing when speedtest on a SD-WAN member.")    
    duplication_max_num: int | None = Field(ge=2, le=4, default=2, description="Maximum number of interface members a packet is duplicated in the SD-WAN zone (2 - 4, default = 2; if set to 3, the original packet plus 2 more copies are created).")    
    duplication_max_discrepancy: int | None = Field(ge=250, le=1000, default=250, description="Maximum discrepancy between two packets for deduplication in milliseconds (250 - 1000, default = 250).")    
    neighbor_hold_down: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable hold switching from the secondary neighbor to the primary neighbor.")    
    neighbor_hold_down_time: int | None = Field(ge=0, le=10000000, default=0, description="Waiting period in seconds when switching from the secondary neighbor to the primary neighbor when hold-down is disabled. (0 - 10000000, default = 0).")    
    app_perf_log_period: int | None = Field(ge=0, le=3600, default=0, description="Time interval in seconds that application performance logs are generated (0 - 3600, default = 0).")    
    neighbor_hold_boot_time: int | None = Field(ge=0, le=10000000, default=0, description="Waiting period in seconds when switching from the primary neighbor to the secondary neighbor from the neighbor start. (0 - 10000000, default = 0).")    
    fail_detect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SD-WAN Internet connection status checking (failure detection).")    
    fail_alert_interfaces: list[FailAlertInterfaces] = Field(default=None, description="Physical interfaces that will be alerted.")    
    zone: list[Zone] = Field(default=None, description="Configure SD-WAN zones.")    
    members: list[Members] = Field(default=None, description="FortiGate interfaces added to the SD-WAN.")    
    health_check: list[HealthCheck] = Field(default=None, description="SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.")    
    service: list[Service] = Field(default=None, description="Create SD-WAN rules (also called services) to control how sessions are distributed to interfaces in the SD-WAN.")    
    neighbor: list[Neighbor] = Field(default=None, description="Create SD-WAN neighbor from BGP neighbor table to control route advertisements according to SLA status.")    
    duplication: list[Duplication] = Field(default=None, description="Create SD-WAN duplication rule.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    # ========================================================================
    # Helper Methods
    # ========================================================================
    
    def to_fortios_dict(self) -> dict[str, Any]:
        """
        Convert model to FortiOS API payload format.
        
        Returns:
            Dict suitable for POST/PUT operations
        """
        # Export with exclude_none to avoid sending null values
        return self.model_dump(exclude_none=True, by_alias=True)
    
    @classmethod
    def from_fortios_response(cls, data: dict[str, Any]) -> "":
        """
        Create model instance from FortiOS API response.
        
        Args:
            data: Response data from API
            
        Returns:
            Validated model instance
        """
        return cls(**data)
    # ========================================================================
    # Datasource Validation Methods
    # ========================================================================    
    async def validate_fail_alert_interfaces_references(self, client: Any) -> list[str]:
        """
        Validate fail_alert_interfaces references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SdwanModel(
            ...     fail_alert_interfaces=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fail_alert_interfaces_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdwan.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "fail_alert_interfaces", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Fail-Alert-Interfaces '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_zone_references(self, client: Any) -> list[str]:
        """
        Validate zone references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdwan/health-check        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SdwanModel(
            ...     zone=[{"advpn-health-check": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_zone_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdwan.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "zone", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("advpn-health-check")
            else:
                value = getattr(item, "advpn-health-check", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.sdwan.health-check.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Zone '{value}' not found in "
                    "system/sdwan/health-check"
                )        
        return errors    
    async def validate_members_references(self, client: Any) -> list[str]:
        """
        Validate members references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdwan/zone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SdwanModel(
            ...     members=[{"zone": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_members_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdwan.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "members", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("zone")
            else:
                value = getattr(item, "zone", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.sdwan.zone.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Members '{value}' not found in "
                    "system/sdwan/zone"
                )        
        return errors    
    async def validate_health_check_references(self, client: Any) -> list[str]:
        """
        Validate health_check references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/traffic-class        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SdwanModel(
            ...     health_check=[{"class-id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_health_check_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdwan.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "health_check", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("class-id")
            else:
                value = getattr(item, "class-id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.traffic-class.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Health-Check '{value}' not found in "
                    "firewall/traffic-class"
                )        
        return errors    
    async def validate_neighbor_references(self, client: Any) -> list[str]:
        """
        Validate neighbor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdwan/health-check        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SdwanModel(
            ...     neighbor=[{"health-check": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_neighbor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdwan.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "neighbor", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("health-check")
            else:
                value = getattr(item, "health-check", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.sdwan.health-check.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Neighbor '{value}' not found in "
                    "system/sdwan/health-check"
                )        
        return errors    
    async def validate_all_references(self, client: Any) -> list[str]:
        """
        Validate ALL datasource references in this model.
        
        Convenience method that runs all validate_*_references() methods
        and aggregates the results.
        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of all validation errors found
            
        Example:
            >>> errors = await policy.validate_all_references(fgt._client)
            >>> if errors:
            ...     for error in errors:
            ...         print(f"  - {error}")
        """
        all_errors = []
        
        errors = await self.validate_fail_alert_interfaces_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_zone_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_members_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_health_check_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_neighbor_references(client)
        all_errors.extend(errors)        
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "SdwanModel",    "SdwanFailAlertInterfaces",    "SdwanZone",    "SdwanMembers",    "SdwanHealthCheck",    "SdwanService",    "SdwanNeighbor",    "SdwanDuplication",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.655354Z
# ============================================================================
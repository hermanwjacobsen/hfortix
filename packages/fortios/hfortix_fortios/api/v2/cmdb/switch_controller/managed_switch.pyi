from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ManagedSwitchPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/managed_switch payload fields.
    
    Configure FortiSwitch devices that are managed by this FortiGate.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.switch-controller.ptp.profile.ProfileEndpoint` (via: ptp-profile)
        - :class:`~.switch-controller.security-policy.local-access.LocalAccessEndpoint` (via: access-profile)
        - :class:`~.switch-controller.switch-profile.SwitchProfileEndpoint` (via: switch-profile)
        - :class:`~.system.interface.InterfaceEndpoint` (via: fsw-wan1-peer)

    **Usage:**
        payload: ManagedSwitchPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    switch_id: str  # Managed-switch name. | MaxLen: 35
    sn: str  # Managed-switch serial number. | MaxLen: 16
    description: str  # Description. | MaxLen: 63
    switch_profile: str  # FortiSwitch profile. | Default: default | MaxLen: 35
    access_profile: str  # FortiSwitch access profile. | Default: default | MaxLen: 31
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # Purdue Level of this FortiSwitch. | Default: 3
    fsw_wan1_peer: str  # FortiSwitch WAN1 peer port. | MaxLen: 35
    fsw_wan1_admin: Literal["discovered", "disable", "enable"]  # FortiSwitch WAN1 admin status; enable to authorize | Default: discovered
    poe_pre_standard_detection: Literal["enable", "disable"]  # Enable/disable PoE pre-standard detection. | Default: disable
    dhcp_server_access_list: Literal["global", "enable", "disable"]  # DHCP snooping server access list. | Default: global
    poe_detection_type: int  # PoE detection type for FortiSwitch. | Default: 0 | Min: 0 | Max: 255
    max_poe_budget: int  # Max PoE budget for FortiSwitch. | Default: 0 | Min: 0 | Max: 65535
    directly_connected: int  # Directly connected FortiSwitch. | Default: 0 | Min: 0 | Max: 1
    version: int  # FortiSwitch version. | Default: 0 | Min: 0 | Max: 255
    max_allowed_trunk_members: int  # FortiSwitch maximum allowed trunk members. | Default: 0 | Min: 0 | Max: 255
    pre_provisioned: int  # Pre-provisioned managed switch. | Default: 0 | Min: 0 | Max: 255
    l3_discovered: int  # Layer 3 management discovered. | Default: 0 | Min: 0 | Max: 1
    mgmt_mode: int  # FortiLink management mode. | Default: 0 | Min: 0 | Max: 255
    tunnel_discovered: int  # SOCKS tunnel management discovered. | Default: 0 | Min: 0 | Max: 1
    tdr_supported: str  # TDR supported. | MaxLen: 31
    dynamic_capability: str  # List of features this FortiSwitch supports | Default: 0x00000000000000000000000000000000
    switch_device_tag: str  # User definable label/tag. | MaxLen: 32
    switch_dhcp_opt43_key: str  # DHCP option43 key. | MaxLen: 63
    mclag_igmp_snooping_aware: Literal["enable", "disable"]  # Enable/disable MCLAG IGMP-snooping awareness. | Default: enable
    dynamically_discovered: int  # Dynamically discovered FortiSwitch. | Default: 0 | Min: 0 | Max: 1
    ptp_status: Literal["disable", "enable"]  # Enable/disable PTP profile on this FortiSwitch. | Default: disable
    ptp_profile: str  # PTP profile configuration. | Default: default | MaxLen: 63
    radius_nas_ip_override: Literal["disable", "enable"]  # Use locally defined NAS-IP. | Default: disable
    radius_nas_ip: str  # NAS-IP address. | Default: 0.0.0.0
    route_offload: Literal["disable", "enable"]  # Enable/disable route offload on this FortiSwitch. | Default: disable
    route_offload_mclag: Literal["disable", "enable"]  # Enable/disable route offload MCLAG on this FortiSw | Default: disable
    route_offload_router: list[dict[str, Any]]  # Configure route offload MCLAG IP address.
    vlan: list[dict[str, Any]]  # Configure VLAN assignment priority.
    type: Literal["virtual", "physical"]  # Indication of switch type, physical or virtual. | Default: physical
    owner_vdom: str  # VDOM which owner of port belongs to. | MaxLen: 31
    flow_identity: str  # Flow-tracking netflow ipfix switch identity in hex | Default: 00000000
    staged_image_version: str  # Staged image version for FortiSwitch. | MaxLen: 127
    delayed_restart_trigger: int  # Delayed restart triggered for this FortiSwitch. | Default: 0 | Min: 0 | Max: 255
    firmware_provision: Literal["enable", "disable"]  # Enable/disable provisioning of firmware to FortiSw | Default: disable
    firmware_provision_version: str  # Firmware version to provision to this FortiSwitch | MaxLen: 35
    firmware_provision_latest: Literal["disable", "once"]  # Enable/disable one-time automatic provisioning of | Default: disable
    ports: list[dict[str, Any]]  # Managed-switch port list.
    ip_source_guard: list[dict[str, Any]]  # IP source guard.
    stp_settings: str  # Configuration method to edit Spanning Tree Protoco
    stp_instance: list[dict[str, Any]]  # Configuration method to edit Spanning Tree Protoco
    override_snmp_sysinfo: Literal["disable", "enable"]  # Enable/disable overriding the global SNMP system i | Default: disable
    snmp_sysinfo: str  # Configuration method to edit Simple Network Manage
    override_snmp_trap_threshold: Literal["enable", "disable"]  # Enable/disable overriding the global SNMP trap thr | Default: disable
    snmp_trap_threshold: str  # Configuration method to edit Simple Network Manage
    override_snmp_community: Literal["enable", "disable"]  # Enable/disable overriding the global SNMP communit | Default: disable
    snmp_community: list[dict[str, Any]]  # Configuration method to edit Simple Network Manage
    override_snmp_user: Literal["enable", "disable"]  # Enable/disable overriding the global SNMP users. | Default: disable
    snmp_user: list[dict[str, Any]]  # Configuration method to edit Simple Network Manage
    qos_drop_policy: Literal["taildrop", "random-early-detection"]  # Set QoS drop-policy. | Default: taildrop
    qos_red_probability: int  # Set QoS RED/WRED drop probability. | Default: 12 | Min: 0 | Max: 100
    switch_log: str  # Configuration method to edit FortiSwitch logging s
    remote_log: list[dict[str, Any]]  # Configure logging by FortiSwitch device to a remot
    storm_control: str  # Configuration method to edit FortiSwitch storm con
    mirror: list[dict[str, Any]]  # Configuration method to edit FortiSwitch packet mi
    static_mac: list[dict[str, Any]]  # Configuration method to edit FortiSwitch Static an
    custom_command: list[dict[str, Any]]  # Configuration method to edit FortiSwitch commands
    dhcp_snooping_static_client: list[dict[str, Any]]  # Configure FortiSwitch DHCP snooping static clients
    igmp_snooping: str  # Configure FortiSwitch IGMP snooping global setting
    x802_1X_settings: str  # Configuration method to edit FortiSwitch 802.1X gl
    router_vrf: list[dict[str, Any]]  # Configure VRF.
    system_interface: list[dict[str, Any]]  # Configure system interface on FortiSwitch.
    router_static: list[dict[str, Any]]  # Configure static routes.
    system_dhcp_server: list[dict[str, Any]]  # Configure DHCP servers.

# Nested TypedDicts for table field children (dict mode)

class ManagedSwitchRouteoffloadrouterItem(TypedDict):
    """Type hints for route-offload-router table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vlan_name: str  # VLAN name. | MaxLen: 15
    router_ip: str  # Router IP address. | Default: 0.0.0.0


class ManagedSwitchVlanItem(TypedDict):
    """Type hints for vlan table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vlan_name: str  # VLAN name. | MaxLen: 15
    assignment_priority: int  # 802.1x Radius (Tunnel-Private-Group-Id) VLANID ass | Default: 128 | Min: 1 | Max: 255


class ManagedSwitchPortsItem(TypedDict):
    """Type hints for ports table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    port_name: str  # Switch port name. | MaxLen: 15
    port_owner: str  # Switch port name. | MaxLen: 15
    switch_id: str  # Switch id. | MaxLen: 35
    speed: Literal["10half", "10full", "100half", "100full", "1000full", "10000full", "auto", "1000auto", "1000full-fiber", "40000full", "auto-module", "100FX-half", "100FX-full", "100000full", "2500auto", "2500full", "25000full", "50000full", "10000cr", "10000sr", "100000sr4", "100000cr4", "40000sr4", "40000cr4", "40000auto", "25000cr", "25000sr", "50000cr", "50000sr", "5000auto", "sgmii-auto"]  # Switch port speed; default and available settings | Default: auto
    status: Literal["up", "down"]  # Switch port admin status: up or down. | Default: up
    poe_status: Literal["enable", "disable"]  # Enable/disable PoE status. | Default: enable
    ip_source_guard: Literal["disable", "enable"]  # Enable/disable IP source guard. | Default: disable
    ptp_status: Literal["disable", "enable"]  # Enable/disable PTP policy on this FortiSwitch port | Default: enable
    ptp_policy: str  # PTP policy configuration. | Default: default | MaxLen: 63
    aggregator_mode: Literal["bandwidth", "count"]  # LACP member select mode. | Default: bandwidth
    flapguard: Literal["enable", "disable"]  # Enable/disable flap guard. | Default: disable
    flap_rate: int  # Number of stage change events needed within flap-d | Default: 5 | Min: 1 | Max: 30
    flap_duration: int  # Period over which flap events are calculated | Default: 30 | Min: 5 | Max: 300
    flap_timeout: int  # Flap guard disabling protection (min). | Default: 0 | Min: 0 | Max: 120
    rpvst_port: Literal["disabled", "enabled"]  # Enable/disable inter-operability with rapid PVST o | Default: disabled
    poe_pre_standard_detection: Literal["enable", "disable"]  # Enable/disable PoE pre-standard detection. | Default: disable
    port_number: int  # Port number. | Default: 0 | Min: 1 | Max: 64
    port_prefix_type: int  # Port prefix type. | Default: 0 | Min: 0 | Max: 1
    fortilink_port: int  # FortiLink uplink port. | Default: 0 | Min: 0 | Max: 1
    poe_capable: int  # PoE capable. | Default: 0 | Min: 0 | Max: 1
    pd_capable: int  # Powered device capable. | Default: 0 | Min: 0 | Max: 1
    stacking_port: int  # Stacking port. | Default: 0 | Min: 0 | Max: 1
    p2p_port: int  # General peer to peer tunnel port. | Default: 0 | Min: 0 | Max: 1
    mclag_icl_port: int  # MCLAG-ICL port. | Default: 0 | Min: 0 | Max: 1
    authenticated_port: int  # Peer to Peer Authenticated port. | Default: 0 | Min: 0 | Max: 1
    restricted_auth_port: int  # Peer to Peer Restricted Authenticated port. | Default: 0 | Min: 0 | Max: 1
    encrypted_port: int  # Peer to Peer Encrypted port. | Default: 0 | Min: 0 | Max: 1
    fiber_port: int  # Fiber-port. | Default: 0 | Min: 0 | Max: 1
    media_type: str  # Media type. | MaxLen: 31
    poe_standard: str  # PoE standard supported. | MaxLen: 63
    poe_max_power: str  # PoE maximum power. | MaxLen: 35
    poe_mode_bt_cabable: int  # PoE mode IEEE 802.3BT capable. | Default: 0 | Min: 0 | Max: 1
    poe_port_mode: Literal["ieee802-3af", "ieee802-3at", "ieee802-3bt"]  # Configure PoE port mode. | Default: ieee802-3at
    poe_port_priority: Literal["critical-priority", "high-priority", "low-priority", "medium-priority"]  # Configure PoE port priority. | Default: low-priority
    poe_port_power: Literal["normal", "perpetual", "perpetual-fast"]  # Configure PoE port power. | Default: normal
    flags: int  # Port properties flags. | Default: 0 | Min: 0 | Max: 4294967295
    isl_local_trunk_name: str  # ISL local trunk name. | MaxLen: 15
    isl_peer_port_name: str  # ISL peer port name. | MaxLen: 15
    isl_peer_device_name: str  # ISL peer device name. | MaxLen: 35
    isl_peer_device_sn: str  # ISL peer device serial number. | MaxLen: 16
    fgt_peer_port_name: str  # FGT peer port name. | MaxLen: 15
    fgt_peer_device_name: str  # FGT peer device name. | MaxLen: 35
    vlan: str  # Assign switch ports to a VLAN. | MaxLen: 15
    allowed_vlans_all: Literal["enable", "disable"]  # Enable/disable all defined vlans on this port. | Default: disable
    allowed_vlans: str  # Configure switch port tagged VLANs.
    untagged_vlans: str  # Configure switch port untagged VLANs.
    type: Literal["physical", "trunk"]  # Interface type: physical or trunk port. | Default: physical
    access_mode: Literal["dynamic", "nac", "static"]  # Access mode of the port. | Default: static
    matched_dpp_policy: str  # Matched child policy in the dynamic port policy. | MaxLen: 63
    matched_dpp_intf_tags: str  # Matched interface tags in the dynamic port policy. | MaxLen: 63
    acl_group: str  # ACL groups on this port.
    fortiswitch_acls: str  # ACLs on this port.
    dhcp_snooping: Literal["untrusted", "trusted"]  # Trusted or untrusted DHCP-snooping interface. | Default: untrusted
    dhcp_snoop_option82_trust: Literal["enable", "disable"]  # Enable/disable allowance of DHCP with option-82 on | Default: disable
    dhcp_snoop_option82_override: str  # Configure DHCP snooping option 82 override.
    arp_inspection_trust: Literal["untrusted", "trusted"]  # Trusted or untrusted dynamic ARP inspection. | Default: untrusted
    igmp_snooping_flood_reports: Literal["enable", "disable"]  # Enable/disable flooding of IGMP reports to this in | Default: disable
    mcast_snooping_flood_traffic: Literal["enable", "disable"]  # Enable/disable flooding of IGMP snooping traffic t | Default: disable
    stp_state: Literal["enabled", "disabled"]  # Enable/disable Spanning Tree Protocol (STP) on thi | Default: enabled
    stp_root_guard: Literal["enabled", "disabled"]  # Enable/disable STP root guard on this interface. | Default: disabled
    stp_bpdu_guard: Literal["enabled", "disabled"]  # Enable/disable STP BPDU guard on this interface. | Default: disabled
    stp_bpdu_guard_timeout: int  # BPDU Guard disabling protection (0 - 120 min). | Default: 5 | Min: 0 | Max: 120
    edge_port: Literal["enable", "disable"]  # Enable/disable this interface as an edge port, bri | Default: enable
    discard_mode: Literal["none", "all-untagged", "all-tagged"]  # Configure discard mode for port. | Default: none
    packet_sampler: Literal["enabled", "disabled"]  # Enable/disable packet sampling on this interface. | Default: disabled
    packet_sample_rate: int  # Packet sampling rate (0 - 99999 p/sec). | Default: 512 | Min: 0 | Max: 99999
    sflow_counter_interval: int  # sFlow sampling counter polling interval in seconds | Default: 0 | Min: 0 | Max: 255
    sample_direction: Literal["tx", "rx", "both"]  # Packet sampling direction. | Default: both
    fec_capable: int  # FEC capable. | Default: 0 | Min: 0 | Max: 1
    fec_state: Literal["disabled", "cl74", "cl91", "detect-by-module"]  # State of forward error correction. | Default: detect-by-module
    flow_control: Literal["disable", "tx", "rx", "both"]  # Flow control direction. | Default: disable
    pause_meter: int  # Configure ingress pause metering rate, in kbps | Default: 0 | Min: 128 | Max: 2147483647
    pause_meter_resume: Literal["75%", "50%", "25%"]  # Resume threshold for resuming traffic on ingress p | Default: 50%
    loop_guard: Literal["enabled", "disabled"]  # Enable/disable loop-guard on this interface, an ST | Default: disabled
    loop_guard_timeout: int  # Loop-guard timeout (0 - 120 min, default = 45). | Default: 45 | Min: 0 | Max: 120
    port_policy: str  # Switch controller dynamic port policy from availab | MaxLen: 63
    qos_policy: str  # Switch controller QoS policy from available option | Default: default | MaxLen: 63
    storm_control_policy: str  # Switch controller storm control policy from availa | Default: default | MaxLen: 63
    port_security_policy: str  # Switch controller authentication policy to apply t | MaxLen: 31
    export_to_pool: str  # Switch controller export port to pool-list. | MaxLen: 35
    interface_tags: str  # Tag(s) associated with the interface for various f
    learning_limit: int  # Limit the number of dynamic MAC addresses on this | Default: 0 | Min: 0 | Max: 128
    sticky_mac: Literal["enable", "disable"]  # Enable or disable sticky-mac on the interface. | Default: disable
    lldp_status: Literal["disable", "rx-only", "tx-only", "tx-rx"]  # LLDP transmit and receive status. | Default: tx-rx
    lldp_profile: str  # LLDP port TLV profile. | Default: default-auto-isl | MaxLen: 63
    export_to: str  # Export managed-switch port to a tenant VDOM. | MaxLen: 31
    mac_addr: str  # Port/Trunk MAC. | Default: 00:00:00:00:00:00
    allow_arp_monitor: Literal["disable", "enable"]  # Enable/Disable allow ARP monitor. | Default: disable
    qnq: str  # 802.1AD VLANs in the VDom. | MaxLen: 15
    log_mac_event: Literal["disable", "enable"]  # Enable/disable logging for dynamic MAC address eve | Default: disable
    port_selection_criteria: Literal["src-mac", "dst-mac", "src-dst-mac", "src-ip", "dst-ip", "src-dst-ip"]  # Algorithm for aggregate port selection. | Default: src-dst-ip
    description: str  # Description for port. | MaxLen: 63
    lacp_speed: Literal["slow", "fast"]  # End Link Aggregation Control Protocol (LACP) messa | Default: slow
    mode: Literal["static", "lacp-passive", "lacp-active"]  # LACP mode: ignore and do not send control messages | Default: static
    bundle: Literal["enable", "disable"]  # Enable/disable Link Aggregation Group (LAG) bundli | Default: disable
    member_withdrawal_behavior: Literal["forward", "block"]  # Port behavior after it withdraws because of loss o | Default: block
    mclag: Literal["enable", "disable"]  # Enable/disable multi-chassis link aggregation | Default: disable
    min_bundle: int  # Minimum size of LAG bundle (1 - 24, default = 1). | Default: 1 | Min: 1 | Max: 24
    max_bundle: int  # Maximum size of LAG bundle (1 - 24, default = 24). | Default: 24 | Min: 1 | Max: 24
    members: str  # Aggregated LAG bundle interfaces.
    fallback_port: str  # LACP fallback port. | MaxLen: 79


class ManagedSwitchIpsourceguardItem(TypedDict):
    """Type hints for ip-source-guard table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    port: str  # Ingress interface to which source guard is bound. | MaxLen: 15
    description: str  # Description. | MaxLen: 63
    binding_entry: str  # IP and MAC address configuration.


class ManagedSwitchStpinstanceItem(TypedDict):
    """Type hints for stp-instance table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: str  # Instance ID. | MaxLen: 2
    priority: Literal["0", "4096", "8192", "12288", "16384", "20480", "24576", "28672", "32768", "36864", "40960", "45056", "49152", "53248", "57344", "61440"]  # Priority. | Default: 32768


class ManagedSwitchSnmpcommunityItem(TypedDict):
    """Type hints for snmp-community table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # SNMP community ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # SNMP community name. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable this SNMP community. | Default: enable
    hosts: str  # Configure IPv4 SNMP managers (hosts).
    query_v1_status: Literal["disable", "enable"]  # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_port: int  # SNMP v1 query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v2c_status: Literal["disable", "enable"]  # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_port: int  # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    trap_v1_status: Literal["disable", "enable"]  # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v1_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_status: Literal["disable", "enable"]  # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_lport: int  # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_rport: int  # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]  # SNMP notifications (traps) to send. | Default: cpu-high mem-low log-full intf-ip ent-conf-change l2mac


class ManagedSwitchSnmpuserItem(TypedDict):
    """Type hints for snmp-user table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # SNMP user name. | MaxLen: 32
    queries: Literal["disable", "enable"]  # Enable/disable SNMP queries for this user. | Default: enable
    query_port: int  # SNMPv3 query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]  # Security level for message authentication and encr | Default: no-auth-no-priv
    auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]  # Authentication protocol. | Default: sha256
    auth_pwd: str  # Password for authentication protocol. | MaxLen: 128
    priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"]  # Privacy (encryption) protocol. | Default: aes128
    priv_pwd: str  # Password for privacy (encryption) protocol. | MaxLen: 128


class ManagedSwitchRemotelogItem(TypedDict):
    """Type hints for remote-log table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Remote log name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Enable/disable logging by FortiSwitch device to a | Default: disable
    server: str  # IPv4 address of the remote syslog server. | MaxLen: 63
    port: int  # Remote syslog server listening port. | Default: 514 | Min: 0 | Max: 65535
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]  # Severity of logs to be transferred to remote log s | Default: information
    csv: Literal["enable", "disable"]  # Enable/disable comma-separated value (CSV) strings | Default: disable
    facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]  # Facility to log to remote syslog server. | Default: local7


class ManagedSwitchMirrorItem(TypedDict):
    """Type hints for mirror table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Mirror name. | MaxLen: 63
    status: Literal["active", "inactive"]  # Active/inactive mirror configuration. | Default: inactive
    switching_packet: Literal["enable", "disable"]  # Enable/disable switching functionality when mirror | Default: disable
    dst: str  # Destination port. | MaxLen: 63
    src_ingress: str  # Source ingress interfaces.
    src_egress: str  # Source egress interfaces.


class ManagedSwitchStaticmacItem(TypedDict):
    """Type hints for static-mac table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    type: Literal["static", "sticky"]  # Type. | Default: static
    vlan: str  # Vlan. | MaxLen: 15
    mac: str  # MAC address. | Default: 00:00:00:00:00:00
    interface: str  # Interface name. | MaxLen: 35
    description: str  # Description. | MaxLen: 63


class ManagedSwitchCustomcommandItem(TypedDict):
    """Type hints for custom-command table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    command_entry: str  # List of FortiSwitch commands. | MaxLen: 35
    command_name: str  # Names of commands to be pushed to this FortiSwitch | MaxLen: 35


class ManagedSwitchDhcpsnoopingstaticclientItem(TypedDict):
    """Type hints for dhcp-snooping-static-client table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Client name. | MaxLen: 35
    vlan: str  # VLAN name. | MaxLen: 15
    ip: str  # Client static IP address. | Default: 0.0.0.0
    mac: str  # Client MAC address. | Default: 00:00:00:00:00:00
    port: str  # Interface name. | MaxLen: 15


class ManagedSwitchRoutervrfItem(TypedDict):
    """Type hints for router-vrf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # VRF entry name. | MaxLen: 35
    switch_id: str  # Switch ID. | MaxLen: 35
    vrfid: int  # VRF ID. | Default: 0 | Min: 0 | Max: 1023


class ManagedSwitchSysteminterfaceItem(TypedDict):
    """Type hints for system-interface table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Interface name. | MaxLen: 15
    switch_id: str  # Switch ID. | MaxLen: 35
    mode: Literal["static", "dhcp"]  # Interface addressing mode. | Default: static
    ip: str  # IP and mask for this interface. | Default: 0.0.0.0 0.0.0.0
    status: Literal["disable", "enable"]  # Enable/disable interface status. | Default: enable
    allowaccess: Literal["ping", "https", "http", "ssh", "snmp", "telnet", "radius-acct"]  # Permitted types of management access to this inter
    vlan: str  # VLAN name. | MaxLen: 15
    type: Literal["vlan", "physical"]  # Interface type. | Default: vlan
    interface: str  # Interface name. | MaxLen: 63
    vrf: str  # VRF for this route. | MaxLen: 63


class ManagedSwitchRouterstaticItem(TypedDict):
    """Type hints for router-static table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry sequence number. | Default: 0 | Min: 0 | Max: 4294967295
    switch_id: str  # Switch ID. | MaxLen: 35
    blackhole: Literal["disable", "enable"]  # Enable/disable blackhole on this route. | Default: disable
    comment: str  # Comment. | MaxLen: 63
    device: str  # Gateway out interface. | MaxLen: 35
    distance: int  # Administrative distance for the route | Default: 10 | Min: 1 | Max: 255
    dst: str  # Destination ip and mask for this route. | Default: 0.0.0.0 0.0.0.0
    dynamic_gateway: Literal["disable", "enable"]  # Enable/disable dynamic gateway. | Default: disable
    gateway: str  # Gateway ip for this route. | Default: 0.0.0.0
    status: Literal["disable", "enable"]  # Enable/disable route status. | Default: enable
    vrf: str  # VRF for this route. | MaxLen: 35


class ManagedSwitchSystemdhcpserverItem(TypedDict):
    """Type hints for system-dhcp-server table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    switch_id: str  # Switch ID. | MaxLen: 35
    status: Literal["disable", "enable"]  # Enable/disable this DHCP configuration. | Default: enable
    lease_time: int  # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 0 | Max: 4294967295
    dns_service: Literal["local", "default", "specify"]  # Options for assigning DNS servers to DHCP clients. | Default: specify
    dns_server1: str  # DNS server 1. | Default: 0.0.0.0
    dns_server2: str  # DNS server 2. | Default: 0.0.0.0
    dns_server3: str  # DNS server 3. | Default: 0.0.0.0
    ntp_service: Literal["local", "default", "specify"]  # Options for assigning Network Time Protocol (NTP) | Default: specify
    ntp_server1: str  # NTP server 1. | Default: 0.0.0.0
    ntp_server2: str  # NTP server 2. | Default: 0.0.0.0
    ntp_server3: str  # NTP server 3. | Default: 0.0.0.0
    default_gateway: str  # Default gateway IP address assigned by the DHCP se | Default: 0.0.0.0
    netmask: str  # Netmask assigned by the DHCP server. | Default: 0.0.0.0
    interface: str  # DHCP server can assign IP configurations to client | MaxLen: 15
    ip_range: str  # DHCP IP range configuration.
    options: str  # DHCP options.


# Nested classes for table field children (object mode)

@final
class ManagedSwitchRouteoffloadrouterObject:
    """Typed object for route-offload-router table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name. | MaxLen: 15
    vlan_name: str
    # Router IP address. | Default: 0.0.0.0
    router_ip: str
    
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
class ManagedSwitchVlanObject:
    """Typed object for vlan table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VLAN name. | MaxLen: 15
    vlan_name: str
    # 802.1x Radius (Tunnel-Private-Group-Id) VLANID assign-by-nam | Default: 128 | Min: 1 | Max: 255
    assignment_priority: int
    
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
class ManagedSwitchPortsObject:
    """Typed object for ports table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Switch port name. | MaxLen: 15
    port_name: str
    # Switch port name. | MaxLen: 15
    port_owner: str
    # Switch id. | MaxLen: 35
    switch_id: str
    # Switch port speed; default and available settings depend on | Default: auto
    speed: Literal["10half", "10full", "100half", "100full", "1000full", "10000full", "auto", "1000auto", "1000full-fiber", "40000full", "auto-module", "100FX-half", "100FX-full", "100000full", "2500auto", "2500full", "25000full", "50000full", "10000cr", "10000sr", "100000sr4", "100000cr4", "40000sr4", "40000cr4", "40000auto", "25000cr", "25000sr", "50000cr", "50000sr", "5000auto", "sgmii-auto"]
    # Switch port admin status: up or down. | Default: up
    status: Literal["up", "down"]
    # Enable/disable PoE status. | Default: enable
    poe_status: Literal["enable", "disable"]
    # Enable/disable IP source guard. | Default: disable
    ip_source_guard: Literal["disable", "enable"]
    # Enable/disable PTP policy on this FortiSwitch port. | Default: enable
    ptp_status: Literal["disable", "enable"]
    # PTP policy configuration. | Default: default | MaxLen: 63
    ptp_policy: str
    # LACP member select mode. | Default: bandwidth
    aggregator_mode: Literal["bandwidth", "count"]
    # Enable/disable flap guard. | Default: disable
    flapguard: Literal["enable", "disable"]
    # Number of stage change events needed within flap-duration. | Default: 5 | Min: 1 | Max: 30
    flap_rate: int
    # Period over which flap events are calculated (seconds). | Default: 30 | Min: 5 | Max: 300
    flap_duration: int
    # Flap guard disabling protection (min). | Default: 0 | Min: 0 | Max: 120
    flap_timeout: int
    # Enable/disable inter-operability with rapid PVST on this int | Default: disabled
    rpvst_port: Literal["disabled", "enabled"]
    # Enable/disable PoE pre-standard detection. | Default: disable
    poe_pre_standard_detection: Literal["enable", "disable"]
    # Port number. | Default: 0 | Min: 1 | Max: 64
    port_number: int
    # Port prefix type. | Default: 0 | Min: 0 | Max: 1
    port_prefix_type: int
    # FortiLink uplink port. | Default: 0 | Min: 0 | Max: 1
    fortilink_port: int
    # PoE capable. | Default: 0 | Min: 0 | Max: 1
    poe_capable: int
    # Powered device capable. | Default: 0 | Min: 0 | Max: 1
    pd_capable: int
    # Stacking port. | Default: 0 | Min: 0 | Max: 1
    stacking_port: int
    # General peer to peer tunnel port. | Default: 0 | Min: 0 | Max: 1
    p2p_port: int
    # MCLAG-ICL port. | Default: 0 | Min: 0 | Max: 1
    mclag_icl_port: int
    # Peer to Peer Authenticated port. | Default: 0 | Min: 0 | Max: 1
    authenticated_port: int
    # Peer to Peer Restricted Authenticated port. | Default: 0 | Min: 0 | Max: 1
    restricted_auth_port: int
    # Peer to Peer Encrypted port. | Default: 0 | Min: 0 | Max: 1
    encrypted_port: int
    # Fiber-port. | Default: 0 | Min: 0 | Max: 1
    fiber_port: int
    # Media type. | MaxLen: 31
    media_type: str
    # PoE standard supported. | MaxLen: 63
    poe_standard: str
    # PoE maximum power. | MaxLen: 35
    poe_max_power: str
    # PoE mode IEEE 802.3BT capable. | Default: 0 | Min: 0 | Max: 1
    poe_mode_bt_cabable: int
    # Configure PoE port mode. | Default: ieee802-3at
    poe_port_mode: Literal["ieee802-3af", "ieee802-3at", "ieee802-3bt"]
    # Configure PoE port priority. | Default: low-priority
    poe_port_priority: Literal["critical-priority", "high-priority", "low-priority", "medium-priority"]
    # Configure PoE port power. | Default: normal
    poe_port_power: Literal["normal", "perpetual", "perpetual-fast"]
    # Port properties flags. | Default: 0 | Min: 0 | Max: 4294967295
    flags: int
    # ISL local trunk name. | MaxLen: 15
    isl_local_trunk_name: str
    # ISL peer port name. | MaxLen: 15
    isl_peer_port_name: str
    # ISL peer device name. | MaxLen: 35
    isl_peer_device_name: str
    # ISL peer device serial number. | MaxLen: 16
    isl_peer_device_sn: str
    # FGT peer port name. | MaxLen: 15
    fgt_peer_port_name: str
    # FGT peer device name. | MaxLen: 35
    fgt_peer_device_name: str
    # Assign switch ports to a VLAN. | MaxLen: 15
    vlan: str
    # Enable/disable all defined vlans on this port. | Default: disable
    allowed_vlans_all: Literal["enable", "disable"]
    # Configure switch port tagged VLANs.
    allowed_vlans: str
    # Configure switch port untagged VLANs.
    untagged_vlans: str
    # Interface type: physical or trunk port. | Default: physical
    type: Literal["physical", "trunk"]
    # Access mode of the port. | Default: static
    access_mode: Literal["dynamic", "nac", "static"]
    # Matched child policy in the dynamic port policy. | MaxLen: 63
    matched_dpp_policy: str
    # Matched interface tags in the dynamic port policy. | MaxLen: 63
    matched_dpp_intf_tags: str
    # ACL groups on this port.
    acl_group: str
    # ACLs on this port.
    fortiswitch_acls: str
    # Trusted or untrusted DHCP-snooping interface. | Default: untrusted
    dhcp_snooping: Literal["untrusted", "trusted"]
    # Enable/disable allowance of DHCP with option-82 on untrusted | Default: disable
    dhcp_snoop_option82_trust: Literal["enable", "disable"]
    # Configure DHCP snooping option 82 override.
    dhcp_snoop_option82_override: str
    # Trusted or untrusted dynamic ARP inspection. | Default: untrusted
    arp_inspection_trust: Literal["untrusted", "trusted"]
    # Enable/disable flooding of IGMP reports to this interface wh | Default: disable
    igmp_snooping_flood_reports: Literal["enable", "disable"]
    # Enable/disable flooding of IGMP snooping traffic to this int | Default: disable
    mcast_snooping_flood_traffic: Literal["enable", "disable"]
    # Enable/disable Spanning Tree Protocol (STP) on this interfac | Default: enabled
    stp_state: Literal["enabled", "disabled"]
    # Enable/disable STP root guard on this interface. | Default: disabled
    stp_root_guard: Literal["enabled", "disabled"]
    # Enable/disable STP BPDU guard on this interface. | Default: disabled
    stp_bpdu_guard: Literal["enabled", "disabled"]
    # BPDU Guard disabling protection (0 - 120 min). | Default: 5 | Min: 0 | Max: 120
    stp_bpdu_guard_timeout: int
    # Enable/disable this interface as an edge port, bridging conn | Default: enable
    edge_port: Literal["enable", "disable"]
    # Configure discard mode for port. | Default: none
    discard_mode: Literal["none", "all-untagged", "all-tagged"]
    # Enable/disable packet sampling on this interface. | Default: disabled
    packet_sampler: Literal["enabled", "disabled"]
    # Packet sampling rate (0 - 99999 p/sec). | Default: 512 | Min: 0 | Max: 99999
    packet_sample_rate: int
    # sFlow sampling counter polling interval in seconds (0 - 255) | Default: 0 | Min: 0 | Max: 255
    sflow_counter_interval: int
    # Packet sampling direction. | Default: both
    sample_direction: Literal["tx", "rx", "both"]
    # FEC capable. | Default: 0 | Min: 0 | Max: 1
    fec_capable: int
    # State of forward error correction. | Default: detect-by-module
    fec_state: Literal["disabled", "cl74", "cl91", "detect-by-module"]
    # Flow control direction. | Default: disable
    flow_control: Literal["disable", "tx", "rx", "both"]
    # Configure ingress pause metering rate, in kbps | Default: 0 | Min: 128 | Max: 2147483647
    pause_meter: int
    # Resume threshold for resuming traffic on ingress port. | Default: 50%
    pause_meter_resume: Literal["75%", "50%", "25%"]
    # Enable/disable loop-guard on this interface, an STP optimiza | Default: disabled
    loop_guard: Literal["enabled", "disabled"]
    # Loop-guard timeout (0 - 120 min, default = 45). | Default: 45 | Min: 0 | Max: 120
    loop_guard_timeout: int
    # Switch controller dynamic port policy from available options | MaxLen: 63
    port_policy: str
    # Switch controller QoS policy from available options. | Default: default | MaxLen: 63
    qos_policy: str
    # Switch controller storm control policy from available option | Default: default | MaxLen: 63
    storm_control_policy: str
    # Switch controller authentication policy to apply to this man | MaxLen: 31
    port_security_policy: str
    # Switch controller export port to pool-list. | MaxLen: 35
    export_to_pool: str
    # Tag(s) associated with the interface for various features in
    interface_tags: str
    # Limit the number of dynamic MAC addresses on this Port | Default: 0 | Min: 0 | Max: 128
    learning_limit: int
    # Enable or disable sticky-mac on the interface. | Default: disable
    sticky_mac: Literal["enable", "disable"]
    # LLDP transmit and receive status. | Default: tx-rx
    lldp_status: Literal["disable", "rx-only", "tx-only", "tx-rx"]
    # LLDP port TLV profile. | Default: default-auto-isl | MaxLen: 63
    lldp_profile: str
    # Export managed-switch port to a tenant VDOM. | MaxLen: 31
    export_to: str
    # Port/Trunk MAC. | Default: 00:00:00:00:00:00
    mac_addr: str
    # Enable/Disable allow ARP monitor. | Default: disable
    allow_arp_monitor: Literal["disable", "enable"]
    # 802.1AD VLANs in the VDom. | MaxLen: 15
    qnq: str
    # Enable/disable logging for dynamic MAC address events. | Default: disable
    log_mac_event: Literal["disable", "enable"]
    # Algorithm for aggregate port selection. | Default: src-dst-ip
    port_selection_criteria: Literal["src-mac", "dst-mac", "src-dst-mac", "src-ip", "dst-ip", "src-dst-ip"]
    # Description for port. | MaxLen: 63
    description: str
    # End Link Aggregation Control Protocol (LACP) messages every | Default: slow
    lacp_speed: Literal["slow", "fast"]
    # LACP mode: ignore and do not send control messages, or negot | Default: static
    mode: Literal["static", "lacp-passive", "lacp-active"]
    # Enable/disable Link Aggregation Group (LAG) bundling for non | Default: disable
    bundle: Literal["enable", "disable"]
    # Port behavior after it withdraws because of loss of control | Default: block
    member_withdrawal_behavior: Literal["forward", "block"]
    # Enable/disable multi-chassis link aggregation (MCLAG). | Default: disable
    mclag: Literal["enable", "disable"]
    # Minimum size of LAG bundle (1 - 24, default = 1). | Default: 1 | Min: 1 | Max: 24
    min_bundle: int
    # Maximum size of LAG bundle (1 - 24, default = 24). | Default: 24 | Min: 1 | Max: 24
    max_bundle: int
    # Aggregated LAG bundle interfaces.
    members: str
    # LACP fallback port. | MaxLen: 79
    fallback_port: str
    
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
class ManagedSwitchIpsourceguardObject:
    """Typed object for ip-source-guard table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Ingress interface to which source guard is bound. | MaxLen: 15
    port: str
    # Description. | MaxLen: 63
    description: str
    # IP and MAC address configuration.
    binding_entry: str
    
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
class ManagedSwitchStpinstanceObject:
    """Typed object for stp-instance table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Instance ID. | MaxLen: 2
    id: str
    # Priority. | Default: 32768
    priority: Literal["0", "4096", "8192", "12288", "16384", "20480", "24576", "28672", "32768", "36864", "40960", "45056", "49152", "53248", "57344", "61440"]
    
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
class ManagedSwitchSnmpcommunityObject:
    """Typed object for snmp-community table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SNMP community ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # SNMP community name. | MaxLen: 35
    name: str
    # Enable/disable this SNMP community. | Default: enable
    status: Literal["disable", "enable"]
    # Configure IPv4 SNMP managers (hosts).
    hosts: str
    # Enable/disable SNMP v1 queries. | Default: enable
    query_v1_status: Literal["disable", "enable"]
    # SNMP v1 query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v1_port: int
    # Enable/disable SNMP v2c queries. | Default: enable
    query_v2c_status: Literal["disable", "enable"]
    # SNMP v2c query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_v2c_port: int
    # Enable/disable SNMP v1 traps. | Default: enable
    trap_v1_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v1_lport: int
    # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v1_rport: int
    # Enable/disable SNMP v2c traps. | Default: enable
    trap_v2c_status: Literal["disable", "enable"]
    # SNMP v2c trap local port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_lport: int
    # SNMP v2c trap remote port (default = 162). | Default: 162 | Min: 0 | Max: 65535
    trap_v2c_rport: int
    # SNMP notifications (traps) to send. | Default: cpu-high mem-low log-full intf-ip ent-conf-change l2mac
    events: Literal["cpu-high", "mem-low", "log-full", "intf-ip", "ent-conf-change", "l2mac"]
    
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
class ManagedSwitchSnmpuserObject:
    """Typed object for snmp-user table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # SNMP user name. | MaxLen: 32
    name: str
    # Enable/disable SNMP queries for this user. | Default: enable
    queries: Literal["disable", "enable"]
    # SNMPv3 query port (default = 161). | Default: 161 | Min: 0 | Max: 65535
    query_port: int
    # Security level for message authentication and encryption. | Default: no-auth-no-priv
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"]
    # Authentication protocol. | Default: sha256
    auth_proto: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
    # Password for authentication protocol. | MaxLen: 128
    auth_pwd: str
    # Privacy (encryption) protocol. | Default: aes128
    priv_proto: Literal["aes128", "aes192", "aes192c", "aes256", "aes256c", "des"]
    # Password for privacy (encryption) protocol. | MaxLen: 128
    priv_pwd: str
    
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
class ManagedSwitchRemotelogObject:
    """Typed object for remote-log table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Remote log name. | MaxLen: 35
    name: str
    # Enable/disable logging by FortiSwitch device to a remote sys | Default: disable
    status: Literal["enable", "disable"]
    # IPv4 address of the remote syslog server. | MaxLen: 63
    server: str
    # Remote syslog server listening port. | Default: 514 | Min: 0 | Max: 65535
    port: int
    # Severity of logs to be transferred to remote log server. | Default: information
    severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]
    # Enable/disable comma-separated value (CSV) strings. | Default: disable
    csv: Literal["enable", "disable"]
    # Facility to log to remote syslog server. | Default: local7
    facility: Literal["kernel", "user", "mail", "daemon", "auth", "syslog", "lpr", "news", "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"]
    
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
class ManagedSwitchMirrorObject:
    """Typed object for mirror table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Mirror name. | MaxLen: 63
    name: str
    # Active/inactive mirror configuration. | Default: inactive
    status: Literal["active", "inactive"]
    # Enable/disable switching functionality when mirroring. | Default: disable
    switching_packet: Literal["enable", "disable"]
    # Destination port. | MaxLen: 63
    dst: str
    # Source ingress interfaces.
    src_ingress: str
    # Source egress interfaces.
    src_egress: str
    
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
class ManagedSwitchStaticmacObject:
    """Typed object for static-mac table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Type. | Default: static
    type: Literal["static", "sticky"]
    # Vlan. | MaxLen: 15
    vlan: str
    # MAC address. | Default: 00:00:00:00:00:00
    mac: str
    # Interface name. | MaxLen: 35
    interface: str
    # Description. | MaxLen: 63
    description: str
    
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
class ManagedSwitchCustomcommandObject:
    """Typed object for custom-command table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # List of FortiSwitch commands. | MaxLen: 35
    command_entry: str
    # Names of commands to be pushed to this FortiSwitch device, a | MaxLen: 35
    command_name: str
    
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
class ManagedSwitchDhcpsnoopingstaticclientObject:
    """Typed object for dhcp-snooping-static-client table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Client name. | MaxLen: 35
    name: str
    # VLAN name. | MaxLen: 15
    vlan: str
    # Client static IP address. | Default: 0.0.0.0
    ip: str
    # Client MAC address. | Default: 00:00:00:00:00:00
    mac: str
    # Interface name. | MaxLen: 15
    port: str
    
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
class ManagedSwitchRoutervrfObject:
    """Typed object for router-vrf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # VRF entry name. | MaxLen: 35
    name: str
    # Switch ID. | MaxLen: 35
    switch_id: str
    # VRF ID. | Default: 0 | Min: 0 | Max: 1023
    vrfid: int
    
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
class ManagedSwitchSysteminterfaceObject:
    """Typed object for system-interface table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Interface name. | MaxLen: 15
    name: str
    # Switch ID. | MaxLen: 35
    switch_id: str
    # Interface addressing mode. | Default: static
    mode: Literal["static", "dhcp"]
    # IP and mask for this interface. | Default: 0.0.0.0 0.0.0.0
    ip: str
    # Enable/disable interface status. | Default: enable
    status: Literal["disable", "enable"]
    # Permitted types of management access to this interface.
    allowaccess: Literal["ping", "https", "http", "ssh", "snmp", "telnet", "radius-acct"]
    # VLAN name. | MaxLen: 15
    vlan: str
    # Interface type. | Default: vlan
    type: Literal["vlan", "physical"]
    # Interface name. | MaxLen: 63
    interface: str
    # VRF for this route. | MaxLen: 63
    vrf: str
    
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
class ManagedSwitchRouterstaticObject:
    """Typed object for router-static table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry sequence number. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Switch ID. | MaxLen: 35
    switch_id: str
    # Enable/disable blackhole on this route. | Default: disable
    blackhole: Literal["disable", "enable"]
    # Comment. | MaxLen: 63
    comment: str
    # Gateway out interface. | MaxLen: 35
    device: str
    # Administrative distance for the route | Default: 10 | Min: 1 | Max: 255
    distance: int
    # Destination ip and mask for this route. | Default: 0.0.0.0 0.0.0.0
    dst: str
    # Enable/disable dynamic gateway. | Default: disable
    dynamic_gateway: Literal["disable", "enable"]
    # Gateway ip for this route. | Default: 0.0.0.0
    gateway: str
    # Enable/disable route status. | Default: enable
    status: Literal["disable", "enable"]
    # VRF for this route. | MaxLen: 35
    vrf: str
    
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
class ManagedSwitchSystemdhcpserverObject:
    """Typed object for system-dhcp-server table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Switch ID. | MaxLen: 35
    switch_id: str
    # Enable/disable this DHCP configuration. | Default: enable
    status: Literal["disable", "enable"]
    # Lease time in seconds, 0 means unlimited. | Default: 604800 | Min: 0 | Max: 4294967295
    lease_time: int
    # Options for assigning DNS servers to DHCP clients. | Default: specify
    dns_service: Literal["local", "default", "specify"]
    # DNS server 1. | Default: 0.0.0.0
    dns_server1: str
    # DNS server 2. | Default: 0.0.0.0
    dns_server2: str
    # DNS server 3. | Default: 0.0.0.0
    dns_server3: str
    # Options for assigning Network Time Protocol (NTP) servers to | Default: specify
    ntp_service: Literal["local", "default", "specify"]
    # NTP server 1. | Default: 0.0.0.0
    ntp_server1: str
    # NTP server 2. | Default: 0.0.0.0
    ntp_server2: str
    # NTP server 3. | Default: 0.0.0.0
    ntp_server3: str
    # Default gateway IP address assigned by the DHCP server. | Default: 0.0.0.0
    default_gateway: str
    # Netmask assigned by the DHCP server. | Default: 0.0.0.0
    netmask: str
    # DHCP server can assign IP configurations to clients connecte | MaxLen: 15
    interface: str
    # DHCP IP range configuration.
    ip_range: str
    # DHCP options.
    options: str
    
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
class ManagedSwitchResponse(TypedDict):
    """
    Type hints for switch_controller/managed_switch API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    switch_id: str  # Managed-switch name. | MaxLen: 35
    sn: str  # Managed-switch serial number. | MaxLen: 16
    description: str  # Description. | MaxLen: 63
    switch_profile: str  # FortiSwitch profile. | Default: default | MaxLen: 35
    access_profile: str  # FortiSwitch access profile. | Default: default | MaxLen: 31
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # Purdue Level of this FortiSwitch. | Default: 3
    fsw_wan1_peer: str  # FortiSwitch WAN1 peer port. | MaxLen: 35
    fsw_wan1_admin: Literal["discovered", "disable", "enable"]  # FortiSwitch WAN1 admin status; enable to authorize | Default: discovered
    poe_pre_standard_detection: Literal["enable", "disable"]  # Enable/disable PoE pre-standard detection. | Default: disable
    dhcp_server_access_list: Literal["global", "enable", "disable"]  # DHCP snooping server access list. | Default: global
    poe_detection_type: int  # PoE detection type for FortiSwitch. | Default: 0 | Min: 0 | Max: 255
    max_poe_budget: int  # Max PoE budget for FortiSwitch. | Default: 0 | Min: 0 | Max: 65535
    directly_connected: int  # Directly connected FortiSwitch. | Default: 0 | Min: 0 | Max: 1
    version: int  # FortiSwitch version. | Default: 0 | Min: 0 | Max: 255
    max_allowed_trunk_members: int  # FortiSwitch maximum allowed trunk members. | Default: 0 | Min: 0 | Max: 255
    pre_provisioned: int  # Pre-provisioned managed switch. | Default: 0 | Min: 0 | Max: 255
    l3_discovered: int  # Layer 3 management discovered. | Default: 0 | Min: 0 | Max: 1
    mgmt_mode: int  # FortiLink management mode. | Default: 0 | Min: 0 | Max: 255
    tunnel_discovered: int  # SOCKS tunnel management discovered. | Default: 0 | Min: 0 | Max: 1
    tdr_supported: str  # TDR supported. | MaxLen: 31
    dynamic_capability: str  # List of features this FortiSwitch supports | Default: 0x00000000000000000000000000000000
    switch_device_tag: str  # User definable label/tag. | MaxLen: 32
    switch_dhcp_opt43_key: str  # DHCP option43 key. | MaxLen: 63
    mclag_igmp_snooping_aware: Literal["enable", "disable"]  # Enable/disable MCLAG IGMP-snooping awareness. | Default: enable
    dynamically_discovered: int  # Dynamically discovered FortiSwitch. | Default: 0 | Min: 0 | Max: 1
    ptp_status: Literal["disable", "enable"]  # Enable/disable PTP profile on this FortiSwitch. | Default: disable
    ptp_profile: str  # PTP profile configuration. | Default: default | MaxLen: 63
    radius_nas_ip_override: Literal["disable", "enable"]  # Use locally defined NAS-IP. | Default: disable
    radius_nas_ip: str  # NAS-IP address. | Default: 0.0.0.0
    route_offload: Literal["disable", "enable"]  # Enable/disable route offload on this FortiSwitch. | Default: disable
    route_offload_mclag: Literal["disable", "enable"]  # Enable/disable route offload MCLAG on this FortiSw | Default: disable
    route_offload_router: list[ManagedSwitchRouteoffloadrouterItem]  # Configure route offload MCLAG IP address.
    vlan: list[ManagedSwitchVlanItem]  # Configure VLAN assignment priority.
    type: Literal["virtual", "physical"]  # Indication of switch type, physical or virtual. | Default: physical
    owner_vdom: str  # VDOM which owner of port belongs to. | MaxLen: 31
    flow_identity: str  # Flow-tracking netflow ipfix switch identity in hex | Default: 00000000
    staged_image_version: str  # Staged image version for FortiSwitch. | MaxLen: 127
    delayed_restart_trigger: int  # Delayed restart triggered for this FortiSwitch. | Default: 0 | Min: 0 | Max: 255
    firmware_provision: Literal["enable", "disable"]  # Enable/disable provisioning of firmware to FortiSw | Default: disable
    firmware_provision_version: str  # Firmware version to provision to this FortiSwitch | MaxLen: 35
    firmware_provision_latest: Literal["disable", "once"]  # Enable/disable one-time automatic provisioning of | Default: disable
    ports: list[ManagedSwitchPortsItem]  # Managed-switch port list.
    ip_source_guard: list[ManagedSwitchIpsourceguardItem]  # IP source guard.
    stp_settings: str  # Configuration method to edit Spanning Tree Protoco
    stp_instance: list[ManagedSwitchStpinstanceItem]  # Configuration method to edit Spanning Tree Protoco
    override_snmp_sysinfo: Literal["disable", "enable"]  # Enable/disable overriding the global SNMP system i | Default: disable
    snmp_sysinfo: str  # Configuration method to edit Simple Network Manage
    override_snmp_trap_threshold: Literal["enable", "disable"]  # Enable/disable overriding the global SNMP trap thr | Default: disable
    snmp_trap_threshold: str  # Configuration method to edit Simple Network Manage
    override_snmp_community: Literal["enable", "disable"]  # Enable/disable overriding the global SNMP communit | Default: disable
    snmp_community: list[ManagedSwitchSnmpcommunityItem]  # Configuration method to edit Simple Network Manage
    override_snmp_user: Literal["enable", "disable"]  # Enable/disable overriding the global SNMP users. | Default: disable
    snmp_user: list[ManagedSwitchSnmpuserItem]  # Configuration method to edit Simple Network Manage
    qos_drop_policy: Literal["taildrop", "random-early-detection"]  # Set QoS drop-policy. | Default: taildrop
    qos_red_probability: int  # Set QoS RED/WRED drop probability. | Default: 12 | Min: 0 | Max: 100
    switch_log: str  # Configuration method to edit FortiSwitch logging s
    remote_log: list[ManagedSwitchRemotelogItem]  # Configure logging by FortiSwitch device to a remot
    storm_control: str  # Configuration method to edit FortiSwitch storm con
    mirror: list[ManagedSwitchMirrorItem]  # Configuration method to edit FortiSwitch packet mi
    static_mac: list[ManagedSwitchStaticmacItem]  # Configuration method to edit FortiSwitch Static an
    custom_command: list[ManagedSwitchCustomcommandItem]  # Configuration method to edit FortiSwitch commands
    dhcp_snooping_static_client: list[ManagedSwitchDhcpsnoopingstaticclientItem]  # Configure FortiSwitch DHCP snooping static clients
    igmp_snooping: str  # Configure FortiSwitch IGMP snooping global setting
    x802_1X_settings: str  # Configuration method to edit FortiSwitch 802.1X gl
    router_vrf: list[ManagedSwitchRoutervrfItem]  # Configure VRF.
    system_interface: list[ManagedSwitchSysteminterfaceItem]  # Configure system interface on FortiSwitch.
    router_static: list[ManagedSwitchRouterstaticItem]  # Configure static routes.
    system_dhcp_server: list[ManagedSwitchSystemdhcpserverItem]  # Configure DHCP servers.


@final
class ManagedSwitchObject:
    """Typed FortiObject for switch_controller/managed_switch with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Managed-switch name. | MaxLen: 35
    switch_id: str
    # Managed-switch serial number. | MaxLen: 16
    sn: str
    # Description. | MaxLen: 63
    description: str
    # FortiSwitch profile. | Default: default | MaxLen: 35
    switch_profile: str
    # FortiSwitch access profile. | Default: default | MaxLen: 31
    access_profile: str
    # Purdue Level of this FortiSwitch. | Default: 3
    purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # FortiSwitch WAN1 peer port. | MaxLen: 35
    fsw_wan1_peer: str
    # FortiSwitch WAN1 admin status; enable to authorize the Forti | Default: discovered
    fsw_wan1_admin: Literal["discovered", "disable", "enable"]
    # Enable/disable PoE pre-standard detection. | Default: disable
    poe_pre_standard_detection: Literal["enable", "disable"]
    # DHCP snooping server access list. | Default: global
    dhcp_server_access_list: Literal["global", "enable", "disable"]
    # PoE detection type for FortiSwitch. | Default: 0 | Min: 0 | Max: 255
    poe_detection_type: int
    # Max PoE budget for FortiSwitch. | Default: 0 | Min: 0 | Max: 65535
    max_poe_budget: int
    # Directly connected FortiSwitch. | Default: 0 | Min: 0 | Max: 1
    directly_connected: int
    # FortiSwitch version. | Default: 0 | Min: 0 | Max: 255
    version: int
    # FortiSwitch maximum allowed trunk members. | Default: 0 | Min: 0 | Max: 255
    max_allowed_trunk_members: int
    # Pre-provisioned managed switch. | Default: 0 | Min: 0 | Max: 255
    pre_provisioned: int
    # Layer 3 management discovered. | Default: 0 | Min: 0 | Max: 1
    l3_discovered: int
    # FortiLink management mode. | Default: 0 | Min: 0 | Max: 255
    mgmt_mode: int
    # SOCKS tunnel management discovered. | Default: 0 | Min: 0 | Max: 1
    tunnel_discovered: int
    # TDR supported. | MaxLen: 31
    tdr_supported: str
    # List of features this FortiSwitch supports | Default: 0x00000000000000000000000000000000
    dynamic_capability: str
    # User definable label/tag. | MaxLen: 32
    switch_device_tag: str
    # DHCP option43 key. | MaxLen: 63
    switch_dhcp_opt43_key: str
    # Enable/disable MCLAG IGMP-snooping awareness. | Default: enable
    mclag_igmp_snooping_aware: Literal["enable", "disable"]
    # Dynamically discovered FortiSwitch. | Default: 0 | Min: 0 | Max: 1
    dynamically_discovered: int
    # Enable/disable PTP profile on this FortiSwitch. | Default: disable
    ptp_status: Literal["disable", "enable"]
    # PTP profile configuration. | Default: default | MaxLen: 63
    ptp_profile: str
    # Use locally defined NAS-IP. | Default: disable
    radius_nas_ip_override: Literal["disable", "enable"]
    # NAS-IP address. | Default: 0.0.0.0
    radius_nas_ip: str
    # Enable/disable route offload on this FortiSwitch. | Default: disable
    route_offload: Literal["disable", "enable"]
    # Enable/disable route offload MCLAG on this FortiSwitch. | Default: disable
    route_offload_mclag: Literal["disable", "enable"]
    # Configure route offload MCLAG IP address.
    route_offload_router: list[ManagedSwitchRouteoffloadrouterObject]
    # Configure VLAN assignment priority.
    vlan: list[ManagedSwitchVlanObject]
    # Indication of switch type, physical or virtual. | Default: physical
    type: Literal["virtual", "physical"]
    # VDOM which owner of port belongs to. | MaxLen: 31
    owner_vdom: str
    # Flow-tracking netflow ipfix switch identity in hex format | Default: 00000000
    flow_identity: str
    # Staged image version for FortiSwitch. | MaxLen: 127
    staged_image_version: str
    # Delayed restart triggered for this FortiSwitch. | Default: 0 | Min: 0 | Max: 255
    delayed_restart_trigger: int
    # Enable/disable provisioning of firmware to FortiSwitches on | Default: disable
    firmware_provision: Literal["enable", "disable"]
    # Firmware version to provision to this FortiSwitch on bootup | MaxLen: 35
    firmware_provision_version: str
    # Enable/disable one-time automatic provisioning of the latest | Default: disable
    firmware_provision_latest: Literal["disable", "once"]
    # Managed-switch port list.
    ports: list[ManagedSwitchPortsObject]
    # IP source guard.
    ip_source_guard: list[ManagedSwitchIpsourceguardObject]
    # Configuration method to edit Spanning Tree Protocol (STP) se
    stp_settings: str
    # Configuration method to edit Spanning Tree Protocol (STP) in
    stp_instance: list[ManagedSwitchStpinstanceObject]
    # Enable/disable overriding the global SNMP system information | Default: disable
    override_snmp_sysinfo: Literal["disable", "enable"]
    # Configuration method to edit Simple Network Management Proto
    snmp_sysinfo: str
    # Enable/disable overriding the global SNMP trap threshold val | Default: disable
    override_snmp_trap_threshold: Literal["enable", "disable"]
    # Configuration method to edit Simple Network Management Proto
    snmp_trap_threshold: str
    # Enable/disable overriding the global SNMP communities. | Default: disable
    override_snmp_community: Literal["enable", "disable"]
    # Configuration method to edit Simple Network Management Proto
    snmp_community: list[ManagedSwitchSnmpcommunityObject]
    # Enable/disable overriding the global SNMP users. | Default: disable
    override_snmp_user: Literal["enable", "disable"]
    # Configuration method to edit Simple Network Management Proto
    snmp_user: list[ManagedSwitchSnmpuserObject]
    # Set QoS drop-policy. | Default: taildrop
    qos_drop_policy: Literal["taildrop", "random-early-detection"]
    # Set QoS RED/WRED drop probability. | Default: 12 | Min: 0 | Max: 100
    qos_red_probability: int
    # Configuration method to edit FortiSwitch logging settings
    switch_log: str
    # Configure logging by FortiSwitch device to a remote syslog s
    remote_log: list[ManagedSwitchRemotelogObject]
    # Configuration method to edit FortiSwitch storm control for m
    storm_control: str
    # Configuration method to edit FortiSwitch packet mirror.
    mirror: list[ManagedSwitchMirrorObject]
    # Configuration method to edit FortiSwitch Static and Sticky M
    static_mac: list[ManagedSwitchStaticmacObject]
    # Configuration method to edit FortiSwitch commands to be push
    custom_command: list[ManagedSwitchCustomcommandObject]
    # Configure FortiSwitch DHCP snooping static clients.
    dhcp_snooping_static_client: list[ManagedSwitchDhcpsnoopingstaticclientObject]
    # Configure FortiSwitch IGMP snooping global settings.
    igmp_snooping: str
    # Configuration method to edit FortiSwitch 802.1X global setti
    x802_1X_settings: str
    # Configure VRF.
    router_vrf: list[ManagedSwitchRoutervrfObject]
    # Configure system interface on FortiSwitch.
    system_interface: list[ManagedSwitchSysteminterfaceObject]
    # Configure static routes.
    router_static: list[ManagedSwitchRouterstaticObject]
    # Configure DHCP servers.
    system_dhcp_server: list[ManagedSwitchSystemdhcpserverObject]
    
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
    def to_dict(self) -> ManagedSwitchPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ManagedSwitch:
    """
    Configure FortiSwitch devices that are managed by this FortiGate.
    
    Path: switch_controller/managed_switch
    Category: cmdb
    Primary Key: switch-id
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        switch_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ManagedSwitchObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        switch_id: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ManagedSwitchObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        switch_id: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> list[ManagedSwitchObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        switch_id: str,
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
    ) -> ManagedSwitchObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        switch_id: str,
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
    ) -> ManagedSwitchObject: ...
    
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
    ) -> list[ManagedSwitchObject]: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def get(
        self,
        switch_id: str | None = ...,
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
        switch_id: str,
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
    ) -> ManagedSwitchObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        switch_id: str,
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
    ) -> ManagedSwitchObject: ...
    
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
    ) -> list[ManagedSwitchObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        switch_id: str | None = ...,
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
        switch_id: str | None = ...,
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
    ) -> ManagedSwitchObject | list[ManagedSwitchObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ManagedSwitchObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ManagedSwitchObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ManagedSwitchObject: ...
    
    @overload
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        switch_id: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        switch_id: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ManagedSwitchPayload | None = ...,
        switch_id: str | None = ...,
        sn: str | None = ...,
        description: str | None = ...,
        switch_profile: str | None = ...,
        access_profile: str | None = ...,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        fsw_wan1_peer: str | None = ...,
        fsw_wan1_admin: Literal["discovered", "disable", "enable"] | None = ...,
        poe_pre_standard_detection: Literal["enable", "disable"] | None = ...,
        dhcp_server_access_list: Literal["global", "enable", "disable"] | None = ...,
        poe_detection_type: int | None = ...,
        max_poe_budget: int | None = ...,
        directly_connected: int | None = ...,
        version: int | None = ...,
        max_allowed_trunk_members: int | None = ...,
        pre_provisioned: int | None = ...,
        l3_discovered: int | None = ...,
        mgmt_mode: int | None = ...,
        tunnel_discovered: int | None = ...,
        tdr_supported: str | None = ...,
        dynamic_capability: str | None = ...,
        switch_device_tag: str | None = ...,
        switch_dhcp_opt43_key: str | None = ...,
        mclag_igmp_snooping_aware: Literal["enable", "disable"] | None = ...,
        dynamically_discovered: int | None = ...,
        ptp_status: Literal["disable", "enable"] | None = ...,
        ptp_profile: str | None = ...,
        radius_nas_ip_override: Literal["disable", "enable"] | None = ...,
        radius_nas_ip: str | None = ...,
        route_offload: Literal["disable", "enable"] | None = ...,
        route_offload_mclag: Literal["disable", "enable"] | None = ...,
        route_offload_router: str | list[str] | list[dict[str, Any]] | None = ...,
        vlan: str | list[str] | list[dict[str, Any]] | None = ...,
        type: Literal["virtual", "physical"] | None = ...,
        owner_vdom: str | None = ...,
        flow_identity: str | None = ...,
        staged_image_version: str | None = ...,
        delayed_restart_trigger: int | None = ...,
        firmware_provision: Literal["enable", "disable"] | None = ...,
        firmware_provision_version: str | None = ...,
        firmware_provision_latest: Literal["disable", "once"] | None = ...,
        ports: str | list[str] | list[dict[str, Any]] | None = ...,
        ip_source_guard: str | list[str] | list[dict[str, Any]] | None = ...,
        stp_settings: str | None = ...,
        stp_instance: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_sysinfo: Literal["disable", "enable"] | None = ...,
        snmp_sysinfo: str | None = ...,
        override_snmp_trap_threshold: Literal["enable", "disable"] | None = ...,
        snmp_trap_threshold: str | None = ...,
        override_snmp_community: Literal["enable", "disable"] | None = ...,
        snmp_community: str | list[str] | list[dict[str, Any]] | None = ...,
        override_snmp_user: Literal["enable", "disable"] | None = ...,
        snmp_user: str | list[str] | list[dict[str, Any]] | None = ...,
        qos_drop_policy: Literal["taildrop", "random-early-detection"] | None = ...,
        qos_red_probability: int | None = ...,
        switch_log: str | None = ...,
        remote_log: str | list[str] | list[dict[str, Any]] | None = ...,
        storm_control: str | None = ...,
        mirror: str | list[str] | list[dict[str, Any]] | None = ...,
        static_mac: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_command: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_snooping_static_client: str | list[str] | list[dict[str, Any]] | None = ...,
        igmp_snooping: str | None = ...,
        x802_1X_settings: str | None = ...,
        router_vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        system_interface: str | list[str] | list[dict[str, Any]] | None = ...,
        router_static: str | list[str] | list[dict[str, Any]] | None = ...,
        system_dhcp_server: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ManagedSwitch",
    "ManagedSwitchPayload",
    "ManagedSwitchResponse",
    "ManagedSwitchObject",
]
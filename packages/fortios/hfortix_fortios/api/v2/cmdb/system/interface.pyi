from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class InterfacePayload(TypedDict, total=False):
    """
    Type hints for system/interface payload fields.
    
    Configure interfaces.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.certificate.ca.CaEndpoint` (via: eap-ca-cert)
        - :class:`~.certificate.local.LocalEndpoint` (via: eap-user-cert)
        - :class:`~.firewall.shaping-profile.ShapingProfileEndpoint` (via: egress-shaping-profile, ingress-shaping-profile)
        - :class:`~.switch-controller.fortilink-settings.FortilinkSettingsEndpoint` (via: switch-controller-dynamic, switch-controller-nac)
        - :class:`~.switch-controller.traffic-policy.TrafficPolicyEndpoint` (via: switch-controller-traffic-policy)
        - :class:`~.system.interface.InterfaceEndpoint` (via: dhcp-relay-interface, interface)
        - :class:`~.system.lldp.network-policy.NetworkPolicyEndpoint` (via: lldp-network-policy)
        - :class:`~.system.vdom.VdomEndpoint` (via: vdom)
        - :class:`~.user.saml.SamlEndpoint` (via: ike-saml-server)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: auth-cert)

    **Usage:**
        payload: InterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 15
    vdom: str  # Interface is in this virtual domain (VDOM). | MaxLen: 31
    vrf: int  # Virtual Routing Forwarding ID. | Default: 0 | Min: 0 | Max: 511
    cli_conn_status: int  # CLI connection status. | Default: 0 | Min: 0 | Max: 4294967295
    fortilink: Literal["enable", "disable"]  # Enable FortiLink to dedicate this interface to man | Default: disable
    switch_controller_source_ip: Literal["outbound", "fixed"]  # Source IP address used in FortiLink over L3 connec | Default: outbound
    mode: Literal["static", "dhcp", "pppoe"]  # Addressing mode (static, DHCP, PPPoE). | Default: static
    client_options: list[dict[str, Any]]  # DHCP client options.
    distance: int  # Distance for routes learned through PPPoE or DHCP, | Default: 5 | Min: 1 | Max: 255
    priority: int  # Priority of learned routes. | Default: 1 | Min: 1 | Max: 65535
    dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    dhcp_relay_interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    dhcp_relay_vrf_select: int  # VRF ID used for connection to server. | Default: -1 | Min: 0 | Max: 511
    dhcp_broadcast_flag: Literal["disable", "enable"]  # Enable/disable setting of the broadcast flag in me | Default: enable
    dhcp_relay_service: Literal["disable", "enable"]  # Enable/disable allowing this interface to act as a | Default: disable
    dhcp_relay_ip: list[dict[str, Any]]  # DHCP relay IP address.
    dhcp_relay_source_ip: str  # IP address used by the DHCP relay as its source IP | Default: 0.0.0.0
    dhcp_relay_circuit_id: str  # DHCP relay circuit ID. | MaxLen: 64
    dhcp_relay_link_selection: str  # DHCP relay link selection. | Default: 0.0.0.0
    dhcp_relay_request_all_server: Literal["disable", "enable"]  # Enable/disable sending of DHCP requests to all ser | Default: disable
    dhcp_relay_allow_no_end_option: Literal["disable", "enable"]  # Enable/disable relaying DHCP messages with no end | Default: disable
    dhcp_relay_type: Literal["regular", "ipsec"]  # DHCP relay type (regular or IPsec). | Default: regular
    dhcp_smart_relay: Literal["disable", "enable"]  # Enable/disable DHCP smart relay. | Default: disable
    dhcp_relay_agent_option: Literal["enable", "disable"]  # Enable/disable DHCP relay agent option. | Default: enable
    dhcp_classless_route_addition: Literal["enable", "disable"]  # Enable/disable addition of classless static routes | Default: enable
    management_ip: str  # High Availability in-band management IP address of | Default: 0.0.0.0 0.0.0.0
    ip: str  # Interface IPv4 address and subnet mask, syntax: X. | Default: 0.0.0.0 0.0.0.0
    allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"]  # Permitted types of management access to this inter
    gwdetect: Literal["enable", "disable"]  # Enable/disable detect gateway alive for first. | Default: disable
    ping_serv_status: int  # PING server status. | Default: 0 | Min: 0 | Max: 255
    detectserver: str  # Gateway's ping server for this IP.
    detectprotocol: Literal["ping", "tcp-echo", "udp-echo"]  # Protocols used to detect the server. | Default: ping
    ha_priority: int  # HA election priority for the PING server. | Default: 1 | Min: 1 | Max: 50
    fail_detect: Literal["enable", "disable"]  # Enable/disable fail detection features for this in | Default: disable
    fail_detect_option: Literal["detectserver", "link-down"]  # Options for detecting that this interface has fail | Default: link-down
    fail_alert_method: Literal["link-failed-signal", "link-down"]  # Select link-failed-signal or link-down method to a | Default: link-down
    fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"]  # Action on FortiExtender when interface fail. | Default: soft-restart
    fail_alert_interfaces: list[dict[str, Any]]  # Names of the FortiGate interfaces to which the lin
    dhcp_client_identifier: str  # DHCP client identifier. | MaxLen: 48
    dhcp_renew_time: int  # DHCP renew time in seconds (300-604800), 0 means u | Default: 0 | Min: 300 | Max: 604800
    ipunnumbered: str  # Unnumbered IP used for PPPoE interfaces for which | Default: 0.0.0.0
    username: str  # Username of the PPPoE account, provided by your IS | MaxLen: 64
    pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"]  # CoS in VLAN tag for outgoing PPPoE/PPP packets. | Default: cos0
    pppoe_unnumbered_negotiate: Literal["enable", "disable"]  # Enable/disable PPPoE unnumbered negotiation. | Default: enable
    password: str  # PPPoE account's password. | MaxLen: 128
    idle_timeout: int  # PPPoE auto disconnect after idle timeout seconds, | Default: 0 | Min: 0 | Max: 32767
    multilink: Literal["enable", "disable"]  # Enable/disable PPP multilink support. | Default: disable
    mrru: int  # PPP MRRU (296 - 65535, default = 1500). | Default: 1500 | Min: 296 | Max: 65535
    detected_peer_mtu: int  # MTU of detected peer (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    disc_retry_timeout: int  # Time in seconds to wait before retrying to start a | Default: 1 | Min: 0 | Max: 4294967295
    padt_retry_timeout: int  # PPPoE Active Discovery Terminate (PADT) used to te | Default: 1 | Min: 0 | Max: 4294967295
    service_name: str  # PPPoE service name. | MaxLen: 63
    ac_name: str  # PPPoE server name. | MaxLen: 63
    lcp_echo_interval: int  # Time in seconds between PPPoE Link Control Protoco | Default: 5 | Min: 0 | Max: 32767
    lcp_max_echo_fails: int  # Maximum missed LCP echo messages before disconnect | Default: 3 | Min: 0 | Max: 32767
    defaultgw: Literal["enable", "disable"]  # Enable to get the gateway IP from the DHCP or PPPo | Default: enable
    dns_server_override: Literal["enable", "disable"]  # Enable/disable use DNS acquired by DHCP or PPPoE. | Default: enable
    dns_server_protocol: Literal["cleartext", "dot", "doh"]  # DNS transport protocols. | Default: cleartext
    auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]  # PPP authentication type to use. | Default: auto
    pptp_client: Literal["enable", "disable"]  # Enable/disable PPTP client. | Default: disable
    pptp_user: str  # PPTP user name. | MaxLen: 64
    pptp_password: str  # PPTP password. | MaxLen: 128
    pptp_server_ip: str  # PPTP server IP address. | Default: 0.0.0.0
    pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]  # PPTP authentication type. | Default: auto
    pptp_timeout: int  # Idle timer in minutes (0 for disabled). | Default: 0 | Min: 0 | Max: 65535
    arpforward: Literal["enable", "disable"]  # Enable/disable ARP forwarding. | Default: enable
    ndiscforward: Literal["enable", "disable"]  # Enable/disable NDISC forwarding. | Default: enable
    broadcast_forward: Literal["enable", "disable"]  # Enable/disable broadcast forwarding. | Default: disable
    bfd: Literal["global", "enable", "disable"]  # Bidirectional Forwarding Detection (BFD) settings. | Default: global
    bfd_desired_min_tx: int  # BFD desired minimal transmit interval. | Default: 250 | Min: 1 | Max: 100000
    bfd_detect_mult: int  # BFD detection multiplier. | Default: 3 | Min: 1 | Max: 50
    bfd_required_min_rx: int  # BFD required minimal receive interval. | Default: 250 | Min: 1 | Max: 100000
    l2forward: Literal["enable", "disable"]  # Enable/disable l2 forwarding. | Default: disable
    icmp_send_redirect: Literal["enable", "disable"]  # Enable/disable sending of ICMP redirects. | Default: enable
    icmp_accept_redirect: Literal["enable", "disable"]  # Enable/disable ICMP accept redirect. | Default: enable
    reachable_time: int  # IPv4 reachable time in milliseconds | Default: 30000 | Min: 30000 | Max: 3600000
    vlanforward: Literal["enable", "disable"]  # Enable/disable traffic forwarding between VLANs on | Default: disable
    stpforward: Literal["enable", "disable"]  # Enable/disable STP forwarding. | Default: disable
    stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"]  # Configure STP forwarding mode. | Default: rpl-all-ext-id
    ips_sniffer_mode: Literal["enable", "disable"]  # Enable/disable the use of this interface as a one- | Default: disable
    ident_accept: Literal["enable", "disable"]  # Enable/disable authentication for this interface. | Default: disable
    ipmac: Literal["enable", "disable"]  # Enable/disable IP/MAC binding. | Default: disable
    subst: Literal["enable", "disable"]  # Enable to always send packets from this interface | Default: disable
    macaddr: str  # Change the interface's MAC address. | Default: 00:00:00:00:00:00
    virtual_mac: str  # Change the interface's virtual MAC address. | Default: 00:00:00:00:00:00
    substitute_dst_mac: str  # Destination MAC address that all packets are sent | Default: 00:00:00:00:00:00
    speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"]  # Interface speed. The default setting and the optio | Default: auto
    status: Literal["up", "down"]  # Bring the interface up or shut the interface down. | Default: up
    netbios_forward: Literal["disable", "enable"]  # Enable/disable NETBIOS forwarding. | Default: disable
    wins_ip: str  # WINS server IP. | Default: 0.0.0.0
    type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"]  # Interface type. | Default: vlan
    dedicated_to: Literal["none", "management"]  # Configure interface for single purpose. | Default: none
    trust_ip_1: str  # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip_2: str  # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip_3: str  # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip6_1: str  # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    trust_ip6_2: str  # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    trust_ip6_3: str  # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    ring_rx: int  # RX ring size. | Default: 0 | Min: 0 | Max: 4294967295
    ring_tx: int  # TX ring size. | Default: 0 | Min: 0 | Max: 4294967295
    wccp: Literal["enable", "disable"]  # Enable/disable WCCP on this interface. Used for en | Default: disable
    netflow_sampler: Literal["disable", "tx", "rx", "both"]  # Enable/disable NetFlow on this interface and set t | Default: disable
    netflow_sample_rate: int  # NetFlow sample rate.  Sample one packet every conf | Default: 1 | Min: 1 | Max: 65535
    netflow_sampler_id: int  # Netflow sampler ID. | Default: 0 | Min: 1 | Max: 254
    sflow_sampler: Literal["enable", "disable"]  # Enable/disable sFlow on this interface. | Default: disable
    drop_fragment: Literal["enable", "disable"]  # Enable/disable drop fragment packets. | Default: disable
    src_check: Literal["enable", "disable"]  # Enable/disable source IP check. | Default: enable
    sample_rate: int  # sFlow sample rate (10 - 99999). | Default: 2000 | Min: 10 | Max: 99999
    polling_interval: int  # sFlow polling interval in seconds (1 - 255). | Default: 20 | Min: 1 | Max: 255
    sample_direction: Literal["tx", "rx", "both"]  # Data that NetFlow collects (rx, tx, or both). | Default: both
    explicit_web_proxy: Literal["enable", "disable"]  # Enable/disable the explicit web proxy on this inte | Default: disable
    explicit_ftp_proxy: Literal["enable", "disable"]  # Enable/disable the explicit FTP proxy on this inte | Default: disable
    proxy_captive_portal: Literal["enable", "disable"]  # Enable/disable proxy captive portal on this interf | Default: disable
    tcp_mss: int  # TCP maximum segment size. 0 means do not change se | Default: 0 | Min: 48 | Max: 65535
    inbandwidth: int  # Bandwidth limit for incoming traffic | Default: 0 | Min: 0 | Max: 80000000
    outbandwidth: int  # Bandwidth limit for outgoing traffic | Default: 0 | Min: 0 | Max: 80000000
    egress_shaping_profile: str  # Outgoing traffic shaping profile. | MaxLen: 35
    ingress_shaping_profile: str  # Incoming traffic shaping profile. | MaxLen: 35
    spillover_threshold: int  # Egress Spillover threshold (0 - 16776000 kbps), 0 | Default: 0 | Min: 0 | Max: 16776000
    ingress_spillover_threshold: int  # Ingress Spillover threshold (0 - 16776000 kbps), 0 | Default: 0 | Min: 0 | Max: 16776000
    weight: int  # Default weight for static routes | Default: 0 | Min: 0 | Max: 255
    interface: str  # Interface name. | MaxLen: 15
    external: Literal["enable", "disable"]  # Enable/disable identifying the interface as an ext | Default: disable
    mtu_override: Literal["enable", "disable"]  # Enable to set a custom MTU for this interface. | Default: disable
    mtu: int  # MTU value for this interface. | Default: 1500 | Min: 0 | Max: 4294967295
    vlan_protocol: Literal["8021q", "8021ad"]  # Ethernet protocol of VLAN. | Default: 8021q
    vlanid: int  # VLAN ID (1 - 4094). | Default: 0 | Min: 1 | Max: 4094
    forward_domain: int  # Transparent mode forward domain. | Default: 0 | Min: 0 | Max: 2147483647
    remote_ip: str  # Remote IP address of tunnel. | Default: 0.0.0.0 0.0.0.0
    member: list[dict[str, Any]]  # Physical interfaces that belong to the aggregate o
    lacp_mode: Literal["static", "passive", "active"]  # LACP mode. | Default: active
    lacp_ha_secondary: Literal["enable", "disable"]  # LACP HA secondary member. | Default: enable
    system_id_type: Literal["auto", "user"]  # Method in which system ID is generated. | Default: auto
    system_id: str  # Define a system ID for the aggregate interface. | Default: 00:00:00:00:00:00
    lacp_speed: Literal["slow", "fast"]  # How often the interface sends LACP messages. | Default: slow
    min_links: int  # Minimum number of aggregated ports that must be up | Default: 1 | Min: 1 | Max: 32
    min_links_down: Literal["operational", "administrative"]  # Action to take when less than the configured minim | Default: operational
    algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"]  # Frame distribution algorithm. | Default: L4
    link_up_delay: int  # Number of milliseconds to wait before considering | Default: 50 | Min: 50 | Max: 3600000
    aggregate_type: Literal["physical", "vxlan"]  # Type of aggregation. | Default: physical
    priority_override: Literal["enable", "disable"]  # Enable/disable fail back to higher priority port o | Default: enable
    aggregate: str  # Aggregate interface. | MaxLen: 15
    redundant_interface: str  # Redundant interface. | MaxLen: 15
    devindex: int  # Device Index. | Default: 0 | Min: 0 | Max: 4294967295
    vindex: int  # Switch control interface VLAN ID. | Default: 0 | Min: 0 | Max: 65535
    switch: str  # Contained in switch. | MaxLen: 15
    description: str  # Description. | MaxLen: 255
    alias: str  # Alias will be displayed with the interface name to | MaxLen: 25
    security_mode: Literal["none", "captive-portal", "802.1X"]  # Turn on captive portal authentication for this int | Default: none
    security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"]  # Enable/disable MAC authentication bypass. | Default: disable
    security_ip_auth_bypass: Literal["enable", "disable"]  # Enable/disable IP authentication bypass. | Default: disable
    security_external_web: str  # URL of external authentication web server. | MaxLen: 1023
    security_external_logout: str  # URL of external authentication logout server. | MaxLen: 127
    replacemsg_override_group: str  # Replacement message override group. | MaxLen: 35
    security_redirect_url: str  # URL redirection after disclaimer/authentication. | MaxLen: 1023
    auth_cert: str  # HTTPS server certificate. | MaxLen: 35
    auth_portal_addr: str  # Address of captive portal. | MaxLen: 63
    security_exempt_list: str  # Name of security-exempt-list. | MaxLen: 35
    security_groups: list[dict[str, Any]]  # User groups that can authenticate with the captive
    ike_saml_server: str  # Configure IKE authentication SAML server. | MaxLen: 35
    device_identification: Literal["enable", "disable"]  # Enable/disable passively gathering of device ident | Default: disable
    exclude_signatures: Literal["iot", "ot"]  # Exclude IOT or OT application signatures.
    device_user_identification: Literal["enable", "disable"]  # Enable/disable passive gathering of user identity | Default: enable
    lldp_reception: Literal["enable", "disable", "vdom"]  # Enable/disable Link Layer Discovery Protocol | Default: vdom
    lldp_transmission: Literal["enable", "disable", "vdom"]  # Enable/disable Link Layer Discovery Protocol | Default: vdom
    lldp_network_policy: str  # LLDP-MED network policy profile. | MaxLen: 35
    estimated_upstream_bandwidth: int  # Estimated maximum upstream bandwidth (kbps). Used | Default: 0 | Min: 0 | Max: 4294967295
    estimated_downstream_bandwidth: int  # Estimated maximum downstream bandwidth (kbps). Use | Default: 0 | Min: 0 | Max: 4294967295
    measured_upstream_bandwidth: int  # Measured upstream bandwidth (kbps). | Default: 0 | Min: 0 | Max: 4294967295
    measured_downstream_bandwidth: int  # Measured downstream bandwidth (kbps). | Default: 0 | Min: 0 | Max: 4294967295
    bandwidth_measure_time: int  # Bandwidth measure time. | Default: 0 | Min: 0 | Max: 4294967295
    monitor_bandwidth: Literal["enable", "disable"]  # Enable monitoring bandwidth on this interface. | Default: disable
    vrrp_virtual_mac: Literal["enable", "disable"]  # Enable/disable use of virtual MAC for VRRP. | Default: disable
    vrrp: list[dict[str, Any]]  # VRRP configuration.
    phy_setting: str  # PHY settings
    role: Literal["lan", "wan", "dmz", "undefined"]  # Interface role. | Default: undefined
    snmp_index: int  # Permanent SNMP Index of the interface. | Default: 0 | Min: 0 | Max: 2147483647
    secondary_IP: Literal["enable", "disable"]  # Enable/disable adding a secondary IP to this inter | Default: disable
    secondaryip: list[dict[str, Any]]  # Second IP address of interface.
    preserve_session_route: Literal["enable", "disable"]  # Enable/disable preservation of session route when | Default: disable
    auto_auth_extension_device: Literal["enable", "disable"]  # Enable/disable automatic authorization of dedicate | Default: disable
    ap_discover: Literal["enable", "disable"]  # Enable/disable automatic registration of unknown F | Default: enable
    fortilink_neighbor_detect: Literal["lldp", "fortilink"]  # Protocol for FortiGate neighbor discovery. | Default: lldp
    ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"]  # Enable/disable automatic IP address assignment of | Default: inherit-global
    managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"]  # Number of IP addresses to be allocated by FortiIPA | Default: 256
    fortilink_split_interface: Literal["enable", "disable"]  # Enable/disable FortiLink split interface to connec | Default: enable
    internal: int  # Implicitly created. | Default: 0 | Min: 0 | Max: 255
    fortilink_backup_link: int  # FortiLink split interface backup link. | Default: 0 | Min: 0 | Max: 255
    switch_controller_access_vlan: Literal["enable", "disable"]  # Block FortiSwitch port-to-port traffic. | Default: disable
    switch_controller_traffic_policy: str  # Switch controller traffic policy for the VLAN. | MaxLen: 63
    switch_controller_rspan_mode: Literal["disable", "enable"]  # Stop Layer2 MAC learning and interception of BPDUs | Default: disable
    switch_controller_netflow_collect: Literal["disable", "enable"]  # NetFlow collection and processing. | Default: disable
    switch_controller_mgmt_vlan: int  # VLAN to use for FortiLink management purposes. | Default: 4094 | Min: 1 | Max: 4094
    switch_controller_igmp_snooping: Literal["enable", "disable"]  # Switch controller IGMP snooping. | Default: disable
    switch_controller_igmp_snooping_proxy: Literal["enable", "disable"]  # Switch controller IGMP snooping proxy. | Default: disable
    switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"]  # Switch controller IGMP snooping fast-leave. | Default: disable
    switch_controller_dhcp_snooping: Literal["enable", "disable"]  # Switch controller DHCP snooping. | Default: disable
    switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"]  # Switch controller DHCP snooping verify MAC. | Default: disable
    switch_controller_dhcp_snooping_option82: Literal["enable", "disable"]  # Switch controller DHCP snooping option82. | Default: disable
    dhcp_snooping_server_list: list[dict[str, Any]]  # Configure DHCP server access list.
    switch_controller_arp_inspection: Literal["enable", "disable", "monitor"]  # Enable/disable/Monitor FortiSwitch ARP inspection. | Default: disable
    switch_controller_learning_limit: int  # Limit the number of dynamic MAC addresses on this | Default: 0 | Min: 0 | Max: 128
    switch_controller_nac: str  # Integrated FortiLink settings for managed FortiSwi | MaxLen: 35
    switch_controller_dynamic: str  # Integrated FortiLink settings for managed FortiSwi | MaxLen: 35
    switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"]  # Interface's purpose when assigning traffic | Default: none
    switch_controller_iot_scanning: Literal["enable", "disable"]  # Enable/disable managed FortiSwitch IoT scanning. | Default: disable
    switch_controller_offload: Literal["enable", "disable"]  # Enable/disable managed FortiSwitch routing offload | Default: disable
    switch_controller_offload_ip: str  # IP for routing offload on FortiSwitch. | Default: 0.0.0.0
    switch_controller_offload_gw: Literal["enable", "disable"]  # Enable/disable managed FortiSwitch routing offload | Default: disable
    swc_vlan: int  # Creation status for switch-controller VLANs. | Default: 0 | Min: 0 | Max: 4294967295
    swc_first_create: int  # Initial create for switch-controller VLANs. | Default: 0 | Min: 0 | Max: 4294967295
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    tagging: list[dict[str, Any]]  # Config object tagging.
    eap_supplicant: Literal["enable", "disable"]  # Enable/disable EAP-Supplicant. | Default: disable
    eap_method: Literal["tls", "peap"]  # EAP method.
    eap_identity: str  # EAP identity. | MaxLen: 35
    eap_password: str  # EAP password. | MaxLen: 128
    eap_ca_cert: str  # EAP CA certificate name. | MaxLen: 79
    eap_user_cert: str  # EAP user certificate name. | MaxLen: 35
    default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # default purdue level of device detected on this in | Default: 3
    ipv6: str  # IPv6 of interface.
    physical: str  # Print physical interface information.

# Nested TypedDicts for table field children (dict mode)

class InterfaceClientoptionsItem(TypedDict):
    """Type hints for client-options table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    code: int  # DHCP client option code. | Default: 0 | Min: 0 | Max: 255
    type: Literal["hex", "string", "ip", "fqdn"]  # DHCP client option type. | Default: hex
    value: str  # DHCP client option value. | MaxLen: 312
    ip: str  # DHCP option IPs.


class InterfaceFailalertinterfacesItem(TypedDict):
    """Type hints for fail-alert-interfaces table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Names of the non-virtual interface. | MaxLen: 15


class InterfaceMemberItem(TypedDict):
    """Type hints for member table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    interface_name: str  # Physical interface name. | MaxLen: 79


class InterfaceSecuritygroupsItem(TypedDict):
    """Type hints for security-groups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Names of user groups that can authenticate with th | MaxLen: 79


class InterfaceVrrpItem(TypedDict):
    """Type hints for vrrp table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vrid: int  # Virtual router identifier (1 - 255). | Default: 0 | Min: 1 | Max: 255
    version: Literal["2", "3"]  # VRRP version. | Default: 2
    vrgrp: int  # VRRP group ID (1 - 65535). | Default: 0 | Min: 1 | Max: 65535
    vrip: str  # IP address of the virtual router. | Default: 0.0.0.0
    priority: int  # Priority of the virtual router (1 - 255). | Default: 100 | Min: 1 | Max: 255
    adv_interval: int  # Advertisement interval (250 - 255000 milliseconds) | Default: 1000 | Min: 250 | Max: 255000
    start_time: int  # Startup time (1 - 255 seconds). | Default: 3 | Min: 1 | Max: 255
    preempt: Literal["enable", "disable"]  # Enable/disable preempt mode. | Default: enable
    accept_mode: Literal["enable", "disable"]  # Enable/disable accept mode. | Default: enable
    vrdst: str  # Monitor the route to this destination.
    vrdst_priority: int  # Priority of the virtual router when the virtual ro | Default: 0 | Min: 0 | Max: 254
    ignore_default_route: Literal["enable", "disable"]  # Enable/disable ignoring of default route when chec | Default: disable
    status: Literal["enable", "disable"]  # Enable/disable this VRRP configuration. | Default: enable
    proxy_arp: str  # VRRP Proxy ARP configuration.


class InterfaceSecondaryipItem(TypedDict):
    """Type hints for secondaryip table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    ip: str  # Secondary IP address of the interface. | Default: 0.0.0.0 0.0.0.0
    secip_relay_ip: str  # DHCP relay IP address.
    allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"]  # Management access settings for the secondary IP ad
    gwdetect: Literal["enable", "disable"]  # Enable/disable detect gateway alive for first. | Default: disable
    ping_serv_status: int  # PING server status. | Default: 0 | Min: 0 | Max: 255
    detectserver: str  # Gateway's ping server for this IP.
    detectprotocol: Literal["ping", "tcp-echo", "udp-echo"]  # Protocols used to detect the server. | Default: ping
    ha_priority: int  # HA election priority for the PING server. | Default: 1 | Min: 1 | Max: 50


class InterfaceDhcpsnoopingserverlistItem(TypedDict):
    """Type hints for dhcp-snooping-server-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # DHCP server name. | Default: default | MaxLen: 35
    server_ip: str  # IP address for DHCP server. | Default: 0.0.0.0


class InterfaceTaggingItem(TypedDict):
    """Type hints for tagging table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Tagging entry name. | MaxLen: 63
    category: str  # Tag category. | MaxLen: 63
    tags: str  # Tags.


# Nested classes for table field children (object mode)

@final
class InterfaceClientoptionsObject:
    """Typed object for client-options table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # DHCP client option code. | Default: 0 | Min: 0 | Max: 255
    code: int
    # DHCP client option type. | Default: hex
    type: Literal["hex", "string", "ip", "fqdn"]
    # DHCP client option value. | MaxLen: 312
    value: str
    # DHCP option IPs.
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
class InterfaceFailalertinterfacesObject:
    """Typed object for fail-alert-interfaces table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Names of the non-virtual interface. | MaxLen: 15
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
class InterfaceMemberObject:
    """Typed object for member table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Physical interface name. | MaxLen: 79
    interface_name: str
    
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
class InterfaceSecuritygroupsObject:
    """Typed object for security-groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Names of user groups that can authenticate with the captive | MaxLen: 79
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
class InterfaceVrrpObject:
    """Typed object for vrrp table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Virtual router identifier (1 - 255). | Default: 0 | Min: 1 | Max: 255
    vrid: int
    # VRRP version. | Default: 2
    version: Literal["2", "3"]
    # VRRP group ID (1 - 65535). | Default: 0 | Min: 1 | Max: 65535
    vrgrp: int
    # IP address of the virtual router. | Default: 0.0.0.0
    vrip: str
    # Priority of the virtual router (1 - 255). | Default: 100 | Min: 1 | Max: 255
    priority: int
    # Advertisement interval (250 - 255000 milliseconds). | Default: 1000 | Min: 250 | Max: 255000
    adv_interval: int
    # Startup time (1 - 255 seconds). | Default: 3 | Min: 1 | Max: 255
    start_time: int
    # Enable/disable preempt mode. | Default: enable
    preempt: Literal["enable", "disable"]
    # Enable/disable accept mode. | Default: enable
    accept_mode: Literal["enable", "disable"]
    # Monitor the route to this destination.
    vrdst: str
    # Priority of the virtual router when the virtual router desti | Default: 0 | Min: 0 | Max: 254
    vrdst_priority: int
    # Enable/disable ignoring of default route when checking desti | Default: disable
    ignore_default_route: Literal["enable", "disable"]
    # Enable/disable this VRRP configuration. | Default: enable
    status: Literal["enable", "disable"]
    # VRRP Proxy ARP configuration.
    proxy_arp: str
    
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
class InterfaceSecondaryipObject:
    """Typed object for secondaryip table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Secondary IP address of the interface. | Default: 0.0.0.0 0.0.0.0
    ip: str
    # DHCP relay IP address.
    secip_relay_ip: str
    # Management access settings for the secondary IP address.
    allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"]
    # Enable/disable detect gateway alive for first. | Default: disable
    gwdetect: Literal["enable", "disable"]
    # PING server status. | Default: 0 | Min: 0 | Max: 255
    ping_serv_status: int
    # Gateway's ping server for this IP.
    detectserver: str
    # Protocols used to detect the server. | Default: ping
    detectprotocol: Literal["ping", "tcp-echo", "udp-echo"]
    # HA election priority for the PING server. | Default: 1 | Min: 1 | Max: 50
    ha_priority: int
    
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
class InterfaceDhcpsnoopingserverlistObject:
    """Typed object for dhcp-snooping-server-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DHCP server name. | Default: default | MaxLen: 35
    name: str
    # IP address for DHCP server. | Default: 0.0.0.0
    server_ip: str
    
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
class InterfaceTaggingObject:
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
class InterfaceResponse(TypedDict):
    """
    Type hints for system/interface API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 15
    vdom: str  # Interface is in this virtual domain (VDOM). | MaxLen: 31
    vrf: int  # Virtual Routing Forwarding ID. | Default: 0 | Min: 0 | Max: 511
    cli_conn_status: int  # CLI connection status. | Default: 0 | Min: 0 | Max: 4294967295
    fortilink: Literal["enable", "disable"]  # Enable FortiLink to dedicate this interface to man | Default: disable
    switch_controller_source_ip: Literal["outbound", "fixed"]  # Source IP address used in FortiLink over L3 connec | Default: outbound
    mode: Literal["static", "dhcp", "pppoe"]  # Addressing mode (static, DHCP, PPPoE). | Default: static
    client_options: list[InterfaceClientoptionsItem]  # DHCP client options.
    distance: int  # Distance for routes learned through PPPoE or DHCP, | Default: 5 | Min: 1 | Max: 255
    priority: int  # Priority of learned routes. | Default: 1 | Min: 1 | Max: 65535
    dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    dhcp_relay_interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    dhcp_relay_vrf_select: int  # VRF ID used for connection to server. | Default: -1 | Min: 0 | Max: 511
    dhcp_broadcast_flag: Literal["disable", "enable"]  # Enable/disable setting of the broadcast flag in me | Default: enable
    dhcp_relay_service: Literal["disable", "enable"]  # Enable/disable allowing this interface to act as a | Default: disable
    dhcp_relay_ip: list[dict[str, Any]]  # DHCP relay IP address.
    dhcp_relay_source_ip: str  # IP address used by the DHCP relay as its source IP | Default: 0.0.0.0
    dhcp_relay_circuit_id: str  # DHCP relay circuit ID. | MaxLen: 64
    dhcp_relay_link_selection: str  # DHCP relay link selection. | Default: 0.0.0.0
    dhcp_relay_request_all_server: Literal["disable", "enable"]  # Enable/disable sending of DHCP requests to all ser | Default: disable
    dhcp_relay_allow_no_end_option: Literal["disable", "enable"]  # Enable/disable relaying DHCP messages with no end | Default: disable
    dhcp_relay_type: Literal["regular", "ipsec"]  # DHCP relay type (regular or IPsec). | Default: regular
    dhcp_smart_relay: Literal["disable", "enable"]  # Enable/disable DHCP smart relay. | Default: disable
    dhcp_relay_agent_option: Literal["enable", "disable"]  # Enable/disable DHCP relay agent option. | Default: enable
    dhcp_classless_route_addition: Literal["enable", "disable"]  # Enable/disable addition of classless static routes | Default: enable
    management_ip: str  # High Availability in-band management IP address of | Default: 0.0.0.0 0.0.0.0
    ip: str  # Interface IPv4 address and subnet mask, syntax: X. | Default: 0.0.0.0 0.0.0.0
    allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"]  # Permitted types of management access to this inter
    gwdetect: Literal["enable", "disable"]  # Enable/disable detect gateway alive for first. | Default: disable
    ping_serv_status: int  # PING server status. | Default: 0 | Min: 0 | Max: 255
    detectserver: str  # Gateway's ping server for this IP.
    detectprotocol: Literal["ping", "tcp-echo", "udp-echo"]  # Protocols used to detect the server. | Default: ping
    ha_priority: int  # HA election priority for the PING server. | Default: 1 | Min: 1 | Max: 50
    fail_detect: Literal["enable", "disable"]  # Enable/disable fail detection features for this in | Default: disable
    fail_detect_option: Literal["detectserver", "link-down"]  # Options for detecting that this interface has fail | Default: link-down
    fail_alert_method: Literal["link-failed-signal", "link-down"]  # Select link-failed-signal or link-down method to a | Default: link-down
    fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"]  # Action on FortiExtender when interface fail. | Default: soft-restart
    fail_alert_interfaces: list[InterfaceFailalertinterfacesItem]  # Names of the FortiGate interfaces to which the lin
    dhcp_client_identifier: str  # DHCP client identifier. | MaxLen: 48
    dhcp_renew_time: int  # DHCP renew time in seconds (300-604800), 0 means u | Default: 0 | Min: 300 | Max: 604800
    ipunnumbered: str  # Unnumbered IP used for PPPoE interfaces for which | Default: 0.0.0.0
    username: str  # Username of the PPPoE account, provided by your IS | MaxLen: 64
    pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"]  # CoS in VLAN tag for outgoing PPPoE/PPP packets. | Default: cos0
    pppoe_unnumbered_negotiate: Literal["enable", "disable"]  # Enable/disable PPPoE unnumbered negotiation. | Default: enable
    password: str  # PPPoE account's password. | MaxLen: 128
    idle_timeout: int  # PPPoE auto disconnect after idle timeout seconds, | Default: 0 | Min: 0 | Max: 32767
    multilink: Literal["enable", "disable"]  # Enable/disable PPP multilink support. | Default: disable
    mrru: int  # PPP MRRU (296 - 65535, default = 1500). | Default: 1500 | Min: 296 | Max: 65535
    detected_peer_mtu: int  # MTU of detected peer (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    disc_retry_timeout: int  # Time in seconds to wait before retrying to start a | Default: 1 | Min: 0 | Max: 4294967295
    padt_retry_timeout: int  # PPPoE Active Discovery Terminate (PADT) used to te | Default: 1 | Min: 0 | Max: 4294967295
    service_name: str  # PPPoE service name. | MaxLen: 63
    ac_name: str  # PPPoE server name. | MaxLen: 63
    lcp_echo_interval: int  # Time in seconds between PPPoE Link Control Protoco | Default: 5 | Min: 0 | Max: 32767
    lcp_max_echo_fails: int  # Maximum missed LCP echo messages before disconnect | Default: 3 | Min: 0 | Max: 32767
    defaultgw: Literal["enable", "disable"]  # Enable to get the gateway IP from the DHCP or PPPo | Default: enable
    dns_server_override: Literal["enable", "disable"]  # Enable/disable use DNS acquired by DHCP or PPPoE. | Default: enable
    dns_server_protocol: Literal["cleartext", "dot", "doh"]  # DNS transport protocols. | Default: cleartext
    auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]  # PPP authentication type to use. | Default: auto
    pptp_client: Literal["enable", "disable"]  # Enable/disable PPTP client. | Default: disable
    pptp_user: str  # PPTP user name. | MaxLen: 64
    pptp_password: str  # PPTP password. | MaxLen: 128
    pptp_server_ip: str  # PPTP server IP address. | Default: 0.0.0.0
    pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]  # PPTP authentication type. | Default: auto
    pptp_timeout: int  # Idle timer in minutes (0 for disabled). | Default: 0 | Min: 0 | Max: 65535
    arpforward: Literal["enable", "disable"]  # Enable/disable ARP forwarding. | Default: enable
    ndiscforward: Literal["enable", "disable"]  # Enable/disable NDISC forwarding. | Default: enable
    broadcast_forward: Literal["enable", "disable"]  # Enable/disable broadcast forwarding. | Default: disable
    bfd: Literal["global", "enable", "disable"]  # Bidirectional Forwarding Detection (BFD) settings. | Default: global
    bfd_desired_min_tx: int  # BFD desired minimal transmit interval. | Default: 250 | Min: 1 | Max: 100000
    bfd_detect_mult: int  # BFD detection multiplier. | Default: 3 | Min: 1 | Max: 50
    bfd_required_min_rx: int  # BFD required minimal receive interval. | Default: 250 | Min: 1 | Max: 100000
    l2forward: Literal["enable", "disable"]  # Enable/disable l2 forwarding. | Default: disable
    icmp_send_redirect: Literal["enable", "disable"]  # Enable/disable sending of ICMP redirects. | Default: enable
    icmp_accept_redirect: Literal["enable", "disable"]  # Enable/disable ICMP accept redirect. | Default: enable
    reachable_time: int  # IPv4 reachable time in milliseconds | Default: 30000 | Min: 30000 | Max: 3600000
    vlanforward: Literal["enable", "disable"]  # Enable/disable traffic forwarding between VLANs on | Default: disable
    stpforward: Literal["enable", "disable"]  # Enable/disable STP forwarding. | Default: disable
    stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"]  # Configure STP forwarding mode. | Default: rpl-all-ext-id
    ips_sniffer_mode: Literal["enable", "disable"]  # Enable/disable the use of this interface as a one- | Default: disable
    ident_accept: Literal["enable", "disable"]  # Enable/disable authentication for this interface. | Default: disable
    ipmac: Literal["enable", "disable"]  # Enable/disable IP/MAC binding. | Default: disable
    subst: Literal["enable", "disable"]  # Enable to always send packets from this interface | Default: disable
    macaddr: str  # Change the interface's MAC address. | Default: 00:00:00:00:00:00
    virtual_mac: str  # Change the interface's virtual MAC address. | Default: 00:00:00:00:00:00
    substitute_dst_mac: str  # Destination MAC address that all packets are sent | Default: 00:00:00:00:00:00
    speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"]  # Interface speed. The default setting and the optio | Default: auto
    status: Literal["up", "down"]  # Bring the interface up or shut the interface down. | Default: up
    netbios_forward: Literal["disable", "enable"]  # Enable/disable NETBIOS forwarding. | Default: disable
    wins_ip: str  # WINS server IP. | Default: 0.0.0.0
    type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"]  # Interface type. | Default: vlan
    dedicated_to: Literal["none", "management"]  # Configure interface for single purpose. | Default: none
    trust_ip_1: str  # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip_2: str  # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip_3: str  # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip6_1: str  # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    trust_ip6_2: str  # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    trust_ip6_3: str  # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    ring_rx: int  # RX ring size. | Default: 0 | Min: 0 | Max: 4294967295
    ring_tx: int  # TX ring size. | Default: 0 | Min: 0 | Max: 4294967295
    wccp: Literal["enable", "disable"]  # Enable/disable WCCP on this interface. Used for en | Default: disable
    netflow_sampler: Literal["disable", "tx", "rx", "both"]  # Enable/disable NetFlow on this interface and set t | Default: disable
    netflow_sample_rate: int  # NetFlow sample rate.  Sample one packet every conf | Default: 1 | Min: 1 | Max: 65535
    netflow_sampler_id: int  # Netflow sampler ID. | Default: 0 | Min: 1 | Max: 254
    sflow_sampler: Literal["enable", "disable"]  # Enable/disable sFlow on this interface. | Default: disable
    drop_fragment: Literal["enable", "disable"]  # Enable/disable drop fragment packets. | Default: disable
    src_check: Literal["enable", "disable"]  # Enable/disable source IP check. | Default: enable
    sample_rate: int  # sFlow sample rate (10 - 99999). | Default: 2000 | Min: 10 | Max: 99999
    polling_interval: int  # sFlow polling interval in seconds (1 - 255). | Default: 20 | Min: 1 | Max: 255
    sample_direction: Literal["tx", "rx", "both"]  # Data that NetFlow collects (rx, tx, or both). | Default: both
    explicit_web_proxy: Literal["enable", "disable"]  # Enable/disable the explicit web proxy on this inte | Default: disable
    explicit_ftp_proxy: Literal["enable", "disable"]  # Enable/disable the explicit FTP proxy on this inte | Default: disable
    proxy_captive_portal: Literal["enable", "disable"]  # Enable/disable proxy captive portal on this interf | Default: disable
    tcp_mss: int  # TCP maximum segment size. 0 means do not change se | Default: 0 | Min: 48 | Max: 65535
    inbandwidth: int  # Bandwidth limit for incoming traffic | Default: 0 | Min: 0 | Max: 80000000
    outbandwidth: int  # Bandwidth limit for outgoing traffic | Default: 0 | Min: 0 | Max: 80000000
    egress_shaping_profile: str  # Outgoing traffic shaping profile. | MaxLen: 35
    ingress_shaping_profile: str  # Incoming traffic shaping profile. | MaxLen: 35
    spillover_threshold: int  # Egress Spillover threshold (0 - 16776000 kbps), 0 | Default: 0 | Min: 0 | Max: 16776000
    ingress_spillover_threshold: int  # Ingress Spillover threshold (0 - 16776000 kbps), 0 | Default: 0 | Min: 0 | Max: 16776000
    weight: int  # Default weight for static routes | Default: 0 | Min: 0 | Max: 255
    interface: str  # Interface name. | MaxLen: 15
    external: Literal["enable", "disable"]  # Enable/disable identifying the interface as an ext | Default: disable
    mtu_override: Literal["enable", "disable"]  # Enable to set a custom MTU for this interface. | Default: disable
    mtu: int  # MTU value for this interface. | Default: 1500 | Min: 0 | Max: 4294967295
    vlan_protocol: Literal["8021q", "8021ad"]  # Ethernet protocol of VLAN. | Default: 8021q
    vlanid: int  # VLAN ID (1 - 4094). | Default: 0 | Min: 1 | Max: 4094
    forward_domain: int  # Transparent mode forward domain. | Default: 0 | Min: 0 | Max: 2147483647
    remote_ip: str  # Remote IP address of tunnel. | Default: 0.0.0.0 0.0.0.0
    member: list[InterfaceMemberItem]  # Physical interfaces that belong to the aggregate o
    lacp_mode: Literal["static", "passive", "active"]  # LACP mode. | Default: active
    lacp_ha_secondary: Literal["enable", "disable"]  # LACP HA secondary member. | Default: enable
    system_id_type: Literal["auto", "user"]  # Method in which system ID is generated. | Default: auto
    system_id: str  # Define a system ID for the aggregate interface. | Default: 00:00:00:00:00:00
    lacp_speed: Literal["slow", "fast"]  # How often the interface sends LACP messages. | Default: slow
    min_links: int  # Minimum number of aggregated ports that must be up | Default: 1 | Min: 1 | Max: 32
    min_links_down: Literal["operational", "administrative"]  # Action to take when less than the configured minim | Default: operational
    algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"]  # Frame distribution algorithm. | Default: L4
    link_up_delay: int  # Number of milliseconds to wait before considering | Default: 50 | Min: 50 | Max: 3600000
    aggregate_type: Literal["physical", "vxlan"]  # Type of aggregation. | Default: physical
    priority_override: Literal["enable", "disable"]  # Enable/disable fail back to higher priority port o | Default: enable
    aggregate: str  # Aggregate interface. | MaxLen: 15
    redundant_interface: str  # Redundant interface. | MaxLen: 15
    devindex: int  # Device Index. | Default: 0 | Min: 0 | Max: 4294967295
    vindex: int  # Switch control interface VLAN ID. | Default: 0 | Min: 0 | Max: 65535
    switch: str  # Contained in switch. | MaxLen: 15
    description: str  # Description. | MaxLen: 255
    alias: str  # Alias will be displayed with the interface name to | MaxLen: 25
    security_mode: Literal["none", "captive-portal", "802.1X"]  # Turn on captive portal authentication for this int | Default: none
    security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"]  # Enable/disable MAC authentication bypass. | Default: disable
    security_ip_auth_bypass: Literal["enable", "disable"]  # Enable/disable IP authentication bypass. | Default: disable
    security_external_web: str  # URL of external authentication web server. | MaxLen: 1023
    security_external_logout: str  # URL of external authentication logout server. | MaxLen: 127
    replacemsg_override_group: str  # Replacement message override group. | MaxLen: 35
    security_redirect_url: str  # URL redirection after disclaimer/authentication. | MaxLen: 1023
    auth_cert: str  # HTTPS server certificate. | MaxLen: 35
    auth_portal_addr: str  # Address of captive portal. | MaxLen: 63
    security_exempt_list: str  # Name of security-exempt-list. | MaxLen: 35
    security_groups: list[InterfaceSecuritygroupsItem]  # User groups that can authenticate with the captive
    ike_saml_server: str  # Configure IKE authentication SAML server. | MaxLen: 35
    device_identification: Literal["enable", "disable"]  # Enable/disable passively gathering of device ident | Default: disable
    exclude_signatures: Literal["iot", "ot"]  # Exclude IOT or OT application signatures.
    device_user_identification: Literal["enable", "disable"]  # Enable/disable passive gathering of user identity | Default: enable
    lldp_reception: Literal["enable", "disable", "vdom"]  # Enable/disable Link Layer Discovery Protocol | Default: vdom
    lldp_transmission: Literal["enable", "disable", "vdom"]  # Enable/disable Link Layer Discovery Protocol | Default: vdom
    lldp_network_policy: str  # LLDP-MED network policy profile. | MaxLen: 35
    estimated_upstream_bandwidth: int  # Estimated maximum upstream bandwidth (kbps). Used | Default: 0 | Min: 0 | Max: 4294967295
    estimated_downstream_bandwidth: int  # Estimated maximum downstream bandwidth (kbps). Use | Default: 0 | Min: 0 | Max: 4294967295
    measured_upstream_bandwidth: int  # Measured upstream bandwidth (kbps). | Default: 0 | Min: 0 | Max: 4294967295
    measured_downstream_bandwidth: int  # Measured downstream bandwidth (kbps). | Default: 0 | Min: 0 | Max: 4294967295
    bandwidth_measure_time: int  # Bandwidth measure time. | Default: 0 | Min: 0 | Max: 4294967295
    monitor_bandwidth: Literal["enable", "disable"]  # Enable monitoring bandwidth on this interface. | Default: disable
    vrrp_virtual_mac: Literal["enable", "disable"]  # Enable/disable use of virtual MAC for VRRP. | Default: disable
    vrrp: list[InterfaceVrrpItem]  # VRRP configuration.
    phy_setting: str  # PHY settings
    role: Literal["lan", "wan", "dmz", "undefined"]  # Interface role. | Default: undefined
    snmp_index: int  # Permanent SNMP Index of the interface. | Default: 0 | Min: 0 | Max: 2147483647
    secondary_IP: Literal["enable", "disable"]  # Enable/disable adding a secondary IP to this inter | Default: disable
    secondaryip: list[InterfaceSecondaryipItem]  # Second IP address of interface.
    preserve_session_route: Literal["enable", "disable"]  # Enable/disable preservation of session route when | Default: disable
    auto_auth_extension_device: Literal["enable", "disable"]  # Enable/disable automatic authorization of dedicate | Default: disable
    ap_discover: Literal["enable", "disable"]  # Enable/disable automatic registration of unknown F | Default: enable
    fortilink_neighbor_detect: Literal["lldp", "fortilink"]  # Protocol for FortiGate neighbor discovery. | Default: lldp
    ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"]  # Enable/disable automatic IP address assignment of | Default: inherit-global
    managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"]  # Number of IP addresses to be allocated by FortiIPA | Default: 256
    fortilink_split_interface: Literal["enable", "disable"]  # Enable/disable FortiLink split interface to connec | Default: enable
    internal: int  # Implicitly created. | Default: 0 | Min: 0 | Max: 255
    fortilink_backup_link: int  # FortiLink split interface backup link. | Default: 0 | Min: 0 | Max: 255
    switch_controller_access_vlan: Literal["enable", "disable"]  # Block FortiSwitch port-to-port traffic. | Default: disable
    switch_controller_traffic_policy: str  # Switch controller traffic policy for the VLAN. | MaxLen: 63
    switch_controller_rspan_mode: Literal["disable", "enable"]  # Stop Layer2 MAC learning and interception of BPDUs | Default: disable
    switch_controller_netflow_collect: Literal["disable", "enable"]  # NetFlow collection and processing. | Default: disable
    switch_controller_mgmt_vlan: int  # VLAN to use for FortiLink management purposes. | Default: 4094 | Min: 1 | Max: 4094
    switch_controller_igmp_snooping: Literal["enable", "disable"]  # Switch controller IGMP snooping. | Default: disable
    switch_controller_igmp_snooping_proxy: Literal["enable", "disable"]  # Switch controller IGMP snooping proxy. | Default: disable
    switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"]  # Switch controller IGMP snooping fast-leave. | Default: disable
    switch_controller_dhcp_snooping: Literal["enable", "disable"]  # Switch controller DHCP snooping. | Default: disable
    switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"]  # Switch controller DHCP snooping verify MAC. | Default: disable
    switch_controller_dhcp_snooping_option82: Literal["enable", "disable"]  # Switch controller DHCP snooping option82. | Default: disable
    dhcp_snooping_server_list: list[InterfaceDhcpsnoopingserverlistItem]  # Configure DHCP server access list.
    switch_controller_arp_inspection: Literal["enable", "disable", "monitor"]  # Enable/disable/Monitor FortiSwitch ARP inspection. | Default: disable
    switch_controller_learning_limit: int  # Limit the number of dynamic MAC addresses on this | Default: 0 | Min: 0 | Max: 128
    switch_controller_nac: str  # Integrated FortiLink settings for managed FortiSwi | MaxLen: 35
    switch_controller_dynamic: str  # Integrated FortiLink settings for managed FortiSwi | MaxLen: 35
    switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"]  # Interface's purpose when assigning traffic | Default: none
    switch_controller_iot_scanning: Literal["enable", "disable"]  # Enable/disable managed FortiSwitch IoT scanning. | Default: disable
    switch_controller_offload: Literal["enable", "disable"]  # Enable/disable managed FortiSwitch routing offload | Default: disable
    switch_controller_offload_ip: str  # IP for routing offload on FortiSwitch. | Default: 0.0.0.0
    switch_controller_offload_gw: Literal["enable", "disable"]  # Enable/disable managed FortiSwitch routing offload | Default: disable
    swc_vlan: int  # Creation status for switch-controller VLANs. | Default: 0 | Min: 0 | Max: 4294967295
    swc_first_create: int  # Initial create for switch-controller VLANs. | Default: 0 | Min: 0 | Max: 4294967295
    color: int  # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    tagging: list[InterfaceTaggingItem]  # Config object tagging.
    eap_supplicant: Literal["enable", "disable"]  # Enable/disable EAP-Supplicant. | Default: disable
    eap_method: Literal["tls", "peap"]  # EAP method.
    eap_identity: str  # EAP identity. | MaxLen: 35
    eap_password: str  # EAP password. | MaxLen: 128
    eap_ca_cert: str  # EAP CA certificate name. | MaxLen: 79
    eap_user_cert: str  # EAP user certificate name. | MaxLen: 35
    default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]  # default purdue level of device detected on this in | Default: 3
    ipv6: str  # IPv6 of interface.
    physical: str  # Print physical interface information.


@final
class InterfaceObject:
    """Typed FortiObject for system/interface with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 15
    name: str
    # Interface is in this virtual domain (VDOM). | MaxLen: 31
    vdom: str
    # Virtual Routing Forwarding ID. | Default: 0 | Min: 0 | Max: 511
    vrf: int
    # CLI connection status. | Default: 0 | Min: 0 | Max: 4294967295
    cli_conn_status: int
    # Enable FortiLink to dedicate this interface to manage other | Default: disable
    fortilink: Literal["enable", "disable"]
    # Source IP address used in FortiLink over L3 connections. | Default: outbound
    switch_controller_source_ip: Literal["outbound", "fixed"]
    # Addressing mode (static, DHCP, PPPoE). | Default: static
    mode: Literal["static", "dhcp", "pppoe"]
    # DHCP client options.
    client_options: list[InterfaceClientoptionsObject]
    # Distance for routes learned through PPPoE or DHCP, lower dis | Default: 5 | Min: 1 | Max: 255
    distance: int
    # Priority of learned routes. | Default: 1 | Min: 1 | Max: 65535
    priority: int
    # Specify how to select outgoing interface to reach server. | Default: auto
    dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    dhcp_relay_interface: str
    # VRF ID used for connection to server. | Default: -1 | Min: 0 | Max: 511
    dhcp_relay_vrf_select: int
    # Enable/disable setting of the broadcast flag in messages sen | Default: enable
    dhcp_broadcast_flag: Literal["disable", "enable"]
    # Enable/disable allowing this interface to act as a DHCP rela | Default: disable
    dhcp_relay_service: Literal["disable", "enable"]
    # DHCP relay IP address.
    dhcp_relay_ip: list[dict[str, Any]]
    # IP address used by the DHCP relay as its source IP. | Default: 0.0.0.0
    dhcp_relay_source_ip: str
    # DHCP relay circuit ID. | MaxLen: 64
    dhcp_relay_circuit_id: str
    # DHCP relay link selection. | Default: 0.0.0.0
    dhcp_relay_link_selection: str
    # Enable/disable sending of DHCP requests to all servers. | Default: disable
    dhcp_relay_request_all_server: Literal["disable", "enable"]
    # Enable/disable relaying DHCP messages with no end option. | Default: disable
    dhcp_relay_allow_no_end_option: Literal["disable", "enable"]
    # DHCP relay type (regular or IPsec). | Default: regular
    dhcp_relay_type: Literal["regular", "ipsec"]
    # Enable/disable DHCP smart relay. | Default: disable
    dhcp_smart_relay: Literal["disable", "enable"]
    # Enable/disable DHCP relay agent option. | Default: enable
    dhcp_relay_agent_option: Literal["enable", "disable"]
    # Enable/disable addition of classless static routes retrieved | Default: enable
    dhcp_classless_route_addition: Literal["enable", "disable"]
    # High Availability in-band management IP address of this inte | Default: 0.0.0.0 0.0.0.0
    management_ip: str
    # Interface IPv4 address and subnet mask, syntax: X.X.X.X/24. | Default: 0.0.0.0 0.0.0.0
    ip: str
    # Permitted types of management access to this interface.
    allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"]
    # Enable/disable detect gateway alive for first. | Default: disable
    gwdetect: Literal["enable", "disable"]
    # PING server status. | Default: 0 | Min: 0 | Max: 255
    ping_serv_status: int
    # Gateway's ping server for this IP.
    detectserver: str
    # Protocols used to detect the server. | Default: ping
    detectprotocol: Literal["ping", "tcp-echo", "udp-echo"]
    # HA election priority for the PING server. | Default: 1 | Min: 1 | Max: 50
    ha_priority: int
    # Enable/disable fail detection features for this interface. | Default: disable
    fail_detect: Literal["enable", "disable"]
    # Options for detecting that this interface has failed. | Default: link-down
    fail_detect_option: Literal["detectserver", "link-down"]
    # Select link-failed-signal or link-down method to alert about | Default: link-down
    fail_alert_method: Literal["link-failed-signal", "link-down"]
    # Action on FortiExtender when interface fail. | Default: soft-restart
    fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"]
    # Names of the FortiGate interfaces to which the link failure
    fail_alert_interfaces: list[InterfaceFailalertinterfacesObject]
    # DHCP client identifier. | MaxLen: 48
    dhcp_client_identifier: str
    # DHCP renew time in seconds (300-604800), 0 means use the ren | Default: 0 | Min: 300 | Max: 604800
    dhcp_renew_time: int
    # Unnumbered IP used for PPPoE interfaces for which no unique | Default: 0.0.0.0
    ipunnumbered: str
    # Username of the PPPoE account, provided by your ISP. | MaxLen: 64
    username: str
    # CoS in VLAN tag for outgoing PPPoE/PPP packets. | Default: cos0
    pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"]
    # Enable/disable PPPoE unnumbered negotiation. | Default: enable
    pppoe_unnumbered_negotiate: Literal["enable", "disable"]
    # PPPoE account's password. | MaxLen: 128
    password: str
    # PPPoE auto disconnect after idle timeout seconds, 0 means no | Default: 0 | Min: 0 | Max: 32767
    idle_timeout: int
    # Enable/disable PPP multilink support. | Default: disable
    multilink: Literal["enable", "disable"]
    # PPP MRRU (296 - 65535, default = 1500). | Default: 1500 | Min: 296 | Max: 65535
    mrru: int
    # MTU of detected peer (0 - 4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    detected_peer_mtu: int
    # Time in seconds to wait before retrying to start a PPPoE dis | Default: 1 | Min: 0 | Max: 4294967295
    disc_retry_timeout: int
    # PPPoE Active Discovery Terminate (PADT) used to terminate se | Default: 1 | Min: 0 | Max: 4294967295
    padt_retry_timeout: int
    # PPPoE service name. | MaxLen: 63
    service_name: str
    # PPPoE server name. | MaxLen: 63
    ac_name: str
    # Time in seconds between PPPoE Link Control Protocol (LCP) ec | Default: 5 | Min: 0 | Max: 32767
    lcp_echo_interval: int
    # Maximum missed LCP echo messages before disconnect. | Default: 3 | Min: 0 | Max: 32767
    lcp_max_echo_fails: int
    # Enable to get the gateway IP from the DHCP or PPPoE server. | Default: enable
    defaultgw: Literal["enable", "disable"]
    # Enable/disable use DNS acquired by DHCP or PPPoE. | Default: enable
    dns_server_override: Literal["enable", "disable"]
    # DNS transport protocols. | Default: cleartext
    dns_server_protocol: Literal["cleartext", "dot", "doh"]
    # PPP authentication type to use. | Default: auto
    auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]
    # Enable/disable PPTP client. | Default: disable
    pptp_client: Literal["enable", "disable"]
    # PPTP user name. | MaxLen: 64
    pptp_user: str
    # PPTP password. | MaxLen: 128
    pptp_password: str
    # PPTP server IP address. | Default: 0.0.0.0
    pptp_server_ip: str
    # PPTP authentication type. | Default: auto
    pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"]
    # Idle timer in minutes (0 for disabled). | Default: 0 | Min: 0 | Max: 65535
    pptp_timeout: int
    # Enable/disable ARP forwarding. | Default: enable
    arpforward: Literal["enable", "disable"]
    # Enable/disable NDISC forwarding. | Default: enable
    ndiscforward: Literal["enable", "disable"]
    # Enable/disable broadcast forwarding. | Default: disable
    broadcast_forward: Literal["enable", "disable"]
    # Bidirectional Forwarding Detection (BFD) settings. | Default: global
    bfd: Literal["global", "enable", "disable"]
    # BFD desired minimal transmit interval. | Default: 250 | Min: 1 | Max: 100000
    bfd_desired_min_tx: int
    # BFD detection multiplier. | Default: 3 | Min: 1 | Max: 50
    bfd_detect_mult: int
    # BFD required minimal receive interval. | Default: 250 | Min: 1 | Max: 100000
    bfd_required_min_rx: int
    # Enable/disable l2 forwarding. | Default: disable
    l2forward: Literal["enable", "disable"]
    # Enable/disable sending of ICMP redirects. | Default: enable
    icmp_send_redirect: Literal["enable", "disable"]
    # Enable/disable ICMP accept redirect. | Default: enable
    icmp_accept_redirect: Literal["enable", "disable"]
    # IPv4 reachable time in milliseconds | Default: 30000 | Min: 30000 | Max: 3600000
    reachable_time: int
    # Enable/disable traffic forwarding between VLANs on this inte | Default: disable
    vlanforward: Literal["enable", "disable"]
    # Enable/disable STP forwarding. | Default: disable
    stpforward: Literal["enable", "disable"]
    # Configure STP forwarding mode. | Default: rpl-all-ext-id
    stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"]
    # Enable/disable the use of this interface as a one-armed snif | Default: disable
    ips_sniffer_mode: Literal["enable", "disable"]
    # Enable/disable authentication for this interface. | Default: disable
    ident_accept: Literal["enable", "disable"]
    # Enable/disable IP/MAC binding. | Default: disable
    ipmac: Literal["enable", "disable"]
    # Enable to always send packets from this interface to a desti | Default: disable
    subst: Literal["enable", "disable"]
    # Change the interface's MAC address. | Default: 00:00:00:00:00:00
    macaddr: str
    # Change the interface's virtual MAC address. | Default: 00:00:00:00:00:00
    virtual_mac: str
    # Destination MAC address that all packets are sent to from th | Default: 00:00:00:00:00:00
    substitute_dst_mac: str
    # Interface speed. The default setting and the options availab | Default: auto
    speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"]
    # Bring the interface up or shut the interface down. | Default: up
    status: Literal["up", "down"]
    # Enable/disable NETBIOS forwarding. | Default: disable
    netbios_forward: Literal["disable", "enable"]
    # WINS server IP. | Default: 0.0.0.0
    wins_ip: str
    # Interface type. | Default: vlan
    type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"]
    # Configure interface for single purpose. | Default: none
    dedicated_to: Literal["none", "management"]
    # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip_1: str
    # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip_2: str
    # Trusted host for dedicated management traffic | Default: 0.0.0.0 0.0.0.0
    trust_ip_3: str
    # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    trust_ip6_1: str
    # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    trust_ip6_2: str
    # Trusted IPv6 host for dedicated management traffic | Default: ::/0
    trust_ip6_3: str
    # RX ring size. | Default: 0 | Min: 0 | Max: 4294967295
    ring_rx: int
    # TX ring size. | Default: 0 | Min: 0 | Max: 4294967295
    ring_tx: int
    # Enable/disable WCCP on this interface. Used for encapsulated | Default: disable
    wccp: Literal["enable", "disable"]
    # Enable/disable NetFlow on this interface and set the data th | Default: disable
    netflow_sampler: Literal["disable", "tx", "rx", "both"]
    # NetFlow sample rate.  Sample one packet every configured num | Default: 1 | Min: 1 | Max: 65535
    netflow_sample_rate: int
    # Netflow sampler ID. | Default: 0 | Min: 1 | Max: 254
    netflow_sampler_id: int
    # Enable/disable sFlow on this interface. | Default: disable
    sflow_sampler: Literal["enable", "disable"]
    # Enable/disable drop fragment packets. | Default: disable
    drop_fragment: Literal["enable", "disable"]
    # Enable/disable source IP check. | Default: enable
    src_check: Literal["enable", "disable"]
    # sFlow sample rate (10 - 99999). | Default: 2000 | Min: 10 | Max: 99999
    sample_rate: int
    # sFlow polling interval in seconds (1 - 255). | Default: 20 | Min: 1 | Max: 255
    polling_interval: int
    # Data that NetFlow collects (rx, tx, or both). | Default: both
    sample_direction: Literal["tx", "rx", "both"]
    # Enable/disable the explicit web proxy on this interface. | Default: disable
    explicit_web_proxy: Literal["enable", "disable"]
    # Enable/disable the explicit FTP proxy on this interface. | Default: disable
    explicit_ftp_proxy: Literal["enable", "disable"]
    # Enable/disable proxy captive portal on this interface. | Default: disable
    proxy_captive_portal: Literal["enable", "disable"]
    # TCP maximum segment size. 0 means do not change segment size | Default: 0 | Min: 48 | Max: 65535
    tcp_mss: int
    # Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 | Default: 0 | Min: 0 | Max: 80000000
    inbandwidth: int
    # Bandwidth limit for outgoing traffic (0 - 80000000 kbps). | Default: 0 | Min: 0 | Max: 80000000
    outbandwidth: int
    # Outgoing traffic shaping profile. | MaxLen: 35
    egress_shaping_profile: str
    # Incoming traffic shaping profile. | MaxLen: 35
    ingress_shaping_profile: str
    # Egress Spillover threshold (0 - 16776000 kbps), 0 means unli | Default: 0 | Min: 0 | Max: 16776000
    spillover_threshold: int
    # Ingress Spillover threshold (0 - 16776000 kbps), 0 means unl | Default: 0 | Min: 0 | Max: 16776000
    ingress_spillover_threshold: int
    # Default weight for static routes | Default: 0 | Min: 0 | Max: 255
    weight: int
    # Interface name. | MaxLen: 15
    interface: str
    # Enable/disable identifying the interface as an external inte | Default: disable
    external: Literal["enable", "disable"]
    # Enable to set a custom MTU for this interface. | Default: disable
    mtu_override: Literal["enable", "disable"]
    # MTU value for this interface. | Default: 1500 | Min: 0 | Max: 4294967295
    mtu: int
    # Ethernet protocol of VLAN. | Default: 8021q
    vlan_protocol: Literal["8021q", "8021ad"]
    # VLAN ID (1 - 4094). | Default: 0 | Min: 1 | Max: 4094
    vlanid: int
    # Transparent mode forward domain. | Default: 0 | Min: 0 | Max: 2147483647
    forward_domain: int
    # Remote IP address of tunnel. | Default: 0.0.0.0 0.0.0.0
    remote_ip: str
    # Physical interfaces that belong to the aggregate or redundan
    member: list[InterfaceMemberObject]
    # LACP mode. | Default: active
    lacp_mode: Literal["static", "passive", "active"]
    # LACP HA secondary member. | Default: enable
    lacp_ha_secondary: Literal["enable", "disable"]
    # Method in which system ID is generated. | Default: auto
    system_id_type: Literal["auto", "user"]
    # Define a system ID for the aggregate interface. | Default: 00:00:00:00:00:00
    system_id: str
    # How often the interface sends LACP messages. | Default: slow
    lacp_speed: Literal["slow", "fast"]
    # Minimum number of aggregated ports that must be up. | Default: 1 | Min: 1 | Max: 32
    min_links: int
    # Action to take when less than the configured minimum number | Default: operational
    min_links_down: Literal["operational", "administrative"]
    # Frame distribution algorithm. | Default: L4
    algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"]
    # Number of milliseconds to wait before considering a link is | Default: 50 | Min: 50 | Max: 3600000
    link_up_delay: int
    # Type of aggregation. | Default: physical
    aggregate_type: Literal["physical", "vxlan"]
    # Enable/disable fail back to higher priority port once recove | Default: enable
    priority_override: Literal["enable", "disable"]
    # Aggregate interface. | MaxLen: 15
    aggregate: str
    # Redundant interface. | MaxLen: 15
    redundant_interface: str
    # Device Index. | Default: 0 | Min: 0 | Max: 4294967295
    devindex: int
    # Switch control interface VLAN ID. | Default: 0 | Min: 0 | Max: 65535
    vindex: int
    # Contained in switch. | MaxLen: 15
    switch: str
    # Description. | MaxLen: 255
    description: str
    # Alias will be displayed with the interface name to make it e | MaxLen: 25
    alias: str
    # Turn on captive portal authentication for this interface. | Default: none
    security_mode: Literal["none", "captive-portal", "802.1X"]
    # Enable/disable MAC authentication bypass. | Default: disable
    security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"]
    # Enable/disable IP authentication bypass. | Default: disable
    security_ip_auth_bypass: Literal["enable", "disable"]
    # URL of external authentication web server. | MaxLen: 1023
    security_external_web: str
    # URL of external authentication logout server. | MaxLen: 127
    security_external_logout: str
    # Replacement message override group. | MaxLen: 35
    replacemsg_override_group: str
    # URL redirection after disclaimer/authentication. | MaxLen: 1023
    security_redirect_url: str
    # HTTPS server certificate. | MaxLen: 35
    auth_cert: str
    # Address of captive portal. | MaxLen: 63
    auth_portal_addr: str
    # Name of security-exempt-list. | MaxLen: 35
    security_exempt_list: str
    # User groups that can authenticate with the captive portal.
    security_groups: list[InterfaceSecuritygroupsObject]
    # Configure IKE authentication SAML server. | MaxLen: 35
    ike_saml_server: str
    # Enable/disable passively gathering of device identity inform | Default: disable
    device_identification: Literal["enable", "disable"]
    # Exclude IOT or OT application signatures.
    exclude_signatures: Literal["iot", "ot"]
    # Enable/disable passive gathering of user identity informatio | Default: enable
    device_user_identification: Literal["enable", "disable"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) receptio | Default: vdom
    lldp_reception: Literal["enable", "disable", "vdom"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) transmis | Default: vdom
    lldp_transmission: Literal["enable", "disable", "vdom"]
    # LLDP-MED network policy profile. | MaxLen: 35
    lldp_network_policy: str
    # Estimated maximum upstream bandwidth (kbps). Used to estimat | Default: 0 | Min: 0 | Max: 4294967295
    estimated_upstream_bandwidth: int
    # Estimated maximum downstream bandwidth (kbps). Used to estim | Default: 0 | Min: 0 | Max: 4294967295
    estimated_downstream_bandwidth: int
    # Measured upstream bandwidth (kbps). | Default: 0 | Min: 0 | Max: 4294967295
    measured_upstream_bandwidth: int
    # Measured downstream bandwidth (kbps). | Default: 0 | Min: 0 | Max: 4294967295
    measured_downstream_bandwidth: int
    # Bandwidth measure time. | Default: 0 | Min: 0 | Max: 4294967295
    bandwidth_measure_time: int
    # Enable monitoring bandwidth on this interface. | Default: disable
    monitor_bandwidth: Literal["enable", "disable"]
    # Enable/disable use of virtual MAC for VRRP. | Default: disable
    vrrp_virtual_mac: Literal["enable", "disable"]
    # VRRP configuration.
    vrrp: list[InterfaceVrrpObject]
    # PHY settings
    phy_setting: str
    # Interface role. | Default: undefined
    role: Literal["lan", "wan", "dmz", "undefined"]
    # Permanent SNMP Index of the interface. | Default: 0 | Min: 0 | Max: 2147483647
    snmp_index: int
    # Enable/disable adding a secondary IP to this interface. | Default: disable
    secondary_IP: Literal["enable", "disable"]
    # Second IP address of interface.
    secondaryip: list[InterfaceSecondaryipObject]
    # Enable/disable preservation of session route when dirty. | Default: disable
    preserve_session_route: Literal["enable", "disable"]
    # Enable/disable automatic authorization of dedicated Fortinet | Default: disable
    auto_auth_extension_device: Literal["enable", "disable"]
    # Enable/disable automatic registration of unknown FortiAP dev | Default: enable
    ap_discover: Literal["enable", "disable"]
    # Protocol for FortiGate neighbor discovery. | Default: lldp
    fortilink_neighbor_detect: Literal["lldp", "fortilink"]
    # Enable/disable automatic IP address assignment of this inter | Default: inherit-global
    ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"]
    # Number of IP addresses to be allocated by FortiIPAM and used | Default: 256
    managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"]
    # Enable/disable FortiLink split interface to connect member l | Default: enable
    fortilink_split_interface: Literal["enable", "disable"]
    # Implicitly created. | Default: 0 | Min: 0 | Max: 255
    internal: int
    # FortiLink split interface backup link. | Default: 0 | Min: 0 | Max: 255
    fortilink_backup_link: int
    # Block FortiSwitch port-to-port traffic. | Default: disable
    switch_controller_access_vlan: Literal["enable", "disable"]
    # Switch controller traffic policy for the VLAN. | MaxLen: 63
    switch_controller_traffic_policy: str
    # Stop Layer2 MAC learning and interception of BPDUs and other | Default: disable
    switch_controller_rspan_mode: Literal["disable", "enable"]
    # NetFlow collection and processing. | Default: disable
    switch_controller_netflow_collect: Literal["disable", "enable"]
    # VLAN to use for FortiLink management purposes. | Default: 4094 | Min: 1 | Max: 4094
    switch_controller_mgmt_vlan: int
    # Switch controller IGMP snooping. | Default: disable
    switch_controller_igmp_snooping: Literal["enable", "disable"]
    # Switch controller IGMP snooping proxy. | Default: disable
    switch_controller_igmp_snooping_proxy: Literal["enable", "disable"]
    # Switch controller IGMP snooping fast-leave. | Default: disable
    switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"]
    # Switch controller DHCP snooping. | Default: disable
    switch_controller_dhcp_snooping: Literal["enable", "disable"]
    # Switch controller DHCP snooping verify MAC. | Default: disable
    switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"]
    # Switch controller DHCP snooping option82. | Default: disable
    switch_controller_dhcp_snooping_option82: Literal["enable", "disable"]
    # Configure DHCP server access list.
    dhcp_snooping_server_list: list[InterfaceDhcpsnoopingserverlistObject]
    # Enable/disable/Monitor FortiSwitch ARP inspection. | Default: disable
    switch_controller_arp_inspection: Literal["enable", "disable", "monitor"]
    # Limit the number of dynamic MAC addresses on this VLAN | Default: 0 | Min: 0 | Max: 128
    switch_controller_learning_limit: int
    # Integrated FortiLink settings for managed FortiSwitch. | MaxLen: 35
    switch_controller_nac: str
    # Integrated FortiLink settings for managed FortiSwitch. | MaxLen: 35
    switch_controller_dynamic: str
    # Interface's purpose when assigning traffic (read only). | Default: none
    switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"]
    # Enable/disable managed FortiSwitch IoT scanning. | Default: disable
    switch_controller_iot_scanning: Literal["enable", "disable"]
    # Enable/disable managed FortiSwitch routing offload. | Default: disable
    switch_controller_offload: Literal["enable", "disable"]
    # IP for routing offload on FortiSwitch. | Default: 0.0.0.0
    switch_controller_offload_ip: str
    # Enable/disable managed FortiSwitch routing offload gateway. | Default: disable
    switch_controller_offload_gw: Literal["enable", "disable"]
    # Creation status for switch-controller VLANs. | Default: 0 | Min: 0 | Max: 4294967295
    swc_vlan: int
    # Initial create for switch-controller VLANs. | Default: 0 | Min: 0 | Max: 4294967295
    swc_first_create: int
    # Color of icon on the GUI. | Default: 0 | Min: 0 | Max: 32
    color: int
    # Config object tagging.
    tagging: list[InterfaceTaggingObject]
    # Enable/disable EAP-Supplicant. | Default: disable
    eap_supplicant: Literal["enable", "disable"]
    # EAP method.
    eap_method: Literal["tls", "peap"]
    # EAP identity. | MaxLen: 35
    eap_identity: str
    # EAP password. | MaxLen: 128
    eap_password: str
    # EAP CA certificate name. | MaxLen: 79
    eap_ca_cert: str
    # EAP user certificate name. | MaxLen: 35
    eap_user_cert: str
    # default purdue level of device detected on this interface. | Default: 3
    default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
    # IPv6 of interface.
    ipv6: str
    # Print physical interface information.
    physical: str
    
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
    def to_dict(self) -> InterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Interface:
    """
    Configure interfaces.
    
    Path: system/interface
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
    ) -> InterfaceObject: ...
    
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
    ) -> InterfaceObject: ...
    
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
    ) -> list[InterfaceObject]: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
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
    ) -> list[InterfaceObject]: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
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
    ) -> list[InterfaceObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> InterfaceObject | list[InterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> InterfaceObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: InterfacePayload | None = ...,
        name: str | None = ...,
        vrf: int | None = ...,
        cli_conn_status: int | None = ...,
        fortilink: Literal["enable", "disable"] | None = ...,
        switch_controller_source_ip: Literal["outbound", "fixed"] | None = ...,
        mode: Literal["static", "dhcp", "pppoe"] | None = ...,
        client_options: str | list[str] | list[dict[str, Any]] | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_relay_interface: str | None = ...,
        dhcp_relay_vrf_select: int | None = ...,
        dhcp_broadcast_flag: Literal["disable", "enable"] | None = ...,
        dhcp_relay_service: Literal["disable", "enable"] | None = ...,
        dhcp_relay_ip: str | list[str] | None = ...,
        dhcp_relay_source_ip: str | None = ...,
        dhcp_relay_circuit_id: str | None = ...,
        dhcp_relay_link_selection: str | None = ...,
        dhcp_relay_request_all_server: Literal["disable", "enable"] | None = ...,
        dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = ...,
        dhcp_relay_type: Literal["regular", "ipsec"] | None = ...,
        dhcp_smart_relay: Literal["disable", "enable"] | None = ...,
        dhcp_relay_agent_option: Literal["enable", "disable"] | None = ...,
        dhcp_classless_route_addition: Literal["enable", "disable"] | None = ...,
        management_ip: str | None = ...,
        ip: str | None = ...,
        allowaccess: Literal["ping", "https", "ssh", "snmp", "http", "telnet", "fgfm", "radius-acct", "probe-response", "fabric", "ftm", "speed-test", "scim"] | list[str] | None = ...,
        gwdetect: Literal["enable", "disable"] | None = ...,
        ping_serv_status: int | None = ...,
        detectserver: str | None = ...,
        detectprotocol: Literal["ping", "tcp-echo", "udp-echo"] | list[str] | None = ...,
        ha_priority: int | None = ...,
        fail_detect: Literal["enable", "disable"] | None = ...,
        fail_detect_option: Literal["detectserver", "link-down"] | list[str] | None = ...,
        fail_alert_method: Literal["link-failed-signal", "link-down"] | None = ...,
        fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = ...,
        fail_alert_interfaces: str | list[str] | list[dict[str, Any]] | None = ...,
        dhcp_client_identifier: str | None = ...,
        dhcp_renew_time: int | None = ...,
        ipunnumbered: str | None = ...,
        username: str | None = ...,
        pppoe_egress_cos: Literal["cos0", "cos1", "cos2", "cos3", "cos4", "cos5", "cos6", "cos7"] | None = ...,
        pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = ...,
        password: str | None = ...,
        idle_timeout: int | None = ...,
        multilink: Literal["enable", "disable"] | None = ...,
        mrru: int | None = ...,
        detected_peer_mtu: int | None = ...,
        disc_retry_timeout: int | None = ...,
        padt_retry_timeout: int | None = ...,
        service_name: str | None = ...,
        ac_name: str | None = ...,
        lcp_echo_interval: int | None = ...,
        lcp_max_echo_fails: int | None = ...,
        defaultgw: Literal["enable", "disable"] | None = ...,
        dns_server_override: Literal["enable", "disable"] | None = ...,
        dns_server_protocol: Literal["cleartext", "dot", "doh"] | list[str] | None = ...,
        auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_client: Literal["enable", "disable"] | None = ...,
        pptp_user: str | None = ...,
        pptp_password: str | None = ...,
        pptp_server_ip: str | None = ...,
        pptp_auth_type: Literal["auto", "pap", "chap", "mschapv1", "mschapv2"] | None = ...,
        pptp_timeout: int | None = ...,
        arpforward: Literal["enable", "disable"] | None = ...,
        ndiscforward: Literal["enable", "disable"] | None = ...,
        broadcast_forward: Literal["enable", "disable"] | None = ...,
        bfd: Literal["global", "enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        l2forward: Literal["enable", "disable"] | None = ...,
        icmp_send_redirect: Literal["enable", "disable"] | None = ...,
        icmp_accept_redirect: Literal["enable", "disable"] | None = ...,
        reachable_time: int | None = ...,
        vlanforward: Literal["enable", "disable"] | None = ...,
        stpforward: Literal["enable", "disable"] | None = ...,
        stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = ...,
        ips_sniffer_mode: Literal["enable", "disable"] | None = ...,
        ident_accept: Literal["enable", "disable"] | None = ...,
        ipmac: Literal["enable", "disable"] | None = ...,
        subst: Literal["enable", "disable"] | None = ...,
        macaddr: str | None = ...,
        virtual_mac: str | None = ...,
        substitute_dst_mac: str | None = ...,
        speed: Literal["auto", "10full", "10half", "100full", "100half", "100auto", "1000full", "1000auto"] | None = ...,
        status: Literal["up", "down"] | None = ...,
        netbios_forward: Literal["disable", "enable"] | None = ...,
        wins_ip: str | None = ...,
        type: Literal["physical", "vlan", "aggregate", "redundant", "tunnel", "vdom-link", "loopback", "switch", "vap-switch", "wl-mesh", "fext-wan", "vxlan", "geneve", "switch-vlan", "emac-vlan", "lan-extension"] | None = ...,
        dedicated_to: Literal["none", "management"] | None = ...,
        trust_ip_1: str | None = ...,
        trust_ip_2: str | None = ...,
        trust_ip_3: str | None = ...,
        trust_ip6_1: str | None = ...,
        trust_ip6_2: str | None = ...,
        trust_ip6_3: str | None = ...,
        ring_rx: int | None = ...,
        ring_tx: int | None = ...,
        wccp: Literal["enable", "disable"] | None = ...,
        netflow_sampler: Literal["disable", "tx", "rx", "both"] | None = ...,
        netflow_sample_rate: int | None = ...,
        netflow_sampler_id: int | None = ...,
        sflow_sampler: Literal["enable", "disable"] | None = ...,
        drop_fragment: Literal["enable", "disable"] | None = ...,
        src_check: Literal["enable", "disable"] | None = ...,
        sample_rate: int | None = ...,
        polling_interval: int | None = ...,
        sample_direction: Literal["tx", "rx", "both"] | None = ...,
        explicit_web_proxy: Literal["enable", "disable"] | None = ...,
        explicit_ftp_proxy: Literal["enable", "disable"] | None = ...,
        proxy_captive_portal: Literal["enable", "disable"] | None = ...,
        tcp_mss: int | None = ...,
        inbandwidth: int | None = ...,
        outbandwidth: int | None = ...,
        egress_shaping_profile: str | None = ...,
        ingress_shaping_profile: str | None = ...,
        spillover_threshold: int | None = ...,
        ingress_spillover_threshold: int | None = ...,
        weight: int | None = ...,
        interface: str | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        mtu_override: Literal["enable", "disable"] | None = ...,
        mtu: int | None = ...,
        vlan_protocol: Literal["8021q", "8021ad"] | None = ...,
        vlanid: int | None = ...,
        forward_domain: int | None = ...,
        remote_ip: str | None = ...,
        member: str | list[str] | list[dict[str, Any]] | None = ...,
        lacp_mode: Literal["static", "passive", "active"] | None = ...,
        lacp_ha_secondary: Literal["enable", "disable"] | None = ...,
        system_id_type: Literal["auto", "user"] | None = ...,
        system_id: str | None = ...,
        lacp_speed: Literal["slow", "fast"] | None = ...,
        min_links: int | None = ...,
        min_links_down: Literal["operational", "administrative"] | None = ...,
        algorithm: Literal["L2", "L3", "L4", "NPU-GRE", "Source-MAC"] | None = ...,
        link_up_delay: int | None = ...,
        aggregate_type: Literal["physical", "vxlan"] | None = ...,
        priority_override: Literal["enable", "disable"] | None = ...,
        aggregate: str | None = ...,
        redundant_interface: str | None = ...,
        devindex: int | None = ...,
        vindex: int | None = ...,
        switch: str | None = ...,
        description: str | None = ...,
        alias: str | None = ...,
        security_mode: Literal["none", "captive-portal", "802.1X"] | None = ...,
        security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = ...,
        security_ip_auth_bypass: Literal["enable", "disable"] | None = ...,
        security_external_web: str | None = ...,
        security_external_logout: str | None = ...,
        replacemsg_override_group: str | None = ...,
        security_redirect_url: str | None = ...,
        auth_cert: str | None = ...,
        auth_portal_addr: str | None = ...,
        security_exempt_list: str | None = ...,
        security_groups: str | list[str] | list[dict[str, Any]] | None = ...,
        ike_saml_server: str | None = ...,
        device_identification: Literal["enable", "disable"] | None = ...,
        exclude_signatures: Literal["iot", "ot"] | list[str] | None = ...,
        device_user_identification: Literal["enable", "disable"] | None = ...,
        lldp_reception: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "vdom"] | None = ...,
        lldp_network_policy: str | None = ...,
        estimated_upstream_bandwidth: int | None = ...,
        estimated_downstream_bandwidth: int | None = ...,
        measured_upstream_bandwidth: int | None = ...,
        measured_downstream_bandwidth: int | None = ...,
        bandwidth_measure_time: int | None = ...,
        monitor_bandwidth: Literal["enable", "disable"] | None = ...,
        vrrp_virtual_mac: Literal["enable", "disable"] | None = ...,
        vrrp: str | list[str] | list[dict[str, Any]] | None = ...,
        phy_setting: str | None = ...,
        role: Literal["lan", "wan", "dmz", "undefined"] | None = ...,
        snmp_index: int | None = ...,
        secondary_IP: Literal["enable", "disable"] | None = ...,
        secondaryip: str | list[str] | list[dict[str, Any]] | None = ...,
        preserve_session_route: Literal["enable", "disable"] | None = ...,
        auto_auth_extension_device: Literal["enable", "disable"] | None = ...,
        ap_discover: Literal["enable", "disable"] | None = ...,
        fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = ...,
        ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = ...,
        managed_subnetwork_size: Literal["4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608", "16777216"] | None = ...,
        fortilink_split_interface: Literal["enable", "disable"] | None = ...,
        internal: int | None = ...,
        fortilink_backup_link: int | None = ...,
        switch_controller_access_vlan: Literal["enable", "disable"] | None = ...,
        switch_controller_traffic_policy: str | None = ...,
        switch_controller_rspan_mode: Literal["disable", "enable"] | None = ...,
        switch_controller_netflow_collect: Literal["disable", "enable"] | None = ...,
        switch_controller_mgmt_vlan: int | None = ...,
        switch_controller_igmp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = ...,
        switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = ...,
        switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = ...,
        dhcp_snooping_server_list: str | list[str] | list[dict[str, Any]] | None = ...,
        switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = ...,
        switch_controller_learning_limit: int | None = ...,
        switch_controller_nac: str | None = ...,
        switch_controller_dynamic: str | None = ...,
        switch_controller_feature: Literal["none", "default-vlan", "quarantine", "rspan", "voice", "video", "nac", "nac-segment"] | None = ...,
        switch_controller_iot_scanning: Literal["enable", "disable"] | None = ...,
        switch_controller_offload: Literal["enable", "disable"] | None = ...,
        switch_controller_offload_ip: str | None = ...,
        switch_controller_offload_gw: Literal["enable", "disable"] | None = ...,
        swc_vlan: int | None = ...,
        swc_first_create: int | None = ...,
        color: int | None = ...,
        tagging: str | list[str] | list[dict[str, Any]] | None = ...,
        eap_supplicant: Literal["enable", "disable"] | None = ...,
        eap_method: Literal["tls", "peap"] | None = ...,
        eap_identity: str | None = ...,
        eap_password: str | None = ...,
        eap_ca_cert: str | None = ...,
        eap_user_cert: str | None = ...,
        default_purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = ...,
        ipv6: str | None = ...,
        physical: str | None = ...,
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
    "Interface",
    "InterfacePayload",
    "InterfaceResponse",
    "InterfaceObject",
]
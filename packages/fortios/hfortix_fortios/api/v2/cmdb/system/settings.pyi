from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingsPayload(TypedDict, total=False):
    """
    Type hints for system/settings payload fields.
    
    Configure VDOM settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: device, dhcp-proxy-interface)

    **Usage:**
        payload: SettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    comments: str  # VDOM comments. | MaxLen: 255
    vdom_type: Literal["traffic", "lan-extension", "admin"]  # Vdom type (traffic, lan-extension or admin). | Default: traffic
    lan_extension_controller_addr: str  # Controller IP address or FQDN to connect. | MaxLen: 255
    lan_extension_controller_port: int  # Controller port to connect. | Default: 5246 | Min: 1024 | Max: 65535
    opmode: Literal["nat", "transparent"]  # Firewall operation mode (NAT or Transparent). | Default: nat
    ngfw_mode: Literal["profile-based", "policy-based"]  # Next Generation Firewall (NGFW) mode. | Default: profile-based
    http_external_dest: Literal["fortiweb", "forticache"]  # Offload HTTP traffic to FortiWeb or FortiCache. | Default: fortiweb
    firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"]  # Select how to manage sessions affected by firewall | Default: check-all
    manageip: str  # Transparent mode IPv4 management IP address and ne
    gateway: str  # Transparent mode IPv4 default gateway IP address. | Default: 0.0.0.0
    ip: str  # IP address and netmask. | Default: 0.0.0.0 0.0.0.0
    manageip6: str  # Transparent mode IPv6 management IP address and ne | Default: ::/0
    gateway6: str  # Transparent mode IPv6 default gateway IP address. | Default: ::
    ip6: str  # IPv6 address prefix for NAT mode. | Default: ::/0
    device: str  # Interface to use for management access for NAT mod | MaxLen: 35
    bfd: Literal["enable", "disable"]  # Enable/disable Bi-directional Forwarding Detection | Default: disable
    bfd_desired_min_tx: int  # BFD desired minimal transmit interval | Default: 250 | Min: 1 | Max: 100000
    bfd_required_min_rx: int  # BFD required minimal receive interval | Default: 250 | Min: 1 | Max: 100000
    bfd_detect_mult: int  # BFD detection multiplier (1 - 50, default = 3). | Default: 3 | Min: 1 | Max: 50
    bfd_dont_enforce_src_port: Literal["enable", "disable"]  # Enable to not enforce verifying the source port of | Default: disable
    utf8_spam_tagging: Literal["enable", "disable"]  # Enable/disable converting antispam tags to UTF-8 f | Default: enable
    wccp_cache_engine: Literal["enable", "disable"]  # Enable/disable WCCP cache engine. | Default: disable
    vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"]  # Enable/disable periodic VPN log statistics for one | Default: ipsec pptp l2tp ssl
    vpn_stats_period: int  # Period to send VPN log statistics | Default: 600 | Min: 0 | Max: 4294967295
    v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"]  # IPv4 Equal-cost multi-path (ECMP) routing and load | Default: source-ip-based
    mac_ttl: int  # Duration of MAC addresses in Transparent mode | Default: 300 | Min: 300 | Max: 8640000
    fw_session_hairpin: Literal["enable", "disable"]  # Enable/disable checking for a matching policy each | Default: disable
    prp_trailer_action: Literal["enable", "disable"]  # Enable/disable action to take on PRP trailer. | Default: disable
    snat_hairpin_traffic: Literal["enable", "disable"]  # Enable/disable source NAT (SNAT) for VIP hairpin t | Default: enable
    dhcp_proxy: Literal["enable", "disable"]  # Enable/disable the DHCP Proxy. | Default: disable
    dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    dhcp_proxy_interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    dhcp_proxy_vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    dhcp_server_ip: list[dict[str, Any]]  # DHCP Server IPv4 address.
    dhcp6_server_ip: list[dict[str, Any]]  # DHCPv6 server IPv6 address.
    central_nat: Literal["enable", "disable"]  # Enable/disable central NAT. | Default: disable
    gui_default_policy_columns: list[dict[str, Any]]  # Default columns to display for policy lists on GUI
    lldp_reception: Literal["enable", "disable", "global"]  # Enable/disable Link Layer Discovery Protocol | Default: global
    lldp_transmission: Literal["enable", "disable", "global"]  # Enable/disable Link Layer Discovery Protocol | Default: global
    link_down_access: Literal["enable", "disable"]  # Enable/disable link down access traffic. | Default: enable
    nat46_generate_ipv6_fragment_header: Literal["enable", "disable"]  # Enable/disable NAT46 IPv6 fragment header generati | Default: disable
    nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"]  # Enable/disable mandatory IPv4 packet forwarding in | Default: disable
    nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"]  # Enable/disable mandatory IPv6 packet forwarding in | Default: enable
    detect_unknown_esp: Literal["enable", "disable"]  # Enable/disable detection of unknown ESP packets | Default: enable
    intree_ses_best_route: Literal["force", "disable"]  # Force the intree session to always use the best ro | Default: disable
    auxiliary_session: Literal["enable", "disable"]  # Enable/disable auxiliary session. | Default: disable
    asymroute: Literal["enable", "disable"]  # Enable/disable IPv4 asymmetric routing. | Default: disable
    asymroute_icmp: Literal["enable", "disable"]  # Enable/disable ICMP asymmetric routing. | Default: disable
    tcp_session_without_syn: Literal["enable", "disable"]  # Enable/disable allowing TCP session without SYN fl | Default: disable
    ses_denied_traffic: Literal["enable", "disable"]  # Enable/disable including denied session in the ses | Default: disable
    ses_denied_multicast_traffic: Literal["enable", "disable"]  # Enable/disable including denied multicast session | Default: disable
    strict_src_check: Literal["enable", "disable"]  # Enable/disable strict source verification. | Default: disable
    allow_linkdown_path: Literal["enable", "disable"]  # Enable/disable link down path. | Default: disable
    asymroute6: Literal["enable", "disable"]  # Enable/disable asymmetric IPv6 routing. | Default: disable
    asymroute6_icmp: Literal["enable", "disable"]  # Enable/disable asymmetric ICMPv6 routing. | Default: disable
    sctp_session_without_init: Literal["enable", "disable"]  # Enable/disable SCTP session creation without SCTP | Default: disable
    sip_expectation: Literal["enable", "disable"]  # Enable/disable the SIP kernel session helper to cr | Default: disable
    sip_nat_trace: Literal["enable", "disable"]  # Enable/disable recording the original SIP source I | Default: enable
    h323_direct_model: Literal["disable", "enable"]  # Enable/disable H323 direct model. | Default: disable
    status: Literal["enable", "disable"]  # Enable/disable this VDOM. | Default: enable
    sip_tcp_port: int  # TCP port the SIP proxy monitors for SIP traffic | Default: 5060 | Min: 1 | Max: 65535
    sip_udp_port: int  # UDP port the SIP proxy monitors for SIP traffic | Default: 5060 | Min: 1 | Max: 65535
    sip_ssl_port: int  # TCP port the SIP proxy monitors for SIP SSL/TLS tr | Default: 5061 | Min: 0 | Max: 65535
    sccp_port: int  # TCP port the SCCP proxy monitors for SCCP traffic | Default: 2000 | Min: 0 | Max: 65535
    multicast_forward: Literal["enable", "disable"]  # Enable/disable multicast forwarding. | Default: enable
    multicast_ttl_notchange: Literal["enable", "disable"]  # Enable/disable preventing the FortiGate from chang | Default: disable
    multicast_skip_policy: Literal["enable", "disable"]  # Enable/disable allowing multicast traffic through | Default: disable
    allow_subnet_overlap: Literal["enable", "disable"]  # Enable/disable allowing interface subnets to use o | Default: disable
    deny_tcp_with_icmp: Literal["enable", "disable"]  # Enable/disable denying TCP by sending an ICMP comm | Default: disable
    ecmp_max_paths: int  # Maximum number of Equal Cost Multi-Path (ECMP) nex | Default: 255 | Min: 1 | Max: 255
    discovered_device_timeout: int  # Timeout for discovered devices | Default: 28 | Min: 1 | Max: 365
    email_portal_check_dns: Literal["disable", "enable"]  # Enable/disable using DNS to validate email address | Default: enable
    default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"]  # Configure how the FortiGate handles VoIP traffic w | Default: proxy-based
    gui_icap: Literal["enable", "disable"]  # Enable/disable ICAP on the GUI. | Default: disable
    gui_implicit_policy: Literal["enable", "disable"]  # Enable/disable implicit firewall policies on the G | Default: enable
    gui_dns_database: Literal["enable", "disable"]  # Enable/disable DNS database settings on the GUI. | Default: disable
    gui_load_balance: Literal["enable", "disable"]  # Enable/disable server load balancing on the GUI. | Default: disable
    gui_multicast_policy: Literal["enable", "disable"]  # Enable/disable multicast firewall policies on the | Default: disable
    gui_dos_policy: Literal["enable", "disable"]  # Enable/disable DoS policies on the GUI. | Default: enable
    gui_object_colors: Literal["enable", "disable"]  # Enable/disable object colors on the GUI. | Default: enable
    gui_route_tag_address_creation: Literal["enable", "disable"]  # Enable/disable route-tag addresses on the GUI. | Default: disable
    gui_voip_profile: Literal["enable", "disable"]  # Enable/disable VoIP profiles on the GUI. | Default: disable
    gui_ap_profile: Literal["enable", "disable"]  # Enable/disable FortiAP profiles on the GUI. | Default: enable
    gui_security_profile_group: Literal["enable", "disable"]  # Enable/disable Security Profile Groups on the GUI. | Default: disable
    gui_local_in_policy: Literal["enable", "disable"]  # Enable/disable Local-In policies on the GUI. | Default: disable
    gui_wanopt_cache: Literal["enable", "disable"]  # Enable/disable WAN Optimization and Web Caching on | Default: disable
    gui_explicit_proxy: Literal["enable", "disable"]  # Enable/disable the explicit proxy on the GUI. | Default: disable
    gui_dynamic_routing: Literal["enable", "disable"]  # Enable/disable dynamic routing on the GUI. | Default: enable
    gui_sslvpn_personal_bookmarks: Literal["enable", "disable"]  # Enable/disable SSL-VPN personal bookmark managemen | Default: disable
    gui_sslvpn_realms: Literal["enable", "disable"]  # Enable/disable SSL-VPN realms on the GUI. | Default: disable
    gui_policy_based_ipsec: Literal["enable", "disable"]  # Enable/disable policy-based IPsec VPN on the GUI. | Default: disable
    gui_threat_weight: Literal["enable", "disable"]  # Enable/disable threat weight on the GUI. | Default: enable
    gui_spamfilter: Literal["enable", "disable"]  # Enable/disable Antispam on the GUI. | Default: disable
    gui_file_filter: Literal["enable", "disable"]  # Enable/disable File-filter on the GUI. | Default: enable
    gui_application_control: Literal["enable", "disable"]  # Enable/disable application control on the GUI. | Default: enable
    gui_ips: Literal["enable", "disable"]  # Enable/disable IPS on the GUI. | Default: enable
    gui_dhcp_advanced: Literal["enable", "disable"]  # Enable/disable advanced DHCP options on the GUI. | Default: enable
    gui_vpn: Literal["enable", "disable"]  # Enable/disable IPsec VPN settings pages on the GUI | Default: enable
    gui_sslvpn: Literal["enable", "disable"]  # Enable/disable SSL-VPN settings pages on the GUI. | Default: disable
    gui_wireless_controller: Literal["enable", "disable"]  # Enable/disable the wireless controller on the GUI. | Default: enable
    gui_advanced_wireless_features: Literal["enable", "disable"]  # Enable/disable advanced wireless features in GUI. | Default: disable
    gui_switch_controller: Literal["enable", "disable"]  # Enable/disable the switch controller on the GUI. | Default: enable
    gui_fortiap_split_tunneling: Literal["enable", "disable"]  # Enable/disable FortiAP split tunneling on the GUI. | Default: disable
    gui_webfilter_advanced: Literal["enable", "disable"]  # Enable/disable advanced web filtering on the GUI. | Default: disable
    gui_traffic_shaping: Literal["enable", "disable"]  # Enable/disable traffic shaping on the GUI. | Default: enable
    gui_wan_load_balancing: Literal["enable", "disable"]  # Enable/disable SD-WAN on the GUI. | Default: enable
    gui_antivirus: Literal["enable", "disable"]  # Enable/disable AntiVirus on the GUI. | Default: enable
    gui_webfilter: Literal["enable", "disable"]  # Enable/disable Web filtering on the GUI. | Default: enable
    gui_videofilter: Literal["enable", "disable"]  # Enable/disable Video filtering on the GUI. | Default: enable
    gui_dnsfilter: Literal["enable", "disable"]  # Enable/disable DNS Filtering on the GUI. | Default: enable
    gui_waf_profile: Literal["enable", "disable"]  # Enable/disable Web Application Firewall on the GUI | Default: disable
    gui_dlp_profile: Literal["enable", "disable"]  # Enable/disable Data Loss Prevention on the GUI. | Default: disable
    gui_dlp_advanced: Literal["enable", "disable"]  # Enable/disable Show advanced DLP expressions on th | Default: disable
    gui_virtual_patch_profile: Literal["enable", "disable"]  # Enable/disable Virtual Patching on the GUI. | Default: disable
    gui_casb: Literal["enable", "disable"]  # Enable/disable Inline-CASB on the GUI. | Default: disable
    gui_fortiextender_controller: Literal["enable", "disable"]  # Enable/disable FortiExtender on the GUI. | Default: disable
    gui_advanced_policy: Literal["enable", "disable"]  # Enable/disable advanced policy configuration on th | Default: disable
    gui_allow_unnamed_policy: Literal["enable", "disable"]  # Enable/disable the requirement for policy naming o | Default: disable
    gui_email_collection: Literal["enable", "disable"]  # Enable/disable email collection on the GUI. | Default: disable
    gui_multiple_interface_policy: Literal["enable", "disable"]  # Enable/disable adding multiple interfaces to a pol | Default: disable
    gui_policy_disclaimer: Literal["enable", "disable"]  # Enable/disable policy disclaimer on the GUI. | Default: disable
    gui_ztna: Literal["enable", "disable"]  # Enable/disable Zero Trust Network Access features | Default: disable
    gui_ot: Literal["enable", "disable"]  # Enable/disable Operational technology features on | Default: disable
    gui_dynamic_device_os_id: Literal["enable", "disable"]  # Enable/disable Create dynamic addresses to manage | Default: disable
    gui_gtp: Literal["enable", "disable"]  # Enable/disable Manage general radio packet service | Default: enable
    location_id: str  # Local location ID in the form of an IPv4 address. | Default: 0.0.0.0
    ike_session_resume: Literal["enable", "disable"]  # Enable/disable IKEv2 session resumption (RFC 5723) | Default: disable
    ike_quick_crash_detect: Literal["enable", "disable"]  # Enable/disable IKE quick crash detection | Default: disable
    ike_dn_format: Literal["with-space", "no-space"]  # Configure IKE ASN.1 Distinguished Name format conv | Default: with-space
    ike_port: int  # UDP port for IKE/IPsec traffic (default 500). | Default: 500 | Min: 1024 | Max: 65535
    ike_tcp_port: int  # TCP port for IKE/IPsec traffic (default 443). | Default: 443 | Min: 1 | Max: 65535
    ike_policy_route: Literal["enable", "disable"]  # Enable/disable IKE Policy Based Routing (PBR). | Default: disable
    ike_detailed_event_logs: Literal["disable", "enable"]  # Enable/disable detail log for IKE events. | Default: disable
    block_land_attack: Literal["disable", "enable"]  # Enable/disable blocking of land attacks. | Default: disable
    default_app_port_as_service: Literal["enable", "disable"]  # Enable/disable policy service enforcement based on | Default: enable
    fqdn_session_check: Literal["enable", "disable"]  # Enable/disable dirty session check caused by FQDN | Default: disable
    ext_resource_session_check: Literal["enable", "disable"]  # Enable/disable dirty session check caused by exter | Default: disable
    dyn_addr_session_check: Literal["enable", "disable"]  # Enable/disable dirty session check caused by dynam | Default: disable
    default_policy_expiry_days: int  # Default policy expiry in days | Default: 30 | Min: 0 | Max: 365
    gui_enforce_change_summary: Literal["disable", "require", "optional"]  # Enforce change summaries for select tables in the | Default: require
    internet_service_database_cache: Literal["disable", "enable"]  # Enable/disable Internet Service database caching. | Default: disable
    internet_service_app_ctrl_size: int  # Maximum number of tuple entries | Default: 32768 | Min: 0 | Max: 4294967295

# Nested TypedDicts for table field children (dict mode)

class SettingsGuidefaultpolicycolumnsItem(TypedDict):
    """Type hints for gui-default-policy-columns table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Select column name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class SettingsGuidefaultpolicycolumnsObject:
    """Typed object for gui-default-policy-columns table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Select column name. | MaxLen: 79
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



# Response TypedDict for GET returns (all fields present in API response)
class SettingsResponse(TypedDict):
    """
    Type hints for system/settings API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    comments: str  # VDOM comments. | MaxLen: 255
    vdom_type: Literal["traffic", "lan-extension", "admin"]  # Vdom type (traffic, lan-extension or admin). | Default: traffic
    lan_extension_controller_addr: str  # Controller IP address or FQDN to connect. | MaxLen: 255
    lan_extension_controller_port: int  # Controller port to connect. | Default: 5246 | Min: 1024 | Max: 65535
    opmode: Literal["nat", "transparent"]  # Firewall operation mode (NAT or Transparent). | Default: nat
    ngfw_mode: Literal["profile-based", "policy-based"]  # Next Generation Firewall (NGFW) mode. | Default: profile-based
    http_external_dest: Literal["fortiweb", "forticache"]  # Offload HTTP traffic to FortiWeb or FortiCache. | Default: fortiweb
    firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"]  # Select how to manage sessions affected by firewall | Default: check-all
    manageip: str  # Transparent mode IPv4 management IP address and ne
    gateway: str  # Transparent mode IPv4 default gateway IP address. | Default: 0.0.0.0
    ip: str  # IP address and netmask. | Default: 0.0.0.0 0.0.0.0
    manageip6: str  # Transparent mode IPv6 management IP address and ne | Default: ::/0
    gateway6: str  # Transparent mode IPv6 default gateway IP address. | Default: ::
    ip6: str  # IPv6 address prefix for NAT mode. | Default: ::/0
    device: str  # Interface to use for management access for NAT mod | MaxLen: 35
    bfd: Literal["enable", "disable"]  # Enable/disable Bi-directional Forwarding Detection | Default: disable
    bfd_desired_min_tx: int  # BFD desired minimal transmit interval | Default: 250 | Min: 1 | Max: 100000
    bfd_required_min_rx: int  # BFD required minimal receive interval | Default: 250 | Min: 1 | Max: 100000
    bfd_detect_mult: int  # BFD detection multiplier (1 - 50, default = 3). | Default: 3 | Min: 1 | Max: 50
    bfd_dont_enforce_src_port: Literal["enable", "disable"]  # Enable to not enforce verifying the source port of | Default: disable
    utf8_spam_tagging: Literal["enable", "disable"]  # Enable/disable converting antispam tags to UTF-8 f | Default: enable
    wccp_cache_engine: Literal["enable", "disable"]  # Enable/disable WCCP cache engine. | Default: disable
    vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"]  # Enable/disable periodic VPN log statistics for one | Default: ipsec pptp l2tp ssl
    vpn_stats_period: int  # Period to send VPN log statistics | Default: 600 | Min: 0 | Max: 4294967295
    v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"]  # IPv4 Equal-cost multi-path (ECMP) routing and load | Default: source-ip-based
    mac_ttl: int  # Duration of MAC addresses in Transparent mode | Default: 300 | Min: 300 | Max: 8640000
    fw_session_hairpin: Literal["enable", "disable"]  # Enable/disable checking for a matching policy each | Default: disable
    prp_trailer_action: Literal["enable", "disable"]  # Enable/disable action to take on PRP trailer. | Default: disable
    snat_hairpin_traffic: Literal["enable", "disable"]  # Enable/disable source NAT (SNAT) for VIP hairpin t | Default: enable
    dhcp_proxy: Literal["enable", "disable"]  # Enable/disable the DHCP Proxy. | Default: disable
    dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    dhcp_proxy_interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    dhcp_proxy_vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    dhcp_server_ip: list[dict[str, Any]]  # DHCP Server IPv4 address.
    dhcp6_server_ip: list[dict[str, Any]]  # DHCPv6 server IPv6 address.
    central_nat: Literal["enable", "disable"]  # Enable/disable central NAT. | Default: disable
    gui_default_policy_columns: list[SettingsGuidefaultpolicycolumnsItem]  # Default columns to display for policy lists on GUI
    lldp_reception: Literal["enable", "disable", "global"]  # Enable/disable Link Layer Discovery Protocol | Default: global
    lldp_transmission: Literal["enable", "disable", "global"]  # Enable/disable Link Layer Discovery Protocol | Default: global
    link_down_access: Literal["enable", "disable"]  # Enable/disable link down access traffic. | Default: enable
    nat46_generate_ipv6_fragment_header: Literal["enable", "disable"]  # Enable/disable NAT46 IPv6 fragment header generati | Default: disable
    nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"]  # Enable/disable mandatory IPv4 packet forwarding in | Default: disable
    nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"]  # Enable/disable mandatory IPv6 packet forwarding in | Default: enable
    detect_unknown_esp: Literal["enable", "disable"]  # Enable/disable detection of unknown ESP packets | Default: enable
    intree_ses_best_route: Literal["force", "disable"]  # Force the intree session to always use the best ro | Default: disable
    auxiliary_session: Literal["enable", "disable"]  # Enable/disable auxiliary session. | Default: disable
    asymroute: Literal["enable", "disable"]  # Enable/disable IPv4 asymmetric routing. | Default: disable
    asymroute_icmp: Literal["enable", "disable"]  # Enable/disable ICMP asymmetric routing. | Default: disable
    tcp_session_without_syn: Literal["enable", "disable"]  # Enable/disable allowing TCP session without SYN fl | Default: disable
    ses_denied_traffic: Literal["enable", "disable"]  # Enable/disable including denied session in the ses | Default: disable
    ses_denied_multicast_traffic: Literal["enable", "disable"]  # Enable/disable including denied multicast session | Default: disable
    strict_src_check: Literal["enable", "disable"]  # Enable/disable strict source verification. | Default: disable
    allow_linkdown_path: Literal["enable", "disable"]  # Enable/disable link down path. | Default: disable
    asymroute6: Literal["enable", "disable"]  # Enable/disable asymmetric IPv6 routing. | Default: disable
    asymroute6_icmp: Literal["enable", "disable"]  # Enable/disable asymmetric ICMPv6 routing. | Default: disable
    sctp_session_without_init: Literal["enable", "disable"]  # Enable/disable SCTP session creation without SCTP | Default: disable
    sip_expectation: Literal["enable", "disable"]  # Enable/disable the SIP kernel session helper to cr | Default: disable
    sip_nat_trace: Literal["enable", "disable"]  # Enable/disable recording the original SIP source I | Default: enable
    h323_direct_model: Literal["disable", "enable"]  # Enable/disable H323 direct model. | Default: disable
    status: Literal["enable", "disable"]  # Enable/disable this VDOM. | Default: enable
    sip_tcp_port: int  # TCP port the SIP proxy monitors for SIP traffic | Default: 5060 | Min: 1 | Max: 65535
    sip_udp_port: int  # UDP port the SIP proxy monitors for SIP traffic | Default: 5060 | Min: 1 | Max: 65535
    sip_ssl_port: int  # TCP port the SIP proxy monitors for SIP SSL/TLS tr | Default: 5061 | Min: 0 | Max: 65535
    sccp_port: int  # TCP port the SCCP proxy monitors for SCCP traffic | Default: 2000 | Min: 0 | Max: 65535
    multicast_forward: Literal["enable", "disable"]  # Enable/disable multicast forwarding. | Default: enable
    multicast_ttl_notchange: Literal["enable", "disable"]  # Enable/disable preventing the FortiGate from chang | Default: disable
    multicast_skip_policy: Literal["enable", "disable"]  # Enable/disable allowing multicast traffic through | Default: disable
    allow_subnet_overlap: Literal["enable", "disable"]  # Enable/disable allowing interface subnets to use o | Default: disable
    deny_tcp_with_icmp: Literal["enable", "disable"]  # Enable/disable denying TCP by sending an ICMP comm | Default: disable
    ecmp_max_paths: int  # Maximum number of Equal Cost Multi-Path (ECMP) nex | Default: 255 | Min: 1 | Max: 255
    discovered_device_timeout: int  # Timeout for discovered devices | Default: 28 | Min: 1 | Max: 365
    email_portal_check_dns: Literal["disable", "enable"]  # Enable/disable using DNS to validate email address | Default: enable
    default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"]  # Configure how the FortiGate handles VoIP traffic w | Default: proxy-based
    gui_icap: Literal["enable", "disable"]  # Enable/disable ICAP on the GUI. | Default: disable
    gui_implicit_policy: Literal["enable", "disable"]  # Enable/disable implicit firewall policies on the G | Default: enable
    gui_dns_database: Literal["enable", "disable"]  # Enable/disable DNS database settings on the GUI. | Default: disable
    gui_load_balance: Literal["enable", "disable"]  # Enable/disable server load balancing on the GUI. | Default: disable
    gui_multicast_policy: Literal["enable", "disable"]  # Enable/disable multicast firewall policies on the | Default: disable
    gui_dos_policy: Literal["enable", "disable"]  # Enable/disable DoS policies on the GUI. | Default: enable
    gui_object_colors: Literal["enable", "disable"]  # Enable/disable object colors on the GUI. | Default: enable
    gui_route_tag_address_creation: Literal["enable", "disable"]  # Enable/disable route-tag addresses on the GUI. | Default: disable
    gui_voip_profile: Literal["enable", "disable"]  # Enable/disable VoIP profiles on the GUI. | Default: disable
    gui_ap_profile: Literal["enable", "disable"]  # Enable/disable FortiAP profiles on the GUI. | Default: enable
    gui_security_profile_group: Literal["enable", "disable"]  # Enable/disable Security Profile Groups on the GUI. | Default: disable
    gui_local_in_policy: Literal["enable", "disable"]  # Enable/disable Local-In policies on the GUI. | Default: disable
    gui_wanopt_cache: Literal["enable", "disable"]  # Enable/disable WAN Optimization and Web Caching on | Default: disable
    gui_explicit_proxy: Literal["enable", "disable"]  # Enable/disable the explicit proxy on the GUI. | Default: disable
    gui_dynamic_routing: Literal["enable", "disable"]  # Enable/disable dynamic routing on the GUI. | Default: enable
    gui_sslvpn_personal_bookmarks: Literal["enable", "disable"]  # Enable/disable SSL-VPN personal bookmark managemen | Default: disable
    gui_sslvpn_realms: Literal["enable", "disable"]  # Enable/disable SSL-VPN realms on the GUI. | Default: disable
    gui_policy_based_ipsec: Literal["enable", "disable"]  # Enable/disable policy-based IPsec VPN on the GUI. | Default: disable
    gui_threat_weight: Literal["enable", "disable"]  # Enable/disable threat weight on the GUI. | Default: enable
    gui_spamfilter: Literal["enable", "disable"]  # Enable/disable Antispam on the GUI. | Default: disable
    gui_file_filter: Literal["enable", "disable"]  # Enable/disable File-filter on the GUI. | Default: enable
    gui_application_control: Literal["enable", "disable"]  # Enable/disable application control on the GUI. | Default: enable
    gui_ips: Literal["enable", "disable"]  # Enable/disable IPS on the GUI. | Default: enable
    gui_dhcp_advanced: Literal["enable", "disable"]  # Enable/disable advanced DHCP options on the GUI. | Default: enable
    gui_vpn: Literal["enable", "disable"]  # Enable/disable IPsec VPN settings pages on the GUI | Default: enable
    gui_sslvpn: Literal["enable", "disable"]  # Enable/disable SSL-VPN settings pages on the GUI. | Default: disable
    gui_wireless_controller: Literal["enable", "disable"]  # Enable/disable the wireless controller on the GUI. | Default: enable
    gui_advanced_wireless_features: Literal["enable", "disable"]  # Enable/disable advanced wireless features in GUI. | Default: disable
    gui_switch_controller: Literal["enable", "disable"]  # Enable/disable the switch controller on the GUI. | Default: enable
    gui_fortiap_split_tunneling: Literal["enable", "disable"]  # Enable/disable FortiAP split tunneling on the GUI. | Default: disable
    gui_webfilter_advanced: Literal["enable", "disable"]  # Enable/disable advanced web filtering on the GUI. | Default: disable
    gui_traffic_shaping: Literal["enable", "disable"]  # Enable/disable traffic shaping on the GUI. | Default: enable
    gui_wan_load_balancing: Literal["enable", "disable"]  # Enable/disable SD-WAN on the GUI. | Default: enable
    gui_antivirus: Literal["enable", "disable"]  # Enable/disable AntiVirus on the GUI. | Default: enable
    gui_webfilter: Literal["enable", "disable"]  # Enable/disable Web filtering on the GUI. | Default: enable
    gui_videofilter: Literal["enable", "disable"]  # Enable/disable Video filtering on the GUI. | Default: enable
    gui_dnsfilter: Literal["enable", "disable"]  # Enable/disable DNS Filtering on the GUI. | Default: enable
    gui_waf_profile: Literal["enable", "disable"]  # Enable/disable Web Application Firewall on the GUI | Default: disable
    gui_dlp_profile: Literal["enable", "disable"]  # Enable/disable Data Loss Prevention on the GUI. | Default: disable
    gui_dlp_advanced: Literal["enable", "disable"]  # Enable/disable Show advanced DLP expressions on th | Default: disable
    gui_virtual_patch_profile: Literal["enable", "disable"]  # Enable/disable Virtual Patching on the GUI. | Default: disable
    gui_casb: Literal["enable", "disable"]  # Enable/disable Inline-CASB on the GUI. | Default: disable
    gui_fortiextender_controller: Literal["enable", "disable"]  # Enable/disable FortiExtender on the GUI. | Default: disable
    gui_advanced_policy: Literal["enable", "disable"]  # Enable/disable advanced policy configuration on th | Default: disable
    gui_allow_unnamed_policy: Literal["enable", "disable"]  # Enable/disable the requirement for policy naming o | Default: disable
    gui_email_collection: Literal["enable", "disable"]  # Enable/disable email collection on the GUI. | Default: disable
    gui_multiple_interface_policy: Literal["enable", "disable"]  # Enable/disable adding multiple interfaces to a pol | Default: disable
    gui_policy_disclaimer: Literal["enable", "disable"]  # Enable/disable policy disclaimer on the GUI. | Default: disable
    gui_ztna: Literal["enable", "disable"]  # Enable/disable Zero Trust Network Access features | Default: disable
    gui_ot: Literal["enable", "disable"]  # Enable/disable Operational technology features on | Default: disable
    gui_dynamic_device_os_id: Literal["enable", "disable"]  # Enable/disable Create dynamic addresses to manage | Default: disable
    gui_gtp: Literal["enable", "disable"]  # Enable/disable Manage general radio packet service | Default: enable
    location_id: str  # Local location ID in the form of an IPv4 address. | Default: 0.0.0.0
    ike_session_resume: Literal["enable", "disable"]  # Enable/disable IKEv2 session resumption (RFC 5723) | Default: disable
    ike_quick_crash_detect: Literal["enable", "disable"]  # Enable/disable IKE quick crash detection | Default: disable
    ike_dn_format: Literal["with-space", "no-space"]  # Configure IKE ASN.1 Distinguished Name format conv | Default: with-space
    ike_port: int  # UDP port for IKE/IPsec traffic (default 500). | Default: 500 | Min: 1024 | Max: 65535
    ike_tcp_port: int  # TCP port for IKE/IPsec traffic (default 443). | Default: 443 | Min: 1 | Max: 65535
    ike_policy_route: Literal["enable", "disable"]  # Enable/disable IKE Policy Based Routing (PBR). | Default: disable
    ike_detailed_event_logs: Literal["disable", "enable"]  # Enable/disable detail log for IKE events. | Default: disable
    block_land_attack: Literal["disable", "enable"]  # Enable/disable blocking of land attacks. | Default: disable
    default_app_port_as_service: Literal["enable", "disable"]  # Enable/disable policy service enforcement based on | Default: enable
    fqdn_session_check: Literal["enable", "disable"]  # Enable/disable dirty session check caused by FQDN | Default: disable
    ext_resource_session_check: Literal["enable", "disable"]  # Enable/disable dirty session check caused by exter | Default: disable
    dyn_addr_session_check: Literal["enable", "disable"]  # Enable/disable dirty session check caused by dynam | Default: disable
    default_policy_expiry_days: int  # Default policy expiry in days | Default: 30 | Min: 0 | Max: 365
    gui_enforce_change_summary: Literal["disable", "require", "optional"]  # Enforce change summaries for select tables in the | Default: require
    internet_service_database_cache: Literal["disable", "enable"]  # Enable/disable Internet Service database caching. | Default: disable
    internet_service_app_ctrl_size: int  # Maximum number of tuple entries | Default: 32768 | Min: 0 | Max: 4294967295


@final
class SettingsObject:
    """Typed FortiObject for system/settings with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # VDOM comments. | MaxLen: 255
    comments: str
    # Vdom type (traffic, lan-extension or admin). | Default: traffic
    vdom_type: Literal["traffic", "lan-extension", "admin"]
    # Controller IP address or FQDN to connect. | MaxLen: 255
    lan_extension_controller_addr: str
    # Controller port to connect. | Default: 5246 | Min: 1024 | Max: 65535
    lan_extension_controller_port: int
    # Firewall operation mode (NAT or Transparent). | Default: nat
    opmode: Literal["nat", "transparent"]
    # Next Generation Firewall (NGFW) mode. | Default: profile-based
    ngfw_mode: Literal["profile-based", "policy-based"]
    # Offload HTTP traffic to FortiWeb or FortiCache. | Default: fortiweb
    http_external_dest: Literal["fortiweb", "forticache"]
    # Select how to manage sessions affected by firewall policy co | Default: check-all
    firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"]
    # Transparent mode IPv4 management IP address and netmask.
    manageip: str
    # Transparent mode IPv4 default gateway IP address. | Default: 0.0.0.0
    gateway: str
    # IP address and netmask. | Default: 0.0.0.0 0.0.0.0
    ip: str
    # Transparent mode IPv6 management IP address and netmask. | Default: ::/0
    manageip6: str
    # Transparent mode IPv6 default gateway IP address. | Default: ::
    gateway6: str
    # IPv6 address prefix for NAT mode. | Default: ::/0
    ip6: str
    # Interface to use for management access for NAT mode. | MaxLen: 35
    device: str
    # Enable/disable Bi-directional Forwarding Detection (BFD) on | Default: disable
    bfd: Literal["enable", "disable"]
    # BFD desired minimal transmit interval | Default: 250 | Min: 1 | Max: 100000
    bfd_desired_min_tx: int
    # BFD required minimal receive interval | Default: 250 | Min: 1 | Max: 100000
    bfd_required_min_rx: int
    # BFD detection multiplier (1 - 50, default = 3). | Default: 3 | Min: 1 | Max: 50
    bfd_detect_mult: int
    # Enable to not enforce verifying the source port of BFD Packe | Default: disable
    bfd_dont_enforce_src_port: Literal["enable", "disable"]
    # Enable/disable converting antispam tags to UTF-8 for better | Default: enable
    utf8_spam_tagging: Literal["enable", "disable"]
    # Enable/disable WCCP cache engine. | Default: disable
    wccp_cache_engine: Literal["enable", "disable"]
    # Enable/disable periodic VPN log statistics for one or more t | Default: ipsec pptp l2tp ssl
    vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"]
    # Period to send VPN log statistics (0 or 60 - 86400 sec). | Default: 600 | Min: 0 | Max: 4294967295
    vpn_stats_period: int
    # IPv4 Equal-cost multi-path (ECMP) routing and load balancing | Default: source-ip-based
    v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"]
    # Duration of MAC addresses in Transparent mode | Default: 300 | Min: 300 | Max: 8640000
    mac_ttl: int
    # Enable/disable checking for a matching policy each time hair | Default: disable
    fw_session_hairpin: Literal["enable", "disable"]
    # Enable/disable action to take on PRP trailer. | Default: disable
    prp_trailer_action: Literal["enable", "disable"]
    # Enable/disable source NAT (SNAT) for VIP hairpin traffic. | Default: enable
    snat_hairpin_traffic: Literal["enable", "disable"]
    # Enable/disable the DHCP Proxy. | Default: disable
    dhcp_proxy: Literal["enable", "disable"]
    # Specify how to select outgoing interface to reach server. | Default: auto
    dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    dhcp_proxy_interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    dhcp_proxy_vrf_select: int
    # DHCP Server IPv4 address.
    dhcp_server_ip: list[dict[str, Any]]
    # DHCPv6 server IPv6 address.
    dhcp6_server_ip: list[dict[str, Any]]
    # Enable/disable central NAT. | Default: disable
    central_nat: Literal["enable", "disable"]
    # Default columns to display for policy lists on GUI.
    gui_default_policy_columns: list[SettingsGuidefaultpolicycolumnsObject]
    # Enable/disable Link Layer Discovery Protocol (LLDP) receptio | Default: global
    lldp_reception: Literal["enable", "disable", "global"]
    # Enable/disable Link Layer Discovery Protocol (LLDP) transmis | Default: global
    lldp_transmission: Literal["enable", "disable", "global"]
    # Enable/disable link down access traffic. | Default: enable
    link_down_access: Literal["enable", "disable"]
    # Enable/disable NAT46 IPv6 fragment header generation. | Default: disable
    nat46_generate_ipv6_fragment_header: Literal["enable", "disable"]
    # Enable/disable mandatory IPv4 packet forwarding in NAT46. | Default: disable
    nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"]
    # Enable/disable mandatory IPv6 packet forwarding in NAT64. | Default: enable
    nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"]
    # Enable/disable detection of unknown ESP packets | Default: enable
    detect_unknown_esp: Literal["enable", "disable"]
    # Force the intree session to always use the best route. | Default: disable
    intree_ses_best_route: Literal["force", "disable"]
    # Enable/disable auxiliary session. | Default: disable
    auxiliary_session: Literal["enable", "disable"]
    # Enable/disable IPv4 asymmetric routing. | Default: disable
    asymroute: Literal["enable", "disable"]
    # Enable/disable ICMP asymmetric routing. | Default: disable
    asymroute_icmp: Literal["enable", "disable"]
    # Enable/disable allowing TCP session without SYN flags. | Default: disable
    tcp_session_without_syn: Literal["enable", "disable"]
    # Enable/disable including denied session in the session table | Default: disable
    ses_denied_traffic: Literal["enable", "disable"]
    # Enable/disable including denied multicast session in the ses | Default: disable
    ses_denied_multicast_traffic: Literal["enable", "disable"]
    # Enable/disable strict source verification. | Default: disable
    strict_src_check: Literal["enable", "disable"]
    # Enable/disable link down path. | Default: disable
    allow_linkdown_path: Literal["enable", "disable"]
    # Enable/disable asymmetric IPv6 routing. | Default: disable
    asymroute6: Literal["enable", "disable"]
    # Enable/disable asymmetric ICMPv6 routing. | Default: disable
    asymroute6_icmp: Literal["enable", "disable"]
    # Enable/disable SCTP session creation without SCTP INIT. | Default: disable
    sctp_session_without_init: Literal["enable", "disable"]
    # Enable/disable the SIP kernel session helper to create an ex | Default: disable
    sip_expectation: Literal["enable", "disable"]
    # Enable/disable recording the original SIP source IP address | Default: enable
    sip_nat_trace: Literal["enable", "disable"]
    # Enable/disable H323 direct model. | Default: disable
    h323_direct_model: Literal["disable", "enable"]
    # Enable/disable this VDOM. | Default: enable
    status: Literal["enable", "disable"]
    # TCP port the SIP proxy monitors for SIP traffic | Default: 5060 | Min: 1 | Max: 65535
    sip_tcp_port: int
    # UDP port the SIP proxy monitors for SIP traffic | Default: 5060 | Min: 1 | Max: 65535
    sip_udp_port: int
    # TCP port the SIP proxy monitors for SIP SSL/TLS traffic | Default: 5061 | Min: 0 | Max: 65535
    sip_ssl_port: int
    # TCP port the SCCP proxy monitors for SCCP traffic | Default: 2000 | Min: 0 | Max: 65535
    sccp_port: int
    # Enable/disable multicast forwarding. | Default: enable
    multicast_forward: Literal["enable", "disable"]
    # Enable/disable preventing the FortiGate from changing the TT | Default: disable
    multicast_ttl_notchange: Literal["enable", "disable"]
    # Enable/disable allowing multicast traffic through the FortiG | Default: disable
    multicast_skip_policy: Literal["enable", "disable"]
    # Enable/disable allowing interface subnets to use overlapping | Default: disable
    allow_subnet_overlap: Literal["enable", "disable"]
    # Enable/disable denying TCP by sending an ICMP communication | Default: disable
    deny_tcp_with_icmp: Literal["enable", "disable"]
    # Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Se | Default: 255 | Min: 1 | Max: 255
    ecmp_max_paths: int
    # Timeout for discovered devices (1 - 365 days, default = 28). | Default: 28 | Min: 1 | Max: 365
    discovered_device_timeout: int
    # Enable/disable using DNS to validate email addresses collect | Default: enable
    email_portal_check_dns: Literal["disable", "enable"]
    # Configure how the FortiGate handles VoIP traffic when a poli | Default: proxy-based
    default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"]
    # Enable/disable ICAP on the GUI. | Default: disable
    gui_icap: Literal["enable", "disable"]
    # Enable/disable implicit firewall policies on the GUI. | Default: enable
    gui_implicit_policy: Literal["enable", "disable"]
    # Enable/disable DNS database settings on the GUI. | Default: disable
    gui_dns_database: Literal["enable", "disable"]
    # Enable/disable server load balancing on the GUI. | Default: disable
    gui_load_balance: Literal["enable", "disable"]
    # Enable/disable multicast firewall policies on the GUI. | Default: disable
    gui_multicast_policy: Literal["enable", "disable"]
    # Enable/disable DoS policies on the GUI. | Default: enable
    gui_dos_policy: Literal["enable", "disable"]
    # Enable/disable object colors on the GUI. | Default: enable
    gui_object_colors: Literal["enable", "disable"]
    # Enable/disable route-tag addresses on the GUI. | Default: disable
    gui_route_tag_address_creation: Literal["enable", "disable"]
    # Enable/disable VoIP profiles on the GUI. | Default: disable
    gui_voip_profile: Literal["enable", "disable"]
    # Enable/disable FortiAP profiles on the GUI. | Default: enable
    gui_ap_profile: Literal["enable", "disable"]
    # Enable/disable Security Profile Groups on the GUI. | Default: disable
    gui_security_profile_group: Literal["enable", "disable"]
    # Enable/disable Local-In policies on the GUI. | Default: disable
    gui_local_in_policy: Literal["enable", "disable"]
    # Enable/disable WAN Optimization and Web Caching on the GUI. | Default: disable
    gui_wanopt_cache: Literal["enable", "disable"]
    # Enable/disable the explicit proxy on the GUI. | Default: disable
    gui_explicit_proxy: Literal["enable", "disable"]
    # Enable/disable dynamic routing on the GUI. | Default: enable
    gui_dynamic_routing: Literal["enable", "disable"]
    # Enable/disable SSL-VPN personal bookmark management on the G | Default: disable
    gui_sslvpn_personal_bookmarks: Literal["enable", "disable"]
    # Enable/disable SSL-VPN realms on the GUI. | Default: disable
    gui_sslvpn_realms: Literal["enable", "disable"]
    # Enable/disable policy-based IPsec VPN on the GUI. | Default: disable
    gui_policy_based_ipsec: Literal["enable", "disable"]
    # Enable/disable threat weight on the GUI. | Default: enable
    gui_threat_weight: Literal["enable", "disable"]
    # Enable/disable Antispam on the GUI. | Default: disable
    gui_spamfilter: Literal["enable", "disable"]
    # Enable/disable File-filter on the GUI. | Default: enable
    gui_file_filter: Literal["enable", "disable"]
    # Enable/disable application control on the GUI. | Default: enable
    gui_application_control: Literal["enable", "disable"]
    # Enable/disable IPS on the GUI. | Default: enable
    gui_ips: Literal["enable", "disable"]
    # Enable/disable advanced DHCP options on the GUI. | Default: enable
    gui_dhcp_advanced: Literal["enable", "disable"]
    # Enable/disable IPsec VPN settings pages on the GUI. | Default: enable
    gui_vpn: Literal["enable", "disable"]
    # Enable/disable SSL-VPN settings pages on the GUI. | Default: disable
    gui_sslvpn: Literal["enable", "disable"]
    # Enable/disable the wireless controller on the GUI. | Default: enable
    gui_wireless_controller: Literal["enable", "disable"]
    # Enable/disable advanced wireless features in GUI. | Default: disable
    gui_advanced_wireless_features: Literal["enable", "disable"]
    # Enable/disable the switch controller on the GUI. | Default: enable
    gui_switch_controller: Literal["enable", "disable"]
    # Enable/disable FortiAP split tunneling on the GUI. | Default: disable
    gui_fortiap_split_tunneling: Literal["enable", "disable"]
    # Enable/disable advanced web filtering on the GUI. | Default: disable
    gui_webfilter_advanced: Literal["enable", "disable"]
    # Enable/disable traffic shaping on the GUI. | Default: enable
    gui_traffic_shaping: Literal["enable", "disable"]
    # Enable/disable SD-WAN on the GUI. | Default: enable
    gui_wan_load_balancing: Literal["enable", "disable"]
    # Enable/disable AntiVirus on the GUI. | Default: enable
    gui_antivirus: Literal["enable", "disable"]
    # Enable/disable Web filtering on the GUI. | Default: enable
    gui_webfilter: Literal["enable", "disable"]
    # Enable/disable Video filtering on the GUI. | Default: enable
    gui_videofilter: Literal["enable", "disable"]
    # Enable/disable DNS Filtering on the GUI. | Default: enable
    gui_dnsfilter: Literal["enable", "disable"]
    # Enable/disable Web Application Firewall on the GUI. | Default: disable
    gui_waf_profile: Literal["enable", "disable"]
    # Enable/disable Data Loss Prevention on the GUI. | Default: disable
    gui_dlp_profile: Literal["enable", "disable"]
    # Enable/disable Show advanced DLP expressions on the GUI. | Default: disable
    gui_dlp_advanced: Literal["enable", "disable"]
    # Enable/disable Virtual Patching on the GUI. | Default: disable
    gui_virtual_patch_profile: Literal["enable", "disable"]
    # Enable/disable Inline-CASB on the GUI. | Default: disable
    gui_casb: Literal["enable", "disable"]
    # Enable/disable FortiExtender on the GUI. | Default: disable
    gui_fortiextender_controller: Literal["enable", "disable"]
    # Enable/disable advanced policy configuration on the GUI. | Default: disable
    gui_advanced_policy: Literal["enable", "disable"]
    # Enable/disable the requirement for policy naming on the GUI. | Default: disable
    gui_allow_unnamed_policy: Literal["enable", "disable"]
    # Enable/disable email collection on the GUI. | Default: disable
    gui_email_collection: Literal["enable", "disable"]
    # Enable/disable adding multiple interfaces to a policy on the | Default: disable
    gui_multiple_interface_policy: Literal["enable", "disable"]
    # Enable/disable policy disclaimer on the GUI. | Default: disable
    gui_policy_disclaimer: Literal["enable", "disable"]
    # Enable/disable Zero Trust Network Access features on the GUI | Default: disable
    gui_ztna: Literal["enable", "disable"]
    # Enable/disable Operational technology features on the GUI. | Default: disable
    gui_ot: Literal["enable", "disable"]
    # Enable/disable Create dynamic addresses to manage known devi | Default: disable
    gui_dynamic_device_os_id: Literal["enable", "disable"]
    # Enable/disable Manage general radio packet service (GPRS) pr | Default: enable
    gui_gtp: Literal["enable", "disable"]
    # Local location ID in the form of an IPv4 address. | Default: 0.0.0.0
    location_id: str
    # Enable/disable IKEv2 session resumption (RFC 5723). | Default: disable
    ike_session_resume: Literal["enable", "disable"]
    # Enable/disable IKE quick crash detection (RFC 6290). | Default: disable
    ike_quick_crash_detect: Literal["enable", "disable"]
    # Configure IKE ASN.1 Distinguished Name format conventions. | Default: with-space
    ike_dn_format: Literal["with-space", "no-space"]
    # UDP port for IKE/IPsec traffic (default 500). | Default: 500 | Min: 1024 | Max: 65535
    ike_port: int
    # TCP port for IKE/IPsec traffic (default 443). | Default: 443 | Min: 1 | Max: 65535
    ike_tcp_port: int
    # Enable/disable IKE Policy Based Routing (PBR). | Default: disable
    ike_policy_route: Literal["enable", "disable"]
    # Enable/disable detail log for IKE events. | Default: disable
    ike_detailed_event_logs: Literal["disable", "enable"]
    # Enable/disable blocking of land attacks. | Default: disable
    block_land_attack: Literal["disable", "enable"]
    # Enable/disable policy service enforcement based on applicati | Default: enable
    default_app_port_as_service: Literal["enable", "disable"]
    # Enable/disable dirty session check caused by FQDN updates. | Default: disable
    fqdn_session_check: Literal["enable", "disable"]
    # Enable/disable dirty session check caused by external resour | Default: disable
    ext_resource_session_check: Literal["enable", "disable"]
    # Enable/disable dirty session check caused by dynamic address | Default: disable
    dyn_addr_session_check: Literal["enable", "disable"]
    # Default policy expiry in days (0 - 365 days, default = 30). | Default: 30 | Min: 0 | Max: 365
    default_policy_expiry_days: int
    # Enforce change summaries for select tables in the GUI. | Default: require
    gui_enforce_change_summary: Literal["disable", "require", "optional"]
    # Enable/disable Internet Service database caching. | Default: disable
    internet_service_database_cache: Literal["disable", "enable"]
    # Maximum number of tuple entries | Default: 32768 | Min: 0 | Max: 4294967295
    internet_service_app_ctrl_size: int
    
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
    def to_dict(self) -> SettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Settings:
    """
    Configure VDOM settings.
    
    Path: system/settings
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingsPayload | None = ...,
        comments: str | None = ...,
        vdom_type: Literal["traffic", "lan-extension", "admin"] | None = ...,
        lan_extension_controller_addr: str | None = ...,
        lan_extension_controller_port: int | None = ...,
        opmode: Literal["nat", "transparent"] | None = ...,
        ngfw_mode: Literal["profile-based", "policy-based"] | None = ...,
        http_external_dest: Literal["fortiweb", "forticache"] | None = ...,
        firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = ...,
        manageip: str | None = ...,
        gateway: str | None = ...,
        ip: str | None = ...,
        manageip6: str | None = ...,
        gateway6: str | None = ...,
        ip6: str | None = ...,
        device: str | None = ...,
        bfd: Literal["enable", "disable"] | None = ...,
        bfd_desired_min_tx: int | None = ...,
        bfd_required_min_rx: int | None = ...,
        bfd_detect_mult: int | None = ...,
        bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = ...,
        utf8_spam_tagging: Literal["enable", "disable"] | None = ...,
        wccp_cache_engine: Literal["enable", "disable"] | None = ...,
        vpn_stats_log: Literal["ipsec", "pptp", "l2tp", "ssl"] | list[str] | None = ...,
        vpn_stats_period: int | None = ...,
        v4_ecmp_mode: Literal["source-ip-based", "weight-based", "usage-based", "source-dest-ip-based"] | None = ...,
        mac_ttl: int | None = ...,
        fw_session_hairpin: Literal["enable", "disable"] | None = ...,
        prp_trailer_action: Literal["enable", "disable"] | None = ...,
        snat_hairpin_traffic: Literal["enable", "disable"] | None = ...,
        dhcp_proxy: Literal["enable", "disable"] | None = ...,
        dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        dhcp_proxy_interface: str | None = ...,
        dhcp_proxy_vrf_select: int | None = ...,
        dhcp_server_ip: str | list[str] | None = ...,
        dhcp6_server_ip: str | list[str] | None = ...,
        central_nat: Literal["enable", "disable"] | None = ...,
        gui_default_policy_columns: str | list[str] | list[dict[str, Any]] | None = ...,
        lldp_reception: Literal["enable", "disable", "global"] | None = ...,
        lldp_transmission: Literal["enable", "disable", "global"] | None = ...,
        link_down_access: Literal["enable", "disable"] | None = ...,
        nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = ...,
        nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = ...,
        nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = ...,
        detect_unknown_esp: Literal["enable", "disable"] | None = ...,
        intree_ses_best_route: Literal["force", "disable"] | None = ...,
        auxiliary_session: Literal["enable", "disable"] | None = ...,
        asymroute: Literal["enable", "disable"] | None = ...,
        asymroute_icmp: Literal["enable", "disable"] | None = ...,
        tcp_session_without_syn: Literal["enable", "disable"] | None = ...,
        ses_denied_traffic: Literal["enable", "disable"] | None = ...,
        ses_denied_multicast_traffic: Literal["enable", "disable"] | None = ...,
        strict_src_check: Literal["enable", "disable"] | None = ...,
        allow_linkdown_path: Literal["enable", "disable"] | None = ...,
        asymroute6: Literal["enable", "disable"] | None = ...,
        asymroute6_icmp: Literal["enable", "disable"] | None = ...,
        sctp_session_without_init: Literal["enable", "disable"] | None = ...,
        sip_expectation: Literal["enable", "disable"] | None = ...,
        sip_nat_trace: Literal["enable", "disable"] | None = ...,
        h323_direct_model: Literal["disable", "enable"] | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        sip_tcp_port: int | list[int] | None = ...,
        sip_udp_port: int | list[int] | None = ...,
        sip_ssl_port: int | None = ...,
        sccp_port: int | None = ...,
        multicast_forward: Literal["enable", "disable"] | None = ...,
        multicast_ttl_notchange: Literal["enable", "disable"] | None = ...,
        multicast_skip_policy: Literal["enable", "disable"] | None = ...,
        allow_subnet_overlap: Literal["enable", "disable"] | None = ...,
        deny_tcp_with_icmp: Literal["enable", "disable"] | None = ...,
        ecmp_max_paths: int | None = ...,
        discovered_device_timeout: int | None = ...,
        email_portal_check_dns: Literal["disable", "enable"] | None = ...,
        default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = ...,
        gui_icap: Literal["enable", "disable"] | None = ...,
        gui_implicit_policy: Literal["enable", "disable"] | None = ...,
        gui_dns_database: Literal["enable", "disable"] | None = ...,
        gui_load_balance: Literal["enable", "disable"] | None = ...,
        gui_multicast_policy: Literal["enable", "disable"] | None = ...,
        gui_dos_policy: Literal["enable", "disable"] | None = ...,
        gui_object_colors: Literal["enable", "disable"] | None = ...,
        gui_route_tag_address_creation: Literal["enable", "disable"] | None = ...,
        gui_voip_profile: Literal["enable", "disable"] | None = ...,
        gui_ap_profile: Literal["enable", "disable"] | None = ...,
        gui_security_profile_group: Literal["enable", "disable"] | None = ...,
        gui_local_in_policy: Literal["enable", "disable"] | None = ...,
        gui_wanopt_cache: Literal["enable", "disable"] | None = ...,
        gui_explicit_proxy: Literal["enable", "disable"] | None = ...,
        gui_dynamic_routing: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = ...,
        gui_sslvpn_realms: Literal["enable", "disable"] | None = ...,
        gui_policy_based_ipsec: Literal["enable", "disable"] | None = ...,
        gui_threat_weight: Literal["enable", "disable"] | None = ...,
        gui_spamfilter: Literal["enable", "disable"] | None = ...,
        gui_file_filter: Literal["enable", "disable"] | None = ...,
        gui_application_control: Literal["enable", "disable"] | None = ...,
        gui_ips: Literal["enable", "disable"] | None = ...,
        gui_dhcp_advanced: Literal["enable", "disable"] | None = ...,
        gui_vpn: Literal["enable", "disable"] | None = ...,
        gui_sslvpn: Literal["enable", "disable"] | None = ...,
        gui_wireless_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_wireless_features: Literal["enable", "disable"] | None = ...,
        gui_switch_controller: Literal["enable", "disable"] | None = ...,
        gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = ...,
        gui_webfilter_advanced: Literal["enable", "disable"] | None = ...,
        gui_traffic_shaping: Literal["enable", "disable"] | None = ...,
        gui_wan_load_balancing: Literal["enable", "disable"] | None = ...,
        gui_antivirus: Literal["enable", "disable"] | None = ...,
        gui_webfilter: Literal["enable", "disable"] | None = ...,
        gui_videofilter: Literal["enable", "disable"] | None = ...,
        gui_dnsfilter: Literal["enable", "disable"] | None = ...,
        gui_waf_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_profile: Literal["enable", "disable"] | None = ...,
        gui_dlp_advanced: Literal["enable", "disable"] | None = ...,
        gui_virtual_patch_profile: Literal["enable", "disable"] | None = ...,
        gui_casb: Literal["enable", "disable"] | None = ...,
        gui_fortiextender_controller: Literal["enable", "disable"] | None = ...,
        gui_advanced_policy: Literal["enable", "disable"] | None = ...,
        gui_allow_unnamed_policy: Literal["enable", "disable"] | None = ...,
        gui_email_collection: Literal["enable", "disable"] | None = ...,
        gui_multiple_interface_policy: Literal["enable", "disable"] | None = ...,
        gui_policy_disclaimer: Literal["enable", "disable"] | None = ...,
        gui_ztna: Literal["enable", "disable"] | None = ...,
        gui_ot: Literal["enable", "disable"] | None = ...,
        gui_dynamic_device_os_id: Literal["enable", "disable"] | None = ...,
        gui_gtp: Literal["enable", "disable"] | None = ...,
        location_id: str | None = ...,
        ike_session_resume: Literal["enable", "disable"] | None = ...,
        ike_quick_crash_detect: Literal["enable", "disable"] | None = ...,
        ike_dn_format: Literal["with-space", "no-space"] | None = ...,
        ike_port: int | None = ...,
        ike_tcp_port: int | None = ...,
        ike_policy_route: Literal["enable", "disable"] | None = ...,
        ike_detailed_event_logs: Literal["disable", "enable"] | None = ...,
        block_land_attack: Literal["disable", "enable"] | None = ...,
        default_app_port_as_service: Literal["enable", "disable"] | None = ...,
        fqdn_session_check: Literal["enable", "disable"] | None = ...,
        ext_resource_session_check: Literal["enable", "disable"] | None = ...,
        dyn_addr_session_check: Literal["enable", "disable"] | None = ...,
        default_policy_expiry_days: int | None = ...,
        gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = ...,
        internet_service_database_cache: Literal["disable", "enable"] | None = ...,
        internet_service_app_ctrl_size: int | None = ...,
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
    "Settings",
    "SettingsPayload",
    "SettingsResponse",
    "SettingsObject",
]
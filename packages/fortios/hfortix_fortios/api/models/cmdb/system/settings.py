"""
Pydantic Models for CMDB - system/settings

Runtime validation models for system/settings configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SettingsGuiDefaultPolicyColumns(BaseModel):
    """
    Child table model for gui-default-policy-columns.
    
    Default columns to display for policy lists on GUI.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Select column name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingsVpn_stats_logEnum(str, Enum):
    """Allowed values for vpn_stats_log field."""
    IPSEC = "ipsec"    PPTP = "pptp"    L2TP = "l2tp"    SSL = "ssl"
class SettingsV4_ecmp_modeEnum(str, Enum):
    """Allowed values for v4_ecmp_mode field."""
    SOURCE_IP_BASED = "source-ip-based"    WEIGHT_BASED = "weight-based"    USAGE_BASED = "usage-based"    SOURCE_DEST_IP_BASED = "source-dest-ip-based"

# ============================================================================
# Main Model
# ============================================================================

class SettingsModel(BaseModel):
    """
    Pydantic model for system/settings configuration.
    
    Configure VDOM settings.
    
    Validation Rules:        - comments: max_length=255 pattern=        - vdom_type: pattern=        - lan_extension_controller_addr: max_length=255 pattern=        - lan_extension_controller_port: min=1024 max=65535 pattern=        - opmode: pattern=        - ngfw_mode: pattern=        - http_external_dest: pattern=        - firewall_session_dirty: pattern=        - manageip: pattern=        - gateway: pattern=        - ip: pattern=        - manageip6: pattern=        - gateway6: pattern=        - ip6: pattern=        - device: max_length=35 pattern=        - bfd: pattern=        - bfd_desired_min_tx: min=1 max=100000 pattern=        - bfd_required_min_rx: min=1 max=100000 pattern=        - bfd_detect_mult: min=1 max=50 pattern=        - bfd_dont_enforce_src_port: pattern=        - utf8_spam_tagging: pattern=        - wccp_cache_engine: pattern=        - vpn_stats_log: pattern=        - vpn_stats_period: min=0 max=4294967295 pattern=        - v4_ecmp_mode: pattern=        - mac_ttl: min=300 max=8640000 pattern=        - fw_session_hairpin: pattern=        - prp_trailer_action: pattern=        - snat_hairpin_traffic: pattern=        - dhcp_proxy: pattern=        - dhcp_proxy_interface_select_method: pattern=        - dhcp_proxy_interface: max_length=15 pattern=        - dhcp_proxy_vrf_select: min=0 max=511 pattern=        - dhcp_server_ip: pattern=        - dhcp6_server_ip: pattern=        - central_nat: pattern=        - gui_default_policy_columns: pattern=        - lldp_reception: pattern=        - lldp_transmission: pattern=        - link_down_access: pattern=        - nat46_generate_ipv6_fragment_header: pattern=        - nat46_force_ipv4_packet_forwarding: pattern=        - nat64_force_ipv6_packet_forwarding: pattern=        - detect_unknown_esp: pattern=        - intree_ses_best_route: pattern=        - auxiliary_session: pattern=        - asymroute: pattern=        - asymroute_icmp: pattern=        - tcp_session_without_syn: pattern=        - ses_denied_traffic: pattern=        - ses_denied_multicast_traffic: pattern=        - strict_src_check: pattern=        - allow_linkdown_path: pattern=        - asymroute6: pattern=        - asymroute6_icmp: pattern=        - sctp_session_without_init: pattern=        - sip_expectation: pattern=        - sip_nat_trace: pattern=        - h323_direct_model: pattern=        - status: pattern=        - sip_tcp_port: min=1 max=65535 pattern=        - sip_udp_port: min=1 max=65535 pattern=        - sip_ssl_port: min=0 max=65535 pattern=        - sccp_port: min=0 max=65535 pattern=        - multicast_forward: pattern=        - multicast_ttl_notchange: pattern=        - multicast_skip_policy: pattern=        - allow_subnet_overlap: pattern=        - deny_tcp_with_icmp: pattern=        - ecmp_max_paths: min=1 max=255 pattern=        - discovered_device_timeout: min=1 max=365 pattern=        - email_portal_check_dns: pattern=        - default_voip_alg_mode: pattern=        - gui_icap: pattern=        - gui_implicit_policy: pattern=        - gui_dns_database: pattern=        - gui_load_balance: pattern=        - gui_multicast_policy: pattern=        - gui_dos_policy: pattern=        - gui_object_colors: pattern=        - gui_route_tag_address_creation: pattern=        - gui_voip_profile: pattern=        - gui_ap_profile: pattern=        - gui_security_profile_group: pattern=        - gui_local_in_policy: pattern=        - gui_wanopt_cache: pattern=        - gui_explicit_proxy: pattern=        - gui_dynamic_routing: pattern=        - gui_sslvpn_personal_bookmarks: pattern=        - gui_sslvpn_realms: pattern=        - gui_policy_based_ipsec: pattern=        - gui_threat_weight: pattern=        - gui_spamfilter: pattern=        - gui_file_filter: pattern=        - gui_application_control: pattern=        - gui_ips: pattern=        - gui_dhcp_advanced: pattern=        - gui_vpn: pattern=        - gui_sslvpn: pattern=        - gui_wireless_controller: pattern=        - gui_advanced_wireless_features: pattern=        - gui_switch_controller: pattern=        - gui_fortiap_split_tunneling: pattern=        - gui_webfilter_advanced: pattern=        - gui_traffic_shaping: pattern=        - gui_wan_load_balancing: pattern=        - gui_antivirus: pattern=        - gui_webfilter: pattern=        - gui_videofilter: pattern=        - gui_dnsfilter: pattern=        - gui_waf_profile: pattern=        - gui_dlp_profile: pattern=        - gui_dlp_advanced: pattern=        - gui_virtual_patch_profile: pattern=        - gui_casb: pattern=        - gui_fortiextender_controller: pattern=        - gui_advanced_policy: pattern=        - gui_allow_unnamed_policy: pattern=        - gui_email_collection: pattern=        - gui_multiple_interface_policy: pattern=        - gui_policy_disclaimer: pattern=        - gui_ztna: pattern=        - gui_ot: pattern=        - gui_dynamic_device_os_id: pattern=        - gui_gtp: pattern=        - location_id: pattern=        - ike_session_resume: pattern=        - ike_quick_crash_detect: pattern=        - ike_dn_format: pattern=        - ike_port: min=1024 max=65535 pattern=        - ike_tcp_port: min=1 max=65535 pattern=        - ike_policy_route: pattern=        - ike_detailed_event_logs: pattern=        - block_land_attack: pattern=        - default_app_port_as_service: pattern=        - fqdn_session_check: pattern=        - ext_resource_session_check: pattern=        - dyn_addr_session_check: pattern=        - default_policy_expiry_days: min=0 max=365 pattern=        - gui_enforce_change_summary: pattern=        - internet_service_database_cache: pattern=        - internet_service_app_ctrl_size: min=0 max=4294967295 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    comments: str | None = Field(max_length=255, default=None, description="VDOM comments.")    
    vdom_type: Literal["traffic", "lan-extension", "admin"] = Field(default="traffic", description="Vdom type (traffic, lan-extension or admin).")    
    lan_extension_controller_addr: str | None = Field(max_length=255, default="", description="Controller IP address or FQDN to connect.")    
    lan_extension_controller_port: int | None = Field(ge=1024, le=65535, default=5246, description="Controller port to connect.")    
    opmode: Literal["nat", "transparent"] = Field(default="nat", description="Firewall operation mode (NAT or Transparent).")    
    ngfw_mode: Literal["profile-based", "policy-based"] | None = Field(default="profile-based", description="Next Generation Firewall (NGFW) mode.")    
    http_external_dest: Literal["fortiweb", "forticache"] | None = Field(default="fortiweb", description="Offload HTTP traffic to FortiWeb or FortiCache.")    
    firewall_session_dirty: Literal["check-all", "check-new", "check-policy-option"] | None = Field(default="check-all", description="Select how to manage sessions affected by firewall policy configuration changes.")    
    manageip: str = Field(default="", description="Transparent mode IPv4 management IP address and netmask.")    
    gateway: str | None = Field(default="0.0.0.0", description="Transparent mode IPv4 default gateway IP address.")    
    ip: Any = Field(default="0.0.0.0 0.0.0.0", description="IP address and netmask.")    
    manageip6: str | None = Field(default="::/0", description="Transparent mode IPv6 management IP address and netmask.")    
    gateway6: str | None = Field(default="::", description="Transparent mode IPv6 default gateway IP address.")    
    ip6: str | None = Field(default="::/0", description="IPv6 address prefix for NAT mode.")    
    device: str = Field(max_length=35, default="", description="Interface to use for management access for NAT mode.")  # datasource: ['system.interface.name']    
    bfd: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Bi-directional Forwarding Detection (BFD) on all interfaces.")    
    bfd_desired_min_tx: int | None = Field(ge=1, le=100000, default=250, description="BFD desired minimal transmit interval (1 - 100000 ms, default = 250).")    
    bfd_required_min_rx: int | None = Field(ge=1, le=100000, default=250, description="BFD required minimal receive interval (1 - 100000 ms, default = 250).")    
    bfd_detect_mult: int | None = Field(ge=1, le=50, default=3, description="BFD detection multiplier (1 - 50, default = 3).")    
    bfd_dont_enforce_src_port: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to not enforce verifying the source port of BFD Packets.")    
    utf8_spam_tagging: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable converting antispam tags to UTF-8 for better non-ASCII character support.")    
    wccp_cache_engine: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WCCP cache engine.")    
    vpn_stats_log: list[VpnStatsLog] = Field(default="ipsec pptp l2tp ssl", description="Enable/disable periodic VPN log statistics for one or more types of VPN. Separate names with a space.")    
    vpn_stats_period: int | None = Field(ge=0, le=4294967295, default=600, description="Period to send VPN log statistics (0 or 60 - 86400 sec).")    
    v4_ecmp_mode: V4EcmpModeEnum | None = Field(default="source-ip-based", description="IPv4 Equal-cost multi-path (ECMP) routing and load balancing mode.")    
    mac_ttl: int | None = Field(ge=300, le=8640000, default=300, description="Duration of MAC addresses in Transparent mode (300 - 8640000 sec, default = 300).")    
    fw_session_hairpin: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable checking for a matching policy each time hairpin traffic goes through the FortiGate.")    
    prp_trailer_action: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable action to take on PRP trailer.")    
    snat_hairpin_traffic: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable source NAT (SNAT) for VIP hairpin traffic.")    
    dhcp_proxy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the DHCP Proxy.")    
    dhcp_proxy_interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    dhcp_proxy_interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    dhcp_proxy_vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    dhcp_server_ip: list[DhcpServerIp] = Field(default="", description="DHCP Server IPv4 address.")    
    dhcp6_server_ip: list[Dhcp6ServerIp] = Field(default="", description="DHCPv6 server IPv6 address.")    
    central_nat: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable central NAT.")    
    gui_default_policy_columns: list[GuiDefaultPolicyColumns] = Field(default=None, description="Default columns to display for policy lists on GUI.")    
    lldp_reception: Literal["enable", "disable", "global"] | None = Field(default="global", description="Enable/disable Link Layer Discovery Protocol (LLDP) reception for this VDOM or apply global settings to this VDOM.")    
    lldp_transmission: Literal["enable", "disable", "global"] | None = Field(default="global", description="Enable/disable Link Layer Discovery Protocol (LLDP) transmission for this VDOM or apply global settings to this VDOM.")    
    link_down_access: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable link down access traffic.")    
    nat46_generate_ipv6_fragment_header: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT46 IPv6 fragment header generation.")    
    nat46_force_ipv4_packet_forwarding: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable mandatory IPv4 packet forwarding in NAT46.")    
    nat64_force_ipv6_packet_forwarding: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable mandatory IPv6 packet forwarding in NAT64.")    
    detect_unknown_esp: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable detection of unknown ESP packets (default = enable).")    
    intree_ses_best_route: Literal["force", "disable"] | None = Field(default="disable", description="Force the intree session to always use the best route.")    
    auxiliary_session: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable auxiliary session.")    
    asymroute: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv4 asymmetric routing.")    
    asymroute_icmp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable ICMP asymmetric routing.")    
    tcp_session_without_syn: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowing TCP session without SYN flags.")    
    ses_denied_traffic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable including denied session in the session table.")    
    ses_denied_multicast_traffic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable including denied multicast session in the session table.")    
    strict_src_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable strict source verification.")    
    allow_linkdown_path: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable link down path.")    
    asymroute6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable asymmetric IPv6 routing.")    
    asymroute6_icmp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable asymmetric ICMPv6 routing.")    
    sctp_session_without_init: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SCTP session creation without SCTP INIT.")    
    sip_expectation: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the SIP kernel session helper to create an expectation for port 5060.")    
    sip_nat_trace: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable recording the original SIP source IP address when NAT is used.")    
    h323_direct_model: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable H323 direct model.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this VDOM.")    
    sip_tcp_port: list[SipTcpPort] = Field(ge=1, le=65535, default=5060, description="TCP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).")    
    sip_udp_port: list[SipUdpPort] = Field(ge=1, le=65535, default=5060, description="UDP port the SIP proxy monitors for SIP traffic (0 - 65535, default = 5060).")    
    sip_ssl_port: int | None = Field(ge=0, le=65535, default=5061, description="TCP port the SIP proxy monitors for SIP SSL/TLS traffic (0 - 65535, default = 5061).")    
    sccp_port: int | None = Field(ge=0, le=65535, default=2000, description="TCP port the SCCP proxy monitors for SCCP traffic (0 - 65535, default = 2000).")    
    multicast_forward: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable multicast forwarding.")    
    multicast_ttl_notchange: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable preventing the FortiGate from changing the TTL for forwarded multicast packets.")    
    multicast_skip_policy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowing multicast traffic through the FortiGate without a policy check.")    
    allow_subnet_overlap: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowing interface subnets to use overlapping IP addresses.")    
    deny_tcp_with_icmp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable denying TCP by sending an ICMP communication prohibited packet.")    
    ecmp_max_paths: int | None = Field(ge=1, le=255, default=255, description="Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Set to 1 to disable ECMP routing (1 - 255, default = 255).")    
    discovered_device_timeout: int | None = Field(ge=1, le=365, default=28, description="Timeout for discovered devices (1 - 365 days, default = 28).")    
    email_portal_check_dns: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable using DNS to validate email addresses collected by a captive portal.")    
    default_voip_alg_mode: Literal["proxy-based", "kernel-helper-based"] | None = Field(default="proxy-based", description="Configure how the FortiGate handles VoIP traffic when a policy that accepts the traffic doesn't include a VoIP profile.")    
    gui_icap: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable ICAP on the GUI.")    
    gui_implicit_policy: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable implicit firewall policies on the GUI.")    
    gui_dns_database: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DNS database settings on the GUI.")    
    gui_load_balance: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable server load balancing on the GUI.")    
    gui_multicast_policy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable multicast firewall policies on the GUI.")    
    gui_dos_policy: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable DoS policies on the GUI.")    
    gui_object_colors: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable object colors on the GUI.")    
    gui_route_tag_address_creation: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable route-tag addresses on the GUI.")    
    gui_voip_profile: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable VoIP profiles on the GUI.")    
    gui_ap_profile: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiAP profiles on the GUI.")    
    gui_security_profile_group: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Security Profile Groups on the GUI.")    
    gui_local_in_policy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Local-In policies on the GUI.")    
    gui_wanopt_cache: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WAN Optimization and Web Caching on the GUI.")    
    gui_explicit_proxy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the explicit proxy on the GUI.")    
    gui_dynamic_routing: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable dynamic routing on the GUI.")    
    gui_sslvpn_personal_bookmarks: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SSL-VPN personal bookmark management on the GUI.")    
    gui_sslvpn_realms: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SSL-VPN realms on the GUI.")    
    gui_policy_based_ipsec: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable policy-based IPsec VPN on the GUI.")    
    gui_threat_weight: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable threat weight on the GUI.")    
    gui_spamfilter: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Antispam on the GUI.")    
    gui_file_filter: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable File-filter on the GUI.")    
    gui_application_control: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable application control on the GUI.")    
    gui_ips: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IPS on the GUI.")    
    gui_dhcp_advanced: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable advanced DHCP options on the GUI.")    
    gui_vpn: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IPsec VPN settings pages on the GUI.")    
    gui_sslvpn: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SSL-VPN settings pages on the GUI.")    
    gui_wireless_controller: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the wireless controller on the GUI.")    
    gui_advanced_wireless_features: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable advanced wireless features in GUI.")    
    gui_switch_controller: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the switch controller on the GUI.")    
    gui_fortiap_split_tunneling: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiAP split tunneling on the GUI.")    
    gui_webfilter_advanced: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable advanced web filtering on the GUI.")    
    gui_traffic_shaping: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable traffic shaping on the GUI.")    
    gui_wan_load_balancing: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SD-WAN on the GUI.")    
    gui_antivirus: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable AntiVirus on the GUI.")    
    gui_webfilter: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Web filtering on the GUI.")    
    gui_videofilter: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Video filtering on the GUI.")    
    gui_dnsfilter: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable DNS Filtering on the GUI.")    
    gui_waf_profile: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Web Application Firewall on the GUI.")    
    gui_dlp_profile: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Data Loss Prevention on the GUI.")    
    gui_dlp_advanced: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Show advanced DLP expressions on the GUI.")    
    gui_virtual_patch_profile: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Virtual Patching on the GUI.")    
    gui_casb: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Inline-CASB on the GUI.")    
    gui_fortiextender_controller: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiExtender on the GUI.")    
    gui_advanced_policy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable advanced policy configuration on the GUI.")    
    gui_allow_unnamed_policy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the requirement for policy naming on the GUI.")    
    gui_email_collection: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable email collection on the GUI.")    
    gui_multiple_interface_policy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adding multiple interfaces to a policy on the GUI.")    
    gui_policy_disclaimer: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable policy disclaimer on the GUI.")    
    gui_ztna: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Zero Trust Network Access features on the GUI.")    
    gui_ot: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Operational technology features on the GUI.")    
    gui_dynamic_device_os_id: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Create dynamic addresses to manage known devices.")    
    gui_gtp: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Manage general radio packet service (GPRS) protocols on the GUI.")    
    location_id: str | None = Field(default="0.0.0.0", description="Local location ID in the form of an IPv4 address.")    
    ike_session_resume: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IKEv2 session resumption (RFC 5723).")    
    ike_quick_crash_detect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IKE quick crash detection (RFC 6290).")    
    ike_dn_format: Literal["with-space", "no-space"] | None = Field(default="with-space", description="Configure IKE ASN.1 Distinguished Name format conventions.")    
    ike_port: int | None = Field(ge=1024, le=65535, default=500, description="UDP port for IKE/IPsec traffic (default 500).")    
    ike_tcp_port: int | None = Field(ge=1, le=65535, default=443, description="TCP port for IKE/IPsec traffic (default 443).")    
    ike_policy_route: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IKE Policy Based Routing (PBR).")    
    ike_detailed_event_logs: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable detail log for IKE events.")    
    block_land_attack: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable blocking of land attacks.")    
    default_app_port_as_service: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable policy service enforcement based on application default ports.")    
    fqdn_session_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dirty session check caused by FQDN updates.")    
    ext_resource_session_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dirty session check caused by external resource updates.")    
    dyn_addr_session_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dirty session check caused by dynamic address updates.")    
    default_policy_expiry_days: int | None = Field(ge=0, le=365, default=30, description="Default policy expiry in days (0 - 365 days, default = 30).")    
    gui_enforce_change_summary: Literal["disable", "require", "optional"] | None = Field(default="require", description="Enforce change summaries for select tables in the GUI.")    
    internet_service_database_cache: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable Internet Service database caching.")    
    internet_service_app_ctrl_size: int | None = Field(ge=0, le=4294967295, default=32768, description="Maximum number of tuple entries (protocol, port, IP address, application ID) stored by the FortiGate unit (0 - 4294967295, default = 32768). A smaller value limits the FortiGate unit from learning about internet applications.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('device')
    @classmethod
    def validate_device(cls, v: Any) -> Any:
        """
        Validate device field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dhcp_proxy_interface')
    @classmethod
    def validate_dhcp_proxy_interface(cls, v: Any) -> Any:
        """
        Validate dhcp_proxy_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    async def validate_device_references(self, client: Any) -> list[str]:
        """
        Validate device references exist in FortiGate.
        
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
            >>> policy = SettingsModel(
            ...     device="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_device_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.settings.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "device", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Device '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_dhcp_proxy_interface_references(self, client: Any) -> list[str]:
        """
        Validate dhcp_proxy_interface references exist in FortiGate.
        
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
            >>> policy = SettingsModel(
            ...     dhcp_proxy_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dhcp_proxy_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.settings.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dhcp_proxy_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dhcp-Proxy-Interface '{value}' not found in "
                "system/interface"
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
        
        errors = await self.validate_device_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dhcp_proxy_interface_references(client)
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
    "SettingsModel",    "SettingsGuiDefaultPolicyColumns",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.274841Z
# ============================================================================
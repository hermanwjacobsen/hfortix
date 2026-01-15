"""
Pydantic Models for CMDB - system/interface

Runtime validation models for system/interface configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class InterfaceClientOptions(BaseModel):
    """
    Child table model for client-options.
    
    DHCP client options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    code: int = Field(ge=0, le=255, default=0, description="DHCP client option code.")    
    type: TypeEnum | None = Field(default="hex", description="DHCP client option type.")    
    value: str | None = Field(max_length=312, default="", description="DHCP client option value.")    
    ip: list[Ip] = Field(default="", description="DHCP option IPs.")
class InterfaceFailAlertInterfaces(BaseModel):
    """
    Child table model for fail-alert-interfaces.
    
    Names of the FortiGate interfaces to which the link failure alert is sent.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=15, default="", description="Names of the non-virtual interface.")  # datasource: ['system.interface.name']
class InterfaceMember(BaseModel):
    """
    Child table model for member.
    
    Physical interfaces that belong to the aggregate or redundant interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_name: str | None = Field(max_length=79, default="", description="Physical interface name.")  # datasource: ['system.interface.name']
class InterfaceSecurityGroups(BaseModel):
    """
    Child table model for security-groups.
    
    User groups that can authenticate with the captive portal.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Names of user groups that can authenticate with the captive portal.")  # datasource: ['user.group.name']
class InterfaceVrrp(BaseModel):
    """
    Child table model for vrrp.
    
    VRRP configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    vrid: int = Field(ge=1, le=255, default=0, description="Virtual router identifier (1 - 255).")    
    version: Literal["2", "3"] | None = Field(default="2", description="VRRP version.")    
    vrgrp: int | None = Field(ge=1, le=65535, default=0, description="VRRP group ID (1 - 65535).")    
    vrip: str = Field(default="0.0.0.0", description="IP address of the virtual router.")    
    priority: int | None = Field(ge=1, le=255, default=100, description="Priority of the virtual router (1 - 255).")    
    adv_interval: int | None = Field(ge=250, le=255000, default=1000, description="Advertisement interval (250 - 255000 milliseconds).")    
    start_time: int | None = Field(ge=1, le=255, default=3, description="Startup time (1 - 255 seconds).")    
    preempt: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable preempt mode.")    
    accept_mode: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable accept mode.")    
    vrdst: list[Vrdst] = Field(default="", description="Monitor the route to this destination.")    
    vrdst_priority: int | None = Field(ge=0, le=254, default=0, description="Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254).")    
    ignore_default_route: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable ignoring of default route when checking destination.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this VRRP configuration.")    
    proxy_arp: list[ProxyArp] = Field(default=None, description="VRRP Proxy ARP configuration.")
class InterfacePhySetting(BaseModel):
    """
    Child table model for phy-setting.
    
    PHY settings
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    signal_ok_threshold: int = Field(ge=0, le=12, default=0, description="Configure the signal strength value at which the FortiGate unit detects that the receiving signal is idle or that data is not being received. Zero means idle detection is disabled. Higher values mean the signal strength must be higher in order for the FortiGate unit to consider the interface is not idle (0 - 12, default = 0).")
class InterfaceSecondaryip(BaseModel):
    """
    Child table model for secondaryip.
    
    Second IP address of interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    ip: Any = Field(default="0.0.0.0 0.0.0.0", description="Secondary IP address of the interface.")    
    secip_relay_ip: list[SecipRelayIp] = Field(default="", description="DHCP relay IP address.")    
    allowaccess: list[Allowaccess] = Field(default="", description="Management access settings for the secondary IP address.")    
    gwdetect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable detect gateway alive for first.")    
    ping_serv_status: int | None = Field(ge=0, le=255, default=0, description="PING server status.")    
    detectserver: str | None = Field(default="", description="Gateway's ping server for this IP.")    
    detectprotocol: list[Detectprotocol] = Field(default="ping", description="Protocols used to detect the server.")    
    ha_priority: int | None = Field(ge=1, le=50, default=1, description="HA election priority for the PING server.")
class InterfaceDhcpSnoopingServerList(BaseModel):
    """
    Child table model for dhcp-snooping-server-list.
    
    Configure DHCP server access list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="default", description="DHCP server name.")    
    server_ip: str | None = Field(default="0.0.0.0", description="IP address for DHCP server.")
class InterfaceTagging(BaseModel):
    """
    Child table model for tagging.
    
    Config object tagging.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Tagging entry name.")    
    category: str | None = Field(max_length=63, default="", description="Tag category.")  # datasource: ['system.object-tagging.category']    
    tags: list[Tags] = Field(default=None, description="Tags.")
class InterfaceIpv6(BaseModel):
    """
    Child table model for ipv6.
    
    IPv6 of interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip6_mode: Ip6ModeEnum | None = Field(default="static", description="Addressing mode (static, DHCP, delegated).")    
    client_options: list[ClientOptions] = Field(default=None, description="DHCP6 client options.")    
    nd_mode: Literal["basic", "SEND-compatible"] | None = Field(default="basic", description="Neighbor discovery mode.")    
    nd_cert: str = Field(max_length=35, default="", description="Neighbor discovery certificate.")  # datasource: ['certificate.local.name']    
    nd_security_level: int | None = Field(ge=0, le=7, default=0, description="Neighbor discovery security level (0 - 7; 0 = least secure, default = 0).")    
    nd_timestamp_delta: int | None = Field(ge=1, le=3600, default=300, description="Neighbor discovery timestamp delta value (1 - 3600 sec; default = 300).")    
    nd_timestamp_fuzz: int | None = Field(ge=1, le=60, default=1, description="Neighbor discovery timestamp fuzz factor (1 - 60 sec; default = 1).")    
    nd_cga_modifier: str | None = Field(default="", description="Neighbor discovery CGA modifier.")    
    ip6_dns_server_override: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable using the DNS server acquired by DHCP.")    
    ip6_address: str | None = Field(default="::/0", description="Primary IPv6 address prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.")    
    ip6_extra_addr: list[Ip6ExtraAddr] = Field(default=None, description="Extra IPv6 address prefixes of interface.")    
    ip6_allowaccess: list[Ip6Allowaccess] = Field(default="", description="Allow management access to the interface.")    
    ip6_send_adv: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending advertisements about the interface.")    
    icmp6_send_redirect: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending of ICMPv6 redirects.")    
    ip6_manage_flag: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the managed flag.")    
    ip6_other_flag: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the other IPv6 flag.")    
    ip6_max_interval: int | None = Field(ge=4, le=1800, default=600, description="IPv6 maximum interval (4 to 1800 sec).")    
    ip6_min_interval: int | None = Field(ge=3, le=1350, default=198, description="IPv6 minimum interval (3 to 1350 sec).")    
    ip6_link_mtu: int | None = Field(ge=1280, le=16000, default=0, description="IPv6 link MTU.")    
    ra_send_mtu: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending link MTU in RA packet.")    
    ip6_reachable_time: int | None = Field(ge=0, le=3600000, default=0, description="IPv6 reachable time (milliseconds; 0 means unspecified).")    
    ip6_retrans_time: int | None = Field(ge=0, le=4294967295, default=0, description="IPv6 retransmit time (milliseconds; 0 means unspecified).")    
    ip6_default_life: int | None = Field(ge=0, le=9000, default=1800, description="Default life (sec).")    
    ip6_hop_limit: int | None = Field(ge=0, le=255, default=0, description="Hop limit (0 means unspecified).")    
    ip6_adv_rio: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending advertisements with route information option.")    
    ip6_route_pref: Literal["medium", "high", "low"] | None = Field(default="medium", description="Set route preference to the interface (default = medium).")    
    ip6_route_list: list[Ip6RouteList] = Field(default=None, description="Advertised route list.")    
    autoconf: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable address auto config.")    
    unique_autoconf_addr: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable unique auto config address.")    
    interface_identifier: str | None = Field(default="::", description="IPv6 interface identifier.")    
    ip6_prefix_mode: Literal["dhcp6", "ra"] | None = Field(default="dhcp6", description="Assigning a prefix from DHCP or RA.")    
    ip6_delegated_prefix_iaid: int = Field(ge=0, le=4294967295, default=0, description="IAID of obtained delegated-prefix from the upstream interface.")    
    ip6_upstream_interface: str = Field(max_length=15, default="", description="Interface name providing delegated information.")  # datasource: ['system.interface.name']    
    ip6_subnet: str | None = Field(default="::/0", description="Subnet to routing prefix. Syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.")    
    ip6_prefix_list: list[Ip6PrefixList] = Field(default=None, description="Advertised prefix list.")    
    ip6_rdnss_list: list[Ip6RdnssList] = Field(default=None, description="Advertised IPv6 RDNSS list.")    
    ip6_dnssl_list: list[Ip6DnsslList] = Field(default=None, description="Advertised IPv6 DNSS list.")    
    ip6_delegated_prefix_list: list[Ip6DelegatedPrefixList] = Field(default=None, description="Advertised IPv6 delegated prefix list.")    
    dhcp6_relay_service: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable DHCPv6 relay.")    
    dhcp6_relay_type: Literal["regular"] | None = Field(default="regular", description="DHCPv6 relay type.")    
    dhcp6_relay_source_interface: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of address on this interface as the source address of the relay message.")    
    dhcp6_relay_ip: list[Dhcp6RelayIp] = Field(default="", description="DHCPv6 relay IP address.")    
    dhcp6_relay_source_ip: str | None = Field(default="::", description="IPv6 address used by the DHCP6 relay as its source IP.")    
    dhcp6_relay_interface_id: str | None = Field(max_length=64, default="", description="DHCP6 relay interface ID.")    
    dhcp6_client_options: list[Dhcp6ClientOptions] = Field(default="", description="DHCPv6 client options.")    
    dhcp6_prefix_delegation: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DHCPv6 prefix delegation.")    
    dhcp6_information_request: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DHCPv6 information request.")    
    dhcp6_iapd_list: list[Dhcp6IapdList] = Field(default=None, description="DHCPv6 IA-PD list.")    
    cli_conn6_status: int | None = Field(ge=0, le=4294967295, default=0, description="CLI IPv6 connection status.")    
    vrrp_virtual_mac6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable virtual MAC for VRRP.")    
    vrip6_link_local: str | None = Field(default="::", description="Link-local IPv6 address of virtual router.")    
    vrrp6: list[Vrrp6] = Field(default=None, description="IPv6 VRRP configuration.")
class InterfacePhysical(BaseModel):
    """
    Child table model for physical.
    
    Print physical interface information.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    <interface>: Any = Field(default=None, description="Interface name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class InterfaceAllowaccessEnum(str, Enum):
    """Allowed values for allowaccess field."""
    PING = "ping"    HTTPS = "https"    SSH = "ssh"    SNMP = "snmp"    HTTP = "http"    TELNET = "telnet"    FGFM = "fgfm"    RADIUS_ACCT = "radius-acct"    PROBE_RESPONSE = "probe-response"    FABRIC = "fabric"    FTM = "ftm"    SPEED_TEST = "speed-test"    SCIM = "scim"
class InterfacePppoe_egress_cosEnum(str, Enum):
    """Allowed values for pppoe_egress_cos field."""
    COS0 = "cos0"    COS1 = "cos1"    COS2 = "cos2"    COS3 = "cos3"    COS4 = "cos4"    COS5 = "cos5"    COS6 = "cos6"    COS7 = "cos7"
class InterfaceAuth_typeEnum(str, Enum):
    """Allowed values for auth_type field."""
    AUTO = "auto"    PAP = "pap"    CHAP = "chap"    MSCHAPV1 = "mschapv1"    MSCHAPV2 = "mschapv2"
class InterfacePptp_auth_typeEnum(str, Enum):
    """Allowed values for pptp_auth_type field."""
    AUTO = "auto"    PAP = "pap"    CHAP = "chap"    MSCHAPV1 = "mschapv1"    MSCHAPV2 = "mschapv2"
class InterfaceSpeedEnum(str, Enum):
    """Allowed values for speed field."""
    AUTO = "auto"    10FULL = "10full"    10HALF = "10half"    100FULL = "100full"    100HALF = "100half"    100AUTO = "100auto"    1000FULL = "1000full"    1000AUTO = "1000auto"
class InterfaceTypeEnum(str, Enum):
    """Allowed values for type field."""
    PHYSICAL = "physical"    VLAN = "vlan"    AGGREGATE = "aggregate"    REDUNDANT = "redundant"    TUNNEL = "tunnel"    VDOM_LINK = "vdom-link"    LOOPBACK = "loopback"    SWITCH = "switch"    VAP_SWITCH = "vap-switch"    WL_MESH = "wl-mesh"    FEXT_WAN = "fext-wan"    VXLAN = "vxlan"    GENEVE = "geneve"    SWITCH_VLAN = "switch-vlan"    EMAC_VLAN = "emac-vlan"    LAN_EXTENSION = "lan-extension"
class InterfaceNetflow_samplerEnum(str, Enum):
    """Allowed values for netflow_sampler field."""
    DISABLE = "disable"    TX = "tx"    RX = "rx"    BOTH = "both"
class InterfaceAlgorithmEnum(str, Enum):
    """Allowed values for algorithm field."""
    L2 = "L2"    L3 = "L3"    L4 = "L4"    NPU_GRE = "NPU-GRE"    SOURCE_MAC = "Source-MAC"
class InterfaceRoleEnum(str, Enum):
    """Allowed values for role field."""
    LAN = "lan"    WAN = "wan"    DMZ = "dmz"    UNDEFINED = "undefined"
class InterfaceManaged_subnetwork_sizeEnum(str, Enum):
    """Allowed values for managed_subnetwork_size field."""
    4 = "4"    8 = "8"    16 = "16"    32 = "32"    64 = "64"    128 = "128"    256 = "256"    512 = "512"    1024 = "1024"    2048 = "2048"    4096 = "4096"    8192 = "8192"    16384 = "16384"    32768 = "32768"    65536 = "65536"    131072 = "131072"    262144 = "262144"    524288 = "524288"    1048576 = "1048576"    2097152 = "2097152"    4194304 = "4194304"    8388608 = "8388608"    16777216 = "16777216"
class InterfaceSwitch_controller_featureEnum(str, Enum):
    """Allowed values for switch_controller_feature field."""
    NONE = "none"    DEFAULT_VLAN = "default-vlan"    QUARANTINE = "quarantine"    RSPAN = "rspan"    VOICE = "voice"    VIDEO = "video"    NAC = "nac"    NAC_SEGMENT = "nac-segment"
class InterfaceDefault_purdue_levelEnum(str, Enum):
    """Allowed values for default_purdue_level field."""
    1 = "1"    1_5 = "1.5"    2 = "2"    2_5 = "2.5"    3 = "3"    3_5 = "3.5"    4 = "4"    5 = "5"    5_5 = "5.5"

# ============================================================================
# Main Model
# ============================================================================

class InterfaceModel(BaseModel):
    """
    Pydantic model for system/interface configuration.
    
    Configure interfaces.
    
    Validation Rules:        - name: max_length=15 pattern=        - vdom: max_length=31 pattern=        - vrf: min=0 max=511 pattern=        - cli_conn_status: min=0 max=4294967295 pattern=        - fortilink: pattern=        - switch_controller_source_ip: pattern=        - mode: pattern=        - client_options: pattern=        - distance: min=1 max=255 pattern=        - priority: min=1 max=65535 pattern=        - dhcp_relay_interface_select_method: pattern=        - dhcp_relay_interface: max_length=15 pattern=        - dhcp_relay_vrf_select: min=0 max=511 pattern=        - dhcp_broadcast_flag: pattern=        - dhcp_relay_service: pattern=        - dhcp_relay_ip: pattern=        - dhcp_relay_source_ip: pattern=        - dhcp_relay_circuit_id: max_length=64 pattern=        - dhcp_relay_link_selection: pattern=        - dhcp_relay_request_all_server: pattern=        - dhcp_relay_allow_no_end_option: pattern=        - dhcp_relay_type: pattern=        - dhcp_smart_relay: pattern=        - dhcp_relay_agent_option: pattern=        - dhcp_classless_route_addition: pattern=        - management_ip: pattern=        - ip: pattern=        - allowaccess: pattern=        - gwdetect: pattern=        - ping_serv_status: min=0 max=255 pattern=        - detectserver: pattern=        - detectprotocol: pattern=        - ha_priority: min=1 max=50 pattern=        - fail_detect: pattern=        - fail_detect_option: pattern=        - fail_alert_method: pattern=        - fail_action_on_extender: pattern=        - fail_alert_interfaces: pattern=        - dhcp_client_identifier: max_length=48 pattern=        - dhcp_renew_time: min=300 max=604800 pattern=        - ipunnumbered: pattern=        - username: max_length=64 pattern=        - pppoe_egress_cos: pattern=        - pppoe_unnumbered_negotiate: pattern=        - password: max_length=128 pattern=        - idle_timeout: min=0 max=32767 pattern=        - multilink: pattern=        - mrru: min=296 max=65535 pattern=        - detected_peer_mtu: min=0 max=4294967295 pattern=        - disc_retry_timeout: min=0 max=4294967295 pattern=        - padt_retry_timeout: min=0 max=4294967295 pattern=        - service_name: max_length=63 pattern=        - ac_name: max_length=63 pattern=        - lcp_echo_interval: min=0 max=32767 pattern=        - lcp_max_echo_fails: min=0 max=32767 pattern=        - defaultgw: pattern=        - dns_server_override: pattern=        - dns_server_protocol: pattern=        - auth_type: pattern=        - pptp_client: pattern=        - pptp_user: max_length=64 pattern=        - pptp_password: max_length=128 pattern=        - pptp_server_ip: pattern=        - pptp_auth_type: pattern=        - pptp_timeout: min=0 max=65535 pattern=        - arpforward: pattern=        - ndiscforward: pattern=        - broadcast_forward: pattern=        - bfd: pattern=        - bfd_desired_min_tx: min=1 max=100000 pattern=        - bfd_detect_mult: min=1 max=50 pattern=        - bfd_required_min_rx: min=1 max=100000 pattern=        - l2forward: pattern=        - icmp_send_redirect: pattern=        - icmp_accept_redirect: pattern=        - reachable_time: min=30000 max=3600000 pattern=        - vlanforward: pattern=        - stpforward: pattern=        - stpforward_mode: pattern=        - ips_sniffer_mode: pattern=        - ident_accept: pattern=        - ipmac: pattern=        - subst: pattern=        - macaddr: pattern=        - virtual_mac: pattern=        - substitute_dst_mac: pattern=        - speed: pattern=        - status: pattern=        - netbios_forward: pattern=        - wins_ip: pattern=        - type: pattern=        - dedicated_to: pattern=        - trust_ip_1: pattern=        - trust_ip_2: pattern=        - trust_ip_3: pattern=        - trust_ip6_1: pattern=        - trust_ip6_2: pattern=        - trust_ip6_3: pattern=        - ring_rx: min=0 max=4294967295 pattern=        - ring_tx: min=0 max=4294967295 pattern=        - wccp: pattern=        - netflow_sampler: pattern=        - netflow_sample_rate: min=1 max=65535 pattern=        - netflow_sampler_id: min=1 max=254 pattern=        - sflow_sampler: pattern=        - drop_fragment: pattern=        - src_check: pattern=        - sample_rate: min=10 max=99999 pattern=        - polling_interval: min=1 max=255 pattern=        - sample_direction: pattern=        - explicit_web_proxy: pattern=        - explicit_ftp_proxy: pattern=        - proxy_captive_portal: pattern=        - tcp_mss: min=48 max=65535 pattern=        - inbandwidth: min=0 max=80000000 pattern=        - outbandwidth: min=0 max=80000000 pattern=        - egress_shaping_profile: max_length=35 pattern=        - ingress_shaping_profile: max_length=35 pattern=        - spillover_threshold: min=0 max=16776000 pattern=        - ingress_spillover_threshold: min=0 max=16776000 pattern=        - weight: min=0 max=255 pattern=        - interface: max_length=15 pattern=        - external: pattern=        - mtu_override: pattern=        - mtu: min=0 max=4294967295 pattern=        - vlan_protocol: pattern=        - vlanid: min=1 max=4094 pattern=        - forward_domain: min=0 max=2147483647 pattern=        - remote_ip: pattern=        - member: pattern=        - lacp_mode: pattern=        - lacp_ha_secondary: pattern=        - system_id_type: pattern=        - system_id: pattern=        - lacp_speed: pattern=        - min_links: min=1 max=32 pattern=        - min_links_down: pattern=        - algorithm: pattern=        - link_up_delay: min=50 max=3600000 pattern=        - aggregate_type: pattern=        - priority_override: pattern=        - aggregate: max_length=15 pattern=        - redundant_interface: max_length=15 pattern=        - devindex: min=0 max=4294967295 pattern=        - vindex: min=0 max=65535 pattern=        - switch: max_length=15 pattern=        - description: max_length=255 pattern=        - alias: max_length=25 pattern=        - security_mode: pattern=        - security_mac_auth_bypass: pattern=        - security_ip_auth_bypass: pattern=        - security_external_web: max_length=1023 pattern=        - security_external_logout: max_length=127 pattern=        - replacemsg_override_group: max_length=35 pattern=        - security_redirect_url: max_length=1023 pattern=        - auth_cert: max_length=35 pattern=        - auth_portal_addr: max_length=63 pattern=        - security_exempt_list: max_length=35 pattern=        - security_groups: pattern=        - ike_saml_server: max_length=35 pattern=        - device_identification: pattern=        - exclude_signatures: pattern=        - device_user_identification: pattern=        - lldp_reception: pattern=        - lldp_transmission: pattern=        - lldp_network_policy: max_length=35 pattern=        - estimated_upstream_bandwidth: min=0 max=4294967295 pattern=        - estimated_downstream_bandwidth: min=0 max=4294967295 pattern=        - measured_upstream_bandwidth: min=0 max=4294967295 pattern=        - measured_downstream_bandwidth: min=0 max=4294967295 pattern=        - bandwidth_measure_time: min=0 max=4294967295 pattern=        - monitor_bandwidth: pattern=        - vrrp_virtual_mac: pattern=        - vrrp: pattern=        - phy_setting: pattern=        - role: pattern=        - snmp_index: min=0 max=2147483647 pattern=        - secondary_IP: pattern=        - secondaryip: pattern=        - preserve_session_route: pattern=        - auto_auth_extension_device: pattern=        - ap_discover: pattern=        - fortilink_neighbor_detect: pattern=        - ip_managed_by_fortiipam: pattern=        - managed_subnetwork_size: pattern=        - fortilink_split_interface: pattern=        - internal: min=0 max=255 pattern=        - fortilink_backup_link: min=0 max=255 pattern=        - switch_controller_access_vlan: pattern=        - switch_controller_traffic_policy: max_length=63 pattern=        - switch_controller_rspan_mode: pattern=        - switch_controller_netflow_collect: pattern=        - switch_controller_mgmt_vlan: min=1 max=4094 pattern=        - switch_controller_igmp_snooping: pattern=        - switch_controller_igmp_snooping_proxy: pattern=        - switch_controller_igmp_snooping_fast_leave: pattern=        - switch_controller_dhcp_snooping: pattern=        - switch_controller_dhcp_snooping_verify_mac: pattern=        - switch_controller_dhcp_snooping_option82: pattern=        - dhcp_snooping_server_list: pattern=        - switch_controller_arp_inspection: pattern=        - switch_controller_learning_limit: min=0 max=128 pattern=        - switch_controller_nac: max_length=35 pattern=        - switch_controller_dynamic: max_length=35 pattern=        - switch_controller_feature: pattern=        - switch_controller_iot_scanning: pattern=        - switch_controller_offload: pattern=        - switch_controller_offload_ip: pattern=        - switch_controller_offload_gw: pattern=        - swc_vlan: min=0 max=4294967295 pattern=        - swc_first_create: min=0 max=4294967295 pattern=        - color: min=0 max=32 pattern=        - tagging: pattern=        - eap_supplicant: pattern=        - eap_method: pattern=        - eap_identity: max_length=35 pattern=        - eap_password: max_length=128 pattern=        - eap_ca_cert: max_length=79 pattern=        - eap_user_cert: max_length=35 pattern=        - default_purdue_level: pattern=        - ipv6: pattern=        - physical: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="Name.")    
    vdom: str = Field(max_length=31, default="", description="Interface is in this virtual domain (VDOM).")  # datasource: ['system.vdom.name']    
    vrf: int | None = Field(ge=0, le=511, default=0, description="Virtual Routing Forwarding ID.")    
    cli_conn_status: int | None = Field(ge=0, le=4294967295, default=0, description="CLI connection status.")    
    fortilink: Literal["enable", "disable"] | None = Field(default="disable", description="Enable FortiLink to dedicate this interface to manage other Fortinet devices.")    
    switch_controller_source_ip: Literal["outbound", "fixed"] | None = Field(default="outbound", description="Source IP address used in FortiLink over L3 connections.")    
    mode: Literal["static", "dhcp", "pppoe"] | None = Field(default="static", description="Addressing mode (static, DHCP, PPPoE).")    
    client_options: list[ClientOptions] = Field(default=None, description="DHCP client options.")    
    distance: int | None = Field(ge=1, le=255, default=5, description="Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.")    
    priority: int | None = Field(ge=1, le=65535, default=1, description="Priority of learned routes.")    
    dhcp_relay_interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    dhcp_relay_interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    dhcp_relay_vrf_select: int | None = Field(ge=0, le=511, default=-1, description="VRF ID used for connection to server.")    
    dhcp_broadcast_flag: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable setting of the broadcast flag in messages sent by the DHCP client (default = enable).")    
    dhcp_relay_service: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allowing this interface to act as a DHCP relay.")    
    dhcp_relay_ip: list[DhcpRelayIp] = Field(default="", description="DHCP relay IP address.")    
    dhcp_relay_source_ip: str | None = Field(default="0.0.0.0", description="IP address used by the DHCP relay as its source IP.")    
    dhcp_relay_circuit_id: str | None = Field(max_length=64, default="", description="DHCP relay circuit ID.")    
    dhcp_relay_link_selection: str | None = Field(default="0.0.0.0", description="DHCP relay link selection.")    
    dhcp_relay_request_all_server: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable sending of DHCP requests to all servers.")    
    dhcp_relay_allow_no_end_option: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable relaying DHCP messages with no end option.")    
    dhcp_relay_type: Literal["regular", "ipsec"] | None = Field(default="regular", description="DHCP relay type (regular or IPsec).")    
    dhcp_smart_relay: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable DHCP smart relay.")    
    dhcp_relay_agent_option: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable DHCP relay agent option.")    
    dhcp_classless_route_addition: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable addition of classless static routes retrieved from DHCP server.")    
    management_ip: Any = Field(default="0.0.0.0 0.0.0.0", description="High Availability in-band management IP address of this interface.")    
    ip: Any = Field(default="0.0.0.0 0.0.0.0", description="Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.")    
    allowaccess: list[Allowaccess] = Field(default="", description="Permitted types of management access to this interface.")    
    gwdetect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable detect gateway alive for first.")    
    ping_serv_status: int | None = Field(ge=0, le=255, default=0, description="PING server status.")    
    detectserver: str | None = Field(default="", description="Gateway's ping server for this IP.")    
    detectprotocol: list[Detectprotocol] = Field(default="ping", description="Protocols used to detect the server.")    
    ha_priority: int | None = Field(ge=1, le=50, default=1, description="HA election priority for the PING server.")    
    fail_detect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fail detection features for this interface.")    
    fail_detect_option: list[FailDetectOption] = Field(default="link-down", description="Options for detecting that this interface has failed.")    
    fail_alert_method: Literal["link-failed-signal", "link-down"] | None = Field(default="link-down", description="Select link-failed-signal or link-down method to alert about a failed link.")    
    fail_action_on_extender: Literal["soft-restart", "hard-restart", "reboot"] | None = Field(default="soft-restart", description="Action on FortiExtender when interface fail.")    
    fail_alert_interfaces: list[FailAlertInterfaces] = Field(default=None, description="Names of the FortiGate interfaces to which the link failure alert is sent.")    
    dhcp_client_identifier: str | None = Field(max_length=48, default="", description="DHCP client identifier.")    
    dhcp_renew_time: int | None = Field(ge=300, le=604800, default=0, description="DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server.")    
    ipunnumbered: str | None = Field(default="0.0.0.0", description="Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.")    
    username: str | None = Field(max_length=64, default="", description="Username of the PPPoE account, provided by your ISP.")    
    pppoe_egress_cos: PppoeEgressCosEnum | None = Field(default="cos0", description="CoS in VLAN tag for outgoing PPPoE/PPP packets.")    
    pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable PPPoE unnumbered negotiation.")    
    password: Any = Field(max_length=128, default=None, description="PPPoE account's password.")    
    idle_timeout: int | None = Field(ge=0, le=32767, default=0, description="PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.")    
    multilink: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PPP multilink support.")    
    mrru: int | None = Field(ge=296, le=65535, default=1500, description="PPP MRRU (296 - 65535, default = 1500).")    
    detected_peer_mtu: int | None = Field(ge=0, le=4294967295, default=0, description="MTU of detected peer (0 - 4294967295).")    
    disc_retry_timeout: int | None = Field(ge=0, le=4294967295, default=1, description="Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout.")    
    padt_retry_timeout: int | None = Field(ge=0, le=4294967295, default=1, description="PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time.")    
    service_name: str | None = Field(max_length=63, default="", description="PPPoE service name.")    
    ac_name: str | None = Field(max_length=63, default="", description="PPPoE server name.")    
    lcp_echo_interval: int | None = Field(ge=0, le=32767, default=5, description="Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.")    
    lcp_max_echo_fails: int | None = Field(ge=0, le=32767, default=3, description="Maximum missed LCP echo messages before disconnect.")    
    defaultgw: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to get the gateway IP from the DHCP or PPPoE server.")    
    dns_server_override: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use DNS acquired by DHCP or PPPoE.")    
    dns_server_protocol: list[DnsServerProtocol] = Field(default="cleartext", description="DNS transport protocols.")    
    auth_type: AuthTypeEnum | None = Field(default="auto", description="PPP authentication type to use.")    
    pptp_client: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PPTP client.")    
    pptp_user: str | None = Field(max_length=64, default="", description="PPTP user name.")    
    pptp_password: Any = Field(max_length=128, default=None, description="PPTP password.")    
    pptp_server_ip: str | None = Field(default="0.0.0.0", description="PPTP server IP address.")    
    pptp_auth_type: PptpAuthTypeEnum | None = Field(default="auto", description="PPTP authentication type.")    
    pptp_timeout: int | None = Field(ge=0, le=65535, default=0, description="Idle timer in minutes (0 for disabled).")    
    arpforward: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable ARP forwarding.")    
    ndiscforward: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable NDISC forwarding.")    
    broadcast_forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable broadcast forwarding.")    
    bfd: Literal["global", "enable", "disable"] | None = Field(default="global", description="Bidirectional Forwarding Detection (BFD) settings.")    
    bfd_desired_min_tx: int | None = Field(ge=1, le=100000, default=250, description="BFD desired minimal transmit interval.")    
    bfd_detect_mult: int | None = Field(ge=1, le=50, default=3, description="BFD detection multiplier.")    
    bfd_required_min_rx: int | None = Field(ge=1, le=100000, default=250, description="BFD required minimal receive interval.")    
    l2forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable l2 forwarding.")    
    icmp_send_redirect: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending of ICMP redirects.")    
    icmp_accept_redirect: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable ICMP accept redirect.")    
    reachable_time: int | None = Field(ge=30000, le=3600000, default=30000, description="IPv4 reachable time in milliseconds (30000 - 3600000, default = 30000).")    
    vlanforward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable traffic forwarding between VLANs on this interface.")    
    stpforward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable STP forwarding.")    
    stpforward_mode: Literal["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"] | None = Field(default="rpl-all-ext-id", description="Configure STP forwarding mode.")    
    ips_sniffer_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the use of this interface as a one-armed sniffer.")    
    ident_accept: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication for this interface.")    
    ipmac: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IP/MAC binding.")    
    subst: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to always send packets from this interface to a destination MAC address.")    
    macaddr: str | None = Field(default="00:00:00:00:00:00", description="Change the interface's MAC address.")    
    virtual_mac: str | None = Field(default="00:00:00:00:00:00", description="Change the interface's virtual MAC address.")    
    substitute_dst_mac: str | None = Field(default="00:00:00:00:00:00", description="Destination MAC address that all packets are sent to from this interface.")    
    speed: SpeedEnum | None = Field(default="auto", description="Interface speed. The default setting and the options available depend on the interface hardware.")    
    status: Literal["up", "down"] | None = Field(default="up", description="Bring the interface up or shut the interface down.")    
    netbios_forward: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable NETBIOS forwarding.")    
    wins_ip: str | None = Field(default="0.0.0.0", description="WINS server IP.")    
    type: TypeEnum | None = Field(default="vlan", description="Interface type.")    
    dedicated_to: Literal["none", "management"] | None = Field(default="none", description="Configure interface for single purpose.")    
    trust_ip_1: Any = Field(default="0.0.0.0 0.0.0.0", description="Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).")    
    trust_ip_2: Any = Field(default="0.0.0.0 0.0.0.0", description="Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).")    
    trust_ip_3: Any = Field(default="0.0.0.0 0.0.0.0", description="Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).")    
    trust_ip6_1: str | None = Field(default="::/0", description="Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).")    
    trust_ip6_2: str | None = Field(default="::/0", description="Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).")    
    trust_ip6_3: str | None = Field(default="::/0", description="Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).")    
    ring_rx: int | None = Field(ge=0, le=4294967295, default=0, description="RX ring size.")    
    ring_tx: int | None = Field(ge=0, le=4294967295, default=0, description="TX ring size.")    
    wccp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.")    
    netflow_sampler: NetflowSamplerEnum | None = Field(default="disable", description="Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).")    
    netflow_sample_rate: int | None = Field(ge=1, le=65535, default=1, description="NetFlow sample rate.  Sample one packet every configured number of packets (1 - 65535, default = 1, which means standard NetFlow where all packets are sampled).")    
    netflow_sampler_id: int | None = Field(ge=1, le=254, default=0, description="Netflow sampler ID.")    
    sflow_sampler: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sFlow on this interface.")    
    drop_fragment: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable drop fragment packets.")    
    src_check: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable source IP check.")    
    sample_rate: int | None = Field(ge=10, le=99999, default=2000, description="sFlow sample rate (10 - 99999).")    
    polling_interval: int | None = Field(ge=1, le=255, default=20, description="sFlow polling interval in seconds (1 - 255).")    
    sample_direction: Literal["tx", "rx", "both"] | None = Field(default="both", description="Data that NetFlow collects (rx, tx, or both).")    
    explicit_web_proxy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the explicit web proxy on this interface.")    
    explicit_ftp_proxy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the explicit FTP proxy on this interface.")    
    proxy_captive_portal: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable proxy captive portal on this interface.")    
    tcp_mss: int | None = Field(ge=48, le=65535, default=0, description="TCP maximum segment size. 0 means do not change segment size.")    
    inbandwidth: int | None = Field(ge=0, le=80000000, default=0, description="Bandwidth limit for incoming traffic (0 - 80000000 kbps), 0 means unlimited.")    
    outbandwidth: int | None = Field(ge=0, le=80000000, default=0, description="Bandwidth limit for outgoing traffic (0 - 80000000 kbps).")    
    egress_shaping_profile: str | None = Field(max_length=35, default="", description="Outgoing traffic shaping profile.")  # datasource: ['firewall.shaping-profile.profile-name']    
    ingress_shaping_profile: str | None = Field(max_length=35, default="", description="Incoming traffic shaping profile.")  # datasource: ['firewall.shaping-profile.profile-name']    
    spillover_threshold: int | None = Field(ge=0, le=16776000, default=0, description="Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.")    
    ingress_spillover_threshold: int | None = Field(ge=0, le=16776000, default=0, description="Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.")    
    weight: int | None = Field(ge=0, le=255, default=0, description="Default weight for static routes (if route has no weight configured).")    
    interface: str = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    external: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable identifying the interface as an external interface (which usually means it's connected to the Internet).")    
    mtu_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to set a custom MTU for this interface.")    
    mtu: int | None = Field(ge=0, le=4294967295, default=1500, description="MTU value for this interface.")    
    vlan_protocol: Literal["8021q", "8021ad"] | None = Field(default="8021q", description="Ethernet protocol of VLAN.")    
    vlanid: int | None = Field(ge=1, le=4094, default=0, description="VLAN ID (1 - 4094).")    
    forward_domain: int | None = Field(ge=0, le=2147483647, default=0, description="Transparent mode forward domain.")    
    remote_ip: Any = Field(default="0.0.0.0 0.0.0.0", description="Remote IP address of tunnel.")    
    member: list[Member] = Field(default=None, description="Physical interfaces that belong to the aggregate or redundant interface.")    
    lacp_mode: Literal["static", "passive", "active"] | None = Field(default="active", description="LACP mode.")    
    lacp_ha_secondary: Literal["enable", "disable"] | None = Field(default="enable", description="LACP HA secondary member.")    
    system_id_type: Literal["auto", "user"] | None = Field(default="auto", description="Method in which system ID is generated.")    
    system_id: str = Field(default="00:00:00:00:00:00", description="Define a system ID for the aggregate interface.")    
    lacp_speed: Literal["slow", "fast"] | None = Field(default="slow", description="How often the interface sends LACP messages.")    
    min_links: int | None = Field(ge=1, le=32, default=1, description="Minimum number of aggregated ports that must be up.")    
    min_links_down: Literal["operational", "administrative"] | None = Field(default="operational", description="Action to take when less than the configured minimum number of links are active.")    
    algorithm: AlgorithmEnum | None = Field(default="L4", description="Frame distribution algorithm.")    
    link_up_delay: int | None = Field(ge=50, le=3600000, default=50, description="Number of milliseconds to wait before considering a link is up.")    
    aggregate_type: Literal["physical", "vxlan"] | None = Field(default="physical", description="Type of aggregation.")    
    priority_override: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable fail back to higher priority port once recovered.")    
    aggregate: str | None = Field(max_length=15, default="", description="Aggregate interface.")    
    redundant_interface: str | None = Field(max_length=15, default="", description="Redundant interface.")    
    devindex: int | None = Field(ge=0, le=4294967295, default=0, description="Device Index.")    
    vindex: int | None = Field(ge=0, le=65535, default=0, description="Switch control interface VLAN ID.")    
    switch: str | None = Field(max_length=15, default="", description="Contained in switch.")    
    description: str | None = Field(max_length=255, default=None, description="Description.")    
    alias: str | None = Field(max_length=25, default="", description="Alias will be displayed with the interface name to make it easier to distinguish.")    
    security_mode: Literal["none", "captive-portal", "802.1X"] | None = Field(default="none", description="Turn on captive portal authentication for this interface.")    
    security_mac_auth_bypass: Literal["mac-auth-only", "enable", "disable"] | None = Field(default="disable", description="Enable/disable MAC authentication bypass.")    
    security_ip_auth_bypass: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IP authentication bypass.")    
    security_external_web: str | None = Field(max_length=1023, default=None, description="URL of external authentication web server.")    
    security_external_logout: str | None = Field(max_length=127, default="", description="URL of external authentication logout server.")    
    replacemsg_override_group: str | None = Field(max_length=35, default="", description="Replacement message override group.")    
    security_redirect_url: str | None = Field(max_length=1023, default=None, description="URL redirection after disclaimer/authentication.")    
    auth_cert: str | None = Field(max_length=35, default="", description="HTTPS server certificate.")  # datasource: ['vpn.certificate.local.name']    
    auth_portal_addr: str | None = Field(max_length=63, default="", description="Address of captive portal.")    
    security_exempt_list: str | None = Field(max_length=35, default="", description="Name of security-exempt-list.")    
    security_groups: list[SecurityGroups] = Field(default=None, description="User groups that can authenticate with the captive portal.")    
    ike_saml_server: str | None = Field(max_length=35, default="", description="Configure IKE authentication SAML server.")  # datasource: ['user.saml.name']    
    device_identification: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.")    
    exclude_signatures: list[ExcludeSignatures] = Field(default="", description="Exclude IOT or OT application signatures.")    
    device_user_identification: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable passive gathering of user identity information about users on this interface.")    
    lldp_reception: Literal["enable", "disable", "vdom"] | None = Field(default="vdom", description="Enable/disable Link Layer Discovery Protocol (LLDP) reception.")    
    lldp_transmission: Literal["enable", "disable", "vdom"] | None = Field(default="vdom", description="Enable/disable Link Layer Discovery Protocol (LLDP) transmission.")    
    lldp_network_policy: str | None = Field(max_length=35, default="", description="LLDP-MED network policy profile.")  # datasource: ['system.lldp.network-policy.name']    
    estimated_upstream_bandwidth: int | None = Field(ge=0, le=4294967295, default=0, description="Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.")    
    estimated_downstream_bandwidth: int | None = Field(ge=0, le=4294967295, default=0, description="Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.")    
    measured_upstream_bandwidth: int | None = Field(ge=0, le=4294967295, default=0, description="Measured upstream bandwidth (kbps).")    
    measured_downstream_bandwidth: int | None = Field(ge=0, le=4294967295, default=0, description="Measured downstream bandwidth (kbps).")    
    bandwidth_measure_time: int | None = Field(ge=0, le=4294967295, default=0, description="Bandwidth measure time.")    
    monitor_bandwidth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable monitoring bandwidth on this interface.")    
    vrrp_virtual_mac: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of virtual MAC for VRRP.")    
    vrrp: list[Vrrp] = Field(default=None, description="VRRP configuration.")    
    phy_setting: list[PhySetting] = Field(default=None, description="PHY settings")    
    role: RoleEnum | None = Field(default="undefined", description="Interface role.")    
    snmp_index: int | None = Field(ge=0, le=2147483647, default=0, description="Permanent SNMP Index of the interface.")    
    secondary_IP: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adding a secondary IP to this interface.")    
    secondaryip: list[Secondaryip] = Field(default=None, description="Second IP address of interface.")    
    preserve_session_route: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable preservation of session route when dirty.")    
    auto_auth_extension_device: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.")    
    ap_discover: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable automatic registration of unknown FortiAP devices.")    
    fortilink_neighbor_detect: Literal["lldp", "fortilink"] | None = Field(default="lldp", description="Protocol for FortiGate neighbor discovery.")    
    ip_managed_by_fortiipam: Literal["inherit-global", "enable", "disable"] | None = Field(default="inherit-global", description="Enable/disable automatic IP address assignment of this interface by FortiIPAM.")    
    managed_subnetwork_size: ManagedSubnetworkSizeEnum | None = Field(default="256", description="Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate unit's DHCP server settings.")    
    fortilink_split_interface: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.")    
    internal: int | None = Field(ge=0, le=255, default=0, description="Implicitly created.")    
    fortilink_backup_link: int | None = Field(ge=0, le=255, default=0, description="FortiLink split interface backup link.")    
    switch_controller_access_vlan: Literal["enable", "disable"] | None = Field(default="disable", description="Block FortiSwitch port-to-port traffic.")    
    switch_controller_traffic_policy: str | None = Field(max_length=63, default="", description="Switch controller traffic policy for the VLAN.")  # datasource: ['switch-controller.traffic-policy.name']    
    switch_controller_rspan_mode: Literal["disable", "enable"] | None = Field(default="disable", description="Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.")    
    switch_controller_netflow_collect: Literal["disable", "enable"] | None = Field(default="disable", description="NetFlow collection and processing.")    
    switch_controller_mgmt_vlan: int | None = Field(ge=1, le=4094, default=4094, description="VLAN to use for FortiLink management purposes.")    
    switch_controller_igmp_snooping: Literal["enable", "disable"] | None = Field(default="disable", description="Switch controller IGMP snooping.")    
    switch_controller_igmp_snooping_proxy: Literal["enable", "disable"] | None = Field(default="disable", description="Switch controller IGMP snooping proxy.")    
    switch_controller_igmp_snooping_fast_leave: Literal["enable", "disable"] | None = Field(default="disable", description="Switch controller IGMP snooping fast-leave.")    
    switch_controller_dhcp_snooping: Literal["enable", "disable"] | None = Field(default="disable", description="Switch controller DHCP snooping.")    
    switch_controller_dhcp_snooping_verify_mac: Literal["enable", "disable"] | None = Field(default="disable", description="Switch controller DHCP snooping verify MAC.")    
    switch_controller_dhcp_snooping_option82: Literal["enable", "disable"] | None = Field(default="disable", description="Switch controller DHCP snooping option82.")    
    dhcp_snooping_server_list: list[DhcpSnoopingServerList] = Field(default=None, description="Configure DHCP server access list.")    
    switch_controller_arp_inspection: Literal["enable", "disable", "monitor"] | None = Field(default="disable", description="Enable/disable/Monitor FortiSwitch ARP inspection.")    
    switch_controller_learning_limit: int | None = Field(ge=0, le=128, default=0, description="Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default).")    
    switch_controller_nac: str | None = Field(max_length=35, default="", description="Integrated FortiLink settings for managed FortiSwitch.")  # datasource: ['switch-controller.fortilink-settings.name']    
    switch_controller_dynamic: str | None = Field(max_length=35, default="", description="Integrated FortiLink settings for managed FortiSwitch.")  # datasource: ['switch-controller.fortilink-settings.name']    
    switch_controller_feature: SwitchControllerFeatureEnum | None = Field(default="none", description="Interface's purpose when assigning traffic (read only).")    
    switch_controller_iot_scanning: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable managed FortiSwitch IoT scanning.")    
    switch_controller_offload: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable managed FortiSwitch routing offload.")    
    switch_controller_offload_ip: str | None = Field(default="0.0.0.0", description="IP for routing offload on FortiSwitch.")    
    switch_controller_offload_gw: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable managed FortiSwitch routing offload gateway.")    
    swc_vlan: int | None = Field(ge=0, le=4294967295, default=0, description="Creation status for switch-controller VLANs.")    
    swc_first_create: int | None = Field(ge=0, le=4294967295, default=0, description="Initial create for switch-controller VLANs.")    
    color: int | None = Field(ge=0, le=32, default=0, description="Color of icon on the GUI.")    
    tagging: list[Tagging] = Field(default=None, description="Config object tagging.")    
    eap_supplicant: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable EAP-Supplicant.")    
    eap_method: Literal["tls", "peap"] | None = Field(default="", description="EAP method.")    
    eap_identity: str | None = Field(max_length=35, default="", description="EAP identity.")    
    eap_password: Any = Field(max_length=128, default=None, description="EAP password.")    
    eap_ca_cert: str | None = Field(max_length=79, default="", description="EAP CA certificate name.")  # datasource: ['certificate.ca.name']    
    eap_user_cert: str | None = Field(max_length=35, default="", description="EAP user certificate name.")  # datasource: ['certificate.local.name']    
    default_purdue_level: DefaultPurdueLevelEnum | None = Field(default="3", description="default purdue level of device detected on this interface.")    
    ipv6: list[Ipv6] = Field(default=None, description="IPv6 of interface.")    
    physical: list[Physical] = Field(default=None, description="Print physical interface information.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vdom')
    @classmethod
    def validate_vdom(cls, v: Any) -> Any:
        """
        Validate vdom field.
        
        Datasource: ['system.vdom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dhcp_relay_interface')
    @classmethod
    def validate_dhcp_relay_interface(cls, v: Any) -> Any:
        """
        Validate dhcp_relay_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('egress_shaping_profile')
    @classmethod
    def validate_egress_shaping_profile(cls, v: Any) -> Any:
        """
        Validate egress_shaping_profile field.
        
        Datasource: ['firewall.shaping-profile.profile-name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ingress_shaping_profile')
    @classmethod
    def validate_ingress_shaping_profile(cls, v: Any) -> Any:
        """
        Validate ingress_shaping_profile field.
        
        Datasource: ['firewall.shaping-profile.profile-name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_cert')
    @classmethod
    def validate_auth_cert(cls, v: Any) -> Any:
        """
        Validate auth_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ike_saml_server')
    @classmethod
    def validate_ike_saml_server(cls, v: Any) -> Any:
        """
        Validate ike_saml_server field.
        
        Datasource: ['user.saml.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('lldp_network_policy')
    @classmethod
    def validate_lldp_network_policy(cls, v: Any) -> Any:
        """
        Validate lldp_network_policy field.
        
        Datasource: ['system.lldp.network-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('switch_controller_traffic_policy')
    @classmethod
    def validate_switch_controller_traffic_policy(cls, v: Any) -> Any:
        """
        Validate switch_controller_traffic_policy field.
        
        Datasource: ['switch-controller.traffic-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('switch_controller_nac')
    @classmethod
    def validate_switch_controller_nac(cls, v: Any) -> Any:
        """
        Validate switch_controller_nac field.
        
        Datasource: ['switch-controller.fortilink-settings.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('switch_controller_dynamic')
    @classmethod
    def validate_switch_controller_dynamic(cls, v: Any) -> Any:
        """
        Validate switch_controller_dynamic field.
        
        Datasource: ['switch-controller.fortilink-settings.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('eap_ca_cert')
    @classmethod
    def validate_eap_ca_cert(cls, v: Any) -> Any:
        """
        Validate eap_ca_cert field.
        
        Datasource: ['certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('eap_user_cert')
    @classmethod
    def validate_eap_user_cert(cls, v: Any) -> Any:
        """
        Validate eap_user_cert field.
        
        Datasource: ['certificate.local.name']
        
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
    async def validate_vdom_references(self, client: Any) -> list[str]:
        """
        Validate vdom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/vdom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     vdom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vdom", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.vdom.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Vdom '{value}' not found in "
                "system/vdom"
            )        
        return errors    
    async def validate_dhcp_relay_interface_references(self, client: Any) -> list[str]:
        """
        Validate dhcp_relay_interface references exist in FortiGate.
        
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
            >>> policy = InterfaceModel(
            ...     dhcp_relay_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dhcp_relay_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dhcp_relay_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dhcp-Relay-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
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
            >>> policy = InterfaceModel(
            ...     fail_alert_interfaces=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fail_alert_interfaces_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
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
    async def validate_egress_shaping_profile_references(self, client: Any) -> list[str]:
        """
        Validate egress_shaping_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/shaping-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     egress_shaping_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_egress_shaping_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "egress_shaping_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.shaping-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Egress-Shaping-Profile '{value}' not found in "
                "firewall/shaping-profile"
            )        
        return errors    
    async def validate_ingress_shaping_profile_references(self, client: Any) -> list[str]:
        """
        Validate ingress_shaping_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/shaping-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     ingress_shaping_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ingress_shaping_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ingress_shaping_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.shaping-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ingress-Shaping-Profile '{value}' not found in "
                "firewall/shaping-profile"
            )        
        return errors    
    async def validate_interface_references(self, client: Any) -> list[str]:
        """
        Validate interface references exist in FortiGate.
        
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
            >>> policy = InterfaceModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_member_references(self, client: Any) -> list[str]:
        """
        Validate member references exist in FortiGate.
        
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
            >>> policy = InterfaceModel(
            ...     member=[{"interface-name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_member_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "member", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("interface-name")
            else:
                value = getattr(item, "interface-name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Member '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_auth_cert_references(self, client: Any) -> list[str]:
        """
        Validate auth_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     auth_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Cert '{value}' not found in "
                "vpn/certificate/local"
            )        
        return errors    
    async def validate_security_groups_references(self, client: Any) -> list[str]:
        """
        Validate security_groups references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     security_groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_security_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "security_groups", [])
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
            if await client.api.cmdb.user.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Security-Groups '{value}' not found in "
                    "user/group"
                )        
        return errors    
    async def validate_ike_saml_server_references(self, client: Any) -> list[str]:
        """
        Validate ike_saml_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/saml        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     ike_saml_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ike_saml_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ike_saml_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.saml.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ike-Saml-Server '{value}' not found in "
                "user/saml"
            )        
        return errors    
    async def validate_lldp_network_policy_references(self, client: Any) -> list[str]:
        """
        Validate lldp_network_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/lldp/network-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     lldp_network_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_lldp_network_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "lldp_network_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.lldp.network-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Lldp-Network-Policy '{value}' not found in "
                "system/lldp/network-policy"
            )        
        return errors    
    async def validate_switch_controller_traffic_policy_references(self, client: Any) -> list[str]:
        """
        Validate switch_controller_traffic_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/traffic-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     switch_controller_traffic_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_switch_controller_traffic_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "switch_controller_traffic_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.traffic-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Switch-Controller-Traffic-Policy '{value}' not found in "
                "switch-controller/traffic-policy"
            )        
        return errors    
    async def validate_switch_controller_nac_references(self, client: Any) -> list[str]:
        """
        Validate switch_controller_nac references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/fortilink-settings        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     switch_controller_nac="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_switch_controller_nac_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "switch_controller_nac", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.fortilink-settings.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Switch-Controller-Nac '{value}' not found in "
                "switch-controller/fortilink-settings"
            )        
        return errors    
    async def validate_switch_controller_dynamic_references(self, client: Any) -> list[str]:
        """
        Validate switch_controller_dynamic references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/fortilink-settings        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     switch_controller_dynamic="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_switch_controller_dynamic_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "switch_controller_dynamic", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.fortilink-settings.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Switch-Controller-Dynamic '{value}' not found in "
                "switch-controller/fortilink-settings"
            )        
        return errors    
    async def validate_tagging_references(self, client: Any) -> list[str]:
        """
        Validate tagging references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/object-tagging        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     tagging=[{"category": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tagging_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "tagging", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("category")
            else:
                value = getattr(item, "category", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.object-tagging.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Tagging '{value}' not found in "
                    "system/object-tagging"
                )        
        return errors    
    async def validate_eap_ca_cert_references(self, client: Any) -> list[str]:
        """
        Validate eap_ca_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     eap_ca_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_eap_ca_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "eap_ca_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Eap-Ca-Cert '{value}' not found in "
                "certificate/ca"
            )        
        return errors    
    async def validate_eap_user_cert_references(self, client: Any) -> list[str]:
        """
        Validate eap_user_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InterfaceModel(
            ...     eap_user_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_eap_user_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "eap_user_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Eap-User-Cert '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_ipv6_references(self, client: Any) -> list[str]:
        """
        Validate ipv6 references exist in FortiGate.
        
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
            >>> policy = InterfaceModel(
            ...     ipv6=[{"ip6-upstream-interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ipv6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ipv6", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("ip6-upstream-interface")
            else:
                value = getattr(item, "ip6-upstream-interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ipv6 '{value}' not found in "
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
        
        errors = await self.validate_vdom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dhcp_relay_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fail_alert_interfaces_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_egress_shaping_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ingress_shaping_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_member_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_security_groups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ike_saml_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_lldp_network_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_switch_controller_traffic_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_switch_controller_nac_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_switch_controller_dynamic_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_tagging_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_eap_ca_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_eap_user_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ipv6_references(client)
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
    "InterfaceModel",    "InterfaceClientOptions",    "InterfaceFailAlertInterfaces",    "InterfaceMember",    "InterfaceSecurityGroups",    "InterfaceVrrp",    "InterfacePhySetting",    "InterfaceSecondaryip",    "InterfaceDhcpSnoopingServerList",    "InterfaceTagging",    "InterfaceIpv6",    "InterfacePhysical",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.202774Z
# ============================================================================
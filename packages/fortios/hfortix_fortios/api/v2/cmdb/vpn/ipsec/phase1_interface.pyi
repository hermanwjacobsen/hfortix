from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class Phase1InterfacePayload(TypedDict, total=False):
    """
    Type hints for vpn/ipsec/phase1_interface payload fields.
    
    Configure VPN remote gateway.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.address.AddressEndpoint` (via: ipv4-name, ipv4-split-exclude, ipv4-split-include)
        - :class:`~.firewall.address6.Address6Endpoint` (via: ipv6-name, ipv6-split-exclude, ipv6-split-include)
        - :class:`~.firewall.addrgrp.AddrgrpEndpoint` (via: ipv4-name, ipv4-split-exclude, ipv4-split-include)
        - :class:`~.firewall.addrgrp6.Addrgrp6Endpoint` (via: ipv6-name, ipv6-split-exclude, ipv6-split-include)
        - :class:`~.firewall.service.custom.CustomEndpoint` (via: split-include-service)
        - :class:`~.firewall.service.group.GroupEndpoint` (via: split-include-service)
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.system.sdwan.health-check.HealthCheckEndpoint` (via: fec-health-check)
        - :class:`~.user.group.GroupEndpoint` (via: authusrgrp, usrgrp)
        - :class:`~.user.peer.PeerEndpoint` (via: peer)
        - ... and 4 more dependencies

    **Usage:**
        payload: Phase1InterfacePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # IPsec remote gateway name. | MaxLen: 15
    type: Literal["static", "dynamic", "ddns"]  # Remote gateway type. | Default: static
    interface: str  # Local physical, aggregate, or VLAN outgoing interf | MaxLen: 35
    ip_version: Literal["4", "6"]  # IP version to use for VPN interface. | Default: 4
    ike_version: Literal["1", "2"]  # IKE protocol version. | Default: 1
    local_gw: str  # IPv4 address of the local gateway's external inter | Default: 0.0.0.0
    local_gw6: str  # IPv6 address of the local gateway's external inter | Default: ::
    remote_gw: str  # IPv4 address of the remote gateway's external inte | Default: 0.0.0.0
    remote_gw6: str  # IPv6 address of the remote gateway's external inte | Default: ::
    remotegw_ddns: str  # Domain name of remote gateway. For example, name.d | MaxLen: 63
    keylife: int  # Time to wait in seconds before phase 1 encryption | Default: 86400 | Min: 120 | Max: 172800
    certificate: list[dict[str, Any]]  # The names of up to 4 signed personal certificates.
    authmethod: Literal["psk", "signature"]  # Authentication method. | Default: psk
    authmethod_remote: Literal["psk", "signature"]  # Authentication method (remote side).
    mode: Literal["aggressive", "main"]  # The ID protection mode used to establish a secure | Default: main
    peertype: Literal["any", "one", "dialup", "peer", "peergrp"]  # Accept this peer type. | Default: peer
    peerid: str  # Accept this peer identity. | MaxLen: 255
    default_gw: str  # IPv4 address of default route gateway to use for t | Default: 0.0.0.0
    default_gw_priority: int  # Priority for default gateway route. A higher prior | Default: 0 | Min: 0 | Max: 4294967295
    usrgrp: str  # User group name for dialup peers. | MaxLen: 35
    peer: str  # Accept this peer certificate. | MaxLen: 35
    peergrp: str  # Accept this peer certificate group. | MaxLen: 35
    monitor: list[dict[str, Any]]  # IPsec interface as backup for primary interface.
    monitor_min: int  # Minimum number of links to become degraded before | Default: 0 | Min: 0 | Max: 4294967295
    monitor_hold_down_type: Literal["immediate", "delay", "time"]  # Recovery time method when primary interface re-est | Default: immediate
    monitor_hold_down_delay: int  # Time to wait in seconds before recovery once prima | Default: 0 | Min: 0 | Max: 31536000
    monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of the week to recover once primary re-establi | Default: sunday
    monitor_hold_down_time: str  # Time of day at which to fail back to primary after
    net_device: Literal["enable", "disable"]  # Enable/disable kernel device creation. | Default: disable
    passive_mode: Literal["enable", "disable"]  # Enable/disable IPsec passive mode for static tunne | Default: disable
    exchange_interface_ip: Literal["enable", "disable"]  # Enable/disable exchange of IPsec interface IP addr | Default: disable
    exchange_ip_addr4: str  # IPv4 address to exchange with peers. | Default: 0.0.0.0
    exchange_ip_addr6: str  # IPv6 address to exchange with peers. | Default: ::
    aggregate_member: Literal["enable", "disable"]  # Enable/disable use as an aggregate member. | Default: disable
    aggregate_weight: int  # Link weight for aggregate. | Default: 1 | Min: 1 | Max: 100
    packet_redistribution: Literal["enable", "disable"]  # Enable/disable packet distribution (RPS) on the IP | Default: disable
    peer_egress_shaping: Literal["enable", "disable"]  # Enable/disable peer egress shaping. | Default: disable
    peer_egress_shaping_value: int  # Configure outbound bandwidth to use for peer egres | Default: 0 | Min: 0 | Max: 80000000
    mode_cfg: Literal["disable", "enable"]  # Enable/disable configuration method. | Default: disable
    mode_cfg_allow_client_selector: Literal["disable", "enable"]  # Enable/disable mode-cfg client to use custom phase | Default: disable
    assign_ip: Literal["disable", "enable"]  # Enable/disable assignment of IP to IPsec interface | Default: enable
    assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"]  # Method by which the IP address will be assigned. | Default: range
    ipv4_start_ip: str  # Start of IPv4 range. | Default: 0.0.0.0
    ipv4_end_ip: str  # End of IPv4 range. | Default: 0.0.0.0
    ipv4_netmask: str  # IPv4 Netmask. | Default: 255.255.255.255
    dhcp_ra_giaddr: str  # Relay agent gateway IP address to use in the giadd | Default: 0.0.0.0
    dhcp6_ra_linkaddr: str  # Relay agent IPv6 link address to use in DHCP6 requ | Default: ::
    dns_mode: Literal["manual", "auto"]  # DNS server mode. | Default: manual
    ipv4_dns_server1: str  # IPv4 DNS server 1. | Default: 0.0.0.0
    ipv4_dns_server2: str  # IPv4 DNS server 2. | Default: 0.0.0.0
    ipv4_dns_server3: str  # IPv4 DNS server 3. | Default: 0.0.0.0
    internal_domain_list: list[dict[str, Any]]  # One or more internal domain names in quotes separa
    dns_suffix_search: list[dict[str, Any]]  # One or more DNS domain name suffixes in quotes sep
    ipv4_wins_server1: str  # WINS server 1. | Default: 0.0.0.0
    ipv4_wins_server2: str  # WINS server 2. | Default: 0.0.0.0
    ipv4_exclude_range: list[dict[str, Any]]  # Configuration Method IPv4 exclude ranges.
    ipv4_split_include: str  # IPv4 split-include subnets. | MaxLen: 79
    split_include_service: str  # Split-include services. | MaxLen: 79
    ipv4_name: str  # IPv4 address name. | MaxLen: 79
    ipv6_start_ip: str  # Start of IPv6 range. | Default: ::
    ipv6_end_ip: str  # End of IPv6 range. | Default: ::
    ipv6_prefix: int  # IPv6 prefix. | Default: 128 | Min: 1 | Max: 128
    ipv6_dns_server1: str  # IPv6 DNS server 1. | Default: ::
    ipv6_dns_server2: str  # IPv6 DNS server 2. | Default: ::
    ipv6_dns_server3: str  # IPv6 DNS server 3. | Default: ::
    ipv6_exclude_range: list[dict[str, Any]]  # Configuration method IPv6 exclude ranges.
    ipv6_split_include: str  # IPv6 split-include subnets. | MaxLen: 79
    ipv6_name: str  # IPv6 address name. | MaxLen: 79
    ip_delay_interval: int  # IP address reuse delay interval in seconds | Default: 0 | Min: 0 | Max: 28800
    unity_support: Literal["disable", "enable"]  # Enable/disable support for Cisco UNITY Configurati | Default: enable
    domain: str  # Instruct unity clients about the single default DN | MaxLen: 63
    banner: str  # Message that unity client should display after con | MaxLen: 1024
    include_local_lan: Literal["disable", "enable"]  # Enable/disable allow local LAN access on unity cli | Default: disable
    ipv4_split_exclude: str  # IPv4 subnets that should not be sent over the IPse | MaxLen: 79
    ipv6_split_exclude: str  # IPv6 subnets that should not be sent over the IPse | MaxLen: 79
    save_password: Literal["disable", "enable"]  # Enable/disable saving XAuth username and password | Default: disable
    client_auto_negotiate: Literal["disable", "enable"]  # Enable/disable allowing the VPN client to bring up | Default: disable
    client_keep_alive: Literal["disable", "enable"]  # Enable/disable allowing the VPN client to keep the | Default: disable
    backup_gateway: list[dict[str, Any]]  # Instruct unity clients about the backup gateway ad
    proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]  # Phase1 proposal.
    add_route: Literal["disable", "enable"]  # Enable/disable control addition of a route to peer | Default: enable
    add_gw_route: Literal["enable", "disable"]  # Enable/disable automatically add a route to the re | Default: disable
    psksecret: str  # Pre-shared secret for PSK authentication
    psksecret_remote: str  # Pre-shared secret for remote side PSK authenticati
    keepalive: int  # NAT-T keep alive interval. | Default: 10 | Min: 5 | Max: 900
    distance: int  # Distance for routes added by IKE (1 - 255). | Default: 15 | Min: 1 | Max: 255
    priority: int  # Priority for routes added by IKE (1 - 65535). | Default: 1 | Min: 1 | Max: 65535
    localid: str  # Local ID. | MaxLen: 63
    localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"]  # Local ID type. | Default: auto
    auto_negotiate: Literal["enable", "disable"]  # Enable/disable automatic initiation of IKE SA nego | Default: enable
    negotiate_timeout: int  # IKE SA negotiation timeout in seconds (1 - 300). | Default: 30 | Min: 1 | Max: 300
    fragmentation: Literal["enable", "disable"]  # Enable/disable fragment IKE message on re-transmis | Default: enable
    ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"]  # Determine whether IP packets are fragmented before | Default: post-encapsulation
    dpd: Literal["disable", "on-idle", "on-demand"]  # Dead Peer Detection mode. | Default: on-demand
    dpd_retrycount: int  # Number of DPD retry attempts. | Default: 3 | Min: 1 | Max: 10
    dpd_retryinterval: str  # DPD retry interval.
    comments: str  # Comment. | MaxLen: 255
    npu_offload: Literal["enable", "disable"]  # Enable/disable offloading NPU. | Default: enable
    send_cert_chain: Literal["enable", "disable"]  # Enable/disable sending certificate chain. | Default: enable
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]  # DH group. | Default: 20
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE1 group.
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE2 group.
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE3 group.
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE4 group.
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE5 group.
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE6 group.
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE7 group.
    suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"]  # Use Suite-B. | Default: disable
    eap: Literal["enable", "disable"]  # Enable/disable IKEv2 EAP authentication. | Default: disable
    eap_identity: Literal["use-id-payload", "send-request"]  # IKEv2 EAP peer identity type. | Default: use-id-payload
    eap_exclude_peergrp: str  # Peer group excluded from EAP authentication. | MaxLen: 35
    eap_cert_auth: Literal["enable", "disable"]  # Enable/disable peer certificate authentication in | Default: disable
    acct_verify: Literal["enable", "disable"]  # Enable/disable verification of RADIUS accounting r | Default: disable
    ppk: Literal["disable", "allow", "require"]  # Enable/disable IKEv2 Postquantum Preshared Key | Default: disable
    ppk_secret: str  # IKEv2 Postquantum Preshared Key
    ppk_identity: str  # IKEv2 Postquantum Preshared Key Identity. | MaxLen: 35
    wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"]  # GUI VPN Wizard Type. | Default: custom
    xauthtype: Literal["disable", "client", "pap", "chap", "auto"]  # XAuth type. | Default: disable
    reauth: Literal["disable", "enable"]  # Enable/disable re-authentication upon IKE SA lifet | Default: disable
    authusr: str  # XAuth user name. | MaxLen: 64
    authpasswd: str  # XAuth password (max 35 characters). | MaxLen: 128
    group_authentication: Literal["enable", "disable"]  # Enable/disable IKEv2 IDi group authentication. | Default: disable
    group_authentication_secret: str  # Password for IKEv2 ID group authentication. ASCII
    authusrgrp: str  # Authentication user group. | MaxLen: 35
    mesh_selector_type: Literal["disable", "subnet", "host"]  # Add selectors containing subsets of the configurat | Default: disable
    idle_timeout: Literal["enable", "disable"]  # Enable/disable IPsec tunnel idle timeout. | Default: disable
    shared_idle_timeout: Literal["enable", "disable"]  # Enable/disable IPsec tunnel shared idle timeout. | Default: disable
    idle_timeoutinterval: int  # IPsec tunnel idle timeout in minutes (5 - 43200). | Default: 15 | Min: 5 | Max: 43200
    ha_sync_esp_seqno: Literal["enable", "disable"]  # Enable/disable sequence number jump ahead for IPse | Default: enable
    fgsp_sync: Literal["enable", "disable"]  # Enable/disable IPsec syncing of tunnels for FGSP I | Default: disable
    inbound_dscp_copy: Literal["enable", "disable"]  # Enable/disable copy the dscp in the ESP header to | Default: disable
    auto_discovery_sender: Literal["enable", "disable"]  # Enable/disable sending auto-discovery short-cut me | Default: disable
    auto_discovery_receiver: Literal["enable", "disable"]  # Enable/disable accepting auto-discovery short-cut | Default: disable
    auto_discovery_forwarder: Literal["enable", "disable"]  # Enable/disable forwarding auto-discovery short-cut | Default: disable
    auto_discovery_psk: Literal["enable", "disable"]  # Enable/disable use of pre-shared secrets for authe | Default: disable
    auto_discovery_shortcuts: Literal["independent", "dependent"]  # Control deletion of child short-cut tunnels when t | Default: independent
    auto_discovery_crossover: Literal["allow", "block"]  # Allow/block set-up of short-cut tunnels between di | Default: allow
    auto_discovery_offer_interval: int  # Interval between shortcut offer messages in second | Default: 5 | Min: 1 | Max: 300
    auto_discovery_dialup_placeholder: Literal["disable", "enable"]  # Control if this dynamic gateway is used for shortc | Default: disable
    encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"]  # Enable/disable GRE/VXLAN/VPNID encapsulation. | Default: none
    encapsulation_address: Literal["ike", "ipv4", "ipv6"]  # Source for GRE/VXLAN tunnel address. | Default: ike
    encap_local_gw4: str  # Local IPv4 address of GRE/VXLAN tunnel. | Default: 0.0.0.0
    encap_local_gw6: str  # Local IPv6 address of GRE/VXLAN tunnel. | Default: ::
    encap_remote_gw4: str  # Remote IPv4 address of GRE/VXLAN tunnel. | Default: 0.0.0.0
    encap_remote_gw6: str  # Remote IPv6 address of GRE/VXLAN tunnel. | Default: ::
    vni: int  # VNI of VXLAN tunnel. | Default: 0 | Min: 1 | Max: 16777215
    nattraversal: Literal["enable", "disable", "forced"]  # Enable/disable NAT traversal. | Default: enable
    esn: Literal["require", "allow", "disable"]  # Extended sequence number (ESN) negotiation. | Default: disable
    fragmentation_mtu: int  # IKE fragmentation MTU (500 - 16000). | Default: 1200 | Min: 500 | Max: 16000
    childless_ike: Literal["enable", "disable"]  # Enable/disable childless IKEv2 initiation | Default: disable
    azure_ad_autoconnect: Literal["enable", "disable"]  # Enable/disable Azure AD Auto-Connect for FortiClie | Default: disable
    client_resume: Literal["enable", "disable"]  # Enable/disable resumption of offline FortiClient s | Default: disable
    client_resume_interval: int  # Maximum time in seconds during which a VPN client | Default: 7200 | Min: 120 | Max: 172800
    rekey: Literal["enable", "disable"]  # Enable/disable phase1 rekey. | Default: enable
    digital_signature_auth: Literal["enable", "disable"]  # Enable/disable IKEv2 Digital Signature Authenticat | Default: disable
    signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"]  # Digital Signature Authentication hash algorithms. | Default: sha2-512
    rsa_signature_format: Literal["pkcs1", "pss"]  # Digital Signature Authentication RSA signature for | Default: pkcs1
    rsa_signature_hash_override: Literal["enable", "disable"]  # Enable/disable IKEv2 RSA signature hash algorithm | Default: disable
    enforce_unique_id: Literal["disable", "keep-new", "keep-old"]  # Enable/disable peer ID uniqueness check. | Default: disable
    cert_id_validation: Literal["enable", "disable"]  # Enable/disable cross validation of peer ID and the | Default: enable
    fec_egress: Literal["enable", "disable"]  # Enable/disable Forward Error Correction for egress | Default: disable
    fec_send_timeout: int  # Timeout in milliseconds before sending Forward Err | Default: 5 | Min: 1 | Max: 1000
    fec_base: int  # Number of base Forward Error Correction packets | Default: 10 | Min: 1 | Max: 20
    fec_codec: Literal["rs", "xor"]  # Forward Error Correction encoding/decoding algorit | Default: rs
    fec_redundant: int  # Number of redundant Forward Error Correction packe | Default: 1 | Min: 1 | Max: 5
    fec_ingress: Literal["enable", "disable"]  # Enable/disable Forward Error Correction for ingres | Default: disable
    fec_receive_timeout: int  # Timeout in milliseconds before dropping Forward Er | Default: 50 | Min: 1 | Max: 1000
    fec_health_check: str  # SD-WAN health check. | MaxLen: 35
    fec_mapping_profile: str  # Forward Error Correction (FEC) mapping profile. | MaxLen: 35
    network_overlay: Literal["disable", "enable"]  # Enable/disable network overlays. | Default: disable
    network_id: int  # VPN gateway network ID. | Default: 0 | Min: 0 | Max: 255
    dev_id_notification: Literal["disable", "enable"]  # Enable/disable device ID notification. | Default: disable
    dev_id: str  # Device ID carried by the device ID notification. | MaxLen: 63
    loopback_asymroute: Literal["enable", "disable"]  # Enable/disable asymmetric routing for IKE traffic | Default: enable
    link_cost: int  # VPN tunnel underlay link cost. | Default: 0 | Min: 0 | Max: 255
    kms: str  # Key Management Services server. | MaxLen: 35
    exchange_fgt_device_id: Literal["enable", "disable"]  # Enable/disable device identifier exchange with pee | Default: disable
    ipv6_auto_linklocal: Literal["enable", "disable"]  # Enable/disable auto generation of IPv6 link-local | Default: disable
    ems_sn_check: Literal["enable", "disable"]  # Enable/disable verification of EMS serial number. | Default: disable
    cert_trust_store: Literal["local", "ems"]  # CA certificate trust store. | Default: local
    qkd: Literal["disable", "allow", "require"]  # Enable/disable use of Quantum Key Distribution | Default: disable
    qkd_hybrid: Literal["disable", "allow", "require"]  # Enable/disable use of Quantum Key Distribution | Default: disable
    qkd_profile: str  # Quantum Key Distribution (QKD) server profile. | MaxLen: 35
    transport: Literal["udp", "auto", "tcp"]  # Set IKE transport protocol. | Default: auto
    fortinet_esp: Literal["enable", "disable"]  # Enable/disable Fortinet ESP encapsulation. | Default: disable
    auto_transport_threshold: int  # Timeout in seconds before falling back to next tra | Default: 15 | Min: 1 | Max: 300
    remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"]  # Set type of IPv4 remote gateway address matching. | Default: any
    remote_gw_subnet: str  # IPv4 address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    remote_gw_start_ip: str  # First IPv4 address in the range. | Default: 0.0.0.0
    remote_gw_end_ip: str  # Last IPv4 address in the range. | Default: 0.0.0.0
    remote_gw_country: str  # IPv4 addresses associated to a specific country. | MaxLen: 2
    remote_gw_ztna_tags: list[dict[str, Any]]  # IPv4 ZTNA posture tags.
    remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"]  # Set type of IPv6 remote gateway address matching. | Default: any
    remote_gw6_subnet: str  # IPv6 address and prefix. | Default: ::/0
    remote_gw6_start_ip: str  # First IPv6 address in the range. | Default: ::
    remote_gw6_end_ip: str  # Last IPv6 address in the range. | Default: ::
    remote_gw6_country: str  # IPv6 addresses associated to a specific country. | MaxLen: 2
    cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"]  # Enable/disable cross validation of peer username a | Default: none
    cert_peer_username_strip: Literal["disable", "enable"]  # Enable/disable domain stripping on certificate ide | Default: disable

# Nested TypedDicts for table field children (dict mode)

class Phase1InterfaceCertificateItem(TypedDict):
    """Type hints for certificate table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Certificate name. | MaxLen: 79


class Phase1InterfaceMonitorItem(TypedDict):
    """Type hints for monitor table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # IPsec interface as backup for primary interface. | MaxLen: 79


class Phase1InterfaceInternaldomainlistItem(TypedDict):
    """Type hints for internal-domain-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    domain_name: str  # Domain name. | MaxLen: 79


class Phase1InterfaceDnssuffixsearchItem(TypedDict):
    """Type hints for dns-suffix-search table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    dns_suffix: str  # DNS suffix. | MaxLen: 79


class Phase1InterfaceIpv4excluderangeItem(TypedDict):
    """Type hints for ipv4-exclude-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    start_ip: str  # Start of IPv4 exclusive range. | Default: 0.0.0.0
    end_ip: str  # End of IPv4 exclusive range. | Default: 0.0.0.0


class Phase1InterfaceIpv6excluderangeItem(TypedDict):
    """Type hints for ipv6-exclude-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    start_ip: str  # Start of IPv6 exclusive range. | Default: ::
    end_ip: str  # End of IPv6 exclusive range. | Default: ::


class Phase1InterfaceBackupgatewayItem(TypedDict):
    """Type hints for backup-gateway table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    address: str  # Address of backup gateway. | MaxLen: 79


class Phase1InterfaceRemotegwztnatagsItem(TypedDict):
    """Type hints for remote-gw-ztna-tags table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Address name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class Phase1InterfaceCertificateObject:
    """Typed object for certificate table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Certificate name. | MaxLen: 79
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
class Phase1InterfaceMonitorObject:
    """Typed object for monitor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPsec interface as backup for primary interface. | MaxLen: 79
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
class Phase1InterfaceInternaldomainlistObject:
    """Typed object for internal-domain-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Domain name. | MaxLen: 79
    domain_name: str
    
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
class Phase1InterfaceDnssuffixsearchObject:
    """Typed object for dns-suffix-search table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # DNS suffix. | MaxLen: 79
    dns_suffix: str
    
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
class Phase1InterfaceIpv4excluderangeObject:
    """Typed object for ipv4-exclude-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Start of IPv4 exclusive range. | Default: 0.0.0.0
    start_ip: str
    # End of IPv4 exclusive range. | Default: 0.0.0.0
    end_ip: str
    
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
class Phase1InterfaceIpv6excluderangeObject:
    """Typed object for ipv6-exclude-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Start of IPv6 exclusive range. | Default: ::
    start_ip: str
    # End of IPv6 exclusive range. | Default: ::
    end_ip: str
    
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
class Phase1InterfaceBackupgatewayObject:
    """Typed object for backup-gateway table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address of backup gateway. | MaxLen: 79
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
class Phase1InterfaceRemotegwztnatagsObject:
    """Typed object for remote-gw-ztna-tags table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Address name. | MaxLen: 79
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
class Phase1InterfaceResponse(TypedDict):
    """
    Type hints for vpn/ipsec/phase1_interface API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # IPsec remote gateway name. | MaxLen: 15
    type: Literal["static", "dynamic", "ddns"]  # Remote gateway type. | Default: static
    interface: str  # Local physical, aggregate, or VLAN outgoing interf | MaxLen: 35
    ip_version: Literal["4", "6"]  # IP version to use for VPN interface. | Default: 4
    ike_version: Literal["1", "2"]  # IKE protocol version. | Default: 1
    local_gw: str  # IPv4 address of the local gateway's external inter | Default: 0.0.0.0
    local_gw6: str  # IPv6 address of the local gateway's external inter | Default: ::
    remote_gw: str  # IPv4 address of the remote gateway's external inte | Default: 0.0.0.0
    remote_gw6: str  # IPv6 address of the remote gateway's external inte | Default: ::
    remotegw_ddns: str  # Domain name of remote gateway. For example, name.d | MaxLen: 63
    keylife: int  # Time to wait in seconds before phase 1 encryption | Default: 86400 | Min: 120 | Max: 172800
    certificate: list[Phase1InterfaceCertificateItem]  # The names of up to 4 signed personal certificates.
    authmethod: Literal["psk", "signature"]  # Authentication method. | Default: psk
    authmethod_remote: Literal["psk", "signature"]  # Authentication method (remote side).
    mode: Literal["aggressive", "main"]  # The ID protection mode used to establish a secure | Default: main
    peertype: Literal["any", "one", "dialup", "peer", "peergrp"]  # Accept this peer type. | Default: peer
    peerid: str  # Accept this peer identity. | MaxLen: 255
    default_gw: str  # IPv4 address of default route gateway to use for t | Default: 0.0.0.0
    default_gw_priority: int  # Priority for default gateway route. A higher prior | Default: 0 | Min: 0 | Max: 4294967295
    usrgrp: str  # User group name for dialup peers. | MaxLen: 35
    peer: str  # Accept this peer certificate. | MaxLen: 35
    peergrp: str  # Accept this peer certificate group. | MaxLen: 35
    monitor: list[Phase1InterfaceMonitorItem]  # IPsec interface as backup for primary interface.
    monitor_min: int  # Minimum number of links to become degraded before | Default: 0 | Min: 0 | Max: 4294967295
    monitor_hold_down_type: Literal["immediate", "delay", "time"]  # Recovery time method when primary interface re-est | Default: immediate
    monitor_hold_down_delay: int  # Time to wait in seconds before recovery once prima | Default: 0 | Min: 0 | Max: 31536000
    monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # Day of the week to recover once primary re-establi | Default: sunday
    monitor_hold_down_time: str  # Time of day at which to fail back to primary after
    net_device: Literal["enable", "disable"]  # Enable/disable kernel device creation. | Default: disable
    passive_mode: Literal["enable", "disable"]  # Enable/disable IPsec passive mode for static tunne | Default: disable
    exchange_interface_ip: Literal["enable", "disable"]  # Enable/disable exchange of IPsec interface IP addr | Default: disable
    exchange_ip_addr4: str  # IPv4 address to exchange with peers. | Default: 0.0.0.0
    exchange_ip_addr6: str  # IPv6 address to exchange with peers. | Default: ::
    aggregate_member: Literal["enable", "disable"]  # Enable/disable use as an aggregate member. | Default: disable
    aggregate_weight: int  # Link weight for aggregate. | Default: 1 | Min: 1 | Max: 100
    packet_redistribution: Literal["enable", "disable"]  # Enable/disable packet distribution (RPS) on the IP | Default: disable
    peer_egress_shaping: Literal["enable", "disable"]  # Enable/disable peer egress shaping. | Default: disable
    peer_egress_shaping_value: int  # Configure outbound bandwidth to use for peer egres | Default: 0 | Min: 0 | Max: 80000000
    mode_cfg: Literal["disable", "enable"]  # Enable/disable configuration method. | Default: disable
    mode_cfg_allow_client_selector: Literal["disable", "enable"]  # Enable/disable mode-cfg client to use custom phase | Default: disable
    assign_ip: Literal["disable", "enable"]  # Enable/disable assignment of IP to IPsec interface | Default: enable
    assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"]  # Method by which the IP address will be assigned. | Default: range
    ipv4_start_ip: str  # Start of IPv4 range. | Default: 0.0.0.0
    ipv4_end_ip: str  # End of IPv4 range. | Default: 0.0.0.0
    ipv4_netmask: str  # IPv4 Netmask. | Default: 255.255.255.255
    dhcp_ra_giaddr: str  # Relay agent gateway IP address to use in the giadd | Default: 0.0.0.0
    dhcp6_ra_linkaddr: str  # Relay agent IPv6 link address to use in DHCP6 requ | Default: ::
    dns_mode: Literal["manual", "auto"]  # DNS server mode. | Default: manual
    ipv4_dns_server1: str  # IPv4 DNS server 1. | Default: 0.0.0.0
    ipv4_dns_server2: str  # IPv4 DNS server 2. | Default: 0.0.0.0
    ipv4_dns_server3: str  # IPv4 DNS server 3. | Default: 0.0.0.0
    internal_domain_list: list[Phase1InterfaceInternaldomainlistItem]  # One or more internal domain names in quotes separa
    dns_suffix_search: list[Phase1InterfaceDnssuffixsearchItem]  # One or more DNS domain name suffixes in quotes sep
    ipv4_wins_server1: str  # WINS server 1. | Default: 0.0.0.0
    ipv4_wins_server2: str  # WINS server 2. | Default: 0.0.0.0
    ipv4_exclude_range: list[Phase1InterfaceIpv4excluderangeItem]  # Configuration Method IPv4 exclude ranges.
    ipv4_split_include: str  # IPv4 split-include subnets. | MaxLen: 79
    split_include_service: str  # Split-include services. | MaxLen: 79
    ipv4_name: str  # IPv4 address name. | MaxLen: 79
    ipv6_start_ip: str  # Start of IPv6 range. | Default: ::
    ipv6_end_ip: str  # End of IPv6 range. | Default: ::
    ipv6_prefix: int  # IPv6 prefix. | Default: 128 | Min: 1 | Max: 128
    ipv6_dns_server1: str  # IPv6 DNS server 1. | Default: ::
    ipv6_dns_server2: str  # IPv6 DNS server 2. | Default: ::
    ipv6_dns_server3: str  # IPv6 DNS server 3. | Default: ::
    ipv6_exclude_range: list[Phase1InterfaceIpv6excluderangeItem]  # Configuration method IPv6 exclude ranges.
    ipv6_split_include: str  # IPv6 split-include subnets. | MaxLen: 79
    ipv6_name: str  # IPv6 address name. | MaxLen: 79
    ip_delay_interval: int  # IP address reuse delay interval in seconds | Default: 0 | Min: 0 | Max: 28800
    unity_support: Literal["disable", "enable"]  # Enable/disable support for Cisco UNITY Configurati | Default: enable
    domain: str  # Instruct unity clients about the single default DN | MaxLen: 63
    banner: str  # Message that unity client should display after con | MaxLen: 1024
    include_local_lan: Literal["disable", "enable"]  # Enable/disable allow local LAN access on unity cli | Default: disable
    ipv4_split_exclude: str  # IPv4 subnets that should not be sent over the IPse | MaxLen: 79
    ipv6_split_exclude: str  # IPv6 subnets that should not be sent over the IPse | MaxLen: 79
    save_password: Literal["disable", "enable"]  # Enable/disable saving XAuth username and password | Default: disable
    client_auto_negotiate: Literal["disable", "enable"]  # Enable/disable allowing the VPN client to bring up | Default: disable
    client_keep_alive: Literal["disable", "enable"]  # Enable/disable allowing the VPN client to keep the | Default: disable
    backup_gateway: list[Phase1InterfaceBackupgatewayItem]  # Instruct unity clients about the backup gateway ad
    proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]  # Phase1 proposal.
    add_route: Literal["disable", "enable"]  # Enable/disable control addition of a route to peer | Default: enable
    add_gw_route: Literal["enable", "disable"]  # Enable/disable automatically add a route to the re | Default: disable
    psksecret: str  # Pre-shared secret for PSK authentication
    psksecret_remote: str  # Pre-shared secret for remote side PSK authenticati
    keepalive: int  # NAT-T keep alive interval. | Default: 10 | Min: 5 | Max: 900
    distance: int  # Distance for routes added by IKE (1 - 255). | Default: 15 | Min: 1 | Max: 255
    priority: int  # Priority for routes added by IKE (1 - 65535). | Default: 1 | Min: 1 | Max: 65535
    localid: str  # Local ID. | MaxLen: 63
    localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"]  # Local ID type. | Default: auto
    auto_negotiate: Literal["enable", "disable"]  # Enable/disable automatic initiation of IKE SA nego | Default: enable
    negotiate_timeout: int  # IKE SA negotiation timeout in seconds (1 - 300). | Default: 30 | Min: 1 | Max: 300
    fragmentation: Literal["enable", "disable"]  # Enable/disable fragment IKE message on re-transmis | Default: enable
    ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"]  # Determine whether IP packets are fragmented before | Default: post-encapsulation
    dpd: Literal["disable", "on-idle", "on-demand"]  # Dead Peer Detection mode. | Default: on-demand
    dpd_retrycount: int  # Number of DPD retry attempts. | Default: 3 | Min: 1 | Max: 10
    dpd_retryinterval: str  # DPD retry interval.
    comments: str  # Comment. | MaxLen: 255
    npu_offload: Literal["enable", "disable"]  # Enable/disable offloading NPU. | Default: enable
    send_cert_chain: Literal["enable", "disable"]  # Enable/disable sending certificate chain. | Default: enable
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]  # DH group. | Default: 20
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE1 group.
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE2 group.
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE3 group.
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE4 group.
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE5 group.
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE6 group.
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]  # ADDKE7 group.
    suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"]  # Use Suite-B. | Default: disable
    eap: Literal["enable", "disable"]  # Enable/disable IKEv2 EAP authentication. | Default: disable
    eap_identity: Literal["use-id-payload", "send-request"]  # IKEv2 EAP peer identity type. | Default: use-id-payload
    eap_exclude_peergrp: str  # Peer group excluded from EAP authentication. | MaxLen: 35
    eap_cert_auth: Literal["enable", "disable"]  # Enable/disable peer certificate authentication in | Default: disable
    acct_verify: Literal["enable", "disable"]  # Enable/disable verification of RADIUS accounting r | Default: disable
    ppk: Literal["disable", "allow", "require"]  # Enable/disable IKEv2 Postquantum Preshared Key | Default: disable
    ppk_secret: str  # IKEv2 Postquantum Preshared Key
    ppk_identity: str  # IKEv2 Postquantum Preshared Key Identity. | MaxLen: 35
    wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"]  # GUI VPN Wizard Type. | Default: custom
    xauthtype: Literal["disable", "client", "pap", "chap", "auto"]  # XAuth type. | Default: disable
    reauth: Literal["disable", "enable"]  # Enable/disable re-authentication upon IKE SA lifet | Default: disable
    authusr: str  # XAuth user name. | MaxLen: 64
    authpasswd: str  # XAuth password (max 35 characters). | MaxLen: 128
    group_authentication: Literal["enable", "disable"]  # Enable/disable IKEv2 IDi group authentication. | Default: disable
    group_authentication_secret: str  # Password for IKEv2 ID group authentication. ASCII
    authusrgrp: str  # Authentication user group. | MaxLen: 35
    mesh_selector_type: Literal["disable", "subnet", "host"]  # Add selectors containing subsets of the configurat | Default: disable
    idle_timeout: Literal["enable", "disable"]  # Enable/disable IPsec tunnel idle timeout. | Default: disable
    shared_idle_timeout: Literal["enable", "disable"]  # Enable/disable IPsec tunnel shared idle timeout. | Default: disable
    idle_timeoutinterval: int  # IPsec tunnel idle timeout in minutes (5 - 43200). | Default: 15 | Min: 5 | Max: 43200
    ha_sync_esp_seqno: Literal["enable", "disable"]  # Enable/disable sequence number jump ahead for IPse | Default: enable
    fgsp_sync: Literal["enable", "disable"]  # Enable/disable IPsec syncing of tunnels for FGSP I | Default: disable
    inbound_dscp_copy: Literal["enable", "disable"]  # Enable/disable copy the dscp in the ESP header to | Default: disable
    auto_discovery_sender: Literal["enable", "disable"]  # Enable/disable sending auto-discovery short-cut me | Default: disable
    auto_discovery_receiver: Literal["enable", "disable"]  # Enable/disable accepting auto-discovery short-cut | Default: disable
    auto_discovery_forwarder: Literal["enable", "disable"]  # Enable/disable forwarding auto-discovery short-cut | Default: disable
    auto_discovery_psk: Literal["enable", "disable"]  # Enable/disable use of pre-shared secrets for authe | Default: disable
    auto_discovery_shortcuts: Literal["independent", "dependent"]  # Control deletion of child short-cut tunnels when t | Default: independent
    auto_discovery_crossover: Literal["allow", "block"]  # Allow/block set-up of short-cut tunnels between di | Default: allow
    auto_discovery_offer_interval: int  # Interval between shortcut offer messages in second | Default: 5 | Min: 1 | Max: 300
    auto_discovery_dialup_placeholder: Literal["disable", "enable"]  # Control if this dynamic gateway is used for shortc | Default: disable
    encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"]  # Enable/disable GRE/VXLAN/VPNID encapsulation. | Default: none
    encapsulation_address: Literal["ike", "ipv4", "ipv6"]  # Source for GRE/VXLAN tunnel address. | Default: ike
    encap_local_gw4: str  # Local IPv4 address of GRE/VXLAN tunnel. | Default: 0.0.0.0
    encap_local_gw6: str  # Local IPv6 address of GRE/VXLAN tunnel. | Default: ::
    encap_remote_gw4: str  # Remote IPv4 address of GRE/VXLAN tunnel. | Default: 0.0.0.0
    encap_remote_gw6: str  # Remote IPv6 address of GRE/VXLAN tunnel. | Default: ::
    vni: int  # VNI of VXLAN tunnel. | Default: 0 | Min: 1 | Max: 16777215
    nattraversal: Literal["enable", "disable", "forced"]  # Enable/disable NAT traversal. | Default: enable
    esn: Literal["require", "allow", "disable"]  # Extended sequence number (ESN) negotiation. | Default: disable
    fragmentation_mtu: int  # IKE fragmentation MTU (500 - 16000). | Default: 1200 | Min: 500 | Max: 16000
    childless_ike: Literal["enable", "disable"]  # Enable/disable childless IKEv2 initiation | Default: disable
    azure_ad_autoconnect: Literal["enable", "disable"]  # Enable/disable Azure AD Auto-Connect for FortiClie | Default: disable
    client_resume: Literal["enable", "disable"]  # Enable/disable resumption of offline FortiClient s | Default: disable
    client_resume_interval: int  # Maximum time in seconds during which a VPN client | Default: 7200 | Min: 120 | Max: 172800
    rekey: Literal["enable", "disable"]  # Enable/disable phase1 rekey. | Default: enable
    digital_signature_auth: Literal["enable", "disable"]  # Enable/disable IKEv2 Digital Signature Authenticat | Default: disable
    signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"]  # Digital Signature Authentication hash algorithms. | Default: sha2-512
    rsa_signature_format: Literal["pkcs1", "pss"]  # Digital Signature Authentication RSA signature for | Default: pkcs1
    rsa_signature_hash_override: Literal["enable", "disable"]  # Enable/disable IKEv2 RSA signature hash algorithm | Default: disable
    enforce_unique_id: Literal["disable", "keep-new", "keep-old"]  # Enable/disable peer ID uniqueness check. | Default: disable
    cert_id_validation: Literal["enable", "disable"]  # Enable/disable cross validation of peer ID and the | Default: enable
    fec_egress: Literal["enable", "disable"]  # Enable/disable Forward Error Correction for egress | Default: disable
    fec_send_timeout: int  # Timeout in milliseconds before sending Forward Err | Default: 5 | Min: 1 | Max: 1000
    fec_base: int  # Number of base Forward Error Correction packets | Default: 10 | Min: 1 | Max: 20
    fec_codec: Literal["rs", "xor"]  # Forward Error Correction encoding/decoding algorit | Default: rs
    fec_redundant: int  # Number of redundant Forward Error Correction packe | Default: 1 | Min: 1 | Max: 5
    fec_ingress: Literal["enable", "disable"]  # Enable/disable Forward Error Correction for ingres | Default: disable
    fec_receive_timeout: int  # Timeout in milliseconds before dropping Forward Er | Default: 50 | Min: 1 | Max: 1000
    fec_health_check: str  # SD-WAN health check. | MaxLen: 35
    fec_mapping_profile: str  # Forward Error Correction (FEC) mapping profile. | MaxLen: 35
    network_overlay: Literal["disable", "enable"]  # Enable/disable network overlays. | Default: disable
    network_id: int  # VPN gateway network ID. | Default: 0 | Min: 0 | Max: 255
    dev_id_notification: Literal["disable", "enable"]  # Enable/disable device ID notification. | Default: disable
    dev_id: str  # Device ID carried by the device ID notification. | MaxLen: 63
    loopback_asymroute: Literal["enable", "disable"]  # Enable/disable asymmetric routing for IKE traffic | Default: enable
    link_cost: int  # VPN tunnel underlay link cost. | Default: 0 | Min: 0 | Max: 255
    kms: str  # Key Management Services server. | MaxLen: 35
    exchange_fgt_device_id: Literal["enable", "disable"]  # Enable/disable device identifier exchange with pee | Default: disable
    ipv6_auto_linklocal: Literal["enable", "disable"]  # Enable/disable auto generation of IPv6 link-local | Default: disable
    ems_sn_check: Literal["enable", "disable"]  # Enable/disable verification of EMS serial number. | Default: disable
    cert_trust_store: Literal["local", "ems"]  # CA certificate trust store. | Default: local
    qkd: Literal["disable", "allow", "require"]  # Enable/disable use of Quantum Key Distribution | Default: disable
    qkd_hybrid: Literal["disable", "allow", "require"]  # Enable/disable use of Quantum Key Distribution | Default: disable
    qkd_profile: str  # Quantum Key Distribution (QKD) server profile. | MaxLen: 35
    transport: Literal["udp", "auto", "tcp"]  # Set IKE transport protocol. | Default: auto
    fortinet_esp: Literal["enable", "disable"]  # Enable/disable Fortinet ESP encapsulation. | Default: disable
    auto_transport_threshold: int  # Timeout in seconds before falling back to next tra | Default: 15 | Min: 1 | Max: 300
    remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"]  # Set type of IPv4 remote gateway address matching. | Default: any
    remote_gw_subnet: str  # IPv4 address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    remote_gw_start_ip: str  # First IPv4 address in the range. | Default: 0.0.0.0
    remote_gw_end_ip: str  # Last IPv4 address in the range. | Default: 0.0.0.0
    remote_gw_country: str  # IPv4 addresses associated to a specific country. | MaxLen: 2
    remote_gw_ztna_tags: list[Phase1InterfaceRemotegwztnatagsItem]  # IPv4 ZTNA posture tags.
    remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"]  # Set type of IPv6 remote gateway address matching. | Default: any
    remote_gw6_subnet: str  # IPv6 address and prefix. | Default: ::/0
    remote_gw6_start_ip: str  # First IPv6 address in the range. | Default: ::
    remote_gw6_end_ip: str  # Last IPv6 address in the range. | Default: ::
    remote_gw6_country: str  # IPv6 addresses associated to a specific country. | MaxLen: 2
    cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"]  # Enable/disable cross validation of peer username a | Default: none
    cert_peer_username_strip: Literal["disable", "enable"]  # Enable/disable domain stripping on certificate ide | Default: disable


@final
class Phase1InterfaceObject:
    """Typed FortiObject for vpn/ipsec/phase1_interface with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # IPsec remote gateway name. | MaxLen: 15
    name: str
    # Remote gateway type. | Default: static
    type: Literal["static", "dynamic", "ddns"]
    # Local physical, aggregate, or VLAN outgoing interface. | MaxLen: 35
    interface: str
    # IP version to use for VPN interface. | Default: 4
    ip_version: Literal["4", "6"]
    # IKE protocol version. | Default: 1
    ike_version: Literal["1", "2"]
    # IPv4 address of the local gateway's external interface. | Default: 0.0.0.0
    local_gw: str
    # IPv6 address of the local gateway's external interface. | Default: ::
    local_gw6: str
    # IPv4 address of the remote gateway's external interface. | Default: 0.0.0.0
    remote_gw: str
    # IPv6 address of the remote gateway's external interface. | Default: ::
    remote_gw6: str
    # Domain name of remote gateway. For example, name.ddns.com. | MaxLen: 63
    remotegw_ddns: str
    # Time to wait in seconds before phase 1 encryption key expire | Default: 86400 | Min: 120 | Max: 172800
    keylife: int
    # The names of up to 4 signed personal certificates.
    certificate: list[Phase1InterfaceCertificateObject]
    # Authentication method. | Default: psk
    authmethod: Literal["psk", "signature"]
    # Authentication method (remote side).
    authmethod_remote: Literal["psk", "signature"]
    # The ID protection mode used to establish a secure channel. | Default: main
    mode: Literal["aggressive", "main"]
    # Accept this peer type. | Default: peer
    peertype: Literal["any", "one", "dialup", "peer", "peergrp"]
    # Accept this peer identity. | MaxLen: 255
    peerid: str
    # IPv4 address of default route gateway to use for traffic exi | Default: 0.0.0.0
    default_gw: str
    # Priority for default gateway route. A higher priority number | Default: 0 | Min: 0 | Max: 4294967295
    default_gw_priority: int
    # User group name for dialup peers. | MaxLen: 35
    usrgrp: str
    # Accept this peer certificate. | MaxLen: 35
    peer: str
    # Accept this peer certificate group. | MaxLen: 35
    peergrp: str
    # IPsec interface as backup for primary interface.
    monitor: list[Phase1InterfaceMonitorObject]
    # Minimum number of links to become degraded before activating | Default: 0 | Min: 0 | Max: 4294967295
    monitor_min: int
    # Recovery time method when primary interface re-establishes. | Default: immediate
    monitor_hold_down_type: Literal["immediate", "delay", "time"]
    # Time to wait in seconds before recovery once primary re-esta | Default: 0 | Min: 0 | Max: 31536000
    monitor_hold_down_delay: int
    # Day of the week to recover once primary re-establishes. | Default: sunday
    monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # Time of day at which to fail back to primary after it re-est
    monitor_hold_down_time: str
    # Enable/disable kernel device creation. | Default: disable
    net_device: Literal["enable", "disable"]
    # Enable/disable IPsec passive mode for static tunnels. | Default: disable
    passive_mode: Literal["enable", "disable"]
    # Enable/disable exchange of IPsec interface IP address. | Default: disable
    exchange_interface_ip: Literal["enable", "disable"]
    # IPv4 address to exchange with peers. | Default: 0.0.0.0
    exchange_ip_addr4: str
    # IPv6 address to exchange with peers. | Default: ::
    exchange_ip_addr6: str
    # Enable/disable use as an aggregate member. | Default: disable
    aggregate_member: Literal["enable", "disable"]
    # Link weight for aggregate. | Default: 1 | Min: 1 | Max: 100
    aggregate_weight: int
    # Enable/disable packet distribution (RPS) on the IPsec interf | Default: disable
    packet_redistribution: Literal["enable", "disable"]
    # Enable/disable peer egress shaping. | Default: disable
    peer_egress_shaping: Literal["enable", "disable"]
    # Configure outbound bandwidth to use for peer egress shaping | Default: 0 | Min: 0 | Max: 80000000
    peer_egress_shaping_value: int
    # Enable/disable configuration method. | Default: disable
    mode_cfg: Literal["disable", "enable"]
    # Enable/disable mode-cfg client to use custom phase2 selector | Default: disable
    mode_cfg_allow_client_selector: Literal["disable", "enable"]
    # Enable/disable assignment of IP to IPsec interface via confi | Default: enable
    assign_ip: Literal["disable", "enable"]
    # Method by which the IP address will be assigned. | Default: range
    assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"]
    # Start of IPv4 range. | Default: 0.0.0.0
    ipv4_start_ip: str
    # End of IPv4 range. | Default: 0.0.0.0
    ipv4_end_ip: str
    # IPv4 Netmask. | Default: 255.255.255.255
    ipv4_netmask: str
    # Relay agent gateway IP address to use in the giaddr field of | Default: 0.0.0.0
    dhcp_ra_giaddr: str
    # Relay agent IPv6 link address to use in DHCP6 requests. | Default: ::
    dhcp6_ra_linkaddr: str
    # DNS server mode. | Default: manual
    dns_mode: Literal["manual", "auto"]
    # IPv4 DNS server 1. | Default: 0.0.0.0
    ipv4_dns_server1: str
    # IPv4 DNS server 2. | Default: 0.0.0.0
    ipv4_dns_server2: str
    # IPv4 DNS server 3. | Default: 0.0.0.0
    ipv4_dns_server3: str
    # One or more internal domain names in quotes separated by spa
    internal_domain_list: list[Phase1InterfaceInternaldomainlistObject]
    # One or more DNS domain name suffixes in quotes separated by
    dns_suffix_search: list[Phase1InterfaceDnssuffixsearchObject]
    # WINS server 1. | Default: 0.0.0.0
    ipv4_wins_server1: str
    # WINS server 2. | Default: 0.0.0.0
    ipv4_wins_server2: str
    # Configuration Method IPv4 exclude ranges.
    ipv4_exclude_range: list[Phase1InterfaceIpv4excluderangeObject]
    # IPv4 split-include subnets. | MaxLen: 79
    ipv4_split_include: str
    # Split-include services. | MaxLen: 79
    split_include_service: str
    # IPv4 address name. | MaxLen: 79
    ipv4_name: str
    # Start of IPv6 range. | Default: ::
    ipv6_start_ip: str
    # End of IPv6 range. | Default: ::
    ipv6_end_ip: str
    # IPv6 prefix. | Default: 128 | Min: 1 | Max: 128
    ipv6_prefix: int
    # IPv6 DNS server 1. | Default: ::
    ipv6_dns_server1: str
    # IPv6 DNS server 2. | Default: ::
    ipv6_dns_server2: str
    # IPv6 DNS server 3. | Default: ::
    ipv6_dns_server3: str
    # Configuration method IPv6 exclude ranges.
    ipv6_exclude_range: list[Phase1InterfaceIpv6excluderangeObject]
    # IPv6 split-include subnets. | MaxLen: 79
    ipv6_split_include: str
    # IPv6 address name. | MaxLen: 79
    ipv6_name: str
    # IP address reuse delay interval in seconds (0 - 28800). | Default: 0 | Min: 0 | Max: 28800
    ip_delay_interval: int
    # Enable/disable support for Cisco UNITY Configuration Method | Default: enable
    unity_support: Literal["disable", "enable"]
    # Instruct unity clients about the single default DNS domain. | MaxLen: 63
    domain: str
    # Message that unity client should display after connecting. | MaxLen: 1024
    banner: str
    # Enable/disable allow local LAN access on unity clients. | Default: disable
    include_local_lan: Literal["disable", "enable"]
    # IPv4 subnets that should not be sent over the IPsec tunnel. | MaxLen: 79
    ipv4_split_exclude: str
    # IPv6 subnets that should not be sent over the IPsec tunnel. | MaxLen: 79
    ipv6_split_exclude: str
    # Enable/disable saving XAuth username and password on VPN cli | Default: disable
    save_password: Literal["disable", "enable"]
    # Enable/disable allowing the VPN client to bring up the tunne | Default: disable
    client_auto_negotiate: Literal["disable", "enable"]
    # Enable/disable allowing the VPN client to keep the tunnel up | Default: disable
    client_keep_alive: Literal["disable", "enable"]
    # Instruct unity clients about the backup gateway address(es).
    backup_gateway: list[Phase1InterfaceBackupgatewayObject]
    # Phase1 proposal.
    proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"]
    # Enable/disable control addition of a route to peer destinati | Default: enable
    add_route: Literal["disable", "enable"]
    # Enable/disable automatically add a route to the remote gatew | Default: disable
    add_gw_route: Literal["enable", "disable"]
    # Pre-shared secret for PSK authentication
    psksecret: str
    # Pre-shared secret for remote side PSK authentication
    psksecret_remote: str
    # NAT-T keep alive interval. | Default: 10 | Min: 5 | Max: 900
    keepalive: int
    # Distance for routes added by IKE (1 - 255). | Default: 15 | Min: 1 | Max: 255
    distance: int
    # Priority for routes added by IKE (1 - 65535). | Default: 1 | Min: 1 | Max: 65535
    priority: int
    # Local ID. | MaxLen: 63
    localid: str
    # Local ID type. | Default: auto
    localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"]
    # Enable/disable automatic initiation of IKE SA negotiation. | Default: enable
    auto_negotiate: Literal["enable", "disable"]
    # IKE SA negotiation timeout in seconds (1 - 300). | Default: 30 | Min: 1 | Max: 300
    negotiate_timeout: int
    # Enable/disable fragment IKE message on re-transmission. | Default: enable
    fragmentation: Literal["enable", "disable"]
    # Determine whether IP packets are fragmented before or after | Default: post-encapsulation
    ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"]
    # Dead Peer Detection mode. | Default: on-demand
    dpd: Literal["disable", "on-idle", "on-demand"]
    # Number of DPD retry attempts. | Default: 3 | Min: 1 | Max: 10
    dpd_retrycount: int
    # DPD retry interval.
    dpd_retryinterval: str
    # Comment. | MaxLen: 255
    comments: str
    # Enable/disable offloading NPU. | Default: enable
    npu_offload: Literal["enable", "disable"]
    # Enable/disable sending certificate chain. | Default: enable
    send_cert_chain: Literal["enable", "disable"]
    # DH group. | Default: 20
    dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"]
    # ADDKE1 group.
    addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # ADDKE2 group.
    addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # ADDKE3 group.
    addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # ADDKE4 group.
    addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # ADDKE5 group.
    addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # ADDKE6 group.
    addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # ADDKE7 group.
    addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"]
    # Use Suite-B. | Default: disable
    suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"]
    # Enable/disable IKEv2 EAP authentication. | Default: disable
    eap: Literal["enable", "disable"]
    # IKEv2 EAP peer identity type. | Default: use-id-payload
    eap_identity: Literal["use-id-payload", "send-request"]
    # Peer group excluded from EAP authentication. | MaxLen: 35
    eap_exclude_peergrp: str
    # Enable/disable peer certificate authentication in addition t | Default: disable
    eap_cert_auth: Literal["enable", "disable"]
    # Enable/disable verification of RADIUS accounting record. | Default: disable
    acct_verify: Literal["enable", "disable"]
    # Enable/disable IKEv2 Postquantum Preshared Key (PPK). | Default: disable
    ppk: Literal["disable", "allow", "require"]
    # IKEv2 Postquantum Preshared Key
    ppk_secret: str
    # IKEv2 Postquantum Preshared Key Identity. | MaxLen: 35
    ppk_identity: str
    # GUI VPN Wizard Type. | Default: custom
    wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"]
    # XAuth type. | Default: disable
    xauthtype: Literal["disable", "client", "pap", "chap", "auto"]
    # Enable/disable re-authentication upon IKE SA lifetime expira | Default: disable
    reauth: Literal["disable", "enable"]
    # XAuth user name. | MaxLen: 64
    authusr: str
    # XAuth password (max 35 characters). | MaxLen: 128
    authpasswd: str
    # Enable/disable IKEv2 IDi group authentication. | Default: disable
    group_authentication: Literal["enable", "disable"]
    # Password for IKEv2 ID group authentication. ASCII string or
    group_authentication_secret: str
    # Authentication user group. | MaxLen: 35
    authusrgrp: str
    # Add selectors containing subsets of the configuration depend | Default: disable
    mesh_selector_type: Literal["disable", "subnet", "host"]
    # Enable/disable IPsec tunnel idle timeout. | Default: disable
    idle_timeout: Literal["enable", "disable"]
    # Enable/disable IPsec tunnel shared idle timeout. | Default: disable
    shared_idle_timeout: Literal["enable", "disable"]
    # IPsec tunnel idle timeout in minutes (5 - 43200). | Default: 15 | Min: 5 | Max: 43200
    idle_timeoutinterval: int
    # Enable/disable sequence number jump ahead for IPsec HA. | Default: enable
    ha_sync_esp_seqno: Literal["enable", "disable"]
    # Enable/disable IPsec syncing of tunnels for FGSP IPsec. | Default: disable
    fgsp_sync: Literal["enable", "disable"]
    # Enable/disable copy the dscp in the ESP header to the inner | Default: disable
    inbound_dscp_copy: Literal["enable", "disable"]
    # Enable/disable sending auto-discovery short-cut messages. | Default: disable
    auto_discovery_sender: Literal["enable", "disable"]
    # Enable/disable accepting auto-discovery short-cut messages. | Default: disable
    auto_discovery_receiver: Literal["enable", "disable"]
    # Enable/disable forwarding auto-discovery short-cut messages. | Default: disable
    auto_discovery_forwarder: Literal["enable", "disable"]
    # Enable/disable use of pre-shared secrets for authentication | Default: disable
    auto_discovery_psk: Literal["enable", "disable"]
    # Control deletion of child short-cut tunnels when the parent | Default: independent
    auto_discovery_shortcuts: Literal["independent", "dependent"]
    # Allow/block set-up of short-cut tunnels between different ne | Default: allow
    auto_discovery_crossover: Literal["allow", "block"]
    # Interval between shortcut offer messages in seconds | Default: 5 | Min: 1 | Max: 300
    auto_discovery_offer_interval: int
    # Control if this dynamic gateway is used for shortcut connect | Default: disable
    auto_discovery_dialup_placeholder: Literal["disable", "enable"]
    # Enable/disable GRE/VXLAN/VPNID encapsulation. | Default: none
    encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"]
    # Source for GRE/VXLAN tunnel address. | Default: ike
    encapsulation_address: Literal["ike", "ipv4", "ipv6"]
    # Local IPv4 address of GRE/VXLAN tunnel. | Default: 0.0.0.0
    encap_local_gw4: str
    # Local IPv6 address of GRE/VXLAN tunnel. | Default: ::
    encap_local_gw6: str
    # Remote IPv4 address of GRE/VXLAN tunnel. | Default: 0.0.0.0
    encap_remote_gw4: str
    # Remote IPv6 address of GRE/VXLAN tunnel. | Default: ::
    encap_remote_gw6: str
    # VNI of VXLAN tunnel. | Default: 0 | Min: 1 | Max: 16777215
    vni: int
    # Enable/disable NAT traversal. | Default: enable
    nattraversal: Literal["enable", "disable", "forced"]
    # Extended sequence number (ESN) negotiation. | Default: disable
    esn: Literal["require", "allow", "disable"]
    # IKE fragmentation MTU (500 - 16000). | Default: 1200 | Min: 500 | Max: 16000
    fragmentation_mtu: int
    # Enable/disable childless IKEv2 initiation (RFC 6023). | Default: disable
    childless_ike: Literal["enable", "disable"]
    # Enable/disable Azure AD Auto-Connect for FortiClient. | Default: disable
    azure_ad_autoconnect: Literal["enable", "disable"]
    # Enable/disable resumption of offline FortiClient sessions. | Default: disable
    client_resume: Literal["enable", "disable"]
    # Maximum time in seconds during which a VPN client may resume | Default: 7200 | Min: 120 | Max: 172800
    client_resume_interval: int
    # Enable/disable phase1 rekey. | Default: enable
    rekey: Literal["enable", "disable"]
    # Enable/disable IKEv2 Digital Signature Authentication | Default: disable
    digital_signature_auth: Literal["enable", "disable"]
    # Digital Signature Authentication hash algorithms. | Default: sha2-512
    signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"]
    # Digital Signature Authentication RSA signature format. | Default: pkcs1
    rsa_signature_format: Literal["pkcs1", "pss"]
    # Enable/disable IKEv2 RSA signature hash algorithm override. | Default: disable
    rsa_signature_hash_override: Literal["enable", "disable"]
    # Enable/disable peer ID uniqueness check. | Default: disable
    enforce_unique_id: Literal["disable", "keep-new", "keep-old"]
    # Enable/disable cross validation of peer ID and the identity | Default: enable
    cert_id_validation: Literal["enable", "disable"]
    # Enable/disable Forward Error Correction for egress IPsec tra | Default: disable
    fec_egress: Literal["enable", "disable"]
    # Timeout in milliseconds before sending Forward Error Correct | Default: 5 | Min: 1 | Max: 1000
    fec_send_timeout: int
    # Number of base Forward Error Correction packets (1 - 20). | Default: 10 | Min: 1 | Max: 20
    fec_base: int
    # Forward Error Correction encoding/decoding algorithm. | Default: rs
    fec_codec: Literal["rs", "xor"]
    # Number of redundant Forward Error Correction packets | Default: 1 | Min: 1 | Max: 5
    fec_redundant: int
    # Enable/disable Forward Error Correction for ingress IPsec tr | Default: disable
    fec_ingress: Literal["enable", "disable"]
    # Timeout in milliseconds before dropping Forward Error Correc | Default: 50 | Min: 1 | Max: 1000
    fec_receive_timeout: int
    # SD-WAN health check. | MaxLen: 35
    fec_health_check: str
    # Forward Error Correction (FEC) mapping profile. | MaxLen: 35
    fec_mapping_profile: str
    # Enable/disable network overlays. | Default: disable
    network_overlay: Literal["disable", "enable"]
    # VPN gateway network ID. | Default: 0 | Min: 0 | Max: 255
    network_id: int
    # Enable/disable device ID notification. | Default: disable
    dev_id_notification: Literal["disable", "enable"]
    # Device ID carried by the device ID notification. | MaxLen: 63
    dev_id: str
    # Enable/disable asymmetric routing for IKE traffic on loopbac | Default: enable
    loopback_asymroute: Literal["enable", "disable"]
    # VPN tunnel underlay link cost. | Default: 0 | Min: 0 | Max: 255
    link_cost: int
    # Key Management Services server. | MaxLen: 35
    kms: str
    # Enable/disable device identifier exchange with peer FortiGat | Default: disable
    exchange_fgt_device_id: Literal["enable", "disable"]
    # Enable/disable auto generation of IPv6 link-local address us | Default: disable
    ipv6_auto_linklocal: Literal["enable", "disable"]
    # Enable/disable verification of EMS serial number. | Default: disable
    ems_sn_check: Literal["enable", "disable"]
    # CA certificate trust store. | Default: local
    cert_trust_store: Literal["local", "ems"]
    # Enable/disable use of Quantum Key Distribution (QKD) server. | Default: disable
    qkd: Literal["disable", "allow", "require"]
    # Enable/disable use of Quantum Key Distribution (QKD) hybrid | Default: disable
    qkd_hybrid: Literal["disable", "allow", "require"]
    # Quantum Key Distribution (QKD) server profile. | MaxLen: 35
    qkd_profile: str
    # Set IKE transport protocol. | Default: auto
    transport: Literal["udp", "auto", "tcp"]
    # Enable/disable Fortinet ESP encapsulation. | Default: disable
    fortinet_esp: Literal["enable", "disable"]
    # Timeout in seconds before falling back to next transport pro | Default: 15 | Min: 1 | Max: 300
    auto_transport_threshold: int
    # Set type of IPv4 remote gateway address matching. | Default: any
    remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"]
    # IPv4 address and subnet mask. | Default: 0.0.0.0 0.0.0.0
    remote_gw_subnet: str
    # First IPv4 address in the range. | Default: 0.0.0.0
    remote_gw_start_ip: str
    # Last IPv4 address in the range. | Default: 0.0.0.0
    remote_gw_end_ip: str
    # IPv4 addresses associated to a specific country. | MaxLen: 2
    remote_gw_country: str
    # IPv4 ZTNA posture tags.
    remote_gw_ztna_tags: list[Phase1InterfaceRemotegwztnatagsObject]
    # Set type of IPv6 remote gateway address matching. | Default: any
    remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"]
    # IPv6 address and prefix. | Default: ::/0
    remote_gw6_subnet: str
    # First IPv6 address in the range. | Default: ::
    remote_gw6_start_ip: str
    # Last IPv6 address in the range. | Default: ::
    remote_gw6_end_ip: str
    # IPv6 addresses associated to a specific country. | MaxLen: 2
    remote_gw6_country: str
    # Enable/disable cross validation of peer username and the ide | Default: none
    cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"]
    # Enable/disable domain stripping on certificate identity. | Default: disable
    cert_peer_username_strip: Literal["disable", "enable"]
    
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
    def to_dict(self) -> Phase1InterfacePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Phase1Interface:
    """
    Configure VPN remote gateway.
    
    Path: vpn/ipsec/phase1_interface
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
    ) -> Phase1InterfaceObject: ...
    
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
    ) -> Phase1InterfaceObject: ...
    
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
    ) -> FortiObjectList[Phase1InterfaceObject]: ...
    
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
    ) -> Phase1InterfaceObject: ...
    
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
    ) -> Phase1InterfaceObject: ...
    
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
    ) -> FortiObjectList[Phase1InterfaceObject]: ...
    
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
    ) -> Phase1InterfaceObject: ...
    
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
    ) -> Phase1InterfaceObject: ...
    
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
    ) -> FortiObjectList[Phase1InterfaceObject]: ...
    
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
    ) -> Phase1InterfaceObject | list[Phase1InterfaceObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Phase1InterfaceObject: ...
    
    @overload
    def post(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> Phase1InterfaceObject: ...
    
    @overload
    def put(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> Phase1InterfaceObject: ...
    
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
        payload_dict: Phase1InterfacePayload | None = ...,
        name: str | None = ...,
        type: Literal["static", "dynamic", "ddns"] | None = ...,
        interface: str | None = ...,
        ip_version: Literal["4", "6"] | None = ...,
        ike_version: Literal["1", "2"] | None = ...,
        local_gw: str | None = ...,
        local_gw6: str | None = ...,
        remote_gw: str | None = ...,
        remote_gw6: str | None = ...,
        remotegw_ddns: str | None = ...,
        keylife: int | None = ...,
        certificate: str | list[str] | list[dict[str, Any]] | None = ...,
        authmethod: Literal["psk", "signature"] | None = ...,
        authmethod_remote: Literal["psk", "signature"] | None = ...,
        mode: Literal["aggressive", "main"] | None = ...,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = ...,
        peerid: str | None = ...,
        default_gw: str | None = ...,
        default_gw_priority: int | None = ...,
        usrgrp: str | None = ...,
        peer: str | None = ...,
        peergrp: str | None = ...,
        monitor: str | list[str] | list[dict[str, Any]] | None = ...,
        monitor_min: int | None = ...,
        monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = ...,
        monitor_hold_down_delay: int | None = ...,
        monitor_hold_down_weekday: Literal["everyday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] | None = ...,
        monitor_hold_down_time: str | None = ...,
        net_device: Literal["enable", "disable"] | None = ...,
        passive_mode: Literal["enable", "disable"] | None = ...,
        exchange_interface_ip: Literal["enable", "disable"] | None = ...,
        exchange_ip_addr4: str | None = ...,
        exchange_ip_addr6: str | None = ...,
        aggregate_member: Literal["enable", "disable"] | None = ...,
        aggregate_weight: int | None = ...,
        packet_redistribution: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping: Literal["enable", "disable"] | None = ...,
        peer_egress_shaping_value: int | None = ...,
        mode_cfg: Literal["disable", "enable"] | None = ...,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = ...,
        assign_ip: Literal["disable", "enable"] | None = ...,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = ...,
        ipv4_start_ip: str | None = ...,
        ipv4_end_ip: str | None = ...,
        ipv4_netmask: str | None = ...,
        dhcp_ra_giaddr: str | None = ...,
        dhcp6_ra_linkaddr: str | None = ...,
        dns_mode: Literal["manual", "auto"] | None = ...,
        ipv4_dns_server1: str | None = ...,
        ipv4_dns_server2: str | None = ...,
        ipv4_dns_server3: str | None = ...,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = ...,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_wins_server1: str | None = ...,
        ipv4_wins_server2: str | None = ...,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv4_split_include: str | None = ...,
        split_include_service: str | None = ...,
        ipv4_name: str | None = ...,
        ipv6_start_ip: str | None = ...,
        ipv6_end_ip: str | None = ...,
        ipv6_prefix: int | None = ...,
        ipv6_dns_server1: str | None = ...,
        ipv6_dns_server2: str | None = ...,
        ipv6_dns_server3: str | None = ...,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = ...,
        ipv6_split_include: str | None = ...,
        ipv6_name: str | None = ...,
        ip_delay_interval: int | None = ...,
        unity_support: Literal["disable", "enable"] | None = ...,
        domain: str | None = ...,
        banner: str | None = ...,
        include_local_lan: Literal["disable", "enable"] | None = ...,
        ipv4_split_exclude: str | None = ...,
        ipv6_split_exclude: str | None = ...,
        save_password: Literal["disable", "enable"] | None = ...,
        client_auto_negotiate: Literal["disable", "enable"] | None = ...,
        client_keep_alive: Literal["disable", "enable"] | None = ...,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = ...,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = ...,
        add_route: Literal["disable", "enable"] | None = ...,
        add_gw_route: Literal["enable", "disable"] | None = ...,
        psksecret: str | None = ...,
        psksecret_remote: str | None = ...,
        keepalive: int | None = ...,
        distance: int | None = ...,
        priority: int | None = ...,
        localid: str | None = ...,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = ...,
        auto_negotiate: Literal["enable", "disable"] | None = ...,
        negotiate_timeout: int | None = ...,
        fragmentation: Literal["enable", "disable"] | None = ...,
        ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = ...,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = ...,
        dpd_retrycount: int | None = ...,
        dpd_retryinterval: str | None = ...,
        comments: str | None = ...,
        npu_offload: Literal["enable", "disable"] | None = ...,
        send_cert_chain: Literal["enable", "disable"] | None = ...,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = ...,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = ...,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = ...,
        eap: Literal["enable", "disable"] | None = ...,
        eap_identity: Literal["use-id-payload", "send-request"] | None = ...,
        eap_exclude_peergrp: str | None = ...,
        eap_cert_auth: Literal["enable", "disable"] | None = ...,
        acct_verify: Literal["enable", "disable"] | None = ...,
        ppk: Literal["disable", "allow", "require"] | None = ...,
        ppk_secret: str | None = ...,
        ppk_identity: str | None = ...,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = ...,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = ...,
        reauth: Literal["disable", "enable"] | None = ...,
        authusr: str | None = ...,
        authpasswd: str | None = ...,
        group_authentication: Literal["enable", "disable"] | None = ...,
        group_authentication_secret: str | None = ...,
        authusrgrp: str | None = ...,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = ...,
        idle_timeout: Literal["enable", "disable"] | None = ...,
        shared_idle_timeout: Literal["enable", "disable"] | None = ...,
        idle_timeoutinterval: int | None = ...,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = ...,
        fgsp_sync: Literal["enable", "disable"] | None = ...,
        inbound_dscp_copy: Literal["enable", "disable"] | None = ...,
        auto_discovery_sender: Literal["enable", "disable"] | None = ...,
        auto_discovery_receiver: Literal["enable", "disable"] | None = ...,
        auto_discovery_forwarder: Literal["enable", "disable"] | None = ...,
        auto_discovery_psk: Literal["enable", "disable"] | None = ...,
        auto_discovery_shortcuts: Literal["independent", "dependent"] | None = ...,
        auto_discovery_crossover: Literal["allow", "block"] | None = ...,
        auto_discovery_offer_interval: int | None = ...,
        auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = ...,
        encapsulation: Literal["none", "gre", "vxlan", "vpn-id-ipip"] | None = ...,
        encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = ...,
        encap_local_gw4: str | None = ...,
        encap_local_gw6: str | None = ...,
        encap_remote_gw4: str | None = ...,
        encap_remote_gw6: str | None = ...,
        vni: int | None = ...,
        nattraversal: Literal["enable", "disable", "forced"] | None = ...,
        esn: Literal["require", "allow", "disable"] | None = ...,
        fragmentation_mtu: int | None = ...,
        childless_ike: Literal["enable", "disable"] | None = ...,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = ...,
        client_resume: Literal["enable", "disable"] | None = ...,
        client_resume_interval: int | None = ...,
        rekey: Literal["enable", "disable"] | None = ...,
        digital_signature_auth: Literal["enable", "disable"] | None = ...,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = ...,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = ...,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = ...,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = ...,
        cert_id_validation: Literal["enable", "disable"] | None = ...,
        fec_egress: Literal["enable", "disable"] | None = ...,
        fec_send_timeout: int | None = ...,
        fec_base: int | None = ...,
        fec_codec: Literal["rs", "xor"] | None = ...,
        fec_redundant: int | None = ...,
        fec_ingress: Literal["enable", "disable"] | None = ...,
        fec_receive_timeout: int | None = ...,
        fec_health_check: str | None = ...,
        fec_mapping_profile: str | None = ...,
        network_overlay: Literal["disable", "enable"] | None = ...,
        network_id: int | None = ...,
        dev_id_notification: Literal["disable", "enable"] | None = ...,
        dev_id: str | None = ...,
        loopback_asymroute: Literal["enable", "disable"] | None = ...,
        link_cost: int | None = ...,
        kms: str | None = ...,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = ...,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = ...,
        ems_sn_check: Literal["enable", "disable"] | None = ...,
        cert_trust_store: Literal["local", "ems"] | None = ...,
        qkd: Literal["disable", "allow", "require"] | None = ...,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = ...,
        qkd_profile: str | None = ...,
        transport: Literal["udp", "auto", "tcp"] | None = ...,
        fortinet_esp: Literal["enable", "disable"] | None = ...,
        auto_transport_threshold: int | None = ...,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = ...,
        remote_gw_subnet: str | None = ...,
        remote_gw_start_ip: str | None = ...,
        remote_gw_end_ip: str | None = ...,
        remote_gw_country: str | None = ...,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = ...,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = ...,
        remote_gw6_subnet: str | None = ...,
        remote_gw6_start_ip: str | None = ...,
        remote_gw6_end_ip: str | None = ...,
        remote_gw6_country: str | None = ...,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = ...,
        cert_peer_username_strip: Literal["disable", "enable"] | None = ...,
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
    "Phase1Interface",
    "Phase1InterfacePayload",
    "Phase1InterfaceResponse",
    "Phase1InterfaceObject",
]
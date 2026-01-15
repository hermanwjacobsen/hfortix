"""
Pydantic Models for CMDB - vpn/ipsec/phase1_interface

Runtime validation models for vpn/ipsec/phase1_interface configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class Phase1InterfaceCertificate(BaseModel):
    """
    Child table model for certificate.
    
    The names of up to 4 signed personal certificates.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Certificate name.")  # datasource: ['vpn.certificate.local.name']
class Phase1InterfaceMonitor(BaseModel):
    """
    Child table model for monitor.
    
    IPsec interface as backup for primary interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="IPsec interface as backup for primary interface.")  # datasource: ['vpn.ipsec.phase1-interface.name']
class Phase1InterfaceInternalDomainList(BaseModel):
    """
    Child table model for internal-domain-list.
    
    One or more internal domain names in quotes separated by spaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    domain_name: str = Field(max_length=79, default="", description="Domain name.")
class Phase1InterfaceDnsSuffixSearch(BaseModel):
    """
    Child table model for dns-suffix-search.
    
    One or more DNS domain name suffixes in quotes separated by spaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    dns_suffix: str = Field(max_length=79, default="", description="DNS suffix.")
class Phase1InterfaceIpv4ExcludeRange(BaseModel):
    """
    Child table model for ipv4-exclude-range.
    
    Configuration Method IPv4 exclude ranges.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    start_ip: str = Field(default="0.0.0.0", description="Start of IPv4 exclusive range.")    
    end_ip: str = Field(default="0.0.0.0", description="End of IPv4 exclusive range.")
class Phase1InterfaceIpv6ExcludeRange(BaseModel):
    """
    Child table model for ipv6-exclude-range.
    
    Configuration method IPv6 exclude ranges.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    start_ip: str = Field(default="::", description="Start of IPv6 exclusive range.")    
    end_ip: str = Field(default="::", description="End of IPv6 exclusive range.")
class Phase1InterfaceBackupGateway(BaseModel):
    """
    Child table model for backup-gateway.
    
    Instruct unity clients about the backup gateway address(es).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    address: str = Field(max_length=79, default="", description="Address of backup gateway.")
class Phase1InterfaceRemoteGwZtnaTags(BaseModel):
    """
    Child table model for remote-gw-ztna-tags.
    
    IPv4 ZTNA posture tags.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class Phase1InterfacePeertypeEnum(str, Enum):
    """Allowed values for peertype field."""
    ANY = "any"    ONE = "one"    DIALUP = "dialup"    PEER = "peer"    PEERGRP = "peergrp"
class Phase1InterfaceMonitor_hold_down_weekdayEnum(str, Enum):
    """Allowed values for monitor_hold_down_weekday field."""
    EVERYDAY = "everyday"    SUNDAY = "sunday"    MONDAY = "monday"    TUESDAY = "tuesday"    WEDNESDAY = "wednesday"    THURSDAY = "thursday"    FRIDAY = "friday"    SATURDAY = "saturday"
class Phase1InterfaceAssign_ip_fromEnum(str, Enum):
    """Allowed values for assign_ip_from field."""
    RANGE = "range"    USRGRP = "usrgrp"    DHCP = "dhcp"    NAME = "name"
class Phase1InterfaceProposalEnum(str, Enum):
    """Allowed values for proposal field."""
    DES_MD5 = "des-md5"    DES_SHA1 = "des-sha1"    DES_SHA256 = "des-sha256"    DES_SHA384 = "des-sha384"    DES_SHA512 = "des-sha512"    3DES_MD5 = "3des-md5"    3DES_SHA1 = "3des-sha1"    3DES_SHA256 = "3des-sha256"    3DES_SHA384 = "3des-sha384"    3DES_SHA512 = "3des-sha512"    AES128_MD5 = "aes128-md5"    AES128_SHA1 = "aes128-sha1"    AES128_SHA256 = "aes128-sha256"    AES128_SHA384 = "aes128-sha384"    AES128_SHA512 = "aes128-sha512"    AES128GCM_PRFSHA1 = "aes128gcm-prfsha1"    AES128GCM_PRFSHA256 = "aes128gcm-prfsha256"    AES128GCM_PRFSHA384 = "aes128gcm-prfsha384"    AES128GCM_PRFSHA512 = "aes128gcm-prfsha512"    AES192_MD5 = "aes192-md5"    AES192_SHA1 = "aes192-sha1"    AES192_SHA256 = "aes192-sha256"    AES192_SHA384 = "aes192-sha384"    AES192_SHA512 = "aes192-sha512"    AES256_MD5 = "aes256-md5"    AES256_SHA1 = "aes256-sha1"    AES256_SHA256 = "aes256-sha256"    AES256_SHA384 = "aes256-sha384"    AES256_SHA512 = "aes256-sha512"    AES256GCM_PRFSHA1 = "aes256gcm-prfsha1"    AES256GCM_PRFSHA256 = "aes256gcm-prfsha256"    AES256GCM_PRFSHA384 = "aes256gcm-prfsha384"    AES256GCM_PRFSHA512 = "aes256gcm-prfsha512"    CHACHA20POLY1305_PRFSHA1 = "chacha20poly1305-prfsha1"    CHACHA20POLY1305_PRFSHA256 = "chacha20poly1305-prfsha256"    CHACHA20POLY1305_PRFSHA384 = "chacha20poly1305-prfsha384"    CHACHA20POLY1305_PRFSHA512 = "chacha20poly1305-prfsha512"    ARIA128_MD5 = "aria128-md5"    ARIA128_SHA1 = "aria128-sha1"    ARIA128_SHA256 = "aria128-sha256"    ARIA128_SHA384 = "aria128-sha384"    ARIA128_SHA512 = "aria128-sha512"    ARIA192_MD5 = "aria192-md5"    ARIA192_SHA1 = "aria192-sha1"    ARIA192_SHA256 = "aria192-sha256"    ARIA192_SHA384 = "aria192-sha384"    ARIA192_SHA512 = "aria192-sha512"    ARIA256_MD5 = "aria256-md5"    ARIA256_SHA1 = "aria256-sha1"    ARIA256_SHA256 = "aria256-sha256"    ARIA256_SHA384 = "aria256-sha384"    ARIA256_SHA512 = "aria256-sha512"    SEED_MD5 = "seed-md5"    SEED_SHA1 = "seed-sha1"    SEED_SHA256 = "seed-sha256"    SEED_SHA384 = "seed-sha384"    SEED_SHA512 = "seed-sha512"
class Phase1InterfaceLocalid_typeEnum(str, Enum):
    """Allowed values for localid_type field."""
    AUTO = "auto"    FQDN = "fqdn"    USER_FQDN = "user-fqdn"    KEYID = "keyid"    ADDRESS = "address"    ASN1DN = "asn1dn"
class Phase1InterfaceDhgrpEnum(str, Enum):
    """Allowed values for dhgrp field."""
    1 = "1"    2 = "2"    5 = "5"    14 = "14"    15 = "15"    16 = "16"    17 = "17"    18 = "18"    19 = "19"    20 = "20"    21 = "21"    27 = "27"    28 = "28"    29 = "29"    30 = "30"    31 = "31"    32 = "32"
class Phase1InterfaceAddke1Enum(str, Enum):
    """Allowed values for addke1 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase1InterfaceAddke2Enum(str, Enum):
    """Allowed values for addke2 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase1InterfaceAddke3Enum(str, Enum):
    """Allowed values for addke3 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase1InterfaceAddke4Enum(str, Enum):
    """Allowed values for addke4 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase1InterfaceAddke5Enum(str, Enum):
    """Allowed values for addke5 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase1InterfaceAddke6Enum(str, Enum):
    """Allowed values for addke6 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase1InterfaceAddke7Enum(str, Enum):
    """Allowed values for addke7 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase1InterfaceWizard_typeEnum(str, Enum):
    """Allowed values for wizard_type field."""
    CUSTOM = "custom"    DIALUP_FORTICLIENT = "dialup-forticlient"    DIALUP_IOS = "dialup-ios"    DIALUP_ANDROID = "dialup-android"    DIALUP_WINDOWS = "dialup-windows"    DIALUP_CISCO = "dialup-cisco"    STATIC_FORTIGATE = "static-fortigate"    DIALUP_FORTIGATE = "dialup-fortigate"    STATIC_CISCO = "static-cisco"    DIALUP_CISCO_FW = "dialup-cisco-fw"    SIMPLIFIED_STATIC_FORTIGATE = "simplified-static-fortigate"    HUB_FORTIGATE_AUTO_DISCOVERY = "hub-fortigate-auto-discovery"    SPOKE_FORTIGATE_AUTO_DISCOVERY = "spoke-fortigate-auto-discovery"    FABRIC_OVERLAY_ORCHESTRATOR = "fabric-overlay-orchestrator"
class Phase1InterfaceXauthtypeEnum(str, Enum):
    """Allowed values for xauthtype field."""
    DISABLE = "disable"    CLIENT = "client"    PAP = "pap"    CHAP = "chap"    AUTO = "auto"
class Phase1InterfaceEncapsulationEnum(str, Enum):
    """Allowed values for encapsulation field."""
    NONE = "none"    GRE = "gre"    VXLAN = "vxlan"    VPN_ID_IPIP = "vpn-id-ipip"
class Phase1InterfaceSignature_hash_algEnum(str, Enum):
    """Allowed values for signature_hash_alg field."""
    SHA1 = "sha1"    SHA2_256 = "sha2-256"    SHA2_384 = "sha2-384"    SHA2_512 = "sha2-512"
class Phase1InterfaceRemote_gw_matchEnum(str, Enum):
    """Allowed values for remote_gw_match field."""
    ANY = "any"    IPMASK = "ipmask"    IPRANGE = "iprange"    GEOGRAPHY = "geography"    ZTNA = "ztna"
class Phase1InterfaceRemote_gw6_matchEnum(str, Enum):
    """Allowed values for remote_gw6_match field."""
    ANY = "any"    IPPREFIX = "ipprefix"    IPRANGE = "iprange"    GEOGRAPHY = "geography"
class Phase1InterfaceCert_peer_username_validationEnum(str, Enum):
    """Allowed values for cert_peer_username_validation field."""
    NONE = "none"    OTHERNAME = "othername"    RFC822NAME = "rfc822name"    CN = "cn"

# ============================================================================
# Main Model
# ============================================================================

class Phase1InterfaceModel(BaseModel):
    """
    Pydantic model for vpn/ipsec/phase1_interface configuration.
    
    Configure VPN remote gateway.
    
    Validation Rules:        - name: max_length=15 pattern=        - type: pattern=        - interface: max_length=35 pattern=        - ip_version: pattern=        - ike_version: pattern=        - local_gw: pattern=        - local_gw6: pattern=        - remote_gw: pattern=        - remote_gw6: pattern=        - remotegw_ddns: max_length=63 pattern=        - keylife: min=120 max=172800 pattern=        - certificate: pattern=        - authmethod: pattern=        - authmethod_remote: pattern=        - mode: pattern=        - peertype: pattern=        - peerid: max_length=255 pattern=        - default_gw: pattern=        - default_gw_priority: min=0 max=4294967295 pattern=        - usrgrp: max_length=35 pattern=        - peer: max_length=35 pattern=        - peergrp: max_length=35 pattern=        - monitor: pattern=        - monitor_min: min=0 max=4294967295 pattern=        - monitor_hold_down_type: pattern=        - monitor_hold_down_delay: min=0 max=31536000 pattern=        - monitor_hold_down_weekday: pattern=        - monitor_hold_down_time: pattern=        - net_device: pattern=        - passive_mode: pattern=        - exchange_interface_ip: pattern=        - exchange_ip_addr4: pattern=        - exchange_ip_addr6: pattern=        - aggregate_member: pattern=        - aggregate_weight: min=1 max=100 pattern=        - packet_redistribution: pattern=        - peer_egress_shaping: pattern=        - peer_egress_shaping_value: min=0 max=80000000 pattern=        - mode_cfg: pattern=        - mode_cfg_allow_client_selector: pattern=        - assign_ip: pattern=        - assign_ip_from: pattern=        - ipv4_start_ip: pattern=        - ipv4_end_ip: pattern=        - ipv4_netmask: pattern=        - dhcp_ra_giaddr: pattern=        - dhcp6_ra_linkaddr: pattern=        - dns_mode: pattern=        - ipv4_dns_server1: pattern=        - ipv4_dns_server2: pattern=        - ipv4_dns_server3: pattern=        - internal_domain_list: pattern=        - dns_suffix_search: pattern=        - ipv4_wins_server1: pattern=        - ipv4_wins_server2: pattern=        - ipv4_exclude_range: pattern=        - ipv4_split_include: max_length=79 pattern=        - split_include_service: max_length=79 pattern=        - ipv4_name: max_length=79 pattern=        - ipv6_start_ip: pattern=        - ipv6_end_ip: pattern=        - ipv6_prefix: min=1 max=128 pattern=        - ipv6_dns_server1: pattern=        - ipv6_dns_server2: pattern=        - ipv6_dns_server3: pattern=        - ipv6_exclude_range: pattern=        - ipv6_split_include: max_length=79 pattern=        - ipv6_name: max_length=79 pattern=        - ip_delay_interval: min=0 max=28800 pattern=        - unity_support: pattern=        - domain: max_length=63 pattern=        - banner: max_length=1024 pattern=        - include_local_lan: pattern=        - ipv4_split_exclude: max_length=79 pattern=        - ipv6_split_exclude: max_length=79 pattern=        - save_password: pattern=        - client_auto_negotiate: pattern=        - client_keep_alive: pattern=        - backup_gateway: pattern=        - proposal: pattern=        - add_route: pattern=        - add_gw_route: pattern=        - psksecret: pattern=        - psksecret_remote: pattern=        - keepalive: min=5 max=900 pattern=        - distance: min=1 max=255 pattern=        - priority: min=1 max=65535 pattern=        - localid: max_length=63 pattern=        - localid_type: pattern=        - auto_negotiate: pattern=        - negotiate_timeout: min=1 max=300 pattern=        - fragmentation: pattern=        - ip_fragmentation: pattern=        - dpd: pattern=        - dpd_retrycount: min=1 max=10 pattern=        - dpd_retryinterval: pattern=        - comments: max_length=255 pattern=        - npu_offload: pattern=        - send_cert_chain: pattern=        - dhgrp: pattern=        - addke1: pattern=        - addke2: pattern=        - addke3: pattern=        - addke4: pattern=        - addke5: pattern=        - addke6: pattern=        - addke7: pattern=        - suite_b: pattern=        - eap: pattern=        - eap_identity: pattern=        - eap_exclude_peergrp: max_length=35 pattern=        - eap_cert_auth: pattern=        - acct_verify: pattern=        - ppk: pattern=        - ppk_secret: pattern=        - ppk_identity: max_length=35 pattern=        - wizard_type: pattern=        - xauthtype: pattern=        - reauth: pattern=        - authusr: max_length=64 pattern=        - authpasswd: max_length=128 pattern=        - group_authentication: pattern=        - group_authentication_secret: pattern=        - authusrgrp: max_length=35 pattern=        - mesh_selector_type: pattern=        - idle_timeout: pattern=        - shared_idle_timeout: pattern=        - idle_timeoutinterval: min=5 max=43200 pattern=        - ha_sync_esp_seqno: pattern=        - fgsp_sync: pattern=        - inbound_dscp_copy: pattern=        - auto_discovery_sender: pattern=        - auto_discovery_receiver: pattern=        - auto_discovery_forwarder: pattern=        - auto_discovery_psk: pattern=        - auto_discovery_shortcuts: pattern=        - auto_discovery_crossover: pattern=        - auto_discovery_offer_interval: min=1 max=300 pattern=        - auto_discovery_dialup_placeholder: pattern=        - encapsulation: pattern=        - encapsulation_address: pattern=        - encap_local_gw4: pattern=        - encap_local_gw6: pattern=        - encap_remote_gw4: pattern=        - encap_remote_gw6: pattern=        - vni: min=1 max=16777215 pattern=        - nattraversal: pattern=        - esn: pattern=        - fragmentation_mtu: min=500 max=16000 pattern=        - childless_ike: pattern=        - azure_ad_autoconnect: pattern=        - client_resume: pattern=        - client_resume_interval: min=120 max=172800 pattern=        - rekey: pattern=        - digital_signature_auth: pattern=        - signature_hash_alg: pattern=        - rsa_signature_format: pattern=        - rsa_signature_hash_override: pattern=        - enforce_unique_id: pattern=        - cert_id_validation: pattern=        - fec_egress: pattern=        - fec_send_timeout: min=1 max=1000 pattern=        - fec_base: min=1 max=20 pattern=        - fec_codec: pattern=        - fec_redundant: min=1 max=5 pattern=        - fec_ingress: pattern=        - fec_receive_timeout: min=1 max=1000 pattern=        - fec_health_check: max_length=35 pattern=        - fec_mapping_profile: max_length=35 pattern=        - network_overlay: pattern=        - network_id: min=0 max=255 pattern=        - dev_id_notification: pattern=        - dev_id: max_length=63 pattern=        - loopback_asymroute: pattern=        - link_cost: min=0 max=255 pattern=        - kms: max_length=35 pattern=        - exchange_fgt_device_id: pattern=        - ipv6_auto_linklocal: pattern=        - ems_sn_check: pattern=        - cert_trust_store: pattern=        - qkd: pattern=        - qkd_hybrid: pattern=        - qkd_profile: max_length=35 pattern=        - transport: pattern=        - fortinet_esp: pattern=        - auto_transport_threshold: min=1 max=300 pattern=        - remote_gw_match: pattern=        - remote_gw_subnet: pattern=        - remote_gw_start_ip: pattern=        - remote_gw_end_ip: pattern=        - remote_gw_country: max_length=2 pattern=        - remote_gw_ztna_tags: pattern=        - remote_gw6_match: pattern=        - remote_gw6_subnet: pattern=        - remote_gw6_start_ip: pattern=        - remote_gw6_end_ip: pattern=        - remote_gw6_country: max_length=2 pattern=        - cert_peer_username_validation: pattern=        - cert_peer_username_strip: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="IPsec remote gateway name.")    
    type: Literal["static", "dynamic", "ddns"] | None = Field(default="static", description="Remote gateway type.")    
    interface: str = Field(max_length=35, default="", description="Local physical, aggregate, or VLAN outgoing interface.")  # datasource: ['system.interface.name']    
    ip_version: Literal["4", "6"] | None = Field(default="4", description="IP version to use for VPN interface.")    
    ike_version: Literal["1", "2"] | None = Field(default="1", description="IKE protocol version.")    
    local_gw: str | None = Field(default="0.0.0.0", description="IPv4 address of the local gateway's external interface.")    
    local_gw6: str | None = Field(default="::", description="IPv6 address of the local gateway's external interface.")    
    remote_gw: str = Field(default="0.0.0.0", description="IPv4 address of the remote gateway's external interface.")    
    remote_gw6: str = Field(default="::", description="IPv6 address of the remote gateway's external interface.")    
    remotegw_ddns: str = Field(max_length=63, default="", description="Domain name of remote gateway. For example, name.ddns.com.")    
    keylife: int | None = Field(ge=120, le=172800, default=86400, description="Time to wait in seconds before phase 1 encryption key expires.")    
    certificate: list[Certificate] = Field(description="The names of up to 4 signed personal certificates.")    
    authmethod: Literal["psk", "signature"] | None = Field(default="psk", description="Authentication method.")    
    authmethod_remote: Literal["psk", "signature"] | None = Field(default="", description="Authentication method (remote side).")    
    mode: Literal["aggressive", "main"] | None = Field(default="main", description="The ID protection mode used to establish a secure channel.")    
    peertype: PeertypeEnum | None = Field(default="peer", description="Accept this peer type.")    
    peerid: str = Field(max_length=255, default="", description="Accept this peer identity.")    
    default_gw: str | None = Field(default="0.0.0.0", description="IPv4 address of default route gateway to use for traffic exiting the interface.")    
    default_gw_priority: int | None = Field(ge=0, le=4294967295, default=0, description="Priority for default gateway route. A higher priority number signifies a less preferred route.")    
    usrgrp: str = Field(max_length=35, default="", description="User group name for dialup peers.")  # datasource: ['user.group.name']    
    peer: str = Field(max_length=35, default="", description="Accept this peer certificate.")  # datasource: ['user.peer.name']    
    peergrp: str = Field(max_length=35, default="", description="Accept this peer certificate group.")  # datasource: ['user.peergrp.name']    
    monitor: list[Monitor] = Field(default=None, description="IPsec interface as backup for primary interface.")    
    monitor_min: int | None = Field(ge=0, le=4294967295, default=0, description="Minimum number of links to become degraded before activating this interface.  Zero (0) means all links must be down before activating this interface.")    
    monitor_hold_down_type: Literal["immediate", "delay", "time"] | None = Field(default="immediate", description="Recovery time method when primary interface re-establishes.")    
    monitor_hold_down_delay: int = Field(ge=0, le=31536000, default=0, description="Time to wait in seconds before recovery once primary re-establishes.")    
    monitor_hold_down_weekday: MonitorHoldDownWeekdayEnum = Field(default="sunday", description="Day of the week to recover once primary re-establishes.")    
    monitor_hold_down_time: str = Field(default="", description="Time of day at which to fail back to primary after it re-establishes.")    
    net_device: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable kernel device creation.")    
    passive_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPsec passive mode for static tunnels.")    
    exchange_interface_ip: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable exchange of IPsec interface IP address.")    
    exchange_ip_addr4: str | None = Field(default="0.0.0.0", description="IPv4 address to exchange with peers.")    
    exchange_ip_addr6: str | None = Field(default="::", description="IPv6 address to exchange with peers.")    
    aggregate_member: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use as an aggregate member.")    
    aggregate_weight: int | None = Field(ge=1, le=100, default=1, description="Link weight for aggregate.")    
    packet_redistribution: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable packet distribution (RPS) on the IPsec interface.")    
    peer_egress_shaping: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable peer egress shaping.")    
    peer_egress_shaping_value: int = Field(ge=0, le=80000000, default=0, description="Configure outbound bandwidth to use for peer egress shaping in kbps (0 - 80000000, default = 0).")    
    mode_cfg: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable configuration method.")    
    mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable mode-cfg client to use custom phase2 selectors.")    
    assign_ip: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable assignment of IP to IPsec interface via configuration method.")    
    assign_ip_from: AssignIpFromEnum | None = Field(default="range", description="Method by which the IP address will be assigned.")    
    ipv4_start_ip: str = Field(default="0.0.0.0", description="Start of IPv4 range.")    
    ipv4_end_ip: str = Field(default="0.0.0.0", description="End of IPv4 range.")    
    ipv4_netmask: str | None = Field(default="255.255.255.255", description="IPv4 Netmask.")    
    dhcp_ra_giaddr: str | None = Field(default="0.0.0.0", description="Relay agent gateway IP address to use in the giaddr field of DHCP requests.")    
    dhcp6_ra_linkaddr: str | None = Field(default="::", description="Relay agent IPv6 link address to use in DHCP6 requests.")    
    dns_mode: Literal["manual", "auto"] | None = Field(default="manual", description="DNS server mode.")    
    ipv4_dns_server1: str | None = Field(default="0.0.0.0", description="IPv4 DNS server 1.")    
    ipv4_dns_server2: str | None = Field(default="0.0.0.0", description="IPv4 DNS server 2.")    
    ipv4_dns_server3: str | None = Field(default="0.0.0.0", description="IPv4 DNS server 3.")    
    internal_domain_list: list[InternalDomainList] = Field(default=None, description="One or more internal domain names in quotes separated by spaces.")    
    dns_suffix_search: list[DnsSuffixSearch] = Field(default=None, description="One or more DNS domain name suffixes in quotes separated by spaces.")    
    ipv4_wins_server1: str | None = Field(default="0.0.0.0", description="WINS server 1.")    
    ipv4_wins_server2: str | None = Field(default="0.0.0.0", description="WINS server 2.")    
    ipv4_exclude_range: list[Ipv4ExcludeRange] = Field(default=None, description="Configuration Method IPv4 exclude ranges.")    
    ipv4_split_include: str | None = Field(max_length=79, default="", description="IPv4 split-include subnets.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    split_include_service: str | None = Field(max_length=79, default="", description="Split-include services.")  # datasource: ['firewall.service.group.name', 'firewall.service.custom.name']    
    ipv4_name: str | None = Field(max_length=79, default="", description="IPv4 address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    ipv6_start_ip: str = Field(default="::", description="Start of IPv6 range.")    
    ipv6_end_ip: str = Field(default="::", description="End of IPv6 range.")    
    ipv6_prefix: int | None = Field(ge=1, le=128, default=128, description="IPv6 prefix.")    
    ipv6_dns_server1: str | None = Field(default="::", description="IPv6 DNS server 1.")    
    ipv6_dns_server2: str | None = Field(default="::", description="IPv6 DNS server 2.")    
    ipv6_dns_server3: str | None = Field(default="::", description="IPv6 DNS server 3.")    
    ipv6_exclude_range: list[Ipv6ExcludeRange] = Field(default=None, description="Configuration method IPv6 exclude ranges.")    
    ipv6_split_include: str | None = Field(max_length=79, default="", description="IPv6 split-include subnets.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']    
    ipv6_name: str | None = Field(max_length=79, default="", description="IPv6 address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']    
    ip_delay_interval: int | None = Field(ge=0, le=28800, default=0, description="IP address reuse delay interval in seconds (0 - 28800).")    
    unity_support: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable support for Cisco UNITY Configuration Method extensions.")    
    domain: str | None = Field(max_length=63, default="", description="Instruct unity clients about the single default DNS domain.")    
    banner: str | None = Field(max_length=1024, default=None, description="Message that unity client should display after connecting.")    
    include_local_lan: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allow local LAN access on unity clients.")    
    ipv4_split_exclude: str | None = Field(max_length=79, default="", description="IPv4 subnets that should not be sent over the IPsec tunnel.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    ipv6_split_exclude: str | None = Field(max_length=79, default="", description="IPv6 subnets that should not be sent over the IPsec tunnel.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']    
    save_password: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable saving XAuth username and password on VPN clients.")    
    client_auto_negotiate: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allowing the VPN client to bring up the tunnel when there is no traffic.")    
    client_keep_alive: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allowing the VPN client to keep the tunnel up when there is no traffic.")    
    backup_gateway: list[BackupGateway] = Field(default=None, description="Instruct unity clients about the backup gateway address(es).")    
    proposal: list[Proposal] = Field(default="", description="Phase1 proposal.")    
    add_route: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable control addition of a route to peer destination selector.")    
    add_gw_route: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatically add a route to the remote gateway.")    
    psksecret: Any = Field(description="Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).")    
    psksecret_remote: Any = Field(description="Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).")    
    keepalive: int | None = Field(ge=5, le=900, default=10, description="NAT-T keep alive interval.")    
    distance: int | None = Field(ge=1, le=255, default=15, description="Distance for routes added by IKE (1 - 255).")    
    priority: int | None = Field(ge=1, le=65535, default=1, description="Priority for routes added by IKE (1 - 65535).")    
    localid: str | None = Field(max_length=63, default="", description="Local ID.")    
    localid_type: LocalidTypeEnum | None = Field(default="auto", description="Local ID type.")    
    auto_negotiate: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable automatic initiation of IKE SA negotiation.")    
    negotiate_timeout: int | None = Field(ge=1, le=300, default=30, description="IKE SA negotiation timeout in seconds (1 - 300).")    
    fragmentation: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable fragment IKE message on re-transmission.")    
    ip_fragmentation: Literal["pre-encapsulation", "post-encapsulation"] | None = Field(default="post-encapsulation", description="Determine whether IP packets are fragmented before or after IPsec encapsulation.")    
    dpd: Literal["disable", "on-idle", "on-demand"] | None = Field(default="on-demand", description="Dead Peer Detection mode.")    
    dpd_retrycount: int | None = Field(ge=1, le=10, default=3, description="Number of DPD retry attempts.")    
    dpd_retryinterval: str | None = Field(default="", description="DPD retry interval.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    npu_offload: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable offloading NPU.")    
    send_cert_chain: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending certificate chain.")    
    dhgrp: list[Dhgrp] = Field(default="20", description="DH group.")    
    addke1: list[Addke1] = Field(default="", description="ADDKE1 group.")    
    addke2: list[Addke2] = Field(default="", description="ADDKE2 group.")    
    addke3: list[Addke3] = Field(default="", description="ADDKE3 group.")    
    addke4: list[Addke4] = Field(default="", description="ADDKE4 group.")    
    addke5: list[Addke5] = Field(default="", description="ADDKE5 group.")    
    addke6: list[Addke6] = Field(default="", description="ADDKE6 group.")    
    addke7: list[Addke7] = Field(default="", description="ADDKE7 group.")    
    suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = Field(default="disable", description="Use Suite-B.")    
    eap: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IKEv2 EAP authentication.")    
    eap_identity: Literal["use-id-payload", "send-request"] | None = Field(default="use-id-payload", description="IKEv2 EAP peer identity type.")    
    eap_exclude_peergrp: str | None = Field(max_length=35, default="", description="Peer group excluded from EAP authentication.")  # datasource: ['user.peergrp.name']    
    eap_cert_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable peer certificate authentication in addition to EAP if peer is a FortiClient endpoint.")    
    acct_verify: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable verification of RADIUS accounting record.")    
    ppk: Literal["disable", "allow", "require"] | None = Field(default="disable", description="Enable/disable IKEv2 Postquantum Preshared Key (PPK).")    
    ppk_secret: Any = Field(description="IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).")    
    ppk_identity: str | None = Field(max_length=35, default="", description="IKEv2 Postquantum Preshared Key Identity.")    
    wizard_type: WizardTypeEnum | None = Field(default="custom", description="GUI VPN Wizard Type.")    
    xauthtype: XauthtypeEnum | None = Field(default="disable", description="XAuth type.")    
    reauth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable re-authentication upon IKE SA lifetime expiration.")    
    authusr: str = Field(max_length=64, default="", description="XAuth user name.")    
    authpasswd: Any = Field(max_length=128, description="XAuth password (max 35 characters).")    
    group_authentication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IKEv2 IDi group authentication.")    
    group_authentication_secret: Any = Field(description="Password for IKEv2 ID group authentication. ASCII string or hexadecimal indicated by a leading 0x.")    
    authusrgrp: str | None = Field(max_length=35, default="", description="Authentication user group.")  # datasource: ['user.group.name']    
    mesh_selector_type: Literal["disable", "subnet", "host"] | None = Field(default="disable", description="Add selectors containing subsets of the configuration depending on traffic.")    
    idle_timeout: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPsec tunnel idle timeout.")    
    shared_idle_timeout: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPsec tunnel shared idle timeout.")    
    idle_timeoutinterval: int | None = Field(ge=5, le=43200, default=15, description="IPsec tunnel idle timeout in minutes (5 - 43200).")    
    ha_sync_esp_seqno: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sequence number jump ahead for IPsec HA.")    
    fgsp_sync: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPsec syncing of tunnels for FGSP IPsec.")    
    inbound_dscp_copy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable copy the dscp in the ESP header to the inner IP Header.")    
    auto_discovery_sender: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending auto-discovery short-cut messages.")    
    auto_discovery_receiver: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable accepting auto-discovery short-cut messages.")    
    auto_discovery_forwarder: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable forwarding auto-discovery short-cut messages.")    
    auto_discovery_psk: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of pre-shared secrets for authentication of auto-discovery tunnels.")    
    auto_discovery_shortcuts: Literal["independent", "dependent"] | None = Field(default="independent", description="Control deletion of child short-cut tunnels when the parent tunnel goes down.")    
    auto_discovery_crossover: Literal["allow", "block"] | None = Field(default="allow", description="Allow/block set-up of short-cut tunnels between different network IDs.")    
    auto_discovery_offer_interval: int | None = Field(ge=1, le=300, default=5, description="Interval between shortcut offer messages in seconds (1 - 300, default = 5).")    
    auto_discovery_dialup_placeholder: Literal["disable", "enable"] | None = Field(default="disable", description="Control if this dynamic gateway is used for shortcut connections only.")    
    encapsulation: EncapsulationEnum | None = Field(default="none", description="Enable/disable GRE/VXLAN/VPNID encapsulation.")    
    encapsulation_address: Literal["ike", "ipv4", "ipv6"] | None = Field(default="ike", description="Source for GRE/VXLAN tunnel address.")    
    encap_local_gw4: str = Field(default="0.0.0.0", description="Local IPv4 address of GRE/VXLAN tunnel.")    
    encap_local_gw6: str = Field(default="::", description="Local IPv6 address of GRE/VXLAN tunnel.")    
    encap_remote_gw4: str = Field(default="0.0.0.0", description="Remote IPv4 address of GRE/VXLAN tunnel.")    
    encap_remote_gw6: str = Field(default="::", description="Remote IPv6 address of GRE/VXLAN tunnel.")    
    vni: int | None = Field(ge=1, le=16777215, default=0, description="VNI of VXLAN tunnel.")    
    nattraversal: Literal["enable", "disable", "forced"] | None = Field(default="enable", description="Enable/disable NAT traversal.")    
    esn: Literal["require", "allow", "disable"] | None = Field(default="disable", description="Extended sequence number (ESN) negotiation.")    
    fragmentation_mtu: int | None = Field(ge=500, le=16000, default=1200, description="IKE fragmentation MTU (500 - 16000).")    
    childless_ike: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable childless IKEv2 initiation (RFC 6023).")    
    azure_ad_autoconnect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Azure AD Auto-Connect for FortiClient.")    
    client_resume: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable resumption of offline FortiClient sessions.  When a FortiClient enabled laptop is closed or enters sleep/hibernate mode, enabling this feature allows FortiClient to keep the tunnel during this period, and allows users to immediately resume using the IPsec tunnel when the device wakes up.")    
    client_resume_interval: int | None = Field(ge=120, le=172800, default=7200, description="Maximum time in seconds during which a VPN client may resume using a tunnel after a client PC has entered sleep mode or temporarily lost its network connection (120 - 172800, default = 7200).")    
    rekey: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable phase1 rekey.")    
    digital_signature_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IKEv2 Digital Signature Authentication (RFC 7427).")    
    signature_hash_alg: list[SignatureHashAlg] = Field(default="sha2-512", description="Digital Signature Authentication hash algorithms.")    
    rsa_signature_format: Literal["pkcs1", "pss"] | None = Field(default="pkcs1", description="Digital Signature Authentication RSA signature format.")    
    rsa_signature_hash_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IKEv2 RSA signature hash algorithm override.")    
    enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = Field(default="disable", description="Enable/disable peer ID uniqueness check.")    
    cert_id_validation: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945.")    
    fec_egress: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Forward Error Correction for egress IPsec traffic.")    
    fec_send_timeout: int | None = Field(ge=1, le=1000, default=5, description="Timeout in milliseconds before sending Forward Error Correction packets (1 - 1000).")    
    fec_base: int | None = Field(ge=1, le=20, default=10, description="Number of base Forward Error Correction packets (1 - 20).")    
    fec_codec: Literal["rs", "xor"] | None = Field(default="rs", description="Forward Error Correction encoding/decoding algorithm.")    
    fec_redundant: int | None = Field(ge=1, le=5, default=1, description="Number of redundant Forward Error Correction packets (1 - 5 for reed-solomon, 1 for xor).")    
    fec_ingress: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Forward Error Correction for ingress IPsec traffic.")    
    fec_receive_timeout: int | None = Field(ge=1, le=1000, default=50, description="Timeout in milliseconds before dropping Forward Error Correction packets (1 - 1000).")    
    fec_health_check: str | None = Field(max_length=35, default="", description="SD-WAN health check.")  # datasource: ['system.sdwan.health-check.name']    
    fec_mapping_profile: str | None = Field(max_length=35, default="", description="Forward Error Correction (FEC) mapping profile.")  # datasource: ['vpn.ipsec.fec.name']    
    network_overlay: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable network overlays.")    
    network_id: int = Field(ge=0, le=255, default=0, description="VPN gateway network ID.")    
    dev_id_notification: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable device ID notification.")    
    dev_id: str = Field(max_length=63, default="", description="Device ID carried by the device ID notification.")    
    loopback_asymroute: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable asymmetric routing for IKE traffic on loopback interface.")    
    link_cost: int | None = Field(ge=0, le=255, default=0, description="VPN tunnel underlay link cost.")    
    kms: str | None = Field(max_length=35, default="", description="Key Management Services server.")  # datasource: ['vpn.kmip-server.name']    
    exchange_fgt_device_id: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable device identifier exchange with peer FortiGate units for use of VPN monitor data by FortiManager.")    
    ipv6_auto_linklocal: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable auto generation of IPv6 link-local address using last 8 bytes of mode-cfg assigned IPv6 address.")    
    ems_sn_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable verification of EMS serial number.")    
    cert_trust_store: Literal["local", "ems"] | None = Field(default="local", description="CA certificate trust store.")    
    qkd: Literal["disable", "allow", "require"] | None = Field(default="disable", description="Enable/disable use of Quantum Key Distribution (QKD) server.")    
    qkd_hybrid: Literal["disable", "allow", "require"] | None = Field(default="disable", description="Enable/disable use of Quantum Key Distribution (QKD) hybrid keys.")    
    qkd_profile: str | None = Field(max_length=35, default="", description="Quantum Key Distribution (QKD) server profile.")  # datasource: ['vpn.qkd.name']    
    transport: Literal["udp", "auto", "tcp"] | None = Field(default="auto", description="Set IKE transport protocol.")    
    fortinet_esp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Fortinet ESP encapsulation.")    
    auto_transport_threshold: int | None = Field(ge=1, le=300, default=15, description="Timeout in seconds before falling back to next transport protocol.")    
    remote_gw_match: RemoteGwMatchEnum | None = Field(default="any", description="Set type of IPv4 remote gateway address matching.")    
    remote_gw_subnet: Any = Field(default="0.0.0.0 0.0.0.0", description="IPv4 address and subnet mask.")    
    remote_gw_start_ip: str | None = Field(default="0.0.0.0", description="First IPv4 address in the range.")    
    remote_gw_end_ip: str | None = Field(default="0.0.0.0", description="Last IPv4 address in the range.")    
    remote_gw_country: str | None = Field(max_length=2, default="", description="IPv4 addresses associated to a specific country.")    
    remote_gw_ztna_tags: list[RemoteGwZtnaTags] = Field(description="IPv4 ZTNA posture tags.")    
    remote_gw6_match: RemoteGw6MatchEnum | None = Field(default="any", description="Set type of IPv6 remote gateway address matching.")    
    remote_gw6_subnet: str | None = Field(default="::/0", description="IPv6 address and prefix.")    
    remote_gw6_start_ip: str | None = Field(default="::", description="First IPv6 address in the range.")    
    remote_gw6_end_ip: str | None = Field(default="::", description="Last IPv6 address in the range.")    
    remote_gw6_country: str | None = Field(max_length=2, default="", description="IPv6 addresses associated to a specific country.")    
    cert_peer_username_validation: CertPeerUsernameValidationEnum | None = Field(default="none", description="Enable/disable cross validation of peer username and the identity in the peer's certificate.")    
    cert_peer_username_strip: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable domain stripping on certificate identity.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    @field_validator('usrgrp')
    @classmethod
    def validate_usrgrp(cls, v: Any) -> Any:
        """
        Validate usrgrp field.
        
        Datasource: ['user.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('peer')
    @classmethod
    def validate_peer(cls, v: Any) -> Any:
        """
        Validate peer field.
        
        Datasource: ['user.peer.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('peergrp')
    @classmethod
    def validate_peergrp(cls, v: Any) -> Any:
        """
        Validate peergrp field.
        
        Datasource: ['user.peergrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ipv4_split_include')
    @classmethod
    def validate_ipv4_split_include(cls, v: Any) -> Any:
        """
        Validate ipv4_split_include field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('split_include_service')
    @classmethod
    def validate_split_include_service(cls, v: Any) -> Any:
        """
        Validate split_include_service field.
        
        Datasource: ['firewall.service.group.name', 'firewall.service.custom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ipv4_name')
    @classmethod
    def validate_ipv4_name(cls, v: Any) -> Any:
        """
        Validate ipv4_name field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ipv6_split_include')
    @classmethod
    def validate_ipv6_split_include(cls, v: Any) -> Any:
        """
        Validate ipv6_split_include field.
        
        Datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ipv6_name')
    @classmethod
    def validate_ipv6_name(cls, v: Any) -> Any:
        """
        Validate ipv6_name field.
        
        Datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ipv4_split_exclude')
    @classmethod
    def validate_ipv4_split_exclude(cls, v: Any) -> Any:
        """
        Validate ipv4_split_exclude field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ipv6_split_exclude')
    @classmethod
    def validate_ipv6_split_exclude(cls, v: Any) -> Any:
        """
        Validate ipv6_split_exclude field.
        
        Datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('eap_exclude_peergrp')
    @classmethod
    def validate_eap_exclude_peergrp(cls, v: Any) -> Any:
        """
        Validate eap_exclude_peergrp field.
        
        Datasource: ['user.peergrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('authusrgrp')
    @classmethod
    def validate_authusrgrp(cls, v: Any) -> Any:
        """
        Validate authusrgrp field.
        
        Datasource: ['user.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fec_health_check')
    @classmethod
    def validate_fec_health_check(cls, v: Any) -> Any:
        """
        Validate fec_health_check field.
        
        Datasource: ['system.sdwan.health-check.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fec_mapping_profile')
    @classmethod
    def validate_fec_mapping_profile(cls, v: Any) -> Any:
        """
        Validate fec_mapping_profile field.
        
        Datasource: ['vpn.ipsec.fec.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('kms')
    @classmethod
    def validate_kms(cls, v: Any) -> Any:
        """
        Validate kms field.
        
        Datasource: ['vpn.kmip-server.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('qkd_profile')
    @classmethod
    def validate_qkd_profile(cls, v: Any) -> Any:
        """
        Validate qkd_profile field.
        
        Datasource: ['vpn.qkd.name']
        
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
            >>> policy = Phase1InterfaceModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
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
    async def validate_certificate_references(self, client: Any) -> list[str]:
        """
        Validate certificate references exist in FortiGate.
        
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
            >>> policy = Phase1InterfaceModel(
            ...     certificate=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "certificate", [])
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
            if await client.api.cmdb.vpn.certificate.local.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Certificate '{value}' not found in "
                    "vpn/certificate/local"
                )        
        return errors    
    async def validate_usrgrp_references(self, client: Any) -> list[str]:
        """
        Validate usrgrp references exist in FortiGate.
        
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
            >>> policy = Phase1InterfaceModel(
            ...     usrgrp="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_usrgrp_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "usrgrp", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Usrgrp '{value}' not found in "
                "user/group"
            )        
        return errors    
    async def validate_peer_references(self, client: Any) -> list[str]:
        """
        Validate peer references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/peer        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     peer="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_peer_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "peer", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.peer.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Peer '{value}' not found in "
                "user/peer"
            )        
        return errors    
    async def validate_peergrp_references(self, client: Any) -> list[str]:
        """
        Validate peergrp references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/peergrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     peergrp="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_peergrp_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "peergrp", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.peergrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Peergrp '{value}' not found in "
                "user/peergrp"
            )        
        return errors    
    async def validate_monitor_references(self, client: Any) -> list[str]:
        """
        Validate monitor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/ipsec/phase1-interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     monitor=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_monitor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "monitor", [])
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
            if await client.api.cmdb.vpn.ipsec.phase1-interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Monitor '{value}' not found in "
                    "vpn/ipsec/phase1-interface"
                )        
        return errors    
    async def validate_ipv4_split_include_references(self, client: Any) -> list[str]:
        """
        Validate ipv4_split_include references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     ipv4_split_include="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ipv4_split_include_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ipv4_split_include", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ipv4-Split-Include '{value}' not found in "
                "firewall/address or firewall/addrgrp"
            )        
        return errors    
    async def validate_split_include_service_references(self, client: Any) -> list[str]:
        """
        Validate split_include_service references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/service/group        - firewall/service/custom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     split_include_service="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_split_include_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "split_include_service", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.service.group.exists(value):
            found = True
        elif await client.api.cmdb.firewall.service.custom.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Split-Include-Service '{value}' not found in "
                "firewall/service/group or firewall/service/custom"
            )        
        return errors    
    async def validate_ipv4_name_references(self, client: Any) -> list[str]:
        """
        Validate ipv4_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     ipv4_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ipv4_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ipv4_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ipv4-Name '{value}' not found in "
                "firewall/address or firewall/addrgrp"
            )        
        return errors    
    async def validate_ipv6_split_include_references(self, client: Any) -> list[str]:
        """
        Validate ipv6_split_include references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     ipv6_split_include="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ipv6_split_include_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ipv6_split_include", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address6.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ipv6-Split-Include '{value}' not found in "
                "firewall/address6 or firewall/addrgrp6"
            )        
        return errors    
    async def validate_ipv6_name_references(self, client: Any) -> list[str]:
        """
        Validate ipv6_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     ipv6_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ipv6_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ipv6_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address6.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ipv6-Name '{value}' not found in "
                "firewall/address6 or firewall/addrgrp6"
            )        
        return errors    
    async def validate_ipv4_split_exclude_references(self, client: Any) -> list[str]:
        """
        Validate ipv4_split_exclude references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     ipv4_split_exclude="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ipv4_split_exclude_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ipv4_split_exclude", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ipv4-Split-Exclude '{value}' not found in "
                "firewall/address or firewall/addrgrp"
            )        
        return errors    
    async def validate_ipv6_split_exclude_references(self, client: Any) -> list[str]:
        """
        Validate ipv6_split_exclude references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     ipv6_split_exclude="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ipv6_split_exclude_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ipv6_split_exclude", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address6.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ipv6-Split-Exclude '{value}' not found in "
                "firewall/address6 or firewall/addrgrp6"
            )        
        return errors    
    async def validate_eap_exclude_peergrp_references(self, client: Any) -> list[str]:
        """
        Validate eap_exclude_peergrp references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/peergrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     eap_exclude_peergrp="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_eap_exclude_peergrp_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "eap_exclude_peergrp", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.peergrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Eap-Exclude-Peergrp '{value}' not found in "
                "user/peergrp"
            )        
        return errors    
    async def validate_authusrgrp_references(self, client: Any) -> list[str]:
        """
        Validate authusrgrp references exist in FortiGate.
        
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
            >>> policy = Phase1InterfaceModel(
            ...     authusrgrp="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_authusrgrp_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "authusrgrp", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Authusrgrp '{value}' not found in "
                "user/group"
            )        
        return errors    
    async def validate_fec_health_check_references(self, client: Any) -> list[str]:
        """
        Validate fec_health_check references exist in FortiGate.
        
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
            >>> policy = Phase1InterfaceModel(
            ...     fec_health_check="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fec_health_check_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fec_health_check", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.sdwan.health-check.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fec-Health-Check '{value}' not found in "
                "system/sdwan/health-check"
            )        
        return errors    
    async def validate_fec_mapping_profile_references(self, client: Any) -> list[str]:
        """
        Validate fec_mapping_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/ipsec/fec        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     fec_mapping_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fec_mapping_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fec_mapping_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.ipsec.fec.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fec-Mapping-Profile '{value}' not found in "
                "vpn/ipsec/fec"
            )        
        return errors    
    async def validate_kms_references(self, client: Any) -> list[str]:
        """
        Validate kms references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/kmip-server        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     kms="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_kms_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "kms", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.kmip-server.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Kms '{value}' not found in "
                "vpn/kmip-server"
            )        
        return errors    
    async def validate_qkd_profile_references(self, client: Any) -> list[str]:
        """
        Validate qkd_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/qkd        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     qkd_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_qkd_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "qkd_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.qkd.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Qkd-Profile '{value}' not found in "
                "vpn/qkd"
            )        
        return errors    
    async def validate_remote_gw_ztna_tags_references(self, client: Any) -> list[str]:
        """
        Validate remote_gw_ztna_tags references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase1InterfaceModel(
            ...     remote_gw_ztna_tags=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_remote_gw_ztna_tags_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase1_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "remote_gw_ztna_tags", [])
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
            if await client.api.cmdb.firewall.address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Remote-Gw-Ztna-Tags '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
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
        
        errors = await self.validate_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_usrgrp_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_peer_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_peergrp_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_monitor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ipv4_split_include_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_split_include_service_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ipv4_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ipv6_split_include_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ipv6_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ipv4_split_exclude_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ipv6_split_exclude_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_eap_exclude_peergrp_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_authusrgrp_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fec_health_check_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fec_mapping_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_kms_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_qkd_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_remote_gw_ztna_tags_references(client)
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
    "Phase1InterfaceModel",    "Phase1InterfaceCertificate",    "Phase1InterfaceMonitor",    "Phase1InterfaceInternalDomainList",    "Phase1InterfaceDnsSuffixSearch",    "Phase1InterfaceIpv4ExcludeRange",    "Phase1InterfaceIpv6ExcludeRange",    "Phase1InterfaceBackupGateway",    "Phase1InterfaceRemoteGwZtnaTags",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.672255Z
# ============================================================================
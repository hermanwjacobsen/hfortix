"""
Pydantic Models for CMDB - firewall/policy

Runtime validation models for firewall/policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class PolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Incoming (ingress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class PolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Outgoing (egress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class PolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source IPv4 address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class PolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination IPv4 address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.vip.name', 'firewall.vipgrp.name', 'system.external-resource.name']
class PolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    Source IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'system.external-resource.name', 'firewall.addrgrp6.name']
class PolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    Destination IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'firewall.vip6.name', 'firewall.vipgrp6.name', 'system.external-resource.name']
class PolicyZtnaEmsTag(BaseModel):
    """
    Child table model for ztna-ems-tag.
    
    Source ztna-ems-tag names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyZtnaEmsTagSecondary(BaseModel):
    """
    Child table model for ztna-ems-tag-secondary.
    
    Source ztna-ems-tag-secondary names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyZtnaGeoTag(BaseModel):
    """
    Child table model for ztna-geo-tag.
    
    Source ztna-geo-tag names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class PolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyNetworkServiceDynamic(BaseModel):
    """
    Child table model for network-service-dynamic.
    
    Dynamic Network Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Dynamic Network Service name.")  # datasource: ['firewall.network-service-dynamic.name']
class PolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicyInternetServiceSrcName(BaseModel):
    """
    Child table model for internet-service-src-name.
    
    Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetServiceSrcGroup(BaseModel):
    """
    Child table model for internet-service-src-group.
    
    Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetServiceSrcCustom(BaseModel):
    """
    Child table model for internet-service-src-custom.
    
    Custom Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyNetworkServiceSrcDynamic(BaseModel):
    """
    Child table model for network-service-src-dynamic.
    
    Dynamic Network Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Dynamic Network Service name.")  # datasource: ['firewall.network-service-dynamic.name']
class PolicyInternetServiceSrcCustomGroup(BaseModel):
    """
    Child table model for internet-service-src-custom-group.
    
    Custom Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicySrcVendorMac(BaseModel):
    """
    Child table model for src-vendor-mac.
    
    Vendor MAC source ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Vendor MAC ID.")  # datasource: ['firewall.vendor-mac.id']
class PolicyInternetService6Name(BaseModel):
    """
    Child table model for internet-service6-name.
    
    IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetService6Group(BaseModel):
    """
    Child table model for internet-service6-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetService6Custom(BaseModel):
    """
    Child table model for internet-service6-custom.
    
    Custom IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyInternetService6CustomGroup(BaseModel):
    """
    Child table model for internet-service6-custom-group.
    
    Custom Internet Service6 group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicyInternetService6SrcName(BaseModel):
    """
    Child table model for internet-service6-src-name.
    
    IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class PolicyInternetService6SrcGroup(BaseModel):
    """
    Child table model for internet-service6-src-group.
    
    Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class PolicyInternetService6SrcCustom(BaseModel):
    """
    Child table model for internet-service6-src-custom.
    
    Custom IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class PolicyInternetService6SrcCustomGroup(BaseModel):
    """
    Child table model for internet-service6-src-custom-group.
    
    Custom Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class PolicyRtpAddr(BaseModel):
    """
    Child table model for rtp-addr.
    
    Address names if this is an RTP NAT policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.internet-service-custom-group.name', 'firewall.addrgrp.name']
class PolicyService(BaseModel):
    """
    Child table model for service.
    
    Service and service group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service and service group names.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class PolicyPcpPoolname(BaseModel):
    """
    Child table model for pcp-poolname.
    
    PCP pool names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="PCP pool name.")  # datasource: ['system.pcp-server.pools.name']
class PolicyPoolname(BaseModel):
    """
    Child table model for poolname.
    
    IP Pool names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IP pool name.")  # datasource: ['firewall.ippool.name']
class PolicyPoolname6(BaseModel):
    """
    Child table model for poolname6.
    
    IPv6 pool names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 pool name.")  # datasource: ['firewall.ippool6.name']
class PolicyNtlmEnabledBrowsers(BaseModel):
    """
    Child table model for ntlm-enabled-browsers.
    
    HTTP-User-Agent value of supported browsers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    user_agent_string: str | None = Field(max_length=79, default="", description="User agent string.")
class PolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Names of user groups that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class PolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Names of individual users that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Names of individual users that can authenticate with this policy.")  # datasource: ['user.local.name', 'user.certificate.name']
class PolicyFssoGroups(BaseModel):
    """
    Child table model for fsso-groups.
    
    Names of FSSO groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=511, default="", description="Names of FSSO groups.")  # datasource: ['user.adgrp.name']
class PolicyCustomLogFields(BaseModel):
    """
    Child table model for custom-log-fields.
    
    Custom fields to append to log messages for this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    field_id: str | None = Field(max_length=35, default="", description="Custom log field.")  # datasource: ['log.custom-field.id']
class PolicySgt(BaseModel):
    """
    Child table model for sgt.
    
    Security group tags.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=65535, default=0, description="Security group tag (1 - 65535).")
class PolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class PolicyInternetServiceSrcFortiguard(BaseModel):
    """
    Child table model for internet-service-src-fortiguard.
    
    FortiGuard Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class PolicyInternetService6Fortiguard(BaseModel):
    """
    Child table model for internet-service6-fortiguard.
    
    FortiGuard IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class PolicyInternetService6SrcFortiguard(BaseModel):
    """
    Child table model for internet-service6-src-fortiguard.
    
    FortiGuard IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class PolicyModel(BaseModel):
    """
    Pydantic model for firewall/policy configuration.
    
    Configure IPv4/IPv6 policies.
    
    Validation Rules:        - policyid: min=0 max=4294967294 pattern=        - status: pattern=        - name: max_length=35 pattern=        - uuid: pattern=        - srcintf: pattern=        - dstintf: pattern=        - action: pattern=        - nat64: pattern=        - nat46: pattern=        - ztna_status: pattern=        - ztna_device_ownership: pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - ztna_ems_tag: pattern=        - ztna_ems_tag_secondary: pattern=        - ztna_tags_match_logic: pattern=        - ztna_geo_tag: pattern=        - internet_service: pattern=        - internet_service_name: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - network_service_dynamic: pattern=        - internet_service_custom_group: pattern=        - internet_service_src: pattern=        - internet_service_src_name: pattern=        - internet_service_src_group: pattern=        - internet_service_src_custom: pattern=        - network_service_src_dynamic: pattern=        - internet_service_src_custom_group: pattern=        - reputation_minimum: min=0 max=4294967295 pattern=        - reputation_direction: pattern=        - src_vendor_mac: pattern=        - internet_service6: pattern=        - internet_service6_name: pattern=        - internet_service6_group: pattern=        - internet_service6_custom: pattern=        - internet_service6_custom_group: pattern=        - internet_service6_src: pattern=        - internet_service6_src_name: pattern=        - internet_service6_src_group: pattern=        - internet_service6_src_custom: pattern=        - internet_service6_src_custom_group: pattern=        - reputation_minimum6: min=0 max=4294967295 pattern=        - reputation_direction6: pattern=        - rtp_nat: pattern=        - rtp_addr: pattern=        - send_deny_packet: pattern=        - firewall_session_dirty: pattern=        - schedule: max_length=35 pattern=        - schedule_timeout: pattern=        - policy_expiry: pattern=        - policy_expiry_date: pattern=        - policy_expiry_date_utc: pattern=        - service: pattern=        - tos_mask: pattern=        - tos: pattern=        - tos_negate: pattern=        - anti_replay: pattern=        - tcp_session_without_syn: pattern=        - geoip_anycast: pattern=        - geoip_match: pattern=        - dynamic_shaping: pattern=        - passive_wan_health_measurement: pattern=        - app_monitor: pattern=        - utm_status: pattern=        - inspection_mode: pattern=        - http_policy_redirect: pattern=        - ssh_policy_redirect: pattern=        - ztna_policy_redirect: pattern=        - webproxy_profile: max_length=63 pattern=        - profile_type: pattern=        - profile_group: max_length=47 pattern=        - profile_protocol_options: max_length=47 pattern=        - ssl_ssh_profile: max_length=47 pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - dnsfilter_profile: max_length=47 pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile: max_length=47 pattern=        - file_filter_profile: max_length=47 pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - voip_profile: max_length=47 pattern=        - ips_voip_filter: max_length=47 pattern=        - sctp_filter_profile: max_length=47 pattern=        - diameter_filter_profile: max_length=47 pattern=        - virtual_patch_profile: max_length=47 pattern=        - icap_profile: max_length=47 pattern=        - videofilter_profile: max_length=47 pattern=        - waf_profile: max_length=47 pattern=        - ssh_filter_profile: max_length=47 pattern=        - casb_profile: max_length=47 pattern=        - logtraffic: pattern=        - logtraffic_start: pattern=        - log_http_transaction: pattern=        - capture_packet: pattern=        - auto_asic_offload: pattern=        - wanopt: pattern=        - wanopt_detection: pattern=        - wanopt_passive_opt: pattern=        - wanopt_profile: max_length=35 pattern=        - wanopt_peer: max_length=35 pattern=        - webcache: pattern=        - webcache_https: pattern=        - webproxy_forward_server: max_length=63 pattern=        - traffic_shaper: max_length=35 pattern=        - traffic_shaper_reverse: max_length=35 pattern=        - per_ip_shaper: max_length=35 pattern=        - nat: pattern=        - pcp_outbound: pattern=        - pcp_inbound: pattern=        - pcp_poolname: pattern=        - permit_any_host: pattern=        - permit_stun_host: pattern=        - fixedport: pattern=        - port_preserve: pattern=        - port_random: pattern=        - ippool: pattern=        - poolname: pattern=        - poolname6: pattern=        - session_ttl: pattern=        - vlan_cos_fwd: min=0 max=7 pattern=        - vlan_cos_rev: min=0 max=7 pattern=        - inbound: pattern=        - outbound: pattern=        - natinbound: pattern=        - natoutbound: pattern=        - fec: pattern=        - wccp: pattern=        - ntlm: pattern=        - ntlm_guest: pattern=        - ntlm_enabled_browsers: pattern=        - fsso_agent_for_ntlm: max_length=35 pattern=        - groups: pattern=        - users: pattern=        - fsso_groups: pattern=        - auth_path: pattern=        - disclaimer: pattern=        - email_collect: pattern=        - vpntunnel: max_length=35 pattern=        - natip: pattern=        - match_vip: pattern=        - match_vip_only: pattern=        - diffserv_copy: pattern=        - diffserv_forward: pattern=        - diffserv_reverse: pattern=        - diffservcode_forward: pattern=        - diffservcode_rev: pattern=        - tcp_mss_sender: min=0 max=65535 pattern=        - tcp_mss_receiver: min=0 max=65535 pattern=        - comments: max_length=1023 pattern=        - auth_cert: max_length=35 pattern=        - auth_redirect_addr: max_length=63 pattern=        - redirect_url: max_length=1023 pattern=        - identity_based_route: max_length=35 pattern=        - block_notification: pattern=        - custom_log_fields: pattern=        - replacemsg_override_group: max_length=35 pattern=        - srcaddr_negate: pattern=        - srcaddr6_negate: pattern=        - dstaddr_negate: pattern=        - dstaddr6_negate: pattern=        - ztna_ems_tag_negate: pattern=        - service_negate: pattern=        - internet_service_negate: pattern=        - internet_service_src_negate: pattern=        - internet_service6_negate: pattern=        - internet_service6_src_negate: pattern=        - timeout_send_rst: pattern=        - captive_portal_exempt: pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - dsri: pattern=        - radius_mac_auth_bypass: pattern=        - radius_ip_auth_bypass: pattern=        - delay_tcp_npu_session: pattern=        - vlan_filter: pattern=        - sgt_check: pattern=        - sgt: pattern=        - internet_service_fortiguard: pattern=        - internet_service_src_fortiguard: pattern=        - internet_service6_fortiguard: pattern=        - internet_service6_src_fortiguard: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967294, default=0, description="Policy ID (0 - 4294967294).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable or disable this policy.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    srcintf: list[Srcintf] = Field(description="Incoming (ingress) interface.")    
    dstintf: list[Dstintf] = Field(description="Outgoing (egress) interface.")    
    action: Literal["accept", "deny", "ipsec"] | None = Field(default="deny", description="Policy action (accept/deny/ipsec).")    
    nat64: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT64.")    
    nat46: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT46.")    
    ztna_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable zero trust access.")    
    ztna_device_ownership: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable zero trust device ownership.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source IPv4 address and address group names.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination IPv4 address and address group names.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Source IPv6 address name and address group names.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="Destination IPv6 address name and address group names.")    
    ztna_ems_tag: list[ZtnaEmsTag] = Field(default=None, description="Source ztna-ems-tag names.")    
    ztna_ems_tag_secondary: list[ZtnaEmsTagSecondary] = Field(default=None, description="Source ztna-ems-tag-secondary names.")    
    ztna_tags_match_logic: Literal["or", "and"] | None = Field(default="or", description="ZTNA tag matching logic.")    
    ztna_geo_tag: list[ZtnaGeoTag] = Field(default=None, description="Source ztna-geo-tag names.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service name.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    network_service_dynamic: list[NetworkServiceDynamic] = Field(default=None, description="Dynamic Network Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service_src_name: list[InternetServiceSrcName] = Field(default=None, description="Internet Service source name.")    
    internet_service_src_group: list[InternetServiceSrcGroup] = Field(default=None, description="Internet Service source group name.")    
    internet_service_src_custom: list[InternetServiceSrcCustom] = Field(default=None, description="Custom Internet Service source name.")    
    network_service_src_dynamic: list[NetworkServiceSrcDynamic] = Field(default=None, description="Dynamic Network Service source name.")    
    internet_service_src_custom_group: list[InternetServiceSrcCustomGroup] = Field(default=None, description="Custom Internet Service source group name.")    
    reputation_minimum: int | None = Field(ge=0, le=4294967295, default=0, description="Minimum Reputation to take action.")  # datasource: ['firewall.internet-service-reputation.id']    
    reputation_direction: Literal["source", "destination"] | None = Field(default="destination", description="Direction of the initial traffic for reputation to take effect.")    
    src_vendor_mac: list[SrcVendorMac] = Field(default=None, description="Vendor MAC source ID.")    
    internet_service6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service6_name: list[InternetService6Name] = Field(default=None, description="IPv6 Internet Service name.")    
    internet_service6_group: list[InternetService6Group] = Field(default=None, description="Internet Service group name.")    
    internet_service6_custom: list[InternetService6Custom] = Field(default=None, description="Custom IPv6 Internet Service name.")    
    internet_service6_custom_group: list[InternetService6CustomGroup] = Field(default=None, description="Custom Internet Service6 group name.")    
    internet_service6_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service6_src_name: list[InternetService6SrcName] = Field(default=None, description="IPv6 Internet Service source name.")    
    internet_service6_src_group: list[InternetService6SrcGroup] = Field(default=None, description="Internet Service6 source group name.")    
    internet_service6_src_custom: list[InternetService6SrcCustom] = Field(default=None, description="Custom IPv6 Internet Service source name.")    
    internet_service6_src_custom_group: list[InternetService6SrcCustomGroup] = Field(default=None, description="Custom Internet Service6 source group name.")    
    reputation_minimum6: int | None = Field(ge=0, le=4294967295, default=0, description="IPv6 Minimum Reputation to take action.")  # datasource: ['firewall.internet-service-reputation.id']    
    reputation_direction6: Literal["source", "destination"] | None = Field(default="destination", description="Direction of the initial traffic for IPv6 reputation to take effect.")    
    rtp_nat: Literal["disable", "enable"] | None = Field(default="disable", description="Enable Real Time Protocol (RTP) NAT.")    
    rtp_addr: list[RtpAddr] = Field(description="Address names if this is an RTP NAT policy.")    
    send_deny_packet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to send a reply when a session is denied or blocked by a firewall policy.")    
    firewall_session_dirty: Literal["check-all", "check-new"] | None = Field(default="check-all", description="How to handle sessions if the configuration of this firewall policy changes.")    
    schedule: str = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    schedule_timeout: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity.")    
    policy_expiry: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable policy expiry.")    
    policy_expiry_date: Any = Field(default="0000-00-00 00:00:00", description="Policy expiry date (YYYY-MM-DD HH:MM:SS).")    
    policy_expiry_date_utc: str | None = Field(default="", description="Policy expiry date and time, in epoch format.")    
    service: list[Service] = Field(default=None, description="Service and service group names.")    
    tos_mask: str | None = Field(default="", description="Non-zero bit positions are used for comparison while zero bit positions are ignored.")    
    tos: str | None = Field(default="", description="ToS (Type of Service) value used for comparison.")    
    tos_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable negated TOS match.")    
    anti_replay: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable anti-replay check.")    
    tcp_session_without_syn: Literal["all", "data-only", "disable"] | None = Field(default="disable", description="Enable/disable creation of TCP session without SYN flag.")    
    geoip_anycast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable recognition of anycast IP addresses using the geography IP database.")    
    geoip_match: Literal["physical-location", "registered-location"] | None = Field(default="physical-location", description="Match geography address based either on its physical location or registered location.")    
    dynamic_shaping: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dynamic RADIUS defined traffic shaping.")    
    passive_wan_health_measurement: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled.")    
    app_monitor: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable application TCP metrics in session logs.When enabled, auto-asic-offload is disabled.")    
    utm_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.")    
    inspection_mode: Literal["proxy", "flow"] | None = Field(default="flow", description="Policy inspection mode (Flow/proxy). Default is Flow mode.")    
    http_policy_redirect: Literal["enable", "disable", "legacy"] | None = Field(default="disable", description="Redirect HTTP(S) traffic to matching transparent web proxy policy.")    
    ssh_policy_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Redirect SSH traffic to matching transparent proxy policy.")    
    ztna_policy_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Redirect ZTNA traffic to matching Access-Proxy proxy-policy.")    
    webproxy_profile: str | None = Field(max_length=63, default="", description="Webproxy profile name.")  # datasource: ['web-proxy.profile.name']    
    profile_type: Literal["single", "group"] | None = Field(default="single", description="Determine whether the firewall policy allows security profile groups or single profiles only.")    
    profile_group: str | None = Field(max_length=47, default="", description="Name of profile group.")  # datasource: ['firewall.profile-group.name']    
    profile_protocol_options: str | None = Field(max_length=47, default="default", description="Name of an existing Protocol options profile.")  # datasource: ['firewall.profile-protocol-options.name']    
    ssl_ssh_profile: str | None = Field(max_length=47, default="no-inspection", description="Name of an existing SSL SSH profile.")  # datasource: ['firewall.ssl-ssh-profile.name']    
    av_profile: str | None = Field(max_length=47, default="", description="Name of an existing Antivirus profile.")  # datasource: ['antivirus.profile.name']    
    webfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web filter profile.")  # datasource: ['webfilter.profile.name']    
    dnsfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing DNS filter profile.")  # datasource: ['dnsfilter.profile.name']    
    emailfilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing email filter profile.")  # datasource: ['emailfilter.profile.name']    
    dlp_profile: str | None = Field(max_length=47, default="", description="Name of an existing DLP profile.")  # datasource: ['dlp.profile.name']    
    file_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing file-filter profile.")  # datasource: ['file-filter.profile.name']    
    ips_sensor: str | None = Field(max_length=47, default="", description="Name of an existing IPS sensor.")  # datasource: ['ips.sensor.name']    
    application_list: str | None = Field(max_length=47, default="", description="Name of an existing Application list.")  # datasource: ['application.list.name']    
    voip_profile: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (voipd) profile.")  # datasource: ['voip.profile.name']    
    ips_voip_filter: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (ips) profile.")  # datasource: ['voip.profile.name']    
    sctp_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SCTP filter profile.")  # datasource: ['sctp-filter.profile.name']    
    diameter_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing Diameter filter profile.")  # datasource: ['diameter-filter.profile.name']    
    virtual_patch_profile: str | None = Field(max_length=47, default="", description="Name of an existing virtual-patch profile.")  # datasource: ['virtual-patch.profile.name']    
    icap_profile: str | None = Field(max_length=47, default="", description="Name of an existing ICAP profile.")  # datasource: ['icap.profile.name']    
    videofilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing VideoFilter profile.")  # datasource: ['videofilter.profile.name']    
    waf_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web application firewall profile.")  # datasource: ['waf.profile.name']    
    ssh_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SSH filter profile.")  # datasource: ['ssh-filter.profile.name']    
    casb_profile: str | None = Field(max_length=47, default="", description="Name of an existing CASB profile.")  # datasource: ['casb.profile.name']    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable or disable logging. Log all sessions or security profile sessions.")    
    logtraffic_start: Literal["enable", "disable"] | None = Field(default="disable", description="Record logs when a session starts.")    
    log_http_transaction: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP transaction log.")    
    capture_packet: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable capture packets.")    
    auto_asic_offload: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable policy traffic ASIC offloading.")    
    wanopt: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WAN optimization.")    
    wanopt_detection: Literal["active", "passive", "off"] | None = Field(default="active", description="WAN optimization auto-detection mode.")    
    wanopt_passive_opt: Literal["default", "transparent", "non-transparent"] | None = Field(default="default", description="WAN optimization passive mode options. This option decides what IP address will be used to connect server.")    
    wanopt_profile: str = Field(max_length=35, default="", description="WAN optimization profile.")  # datasource: ['wanopt.profile.name']    
    wanopt_peer: str = Field(max_length=35, default="", description="WAN optimization peer.")  # datasource: ['wanopt.peer.peer-host-id']    
    webcache: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web cache.")    
    webcache_https: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable web cache for HTTPS.")    
    webproxy_forward_server: str | None = Field(max_length=63, default="", description="Webproxy forward server name.")  # datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']    
    traffic_shaper: str | None = Field(max_length=35, default="", description="Traffic shaper.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    traffic_shaper_reverse: str | None = Field(max_length=35, default="", description="Reverse traffic shaper.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    per_ip_shaper: str | None = Field(max_length=35, default="", description="Per-IP traffic shaper.")  # datasource: ['firewall.shaper.per-ip-shaper.name']    
    nat: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable source NAT.")    
    pcp_outbound: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PCP outbound SNAT.")    
    pcp_inbound: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PCP inbound DNAT.")    
    pcp_poolname: list[PcpPoolname] = Field(default=None, description="PCP pool names.")    
    permit_any_host: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fullcone NAT. Accept UDP packets from any host.")    
    permit_stun_host: Literal["enable", "disable"] | None = Field(default="disable", description="Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.")    
    fixedport: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to prevent source NAT from changing a session's source port.")    
    port_preserve: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable preservation of the original source port from source NAT if it has not been used.")    
    port_random: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable random source port selection for source NAT.")    
    ippool: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use IP Pools for source NAT.")    
    poolname: list[Poolname] = Field(default=None, description="IP Pool names.")    
    poolname6: list[Poolname6] = Field(default=None, description="IPv6 pool names.")    
    session_ttl: str | None = Field(default="", description="TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).")    
    vlan_cos_fwd: int | None = Field(ge=0, le=7, default=255, description="VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.")    
    vlan_cos_rev: int | None = Field(ge=0, le=7, default=255, description="VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.")    
    inbound: Literal["enable", "disable"] | None = Field(default="disable", description="Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.")    
    outbound: Literal["enable", "disable"] | None = Field(default="enable", description="Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.")    
    natinbound: Literal["enable", "disable"] | None = Field(default="disable", description="Policy-based IPsec VPN: apply destination NAT to inbound traffic.")    
    natoutbound: Literal["enable", "disable"] | None = Field(default="disable", description="Policy-based IPsec VPN: apply source NAT to outbound traffic.")    
    fec: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.")    
    wccp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable forwarding traffic matching this policy to a configured WCCP server.")    
    ntlm: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NTLM authentication.")    
    ntlm_guest: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NTLM guest user access.")    
    ntlm_enabled_browsers: list[NtlmEnabledBrowsers] = Field(default=None, description="HTTP-User-Agent value of supported browsers.")    
    fsso_agent_for_ntlm: str | None = Field(max_length=35, default="", description="FSSO agent to use for NTLM authentication.")  # datasource: ['user.fsso.name']    
    groups: list[Groups] = Field(default=None, description="Names of user groups that can authenticate with this policy.")    
    users: list[Users] = Field(default=None, description="Names of individual users that can authenticate with this policy.")    
    fsso_groups: list[FssoGroups] = Field(default=None, description="Names of FSSO groups.")    
    auth_path: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication-based routing.")    
    disclaimer: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable user authentication disclaimer.")    
    email_collect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable email collection.")    
    vpntunnel: str = Field(max_length=35, default="", description="Policy-based IPsec VPN: name of the IPsec VPN Phase 1.")  # datasource: ['vpn.ipsec.phase1.name', 'vpn.ipsec.manualkey.name']    
    natip: str | None = Field(default="0.0.0.0 0.0.0.0", description="Policy-based IPsec VPN: source NAT IP address for outgoing traffic.")    
    match_vip: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to match packets that have had their destination addresses changed by a VIP.")    
    match_vip_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.")    
    diffserv_copy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to copy packet's DiffServ values from session's original direction to its reply direction.")    
    diffserv_forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's DiffServ values to the specified diffservcode-forward value.")    
    diffserv_reverse: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.")    
    diffservcode_forward: str | None = Field(default="", description="Change packet's DiffServ to this value.")    
    diffservcode_rev: str | None = Field(default="", description="Change packet's reverse (reply) DiffServ to this value.")    
    tcp_mss_sender: int | None = Field(ge=0, le=65535, default=0, description="Sender TCP maximum segment size (MSS).")    
    tcp_mss_receiver: int | None = Field(ge=0, le=65535, default=0, description="Receiver TCP maximum segment size (MSS).")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    auth_cert: str | None = Field(max_length=35, default="", description="HTTPS server certificate for policy authentication.")  # datasource: ['vpn.certificate.local.name']    
    auth_redirect_addr: str | None = Field(max_length=63, default="", description="HTTP-to-HTTPS redirect address for firewall authentication.")    
    redirect_url: str | None = Field(max_length=1023, default=None, description="URL users are directed to after seeing and accepting the disclaimer or authenticating.")    
    identity_based_route: str | None = Field(max_length=35, default="", description="Name of identity-based routing rule.")  # datasource: ['firewall.identity-based-route.name']    
    block_notification: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable block notification.")    
    custom_log_fields: list[CustomLogFields] = Field(default=None, description="Custom fields to append to log messages for this policy.")    
    replacemsg_override_group: str | None = Field(max_length=35, default="", description="Override the default replacement message group for this policy.")  # datasource: ['system.replacemsg-group.name']    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr specifies what the source address must NOT be.")    
    srcaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr6 specifies what the source address must NOT be.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr specifies what the destination address must NOT be.")    
    dstaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr6 specifies what the destination address must NOT be.")    
    ztna_ems_tag_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled ztna-ems-tag specifies what the tags must NOT be.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled service specifies what the service must NOT be.")    
    internet_service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service specifies what the service must NOT be.")    
    internet_service_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service-src specifies what the service must NOT be.")    
    internet_service6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6 specifies what the service must NOT be.")    
    internet_service6_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6-src specifies what the service must NOT be.")    
    timeout_send_rst: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending RST packets when TCP sessions expire.")    
    captive_portal_exempt: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to exempt some users from the captive portal.")    
    decrypted_traffic_mirror: str | None = Field(max_length=35, default="", description="Decrypted traffic mirror.")  # datasource: ['firewall.decrypted-traffic-mirror.name']    
    dsri: Literal["enable", "disable"] | None = Field(default="disable", description="Enable DSRI to ignore HTTP server responses.")    
    radius_mac_auth_bypass: Literal["enable", "disable"] | None = Field(default="disable", description="Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.")    
    radius_ip_auth_bypass: Literal["enable", "disable"] | None = Field(default="disable", description="Enable IP authentication bypass. The bypassed IP address must be received from RADIUS server.")    
    delay_tcp_npu_session: Literal["enable", "disable"] | None = Field(default="disable", description="Enable TCP NPU session delay to guarantee packet order of 3-way handshake.")    
    vlan_filter: str | None = Field(default="", description="VLAN ranges to allow")    
    sgt_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable security group tags (SGT) check.")    
    sgt: list[Sgt] = Field(default=None, description="Security group tags.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service_src_fortiguard: list[InternetServiceSrcFortiguard] = Field(default=None, description="FortiGuard Internet Service source name.")    
    internet_service6_fortiguard: list[InternetService6Fortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service name.")    
    internet_service6_src_fortiguard: list[InternetService6SrcFortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service source name.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('reputation_minimum')
    @classmethod
    def validate_reputation_minimum(cls, v: Any) -> Any:
        """
        Validate reputation_minimum field.
        
        Datasource: ['firewall.internet-service-reputation.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('reputation_minimum6')
    @classmethod
    def validate_reputation_minimum6(cls, v: Any) -> Any:
        """
        Validate reputation_minimum6 field.
        
        Datasource: ['firewall.internet-service-reputation.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('schedule')
    @classmethod
    def validate_schedule(cls, v: Any) -> Any:
        """
        Validate schedule field.
        
        Datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webproxy_profile')
    @classmethod
    def validate_webproxy_profile(cls, v: Any) -> Any:
        """
        Validate webproxy_profile field.
        
        Datasource: ['web-proxy.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('profile_group')
    @classmethod
    def validate_profile_group(cls, v: Any) -> Any:
        """
        Validate profile_group field.
        
        Datasource: ['firewall.profile-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('profile_protocol_options')
    @classmethod
    def validate_profile_protocol_options(cls, v: Any) -> Any:
        """
        Validate profile_protocol_options field.
        
        Datasource: ['firewall.profile-protocol-options.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssl_ssh_profile')
    @classmethod
    def validate_ssl_ssh_profile(cls, v: Any) -> Any:
        """
        Validate ssl_ssh_profile field.
        
        Datasource: ['firewall.ssl-ssh-profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('av_profile')
    @classmethod
    def validate_av_profile(cls, v: Any) -> Any:
        """
        Validate av_profile field.
        
        Datasource: ['antivirus.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webfilter_profile')
    @classmethod
    def validate_webfilter_profile(cls, v: Any) -> Any:
        """
        Validate webfilter_profile field.
        
        Datasource: ['webfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dnsfilter_profile')
    @classmethod
    def validate_dnsfilter_profile(cls, v: Any) -> Any:
        """
        Validate dnsfilter_profile field.
        
        Datasource: ['dnsfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('emailfilter_profile')
    @classmethod
    def validate_emailfilter_profile(cls, v: Any) -> Any:
        """
        Validate emailfilter_profile field.
        
        Datasource: ['emailfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dlp_profile')
    @classmethod
    def validate_dlp_profile(cls, v: Any) -> Any:
        """
        Validate dlp_profile field.
        
        Datasource: ['dlp.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('file_filter_profile')
    @classmethod
    def validate_file_filter_profile(cls, v: Any) -> Any:
        """
        Validate file_filter_profile field.
        
        Datasource: ['file-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_sensor')
    @classmethod
    def validate_ips_sensor(cls, v: Any) -> Any:
        """
        Validate ips_sensor field.
        
        Datasource: ['ips.sensor.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('application_list')
    @classmethod
    def validate_application_list(cls, v: Any) -> Any:
        """
        Validate application_list field.
        
        Datasource: ['application.list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('voip_profile')
    @classmethod
    def validate_voip_profile(cls, v: Any) -> Any:
        """
        Validate voip_profile field.
        
        Datasource: ['voip.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_voip_filter')
    @classmethod
    def validate_ips_voip_filter(cls, v: Any) -> Any:
        """
        Validate ips_voip_filter field.
        
        Datasource: ['voip.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sctp_filter_profile')
    @classmethod
    def validate_sctp_filter_profile(cls, v: Any) -> Any:
        """
        Validate sctp_filter_profile field.
        
        Datasource: ['sctp-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('diameter_filter_profile')
    @classmethod
    def validate_diameter_filter_profile(cls, v: Any) -> Any:
        """
        Validate diameter_filter_profile field.
        
        Datasource: ['diameter-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('virtual_patch_profile')
    @classmethod
    def validate_virtual_patch_profile(cls, v: Any) -> Any:
        """
        Validate virtual_patch_profile field.
        
        Datasource: ['virtual-patch.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('icap_profile')
    @classmethod
    def validate_icap_profile(cls, v: Any) -> Any:
        """
        Validate icap_profile field.
        
        Datasource: ['icap.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('videofilter_profile')
    @classmethod
    def validate_videofilter_profile(cls, v: Any) -> Any:
        """
        Validate videofilter_profile field.
        
        Datasource: ['videofilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('waf_profile')
    @classmethod
    def validate_waf_profile(cls, v: Any) -> Any:
        """
        Validate waf_profile field.
        
        Datasource: ['waf.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssh_filter_profile')
    @classmethod
    def validate_ssh_filter_profile(cls, v: Any) -> Any:
        """
        Validate ssh_filter_profile field.
        
        Datasource: ['ssh-filter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('casb_profile')
    @classmethod
    def validate_casb_profile(cls, v: Any) -> Any:
        """
        Validate casb_profile field.
        
        Datasource: ['casb.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('wanopt_profile')
    @classmethod
    def validate_wanopt_profile(cls, v: Any) -> Any:
        """
        Validate wanopt_profile field.
        
        Datasource: ['wanopt.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('wanopt_peer')
    @classmethod
    def validate_wanopt_peer(cls, v: Any) -> Any:
        """
        Validate wanopt_peer field.
        
        Datasource: ['wanopt.peer.peer-host-id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('webproxy_forward_server')
    @classmethod
    def validate_webproxy_forward_server(cls, v: Any) -> Any:
        """
        Validate webproxy_forward_server field.
        
        Datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('traffic_shaper')
    @classmethod
    def validate_traffic_shaper(cls, v: Any) -> Any:
        """
        Validate traffic_shaper field.
        
        Datasource: ['firewall.shaper.traffic-shaper.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('traffic_shaper_reverse')
    @classmethod
    def validate_traffic_shaper_reverse(cls, v: Any) -> Any:
        """
        Validate traffic_shaper_reverse field.
        
        Datasource: ['firewall.shaper.traffic-shaper.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('per_ip_shaper')
    @classmethod
    def validate_per_ip_shaper(cls, v: Any) -> Any:
        """
        Validate per_ip_shaper field.
        
        Datasource: ['firewall.shaper.per-ip-shaper.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fsso_agent_for_ntlm')
    @classmethod
    def validate_fsso_agent_for_ntlm(cls, v: Any) -> Any:
        """
        Validate fsso_agent_for_ntlm field.
        
        Datasource: ['user.fsso.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('vpntunnel')
    @classmethod
    def validate_vpntunnel(cls, v: Any) -> Any:
        """
        Validate vpntunnel field.
        
        Datasource: ['vpn.ipsec.phase1.name', 'vpn.ipsec.manualkey.name']
        
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
    @field_validator('identity_based_route')
    @classmethod
    def validate_identity_based_route(cls, v: Any) -> Any:
        """
        Validate identity_based_route field.
        
        Datasource: ['firewall.identity-based-route.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('replacemsg_override_group')
    @classmethod
    def validate_replacemsg_override_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_override_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('decrypted_traffic_mirror')
    @classmethod
    def validate_decrypted_traffic_mirror(cls, v: Any) -> Any:
        """
        Validate decrypted_traffic_mirror field.
        
        Datasource: ['firewall.decrypted-traffic-mirror.name']
        
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
    async def validate_srcintf_references(self, client: Any) -> list[str]:
        """
        Validate srcintf references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        - system/zone        - system/sdwan/zone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     srcintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "srcintf", [])
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
            elif await client.api.cmdb.system.zone.exists(value):
                found = True
            elif await client.api.cmdb.system.sdwan.zone.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcintf '{value}' not found in "
                    "system/interface or system/zone or system/sdwan/zone"
                )        
        return errors    
    async def validate_dstintf_references(self, client: Any) -> list[str]:
        """
        Validate dstintf references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        - system/zone        - system/sdwan/zone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     dstintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dstintf", [])
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
            elif await client.api.cmdb.system.zone.exists(value):
                found = True
            elif await client.api.cmdb.system.sdwan.zone.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dstintf '{value}' not found in "
                    "system/interface or system/zone or system/sdwan/zone"
                )        
        return errors    
    async def validate_srcaddr_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     srcaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "srcaddr", [])
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
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp or system/external-resource"
                )        
        return errors    
    async def validate_dstaddr_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - firewall/vip        - firewall/vipgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     dstaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dstaddr", [])
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
            elif await client.api.cmdb.firewall.vip.exists(value):
                found = True
            elif await client.api.cmdb.firewall.vipgrp.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dstaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp or firewall/vip or firewall/vipgrp or system/external-resource"
                )        
        return errors    
    async def validate_srcaddr6_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - system/external-resource        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     srcaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "srcaddr6", [])
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
            if await client.api.cmdb.firewall.address6.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcaddr6 '{value}' not found in "
                    "firewall/address6 or system/external-resource or firewall/addrgrp6"
                )        
        return errors    
    async def validate_dstaddr6_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        - firewall/vip6        - firewall/vipgrp6        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     dstaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dstaddr6", [])
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
            if await client.api.cmdb.firewall.address6.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp6.exists(value):
                found = True
            elif await client.api.cmdb.firewall.vip6.exists(value):
                found = True
            elif await client.api.cmdb.firewall.vipgrp6.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dstaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6 or firewall/vip6 or firewall/vipgrp6 or system/external-resource"
                )        
        return errors    
    async def validate_ztna_ems_tag_references(self, client: Any) -> list[str]:
        """
        Validate ztna_ems_tag references exist in FortiGate.
        
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
            >>> policy = PolicyModel(
            ...     ztna_ems_tag=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ztna_ems_tag_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ztna_ems_tag", [])
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
                    f"Ztna-Ems-Tag '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
                )        
        return errors    
    async def validate_ztna_ems_tag_secondary_references(self, client: Any) -> list[str]:
        """
        Validate ztna_ems_tag_secondary references exist in FortiGate.
        
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
            >>> policy = PolicyModel(
            ...     ztna_ems_tag_secondary=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ztna_ems_tag_secondary_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ztna_ems_tag_secondary", [])
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
                    f"Ztna-Ems-Tag-Secondary '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
                )        
        return errors    
    async def validate_ztna_geo_tag_references(self, client: Any) -> list[str]:
        """
        Validate ztna_geo_tag references exist in FortiGate.
        
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
            >>> policy = PolicyModel(
            ...     ztna_geo_tag=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ztna_geo_tag_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ztna_geo_tag", [])
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
                    f"Ztna-Geo-Tag '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
                )        
        return errors    
    async def validate_internet_service_name_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-name        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_name", [])
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
            if await client.api.cmdb.firewall.internet-service-name.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Name '{value}' not found in "
                    "firewall/internet-service-name"
                )        
        return errors    
    async def validate_internet_service_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_group", [])
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
            if await client.api.cmdb.firewall.internet-service-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Group '{value}' not found in "
                    "firewall/internet-service-group"
                )        
        return errors    
    async def validate_internet_service_custom_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_custom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_custom", [])
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
            if await client.api.cmdb.firewall.internet-service-custom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Custom '{value}' not found in "
                    "firewall/internet-service-custom"
                )        
        return errors    
    async def validate_network_service_dynamic_references(self, client: Any) -> list[str]:
        """
        Validate network_service_dynamic references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/network-service-dynamic        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     network_service_dynamic=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_network_service_dynamic_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "network_service_dynamic", [])
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
            if await client.api.cmdb.firewall.network-service-dynamic.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Network-Service-Dynamic '{value}' not found in "
                    "firewall/network-service-dynamic"
                )        
        return errors    
    async def validate_internet_service_custom_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_custom_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_custom_group", [])
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
            if await client.api.cmdb.firewall.internet-service-custom-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Custom-Group '{value}' not found in "
                    "firewall/internet-service-custom-group"
                )        
        return errors    
    async def validate_internet_service_src_name_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_src_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-name        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_src_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_src_name", [])
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
            if await client.api.cmdb.firewall.internet-service-name.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Src-Name '{value}' not found in "
                    "firewall/internet-service-name"
                )        
        return errors    
    async def validate_internet_service_src_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_src_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_src_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_src_group", [])
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
            if await client.api.cmdb.firewall.internet-service-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Src-Group '{value}' not found in "
                    "firewall/internet-service-group"
                )        
        return errors    
    async def validate_internet_service_src_custom_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_src_custom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_src_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_src_custom", [])
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
            if await client.api.cmdb.firewall.internet-service-custom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Src-Custom '{value}' not found in "
                    "firewall/internet-service-custom"
                )        
        return errors    
    async def validate_network_service_src_dynamic_references(self, client: Any) -> list[str]:
        """
        Validate network_service_src_dynamic references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/network-service-dynamic        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     network_service_src_dynamic=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_network_service_src_dynamic_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "network_service_src_dynamic", [])
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
            if await client.api.cmdb.firewall.network-service-dynamic.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Network-Service-Src-Dynamic '{value}' not found in "
                    "firewall/network-service-dynamic"
                )        
        return errors    
    async def validate_internet_service_src_custom_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_src_custom_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_src_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_src_custom_group", [])
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
            if await client.api.cmdb.firewall.internet-service-custom-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Src-Custom-Group '{value}' not found in "
                    "firewall/internet-service-custom-group"
                )        
        return errors    
    async def validate_reputation_minimum_references(self, client: Any) -> list[str]:
        """
        Validate reputation_minimum references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-reputation        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     reputation_minimum="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_reputation_minimum_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "reputation_minimum", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.internet-service-reputation.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Reputation-Minimum '{value}' not found in "
                "firewall/internet-service-reputation"
            )        
        return errors    
    async def validate_src_vendor_mac_references(self, client: Any) -> list[str]:
        """
        Validate src_vendor_mac references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/vendor-mac        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     src_vendor_mac=[{"id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_src_vendor_mac_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "src_vendor_mac", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("id")
            else:
                value = getattr(item, "id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.vendor-mac.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Src-Vendor-Mac '{value}' not found in "
                    "firewall/vendor-mac"
                )        
        return errors    
    async def validate_internet_service6_name_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-name        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_name", [])
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
            if await client.api.cmdb.firewall.internet-service-name.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Name '{value}' not found in "
                    "firewall/internet-service-name"
                )        
        return errors    
    async def validate_internet_service6_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_group", [])
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
            if await client.api.cmdb.firewall.internet-service-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Group '{value}' not found in "
                    "firewall/internet-service-group"
                )        
        return errors    
    async def validate_internet_service6_custom_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_custom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_custom", [])
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
            if await client.api.cmdb.firewall.internet-service-custom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Custom '{value}' not found in "
                    "firewall/internet-service-custom"
                )        
        return errors    
    async def validate_internet_service6_custom_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_custom_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_custom_group", [])
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
            if await client.api.cmdb.firewall.internet-service-custom-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Custom-Group '{value}' not found in "
                    "firewall/internet-service-custom-group"
                )        
        return errors    
    async def validate_internet_service6_src_name_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_src_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-name        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_src_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_src_name", [])
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
            if await client.api.cmdb.firewall.internet-service-name.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Src-Name '{value}' not found in "
                    "firewall/internet-service-name"
                )        
        return errors    
    async def validate_internet_service6_src_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_src_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_src_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_src_group", [])
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
            if await client.api.cmdb.firewall.internet-service-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Src-Group '{value}' not found in "
                    "firewall/internet-service-group"
                )        
        return errors    
    async def validate_internet_service6_src_custom_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_src_custom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_src_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_src_custom", [])
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
            if await client.api.cmdb.firewall.internet-service-custom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Src-Custom '{value}' not found in "
                    "firewall/internet-service-custom"
                )        
        return errors    
    async def validate_internet_service6_src_custom_group_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_src_custom_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_src_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_src_custom_group", [])
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
            if await client.api.cmdb.firewall.internet-service-custom-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Src-Custom-Group '{value}' not found in "
                    "firewall/internet-service-custom-group"
                )        
        return errors    
    async def validate_reputation_minimum6_references(self, client: Any) -> list[str]:
        """
        Validate reputation_minimum6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-reputation        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     reputation_minimum6="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_reputation_minimum6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "reputation_minimum6", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.internet-service-reputation.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Reputation-Minimum6 '{value}' not found in "
                "firewall/internet-service-reputation"
            )        
        return errors    
    async def validate_rtp_addr_references(self, client: Any) -> list[str]:
        """
        Validate rtp_addr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-custom-group        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     rtp_addr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_rtp_addr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "rtp_addr", [])
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
            if await client.api.cmdb.firewall.internet-service-custom-group.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Rtp-Addr '{value}' not found in "
                    "firewall/internet-service-custom-group or firewall/addrgrp"
                )        
        return errors    
    async def validate_schedule_references(self, client: Any) -> list[str]:
        """
        Validate schedule references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/schedule/onetime        - firewall/schedule/recurring        - firewall/schedule/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     schedule="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_schedule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "schedule", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.schedule.onetime.exists(value):
            found = True
        elif await client.api.cmdb.firewall.schedule.recurring.exists(value):
            found = True
        elif await client.api.cmdb.firewall.schedule.group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Schedule '{value}' not found in "
                "firewall/schedule/onetime or firewall/schedule/recurring or firewall/schedule/group"
            )        
        return errors    
    async def validate_service_references(self, client: Any) -> list[str]:
        """
        Validate service references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/service/custom        - firewall/service/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     service=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "service", [])
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
            if await client.api.cmdb.firewall.service.custom.exists(value):
                found = True
            elif await client.api.cmdb.firewall.service.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Service '{value}' not found in "
                    "firewall/service/custom or firewall/service/group"
                )        
        return errors    
    async def validate_webproxy_profile_references(self, client: Any) -> list[str]:
        """
        Validate webproxy_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - web-proxy/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     webproxy_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webproxy_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "webproxy_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.web-proxy.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Webproxy-Profile '{value}' not found in "
                "web-proxy/profile"
            )        
        return errors    
    async def validate_profile_group_references(self, client: Any) -> list[str]:
        """
        Validate profile_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/profile-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     profile_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "profile_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.profile-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Profile-Group '{value}' not found in "
                "firewall/profile-group"
            )        
        return errors    
    async def validate_profile_protocol_options_references(self, client: Any) -> list[str]:
        """
        Validate profile_protocol_options references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/profile-protocol-options        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     profile_protocol_options="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_protocol_options_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "profile_protocol_options", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.profile-protocol-options.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Profile-Protocol-Options '{value}' not found in "
                "firewall/profile-protocol-options"
            )        
        return errors    
    async def validate_ssl_ssh_profile_references(self, client: Any) -> list[str]:
        """
        Validate ssl_ssh_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssl-ssh-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     ssl_ssh_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_ssh_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssl_ssh_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssl-ssh-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssl-Ssh-Profile '{value}' not found in "
                "firewall/ssl-ssh-profile"
            )        
        return errors    
    async def validate_av_profile_references(self, client: Any) -> list[str]:
        """
        Validate av_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - antivirus/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     av_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_av_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "av_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.antivirus.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Av-Profile '{value}' not found in "
                "antivirus/profile"
            )        
        return errors    
    async def validate_webfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate webfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - webfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     webfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "webfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.webfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Webfilter-Profile '{value}' not found in "
                "webfilter/profile"
            )        
        return errors    
    async def validate_dnsfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate dnsfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dnsfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     dnsfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dnsfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dnsfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dnsfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dnsfilter-Profile '{value}' not found in "
                "dnsfilter/profile"
            )        
        return errors    
    async def validate_emailfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate emailfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - emailfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     emailfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_emailfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "emailfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.emailfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Emailfilter-Profile '{value}' not found in "
                "emailfilter/profile"
            )        
        return errors    
    async def validate_dlp_profile_references(self, client: Any) -> list[str]:
        """
        Validate dlp_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dlp/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     dlp_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dlp_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dlp_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dlp.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dlp-Profile '{value}' not found in "
                "dlp/profile"
            )        
        return errors    
    async def validate_file_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate file_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - file-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     file_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_file_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "file_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.file-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"File-Filter-Profile '{value}' not found in "
                "file-filter/profile"
            )        
        return errors    
    async def validate_ips_sensor_references(self, client: Any) -> list[str]:
        """
        Validate ips_sensor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - ips/sensor        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ips_sensor", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.ips.sensor.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ips-Sensor '{value}' not found in "
                "ips/sensor"
            )        
        return errors    
    async def validate_application_list_references(self, client: Any) -> list[str]:
        """
        Validate application_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - application/list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     application_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_application_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "application_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.application.list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Application-List '{value}' not found in "
                "application/list"
            )        
        return errors    
    async def validate_voip_profile_references(self, client: Any) -> list[str]:
        """
        Validate voip_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - voip/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     voip_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_voip_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "voip_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.voip.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Voip-Profile '{value}' not found in "
                "voip/profile"
            )        
        return errors    
    async def validate_ips_voip_filter_references(self, client: Any) -> list[str]:
        """
        Validate ips_voip_filter references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - voip/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     ips_voip_filter="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_voip_filter_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ips_voip_filter", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.voip.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ips-Voip-Filter '{value}' not found in "
                "voip/profile"
            )        
        return errors    
    async def validate_sctp_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate sctp_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - sctp-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     sctp_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sctp_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "sctp_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.sctp-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Sctp-Filter-Profile '{value}' not found in "
                "sctp-filter/profile"
            )        
        return errors    
    async def validate_diameter_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate diameter_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - diameter-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     diameter_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_diameter_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "diameter_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.diameter-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Diameter-Filter-Profile '{value}' not found in "
                "diameter-filter/profile"
            )        
        return errors    
    async def validate_virtual_patch_profile_references(self, client: Any) -> list[str]:
        """
        Validate virtual_patch_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - virtual-patch/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     virtual_patch_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_virtual_patch_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "virtual_patch_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.virtual-patch.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Virtual-Patch-Profile '{value}' not found in "
                "virtual-patch/profile"
            )        
        return errors    
    async def validate_icap_profile_references(self, client: Any) -> list[str]:
        """
        Validate icap_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - icap/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     icap_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_icap_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "icap_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.icap.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Icap-Profile '{value}' not found in "
                "icap/profile"
            )        
        return errors    
    async def validate_videofilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate videofilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - videofilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     videofilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_videofilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "videofilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.videofilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Videofilter-Profile '{value}' not found in "
                "videofilter/profile"
            )        
        return errors    
    async def validate_waf_profile_references(self, client: Any) -> list[str]:
        """
        Validate waf_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - waf/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     waf_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_waf_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "waf_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.waf.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Waf-Profile '{value}' not found in "
                "waf/profile"
            )        
        return errors    
    async def validate_ssh_filter_profile_references(self, client: Any) -> list[str]:
        """
        Validate ssh_filter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - ssh-filter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     ssh_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssh_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssh_filter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.ssh-filter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssh-Filter-Profile '{value}' not found in "
                "ssh-filter/profile"
            )        
        return errors    
    async def validate_casb_profile_references(self, client: Any) -> list[str]:
        """
        Validate casb_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - casb/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     casb_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_casb_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "casb_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.casb.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Casb-Profile '{value}' not found in "
                "casb/profile"
            )        
        return errors    
    async def validate_wanopt_profile_references(self, client: Any) -> list[str]:
        """
        Validate wanopt_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wanopt/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     wanopt_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wanopt_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "wanopt_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wanopt.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Wanopt-Profile '{value}' not found in "
                "wanopt/profile"
            )        
        return errors    
    async def validate_wanopt_peer_references(self, client: Any) -> list[str]:
        """
        Validate wanopt_peer references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wanopt/peer        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     wanopt_peer="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wanopt_peer_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "wanopt_peer", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wanopt.peer.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Wanopt-Peer '{value}' not found in "
                "wanopt/peer"
            )        
        return errors    
    async def validate_webproxy_forward_server_references(self, client: Any) -> list[str]:
        """
        Validate webproxy_forward_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - web-proxy/forward-server        - web-proxy/forward-server-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     webproxy_forward_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webproxy_forward_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "webproxy_forward_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.web-proxy.forward-server.exists(value):
            found = True
        elif await client.api.cmdb.web-proxy.forward-server-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Webproxy-Forward-Server '{value}' not found in "
                "web-proxy/forward-server or web-proxy/forward-server-group"
            )        
        return errors    
    async def validate_traffic_shaper_references(self, client: Any) -> list[str]:
        """
        Validate traffic_shaper references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/shaper/traffic-shaper        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     traffic_shaper="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_shaper_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "traffic_shaper", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.shaper.traffic-shaper.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Traffic-Shaper '{value}' not found in "
                "firewall/shaper/traffic-shaper"
            )        
        return errors    
    async def validate_traffic_shaper_reverse_references(self, client: Any) -> list[str]:
        """
        Validate traffic_shaper_reverse references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/shaper/traffic-shaper        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     traffic_shaper_reverse="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_shaper_reverse_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "traffic_shaper_reverse", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.shaper.traffic-shaper.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Traffic-Shaper-Reverse '{value}' not found in "
                "firewall/shaper/traffic-shaper"
            )        
        return errors    
    async def validate_per_ip_shaper_references(self, client: Any) -> list[str]:
        """
        Validate per_ip_shaper references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/shaper/per-ip-shaper        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     per_ip_shaper="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_per_ip_shaper_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "per_ip_shaper", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.shaper.per-ip-shaper.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Per-Ip-Shaper '{value}' not found in "
                "firewall/shaper/per-ip-shaper"
            )        
        return errors    
    async def validate_pcp_poolname_references(self, client: Any) -> list[str]:
        """
        Validate pcp_poolname references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/pcp-server/pools        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     pcp_poolname=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_pcp_poolname_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "pcp_poolname", [])
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
            if await client.api.cmdb.system.pcp-server.pools.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Pcp-Poolname '{value}' not found in "
                    "system/pcp-server/pools"
                )        
        return errors    
    async def validate_poolname_references(self, client: Any) -> list[str]:
        """
        Validate poolname references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ippool        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     poolname=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_poolname_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "poolname", [])
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
            if await client.api.cmdb.firewall.ippool.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Poolname '{value}' not found in "
                    "firewall/ippool"
                )        
        return errors    
    async def validate_poolname6_references(self, client: Any) -> list[str]:
        """
        Validate poolname6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ippool6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     poolname6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_poolname6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "poolname6", [])
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
            if await client.api.cmdb.firewall.ippool6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Poolname6 '{value}' not found in "
                    "firewall/ippool6"
                )        
        return errors    
    async def validate_fsso_agent_for_ntlm_references(self, client: Any) -> list[str]:
        """
        Validate fsso_agent_for_ntlm references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/fsso        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     fsso_agent_for_ntlm="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fsso_agent_for_ntlm_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fsso_agent_for_ntlm", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.fsso.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fsso-Agent-For-Ntlm '{value}' not found in "
                "user/fsso"
            )        
        return errors    
    async def validate_groups_references(self, client: Any) -> list[str]:
        """
        Validate groups references exist in FortiGate.
        
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
            >>> policy = PolicyModel(
            ...     groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "groups", [])
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
                    f"Groups '{value}' not found in "
                    "user/group"
                )        
        return errors    
    async def validate_users_references(self, client: Any) -> list[str]:
        """
        Validate users references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/local        - user/certificate        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     users=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_users_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "users", [])
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
            if await client.api.cmdb.user.local.exists(value):
                found = True
            elif await client.api.cmdb.user.certificate.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Users '{value}' not found in "
                    "user/local or user/certificate"
                )        
        return errors    
    async def validate_fsso_groups_references(self, client: Any) -> list[str]:
        """
        Validate fsso_groups references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/adgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     fsso_groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fsso_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "fsso_groups", [])
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
            if await client.api.cmdb.user.adgrp.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Fsso-Groups '{value}' not found in "
                    "user/adgrp"
                )        
        return errors    
    async def validate_vpntunnel_references(self, client: Any) -> list[str]:
        """
        Validate vpntunnel references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/ipsec/phase1        - vpn/ipsec/manualkey        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     vpntunnel="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vpntunnel_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vpntunnel", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.ipsec.phase1.exists(value):
            found = True
        elif await client.api.cmdb.vpn.ipsec.manualkey.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Vpntunnel '{value}' not found in "
                "vpn/ipsec/phase1 or vpn/ipsec/manualkey"
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
            >>> policy = PolicyModel(
            ...     auth_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
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
    async def validate_identity_based_route_references(self, client: Any) -> list[str]:
        """
        Validate identity_based_route references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/identity-based-route        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     identity_based_route="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_identity_based_route_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "identity_based_route", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.identity-based-route.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Identity-Based-Route '{value}' not found in "
                "firewall/identity-based-route"
            )        
        return errors    
    async def validate_custom_log_fields_references(self, client: Any) -> list[str]:
        """
        Validate custom_log_fields references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - log/custom-field        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     custom_log_fields=[{"field-id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_custom_log_fields_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "custom_log_fields", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("field-id")
            else:
                value = getattr(item, "field-id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.log.custom-field.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Custom-Log-Fields '{value}' not found in "
                    "log/custom-field"
                )        
        return errors    
    async def validate_replacemsg_override_group_references(self, client: Any) -> list[str]:
        """
        Validate replacemsg_override_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/replacemsg-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     replacemsg_override_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_replacemsg_override_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "replacemsg_override_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.replacemsg-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Replacemsg-Override-Group '{value}' not found in "
                "system/replacemsg-group"
            )        
        return errors    
    async def validate_decrypted_traffic_mirror_references(self, client: Any) -> list[str]:
        """
        Validate decrypted_traffic_mirror references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/decrypted-traffic-mirror        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     decrypted_traffic_mirror="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_decrypted_traffic_mirror_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "decrypted_traffic_mirror", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.decrypted-traffic-mirror.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Decrypted-Traffic-Mirror '{value}' not found in "
                "firewall/decrypted-traffic-mirror"
            )        
        return errors    
    async def validate_internet_service_fortiguard_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_fortiguard references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-fortiguard        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_fortiguard", [])
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
            if await client.api.cmdb.firewall.internet-service-fortiguard.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Fortiguard '{value}' not found in "
                    "firewall/internet-service-fortiguard"
                )        
        return errors    
    async def validate_internet_service_src_fortiguard_references(self, client: Any) -> list[str]:
        """
        Validate internet_service_src_fortiguard references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-fortiguard        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service_src_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service_src_fortiguard", [])
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
            if await client.api.cmdb.firewall.internet-service-fortiguard.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service-Src-Fortiguard '{value}' not found in "
                    "firewall/internet-service-fortiguard"
                )        
        return errors    
    async def validate_internet_service6_fortiguard_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_fortiguard references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-fortiguard        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_fortiguard", [])
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
            if await client.api.cmdb.firewall.internet-service-fortiguard.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Fortiguard '{value}' not found in "
                    "firewall/internet-service-fortiguard"
                )        
        return errors    
    async def validate_internet_service6_src_fortiguard_references(self, client: Any) -> list[str]:
        """
        Validate internet_service6_src_fortiguard references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service-fortiguard        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     internet_service6_src_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "internet_service6_src_fortiguard", [])
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
            if await client.api.cmdb.firewall.internet-service-fortiguard.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Internet-Service6-Src-Fortiguard '{value}' not found in "
                    "firewall/internet-service-fortiguard"
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
        
        errors = await self.validate_srcintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ztna_ems_tag_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ztna_ems_tag_secondary_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ztna_geo_tag_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_network_service_dynamic_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_network_service_src_dynamic_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_reputation_minimum_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_src_vendor_mac_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_reputation_minimum6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_rtp_addr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_schedule_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_service_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webproxy_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_profile_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_profile_protocol_options_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssl_ssh_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_av_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dnsfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_emailfilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dlp_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_file_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_sensor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_application_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_voip_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_voip_filter_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sctp_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_diameter_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_virtual_patch_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_icap_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_videofilter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_waf_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssh_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_casb_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_wanopt_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_wanopt_peer_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webproxy_forward_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_traffic_shaper_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_traffic_shaper_reverse_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_per_ip_shaper_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_pcp_poolname_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_poolname_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_poolname6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fsso_agent_for_ntlm_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_groups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_users_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fsso_groups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vpntunnel_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_identity_based_route_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_custom_log_fields_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_replacemsg_override_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_decrypted_traffic_mirror_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_fortiguard_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_fortiguard_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_fortiguard_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_fortiguard_references(client)
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
    "PolicyModel",    "PolicySrcintf",    "PolicyDstintf",    "PolicySrcaddr",    "PolicyDstaddr",    "PolicySrcaddr6",    "PolicyDstaddr6",    "PolicyZtnaEmsTag",    "PolicyZtnaEmsTagSecondary",    "PolicyZtnaGeoTag",    "PolicyInternetServiceName",    "PolicyInternetServiceGroup",    "PolicyInternetServiceCustom",    "PolicyNetworkServiceDynamic",    "PolicyInternetServiceCustomGroup",    "PolicyInternetServiceSrcName",    "PolicyInternetServiceSrcGroup",    "PolicyInternetServiceSrcCustom",    "PolicyNetworkServiceSrcDynamic",    "PolicyInternetServiceSrcCustomGroup",    "PolicySrcVendorMac",    "PolicyInternetService6Name",    "PolicyInternetService6Group",    "PolicyInternetService6Custom",    "PolicyInternetService6CustomGroup",    "PolicyInternetService6SrcName",    "PolicyInternetService6SrcGroup",    "PolicyInternetService6SrcCustom",    "PolicyInternetService6SrcCustomGroup",    "PolicyRtpAddr",    "PolicyService",    "PolicyPcpPoolname",    "PolicyPoolname",    "PolicyPoolname6",    "PolicyNtlmEnabledBrowsers",    "PolicyGroups",    "PolicyUsers",    "PolicyFssoGroups",    "PolicyCustomLogFields",    "PolicySgt",    "PolicyInternetServiceFortiguard",    "PolicyInternetServiceSrcFortiguard",    "PolicyInternetService6Fortiguard",    "PolicyInternetService6SrcFortiguard",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:18.192669Z
# ============================================================================
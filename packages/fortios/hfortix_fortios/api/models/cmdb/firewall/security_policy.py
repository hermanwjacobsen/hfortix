"""
Pydantic Models for CMDB - firewall/security_policy

Runtime validation models for firewall/security_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class SecurityPolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Incoming (ingress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class SecurityPolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Outgoing (egress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class SecurityPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source IPv4 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class SecurityPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination IPv4 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.vip.name', 'firewall.vipgrp.name', 'system.external-resource.name']
class SecurityPolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    Source IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class SecurityPolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    Destination IPv6 address name and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'firewall.vip6.name', 'firewall.vipgrp6.name', 'system.external-resource.name']
class SecurityPolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyInternetServiceSrcName(BaseModel):
    """
    Child table model for internet-service-src-name.
    
    Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetServiceSrcGroup(BaseModel):
    """
    Child table model for internet-service-src-group.
    
    Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetServiceSrcCustom(BaseModel):
    """
    Child table model for internet-service-src-custom.
    
    Custom Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetServiceSrcCustomGroup(BaseModel):
    """
    Child table model for internet-service-src-custom-group.
    
    Custom Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetServiceSrcFortiguard(BaseModel):
    """
    Child table model for internet-service-src-fortiguard.
    
    FortiGuard Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyInternetService6Name(BaseModel):
    """
    Child table model for internet-service6-name.
    
    IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetService6Group(BaseModel):
    """
    Child table model for internet-service6-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetService6Custom(BaseModel):
    """
    Child table model for internet-service6-custom.
    
    Custom IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom IPv6 Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetService6CustomGroup(BaseModel):
    """
    Child table model for internet-service6-custom-group.
    
    Custom IPv6 Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom IPv6 Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetService6Fortiguard(BaseModel):
    """
    Child table model for internet-service6-fortiguard.
    
    FortiGuard IPv6 Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyInternetService6SrcName(BaseModel):
    """
    Child table model for internet-service6-src-name.
    
    IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class SecurityPolicyInternetService6SrcGroup(BaseModel):
    """
    Child table model for internet-service6-src-group.
    
    Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class SecurityPolicyInternetService6SrcCustom(BaseModel):
    """
    Child table model for internet-service6-src-custom.
    
    Custom IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class SecurityPolicyInternetService6SrcCustomGroup(BaseModel):
    """
    Child table model for internet-service6-src-custom-group.
    
    Custom Internet Service6 source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class SecurityPolicyInternetService6SrcFortiguard(BaseModel):
    """
    Child table model for internet-service6-src-fortiguard.
    
    FortiGuard IPv6 Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class SecurityPolicyService(BaseModel):
    """
    Child table model for service.
    
    Service and service group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class SecurityPolicyApplication(BaseModel):
    """
    Child table model for application.
    
    Application ID list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Application IDs.")
class SecurityPolicyAppCategory(BaseModel):
    """
    Child table model for app-category.
    
    Application category ID list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Category IDs.")
class SecurityPolicyAppGroup(BaseModel):
    """
    Child table model for app-group.
    
    Application group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Application group names.")  # datasource: ['application.group.name']
class SecurityPolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Names of user groups that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="User group name.")  # datasource: ['user.group.name']
class SecurityPolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Names of individual users that can authenticate with this policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User name.")  # datasource: ['user.local.name']
class SecurityPolicyFssoGroups(BaseModel):
    """
    Child table model for fsso-groups.
    
    Names of FSSO groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=511, default="", description="Names of FSSO groups.")  # datasource: ['user.adgrp.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SecurityPolicyModel(BaseModel):
    """
    Pydantic model for firewall/security_policy configuration.
    
    Configure NGFW IPv4/IPv6 application policies.
    
    Validation Rules:        - uuid: pattern=        - policyid: min=0 max=4294967294 pattern=        - name: max_length=35 pattern=        - comments: max_length=1023 pattern=        - srcintf: pattern=        - dstintf: pattern=        - srcaddr: pattern=        - srcaddr_negate: pattern=        - dstaddr: pattern=        - dstaddr_negate: pattern=        - srcaddr6: pattern=        - srcaddr6_negate: pattern=        - dstaddr6: pattern=        - dstaddr6_negate: pattern=        - internet_service: pattern=        - internet_service_name: pattern=        - internet_service_negate: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - internet_service_custom_group: pattern=        - internet_service_fortiguard: pattern=        - internet_service_src: pattern=        - internet_service_src_name: pattern=        - internet_service_src_negate: pattern=        - internet_service_src_group: pattern=        - internet_service_src_custom: pattern=        - internet_service_src_custom_group: pattern=        - internet_service_src_fortiguard: pattern=        - internet_service6: pattern=        - internet_service6_name: pattern=        - internet_service6_negate: pattern=        - internet_service6_group: pattern=        - internet_service6_custom: pattern=        - internet_service6_custom_group: pattern=        - internet_service6_fortiguard: pattern=        - internet_service6_src: pattern=        - internet_service6_src_name: pattern=        - internet_service6_src_negate: pattern=        - internet_service6_src_group: pattern=        - internet_service6_src_custom: pattern=        - internet_service6_src_custom_group: pattern=        - internet_service6_src_fortiguard: pattern=        - enforce_default_app_port: pattern=        - service: pattern=        - service_negate: pattern=        - action: pattern=        - send_deny_packet: pattern=        - schedule: max_length=35 pattern=        - status: pattern=        - logtraffic: pattern=        - learning_mode: pattern=        - nat46: pattern=        - nat64: pattern=        - profile_type: pattern=        - profile_group: max_length=47 pattern=        - profile_protocol_options: max_length=47 pattern=        - ssl_ssh_profile: max_length=47 pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - dnsfilter_profile: max_length=47 pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile: max_length=47 pattern=        - file_filter_profile: max_length=47 pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - voip_profile: max_length=47 pattern=        - ips_voip_filter: max_length=47 pattern=        - sctp_filter_profile: max_length=47 pattern=        - diameter_filter_profile: max_length=47 pattern=        - virtual_patch_profile: max_length=47 pattern=        - icap_profile: max_length=47 pattern=        - videofilter_profile: max_length=47 pattern=        - ssh_filter_profile: max_length=47 pattern=        - casb_profile: max_length=47 pattern=        - application: pattern=        - app_category: pattern=        - url_category: pattern=        - app_group: pattern=        - groups: pattern=        - users: pattern=        - fsso_groups: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    policyid: int | None = Field(ge=0, le=4294967294, default=0, description="Policy ID.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    srcintf: list[Srcintf] = Field(description="Incoming (ingress) interface.")    
    dstintf: list[Dstintf] = Field(description="Outgoing (egress) interface.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source IPv4 address name and address group names.")    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr specifies what the source address must NOT be.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination IPv4 address name and address group names.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr specifies what the destination address must NOT be.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Source IPv6 address name and address group names.")    
    srcaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr6 specifies what the source address must NOT be.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="Destination IPv6 address name and address group names.")    
    dstaddr6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr6 specifies what the destination address must NOT be.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service name.")    
    internet_service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service specifies what the service must NOT be.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service_src_name: list[InternetServiceSrcName] = Field(default=None, description="Internet Service source name.")    
    internet_service_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service-src specifies what the service must NOT be.")    
    internet_service_src_group: list[InternetServiceSrcGroup] = Field(default=None, description="Internet Service source group name.")    
    internet_service_src_custom: list[InternetServiceSrcCustom] = Field(default=None, description="Custom Internet Service source name.")    
    internet_service_src_custom_group: list[InternetServiceSrcCustomGroup] = Field(default=None, description="Custom Internet Service source group name.")    
    internet_service_src_fortiguard: list[InternetServiceSrcFortiguard] = Field(default=None, description="FortiGuard Internet Service source name.")    
    internet_service6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address, service and default application port enforcement are not used.")    
    internet_service6_name: list[InternetService6Name] = Field(default=None, description="IPv6 Internet Service name.")    
    internet_service6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6 specifies what the service must NOT be.")    
    internet_service6_group: list[InternetService6Group] = Field(default=None, description="Internet Service group name.")    
    internet_service6_custom: list[InternetService6Custom] = Field(default=None, description="Custom IPv6 Internet Service name.")    
    internet_service6_custom_group: list[InternetService6CustomGroup] = Field(default=None, description="Custom IPv6 Internet Service group name.")    
    internet_service6_fortiguard: list[InternetService6Fortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service name.")    
    internet_service6_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service6_src_name: list[InternetService6SrcName] = Field(default=None, description="IPv6 Internet Service source name.")    
    internet_service6_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service6-src specifies what the service must NOT be.")    
    internet_service6_src_group: list[InternetService6SrcGroup] = Field(default=None, description="Internet Service6 source group name.")    
    internet_service6_src_custom: list[InternetService6SrcCustom] = Field(default=None, description="Custom IPv6 Internet Service source name.")    
    internet_service6_src_custom_group: list[InternetService6SrcCustomGroup] = Field(default=None, description="Custom Internet Service6 source group name.")    
    internet_service6_src_fortiguard: list[InternetService6SrcFortiguard] = Field(default=None, description="FortiGuard IPv6 Internet Service source name.")    
    enforce_default_app_port: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable default application port enforcement for allowed applications.")    
    service: list[Service] = Field(default=None, description="Service and service group names.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled service specifies what the service must NOT be.")    
    action: Literal["accept", "deny"] | None = Field(default="deny", description="Policy action (accept/deny).")    
    send_deny_packet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to send a reply when a session is denied or blocked by a firewall policy.")    
    schedule: str = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable or disable this policy.")    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable or disable logging. Log all sessions or security profile sessions.")    
    learning_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated.")    
    nat46: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT46.")    
    nat64: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT64.")    
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
    ssh_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SSH filter profile.")  # datasource: ['ssh-filter.profile.name']    
    casb_profile: str | None = Field(max_length=47, default="", description="Name of an existing CASB profile.")  # datasource: ['casb.profile.name']    
    application: list[Application] = Field(default=None, description="Application ID list.")    
    app_category: list[AppCategory] = Field(default=None, description="Application category ID list.")    
    url_category: list[UrlCategory] = Field(default="", description="URL categories or groups.")    
    app_group: list[AppGroup] = Field(default=None, description="Application group names.")    
    groups: list[Groups] = Field(default=None, description="Names of user groups that can authenticate with this policy.")    
    users: list[Users] = Field(default=None, description="Names of individual users that can authenticate with this policy.")    
    fsso_groups: list[FssoGroups] = Field(default=None, description="Names of FSSO groups.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
            >>> policy = SecurityPolicyModel(
            ...     srcintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     dstintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     srcaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     dstaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
        - firewall/address6        - firewall/addrgrp6        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SecurityPolicyModel(
            ...     srcaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            elif await client.api.cmdb.firewall.addrgrp6.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6 or system/external-resource"
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
            >>> policy = SecurityPolicyModel(
            ...     dstaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_src_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_src_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_src_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_src_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service_src_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_src_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_src_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_src_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_src_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     internet_service6_src_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_src_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     service=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     schedule="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_schedule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     profile_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     profile_protocol_options="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_protocol_options_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     ssl_ssh_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_ssh_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     av_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_av_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     webfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     dnsfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dnsfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     emailfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_emailfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     dlp_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dlp_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     file_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_file_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     application_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_application_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     voip_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_voip_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     ips_voip_filter="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_voip_filter_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     sctp_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sctp_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     diameter_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_diameter_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     virtual_patch_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_virtual_patch_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     icap_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_icap_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     videofilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_videofilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     ssh_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssh_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            >>> policy = SecurityPolicyModel(
            ...     casb_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_casb_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
    async def validate_app_group_references(self, client: Any) -> list[str]:
        """
        Validate app_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - application/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SecurityPolicyModel(
            ...     app_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_app_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "app_group", [])
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
            if await client.api.cmdb.application.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"App-Group '{value}' not found in "
                    "application/group"
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
            >>> policy = SecurityPolicyModel(
            ...     groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
        - user/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SecurityPolicyModel(
            ...     users=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_users_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
            
            if not found:
                errors.append(
                    f"Users '{value}' not found in "
                    "user/local"
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
            >>> policy = SecurityPolicyModel(
            ...     fsso_groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fsso_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.security_policy.post(policy.to_fortios_dict())
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
        errors = await self.validate_internet_service_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_fortiguard_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_src_fortiguard_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_fortiguard_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_custom_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service6_src_fortiguard_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_service_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_schedule_references(client)
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
        errors = await self.validate_ssh_filter_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_casb_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_app_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_groups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_users_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fsso_groups_references(client)
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
    "SecurityPolicyModel",    "SecurityPolicySrcintf",    "SecurityPolicyDstintf",    "SecurityPolicySrcaddr",    "SecurityPolicyDstaddr",    "SecurityPolicySrcaddr6",    "SecurityPolicyDstaddr6",    "SecurityPolicyInternetServiceName",    "SecurityPolicyInternetServiceGroup",    "SecurityPolicyInternetServiceCustom",    "SecurityPolicyInternetServiceCustomGroup",    "SecurityPolicyInternetServiceFortiguard",    "SecurityPolicyInternetServiceSrcName",    "SecurityPolicyInternetServiceSrcGroup",    "SecurityPolicyInternetServiceSrcCustom",    "SecurityPolicyInternetServiceSrcCustomGroup",    "SecurityPolicyInternetServiceSrcFortiguard",    "SecurityPolicyInternetService6Name",    "SecurityPolicyInternetService6Group",    "SecurityPolicyInternetService6Custom",    "SecurityPolicyInternetService6CustomGroup",    "SecurityPolicyInternetService6Fortiguard",    "SecurityPolicyInternetService6SrcName",    "SecurityPolicyInternetService6SrcGroup",    "SecurityPolicyInternetService6SrcCustom",    "SecurityPolicyInternetService6SrcCustomGroup",    "SecurityPolicyInternetService6SrcFortiguard",    "SecurityPolicyService",    "SecurityPolicyApplication",    "SecurityPolicyAppCategory",    "SecurityPolicyAppGroup",    "SecurityPolicyGroups",    "SecurityPolicyUsers",    "SecurityPolicyFssoGroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.110316Z
# ============================================================================
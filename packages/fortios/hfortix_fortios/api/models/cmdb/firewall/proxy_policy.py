"""
Pydantic Models for CMDB - firewall/proxy_policy

Runtime validation models for firewall/proxy_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class ProxyPolicyAccessProxy(BaseModel):
    """
    Child table model for access-proxy.
    
    IPv4 access proxy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Access Proxy name.")  # datasource: ['firewall.access-proxy.name']
class ProxyPolicyAccessProxy6(BaseModel):
    """
    Child table model for access-proxy6.
    
    IPv6 access proxy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Access proxy name.")  # datasource: ['firewall.access-proxy6.name']
class ProxyPolicyZtnaProxy(BaseModel):
    """
    Child table model for ztna-proxy.
    
    ZTNA proxies.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="ZTNA proxy name.")  # datasource: ['ztna.traffic-forward-proxy.name', 'ztna.web-proxy.name', 'ztna.web-portal.name']
class ProxyPolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Source interface names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class ProxyPolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Destination interface names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class ProxyPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'system.external-resource.name']
class ProxyPolicyPoolname(BaseModel):
    """
    Child table model for poolname.
    
    Name of IP pool object.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IP pool name.")  # datasource: ['firewall.ippool.name']
class ProxyPolicyPoolname6(BaseModel):
    """
    Child table model for poolname6.
    
    Name of IPv6 pool object.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 pool name.")  # datasource: ['firewall.ippool6.name']
class ProxyPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'firewall.vip.name', 'firewall.vipgrp.name', 'system.external-resource.name']
class ProxyPolicyZtnaEmsTag(BaseModel):
    """
    Child table model for ztna-ems-tag.
    
    ZTNA EMS Tag names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="EMS Tag name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class ProxyPolicyUrlRisk(BaseModel):
    """
    Child table model for url-risk.
    
    URL risk level name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Risk level name.")  # datasource: ['webfilter.ftgd-risk-level.name']
class ProxyPolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class ProxyPolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class ProxyPolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class ProxyPolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ProxyPolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ProxyPolicyInternetService6Name(BaseModel):
    """
    Child table model for internet-service6-name.
    
    Internet Service IPv6 name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Internet Service IPv6 name.")  # datasource: ['firewall.internet-service-name.name']
class ProxyPolicyInternetService6Group(BaseModel):
    """
    Child table model for internet-service6-group.
    
    Internet Service IPv6 group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service IPv6 group name.")  # datasource: ['firewall.internet-service-group.name']
class ProxyPolicyInternetService6Custom(BaseModel):
    """
    Child table model for internet-service6-custom.
    
    Custom Internet Service IPv6 name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service IPv6 name.")  # datasource: ['firewall.internet-service-custom.name']
class ProxyPolicyInternetService6CustomGroup(BaseModel):
    """
    Child table model for internet-service6-custom-group.
    
    Custom Internet Service IPv6 group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service IPv6 group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ProxyPolicyInternetService6Fortiguard(BaseModel):
    """
    Child table model for internet-service6-fortiguard.
    
    FortiGuard Internet Service IPv6 name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service IPv6 name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ProxyPolicyService(BaseModel):
    """
    Child table model for service.
    
    Name of service objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class ProxyPolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    IPv6 source address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class ProxyPolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    IPv6 destination address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'firewall.vip6.name', 'firewall.vipgrp6.name', 'system.external-resource.name']
class ProxyPolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Names of group objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class ProxyPolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Names of user objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.local.name', 'user.certificate.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProxyPolicyProxyEnum(str, Enum):
    """Allowed values for proxy field."""
    EXPLICIT_WEB = "explicit-web"    TRANSPARENT_WEB = "transparent-web"    FTP = "ftp"    SSH = "ssh"    SSH_TUNNEL = "ssh-tunnel"    ACCESS_PROXY = "access-proxy"    ZTNA_PROXY = "ztna-proxy"    WANOPT = "wanopt"
class ProxyPolicyActionEnum(str, Enum):
    """Allowed values for action field."""
    ACCEPT = "accept"    DENY = "deny"    REDIRECT = "redirect"    ISOLATE = "isolate"
class ProxyPolicyDisclaimerEnum(str, Enum):
    """Allowed values for disclaimer field."""
    DISABLE = "disable"    DOMAIN = "domain"    POLICY = "policy"    USER = "user"

# ============================================================================
# Main Model
# ============================================================================

class ProxyPolicyModel(BaseModel):
    """
    Pydantic model for firewall/proxy_policy configuration.
    
    Configure proxy policies.
    
    Validation Rules:        - uuid: pattern=        - policyid: min=0 max=4294967295 pattern=        - name: max_length=35 pattern=        - proxy: pattern=        - access_proxy: pattern=        - access_proxy6: pattern=        - ztna_proxy: pattern=        - srcintf: pattern=        - dstintf: pattern=        - srcaddr: pattern=        - poolname: pattern=        - poolname6: pattern=        - dstaddr: pattern=        - ztna_ems_tag: pattern=        - ztna_tags_match_logic: pattern=        - device_ownership: pattern=        - url_risk: pattern=        - internet_service: pattern=        - internet_service_negate: pattern=        - internet_service_name: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - internet_service_custom_group: pattern=        - internet_service_fortiguard: pattern=        - internet_service6: pattern=        - internet_service6_negate: pattern=        - internet_service6_name: pattern=        - internet_service6_group: pattern=        - internet_service6_custom: pattern=        - internet_service6_custom_group: pattern=        - internet_service6_fortiguard: pattern=        - service: pattern=        - srcaddr_negate: pattern=        - dstaddr_negate: pattern=        - ztna_ems_tag_negate: pattern=        - service_negate: pattern=        - action: pattern=        - status: pattern=        - schedule: max_length=35 pattern=        - logtraffic: pattern=        - session_ttl: min=300 max=2764800 pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - groups: pattern=        - users: pattern=        - http_tunnel_auth: pattern=        - ssh_policy_redirect: pattern=        - webproxy_forward_server: max_length=63 pattern=        - isolator_server: max_length=63 pattern=        - webproxy_profile: max_length=63 pattern=        - transparent: pattern=        - webcache: pattern=        - webcache_https: pattern=        - disclaimer: pattern=        - utm_status: pattern=        - profile_type: pattern=        - profile_group: max_length=47 pattern=        - profile_protocol_options: max_length=47 pattern=        - ssl_ssh_profile: max_length=47 pattern=        - av_profile: max_length=47 pattern=        - webfilter_profile: max_length=47 pattern=        - dnsfilter_profile: max_length=47 pattern=        - emailfilter_profile: max_length=47 pattern=        - dlp_profile: max_length=47 pattern=        - file_filter_profile: max_length=47 pattern=        - ips_sensor: max_length=47 pattern=        - application_list: max_length=47 pattern=        - ips_voip_filter: max_length=47 pattern=        - sctp_filter_profile: max_length=47 pattern=        - icap_profile: max_length=47 pattern=        - videofilter_profile: max_length=47 pattern=        - waf_profile: max_length=47 pattern=        - ssh_filter_profile: max_length=47 pattern=        - casb_profile: max_length=47 pattern=        - replacemsg_override_group: max_length=35 pattern=        - logtraffic_start: pattern=        - log_http_transaction: pattern=        - comments: max_length=1023 pattern=        - block_notification: pattern=        - redirect_url: max_length=1023 pattern=        - https_sub_category: pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - detect_https_in_http_request: pattern=    """
    
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
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="Policy ID.")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    proxy: ProxyEnum = Field(default="", description="Type of explicit proxy.")    
    access_proxy: list[AccessProxy] = Field(default=None, description="IPv4 access proxy.")    
    access_proxy6: list[AccessProxy6] = Field(default=None, description="IPv6 access proxy.")    
    ztna_proxy: list[ZtnaProxy] = Field(default=None, description="ZTNA proxies.")    
    srcintf: list[Srcintf] = Field(description="Source interface names.")    
    dstintf: list[Dstintf] = Field(description="Destination interface names.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Source address objects.")    
    poolname: list[Poolname] = Field(default=None, description="Name of IP pool object.")    
    poolname6: list[Poolname6] = Field(default=None, description="Name of IPv6 pool object.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Destination address objects.")    
    ztna_ems_tag: list[ZtnaEmsTag] = Field(default=None, description="ZTNA EMS Tag names.")    
    ztna_tags_match_logic: Literal["or", "and"] | None = Field(default="or", description="ZTNA tag matching logic.")    
    device_ownership: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, the ownership enforcement will be done at policy level.")    
    url_risk: list[UrlRisk] = Field(default=None, description="URL risk level name.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service name.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services IPv6 for this policy. If enabled, destination IPv6 address and service are not used.")    
    internet_service6_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, Internet Services match against any internet service IPv6 EXCEPT the selected Internet Service IPv6.")    
    internet_service6_name: list[InternetService6Name] = Field(default=None, description="Internet Service IPv6 name.")    
    internet_service6_group: list[InternetService6Group] = Field(default=None, description="Internet Service IPv6 group name.")    
    internet_service6_custom: list[InternetService6Custom] = Field(default=None, description="Custom Internet Service IPv6 name.")    
    internet_service6_custom_group: list[InternetService6CustomGroup] = Field(default=None, description="Custom Internet Service IPv6 group name.")    
    internet_service6_fortiguard: list[InternetService6Fortiguard] = Field(default=None, description="FortiGuard Internet Service IPv6 name.")    
    service: list[Service] = Field(default=None, description="Name of service objects.")    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, source addresses match against any address EXCEPT the specified source addresses.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, destination addresses match against any address EXCEPT the specified destination addresses.")    
    ztna_ems_tag_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, ZTNA EMS tags match against any tag EXCEPT the specified ZTNA EMS tags.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled, services match against any service EXCEPT the specified destination services.")    
    action: ActionEnum | None = Field(default="deny", description="Accept or deny traffic matching the policy parameters.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of the policy.")    
    schedule: str = Field(max_length=35, default="", description="Name of schedule object.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable/disable logging traffic through the policy.")    
    session_ttl: int | None = Field(ge=300, le=2764800, default=0, description="TTL in seconds for sessions accepted by this policy (0 means use the system default session TTL).")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="IPv6 source address objects.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="IPv6 destination address objects.")    
    groups: list[Groups] = Field(default=None, description="Names of group objects.")    
    users: list[Users] = Field(default=None, description="Names of user objects.")    
    http_tunnel_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP tunnel authentication.")    
    ssh_policy_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Redirect SSH traffic to matching transparent proxy policy.")    
    webproxy_forward_server: str | None = Field(max_length=63, default="", description="Web proxy forward server name.")  # datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']    
    isolator_server: str = Field(max_length=63, default="", description="Isolator server name.")  # datasource: ['web-proxy.isolator-server.name']    
    webproxy_profile: str | None = Field(max_length=63, default="", description="Name of web proxy profile.")  # datasource: ['web-proxy.profile.name']    
    transparent: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use the IP address of the client to connect to the server.")    
    webcache: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web caching.")    
    webcache_https: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).")    
    disclaimer: DisclaimerEnum | None = Field(default="disable", description="Web proxy disclaimer setting: by domain, policy, or user.")    
    utm_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable the use of UTM profiles/sensors/lists.")    
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
    ips_voip_filter: str | None = Field(max_length=47, default="", description="Name of an existing VoIP (ips) profile.")  # datasource: ['voip.profile.name']    
    sctp_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SCTP filter profile.")  # datasource: ['sctp-filter.profile.name']    
    icap_profile: str | None = Field(max_length=47, default="", description="Name of an existing ICAP profile.")  # datasource: ['icap.profile.name']    
    videofilter_profile: str | None = Field(max_length=47, default="", description="Name of an existing VideoFilter profile.")  # datasource: ['videofilter.profile.name']    
    waf_profile: str | None = Field(max_length=47, default="", description="Name of an existing Web application firewall profile.")  # datasource: ['waf.profile.name']    
    ssh_filter_profile: str | None = Field(max_length=47, default="", description="Name of an existing SSH filter profile.")  # datasource: ['ssh-filter.profile.name']    
    casb_profile: str | None = Field(max_length=47, default="", description="Name of an existing CASB profile.")  # datasource: ['casb.profile.name']    
    replacemsg_override_group: str | None = Field(max_length=35, default="", description="Authentication replacement message override group.")  # datasource: ['system.replacemsg-group.name']    
    logtraffic_start: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable policy log traffic start.")    
    log_http_transaction: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP transaction log.")    
    comments: str | None = Field(max_length=1023, default=None, description="Optional comments.")    
    block_notification: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable block notification.")    
    redirect_url: str | None = Field(max_length=1023, default=None, description="Redirect URL for further explicit web proxy processing.")    
    https_sub_category: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTPS sub-category policy matching.")    
    decrypted_traffic_mirror: str | None = Field(max_length=35, default="", description="Decrypted traffic mirror.")  # datasource: ['firewall.decrypted-traffic-mirror.name']    
    detect_https_in_http_request: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable detection of HTTPS in HTTP request.")    
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
    @field_validator('isolator_server')
    @classmethod
    def validate_isolator_server(cls, v: Any) -> Any:
        """
        Validate isolator_server field.
        
        Datasource: ['web-proxy.isolator-server.name']
        
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
    async def validate_access_proxy_references(self, client: Any) -> list[str]:
        """
        Validate access_proxy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/access-proxy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyPolicyModel(
            ...     access_proxy=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_access_proxy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "access_proxy", [])
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
            if await client.api.cmdb.firewall.access-proxy.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Access-Proxy '{value}' not found in "
                    "firewall/access-proxy"
                )        
        return errors    
    async def validate_access_proxy6_references(self, client: Any) -> list[str]:
        """
        Validate access_proxy6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/access-proxy6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyPolicyModel(
            ...     access_proxy6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_access_proxy6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "access_proxy6", [])
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
            if await client.api.cmdb.firewall.access-proxy6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Access-Proxy6 '{value}' not found in "
                    "firewall/access-proxy6"
                )        
        return errors    
    async def validate_ztna_proxy_references(self, client: Any) -> list[str]:
        """
        Validate ztna_proxy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - ztna/traffic-forward-proxy        - ztna/web-proxy        - ztna/web-portal        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyPolicyModel(
            ...     ztna_proxy=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ztna_proxy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ztna_proxy", [])
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
            if await client.api.cmdb.ztna.traffic-forward-proxy.exists(value):
                found = True
            elif await client.api.cmdb.ztna.web-proxy.exists(value):
                found = True
            elif await client.api.cmdb.ztna.web-portal.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ztna-Proxy '{value}' not found in "
                    "ztna/traffic-forward-proxy or ztna/web-proxy or ztna/web-portal"
                )        
        return errors    
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
            >>> policy = ProxyPolicyModel(
            ...     srcintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     dstintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
        - firewall/address        - firewall/addrgrp        - firewall/proxy-address        - firewall/proxy-addrgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyPolicyModel(
            ...     srcaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            elif await client.api.cmdb.firewall.proxy-address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.proxy-addrgrp.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp or firewall/proxy-address or firewall/proxy-addrgrp or system/external-resource"
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
            >>> policy = ProxyPolicyModel(
            ...     poolname=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_poolname_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     poolname6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_poolname6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
    async def validate_dstaddr_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - firewall/proxy-address        - firewall/proxy-addrgrp        - firewall/vip        - firewall/vipgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyPolicyModel(
            ...     dstaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            elif await client.api.cmdb.firewall.proxy-address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.proxy-addrgrp.exists(value):
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
                    "firewall/address or firewall/addrgrp or firewall/proxy-address or firewall/proxy-addrgrp or firewall/vip or firewall/vipgrp or system/external-resource"
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
            >>> policy = ProxyPolicyModel(
            ...     ztna_ems_tag=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ztna_ems_tag_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
    async def validate_url_risk_references(self, client: Any) -> list[str]:
        """
        Validate url_risk references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - webfilter/ftgd-risk-level        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyPolicyModel(
            ...     url_risk=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_url_risk_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "url_risk", [])
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
            if await client.api.cmdb.webfilter.ftgd-risk-level.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Url-Risk '{value}' not found in "
                    "webfilter/ftgd-risk-level"
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service6_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service6_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service6_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service6_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     internet_service6_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service6_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     service=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     schedule="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_schedule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     srcaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     dstaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     users=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_users_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     webproxy_forward_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webproxy_forward_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
    async def validate_isolator_server_references(self, client: Any) -> list[str]:
        """
        Validate isolator_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - web-proxy/isolator-server        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyPolicyModel(
            ...     isolator_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_isolator_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "isolator_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.web-proxy.isolator-server.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Isolator-Server '{value}' not found in "
                "web-proxy/isolator-server"
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
            >>> policy = ProxyPolicyModel(
            ...     webproxy_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webproxy_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     profile_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     profile_protocol_options="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_protocol_options_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     ssl_ssh_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_ssh_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     av_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_av_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     webfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_webfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     dnsfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dnsfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     emailfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_emailfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     dlp_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dlp_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     file_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_file_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     application_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_application_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     ips_voip_filter="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_voip_filter_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     sctp_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sctp_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     icap_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_icap_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     videofilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_videofilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     waf_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_waf_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     ssh_filter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssh_filter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     casb_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_casb_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     replacemsg_override_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_replacemsg_override_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
            >>> policy = ProxyPolicyModel(
            ...     decrypted_traffic_mirror="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_decrypted_traffic_mirror_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_policy.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_access_proxy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_access_proxy6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ztna_proxy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_poolname_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_poolname6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ztna_ems_tag_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_url_risk_references(client)
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
        errors = await self.validate_service_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_schedule_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_groups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_users_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_webproxy_forward_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_isolator_server_references(client)
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
        errors = await self.validate_ips_voip_filter_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sctp_filter_profile_references(client)
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
        errors = await self.validate_replacemsg_override_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_decrypted_traffic_mirror_references(client)
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
    "ProxyPolicyModel",    "ProxyPolicyAccessProxy",    "ProxyPolicyAccessProxy6",    "ProxyPolicyZtnaProxy",    "ProxyPolicySrcintf",    "ProxyPolicyDstintf",    "ProxyPolicySrcaddr",    "ProxyPolicyPoolname",    "ProxyPolicyPoolname6",    "ProxyPolicyDstaddr",    "ProxyPolicyZtnaEmsTag",    "ProxyPolicyUrlRisk",    "ProxyPolicyInternetServiceName",    "ProxyPolicyInternetServiceGroup",    "ProxyPolicyInternetServiceCustom",    "ProxyPolicyInternetServiceCustomGroup",    "ProxyPolicyInternetServiceFortiguard",    "ProxyPolicyInternetService6Name",    "ProxyPolicyInternetService6Group",    "ProxyPolicyInternetService6Custom",    "ProxyPolicyInternetService6CustomGroup",    "ProxyPolicyInternetService6Fortiguard",    "ProxyPolicyService",    "ProxyPolicySrcaddr6",    "ProxyPolicyDstaddr6",    "ProxyPolicyGroups",    "ProxyPolicyUsers",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.991243Z
# ============================================================================
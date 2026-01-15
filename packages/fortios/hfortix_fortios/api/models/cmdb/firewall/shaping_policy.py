"""
Pydantic Models for CMDB - firewall/shaping_policy

Runtime validation models for firewall/shaping_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class ShapingPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    IPv4 source address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class ShapingPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    IPv4 destination address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class ShapingPolicySrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    IPv6 source address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class ShapingPolicyDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    IPv6 destination address and address group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class ShapingPolicyInternetServiceName(BaseModel):
    """
    Child table model for internet-service-name.
    
    Internet Service ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class ShapingPolicyInternetServiceGroup(BaseModel):
    """
    Child table model for internet-service-group.
    
    Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class ShapingPolicyInternetServiceCustom(BaseModel):
    """
    Child table model for internet-service-custom.
    
    Custom Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class ShapingPolicyInternetServiceCustomGroup(BaseModel):
    """
    Child table model for internet-service-custom-group.
    
    Custom Internet Service group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ShapingPolicyInternetServiceFortiguard(BaseModel):
    """
    Child table model for internet-service-fortiguard.
    
    FortiGuard Internet Service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ShapingPolicyInternetServiceSrcName(BaseModel):
    """
    Child table model for internet-service-src-name.
    
    Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class ShapingPolicyInternetServiceSrcGroup(BaseModel):
    """
    Child table model for internet-service-src-group.
    
    Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class ShapingPolicyInternetServiceSrcCustom(BaseModel):
    """
    Child table model for internet-service-src-custom.
    
    Custom Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class ShapingPolicyInternetServiceSrcCustomGroup(BaseModel):
    """
    Child table model for internet-service-src-custom-group.
    
    Custom Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class ShapingPolicyInternetServiceSrcFortiguard(BaseModel):
    """
    Child table model for internet-service-src-fortiguard.
    
    FortiGuard Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class ShapingPolicyService(BaseModel):
    """
    Child table model for service.
    
    Service and service group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
class ShapingPolicyUsers(BaseModel):
    """
    Child table model for users.
    
    Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User name.")  # datasource: ['user.local.name']
class ShapingPolicyGroups(BaseModel):
    """
    Child table model for groups.
    
    Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class ShapingPolicyApplication(BaseModel):
    """
    Child table model for application.
    
    IDs of one or more applications that this shaper applies application control traffic shaping to.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Application IDs.")
class ShapingPolicyAppCategory(BaseModel):
    """
    Child table model for app-category.
    
    IDs of one or more application categories that this shaper applies application control traffic shaping to.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Category IDs.")
class ShapingPolicyAppGroup(BaseModel):
    """
    Child table model for app-group.
    
    One or more application group names.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Application group name.")  # datasource: ['application.group.name']
class ShapingPolicyUrlCategory(BaseModel):
    """
    Child table model for url-category.
    
    IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="URL category ID.")
class ShapingPolicySrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    One or more incoming (ingress) interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class ShapingPolicyDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    One or more outgoing (egress) interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ShapingPolicyModel(BaseModel):
    """
    Pydantic model for firewall/shaping_policy configuration.
    
    Configure shaping policies.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - uuid: pattern=        - name: max_length=35 pattern=        - comment: max_length=255 pattern=        - status: pattern=        - ip_version: pattern=        - traffic_type: pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - internet_service: pattern=        - internet_service_name: pattern=        - internet_service_group: pattern=        - internet_service_custom: pattern=        - internet_service_custom_group: pattern=        - internet_service_fortiguard: pattern=        - internet_service_src: pattern=        - internet_service_src_name: pattern=        - internet_service_src_group: pattern=        - internet_service_src_custom: pattern=        - internet_service_src_custom_group: pattern=        - internet_service_src_fortiguard: pattern=        - service: pattern=        - schedule: max_length=35 pattern=        - users: pattern=        - groups: pattern=        - application: pattern=        - app_category: pattern=        - app_group: pattern=        - url_category: pattern=        - srcintf: pattern=        - dstintf: pattern=        - tos_mask: pattern=        - tos: pattern=        - tos_negate: pattern=        - traffic_shaper: max_length=35 pattern=        - traffic_shaper_reverse: max_length=35 pattern=        - per_ip_shaper: max_length=35 pattern=        - class_id: min=0 max=4294967295 pattern=        - diffserv_forward: pattern=        - diffserv_reverse: pattern=        - diffservcode_forward: pattern=        - diffservcode_rev: pattern=        - cos_mask: pattern=        - cos: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Shaping policy ID (0 - 4294967295).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    name: str | None = Field(max_length=35, default="", description="Shaping policy name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comments.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this traffic shaping policy.")    
    ip_version: Literal["4", "6"] | None = Field(default="4", description="Apply this traffic shaping policy to IPv4 or IPv6 traffic.")    
    traffic_type: Literal["forwarding", "local-in", "local-out"] | None = Field(default="forwarding", description="Traffic type.")    
    srcaddr: list[Srcaddr] = Field(description="IPv4 source address and address group names.")    
    dstaddr: list[Dstaddr] = Field(description="IPv4 destination address and address group names.")    
    srcaddr6: list[Srcaddr6] = Field(description="IPv6 source address and address group names.")    
    dstaddr6: list[Dstaddr6] = Field(description="IPv6 destination address and address group names.")    
    internet_service: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.")    
    internet_service_name: list[InternetServiceName] = Field(default=None, description="Internet Service ID.")    
    internet_service_group: list[InternetServiceGroup] = Field(default=None, description="Internet Service group name.")    
    internet_service_custom: list[InternetServiceCustom] = Field(default=None, description="Custom Internet Service name.")    
    internet_service_custom_group: list[InternetServiceCustomGroup] = Field(default=None, description="Custom Internet Service group name.")    
    internet_service_fortiguard: list[InternetServiceFortiguard] = Field(default=None, description="FortiGuard Internet Service name.")    
    internet_service_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.")    
    internet_service_src_name: list[InternetServiceSrcName] = Field(default=None, description="Internet Service source name.")    
    internet_service_src_group: list[InternetServiceSrcGroup] = Field(default=None, description="Internet Service source group name.")    
    internet_service_src_custom: list[InternetServiceSrcCustom] = Field(default=None, description="Custom Internet Service source name.")    
    internet_service_src_custom_group: list[InternetServiceSrcCustomGroup] = Field(default=None, description="Custom Internet Service source group name.")    
    internet_service_src_fortiguard: list[InternetServiceSrcFortiguard] = Field(default=None, description="FortiGuard Internet Service source name.")    
    service: list[Service] = Field(description="Service and service group names.")    
    schedule: str | None = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    users: list[Users] = Field(default=None, description="Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.")    
    groups: list[Groups] = Field(default=None, description="Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.")    
    application: list[Application] = Field(default=None, description="IDs of one or more applications that this shaper applies application control traffic shaping to.")    
    app_category: list[AppCategory] = Field(default=None, description="IDs of one or more application categories that this shaper applies application control traffic shaping to.")    
    app_group: list[AppGroup] = Field(default=None, description="One or more application group names.")    
    url_category: list[UrlCategory] = Field(default=None, description="IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.")    
    srcintf: list[Srcintf] = Field(default=None, description="One or more incoming (ingress) interfaces.")    
    dstintf: list[Dstintf] = Field(description="One or more outgoing (egress) interfaces.")    
    tos_mask: str | None = Field(default="", description="Non-zero bit positions are used for comparison while zero bit positions are ignored.")    
    tos: str | None = Field(default="", description="ToS (Type of Service) value used for comparison.")    
    tos_negate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable negated TOS match.")    
    traffic_shaper: str | None = Field(max_length=35, default="", description="Traffic shaper to apply to traffic forwarded by the firewall policy.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    traffic_shaper_reverse: str | None = Field(max_length=35, default="", description="Traffic shaper to apply to response traffic received by the firewall policy.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    per_ip_shaper: str | None = Field(max_length=35, default="", description="Per-IP traffic shaper to apply with this policy.")  # datasource: ['firewall.shaper.per-ip-shaper.name']    
    class_id: int | None = Field(ge=0, le=4294967295, default=0, description="Traffic class ID.")  # datasource: ['firewall.traffic-class.class-id']    
    diffserv_forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's DiffServ values to the specified diffservcode-forward value.")    
    diffserv_reverse: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to change packet's reverse (reply) DiffServ values to the specified diffservcode-rev value.")    
    diffservcode_forward: str | None = Field(default="", description="Change packet's DiffServ to this value.")    
    diffservcode_rev: str | None = Field(default="", description="Change packet's reverse (reply) DiffServ to this value.")    
    cos_mask: str | None = Field(default="", description="VLAN CoS evaluated bits.")    
    cos: str | None = Field(default="", description="VLAN CoS bit pattern.")    
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
    @field_validator('class_id')
    @classmethod
    def validate_class_id(cls, v: Any) -> Any:
        """
        Validate class_id field.
        
        Datasource: ['firewall.traffic-class.class-id']
        
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
    async def validate_srcaddr_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr references exist in FortiGate.
        
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
            >>> policy = ShapingPolicyModel(
            ...     srcaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            
            if not found:
                errors.append(
                    f"Srcaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
                )        
        return errors    
    async def validate_dstaddr_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr references exist in FortiGate.
        
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
            >>> policy = ShapingPolicyModel(
            ...     dstaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            
            if not found:
                errors.append(
                    f"Dstaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
                )        
        return errors    
    async def validate_srcaddr6_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr6 references exist in FortiGate.
        
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
            >>> policy = ShapingPolicyModel(
            ...     srcaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            
            if not found:
                errors.append(
                    f"Srcaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6"
                )        
        return errors    
    async def validate_dstaddr6_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr6 references exist in FortiGate.
        
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
            >>> policy = ShapingPolicyModel(
            ...     dstaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            
            if not found:
                errors.append(
                    f"Dstaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6"
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_src_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_src_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_src_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_src_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     internet_service_src_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     service=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     schedule="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_schedule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     users=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_users_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     app_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_app_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     srcintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     dstintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     traffic_shaper="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_shaper_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     traffic_shaper_reverse="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_shaper_reverse_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
            >>> policy = ShapingPolicyModel(
            ...     per_ip_shaper="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_per_ip_shaper_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
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
    async def validate_class_id_references(self, client: Any) -> list[str]:
        """
        Validate class_id references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/traffic-class        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ShapingPolicyModel(
            ...     class_id="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_class_id_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "class_id", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.traffic-class.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Class-Id '{value}' not found in "
                "firewall/traffic-class"
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
        errors = await self.validate_service_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_schedule_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_users_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_groups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_app_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_traffic_shaper_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_traffic_shaper_reverse_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_per_ip_shaper_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_class_id_references(client)
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
    "ShapingPolicyModel",    "ShapingPolicySrcaddr",    "ShapingPolicyDstaddr",    "ShapingPolicySrcaddr6",    "ShapingPolicyDstaddr6",    "ShapingPolicyInternetServiceName",    "ShapingPolicyInternetServiceGroup",    "ShapingPolicyInternetServiceCustom",    "ShapingPolicyInternetServiceCustomGroup",    "ShapingPolicyInternetServiceFortiguard",    "ShapingPolicyInternetServiceSrcName",    "ShapingPolicyInternetServiceSrcGroup",    "ShapingPolicyInternetServiceSrcCustom",    "ShapingPolicyInternetServiceSrcCustomGroup",    "ShapingPolicyInternetServiceSrcFortiguard",    "ShapingPolicyService",    "ShapingPolicyUsers",    "ShapingPolicyGroups",    "ShapingPolicyApplication",    "ShapingPolicyAppCategory",    "ShapingPolicyAppGroup",    "ShapingPolicyUrlCategory",    "ShapingPolicySrcintf",    "ShapingPolicyDstintf",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.739601Z
# ============================================================================
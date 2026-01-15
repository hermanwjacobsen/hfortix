"""
Pydantic Models for CMDB - firewall/local_in_policy

Runtime validation models for firewall/local_in_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class LocalInPolicyIntf(BaseModel):
    """
    Child table model for intf.
    
    Incoming interface name from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['system.zone.name', 'system.sdwan.zone.name', 'system.interface.name']
class LocalInPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address object from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class LocalInPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination address object from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class LocalInPolicyInternetServiceSrcName(BaseModel):
    """
    Child table model for internet-service-src-name.
    
    Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service name.")  # datasource: ['firewall.internet-service-name.name']
class LocalInPolicyInternetServiceSrcGroup(BaseModel):
    """
    Child table model for internet-service-src-group.
    
    Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Internet Service group name.")  # datasource: ['firewall.internet-service-group.name']
class LocalInPolicyInternetServiceSrcCustom(BaseModel):
    """
    Child table model for internet-service-src-custom.
    
    Custom Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service name.")  # datasource: ['firewall.internet-service-custom.name']
class LocalInPolicyInternetServiceSrcCustomGroup(BaseModel):
    """
    Child table model for internet-service-src-custom-group.
    
    Custom Internet Service source group name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Custom Internet Service group name.")  # datasource: ['firewall.internet-service-custom-group.name']
class LocalInPolicyInternetServiceSrcFortiguard(BaseModel):
    """
    Child table model for internet-service-src-fortiguard.
    
    FortiGuard Internet Service source name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="FortiGuard Internet Service name.")  # datasource: ['firewall.internet-service-fortiguard.name']
class LocalInPolicyService(BaseModel):
    """
    Child table model for service.
    
    Service object from available options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Service name.")  # datasource: ['firewall.service.custom.name', 'firewall.service.group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class LocalInPolicyModel(BaseModel):
    """
    Pydantic model for firewall/local_in_policy configuration.
    
    Configure user defined IPv4 local-in policies.
    
    Validation Rules:        - policyid: min=0 max=4294967295 pattern=        - uuid: pattern=        - ha_mgmt_intf_only: pattern=        - intf: pattern=        - srcaddr: pattern=        - srcaddr_negate: pattern=        - dstaddr: pattern=        - internet_service_src: pattern=        - internet_service_src_name: pattern=        - internet_service_src_group: pattern=        - internet_service_src_custom: pattern=        - internet_service_src_custom_group: pattern=        - internet_service_src_fortiguard: pattern=        - dstaddr_negate: pattern=        - action: pattern=        - service: pattern=        - service_negate: pattern=        - internet_service_src_negate: pattern=        - schedule: max_length=35 pattern=        - status: pattern=        - virtual_patch: pattern=        - logtraffic: pattern=        - comments: max_length=1023 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="User defined local in policy ID.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    ha_mgmt_intf_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dedicating the HA management interface only for local-in policy.")    
    intf: list[Intf] = Field(description="Incoming interface name from available options.")    
    srcaddr: list[Srcaddr] = Field(description="Source address object from available options.")    
    srcaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled srcaddr specifies what the source address must NOT be.")    
    dstaddr: list[Dstaddr] = Field(description="Destination address object from available options.")    
    internet_service_src: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of Internet Services in source for this local-in policy. If enabled, source address is not used.")    
    internet_service_src_name: list[InternetServiceSrcName] = Field(default=None, description="Internet Service source name.")    
    internet_service_src_group: list[InternetServiceSrcGroup] = Field(default=None, description="Internet Service source group name.")    
    internet_service_src_custom: list[InternetServiceSrcCustom] = Field(default=None, description="Custom Internet Service source name.")    
    internet_service_src_custom_group: list[InternetServiceSrcCustomGroup] = Field(default=None, description="Custom Internet Service source group name.")    
    internet_service_src_fortiguard: list[InternetServiceSrcFortiguard] = Field(default=None, description="FortiGuard Internet Service source name.")    
    dstaddr_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled dstaddr specifies what the destination address must NOT be.")    
    action: Literal["accept", "deny"] | None = Field(default="deny", description="Action performed on traffic matching the policy (default = deny).")    
    service: list[Service] = Field(description="Service object from available options.")    
    service_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled service specifies what the service must NOT be.")    
    internet_service_src_negate: Literal["enable", "disable"] | None = Field(default="disable", description="When enabled internet-service-src specifies what the service must NOT be.")    
    schedule: str = Field(max_length=35, default="", description="Schedule object from available options.")  # datasource: ['firewall.schedule.onetime.name', 'firewall.schedule.recurring.name', 'firewall.schedule.group.name']    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this local-in policy.")    
    virtual_patch: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable virtual patching.")    
    logtraffic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in traffic logging.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
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
    async def validate_intf_references(self, client: Any) -> list[str]:
        """
        Validate intf references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/zone        - system/sdwan/zone        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalInPolicyModel(
            ...     intf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_intf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "intf", [])
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
            if await client.api.cmdb.system.zone.exists(value):
                found = True
            elif await client.api.cmdb.system.sdwan.zone.exists(value):
                found = True
            elif await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Intf '{value}' not found in "
                    "system/zone or system/sdwan/zone or system/interface"
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
            >>> policy = LocalInPolicyModel(
            ...     srcaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
        - firewall/address        - firewall/addrgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalInPolicyModel(
            ...     dstaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dstaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp or system/external-resource"
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
            >>> policy = LocalInPolicyModel(
            ...     internet_service_src_name=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
            >>> policy = LocalInPolicyModel(
            ...     internet_service_src_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
            >>> policy = LocalInPolicyModel(
            ...     internet_service_src_custom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
            >>> policy = LocalInPolicyModel(
            ...     internet_service_src_custom_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_custom_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
            >>> policy = LocalInPolicyModel(
            ...     internet_service_src_fortiguard=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_src_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
            >>> policy = LocalInPolicyModel(
            ...     service=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
            >>> policy = LocalInPolicyModel(
            ...     schedule="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_schedule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.local_in_policy.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_intf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr_references(client)
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
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "LocalInPolicyModel",    "LocalInPolicyIntf",    "LocalInPolicySrcaddr",    "LocalInPolicyDstaddr",    "LocalInPolicyInternetServiceSrcName",    "LocalInPolicyInternetServiceSrcGroup",    "LocalInPolicyInternetServiceSrcCustom",    "LocalInPolicyInternetServiceSrcCustomGroup",    "LocalInPolicyInternetServiceSrcFortiguard",    "LocalInPolicyService",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.980442Z
# ============================================================================
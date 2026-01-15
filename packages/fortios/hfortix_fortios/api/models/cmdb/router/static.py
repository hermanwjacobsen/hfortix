"""
Pydantic Models for CMDB - router/static

Runtime validation models for router/static configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class StaticSdwanZone(BaseModel):
    """
    Child table model for sdwan-zone.
    
    Choose SD-WAN Zone.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="SD-WAN zone name.")  # datasource: ['system.sdwan.zone.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class StaticModel(BaseModel):
    """
    Pydantic model for router/static configuration.
    
    Configure IPv4 static routing tables.
    
    Validation Rules:        - seq_num: min=0 max=4294967295 pattern=        - status: pattern=        - dst: pattern=        - src: pattern=        - gateway: pattern=        - preferred_source: pattern=        - distance: min=1 max=255 pattern=        - weight: min=0 max=255 pattern=        - priority: min=1 max=65535 pattern=        - device: max_length=35 pattern=        - comment: max_length=255 pattern=        - blackhole: pattern=        - dynamic_gateway: pattern=        - sdwan_zone: pattern=        - dstaddr: max_length=79 pattern=        - internet_service: min=0 max=4294967295 pattern=        - internet_service_custom: max_length=64 pattern=        - internet_service_fortiguard: max_length=64 pattern=        - link_monitor_exempt: pattern=        - tag: min=0 max=4294967295 pattern=        - vrf: min=0 max=511 pattern=        - bfd: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    seq_num: int | None = Field(ge=0, le=4294967295, default=0, description="Sequence number.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this static route.")    
    dst: str = Field(default="0.0.0.0 0.0.0.0", description="Destination IP and mask for this route.")    
    src: str | None = Field(default="0.0.0.0 0.0.0.0", description="Source prefix for this route.")    
    gateway: str | None = Field(default="0.0.0.0", description="Gateway IP for this route.")    
    preferred_source: str | None = Field(default="0.0.0.0", description="Preferred source IP for this route.")    
    distance: int | None = Field(ge=1, le=255, default=10, description="Administrative distance (1 - 255).")    
    weight: int | None = Field(ge=0, le=255, default=0, description="Administrative weight (0 - 255).")    
    priority: int | None = Field(ge=1, le=65535, default=1, description="Administrative priority (1 - 65535).")    
    device: str = Field(max_length=35, default="", description="Gateway out interface or tunnel.")  # datasource: ['system.interface.name']    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    blackhole: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable black hole.")    
    dynamic_gateway: Literal["enable", "disable"] | None = Field(default="disable", description="Enable use of dynamic gateway retrieved from a DHCP or PPP server.")    
    sdwan_zone: list[SdwanZone] = Field(default=None, description="Choose SD-WAN Zone.")    
    dstaddr: str | None = Field(max_length=79, default="", description="Name of firewall address or address group.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    internet_service: int | None = Field(ge=0, le=4294967295, default=0, description="Application ID in the Internet service database.")  # datasource: ['firewall.internet-service.id']    
    internet_service_custom: str | None = Field(max_length=64, default="", description="Application name in the Internet service custom database.")  # datasource: ['firewall.internet-service-custom.name']    
    internet_service_fortiguard: str | None = Field(max_length=64, default="", description="Application name in the Internet service fortiguard database.")  # datasource: ['firewall.internet-service-fortiguard.name']    
    link_monitor_exempt: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable withdrawal of this static route when link monitor or health check is down.")    
    tag: int | None = Field(ge=0, le=4294967295, default=0, description="Route tag.")    
    vrf: int | None = Field(ge=0, le=511, default="unspecified", description="Virtual Routing Forwarding ID.")    
    bfd: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Bidirectional Forwarding Detection (BFD).")    
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
    @field_validator('dstaddr')
    @classmethod
    def validate_dstaddr(cls, v: Any) -> Any:
        """
        Validate dstaddr field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internet_service')
    @classmethod
    def validate_internet_service(cls, v: Any) -> Any:
        """
        Validate internet_service field.
        
        Datasource: ['firewall.internet-service.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internet_service_custom')
    @classmethod
    def validate_internet_service_custom(cls, v: Any) -> Any:
        """
        Validate internet_service_custom field.
        
        Datasource: ['firewall.internet-service-custom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internet_service_fortiguard')
    @classmethod
    def validate_internet_service_fortiguard(cls, v: Any) -> Any:
        """
        Validate internet_service_fortiguard field.
        
        Datasource: ['firewall.internet-service-fortiguard.name']
        
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
            >>> policy = StaticModel(
            ...     device="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_device_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static.post(policy.to_fortios_dict())
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
    async def validate_sdwan_zone_references(self, client: Any) -> list[str]:
        """
        Validate sdwan_zone references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdwan/zone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = StaticModel(
            ...     sdwan_zone=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sdwan_zone_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "sdwan_zone", [])
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
            if await client.api.cmdb.system.sdwan.zone.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Sdwan-Zone '{value}' not found in "
                    "system/sdwan/zone"
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
            >>> policy = StaticModel(
            ...     dstaddr="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dstaddr", None)
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
                f"Dstaddr '{value}' not found in "
                "firewall/address or firewall/addrgrp"
            )        
        return errors    
    async def validate_internet_service_references(self, client: Any) -> list[str]:
        """
        Validate internet_service references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = StaticModel(
            ...     internet_service="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "internet_service", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.internet-service.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Internet-Service '{value}' not found in "
                "firewall/internet-service"
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
            >>> policy = StaticModel(
            ...     internet_service_custom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_custom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "internet_service_custom", None)
        if not value:
            return errors
        
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
            >>> policy = StaticModel(
            ...     internet_service_fortiguard="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internet_service_fortiguard_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "internet_service_fortiguard", None)
        if not value:
            return errors
        
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
        errors = await self.validate_sdwan_zone_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_custom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internet_service_fortiguard_references(client)
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
    "StaticModel",    "StaticSdwanZone",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.573908Z
# ============================================================================
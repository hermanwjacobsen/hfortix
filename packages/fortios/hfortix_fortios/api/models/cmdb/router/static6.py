"""
Pydantic Models for CMDB - router/static6

Runtime validation models for router/static6 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class Static6SdwanZone(BaseModel):
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

class Static6Model(BaseModel):
    """
    Pydantic model for router/static6 configuration.
    
    Configure IPv6 static routing tables.
    
    Validation Rules:        - seq_num: min=0 max=4294967295 pattern=        - status: pattern=        - dst: pattern=        - gateway: pattern=        - device: max_length=35 pattern=        - devindex: min=0 max=4294967295 pattern=        - distance: min=1 max=255 pattern=        - weight: min=0 max=255 pattern=        - priority: min=1 max=65535 pattern=        - comment: max_length=255 pattern=        - blackhole: pattern=        - dynamic_gateway: pattern=        - sdwan_zone: pattern=        - dstaddr: max_length=79 pattern=        - link_monitor_exempt: pattern=        - vrf: min=0 max=511 pattern=        - bfd: pattern=        - tag: min=0 max=4294967295 pattern=    """
    
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
    dst: str = Field(default="::/0", description="Destination IPv6 prefix.")    
    gateway: str | None = Field(default="::", description="IPv6 address of the gateway.")    
    device: str = Field(max_length=35, default="", description="Gateway out interface or tunnel.")  # datasource: ['system.interface.name']    
    devindex: int | None = Field(ge=0, le=4294967295, default=0, description="Device index (0 - 4294967295).")    
    distance: int | None = Field(ge=1, le=255, default=10, description="Administrative distance (1 - 255).")    
    weight: int | None = Field(ge=0, le=255, default=0, description="Administrative weight (0 - 255).")    
    priority: int | None = Field(ge=1, le=65535, default=1024, description="Administrative priority (1 - 65535).")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    blackhole: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable black hole.")    
    dynamic_gateway: Literal["enable", "disable"] | None = Field(default="disable", description="Enable use of dynamic gateway retrieved from Router Advertisement (RA).")    
    sdwan_zone: list[SdwanZone] = Field(default=None, description="Choose SD-WAN Zone.")    
    dstaddr: str | None = Field(max_length=79, default="", description="Name of firewall address or address group.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']    
    link_monitor_exempt: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable withdrawal of this static route when link monitor or health check is down.")    
    vrf: int | None = Field(ge=0, le=511, default="unspecified", description="Virtual Routing Forwarding ID.")    
    bfd: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Bidirectional Forwarding Detection (BFD).")    
    tag: int | None = Field(ge=0, le=4294967295, default=0, description="Route tag.")    
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
        
        Datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
        
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
            >>> policy = Static6Model(
            ...     device="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_device_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static6.post(policy.to_fortios_dict())
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
            >>> policy = Static6Model(
            ...     sdwan_zone=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sdwan_zone_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static6.post(policy.to_fortios_dict())
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
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Static6Model(
            ...     dstaddr="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.static6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dstaddr", None)
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
                f"Dstaddr '{value}' not found in "
                "firewall/address6 or firewall/addrgrp6"
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
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "Static6Model",    "Static6SdwanZone",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.899544Z
# ============================================================================
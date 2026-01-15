"""
Pydantic Models for CMDB - system/ipam

Runtime validation models for system/ipam configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class IpamPools(BaseModel):
    """
    Child table model for pools.
    
    Configure IPAM pools.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPAM pool name.")    
    description: str | None = Field(max_length=127, default="", description="Description.")    
    subnet: str = Field(default="0.0.0.0 0.0.0.0", description="Configure IPAM pool subnet, Class A - Class B subnet.")    
    exclude: list[Exclude] = Field(default=None, description="Configure pool exclude subnets.")
class IpamRules(BaseModel):
    """
    Child table model for rules.
    
    Configure IPAM allocation rules.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPAM rule name.")    
    description: str | None = Field(max_length=127, default="", description="Description.")    
    device: list[Device] = Field(description="Configure serial number or wildcard of FortiGate to match.")    
    interface: list[Interface] = Field(description="Configure name or wildcard of interface to match.")    
    role: RoleEnum | None = Field(default="any", description="Configure role of interface to match.")    
    pool: list[Pool] = Field(description="Configure name of IPAM pool to use.")    
    dhcp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DHCP server for matching IPAM interfaces.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class IpamModel(BaseModel):
    """
    Pydantic model for system/ipam configuration.
    
    Configure IP address management services.
    
    Validation Rules:        - status: pattern=        - server_type: pattern=        - automatic_conflict_resolution: pattern=        - require_subnet_size_match: pattern=        - manage_lan_addresses: pattern=        - manage_lan_extension_addresses: pattern=        - manage_ssid_addresses: pattern=        - pools: pattern=        - rules: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IP address management services.")    
    server_type: Literal["fabric-root"] | None = Field(default="fabric-root", description="Configure the type of IPAM server to use.")    
    automatic_conflict_resolution: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable automatic conflict resolution.")    
    require_subnet_size_match: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable reassignment of subnets to make requested and actual sizes match.")    
    manage_lan_addresses: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable default management of LAN interface addresses.")    
    manage_lan_extension_addresses: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable default management of FortiExtender LAN extension interface addresses.")    
    manage_ssid_addresses: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable default management of FortiAP SSID addresses.")    
    pools: list[Pools] = Field(default=None, description="Configure IPAM pools.")    
    rules: list[Rules] = Field(default=None, description="Configure IPAM allocation rules.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "IpamModel",    "IpamPools",    "IpamRules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.965750Z
# ============================================================================
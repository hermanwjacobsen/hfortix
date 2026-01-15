"""
Pydantic Models for CMDB - router/multicast6

Runtime validation models for router/multicast6 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class Multicast6Interface(BaseModel):
    """
    Child table model for interface.
    
    Protocol Independent Multicast (PIM) interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    hello_interval: int | None = Field(ge=1, le=65535, default=30, description="Interval between sending PIM hello messages in seconds (1 - 65535, default = 30).")    
    hello_holdtime: int | None = Field(ge=1, le=65535, default="", description="Time before old neighbor information expires in seconds (1 - 65535, default = 105).")
class Multicast6PimSmGlobal(BaseModel):
    """
    Child table model for pim-sm-global.
    
    PIM sparse-mode global settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    register_rate_limit: int | None = Field(ge=0, le=65535, default=0, description="Limit of packets/sec per source registered through this RP (0 means unlimited).")    
    pim_use_sdwan: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of SDWAN when checking RPF neighbor and sending of REG packet.")    
    rp_address: list[RpAddress] = Field(default=None, description="Statically configured RP addresses.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class Multicast6Model(BaseModel):
    """
    Pydantic model for router/multicast6 configuration.
    
    Configure IPv6 multicast.
    
    Validation Rules:        - multicast_routing: pattern=        - multicast_pmtu: pattern=        - interface: pattern=        - pim_sm_global: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    multicast_routing: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 multicast routing.")    
    multicast_pmtu: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PMTU for IPv6 multicast.")    
    interface: list[Interface] = Field(default=None, description="Protocol Independent Multicast (PIM) interfaces.")    
    pim_sm_global: list[PimSmGlobal] = Field(default=None, description="PIM sparse-mode global settings.")    
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
            >>> policy = Multicast6Model(
            ...     interface=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.multicast6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "interface", [])
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
            
            if not found:
                errors.append(
                    f"Interface '{value}' not found in "
                    "system/interface"
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
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "Multicast6Model",    "Multicast6Interface",    "Multicast6PimSmGlobal",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.408294Z
# ============================================================================
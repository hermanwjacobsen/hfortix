"""
Pydantic Models for CMDB - firewall/vipgrp6

Runtime validation models for firewall/vipgrp6 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class Vipgrp6Member(BaseModel):
    """
    Child table model for member.
    
    Member VIP objects of the group (Separate multiple objects with a space).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 VIP name.")  # datasource: ['firewall.vip6.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class Vipgrp6Model(BaseModel):
    """
    Pydantic model for firewall/vipgrp6 configuration.
    
    Configure IPv6 virtual IP groups.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: pattern=        - color: min=0 max=32 pattern=        - comments: max_length=255 pattern=        - member: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="IPv6 VIP group name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    color: int | None = Field(ge=0, le=32, default=0, description="Integer value to determine the color of the icon in the GUI (range 1 to 32, default = 0, which sets the value to 1).")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    member: list[Member] = Field(description="Member VIP objects of the group (Separate multiple objects with a space).")    
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
    async def validate_member_references(self, client: Any) -> list[str]:
        """
        Validate member references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/vip6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Vipgrp6Model(
            ...     member=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_member_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.vipgrp6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "member", [])
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
            if await client.api.cmdb.firewall.vip6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Member '{value}' not found in "
                    "firewall/vip6"
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
        
        errors = await self.validate_member_references(client)
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
    "Vipgrp6Model",    "Vipgrp6Member",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.321619Z
# ============================================================================
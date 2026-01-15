"""
Pydantic Models for CMDB - firewall/identity_based_route

Runtime validation models for firewall/identity_based_route configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class IdentityBasedRouteRule(BaseModel):
    """
    Child table model for rule.
    
    Rule.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Rule ID.")    
    gateway: str | None = Field(default="0.0.0.0", description="IPv4 address of the gateway (Format: xxx.xxx.xxx.xxx , Default: 0.0.0.0).")    
    device: str = Field(max_length=35, default="", description="Outgoing interface for the rule.")  # datasource: ['system.interface.name']    
    groups: list[Groups] = Field(description="Select one or more group(s) from available groups that are allowed to use this route. Separate group names with a space.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class IdentityBasedRouteModel(BaseModel):
    """
    Pydantic model for firewall/identity_based_route configuration.
    
    Configure identity based routing.
    
    Validation Rules:        - name: max_length=35 pattern=        - comments: max_length=127 pattern=        - rule: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name.")    
    comments: str | None = Field(max_length=127, default="", description="Comments.")    
    rule: list[Rule] = Field(default=None, description="Rule.")    
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
    async def validate_rule_references(self, client: Any) -> list[str]:
        """
        Validate rule references exist in FortiGate.
        
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
            >>> policy = IdentityBasedRouteModel(
            ...     rule=[{"device": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_rule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.identity_based_route.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "rule", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("device")
            else:
                value = getattr(item, "device", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Rule '{value}' not found in "
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
        
        errors = await self.validate_rule_references(client)
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
    "IdentityBasedRouteModel",    "IdentityBasedRouteRule",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.128728Z
# ============================================================================
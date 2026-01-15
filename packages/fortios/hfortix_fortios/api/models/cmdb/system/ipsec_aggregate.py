"""
Pydantic Models for CMDB - system/ipsec_aggregate

Runtime validation models for system/ipsec_aggregate configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class IpsecAggregateMember(BaseModel):
    """
    Child table model for member.
    
    Member tunnels of the aggregate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    tunnel_name: str = Field(max_length=79, default="", description="Tunnel name.")  # datasource: ['vpn.ipsec.phase1-interface.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class IpsecAggregateAlgorithmEnum(str, Enum):
    """Allowed values for algorithm field."""
    L3 = "L3"    L4 = "L4"    ROUND_ROBIN = "round-robin"    REDUNDANT = "redundant"    WEIGHTED_ROUND_ROBIN = "weighted-round-robin"

# ============================================================================
# Main Model
# ============================================================================

class IpsecAggregateModel(BaseModel):
    """
    Pydantic model for system/ipsec_aggregate configuration.
    
    Configure an aggregate of IPsec tunnels.
    
    Validation Rules:        - name: max_length=15 pattern=        - member: pattern=        - algorithm: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="IPsec aggregate name.")    
    member: list[Member] = Field(description="Member tunnels of the aggregate.")    
    algorithm: AlgorithmEnum | None = Field(default="round-robin", description="Frame distribution algorithm.")    
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
        - vpn/ipsec/phase1-interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IpsecAggregateModel(
            ...     member=[{"tunnel-name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_member_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ipsec_aggregate.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "member", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("tunnel-name")
            else:
                value = getattr(item, "tunnel-name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.vpn.ipsec.phase1-interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Member '{value}' not found in "
                    "vpn/ipsec/phase1-interface"
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
    "IpsecAggregateModel",    "IpsecAggregateMember",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.960145Z
# ============================================================================
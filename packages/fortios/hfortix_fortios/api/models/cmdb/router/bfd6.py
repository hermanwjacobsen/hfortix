"""
Pydantic Models for CMDB - router/bfd6

Runtime validation models for router/bfd6 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class Bfd6Neighbor(BaseModel):
    """
    Child table model for neighbor.
    
    Configure neighbor of IPv6 BFD.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip6_address: str = Field(default="::", description="IPv6 address of the BFD neighbor.")    
    interface: str = Field(max_length=15, default="", description="Interface to the BFD neighbor.")  # datasource: ['system.interface.name']
class Bfd6MultihopTemplate(BaseModel):
    """
    Child table model for multihop-template.
    
    BFD IPv6 multi-hop template table.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    src: str = Field(default="::/0", description="Source prefix.")    
    dst: str = Field(default="::/0", description="Destination prefix.")    
    bfd_desired_min_tx: int | None = Field(ge=100, le=30000, default=250, description="BFD desired minimal transmit interval (milliseconds).")    
    bfd_required_min_rx: int | None = Field(ge=100, le=30000, default=250, description="BFD required minimal receive interval (milliseconds).")    
    bfd_detect_mult: int | None = Field(ge=3, le=50, default=3, description="BFD detection multiplier.")    
    auth_mode: Literal["none", "md5"] | None = Field(default="none", description="Authentication mode.")    
    md5_key: Any = Field(max_length=16, default=None, description="MD5 key of key ID 1.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class Bfd6Model(BaseModel):
    """
    Pydantic model for router/bfd6 configuration.
    
    Configure IPv6 BFD.
    
    Validation Rules:        - neighbor: pattern=        - multihop_template: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    neighbor: list[Neighbor] = Field(default=None, description="Configure neighbor of IPv6 BFD.")    
    multihop_template: list[MultihopTemplate] = Field(default=None, description="BFD IPv6 multi-hop template table.")    
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
    async def validate_neighbor_references(self, client: Any) -> list[str]:
        """
        Validate neighbor references exist in FortiGate.
        
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
            >>> policy = Bfd6Model(
            ...     neighbor=[{"interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_neighbor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.bfd6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "neighbor", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("interface")
            else:
                value = getattr(item, "interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Neighbor '{value}' not found in "
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
        
        errors = await self.validate_neighbor_references(client)
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
    "Bfd6Model",    "Bfd6Neighbor",    "Bfd6MultihopTemplate",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.047551Z
# ============================================================================
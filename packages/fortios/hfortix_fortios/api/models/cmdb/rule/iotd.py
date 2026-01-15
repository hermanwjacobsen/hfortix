"""
Pydantic Models for CMDB - rule/iotd

Runtime validation models for rule/iotd configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class IotdParameters(BaseModel):
    """
    Child table model for parameters.
    
    Application parameters.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=31, default="", description="Parameter name.")    
    default value: str | None = Field(max_length=199, default="", description="Parameter default value.")
class IotdMetadata(BaseModel):
    """
    Child table model for metadata.
    
    Meta data.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    metaid: int | None = Field(ge=0, le=4294967295, default=0, description="Meta ID.")    
    valueid: int | None = Field(ge=0, le=4294967295, default=0, description="Value ID.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class IotdModel(BaseModel):
    """
    Pydantic model for rule/iotd configuration.
    
    Show IOT detection signatures.
    
    Validation Rules:        - name: max_length=63 pattern=        - id: min=0 max=4294967295 pattern=        - category: min=0 max=4294967295 pattern=        - popularity: min=0 max=255 pattern=        - risk: min=0 max=255 pattern=        - weight: min=0 max=255 pattern=        - protocol: pattern=        - technology: pattern=        - behavior: pattern=        - vendor: pattern=        - parameters: pattern=        - metadata: pattern=        - status: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Application name.")    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Application ID.")    
    category: int = Field(ge=0, le=4294967295, default=0, description="Application category ID.")    
    popularity: int | None = Field(ge=0, le=255, default=0, description="Application popularity.")    
    risk: int | None = Field(ge=0, le=255, default=0, description="Application risk.")    
    weight: int | None = Field(ge=0, le=255, default=0, description="Application weight.")    
    protocol: str | None = Field(default="", description="Application protocol.")    
    technology: str | None = Field(default="", description="Application technology.")    
    behavior: str | None = Field(default="", description="Application behavior.")    
    vendor: str | None = Field(default="", description="Application vendor.")    
    parameters: list[Parameters] = Field(default=None, description="Application parameters.")    
    metadata: list[Metadata] = Field(default=None, description="Meta data.")    
    status: Any = Field(default=None, description="Print all IOT detection rules information.")    
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
    "IotdModel",    "IotdParameters",    "IotdMetadata",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.638288Z
# ============================================================================
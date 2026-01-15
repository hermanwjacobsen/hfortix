"""
Pydantic Models for CMDB - application/group

Runtime validation models for application/group configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class GroupApplication(BaseModel):
    """
    Child table model for application.
    
    Application ID list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Application IDs.")
class GroupCategory(BaseModel):
    """
    Child table model for category.
    
    Application category ID list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Category IDs.")
class GroupRisk(BaseModel):
    """
    Child table model for risk.
    
    Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    level: int = Field(ge=0, le=4294967295, default=0, description="Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class GroupPopularityEnum(str, Enum):
    """Allowed values for popularity field."""
    1 = "1"    2 = "2"    3 = "3"    4 = "4"    5 = "5"

# ============================================================================
# Main Model
# ============================================================================

class GroupModel(BaseModel):
    """
    Pydantic model for application/group configuration.
    
    Configure firewall application groups.
    
    Validation Rules:        - name: max_length=63 pattern=        - comment: max_length=255 pattern=        - type: pattern=        - application: pattern=        - category: pattern=        - risk: pattern=        - protocols: pattern=        - vendor: pattern=        - technology: pattern=        - behavior: pattern=        - popularity: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Application group name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comments.")    
    type: Literal["application", "filter"] | None = Field(default="application", description="Application group type.")    
    application: list[Application] = Field(default=None, description="Application ID list.")    
    category: list[Category] = Field(default=None, description="Application category ID list.")    
    risk: list[Risk] = Field(default=None, description="Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical).")    
    protocols: list[Protocols] = Field(default="all", description="Application protocol filter.")    
    vendor: list[Vendor] = Field(default="all", description="Application vendor filter.")    
    technology: list[Technology] = Field(default="all", description="Application technology filter.")    
    behavior: list[Behavior] = Field(default="all", description="Application behavior filter.")    
    popularity: list[Popularity] = Field(default="1 2 3 4 5", description="Application popularity filter (1 - 5, from least to most popular).")    
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
    "GroupModel",    "GroupApplication",    "GroupCategory",    "GroupRisk",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.015948Z
# ============================================================================
"""
Pydantic Models for CMDB - switch_controller/acl/ingress

Runtime validation models for switch_controller/acl/ingress configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class IngressAction(BaseModel):
    """
    Child table model for action.
    
    ACL actions.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    drop: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable drop.")    
    count: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable count.")
class IngressClassifier(BaseModel):
    """
    Child table model for classifier.
    
    ACL classifiers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    dst_ip_prefix: str | None = Field(default="0.0.0.0 0.0.0.0", description="Destination IP address to be matched.")    
    dst_mac: str | None = Field(default="00:00:00:00:00:00", description="Destination MAC address to be matched.")    
    src_ip_prefix: str | None = Field(default="0.0.0.0 0.0.0.0", description="Source IP address to be matched.")    
    src_mac: str | None = Field(default="00:00:00:00:00:00", description="Source MAC address to be matched.")    
    vlan: int | None = Field(ge=1, le=4094, default=0, description="VLAN ID to be matched.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class IngressModel(BaseModel):
    """
    Pydantic model for switch_controller/acl/ingress configuration.
    
    Configure ingress ACL policies to be applied on managed FortiSwitch ports.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - description: max_length=63 pattern=        - action: pattern=        - classifier: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ACL ID.")    
    description: str | None = Field(max_length=63, default="", description="Description for the ACL policy.")    
    action: list[Action] = Field(default=None, description="ACL actions.")    
    classifier: list[Classifier] = Field(default=None, description="ACL classifiers.")    
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
    "IngressModel",    "IngressAction",    "IngressClassifier",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.989183Z
# ============================================================================
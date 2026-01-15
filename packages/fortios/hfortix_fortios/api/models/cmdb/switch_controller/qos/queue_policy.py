"""
Pydantic Models for CMDB - switch_controller/qos/queue_policy

Runtime validation models for switch_controller/qos/queue_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class QueuePolicyCosQueue(BaseModel):
    """
    Child table model for cos-queue.
    
    COS queue configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=63, default="", description="Cos queue ID.")    
    description: str | None = Field(max_length=63, default="", description="Description of the COS queue.")    
    min_rate: int | None = Field(ge=0, le=4294967295, default=0, description="Minimum rate (0 - 4294967295 kbps, 0 to disable).")    
    max_rate: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum rate (0 - 4294967295 kbps, 0 to disable).")    
    min_rate_percent: int | None = Field(ge=0, le=4294967295, default=0, description="Minimum rate (% of link speed).")    
    max_rate_percent: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum rate (% of link speed).")    
    drop_policy: Literal["taildrop", "weighted-random-early-detection"] | None = Field(default="taildrop", description="COS queue drop policy.")    
    ecn: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable ECN packet marking to drop eligible packets.")    
    weight: int | None = Field(ge=0, le=4294967295, default=1, description="Weight of weighted round robin scheduling.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class QueuePolicyModel(BaseModel):
    """
    Pydantic model for switch_controller/qos/queue_policy configuration.
    
    Configure FortiSwitch QoS egress queue policy.
    
    Validation Rules:        - name: max_length=63 pattern=        - schedule: pattern=        - rate_by: pattern=        - cos_queue: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=63, default="", description="QoS policy name.")    
    schedule: Literal["strict", "round-robin", "weighted"] = Field(default="round-robin", description="COS queue scheduling.")    
    rate_by: Literal["kbps", "percent"] = Field(default="kbps", description="COS queue rate by kbps or percent.")    
    cos_queue: list[CosQueue] = Field(default=None, description="COS queue configuration.")    
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
    "QueuePolicyModel",    "QueuePolicyCosQueue",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.100466Z
# ============================================================================
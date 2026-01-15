"""
Pydantic Models for CMDB - switch_controller/qos/dot1p_map

Runtime validation models for switch_controller/qos/dot1p_map configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class Dot1pMapPriority_0Enum(str, Enum):
    """Allowed values for priority_0 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"
class Dot1pMapPriority_1Enum(str, Enum):
    """Allowed values for priority_1 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"
class Dot1pMapPriority_2Enum(str, Enum):
    """Allowed values for priority_2 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"
class Dot1pMapPriority_3Enum(str, Enum):
    """Allowed values for priority_3 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"
class Dot1pMapPriority_4Enum(str, Enum):
    """Allowed values for priority_4 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"
class Dot1pMapPriority_5Enum(str, Enum):
    """Allowed values for priority_5 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"
class Dot1pMapPriority_6Enum(str, Enum):
    """Allowed values for priority_6 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"
class Dot1pMapPriority_7Enum(str, Enum):
    """Allowed values for priority_7 field."""
    QUEUE_0 = "queue-0"    QUEUE_1 = "queue-1"    QUEUE_2 = "queue-2"    QUEUE_3 = "queue-3"    QUEUE_4 = "queue-4"    QUEUE_5 = "queue-5"    QUEUE_6 = "queue-6"    QUEUE_7 = "queue-7"

# ============================================================================
# Main Model
# ============================================================================

class Dot1pMapModel(BaseModel):
    """
    Pydantic model for switch_controller/qos/dot1p_map configuration.
    
    Configure FortiSwitch QoS 802.1p.
    
    Validation Rules:        - name: max_length=63 pattern=        - description: max_length=63 pattern=        - egress_pri_tagging: pattern=        - priority_0: pattern=        - priority_1: pattern=        - priority_2: pattern=        - priority_3: pattern=        - priority_4: pattern=        - priority_5: pattern=        - priority_6: pattern=        - priority_7: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=63, default="", description="Dot1p map name.")    
    description: str | None = Field(max_length=63, default="", description="Description of the 802.1p name.")    
    egress_pri_tagging: Literal["disable", "enable"] = Field(default="disable", description="Enable/disable egress priority-tag frame.")    
    priority_0: Priority0Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
    priority_1: Priority1Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
    priority_2: Priority2Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
    priority_3: Priority3Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
    priority_4: Priority4Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
    priority_5: Priority5Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
    priority_6: Priority6Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
    priority_7: Priority7Enum | None = Field(default="queue-0", description="COS queue mapped to dot1p priority number.")    
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
    "Dot1pMapModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.392592Z
# ============================================================================
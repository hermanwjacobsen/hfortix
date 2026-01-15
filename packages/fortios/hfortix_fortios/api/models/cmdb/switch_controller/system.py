"""
Pydantic Models for CMDB - switch_controller/system

Runtime validation models for switch_controller/system configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SystemModel(BaseModel):
    """
    Pydantic model for switch_controller/system configuration.
    
    Configure system-wide switch controller settings.
    
    Validation Rules:        - parallel_process_override: pattern=        - parallel_process: min=1 max=24 pattern=        - data_sync_interval: min=30 max=1800 pattern=        - iot_weight_threshold: min=0 max=255 pattern=        - iot_scan_interval: min=2 max=10080 pattern=        - iot_holdoff: min=0 max=10080 pattern=        - iot_mac_idle: min=0 max=10080 pattern=        - nac_periodic_interval: min=5 max=180 pattern=        - dynamic_periodic_interval: min=5 max=180 pattern=        - tunnel_mode: pattern=        - caputp_echo_interval: min=8 max=600 pattern=        - caputp_max_retransmit: min=0 max=64 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    parallel_process_override: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable parallel process override.")    
    parallel_process: int | None = Field(ge=1, le=24, default=1, description="Maximum number of parallel processes.")    
    data_sync_interval: int | None = Field(ge=30, le=1800, default=60, description="Time interval between collection of switch data (30 - 1800 sec, default = 60, 0 = disable).")    
    iot_weight_threshold: int | None = Field(ge=0, le=255, default=1, description="MAC entry's confidence value. Value is re-queried when below this value (default = 1, 0 = disable).")    
    iot_scan_interval: int | None = Field(ge=2, le=10080, default=60, description="IoT scan interval (2 - 10080 mins, default = 60 mins, 0 = disable).")    
    iot_holdoff: int | None = Field(ge=0, le=10080, default=5, description="MAC entry's creation time. Time must be greater than this value for an entry to be created (0 - 10080 mins, default = 5 mins).")    
    iot_mac_idle: int | None = Field(ge=0, le=10080, default=1440, description="MAC entry's idle time. MAC entry is removed after this value (0 - 10080 mins, default = 1440 mins).")    
    nac_periodic_interval: int | None = Field(ge=5, le=180, default=60, description="Periodic time interval to run NAC engine (5 - 180 sec, default = 60).")    
    dynamic_periodic_interval: int | None = Field(ge=5, le=180, default=60, description="Periodic time interval to run Dynamic port policy engine (5 - 180 sec, default = 60).")    
    tunnel_mode: Literal["compatible", "moderate", "strict"] | None = Field(default="compatible", description="Compatible/strict tunnel mode.")    
    caputp_echo_interval: int | None = Field(ge=8, le=600, default=30, description="Echo interval for the caputp echo requests from swtp.")    
    caputp_max_retransmit: int | None = Field(ge=0, le=64, default=5, description="Maximum retransmission count for the caputp tunnel packets.")    
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
    "SystemModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:41.794177Z
# ============================================================================
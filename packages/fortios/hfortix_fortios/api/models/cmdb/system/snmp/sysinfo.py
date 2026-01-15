"""
Pydantic Models for CMDB - system/snmp/sysinfo

Runtime validation models for system/snmp/sysinfo configuration.
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

class SysinfoModel(BaseModel):
    """
    Pydantic model for system/snmp/sysinfo configuration.
    
    SNMP system info configuration.
    
    Validation Rules:        - status: pattern=        - engine_id_type: pattern=        - engine_id: max_length=54 pattern=        - description: max_length=255 pattern=        - contact_info: max_length=255 pattern=        - location: max_length=255 pattern=        - trap_high_cpu_threshold: min=1 max=100 pattern=        - trap_low_memory_threshold: min=1 max=100 pattern=        - trap_log_full_threshold: min=1 max=100 pattern=        - trap_free_memory_threshold: min=1 max=100 pattern=        - trap_freeable_memory_threshold: min=1 max=100 pattern=        - append_index: pattern=        - non_mgmt_vdom_query: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SNMP.")    
    engine_id_type: Literal["text", "hex", "mac"] | None = Field(default="text", description="Local SNMP engineID type (text/hex/mac).")    
    engine_id: str | None = Field(max_length=54, default="", description="Local SNMP engineID string (maximum 27 characters).")    
    description: str | None = Field(max_length=255, default=None, description="System description.")    
    contact_info: str | None = Field(max_length=255, default=None, description="Contact information.")    
    location: str | None = Field(max_length=255, default=None, description="System location.")    
    trap_high_cpu_threshold: int | None = Field(ge=1, le=100, default=80, description="CPU usage when trap is sent.")    
    trap_low_memory_threshold: int | None = Field(ge=1, le=100, default=80, description="Memory usage when trap is sent.")    
    trap_log_full_threshold: int | None = Field(ge=1, le=100, default=90, description="Log disk usage when trap is sent.")    
    trap_free_memory_threshold: int | None = Field(ge=1, le=100, default=5, description="Free memory usage when trap is sent.")    
    trap_freeable_memory_threshold: int | None = Field(ge=1, le=100, default=60, description="Freeable memory usage when trap is sent.")    
    append_index: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowance of appending vdom or interface index in some RFC tables.")    
    non_mgmt_vdom_query: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowance of SNMPv3 query from non-management vdoms.")    
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
    "SysinfoModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.103620Z
# ============================================================================
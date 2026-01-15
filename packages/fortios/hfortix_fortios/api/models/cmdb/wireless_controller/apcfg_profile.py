"""
Pydantic Models for CMDB - wireless_controller/apcfg_profile

Runtime validation models for wireless_controller/apcfg_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ApcfgProfileCommandList(BaseModel):
    """
    Child table model for command-list.
    
    AP local configuration command list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=1, le=255, default=0, description="Command ID.")    
    type: Literal["non-password", "password"] | None = Field(default="non-password", description="The command type (default = non-password).")    
    name: str | None = Field(max_length=63, default="", description="AP local configuration command name.")    
    value: str | None = Field(max_length=127, default="", description="AP local configuration command value.")    
    passwd_value: Any = Field(max_length=128, default=None, description="AP local configuration command password value.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ApcfgProfileModel(BaseModel):
    """
    Pydantic model for wireless_controller/apcfg_profile configuration.
    
    Configure AP local configuration profiles.
    
    Validation Rules:        - name: max_length=35 pattern=        - ap_family: pattern=        - comment: max_length=255 pattern=        - ac_type: pattern=        - ac_timer: min=3 max=30 pattern=        - ac_ip: pattern=        - ac_port: min=1024 max=49150 pattern=        - command_list: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="AP local configuration profile name.")    
    ap_family: Literal["fap", "fap-u", "fap-c"] | None = Field(default="fap", description="FortiAP family type (default = fap).")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    ac_type: Literal["default", "specify", "apcfg"] | None = Field(default="default", description="Validation controller type (default = default).")    
    ac_timer: int | None = Field(ge=3, le=30, default=10, description="Maximum waiting time for the AP to join the validation controller after applying AP local configuration (3 - 30 min, default = 10).")    
    ac_ip: str | None = Field(default="0.0.0.0", description="IP address of the validation controller that AP must be able to join after applying AP local configuration.")    
    ac_port: int | None = Field(ge=1024, le=49150, default=5246, description="Port of the validation controller that AP must be able to join after applying AP local configuration (1024 - 49150, default = 5246).")    
    command_list: list[CommandList] = Field(default=None, description="AP local configuration command list.")    
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
    "ApcfgProfileModel",    "ApcfgProfileCommandList",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.013455Z
# ============================================================================
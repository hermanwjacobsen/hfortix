"""
Pydantic Models for CMDB - wireless_controller/qos_profile

Runtime validation models for wireless_controller/qos_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class QosProfileDscpWmmVo(BaseModel):
    """
    Child table model for dscp-wmm-vo.
    
    DSCP mapping for voice access (default = 48 56).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=63, default=0, description="DSCP WMM mapping numbers (0 - 63).")
class QosProfileDscpWmmVi(BaseModel):
    """
    Child table model for dscp-wmm-vi.
    
    DSCP mapping for video access (default = 32 40).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=63, default=0, description="DSCP WMM mapping numbers (0 - 63).")
class QosProfileDscpWmmBe(BaseModel):
    """
    Child table model for dscp-wmm-be.
    
    DSCP mapping for best effort access (default = 0 24).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=63, default=0, description="DSCP WMM mapping numbers (0 - 63).")
class QosProfileDscpWmmBk(BaseModel):
    """
    Child table model for dscp-wmm-bk.
    
    DSCP mapping for background access (default = 8 16).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=63, default=0, description="DSCP WMM mapping numbers (0 - 63).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class QosProfileModel(BaseModel):
    """
    Pydantic model for wireless_controller/qos_profile configuration.
    
    Configure WiFi quality of service (QoS) profiles.
    
    Validation Rules:        - name: max_length=35 pattern=        - comment: max_length=63 pattern=        - uplink: min=0 max=2097152 pattern=        - downlink: min=0 max=2097152 pattern=        - uplink_sta: min=0 max=2097152 pattern=        - downlink_sta: min=0 max=2097152 pattern=        - burst: pattern=        - wmm: pattern=        - wmm_uapsd: pattern=        - call_admission_control: pattern=        - call_capacity: min=0 max=60 pattern=        - bandwidth_admission_control: pattern=        - bandwidth_capacity: min=1 max=600000 pattern=        - dscp_wmm_mapping: pattern=        - dscp_wmm_vo: pattern=        - dscp_wmm_vi: pattern=        - dscp_wmm_be: pattern=        - dscp_wmm_bk: pattern=        - wmm_dscp_marking: pattern=        - wmm_vo_dscp: min=0 max=63 pattern=        - wmm_vi_dscp: min=0 max=63 pattern=        - wmm_be_dscp: min=0 max=63 pattern=        - wmm_bk_dscp: min=0 max=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="WiFi QoS profile name.")    
    comment: str | None = Field(max_length=63, default="", description="Comment.")    
    uplink: int | None = Field(ge=0, le=2097152, default=0, description="Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).")    
    downlink: int | None = Field(ge=0, le=2097152, default=0, description="Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).")    
    uplink_sta: int | None = Field(ge=0, le=2097152, default=0, description="Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).")    
    downlink_sta: int | None = Field(ge=0, le=2097152, default=0, description="Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).")    
    burst: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable client rate burst.")    
    wmm: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable WiFi multi-media (WMM) control.")    
    wmm_uapsd: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.")    
    call_admission_control: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WMM call admission control.")    
    call_capacity: int | None = Field(ge=0, le=60, default=10, description="Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10).")    
    bandwidth_admission_control: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WMM bandwidth admission control.")    
    bandwidth_capacity: int | None = Field(ge=1, le=600000, default=2000, description="Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).")    
    dscp_wmm_mapping: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Differentiated Services Code Point (DSCP) mapping.")    
    dscp_wmm_vo: list[DscpWmmVo] = Field(default=None, description="DSCP mapping for voice access (default = 48 56).")    
    dscp_wmm_vi: list[DscpWmmVi] = Field(default=None, description="DSCP mapping for video access (default = 32 40).")    
    dscp_wmm_be: list[DscpWmmBe] = Field(default=None, description="DSCP mapping for best effort access (default = 0 24).")    
    dscp_wmm_bk: list[DscpWmmBk] = Field(default=None, description="DSCP mapping for background access (default = 8 16).")    
    wmm_dscp_marking: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WMM Differentiated Services Code Point (DSCP) marking.")    
    wmm_vo_dscp: int | None = Field(ge=0, le=63, default=48, description="DSCP marking for voice access (default = 48).")    
    wmm_vi_dscp: int | None = Field(ge=0, le=63, default=32, description="DSCP marking for video access (default = 32).")    
    wmm_be_dscp: int | None = Field(ge=0, le=63, default=0, description="DSCP marking for best effort access (default = 0).")    
    wmm_bk_dscp: int | None = Field(ge=0, le=63, default=8, description="DSCP marking for background access (default = 8).")    
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
    "QosProfileModel",    "QosProfileDscpWmmVo",    "QosProfileDscpWmmVi",    "QosProfileDscpWmmBe",    "QosProfileDscpWmmBk",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.641214Z
# ============================================================================
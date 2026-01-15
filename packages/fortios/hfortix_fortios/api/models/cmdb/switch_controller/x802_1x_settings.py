"""
Pydantic Models for CMDB - switch_controller/x802_1x_settings

Runtime validation models for switch_controller/x802_1x_settings configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class X8021xSettingsMac_username_delimiterEnum(str, Enum):
    """Allowed values for mac_username_delimiter field."""
    COLON = "colon"    HYPHEN = "hyphen"    NONE = "none"    SINGLE_HYPHEN = "single-hyphen"
class X8021xSettingsMac_password_delimiterEnum(str, Enum):
    """Allowed values for mac_password_delimiter field."""
    COLON = "colon"    HYPHEN = "hyphen"    NONE = "none"    SINGLE_HYPHEN = "single-hyphen"
class X8021xSettingsMac_calling_station_delimiterEnum(str, Enum):
    """Allowed values for mac_calling_station_delimiter field."""
    COLON = "colon"    HYPHEN = "hyphen"    NONE = "none"    SINGLE_HYPHEN = "single-hyphen"
class X8021xSettingsMac_called_station_delimiterEnum(str, Enum):
    """Allowed values for mac_called_station_delimiter field."""
    COLON = "colon"    HYPHEN = "hyphen"    NONE = "none"    SINGLE_HYPHEN = "single-hyphen"

# ============================================================================
# Main Model
# ============================================================================

class X8021xSettingsModel(BaseModel):
    """
    Pydantic model for switch_controller/x802_1x_settings configuration.
    
    Configure global 802.1X settings.
    
    Validation Rules:        - link_down_auth: pattern=        - reauth_period: min=0 max=1440 pattern=        - max_reauth_attempt: min=0 max=15 pattern=        - tx_period: min=12 max=60 pattern=        - mab_reauth: pattern=        - mac_username_delimiter: pattern=        - mac_password_delimiter: pattern=        - mac_calling_station_delimiter: pattern=        - mac_called_station_delimiter: pattern=        - mac_case: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    link_down_auth: Literal["set-unauth", "no-action"] | None = Field(default="set-unauth", description="Interface-reauthentication state to set if a link is down.")    
    reauth_period: int | None = Field(ge=0, le=1440, default=60, description="Period of time to allow for reauthentication (1 - 1440 sec, default = 60, 0 = disable reauthentication).")    
    max_reauth_attempt: int | None = Field(ge=0, le=15, default=3, description="Maximum number of authentication attempts (0 - 15, default = 3).")    
    tx_period: int | None = Field(ge=12, le=60, default=30, description="802.1X Tx period (seconds, default=30).")    
    mab_reauth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable MAB re-authentication.")    
    mac_username_delimiter: MacUsernameDelimiterEnum | None = Field(default="hyphen", description="MAC authentication username delimiter (default = hyphen).")    
    mac_password_delimiter: MacPasswordDelimiterEnum | None = Field(default="hyphen", description="MAC authentication password delimiter (default = hyphen).")    
    mac_calling_station_delimiter: MacCallingStationDelimiterEnum | None = Field(default="hyphen", description="MAC calling station delimiter (default = hyphen).")    
    mac_called_station_delimiter: MacCalledStationDelimiterEnum | None = Field(default="hyphen", description="MAC called station delimiter (default = hyphen).")    
    mac_case: Literal["lowercase", "uppercase"] | None = Field(default="lowercase", description="MAC case (default = lowercase).")    
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
    "X8021xSettingsModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.765820Z
# ============================================================================
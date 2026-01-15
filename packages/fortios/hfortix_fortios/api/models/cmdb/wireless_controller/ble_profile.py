"""
Pydantic Models for CMDB - wireless_controller/ble_profile

Runtime validation models for wireless_controller/ble_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class BleProfileTxpowerEnum(str, Enum):
    """Allowed values for txpower field."""
    0 = "0"    1 = "1"    2 = "2"    3 = "3"    4 = "4"    5 = "5"    6 = "6"    7 = "7"    8 = "8"    9 = "9"    10 = "10"    11 = "11"    12 = "12"    13 = "13"    14 = "14"    15 = "15"    16 = "16"    17 = "17"

# ============================================================================
# Main Model
# ============================================================================

class BleProfileModel(BaseModel):
    """
    Pydantic model for wireless_controller/ble_profile configuration.
    
    Configure Bluetooth Low Energy profile.
    
    Validation Rules:        - name: max_length=35 pattern=        - comment: max_length=63 pattern=        - advertising: pattern=        - ibeacon_uuid: max_length=63 pattern=        - major_id: min=0 max=65535 pattern=        - minor_id: min=0 max=65535 pattern=        - eddystone_namespace: max_length=20 pattern=        - eddystone_instance: max_length=12 pattern=        - eddystone_url: max_length=127 pattern=        - txpower: pattern=        - beacon_interval: min=40 max=3500 pattern=        - ble_scanning: pattern=        - scan_type: pattern=        - scan_threshold: max_length=7 pattern=        - scan_period: min=1000 max=10000 pattern=        - scan_time: min=1000 max=10000 pattern=        - scan_interval: min=10 max=1000 pattern=        - scan_window: min=10 max=1000 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Bluetooth Low Energy profile name.")    
    comment: str | None = Field(max_length=63, default="", description="Comment.")    
    advertising: list[Advertising] = Field(default="", description="Advertising type.")    
    ibeacon_uuid: str | None = Field(max_length=63, default="005ea414-cbd1-11e5-9956-625662870761", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    major_id: int | None = Field(ge=0, le=65535, default=1000, description="Major ID.")    
    minor_id: int | None = Field(ge=0, le=65535, default=2000, description="Minor ID.")    
    eddystone_namespace: str | None = Field(max_length=20, default="0102030405", description="Eddystone namespace ID.")    
    eddystone_instance: str | None = Field(max_length=12, default="abcdef", description="Eddystone instance ID.")    
    eddystone_url: str | None = Field(max_length=127, default="http://www.fortinet.com", description="Eddystone URL.")    
    txpower: TxpowerEnum | None = Field(default="0", description="Transmit power level (default = 0).")    
    beacon_interval: int | None = Field(ge=40, le=3500, default=100, description="Beacon interval (default = 100 msec).")    
    ble_scanning: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Bluetooth Low Energy (BLE) scanning.")    
    scan_type: Literal["active", "passive"] | None = Field(default="active", description="Scan Type (default = active).")    
    scan_threshold: str | None = Field(max_length=7, default="-90", description="Minimum signal level/threshold in dBm required for the AP to report detected BLE device (-95 to -20, default = -90).")    
    scan_period: int | None = Field(ge=1000, le=10000, default=4000, description="Scan Period (default = 4000 msec).")    
    scan_time: int | None = Field(ge=1000, le=10000, default=1000, description="Scan Time (default = 1000 msec).")    
    scan_interval: int | None = Field(ge=10, le=1000, default=50, description="Scan Interval (default = 50 msec).")    
    scan_window: int | None = Field(ge=10, le=1000, default=50, description="Scan Windows (default = 50 msec).")    
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
    "BleProfileModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.914163Z
# ============================================================================
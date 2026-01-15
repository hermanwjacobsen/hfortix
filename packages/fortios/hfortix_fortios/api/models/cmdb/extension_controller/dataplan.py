"""
Pydantic Models for CMDB - extension_controller/dataplan

Runtime validation models for extension_controller/dataplan configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class DataplanTypeEnum(str, Enum):
    """Allowed values for type field."""
    CARRIER = "carrier"    SLOT = "slot"    ICCID = "iccid"    GENERIC = "generic"

# ============================================================================
# Main Model
# ============================================================================

class DataplanModel(BaseModel):
    """
    Pydantic model for extension_controller/dataplan configuration.
    
    FortiExtender dataplan configuration.
    
    Validation Rules:        - name: max_length=31 pattern=        - modem_id: pattern=        - type: pattern=        - slot: pattern=        - iccid: max_length=31 pattern=        - carrier: max_length=31 pattern=        - apn: max_length=63 pattern=        - auth_type: pattern=        - username: max_length=127 pattern=        - password: max_length=64 pattern=        - pdn: pattern=        - signal_threshold: min=50 max=100 pattern=        - signal_period: min=600 max=18000 pattern=        - capacity: min=0 max=102400000 pattern=        - monthly_fee: min=0 max=1000000 pattern=        - billing_date: min=1 max=31 pattern=        - overage: pattern=        - preferred_subnet: min=0 max=32 pattern=        - private_network: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=31, default="", description="FortiExtender data plan name.")    
    modem_id: Literal["modem1", "modem2", "all"] | None = Field(default="all", description="Dataplan's modem specifics, if any.")    
    type: TypeEnum = Field(default="generic", description="Type preferences configuration.")    
    slot: Literal["sim1", "sim2"] = Field(default="", description="SIM slot configuration.")    
    iccid: str = Field(max_length=31, default="", description="ICCID configuration.")    
    carrier: str = Field(max_length=31, default="", description="Carrier configuration.")    
    apn: str | None = Field(max_length=63, default="", description="APN configuration.")    
    auth_type: Literal["none", "pap", "chap"] | None = Field(default="none", description="Authentication type.")    
    username: str = Field(max_length=127, default="", description="Username.")    
    password: Any = Field(max_length=64, description="Password.")    
    pdn: Literal["ipv4-only", "ipv6-only", "ipv4-ipv6"] | None = Field(default="ipv4-only", description="PDN type.")    
    signal_threshold: int | None = Field(ge=50, le=100, default=100, description="Signal threshold. Specify the range between 50 - 100, where 50/100 means -50/-100 dBm.")    
    signal_period: int | None = Field(ge=600, le=18000, default=3600, description="Signal period (600 to 18000 seconds).")    
    capacity: int | None = Field(ge=0, le=102400000, default=0, description="Capacity in MB (0 - 102400000).")    
    monthly_fee: int | None = Field(ge=0, le=1000000, default=0, description="Monthly fee of dataplan (0 - 100000, in local currency).")    
    billing_date: int | None = Field(ge=1, le=31, default=1, description="Billing day of the month (1 - 31).")    
    overage: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable dataplan overage detection.")    
    preferred_subnet: int | None = Field(ge=0, le=32, default=0, description="Preferred subnet mask (0 - 32).")    
    private_network: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable dataplan private network support.")    
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
    "DataplanModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.580377Z
# ============================================================================
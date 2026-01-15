"""
Pydantic Models for CMDB - log/webtrends/filter

Runtime validation models for log/webtrends/filter configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class FilterFreeStyle(BaseModel):
    """
    Child table model for free-style.
    
    Free style filters.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    category: CategoryEnum = Field(default="traffic", description="Log category.")    
    filter: str = Field(max_length=1023, default="", description="Free style filter string.")    
    filter_type: Literal["include", "exclude"] | None = Field(default="include", description="Include/exclude logs that match the filter.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class FilterSeverityEnum(str, Enum):
    """Allowed values for severity field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"

# ============================================================================
# Main Model
# ============================================================================

class FilterModel(BaseModel):
    """
    Pydantic model for log/webtrends/filter configuration.
    
    Filters for WebTrends.
    
    Validation Rules:        - severity: pattern=        - forward_traffic: pattern=        - local_traffic: pattern=        - multicast_traffic: pattern=        - sniffer_traffic: pattern=        - ztna_traffic: pattern=        - http_transaction: pattern=        - anomaly: pattern=        - voip: pattern=        - gtp: pattern=        - forti_switch: pattern=        - debug: pattern=        - free_style: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    severity: SeverityEnum | None = Field(default="information", description="Lowest severity level to log to WebTrends.")    
    forward_traffic: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable forward traffic logging.")    
    local_traffic: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable local in or out traffic logging.")    
    multicast_traffic: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable multicast traffic logging.")    
    sniffer_traffic: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sniffer traffic logging.")    
    ztna_traffic: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable ztna traffic logging.")    
    http_transaction: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable log HTTP transaction messages.")    
    anomaly: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable anomaly logging.")    
    voip: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable VoIP logging.")    
    gtp: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable GTP messages logging.")    
    forti_switch: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Forti-Switch logging.")    
    debug: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable debug logging.")    
    free_style: list[FreeStyle] = Field(default=None, description="Free style filters.")    
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
    "FilterModel",    "FilterFreeStyle",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.117543Z
# ============================================================================
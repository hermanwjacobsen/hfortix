"""
Pydantic Models for CMDB - wireless_controller/log

Runtime validation models for wireless_controller/log configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LogAddrgrp_logEnum(str, Enum):
    """Allowed values for addrgrp_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogBle_logEnum(str, Enum):
    """Allowed values for ble_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogClb_logEnum(str, Enum):
    """Allowed values for clb_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogDhcp_starv_logEnum(str, Enum):
    """Allowed values for dhcp_starv_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogLed_sched_logEnum(str, Enum):
    """Allowed values for led_sched_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogRadio_event_logEnum(str, Enum):
    """Allowed values for radio_event_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogRogue_event_logEnum(str, Enum):
    """Allowed values for rogue_event_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogSta_event_logEnum(str, Enum):
    """Allowed values for sta_event_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogSta_locate_logEnum(str, Enum):
    """Allowed values for sta_locate_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogWids_logEnum(str, Enum):
    """Allowed values for wids_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogWtp_event_logEnum(str, Enum):
    """Allowed values for wtp_event_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"
class LogWtp_fips_event_logEnum(str, Enum):
    """Allowed values for wtp_fips_event_log field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"

# ============================================================================
# Main Model
# ============================================================================

class LogModel(BaseModel):
    """
    Pydantic model for wireless_controller/log configuration.
    
    Configure wireless controller event log filters.
    
    Validation Rules:        - status: pattern=        - addrgrp_log: pattern=        - ble_log: pattern=        - clb_log: pattern=        - dhcp_starv_log: pattern=        - led_sched_log: pattern=        - radio_event_log: pattern=        - rogue_event_log: pattern=        - sta_event_log: pattern=        - sta_locate_log: pattern=        - wids_log: pattern=        - wtp_event_log: pattern=        - wtp_fips_event_log: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable wireless event logging.")    
    addrgrp_log: AddrgrpLogEnum | None = Field(default="notification", description="Lowest severity level to log address group message.")    
    ble_log: BleLogEnum | None = Field(default="notification", description="Lowest severity level to log BLE detection message.")    
    clb_log: ClbLogEnum | None = Field(default="notification", description="Lowest severity level to log client load balancing message.")    
    dhcp_starv_log: DhcpStarvLogEnum | None = Field(default="notification", description="Lowest severity level to log DHCP starvation event message.")    
    led_sched_log: LedSchedLogEnum | None = Field(default="notification", description="Lowest severity level to log LED schedule event message.")    
    radio_event_log: RadioEventLogEnum | None = Field(default="notification", description="Lowest severity level to log radio event message.")    
    rogue_event_log: RogueEventLogEnum | None = Field(default="notification", description="Lowest severity level to log rogue AP event message.")    
    sta_event_log: StaEventLogEnum | None = Field(default="notification", description="Lowest severity level to log station event message.")    
    sta_locate_log: StaLocateLogEnum | None = Field(default="notification", description="Lowest severity level to log station locate message.")    
    wids_log: WidsLogEnum | None = Field(default="notification", description="Lowest severity level to log WIDS message.")    
    wtp_event_log: WtpEventLogEnum | None = Field(default="notification", description="Lowest severity level to log WTP event message.")    
    wtp_fips_event_log: WtpFipsEventLogEnum | None = Field(default="notification", description="Lowest severity level to log FAP fips event message.")    
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
    "LogModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.486355Z
# ============================================================================
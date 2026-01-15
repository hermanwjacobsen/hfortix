"""
Pydantic Models for CMDB - alertemail/setting

Runtime validation models for alertemail/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingSeverityEnum(str, Enum):
    """Allowed values for severity field."""
    EMERGENCY = "emergency"    ALERT = "alert"    CRITICAL = "critical"    ERROR = "error"    WARNING = "warning"    NOTIFICATION = "notification"    INFORMATION = "information"    DEBUG = "debug"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for alertemail/setting configuration.
    
    Configure alert email settings.
    
    Validation Rules:        - username: max_length=63 pattern=        - mailto1: max_length=63 pattern=        - mailto2: max_length=63 pattern=        - mailto3: max_length=63 pattern=        - filter_mode: pattern=        - email_interval: min=1 max=99999 pattern=        - IPS_logs: pattern=        - firewall_authentication_failure_logs: pattern=        - HA_logs: pattern=        - IPsec_errors_logs: pattern=        - FDS_update_logs: pattern=        - PPP_errors_logs: pattern=        - sslvpn_authentication_errors_logs: pattern=        - antivirus_logs: pattern=        - webfilter_logs: pattern=        - configuration_changes_logs: pattern=        - violation_traffic_logs: pattern=        - admin_login_logs: pattern=        - FDS_license_expiring_warning: pattern=        - log_disk_usage_warning: pattern=        - fortiguard_log_quota_warning: pattern=        - amc_interface_bypass_mode: pattern=        - FIPS_CC_errors: pattern=        - FSSO_disconnect_logs: pattern=        - ssh_logs: pattern=        - local_disk_usage: min=1 max=99 pattern=        - emergency_interval: min=1 max=99999 pattern=        - alert_interval: min=1 max=99999 pattern=        - critical_interval: min=1 max=99999 pattern=        - error_interval: min=1 max=99999 pattern=        - warning_interval: min=1 max=99999 pattern=        - notification_interval: min=1 max=99999 pattern=        - information_interval: min=1 max=99999 pattern=        - debug_interval: min=1 max=99999 pattern=        - severity: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    username: str | None = Field(max_length=63, default="", description="Name that appears in the From: field of alert emails (max. 63 characters).")    
    mailto1: str | None = Field(max_length=63, default="", description="Email address to send alert email to (usually a system administrator) (max. 63 characters).")    
    mailto2: str | None = Field(max_length=63, default="", description="Optional second email address to send alert email to (max. 63 characters).")    
    mailto3: str | None = Field(max_length=63, default="", description="Optional third email address to send alert email to (max. 63 characters).")    
    filter_mode: Literal["category", "threshold"] | None = Field(default="category", description="How to filter log messages that are sent to alert emails.")    
    email_interval: int | None = Field(ge=1, le=99999, default=5, description="Interval between sending alert emails (1 - 99999 min, default = 5).")    
    IPS_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPS logs in alert email.")    
    firewall_authentication_failure_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable firewall authentication failure logs in alert email.")    
    HA_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HA logs in alert email.")    
    IPsec_errors_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPsec error logs in alert email.")    
    FDS_update_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiGuard update logs in alert email.")    
    PPP_errors_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PPP error logs in alert email.")    
    sslvpn_authentication_errors_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Agentless VPN authentication error logs in alert email.")    
    antivirus_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable antivirus logs in alert email.")    
    webfilter_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web filter logs in alert email.")    
    configuration_changes_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable configuration change logs in alert email.")    
    violation_traffic_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable violation traffic logs in alert email.")    
    admin_login_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable administrator login/logout logs in alert email.")    
    FDS_license_expiring_warning: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiGuard license expiration warnings in alert email.")    
    log_disk_usage_warning: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable disk usage warnings in alert email.")    
    fortiguard_log_quota_warning: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiCloud log quota warnings in alert email.")    
    amc_interface_bypass_mode: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Fortinet Advanced Mezzanine Card (AMC) interface bypass mode logs in alert email.")    
    FIPS_CC_errors: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FIPS and Common Criteria error logs in alert email.")    
    FSSO_disconnect_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging of FSSO collector agent disconnect.")    
    ssh_logs: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SSH logs in alert email.")    
    local_disk_usage: int | None = Field(ge=1, le=99, default=75, description="Disk usage percentage at which to send alert email (1 - 99 percent, default = 75).")    
    emergency_interval: int | None = Field(ge=1, le=99999, default=1, description="Emergency alert interval in minutes.")    
    alert_interval: int | None = Field(ge=1, le=99999, default=2, description="Alert alert interval in minutes.")    
    critical_interval: int | None = Field(ge=1, le=99999, default=3, description="Critical alert interval in minutes.")    
    error_interval: int | None = Field(ge=1, le=99999, default=5, description="Error alert interval in minutes.")    
    warning_interval: int | None = Field(ge=1, le=99999, default=10, description="Warning alert interval in minutes.")    
    notification_interval: int | None = Field(ge=1, le=99999, default=20, description="Notification alert interval in minutes.")    
    information_interval: int | None = Field(ge=1, le=99999, default=30, description="Information alert interval in minutes.")    
    debug_interval: int | None = Field(ge=1, le=99999, default=60, description="Debug alert interval in minutes.")    
    severity: SeverityEnum | None = Field(default="alert", description="Lowest severity level to log.")    
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
    "SettingModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.590148Z
# ============================================================================
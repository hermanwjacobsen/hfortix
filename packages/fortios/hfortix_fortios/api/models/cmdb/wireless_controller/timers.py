"""
Pydantic Models for CMDB - wireless_controller/timers

Runtime validation models for wireless_controller/timers configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class TimersModel(BaseModel):
    """
    Pydantic model for wireless_controller/timers configuration.
    
    Configure CAPWAP timers.
    
    Validation Rules:        - echo_interval: min=1 max=255 pattern=        - nat_session_keep_alive: min=0 max=255 pattern=        - discovery_interval: min=2 max=180 pattern=        - client_idle_timeout: min=20 max=3600 pattern=        - client_idle_rehome_timeout: min=2 max=3600 pattern=        - auth_timeout: min=5 max=30 pattern=        - rogue_ap_log: min=0 max=1440 pattern=        - fake_ap_log: min=1 max=1440 pattern=        - sta_offline_cleanup: min=0 max=4294967295 pattern=        - sta_offline_ip2mac_cleanup: min=0 max=4294967295 pattern=        - sta_cap_cleanup: min=0 max=4294967295 pattern=        - rogue_ap_cleanup: min=0 max=4294967295 pattern=        - rogue_sta_cleanup: min=0 max=4294967295 pattern=        - wids_entry_cleanup: min=0 max=4294967295 pattern=        - ble_device_cleanup: min=0 max=4294967295 pattern=        - sta_stats_interval: min=1 max=255 pattern=        - vap_stats_interval: min=1 max=255 pattern=        - radio_stats_interval: min=1 max=255 pattern=        - sta_capability_interval: min=1 max=255 pattern=        - sta_locate_timer: min=0 max=86400 pattern=        - ipsec_intf_cleanup: min=30 max=3600 pattern=        - ble_scan_report_intv: min=10 max=3600 pattern=        - drma_interval: min=1 max=1440 pattern=        - ap_reboot_wait_interval1: min=5 max=65535 pattern=        - ap_reboot_wait_time: max_length=7 pattern=        - ap_reboot_wait_interval2: min=5 max=65535 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    echo_interval: int | None = Field(ge=1, le=255, default=30, description="Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec, default = 30).")    
    nat_session_keep_alive: int | None = Field(ge=0, le=255, default=0, description="Maximal time in seconds between control requests sent by the managed WTP, AP, or FortiAP (0 - 255 sec, default = 0).")    
    discovery_interval: int | None = Field(ge=2, le=180, default=5, description="Time between discovery requests (2 - 180 sec, default = 5).")    
    client_idle_timeout: int | None = Field(ge=20, le=3600, default=300, description="Time after which a client is considered idle and times out (20 - 3600 sec, default = 300, 0 for no timeout).")    
    client_idle_rehome_timeout: int | None = Field(ge=2, le=3600, default=20, description="Time after which a client is considered idle and disconnected from the home controller (2 - 3600 sec, default = 20, 0 for no timeout).")    
    auth_timeout: int | None = Field(ge=5, le=30, default=5, description="Time after which a client is considered failed in RADIUS authentication and times out (5 - 30 sec, default = 5).")    
    rogue_ap_log: int | None = Field(ge=0, le=1440, default=0, description="Time between logging rogue AP messages if periodic rogue AP logging is configured (0 - 1440 min, default = 0).")    
    fake_ap_log: int | None = Field(ge=1, le=1440, default=1, description="Time between recording logs about fake APs if periodic fake AP logging is configured (1 - 1440 min, default = 1).")    
    sta_offline_cleanup: int | None = Field(ge=0, le=4294967295, default=300, description="Time period in seconds to keep station offline data after it is gone (default = 300).")    
    sta_offline_ip2mac_cleanup: int | None = Field(ge=0, le=4294967295, default=300, description="Time period in seconds to keep station offline Ip2mac data after it is gone (default = 300).")    
    sta_cap_cleanup: int | None = Field(ge=0, le=4294967295, default=0, description="Time period in minutes to keep station capability data after it is gone (default = 0).")    
    rogue_ap_cleanup: int | None = Field(ge=0, le=4294967295, default=0, description="Time period in minutes to keep rogue AP after it is gone (default = 0).")    
    rogue_sta_cleanup: int | None = Field(ge=0, le=4294967295, default=0, description="Time period in minutes to keep rogue station after it is gone (default = 0).")    
    wids_entry_cleanup: int | None = Field(ge=0, le=4294967295, default=0, description="Time period in minutes to keep wids entry after it is gone (default = 0).")    
    ble_device_cleanup: int | None = Field(ge=0, le=4294967295, default=60, description="Time period in minutes to keep BLE device after it is gone (default = 60).")    
    sta_stats_interval: int | None = Field(ge=1, le=255, default=10, description="Time between running client (station) reports (1 - 255 sec, default = 10).")    
    vap_stats_interval: int | None = Field(ge=1, le=255, default=15, description="Time between running Virtual Access Point (VAP) reports (1 - 255 sec, default = 15).")    
    radio_stats_interval: int | None = Field(ge=1, le=255, default=15, description="Time between running radio reports (1 - 255 sec, default = 15).")    
    sta_capability_interval: int | None = Field(ge=1, le=255, default=30, description="Time between running station capability reports (1 - 255 sec, default = 30).")    
    sta_locate_timer: int | None = Field(ge=0, le=86400, default=1800, description="Time between running client presence flushes to remove clients that are listed but no longer present (0 - 86400 sec, default = 1800).")    
    ipsec_intf_cleanup: int | None = Field(ge=30, le=3600, default=120, description="Time period to keep IPsec VPN interfaces up after WTP sessions are disconnected (30 - 3600 sec, default = 120).")    
    ble_scan_report_intv: int | None = Field(ge=10, le=3600, default=30, description="Time between running Bluetooth Low Energy (BLE) reports (10 - 3600 sec, default = 30).")    
    drma_interval: int | None = Field(ge=1, le=1440, default=60, description="Dynamic radio mode assignment (DRMA) schedule interval in minutes (1 - 1440, default = 60).")    
    ap_reboot_wait_interval1: int | None = Field(ge=5, le=65535, default=0, description="Time in minutes to wait before AP reboots when there is no controller detected (5 - 65535, default = 0, 0 for no reboot).")    
    ap_reboot_wait_time: str | None = Field(max_length=7, default="", description="Time to reboot the AP when there is no controller detected and standalone SSIDs are pushed to the AP in the previous session, format hh:mm.")    
    ap_reboot_wait_interval2: int | None = Field(ge=5, le=65535, default=0, description="Time in minutes to wait before AP reboots when there is no controller detected and standalone SSIDs are pushed to the AP in the previous session (5 - 65535, default = 0, 0 for no reboot).")    
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
    "TimersModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.589401Z
# ============================================================================
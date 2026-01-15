"""
Pydantic Models for CMDB - wireless_controller/global_

Runtime validation models for wireless_controller/global_ configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class GlobalControl_message_offloadEnum(str, Enum):
    """Allowed values for control_message_offload field."""
    EBP_FRAME = "ebp-frame"    AEROSCOUT_TAG = "aeroscout-tag"    AP_LIST = "ap-list"    STA_LIST = "sta-list"    STA_CAP_LIST = "sta-cap-list"    STATS = "stats"    AEROSCOUT_MU = "aeroscout-mu"    STA_HEALTH = "sta-health"    SPECTRAL_ANALYSIS = "spectral-analysis"

# ============================================================================
# Main Model
# ============================================================================

class GlobalModel(BaseModel):
    """
    Pydantic model for wireless_controller/global_ configuration.
    
    Configure wireless controller global settings.
    
    Validation Rules:        - name: max_length=35 pattern=        - location: max_length=35 pattern=        - acd_process_count: min=0 max=255 pattern=        - wpad_process_count: min=0 max=255 pattern=        - image_download: pattern=        - rolling_wtp_upgrade: pattern=        - rolling_wtp_upgrade_threshold: max_length=7 pattern=        - max_retransmit: min=0 max=64 pattern=        - control_message_offload: pattern=        - data_ethernet_II: pattern=        - link_aggregation: pattern=        - mesh_eth_type: min=0 max=65535 pattern=        - fiapp_eth_type: min=0 max=65535 pattern=        - discovery_mc_addr: pattern=        - discovery_mc_addr6: pattern=        - max_clients: min=0 max=4294967295 pattern=        - rogue_scan_mac_adjacency: min=0 max=31 pattern=        - ipsec_base_ip: pattern=        - wtp_share: pattern=        - tunnel_mode: pattern=        - nac_interval: min=10 max=600 pattern=        - ap_log_server: pattern=        - ap_log_server_ip: pattern=        - ap_log_server_port: min=0 max=65535 pattern=        - max_sta_offline: min=0 max=4294967295 pattern=        - max_sta_offline_ip2mac: min=0 max=4294967295 pattern=        - max_sta_cap: min=0 max=4294967295 pattern=        - max_sta_cap_wtp: min=1 max=8 pattern=        - max_rogue_ap: min=0 max=4294967295 pattern=        - max_rogue_ap_wtp: min=1 max=16 pattern=        - max_rogue_sta: min=0 max=4294967295 pattern=        - max_wids_entry: min=0 max=4294967295 pattern=        - max_ble_device: min=0 max=4294967295 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Name of the wireless controller.")    
    location: str | None = Field(max_length=35, default="", description="Description of the location of the wireless controller.")    
    acd_process_count: int | None = Field(ge=0, le=255, default=0, description="Configure the number cw_acd daemons for multi-core CPU support (default = 0).")    
    wpad_process_count: int | None = Field(ge=0, le=255, default=0, description="Wpad daemon process count for multi-core CPU support.")    
    image_download: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable WTP image download at join time.")    
    rolling_wtp_upgrade: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable rolling WTP upgrade (default = disable).")    
    rolling_wtp_upgrade_threshold: str | None = Field(max_length=7, default="-80", description="Minimum signal level/threshold in dBm required for the managed WTP to be included in rolling WTP upgrade (-95 to -20, default = -80).")    
    max_retransmit: int | None = Field(ge=0, le=64, default=3, description="Maximum number of tunnel packet retransmissions (0 - 64, default = 3).")    
    control_message_offload: list[ControlMessageOffload] = Field(default="ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis", description="Configure CAPWAP control message data channel offload.")    
    data_ethernet_II: Literal["enable", "disable"] | None = Field(default="enable", description="Configure the wireless controller to use Ethernet II or 802.3 frames with 802.3 data tunnel mode (default = enable).")    
    link_aggregation: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable calculating the CAPWAP transmit hash to load balance sessions to link aggregation nodes (default = disable).")    
    mesh_eth_type: int | None = Field(ge=0, le=65535, default=8755, description="Mesh Ethernet identifier included in backhaul packets (0 - 65535, default = 8755).")    
    fiapp_eth_type: int | None = Field(ge=0, le=65535, default=5252, description="Ethernet type for Fortinet Inter-Access Point Protocol (IAPP), or IEEE 802.11f, packets (0 - 65535, default = 5252).")    
    discovery_mc_addr: Any = Field(default="224.0.1.140", description="Multicast IP address for AP discovery (default = 244.0.1.140).")    
    discovery_mc_addr6: str | None = Field(default="ff02::18c", description="Multicast IPv6 address for AP discovery (default = FF02::18C).")    
    max_clients: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of clients that can connect simultaneously (default = 0, meaning no limitation).")    
    rogue_scan_mac_adjacency: int | None = Field(ge=0, le=31, default=7, description="Maximum numerical difference between an AP's Ethernet and wireless MAC values to match for rogue detection (0 - 31, default = 7).")    
    ipsec_base_ip: str | None = Field(default="169.254.0.1", description="Base IP address for IPsec VPN tunnels between the access points and the wireless controller (default = 169.254.0.1).")    
    wtp_share: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sharing of WTPs between VDOMs.")    
    tunnel_mode: Literal["compatible", "strict"] | None = Field(default="compatible", description="Compatible/strict tunnel mode.")    
    nac_interval: int | None = Field(ge=10, le=600, default=120, description="Interval in seconds between two WiFi network access control (NAC) checks (10 - 600, default = 120).")    
    ap_log_server: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable configuring FortiGate to redirect wireless event log messages or FortiAPs to send UTM log messages to a syslog server (default = disable).")    
    ap_log_server_ip: str | None = Field(default="0.0.0.0", description="IP address that FortiGate or FortiAPs send log messages to.")    
    ap_log_server_port: int | None = Field(ge=0, le=65535, default=0, description="Port that FortiGate or FortiAPs send log messages to.")    
    max_sta_offline: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of station offline stored on the controller (default = 0).")    
    max_sta_offline_ip2mac: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of station offline ip2mac stored on the controller (default = 0).")    
    max_sta_cap: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of station cap stored on the controller (default = 0).")    
    max_sta_cap_wtp: int | None = Field(ge=1, le=8, default=8, description="Maximum number of station cap's wtp info stored on the controller (1 - 16, default = 8).")    
    max_rogue_ap: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of rogue APs stored on the controller (default = 0).")    
    max_rogue_ap_wtp: int | None = Field(ge=1, le=16, default=16, description="Maximum number of rogue AP's wtp info stored on the controller (1 - 16, default = 16).")    
    max_rogue_sta: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of rogue stations stored on the controller (default = 0).")    
    max_wids_entry: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of wids entries stored on the controller (default = 0).")    
    max_ble_device: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of BLE devices stored on the controller (default = 0).")    
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
    "GlobalModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.329026Z
# ============================================================================
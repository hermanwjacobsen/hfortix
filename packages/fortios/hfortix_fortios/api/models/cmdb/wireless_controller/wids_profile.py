"""
Pydantic Models for CMDB - wireless_controller/wids_profile

Runtime validation models for wireless_controller/wids_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class WidsProfileApScanChannelList2g5g(BaseModel):
    """
    Child table model for ap-scan-channel-list-2G-5G.
    
    Selected ap scan channel list for 2.4G and 5G bands.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    chan: str = Field(max_length=3, default="", description="Channel number.")
class WidsProfileApScanChannelList6g(BaseModel):
    """
    Child table model for ap-scan-channel-list-6G.
    
    Selected ap scan channel list for 6G band.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    chan: str = Field(max_length=3, default="", description="Channel 6g number.")
class WidsProfileApBgscanDisableSchedules(BaseModel):
    """
    Child table model for ap-bgscan-disable-schedules.
    
    Firewall schedules for turning off FortiAP radio background scan. Background scan will be disabled when at least one of the schedules is valid. Separate multiple schedule names with a space.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Schedule name.")  # datasource: ['firewall.schedule.group.name', 'firewall.schedule.recurring.name', 'firewall.schedule.onetime.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class WidsProfileModel(BaseModel):
    """
    Pydantic model for wireless_controller/wids_profile configuration.
    
    Configure wireless intrusion detection system (WIDS) profiles.
    
    Validation Rules:        - name: max_length=35 pattern=        - comment: max_length=63 pattern=        - sensor_mode: pattern=        - ap_scan: pattern=        - ap_scan_channel_list_2G_5G: pattern=        - ap_scan_channel_list_6G: pattern=        - ap_bgscan_period: min=10 max=3600 pattern=        - ap_bgscan_intv: min=1 max=600 pattern=        - ap_bgscan_duration: min=10 max=1000 pattern=        - ap_bgscan_idle: min=0 max=1000 pattern=        - ap_bgscan_report_intv: min=15 max=600 pattern=        - ap_bgscan_disable_schedules: pattern=        - ap_fgscan_report_intv: min=15 max=600 pattern=        - ap_scan_passive: pattern=        - ap_scan_threshold: max_length=7 pattern=        - ap_auto_suppress: pattern=        - wireless_bridge: pattern=        - deauth_broadcast: pattern=        - null_ssid_probe_resp: pattern=        - long_duration_attack: pattern=        - long_duration_thresh: min=1000 max=32767 pattern=        - invalid_mac_oui: pattern=        - weak_wep_iv: pattern=        - auth_frame_flood: pattern=        - auth_flood_time: min=5 max=120 pattern=        - auth_flood_thresh: min=1 max=100 pattern=        - assoc_frame_flood: pattern=        - assoc_flood_time: min=5 max=120 pattern=        - assoc_flood_thresh: min=1 max=100 pattern=        - reassoc_flood: pattern=        - reassoc_flood_time: min=1 max=120 pattern=        - reassoc_flood_thresh: min=1 max=65100 pattern=        - probe_flood: pattern=        - probe_flood_time: min=1 max=120 pattern=        - probe_flood_thresh: min=1 max=65100 pattern=        - bcn_flood: pattern=        - bcn_flood_time: min=1 max=120 pattern=        - bcn_flood_thresh: min=1 max=65100 pattern=        - rts_flood: pattern=        - rts_flood_time: min=1 max=120 pattern=        - rts_flood_thresh: min=1 max=65100 pattern=        - cts_flood: pattern=        - cts_flood_time: min=1 max=120 pattern=        - cts_flood_thresh: min=1 max=65100 pattern=        - client_flood: pattern=        - client_flood_time: min=1 max=120 pattern=        - client_flood_thresh: min=1 max=65100 pattern=        - block_ack_flood: pattern=        - block_ack_flood_time: min=1 max=120 pattern=        - block_ack_flood_thresh: min=1 max=65100 pattern=        - pspoll_flood: pattern=        - pspoll_flood_time: min=1 max=120 pattern=        - pspoll_flood_thresh: min=1 max=65100 pattern=        - netstumbler: pattern=        - netstumbler_time: min=1 max=120 pattern=        - netstumbler_thresh: min=1 max=65100 pattern=        - wellenreiter: pattern=        - wellenreiter_time: min=1 max=120 pattern=        - wellenreiter_thresh: min=1 max=65100 pattern=        - spoofed_deauth: pattern=        - asleap_attack: pattern=        - eapol_start_flood: pattern=        - eapol_start_thresh: min=2 max=100 pattern=        - eapol_start_intv: min=1 max=3600 pattern=        - eapol_logoff_flood: pattern=        - eapol_logoff_thresh: min=2 max=100 pattern=        - eapol_logoff_intv: min=1 max=3600 pattern=        - eapol_succ_flood: pattern=        - eapol_succ_thresh: min=2 max=100 pattern=        - eapol_succ_intv: min=1 max=3600 pattern=        - eapol_fail_flood: pattern=        - eapol_fail_thresh: min=2 max=100 pattern=        - eapol_fail_intv: min=1 max=3600 pattern=        - eapol_pre_succ_flood: pattern=        - eapol_pre_succ_thresh: min=2 max=100 pattern=        - eapol_pre_succ_intv: min=1 max=3600 pattern=        - eapol_pre_fail_flood: pattern=        - eapol_pre_fail_thresh: min=2 max=100 pattern=        - eapol_pre_fail_intv: min=1 max=3600 pattern=        - deauth_unknown_src_thresh: min=0 max=65535 pattern=        - windows_bridge: pattern=        - disassoc_broadcast: pattern=        - ap_spoofing: pattern=        - chan_based_mitm: pattern=        - adhoc_valid_ssid: pattern=        - adhoc_network: pattern=        - eapol_key_overflow: pattern=        - ap_impersonation: pattern=        - invalid_addr_combination: pattern=        - beacon_wrong_channel: pattern=        - ht_greenfield: pattern=        - overflow_ie: pattern=        - malformed_ht_ie: pattern=        - malformed_auth: pattern=        - malformed_association: pattern=        - ht_40mhz_intolerance: pattern=        - valid_ssid_misuse: pattern=        - valid_client_misassociation: pattern=        - hotspotter_attack: pattern=        - pwsave_dos_attack: pattern=        - omerta_attack: pattern=        - disconnect_station: pattern=        - unencrypted_valid: pattern=        - fata_jack: pattern=        - risky_encryption: pattern=        - fuzzed_beacon: pattern=        - fuzzed_probe_request: pattern=        - fuzzed_probe_response: pattern=        - air_jack: pattern=        - wpa_ft_attack: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="WIDS profile name.")    
    comment: str | None = Field(max_length=63, default="", description="Comment.")    
    sensor_mode: Literal["disable", "foreign", "both"] | None = Field(default="disable", description="Scan nearby WiFi stations (default = disable).")    
    ap_scan: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable rogue AP detection.")    
    ap_scan_channel_list_2G_5G: list[ApScanChannelList2G5G] = Field(default=None, description="Selected ap scan channel list for 2.4G and 5G bands.")    
    ap_scan_channel_list_6G: list[ApScanChannelList6G] = Field(default=None, description="Selected ap scan channel list for 6G band.")    
    ap_bgscan_period: int | None = Field(ge=10, le=3600, default=600, description="Period between background scans (10 - 3600 sec, default = 600).")    
    ap_bgscan_intv: int | None = Field(ge=1, le=600, default=3, description="Period between successive channel scans (1 - 600 sec, default = 3).")    
    ap_bgscan_duration: int | None = Field(ge=10, le=1000, default=30, description="Listen time on scanning a channel (10 - 1000 msec, default = 30).")    
    ap_bgscan_idle: int | None = Field(ge=0, le=1000, default=20, description="Wait time for channel inactivity before scanning this channel (0 - 1000 msec, default = 20).")    
    ap_bgscan_report_intv: int | None = Field(ge=15, le=600, default=30, description="Period between background scan reports (15 - 600 sec, default = 30).")    
    ap_bgscan_disable_schedules: list[ApBgscanDisableSchedules] = Field(default=None, description="Firewall schedules for turning off FortiAP radio background scan. Background scan will be disabled when at least one of the schedules is valid. Separate multiple schedule names with a space.")    
    ap_fgscan_report_intv: int | None = Field(ge=15, le=600, default=15, description="Period between foreground scan reports (15 - 600 sec, default = 15).")    
    ap_scan_passive: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable passive scanning. Enable means do not send probe request on any channels (default = disable).")    
    ap_scan_threshold: str | None = Field(max_length=7, default="-90", description="Minimum signal level/threshold in dBm required for the AP to report detected rogue AP (-95 to -20, default = -90).")    
    ap_auto_suppress: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable on-wire rogue AP auto-suppression (default = disable).")    
    wireless_bridge: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable wireless bridge detection (default = disable).")    
    deauth_broadcast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable broadcasting de-authentication detection (default = disable).")    
    null_ssid_probe_resp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable null SSID probe response detection (default = disable).")    
    long_duration_attack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable long duration attack detection based on user configured threshold (default = disable).")    
    long_duration_thresh: int | None = Field(ge=1000, le=32767, default=8200, description="Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200).")    
    invalid_mac_oui: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable invalid MAC OUI detection.")    
    weak_wep_iv: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable weak WEP IV (Initialization Vector) detection (default = disable).")    
    auth_frame_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication frame flooding detection (default = disable).")    
    auth_flood_time: int | None = Field(ge=5, le=120, default=10, description="Number of seconds after which a station is considered not connected.")    
    auth_flood_thresh: int | None = Field(ge=1, le=100, default=30, description="The threshold value for authentication frame flooding.")    
    assoc_frame_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable association frame flooding detection (default = disable).")    
    assoc_flood_time: int | None = Field(ge=5, le=120, default=10, description="Number of seconds after which a station is considered not connected.")    
    assoc_flood_thresh: int | None = Field(ge=1, le=100, default=30, description="The threshold value for association frame flooding.")    
    reassoc_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable reassociation flood detection (default = disable).")    
    reassoc_flood_time: int | None = Field(ge=1, le=120, default=10, description="Detection Window Period.")    
    reassoc_flood_thresh: int | None = Field(ge=1, le=65100, default=30, description="The threshold value for reassociation flood.")    
    probe_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable probe flood detection (default = disable).")    
    probe_flood_time: int | None = Field(ge=1, le=120, default=1, description="Detection Window Period.")    
    probe_flood_thresh: int | None = Field(ge=1, le=65100, default=30, description="The threshold value for probe flood.")    
    bcn_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable bcn flood detection (default = disable).")    
    bcn_flood_time: int | None = Field(ge=1, le=120, default=1, description="Detection Window Period.")    
    bcn_flood_thresh: int | None = Field(ge=1, le=65100, default=15, description="The threshold value for bcn flood.")    
    rts_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable rts flood detection (default = disable).")    
    rts_flood_time: int | None = Field(ge=1, le=120, default=10, description="Detection Window Period.")    
    rts_flood_thresh: int | None = Field(ge=1, le=65100, default=30, description="The threshold value for rts flood.")    
    cts_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable cts flood detection (default = disable).")    
    cts_flood_time: int | None = Field(ge=1, le=120, default=10, description="Detection Window Period.")    
    cts_flood_thresh: int | None = Field(ge=1, le=65100, default=30, description="The threshold value for cts flood.")    
    client_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable client flood detection (default = disable).")    
    client_flood_time: int | None = Field(ge=1, le=120, default=10, description="Detection Window Period.")    
    client_flood_thresh: int | None = Field(ge=1, le=65100, default=30, description="The threshold value for client flood.")    
    block_ack_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable block_ack flood detection (default = disable).")    
    block_ack_flood_time: int | None = Field(ge=1, le=120, default=1, description="Detection Window Period.")    
    block_ack_flood_thresh: int | None = Field(ge=1, le=65100, default=50, description="The threshold value for block_ack flood.")    
    pspoll_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable pspoll flood detection (default = disable).")    
    pspoll_flood_time: int | None = Field(ge=1, le=120, default=1, description="Detection Window Period.")    
    pspoll_flood_thresh: int | None = Field(ge=1, le=65100, default=30, description="The threshold value for pspoll flood.")    
    netstumbler: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable netstumbler detection (default = disable).")    
    netstumbler_time: int | None = Field(ge=1, le=120, default=30, description="Detection Window Period.")    
    netstumbler_thresh: int | None = Field(ge=1, le=65100, default=5, description="The threshold value for netstumbler.")    
    wellenreiter: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable wellenreiter detection (default = disable).")    
    wellenreiter_time: int | None = Field(ge=1, le=120, default=30, description="Detection Window Period.")    
    wellenreiter_thresh: int | None = Field(ge=1, le=65100, default=5, description="The threshold value for wellenreiter.")    
    spoofed_deauth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable spoofed de-authentication attack detection (default = disable).")    
    asleap_attack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable asleap attack detection (default = disable).")    
    eapol_start_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable EAPOL-Start flooding (to AP) detection (default = disable).")    
    eapol_start_thresh: int | None = Field(ge=2, le=100, default=10, description="The threshold value for EAPOL-Start flooding in specified interval.")    
    eapol_start_intv: int | None = Field(ge=1, le=3600, default=1, description="The detection interval for EAPOL-Start flooding (1 - 3600 sec).")    
    eapol_logoff_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable).")    
    eapol_logoff_thresh: int | None = Field(ge=2, le=100, default=10, description="The threshold value for EAPOL-Logoff flooding in specified interval.")    
    eapol_logoff_intv: int | None = Field(ge=1, le=3600, default=1, description="The detection interval for EAPOL-Logoff flooding (1 - 3600 sec).")    
    eapol_succ_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable EAPOL-Success flooding (to AP) detection (default = disable).")    
    eapol_succ_thresh: int | None = Field(ge=2, le=100, default=10, description="The threshold value for EAPOL-Success flooding in specified interval.")    
    eapol_succ_intv: int | None = Field(ge=1, le=3600, default=1, description="The detection interval for EAPOL-Success flooding (1 - 3600 sec).")    
    eapol_fail_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable).")    
    eapol_fail_thresh: int | None = Field(ge=2, le=100, default=10, description="The threshold value for EAPOL-Failure flooding in specified interval.")    
    eapol_fail_intv: int | None = Field(ge=1, le=3600, default=1, description="The detection interval for EAPOL-Failure flooding (1 - 3600 sec).")    
    eapol_pre_succ_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable).")    
    eapol_pre_succ_thresh: int | None = Field(ge=2, le=100, default=10, description="The threshold value for premature EAPOL-Success flooding in specified interval.")    
    eapol_pre_succ_intv: int | None = Field(ge=1, le=3600, default=1, description="The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).")    
    eapol_pre_fail_flood: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable).")    
    eapol_pre_fail_thresh: int | None = Field(ge=2, le=100, default=10, description="The threshold value for premature EAPOL-Failure flooding in specified interval.")    
    eapol_pre_fail_intv: int | None = Field(ge=1, le=3600, default=1, description="The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).")    
    deauth_unknown_src_thresh: int | None = Field(ge=0, le=65535, default=10, description="Threshold value per second to deauth unknown src for DoS attack (0: no limit).")    
    windows_bridge: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable windows bridge detection (default = disable).")    
    disassoc_broadcast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable broadcast dis-association detection (default = disable).")    
    ap_spoofing: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AP spoofing detection (default = disable).")    
    chan_based_mitm: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable channel based mitm detection (default = disable).")    
    adhoc_valid_ssid: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adhoc using valid SSID detection (default = disable).")    
    adhoc_network: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adhoc network detection (default = disable).")    
    eapol_key_overflow: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable overflow EAPOL key detection (default = disable).")    
    ap_impersonation: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AP impersonation detection (default = disable).")    
    invalid_addr_combination: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable invalid address combination detection (default = disable).")    
    beacon_wrong_channel: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable beacon wrong channel detection (default = disable).")    
    ht_greenfield: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HT greenfield detection (default = disable).")    
    overflow_ie: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable overflow IE detection (default = disable).")    
    malformed_ht_ie: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable malformed HT IE detection (default = disable).")    
    malformed_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable malformed auth frame detection (default = disable).")    
    malformed_association: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable malformed association request detection (default = disable).")    
    ht_40mhz_intolerance: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HT 40 MHz intolerance detection (default = disable).")    
    valid_ssid_misuse: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable valid SSID misuse detection (default = disable).")    
    valid_client_misassociation: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable valid client misassociation detection (default = disable).")    
    hotspotter_attack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable hotspotter attack detection (default = disable).")    
    pwsave_dos_attack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable power save DOS attack detection (default = disable).")    
    omerta_attack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable omerta attack detection (default = disable).")    
    disconnect_station: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable disconnect station detection (default = disable).")    
    unencrypted_valid: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable unencrypted valid detection (default = disable).")    
    fata_jack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FATA-Jack detection (default = disable).")    
    risky_encryption: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Risky Encryption detection (default = disable).")    
    fuzzed_beacon: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fuzzed beacon detection (default = disable).")    
    fuzzed_probe_request: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fuzzed probe request detection (default = disable).")    
    fuzzed_probe_response: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fuzzed probe response detection (default = disable).")    
    air_jack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AirJack detection (default = disable).")    
    wpa_ft_attack: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable WPA FT attack detection (default = disable).")    
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
    # ========================================================================
    # Datasource Validation Methods
    # ========================================================================    
    async def validate_ap_bgscan_disable_schedules_references(self, client: Any) -> list[str]:
        """
        Validate ap_bgscan_disable_schedules references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/schedule/group        - firewall/schedule/recurring        - firewall/schedule/onetime        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WidsProfileModel(
            ...     ap_bgscan_disable_schedules=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ap_bgscan_disable_schedules_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.wids_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ap_bgscan_disable_schedules", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.schedule.group.exists(value):
                found = True
            elif await client.api.cmdb.firewall.schedule.recurring.exists(value):
                found = True
            elif await client.api.cmdb.firewall.schedule.onetime.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ap-Bgscan-Disable-Schedules '{value}' not found in "
                    "firewall/schedule/group or firewall/schedule/recurring or firewall/schedule/onetime"
                )        
        return errors    
    async def validate_all_references(self, client: Any) -> list[str]:
        """
        Validate ALL datasource references in this model.
        
        Convenience method that runs all validate_*_references() methods
        and aggregates the results.
        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of all validation errors found
            
        Example:
            >>> errors = await policy.validate_all_references(fgt._client)
            >>> if errors:
            ...     for error in errors:
            ...         print(f"  - {error}")
        """
        all_errors = []
        
        errors = await self.validate_ap_bgscan_disable_schedules_references(client)
        all_errors.extend(errors)        
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "WidsProfileModel",    "WidsProfileApScanChannelList2g5g",    "WidsProfileApScanChannelList6g",    "WidsProfileApBgscanDisableSchedules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.440808Z
# ============================================================================
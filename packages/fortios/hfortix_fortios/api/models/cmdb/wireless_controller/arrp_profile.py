"""
Pydantic Models for CMDB - wireless_controller/arrp_profile

Runtime validation models for wireless_controller/arrp_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ArrpProfileDarrpOptimizeSchedules(BaseModel):
    """
    Child table model for darrp-optimize-schedules.
    
    Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space.
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

class ArrpProfileModel(BaseModel):
    """
    Pydantic model for wireless_controller/arrp_profile configuration.
    
    Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
    
    Validation Rules:        - name: max_length=35 pattern=        - comment: max_length=255 pattern=        - selection_period: min=0 max=65535 pattern=        - monitor_period: min=0 max=65535 pattern=        - weight_managed_ap: min=0 max=2000 pattern=        - weight_rogue_ap: min=0 max=2000 pattern=        - weight_noise_floor: min=0 max=2000 pattern=        - weight_channel_load: min=0 max=2000 pattern=        - weight_spectral_rssi: min=0 max=2000 pattern=        - weight_weather_channel: min=0 max=2000 pattern=        - weight_dfs_channel: min=0 max=2000 pattern=        - threshold_ap: min=0 max=500 pattern=        - threshold_noise_floor: max_length=7 pattern=        - threshold_channel_load: min=0 max=100 pattern=        - threshold_spectral_rssi: max_length=7 pattern=        - threshold_tx_retries: min=0 max=1000 pattern=        - threshold_rx_errors: min=0 max=100 pattern=        - include_weather_channel: pattern=        - include_dfs_channel: pattern=        - override_darrp_optimize: pattern=        - darrp_optimize: min=0 max=86400 pattern=        - darrp_optimize_schedules: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="WiFi ARRP profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    selection_period: int | None = Field(ge=0, le=65535, default=3600, description="Period in seconds to measure average channel load, noise floor, spectral RSSI (default = 3600).")    
    monitor_period: int | None = Field(ge=0, le=65535, default=300, description="Period in seconds to measure average transmit retries and receive errors (default = 300).")    
    weight_managed_ap: int | None = Field(ge=0, le=2000, default=50, description="Weight in DARRP channel score calculation for managed APs (0 - 2000, default = 50).")    
    weight_rogue_ap: int | None = Field(ge=0, le=2000, default=10, description="Weight in DARRP channel score calculation for rogue APs (0 - 2000, default = 10).")    
    weight_noise_floor: int | None = Field(ge=0, le=2000, default=40, description="Weight in DARRP channel score calculation for noise floor (0 - 2000, default = 40).")    
    weight_channel_load: int | None = Field(ge=0, le=2000, default=20, description="Weight in DARRP channel score calculation for channel load (0 - 2000, default = 20).")    
    weight_spectral_rssi: int | None = Field(ge=0, le=2000, default=40, description="Weight in DARRP channel score calculation for spectral RSSI (0 - 2000, default = 40).")    
    weight_weather_channel: int | None = Field(ge=0, le=2000, default=0, description="Weight in DARRP channel score calculation for weather channel (0 - 2000, default = 0).")    
    weight_dfs_channel: int | None = Field(ge=0, le=2000, default=0, description="Weight in DARRP channel score calculation for DFS channel (0 - 2000, default = 0).")    
    threshold_ap: int | None = Field(ge=0, le=500, default=250, description="Threshold to reject channel in DARRP channel selection phase 1 due to surrounding APs (0 - 500, default = 250).")    
    threshold_noise_floor: str | None = Field(max_length=7, default="-85", description="Threshold in dBm to reject channel in DARRP channel selection phase 1 due to noise floor (-95 to -20, default = -85).")    
    threshold_channel_load: int | None = Field(ge=0, le=100, default=60, description="Threshold in percentage to reject channel in DARRP channel selection phase 1 due to channel load (0 - 100, default = 60).")    
    threshold_spectral_rssi: str | None = Field(max_length=7, default="-65", description="Threshold in dBm to reject channel in DARRP channel selection phase 1 due to spectral RSSI (-95 to -20, default = -65).")    
    threshold_tx_retries: int | None = Field(ge=0, le=1000, default=300, description="Threshold in percentage for transmit retries to trigger channel reselection in DARRP monitor stage (0 - 1000, default = 300).")    
    threshold_rx_errors: int | None = Field(ge=0, le=100, default=50, description="Threshold in percentage for receive errors to trigger channel reselection in DARRP monitor stage (0 - 100, default = 50).")    
    include_weather_channel: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of weather channel in DARRP channel selection phase 1 (default = enable).")    
    include_dfs_channel: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of DFS channel in DARRP channel selection phase 1 (default = enable).")    
    override_darrp_optimize: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to override setting darrp-optimize and darrp-optimize-schedules (default = disable).")    
    darrp_optimize: int | None = Field(ge=0, le=86400, default=86400, description="Time for running Distributed Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default = 86400, 0 = disable).")    
    darrp_optimize_schedules: list[DarrpOptimizeSchedules] = Field(default=None, description="Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space.")    
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
    async def validate_darrp_optimize_schedules_references(self, client: Any) -> list[str]:
        """
        Validate darrp_optimize_schedules references exist in FortiGate.
        
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
            >>> policy = ArrpProfileModel(
            ...     darrp_optimize_schedules=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_darrp_optimize_schedules_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.arrp_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "darrp_optimize_schedules", [])
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
                    f"Darrp-Optimize-Schedules '{value}' not found in "
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
        
        errors = await self.validate_darrp_optimize_schedules_references(client)
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
    "ArrpProfileModel",    "ArrpProfileDarrpOptimizeSchedules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.605985Z
# ============================================================================
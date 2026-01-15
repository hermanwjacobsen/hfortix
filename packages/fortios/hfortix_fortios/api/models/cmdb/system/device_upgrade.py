"""
Pydantic Models for CMDB - system/device_upgrade

Runtime validation models for system/device_upgrade configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class DeviceUpgradeKnownHaMembers(BaseModel):
    """
    Child table model for known-ha-members.
    
    Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    serial: str = Field(max_length=79, default="", description="Serial number of HA member")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class DeviceUpgradeStatusEnum(str, Enum):
    """Allowed values for status field."""
    DISABLED = "disabled"    INITIALIZED = "initialized"    DOWNLOADING = "downloading"    DEVICE_DISCONNECTED = "device-disconnected"    READY = "ready"    COORDINATING = "coordinating"    STAGING = "staging"    FINAL_CHECK = "final-check"    UPGRADE_DEVICES = "upgrade-devices"    CANCELLED = "cancelled"    CONFIRMED = "confirmed"    DONE = "done"    FAILED = "failed"
class DeviceUpgradeDevice_typeEnum(str, Enum):
    """Allowed values for device_type field."""
    FORTIGATE = "fortigate"    FORTISWITCH = "fortiswitch"    FORTIAP = "fortiap"    FORTIEXTENDER = "fortiextender"
class DeviceUpgradeFailure_reasonEnum(str, Enum):
    """Allowed values for failure_reason field."""
    NONE = "none"    INTERNAL = "internal"    TIMEOUT = "timeout"    DEVICE_TYPE_UNSUPPORTED = "device-type-unsupported"    DOWNLOAD_FAILED = "download-failed"    DEVICE_MISSING = "device-missing"    VERSION_UNAVAILABLE = "version-unavailable"    STAGING_FAILED = "staging-failed"    REBOOT_FAILED = "reboot-failed"    DEVICE_NOT_RECONNECTED = "device-not-reconnected"    NODE_NOT_READY = "node-not-ready"    NO_FINAL_CONFIRMATION = "no-final-confirmation"    NO_CONFIRMATION_QUERY = "no-confirmation-query"    CONFIG_ERROR_LOG_NONEMPTY = "config-error-log-nonempty"    CSF_TREE_NOT_SUPPORTED = "csf-tree-not-supported"    FIRMWARE_CHANGED = "firmware-changed"    NODE_FAILED = "node-failed"    IMAGE_MISSING = "image-missing"

# ============================================================================
# Main Model
# ============================================================================

class DeviceUpgradeModel(BaseModel):
    """
    Pydantic model for system/device_upgrade configuration.
    
    Independent upgrades for managed devices.
    
    Validation Rules:        - vdom: max_length=31 pattern=        - status: pattern=        - ha_reboot_controller: max_length=79 pattern=        - next_path_index: min=0 max=10 pattern=        - known_ha_members: pattern=        - initial_version: pattern=        - starter_admin: max_length=64 pattern=        - serial: max_length=79 pattern=        - timing: pattern=        - maximum_minutes: min=5 max=10080 pattern=        - time: pattern=        - setup_time: pattern=        - upgrade_path: pattern=        - device_type: pattern=        - allow_download: pattern=        - failure_reason: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    vdom: str | None = Field(max_length=31, default="", description="Limit upgrade to this virtual domain (VDOM).")  # datasource: ['system.vdom.name']    
    status: StatusEnum = Field(default="disabled", description="Current status of the upgrade.")    
    ha_reboot_controller: str | None = Field(max_length=79, default="", description="Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.")    
    next_path_index: int = Field(ge=0, le=10, default=0, description="The index of the next image to upgrade to.")    
    known_ha_members: list[KnownHaMembers] = Field(description="Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.")    
    initial_version: str | None = Field(default="", description="Firmware version when the upgrade was set up.")    
    starter_admin: str | None = Field(max_length=64, default="", description="Admin that started the upgrade.")    
    serial: str = Field(max_length=79, default="", description="Serial number of the node to include.")    
    timing: Literal["immediate", "scheduled"] = Field(default="immediate", description="Run immediately or at a scheduled time.")    
    maximum_minutes: int = Field(ge=5, le=10080, default=15, description="Maximum number of minutes to allow for immediate upgrade preparation.")    
    time: str = Field(default="", description="Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).")    
    setup_time: str = Field(default="", description="Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).")    
    upgrade_path: str = Field(default="", description="Fortinet OS image versions to upgrade through in major-minor-patch format, such as 7-0-4.")    
    device_type: DeviceTypeEnum = Field(default="fortigate", description="Fortinet device type.")    
    allow_download: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable download firmware images.")    
    failure_reason: FailureReasonEnum | None = Field(default="none", description="Upgrade failure reason.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vdom')
    @classmethod
    def validate_vdom(cls, v: Any) -> Any:
        """
        Validate vdom field.
        
        Datasource: ['system.vdom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    async def validate_vdom_references(self, client: Any) -> list[str]:
        """
        Validate vdom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/vdom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DeviceUpgradeModel(
            ...     vdom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.device_upgrade.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vdom", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.vdom.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Vdom '{value}' not found in "
                "system/vdom"
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
        
        errors = await self.validate_vdom_references(client)
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
    "DeviceUpgradeModel",    "DeviceUpgradeKnownHaMembers",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.758492Z
# ============================================================================
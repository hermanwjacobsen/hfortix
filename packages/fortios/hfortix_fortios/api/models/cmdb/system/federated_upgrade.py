"""
Pydantic Models for CMDB - system/federated_upgrade

Runtime validation models for system/federated_upgrade configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class FederatedUpgradeKnownHaMembers(BaseModel):
    """
    Child table model for known-ha-members.
    
    Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    serial: str = Field(max_length=79, default="", description="Serial number of HA member")
class FederatedUpgradeNodeList(BaseModel):
    """
    Child table model for node-list.
    
    Nodes which will be included in the upgrade.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    serial: str = Field(max_length=79, default="", description="Serial number of the node to include.")    
    timing: Literal["immediate", "scheduled"] = Field(default="immediate", description="Run immediately or at a scheduled time.")    
    maximum_minutes: int = Field(ge=5, le=10080, default=15, description="Maximum number of minutes to allow for immediate upgrade preparation.")    
    time: str = Field(default="", description="Scheduled upgrade execution time in UTC (hh:mm yyyy/mm/dd UTC).")    
    setup_time: str = Field(default="", description="Upgrade preparation start time in UTC (hh:mm yyyy/mm/dd UTC).")    
    upgrade_path: str = Field(default="", description="Fortinet OS image versions to upgrade through in major-minor-patch format, such as 7-0-4.")    
    device_type: DeviceTypeEnum = Field(default="fortigate", description="Fortinet device type.")    
    allow_download: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable download firmware images.")    
    coordinating_fortigate: str | None = Field(max_length=79, default="", description="Serial number of the FortiGate unit that controls this device.")    
    failure_reason: FailureReasonEnum | None = Field(default="none", description="Upgrade failure reason.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class FederatedUpgradeStatusEnum(str, Enum):
    """Allowed values for status field."""
    DISABLED = "disabled"    INITIALIZED = "initialized"    DOWNLOADING = "downloading"    DEVICE_DISCONNECTED = "device-disconnected"    READY = "ready"    COORDINATING = "coordinating"    STAGING = "staging"    FINAL_CHECK = "final-check"    UPGRADE_DEVICES = "upgrade-devices"    CANCELLED = "cancelled"    CONFIRMED = "confirmed"    DONE = "done"    FAILED = "failed"
class FederatedUpgradeFailure_reasonEnum(str, Enum):
    """Allowed values for failure_reason field."""
    NONE = "none"    INTERNAL = "internal"    TIMEOUT = "timeout"    DEVICE_TYPE_UNSUPPORTED = "device-type-unsupported"    DOWNLOAD_FAILED = "download-failed"    DEVICE_MISSING = "device-missing"    VERSION_UNAVAILABLE = "version-unavailable"    STAGING_FAILED = "staging-failed"    REBOOT_FAILED = "reboot-failed"    DEVICE_NOT_RECONNECTED = "device-not-reconnected"    NODE_NOT_READY = "node-not-ready"    NO_FINAL_CONFIRMATION = "no-final-confirmation"    NO_CONFIRMATION_QUERY = "no-confirmation-query"    CONFIG_ERROR_LOG_NONEMPTY = "config-error-log-nonempty"    CSF_TREE_NOT_SUPPORTED = "csf-tree-not-supported"    FIRMWARE_CHANGED = "firmware-changed"    NODE_FAILED = "node-failed"    IMAGE_MISSING = "image-missing"

# ============================================================================
# Main Model
# ============================================================================

class FederatedUpgradeModel(BaseModel):
    """
    Pydantic model for system/federated_upgrade configuration.
    
    Coordinate federated upgrades within the Security Fabric.
    
    Validation Rules:        - status: pattern=        - source: pattern=        - failure_reason: pattern=        - failure_device: max_length=79 pattern=        - upgrade_id: min=0 max=4294967295 pattern=        - next_path_index: min=0 max=10 pattern=        - ignore_signing_errors: pattern=        - ha_reboot_controller: max_length=79 pattern=        - known_ha_members: pattern=        - initial_version: pattern=        - starter_admin: max_length=64 pattern=        - node_list: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: StatusEnum = Field(default="disabled", description="Current status of the upgrade.")    
    source: Literal["user", "auto-firmware-upgrade", "forced-upgrade"] | None = Field(default="user", description="Source that set up the federated upgrade config.")    
    failure_reason: FailureReasonEnum | None = Field(default="none", description="Reason for upgrade failure.")    
    failure_device: str | None = Field(max_length=79, default="", description="Serial number of the node to include.")    
    upgrade_id: int | None = Field(ge=0, le=4294967295, default=0, description="Unique identifier for this upgrade.")    
    next_path_index: int = Field(ge=0, le=10, default=0, description="The index of the next image to upgrade to.")    
    ignore_signing_errors: Literal["enable", "disable"] | None = Field(default="disable", description="Allow/reject use of FortiGate firmware images that are unsigned.")    
    ha_reboot_controller: str | None = Field(max_length=79, default="", description="Serial number of the FortiGate unit that will control the reboot process for the federated upgrade of the HA cluster.")    
    known_ha_members: list[KnownHaMembers] = Field(description="Known members of the HA cluster. If a member is missing at upgrade time, the upgrade will be cancelled.")    
    initial_version: str | None = Field(default="", description="Firmware version when the upgrade was set up.")    
    starter_admin: str | None = Field(max_length=64, default="", description="Admin that started the upgrade.")    
    node_list: list[NodeList] = Field(default=None, description="Nodes which will be included in the upgrade.")    
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
    "FederatedUpgradeModel",    "FederatedUpgradeKnownHaMembers",    "FederatedUpgradeNodeList",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.612618Z
# ============================================================================
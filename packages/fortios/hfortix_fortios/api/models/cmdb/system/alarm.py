"""
Pydantic Models for CMDB - system/alarm

Runtime validation models for system/alarm configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class AlarmGroups(BaseModel):
    """
    Child table model for groups.
    
    Alarm groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Group ID.")    
    period: int | None = Field(ge=0, le=4294967295, default=0, description="Time period in seconds (0 = from start up).")    
    admin_auth_failure_threshold: int | None = Field(ge=0, le=1024, default=0, description="Admin authentication failure threshold.")    
    admin_auth_lockout_threshold: int | None = Field(ge=0, le=1024, default=0, description="Admin authentication lockout threshold.")    
    user_auth_failure_threshold: int | None = Field(ge=0, le=1024, default=0, description="User authentication failure threshold.")    
    user_auth_lockout_threshold: int | None = Field(ge=0, le=1024, default=0, description="User authentication lockout threshold.")    
    replay_attempt_threshold: int | None = Field(ge=0, le=1024, default=0, description="Replay attempt threshold.")    
    self_test_failure_threshold: int | None = Field(ge=0, le=1, default=0, description="Self-test failure threshold.")    
    log_full_warning_threshold: int | None = Field(ge=0, le=1024, default=0, description="Log full warning threshold.")    
    encryption_failure_threshold: int | None = Field(ge=0, le=1024, default=0, description="Encryption failure threshold.")    
    decryption_failure_threshold: int | None = Field(ge=0, le=1024, default=0, description="Decryption failure threshold.")    
    fw_policy_violations: list[FwPolicyViolations] = Field(default=None, description="Firewall policy violations.")    
    fw_policy_id: int | None = Field(ge=0, le=4294967295, default=0, description="Firewall policy ID.")    
    fw_policy_id_threshold: int | None = Field(ge=0, le=1024, default=0, description="Firewall policy ID threshold.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AlarmModel(BaseModel):
    """
    Pydantic model for system/alarm configuration.
    
    Configure alarm.
    
    Validation Rules:        - status: pattern=        - audible: pattern=        - groups: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable alarm.")    
    audible: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable audible alarm.")    
    groups: list[Groups] = Field(default=None, description="Alarm groups.")    
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
    "AlarmModel",    "AlarmGroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.418210Z
# ============================================================================
"""
Pydantic Models for CMDB - diameter_filter/profile

Runtime validation models for diameter_filter/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProfileMissing_request_actionEnum(str, Enum):
    """Allowed values for missing_request_action field."""
    ALLOW = "allow"    BLOCK = "block"    RESET = "reset"    MONITOR = "monitor"
class ProfileProtocol_version_invalidEnum(str, Enum):
    """Allowed values for protocol_version_invalid field."""
    ALLOW = "allow"    BLOCK = "block"    RESET = "reset"    MONITOR = "monitor"
class ProfileMessage_length_invalidEnum(str, Enum):
    """Allowed values for message_length_invalid field."""
    ALLOW = "allow"    BLOCK = "block"    RESET = "reset"    MONITOR = "monitor"
class ProfileRequest_error_flag_setEnum(str, Enum):
    """Allowed values for request_error_flag_set field."""
    ALLOW = "allow"    BLOCK = "block"    RESET = "reset"    MONITOR = "monitor"
class ProfileCmd_flags_reserve_setEnum(str, Enum):
    """Allowed values for cmd_flags_reserve_set field."""
    ALLOW = "allow"    BLOCK = "block"    RESET = "reset"    MONITOR = "monitor"
class ProfileCommand_code_invalidEnum(str, Enum):
    """Allowed values for command_code_invalid field."""
    ALLOW = "allow"    BLOCK = "block"    RESET = "reset"    MONITOR = "monitor"

# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for diameter_filter/profile configuration.
    
    Configure Diameter filter profiles.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - monitor_all_messages: pattern=        - log_packet: pattern=        - track_requests_answers: pattern=        - missing_request_action: pattern=        - protocol_version_invalid: pattern=        - message_length_invalid: pattern=        - request_error_flag_set: pattern=        - cmd_flags_reserve_set: pattern=        - command_code_invalid: pattern=        - command_code_range: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    monitor_all_messages: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging for all User Name and Result Code AVP messages.")    
    log_packet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable packet log for triggered diameter settings.")    
    track_requests_answers: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable validation that each answer has a corresponding request.")    
    missing_request_action: MissingRequestActionEnum | None = Field(default="block", description="Action to be taken for answers without corresponding request.")    
    protocol_version_invalid: ProtocolVersionInvalidEnum | None = Field(default="block", description="Action to be taken for invalid protocol version.")    
    message_length_invalid: MessageLengthInvalidEnum | None = Field(default="block", description="Action to be taken for invalid message length.")    
    request_error_flag_set: RequestErrorFlagSetEnum | None = Field(default="block", description="Action to be taken for request messages with error flag set.")    
    cmd_flags_reserve_set: CmdFlagsReserveSetEnum | None = Field(default="block", description="Action to be taken for messages with cmd flag reserve bits set.")    
    command_code_invalid: CommandCodeInvalidEnum | None = Field(default="block", description="Action to be taken for messages with invalid command code.")    
    command_code_range: str | None = Field(default="", description="Valid range for command codes (0-16777215).")    
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
    "ProfileModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:18.292226Z
# ============================================================================
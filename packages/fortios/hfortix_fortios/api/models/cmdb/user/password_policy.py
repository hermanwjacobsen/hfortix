"""
Pydantic Models for CMDB - user/password_policy

Runtime validation models for user/password_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class PasswordPolicyModel(BaseModel):
    """
    Pydantic model for user/password_policy configuration.
    
    Configure user password policy.
    
    Validation Rules:        - name: max_length=35 pattern=        - expire_status: pattern=        - expire_days: min=0 max=999 pattern=        - warn_days: min=0 max=30 pattern=        - expired_password_renewal: pattern=        - minimum_length: min=8 max=128 pattern=        - min_lower_case_letter: min=0 max=128 pattern=        - min_upper_case_letter: min=0 max=128 pattern=        - min_non_alphanumeric: min=0 max=128 pattern=        - min_number: min=0 max=128 pattern=        - min_change_characters: min=0 max=128 pattern=        - reuse_password: pattern=        - reuse_password_limit: min=0 max=20 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Password policy name.")    
    expire_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable password expiration.")    
    expire_days: int | None = Field(ge=0, le=999, default=180, description="Time in days before the user's password expires.")    
    warn_days: int | None = Field(ge=0, le=30, default=15, description="Time in days before a password expiration warning message is displayed to the user upon login.")    
    expired_password_renewal: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable renewal of a password that already is expired.")    
    minimum_length: int | None = Field(ge=8, le=128, default=8, description="Minimum password length (8 - 128, default = 8).")    
    min_lower_case_letter: int | None = Field(ge=0, le=128, default=0, description="Minimum number of lowercase characters in password (0 - 128, default = 0).")    
    min_upper_case_letter: int | None = Field(ge=0, le=128, default=0, description="Minimum number of uppercase characters in password (0 - 128, default = 0).")    
    min_non_alphanumeric: int | None = Field(ge=0, le=128, default=0, description="Minimum number of non-alphanumeric characters in password (0 - 128, default = 0).")    
    min_number: int | None = Field(ge=0, le=128, default=0, description="Minimum number of numeric characters in password (0 - 128, default = 0).")    
    min_change_characters: int | None = Field(ge=0, le=128, default=0, description="Minimum number of unique characters in new password which do not exist in old password (0 - 128, default = 0. This attribute overrides reuse-password if both are enabled).")    
    reuse_password: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable reuse of password. If both reuse-password and min-change-characters are enabled, min-change-characters overrides.")    
    reuse_password_limit: int | None = Field(ge=0, le=20, default=0, description="Number of times passwords can be reused (0 - 20, default = 0. If set to 0, can reuse password an unlimited number of times.).")    
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
    "PasswordPolicyModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.790546Z
# ============================================================================
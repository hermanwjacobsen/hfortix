"""
Pydantic Models for CMDB - system/password_policy

Runtime validation models for system/password_policy configuration.
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
    Pydantic model for system/password_policy configuration.
    
    Configure password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.
    
    Validation Rules:        - status: pattern=        - apply_to: pattern=        - minimum_length: min=12 max=128 pattern=        - min_lower_case_letter: min=0 max=128 pattern=        - min_upper_case_letter: min=0 max=128 pattern=        - min_non_alphanumeric: min=0 max=128 pattern=        - min_number: min=0 max=128 pattern=        - expire_status: pattern=        - expire_day: min=1 max=999 pattern=        - reuse_password: pattern=        - reuse_password_limit: min=0 max=20 pattern=        - login_lockout_upon_weaker_encryption: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable setting a password policy for locally defined administrator passwords and IPsec VPN pre-shared keys.")    
    apply_to: list[ApplyTo] = Field(default="admin-password", description="Apply password policy to administrator passwords or IPsec pre-shared keys or both. Separate entries with a space.")    
    minimum_length: int | None = Field(ge=12, le=128, default=12, description="Minimum password length (12 - 128, default = 12).")    
    min_lower_case_letter: int | None = Field(ge=0, le=128, default=1, description="Minimum number of lowercase characters in password (0 - 128, default = 1).")    
    min_upper_case_letter: int | None = Field(ge=0, le=128, default=1, description="Minimum number of uppercase characters in password (0 - 128, default = 1).")    
    min_non_alphanumeric: int | None = Field(ge=0, le=128, default=1, description="Minimum number of non-alphanumeric characters in password (0 - 128, default = 1).")    
    min_number: int | None = Field(ge=0, le=128, default=1, description="Minimum number of numeric characters in password (0 - 128, default = 1).")    
    expire_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable password expiration.")    
    expire_day: int | None = Field(ge=1, le=999, default=90, description="Number of days after which passwords expire (1 - 999 days, default = 90).")    
    reuse_password: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable reuse of password.")    
    reuse_password_limit: int | None = Field(ge=0, le=20, default=0, description="Number of times passwords can be reused (0 - 20, default = 0. If set to 0, can reuse password an unlimited number of times.).")    
    login_lockout_upon_weaker_encryption: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable administrative user login lockout upon downgrade (defaut = disable). If enabled, changing the FortiOS firmware to a version where safer passwords are unsupported will lock out administrative users.")    
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
# Generated: 2026-01-15T22:00:17.313870Z
# ============================================================================
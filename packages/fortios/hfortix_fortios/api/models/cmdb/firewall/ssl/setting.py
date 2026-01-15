"""
Pydantic Models for CMDB - firewall/ssl/setting

Runtime validation models for firewall/ssl/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingSsl_dh_bitsEnum(str, Enum):
    """Allowed values for ssl_dh_bits field."""
    768 = "768"    1024 = "1024"    1536 = "1536"    2048 = "2048"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for firewall/ssl/setting configuration.
    
    SSL proxy settings.
    
    Validation Rules:        - proxy_connect_timeout: min=1 max=60 pattern=        - ssl_dh_bits: pattern=        - ssl_send_empty_frags: pattern=        - no_matching_cipher_action: pattern=        - cert_manager_cache_timeout: min=24 max=720 pattern=        - resigned_short_lived_certificate: pattern=        - cert_cache_capacity: min=0 max=500 pattern=        - cert_cache_timeout: min=1 max=120 pattern=        - session_cache_capacity: min=0 max=1000 pattern=        - session_cache_timeout: min=1 max=60 pattern=        - abbreviate_handshake: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    proxy_connect_timeout: int = Field(ge=1, le=60, default=30, description="Time limit to make an internal connection to the appropriate proxy process (1 - 60 sec, default = 30).")    
    ssl_dh_bits: SslDhBitsEnum = Field(default="2048", description="Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).")    
    ssl_send_empty_frags: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable sending empty fragments to avoid attack on CBC IV (for SSL 3.0 and TLS 1.0 only).")    
    no_matching_cipher_action: Literal["bypass", "drop"] = Field(default="bypass", description="Bypass or drop the connection when no matching cipher is found.")    
    cert_manager_cache_timeout: int = Field(ge=24, le=720, default=72, description="Time limit for certificate manager to keep FortiGate re-signed server certificate (24 - 720 hours, default = 72).")    
    resigned_short_lived_certificate: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable short-lived certificate.")    
    cert_cache_capacity: int = Field(ge=0, le=500, default=200, description="Maximum capacity of the host certificate cache (0 - 500, default = 200).")    
    cert_cache_timeout: int = Field(ge=1, le=120, default=10, description="Time limit to keep certificate cache (1 - 120 min, default = 10).")    
    session_cache_capacity: int = Field(ge=0, le=1000, default=500, description="Capacity of the SSL session cache (--Obsolete--) (1 - 1000, default = 500).")    
    session_cache_timeout: int = Field(ge=1, le=60, default=20, description="Time limit to keep SSL session state (1 - 60 min, default = 20).")    
    abbreviate_handshake: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of SSL abbreviated handshake.")    
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
    "SettingModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.173942Z
# ============================================================================
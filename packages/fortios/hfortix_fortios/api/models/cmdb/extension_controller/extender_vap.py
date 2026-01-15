"""
Pydantic Models for CMDB - extension_controller/extender_vap

Runtime validation models for extension_controller/extender_vap configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExtenderVapSecurityEnum(str, Enum):
    """Allowed values for security field."""
    OPEN = "OPEN"    WPA2_PERSONAL = "WPA2-Personal"    WPA_WPA2_PERSONAL = "WPA-WPA2-Personal"    WPA3_SAE = "WPA3-SAE"    WPA3_SAE_TRANSITION = "WPA3-SAE-Transition"    WPA2_ENTERPRISE = "WPA2-Enterprise"    WPA3_ENTERPRISE_ONLY = "WPA3-Enterprise-only"    WPA3_ENTERPRISE_TRANSITION = "WPA3-Enterprise-transition"    WPA3_ENTERPRISE_192_BIT = "WPA3-Enterprise-192-bit"
class ExtenderVapAllowaccessEnum(str, Enum):
    """Allowed values for allowaccess field."""
    PING = "ping"    TELNET = "telnet"    HTTP = "http"    HTTPS = "https"    SSH = "ssh"    SNMP = "snmp"

# ============================================================================
# Main Model
# ============================================================================

class ExtenderVapModel(BaseModel):
    """
    Pydantic model for extension_controller/extender_vap configuration.
    
    FortiExtender wifi vap configuration.
    
    Validation Rules:        - name: max_length=15 pattern=        - type: pattern=        - ssid: max_length=32 pattern=        - max_clients: min=0 max=512 pattern=        - broadcast_ssid: pattern=        - security: pattern=        - dtim: min=1 max=255 pattern=        - rts_threshold: min=256 max=2347 pattern=        - pmf: pattern=        - target_wake_time: pattern=        - bss_color_partial: pattern=        - mu_mimo: pattern=        - passphrase: max_length=59 pattern=        - sae_password: max_length=124 pattern=        - auth_server_address: max_length=63 pattern=        - auth_server_port: min=1 max=65535 pattern=        - auth_server_secret: max_length=63 pattern=        - ip_address: pattern=        - start_ip: pattern=        - end_ip: pattern=        - allowaccess: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="Wi-Fi VAP name.")    
    type: Literal["local-vap", "lan-ext-vap"] = Field(default="", description="Wi-Fi VAP type local-vap / lan-extension-vap.")    
    ssid: str = Field(max_length=32, default="", description="Wi-Fi SSID.")    
    max_clients: int | None = Field(ge=0, le=512, default=0, description="Wi-Fi max clients (0 - 512), default = 0 (no limit) ")    
    broadcast_ssid: Literal["disable", "enable"] | None = Field(default="enable", description="Wi-Fi broadcast SSID enable / disable.")    
    security: SecurityEnum = Field(default="WPA2-Personal", description="Wi-Fi security.")    
    dtim: int | None = Field(ge=1, le=255, default=1, description="Wi-Fi DTIM (1 - 255) default = 1.")    
    rts_threshold: int | None = Field(ge=256, le=2347, default=2347, description="Wi-Fi RTS Threshold (256 - 2347), default = 2347 (RTS/CTS disabled).")    
    pmf: Literal["disabled", "optional", "required"] | None = Field(default="disabled", description="Wi-Fi pmf enable/disable, default = disable.")    
    target_wake_time: Literal["disable", "enable"] | None = Field(default="enable", description="Wi-Fi 802.11AX target wake time enable / disable, default = enable.")    
    bss_color_partial: Literal["disable", "enable"] | None = Field(default="enable", description="Wi-Fi 802.11AX bss color partial enable / disable, default = enable.")    
    mu_mimo: Literal["disable", "enable"] | None = Field(default="enable", description="Wi-Fi multi-user MIMO enable / disable, default = enable.")    
    passphrase: Any = Field(max_length=59, description="Wi-Fi passphrase.")    
    sae_password: Any = Field(max_length=124, description="Wi-Fi SAE Password.")    
    auth_server_address: str = Field(max_length=63, default="", description="Wi-Fi Authentication Server Address (IPv4 format).")    
    auth_server_port: int = Field(ge=1, le=65535, default=0, description="Wi-Fi Authentication Server Port.")    
    auth_server_secret: str = Field(max_length=63, default="", description="Wi-Fi Authentication Server Secret.")    
    ip_address: Any = Field(default="0.0.0.0 0.0.0.0", description="Extender ip address.")    
    start_ip: str | None = Field(default="0.0.0.0", description="Start ip address.")    
    end_ip: str | None = Field(default="0.0.0.0", description="End ip address.")    
    allowaccess: list[Allowaccess] = Field(default="", description="Control management access to the managed extender. Separate entries with a space.")    
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
    "ExtenderVapModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.137853Z
# ============================================================================
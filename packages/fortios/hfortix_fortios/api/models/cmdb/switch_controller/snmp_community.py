"""
Pydantic Models for CMDB - switch_controller/snmp_community

Runtime validation models for switch_controller/snmp_community configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SnmpCommunityHosts(BaseModel):
    """
    Child table model for hosts.
    
    Configure IPv4 SNMP managers (hosts).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Host entry ID.")    
    ip: str = Field(default="", description="IPv4 address of the SNMP manager (host).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SnmpCommunityEventsEnum(str, Enum):
    """Allowed values for events field."""
    CPU_HIGH = "cpu-high"    MEM_LOW = "mem-low"    LOG_FULL = "log-full"    INTF_IP = "intf-ip"    ENT_CONF_CHANGE = "ent-conf-change"    L2MAC = "l2mac"

# ============================================================================
# Main Model
# ============================================================================

class SnmpCommunityModel(BaseModel):
    """
    Pydantic model for switch_controller/snmp_community configuration.
    
    Configure FortiSwitch SNMP v1/v2c communities globally.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - name: max_length=35 pattern=        - status: pattern=        - hosts: pattern=        - query_v1_status: pattern=        - query_v1_port: min=0 max=65535 pattern=        - query_v2c_status: pattern=        - query_v2c_port: min=0 max=65535 pattern=        - trap_v1_status: pattern=        - trap_v1_lport: min=0 max=65535 pattern=        - trap_v1_rport: min=0 max=65535 pattern=        - trap_v2c_status: pattern=        - trap_v2c_lport: min=0 max=65535 pattern=        - trap_v2c_rport: min=0 max=65535 pattern=        - events: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int = Field(ge=0, le=4294967295, default=0, description="SNMP community ID.")    
    name: str = Field(max_length=35, default="", description="SNMP community name.")    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable this SNMP community.")    
    hosts: list[Hosts] = Field(default=None, description="Configure IPv4 SNMP managers (hosts).")    
    query_v1_status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SNMP v1 queries.")    
    query_v1_port: int | None = Field(ge=0, le=65535, default=161, description="SNMP v1 query port (default = 161).")    
    query_v2c_status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SNMP v2c queries.")    
    query_v2c_port: int | None = Field(ge=0, le=65535, default=161, description="SNMP v2c query port (default = 161).")    
    trap_v1_status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SNMP v1 traps.")    
    trap_v1_lport: int | None = Field(ge=0, le=65535, default=162, description="SNMP v2c trap local port (default = 162).")    
    trap_v1_rport: int | None = Field(ge=0, le=65535, default=162, description="SNMP v2c trap remote port (default = 162).")    
    trap_v2c_status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SNMP v2c traps.")    
    trap_v2c_lport: int | None = Field(ge=0, le=65535, default=162, description="SNMP v2c trap local port (default = 162).")    
    trap_v2c_rport: int | None = Field(ge=0, le=65535, default=162, description="SNMP v2c trap remote port (default = 162).")    
    events: list[Events] = Field(default="cpu-high mem-low log-full intf-ip ent-conf-change l2mac", description="SNMP notifications (traps) to send.")    
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
    "SnmpCommunityModel",    "SnmpCommunityHosts",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.361473Z
# ============================================================================
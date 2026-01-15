"""
Pydantic Models for CMDB - wireless_controller/snmp

Runtime validation models for wireless_controller/snmp configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class SnmpCommunity(BaseModel):
    """
    Child table model for community.
    
    SNMP Community Configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Community ID.")    
    name: str = Field(max_length=35, default="", description="Community name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this SNMP community.")    
    query_v1_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SNMP v1 queries.")    
    query_v2c_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SNMP v2c queries.")    
    trap_v1_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SNMP v1 traps.")    
    trap_v2c_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SNMP v2c traps.")    
    hosts: list[Hosts] = Field(default=None, description="Configure IPv4 SNMP managers (hosts).")    
    hosts6: list[Hosts6] = Field(default=None, description="Configure IPv6 SNMP managers (hosts).")
class SnmpUser(BaseModel):
    """
    Child table model for user.
    
    SNMP User Configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=32, default="", description="SNMP user name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="SNMP user enable.")    
    queries: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SNMP queries for this user.")    
    trap_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable traps for this SNMP user.")    
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = Field(default="no-auth-no-priv", description="Security level for message authentication and encryption.")    
    auth_proto: AuthProtoEnum | None = Field(default="sha", description="Authentication protocol.")    
    auth_pwd: Any = Field(max_length=128, description="Password for authentication protocol.")    
    priv_proto: PrivProtoEnum | None = Field(default="aes", description="Privacy (encryption) protocol.")    
    priv_pwd: Any = Field(max_length=128, description="Password for privacy (encryption) protocol.")    
    notify_hosts: list[NotifyHosts] = Field(default="", description="Configure SNMP User Notify Hosts.")    
    notify_hosts6: list[NotifyHosts6] = Field(default="", description="Configure IPv6 SNMP User Notify Hosts.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SnmpModel(BaseModel):
    """
    Pydantic model for wireless_controller/snmp configuration.
    
    Configure SNMP.
    
    Validation Rules:        - engine_id: max_length=23 pattern=        - contact_info: max_length=31 pattern=        - trap_high_cpu_threshold: min=10 max=100 pattern=        - trap_high_mem_threshold: min=10 max=100 pattern=        - community: pattern=        - user: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    engine_id: str | None = Field(max_length=23, default="", description="AC SNMP engineID string (maximum 24 characters).")    
    contact_info: str | None = Field(max_length=31, default="", description="Contact Information.")    
    trap_high_cpu_threshold: int | None = Field(ge=10, le=100, default=80, description="CPU usage when trap is sent.")    
    trap_high_mem_threshold: int | None = Field(ge=10, le=100, default=80, description="Memory usage when trap is sent.")    
    community: list[Community] = Field(default=None, description="SNMP Community Configuration.")    
    user: list[User] = Field(default=None, description="SNMP User Configuration.")    
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
    "SnmpModel",    "SnmpCommunity",    "SnmpUser",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.165312Z
# ============================================================================
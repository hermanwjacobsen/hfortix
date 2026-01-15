"""
Pydantic Models for CMDB - system/resource_limits

Runtime validation models for system/resource_limits configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ResourceLimitsModel(BaseModel):
    """
    Pydantic model for system/resource_limits configuration.
    
    Configure resource limits.
    
    Validation Rules:        - session: min=0 max=4294967295 pattern=        - ipsec_phase1: min=0 max=4294967295 pattern=        - ipsec_phase2: min=0 max=4294967295 pattern=        - ipsec_phase1_interface: min=0 max=4294967295 pattern=        - ipsec_phase2_interface: min=0 max=4294967295 pattern=        - dialup_tunnel: min=0 max=4294967295 pattern=        - firewall_policy: min=0 max=4294967295 pattern=        - firewall_address: min=0 max=4294967295 pattern=        - firewall_addrgrp: min=0 max=4294967295 pattern=        - custom_service: min=0 max=4294967295 pattern=        - service_group: min=0 max=4294967295 pattern=        - onetime_schedule: min=0 max=4294967295 pattern=        - recurring_schedule: min=0 max=4294967295 pattern=        - user: min=0 max=4294967295 pattern=        - user_group: min=0 max=4294967295 pattern=        - sslvpn: min=0 max=4294967295 pattern=        - proxy: min=0 max=4294967295 pattern=        - log_disk_quota: min=0 max=4294967295 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    session: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of sessions.")    
    ipsec_phase1: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of VPN IPsec phase1 tunnels.")    
    ipsec_phase2: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of VPN IPsec phase2 tunnels.")    
    ipsec_phase1_interface: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of VPN IPsec phase1 interface tunnels.")    
    ipsec_phase2_interface: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of VPN IPsec phase2 interface tunnels.")    
    dialup_tunnel: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of dial-up tunnels.")    
    firewall_policy: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of firewall policies (policy, DoS-policy4, DoS-policy6, multicast).")    
    firewall_address: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of firewall addresses (IPv4, IPv6, multicast).")    
    firewall_addrgrp: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of firewall address groups (IPv4, IPv6).")    
    custom_service: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of firewall custom services.")    
    service_group: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of firewall service groups.")    
    onetime_schedule: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of firewall one-time schedules.")    
    recurring_schedule: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of firewall recurring schedules.")    
    user: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of local users.")    
    user_group: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of user groups.")    
    sslvpn: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of Agentless VPN.")    
    proxy: int | None = Field(ge=0, le=4294967295, default="", description="Maximum number of concurrent proxy users.")    
    log_disk_quota: int | None = Field(ge=0, le=4294967295, default=0, description="Log disk quota in megabytes (MB).")    
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
    "ResourceLimitsModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.670576Z
# ============================================================================
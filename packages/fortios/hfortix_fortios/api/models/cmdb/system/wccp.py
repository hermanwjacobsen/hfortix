"""
Pydantic Models for CMDB - system/wccp

Runtime validation models for system/wccp configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class WccpPrimary_hashEnum(str, Enum):
    """Allowed values for primary_hash field."""
    SRC_IP = "src-ip"    DST_IP = "dst-ip"    SRC_PORT = "src-port"    DST_PORT = "dst-port"

# ============================================================================
# Main Model
# ============================================================================

class WccpModel(BaseModel):
    """
    Pydantic model for system/wccp configuration.
    
    Configure WCCP.
    
    Validation Rules:        - service_id: max_length=3 pattern=        - router_id: pattern=        - cache_id: pattern=        - group_address: pattern=        - server_list: pattern=        - router_list: pattern=        - ports_defined: pattern=        - server_type: pattern=        - ports: pattern=        - authentication: pattern=        - password: max_length=128 pattern=        - forward_method: pattern=        - cache_engine_method: pattern=        - service_type: pattern=        - primary_hash: pattern=        - priority: min=0 max=255 pattern=        - protocol: min=0 max=255 pattern=        - assignment_weight: min=0 max=255 pattern=        - assignment_bucket_format: pattern=        - return_method: pattern=        - assignment_method: pattern=        - assignment_srcaddr_mask: pattern=        - assignment_dstaddr_mask: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    service_id: str | None = Field(max_length=3, default="", description="Service ID.")    
    router_id: str | None = Field(default="0.0.0.0", description="IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.")    
    cache_id: str | None = Field(default="0.0.0.0", description="IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.")    
    group_address: Any = Field(default="0.0.0.0", description="IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.")    
    server_list: list[ServerList] = Field(default="", description="IP addresses and netmasks for up to four cache servers.")    
    router_list: list[RouterList] = Field(default="", description="IP addresses of one or more WCCP routers.")    
    ports_defined: Literal["source", "destination"] | None = Field(default="", description="Match method.")    
    server_type: Literal["forward", "proxy"] | None = Field(default="forward", description="Cache server type.")    
    ports: list[Ports] = Field(default="", description="Service ports.")    
    authentication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable MD5 authentication.")    
    password: Any = Field(max_length=128, default=None, description="Password for MD5 authentication.")    
    forward_method: Literal["GRE", "L2", "any"] | None = Field(default="GRE", description="Method used to forward traffic to the cache servers.")    
    cache_engine_method: Literal["GRE", "L2"] | None = Field(default="GRE", description="Method used to forward traffic to the routers or to return to the cache engine.")    
    service_type: Literal["auto", "standard", "dynamic"] | None = Field(default="auto", description="WCCP service type used by the cache server for logical interception and redirection of traffic.")    
    primary_hash: list[PrimaryHash] = Field(default="dst-ip", description="Hash method.")    
    priority: int | None = Field(ge=0, le=255, default=0, description="Service priority.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Service protocol.")    
    assignment_weight: int | None = Field(ge=0, le=255, default=0, description="Assignment of hash weight/ratio for the WCCP cache engine.")    
    assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = Field(default="cisco-implementation", description="Assignment bucket format for the WCCP cache engine.")    
    return_method: Literal["GRE", "L2", "any"] | None = Field(default="GRE", description="Method used to decline a redirected packet and return it to the FortiGate unit.")    
    assignment_method: Literal["HASH", "MASK", "any"] | None = Field(default="HASH", description="Hash key assignment preference.")    
    assignment_srcaddr_mask: Any = Field(default="0.0.23.65", description="Assignment source address mask.")    
    assignment_dstaddr_mask: Any = Field(default="0.0.0.0", description="Assignment destination address mask.")    
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
    "WccpModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.962113Z
# ============================================================================
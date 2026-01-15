"""
Pydantic Models for CMDB - wireless_controller/inter_controller

Runtime validation models for wireless_controller/inter_controller configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class InterControllerInterControllerPeer(BaseModel):
    """
    Child table model for inter-controller-peer.
    
    Fast failover peer wireless controller list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    peer_ip: str | None = Field(default="0.0.0.0", description="Peer wireless controller's IP address.")    
    peer_port: int | None = Field(ge=1024, le=49150, default=5246, description="Port used by the wireless controller's for inter-controller communications (1024 - 49150, default = 5246).")    
    peer_priority: Literal["primary", "secondary"] | None = Field(default="primary", description="Peer wireless controller's priority (primary or secondary, default = primary).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class InterControllerModel(BaseModel):
    """
    Pydantic model for wireless_controller/inter_controller configuration.
    
    Configure inter wireless controller operation.
    
    Validation Rules:        - inter_controller_mode: pattern=        - l3_roaming: pattern=        - inter_controller_key: max_length=127 pattern=        - inter_controller_pri: pattern=        - fast_failover_max: min=3 max=64 pattern=        - fast_failover_wait: min=10 max=86400 pattern=        - inter_controller_peer: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    inter_controller_mode: Literal["disable", "l2-roaming", "1+1"] | None = Field(default="disable", description="Configure inter-controller mode (disable, l2-roaming, 1+1, default = disable).")    
    l3_roaming: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable layer 3 roaming (default = disable).")    
    inter_controller_key: Any = Field(max_length=127, default=None, description="Secret key for inter-controller communications.")    
    inter_controller_pri: Literal["primary", "secondary"] | None = Field(default="primary", description="Configure inter-controller's priority (primary or secondary, default = primary).")    
    fast_failover_max: int | None = Field(ge=3, le=64, default=10, description="Maximum number of retransmissions for fast failover HA messages between peer wireless controllers (3 - 64, default = 10).")    
    fast_failover_wait: int | None = Field(ge=10, le=86400, default=10, description="Minimum wait time before an AP transitions from secondary controller to primary controller (10 - 86400 sec, default = 10).")    
    inter_controller_peer: list[InterControllerPeer] = Field(default=None, description="Fast failover peer wireless controller list.")    
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
    "InterControllerModel",    "InterControllerInterControllerPeer",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.257642Z
# ============================================================================
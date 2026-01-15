"""
Pydantic Models for CMDB - firewall/shaper/per_ip_shaper

Runtime validation models for firewall/shaper/per_ip_shaper configuration.
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

class PerIpShaperModel(BaseModel):
    """
    Pydantic model for firewall/shaper/per_ip_shaper configuration.
    
    Configure per-IP traffic shaper.
    
    Validation Rules:        - name: max_length=35 pattern=        - max_bandwidth: min=0 max=80000000 pattern=        - bandwidth_unit: pattern=        - max_concurrent_session: min=0 max=2097000 pattern=        - max_concurrent_tcp_session: min=0 max=2097000 pattern=        - max_concurrent_udp_session: min=0 max=2097000 pattern=        - diffserv_forward: pattern=        - diffserv_reverse: pattern=        - diffservcode_forward: pattern=        - diffservcode_rev: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Traffic shaper name.")    
    max_bandwidth: int | None = Field(ge=0, le=80000000, default=0, description="Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting.")    
    bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = Field(default="kbps", description="Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps).")    
    max_concurrent_session: int | None = Field(ge=0, le=2097000, default=0, description="Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 means no limit.")    
    max_concurrent_tcp_session: int | None = Field(ge=0, le=2097000, default=0, description="Maximum number of concurrent TCP sessions allowed by this shaper (0 - 2097000). 0 means no limit.")    
    max_concurrent_udp_session: int | None = Field(ge=0, le=2097000, default=0, description="Maximum number of concurrent UDP sessions allowed by this shaper (0 - 2097000). 0 means no limit.")    
    diffserv_forward: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable changing the Forward (original) DiffServ setting applied to traffic accepted by this shaper.")    
    diffserv_reverse: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic accepted by this shaper.")    
    diffservcode_forward: str | None = Field(default="", description="Forward (original) DiffServ setting to be applied to traffic accepted by this shaper.")    
    diffservcode_rev: str | None = Field(default="", description="Reverse (reply) DiffServ setting to be applied to traffic accepted by this shaper.")    
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
    "PerIpShaperModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.641080Z
# ============================================================================
"""
Pydantic Models for CMDB - wireless_controller/hotspot20/h2qp_conn_capability

Runtime validation models for wireless_controller/hotspot20/h2qp_conn_capability configuration.
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

class H2qpConnCapabilityModel(BaseModel):
    """
    Pydantic model for wireless_controller/hotspot20/h2qp_conn_capability configuration.
    
    Configure connection capability.
    
    Validation Rules:        - name: max_length=35 pattern=        - icmp_port: pattern=        - ftp_port: pattern=        - ssh_port: pattern=        - http_port: pattern=        - tls_port: pattern=        - pptp_vpn_port: pattern=        - voip_tcp_port: pattern=        - voip_udp_port: pattern=        - ikev2_port: pattern=        - ikev2_xx_port: pattern=        - esp_port: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Connection capability name.")    
    icmp_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set ICMP port service status.")    
    ftp_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set FTP port service status.")    
    ssh_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set SSH port service status.")    
    http_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set HTTP port service status.")    
    tls_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set TLS VPN (HTTPS) port service status.")    
    pptp_vpn_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set Point to Point Tunneling Protocol (PPTP) VPN port service status.")    
    voip_tcp_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set VoIP TCP port service status.")    
    voip_udp_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set VoIP UDP port service status.")    
    ikev2_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set IKEv2 port service for IPsec VPN status.")    
    ikev2_xx_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status.")    
    esp_port: Literal["closed", "open", "unknown"] | None = Field(default="unknown", description="Set ESP port service (used by IPsec VPNs) status.")    
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
    "H2qpConnCapabilityModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.308336Z
# ============================================================================
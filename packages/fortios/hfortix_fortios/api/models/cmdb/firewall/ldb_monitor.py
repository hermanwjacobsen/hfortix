"""
Pydantic Models for CMDB - firewall/ldb_monitor

Runtime validation models for firewall/ldb_monitor configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LdbMonitorTypeEnum(str, Enum):
    """Allowed values for type field."""
    PING = "ping"    TCP = "tcp"    HTTP = "http"    HTTPS = "https"    DNS = "dns"

# ============================================================================
# Main Model
# ============================================================================

class LdbMonitorModel(BaseModel):
    """
    Pydantic model for firewall/ldb_monitor configuration.
    
    Configure server load balancing health monitors.
    
    Validation Rules:        - name: max_length=35 pattern=        - type: pattern=        - interval: min=5 max=65535 pattern=        - timeout: min=1 max=255 pattern=        - retry: min=1 max=255 pattern=        - port: min=0 max=65535 pattern=        - src_ip: pattern=        - http_get: max_length=255 pattern=        - http_match: max_length=255 pattern=        - http_max_redirects: min=0 max=5 pattern=        - dns_protocol: pattern=        - dns_request_domain: max_length=255 pattern=        - dns_match_ip: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Monitor name.")    
    type: TypeEnum = Field(default="", description="Select the Monitor type used by the health check monitor to check the health of the server (PING | TCP | HTTP | HTTPS | DNS).")    
    interval: int | None = Field(ge=5, le=65535, default=10, description="Time between health checks (5 - 65535 sec, default = 10).")    
    timeout: int | None = Field(ge=1, le=255, default=2, description="Time to wait to receive response to a health check from a server. Reaching the timeout means the health check failed (1 - 255 sec, default = 2).")    
    retry: int | None = Field(ge=1, le=255, default=3, description="Number health check attempts before the server is considered down (1 - 255, default = 3).")    
    port: int | None = Field(ge=0, le=65535, default=0, description="Service port used to perform the health check. If 0, health check monitor inherits port configured for the server (0 - 65535, default = 0).")    
    src_ip: str | None = Field(default="0.0.0.0", description="Source IP for ldb-monitor.")    
    http_get: str | None = Field(max_length=255, default="", description="Request URI used to send a GET request to check the health of an HTTP server. Optionally provide a hostname before the first '/' and it will be used as the HTTP Host Header.")    
    http_match: str | None = Field(max_length=255, default="", description="String to match the value expected in response to an HTTP-GET request.")    
    http_max_redirects: int | None = Field(ge=0, le=5, default=0, description="The maximum number of HTTP redirects to be allowed (0 - 5, default = 0).")    
    dns_protocol: Literal["udp", "tcp"] | None = Field(default="udp", description="Select the protocol used by the DNS health check monitor to check the health of the server (UDP | TCP).")    
    dns_request_domain: str | None = Field(max_length=255, default="", description="Fully qualified domain name to resolve for the DNS probe.")    
    dns_match_ip: str | None = Field(default="0.0.0.0", description="Response IP expected from DNS server.")    
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
    "LdbMonitorModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.534537Z
# ============================================================================
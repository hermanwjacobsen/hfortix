"""
Pydantic Models for CMDB - webfilter/fortiguard

Runtime validation models for webfilter/fortiguard configuration.
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

class FortiguardModel(BaseModel):
    """
    Pydantic model for webfilter/fortiguard configuration.
    
    Configure FortiGuard Web Filter service.
    
    Validation Rules:        - cache_mode: pattern=        - cache_prefix_match: pattern=        - cache_mem_permille: min=1 max=150 pattern=        - ovrd_auth_port_http: min=0 max=65535 pattern=        - ovrd_auth_port_https: min=0 max=65535 pattern=        - ovrd_auth_port_https_flow: min=0 max=65535 pattern=        - ovrd_auth_port_warning: min=0 max=65535 pattern=        - ovrd_auth_https: pattern=        - warn_auth_https: pattern=        - close_ports: pattern=        - request_packet_size_limit: min=576 max=10000 pattern=        - embed_image: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    cache_mode: Literal["ttl", "db-ver"] | None = Field(default="ttl", description="Cache entry expiration mode.")    
    cache_prefix_match: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable prefix matching in the cache.")    
    cache_mem_permille: int | None = Field(ge=1, le=150, default=1, description="Maximum permille of available memory allocated to caching (1 - 150).")    
    ovrd_auth_port_http: int | None = Field(ge=0, le=65535, default=8008, description="Port to use for FortiGuard Web Filter HTTP override authentication.")    
    ovrd_auth_port_https: int | None = Field(ge=0, le=65535, default=8010, description="Port to use for FortiGuard Web Filter HTTPS override authentication in proxy mode.")    
    ovrd_auth_port_https_flow: int | None = Field(ge=0, le=65535, default=8015, description="Port to use for FortiGuard Web Filter HTTPS override authentication in flow mode.")    
    ovrd_auth_port_warning: int | None = Field(ge=0, le=65535, default=8020, description="Port to use for FortiGuard Web Filter Warning override authentication.")    
    ovrd_auth_https: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of HTTPS for override authentication.")    
    warn_auth_https: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of HTTPS for warning and authentication.")    
    close_ports: Literal["enable", "disable"] | None = Field(default="disable", description="Close ports used for HTTP/HTTPS override authentication and disable user overrides.")    
    request_packet_size_limit: int | None = Field(ge=576, le=10000, default=0, description="Limit size of URL request packets sent to FortiGuard server (0 for default).")    
    embed_image: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable embedding images into replacement messages (default = enable).")    
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
    "FortiguardModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.186265Z
# ============================================================================
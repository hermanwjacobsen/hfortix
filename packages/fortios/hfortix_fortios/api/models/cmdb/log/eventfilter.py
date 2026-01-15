"""
Pydantic Models for CMDB - log/eventfilter

Runtime validation models for log/eventfilter configuration.
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

class EventfilterModel(BaseModel):
    """
    Pydantic model for log/eventfilter configuration.
    
    Configure log event filters.
    
    Validation Rules:        - event: pattern=        - system: pattern=        - vpn: pattern=        - user: pattern=        - router: pattern=        - wireless_activity: pattern=        - wan_opt: pattern=        - endpoint: pattern=        - ha: pattern=        - security_rating: pattern=        - fortiextender: pattern=        - connector: pattern=        - sdwan: pattern=        - cifs: pattern=        - switch_controller: pattern=        - rest_api: pattern=        - web_svc: pattern=        - webproxy: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    event: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable event logging.")    
    system: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable system event logging.")    
    vpn: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable VPN event logging.")    
    user: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable user authentication event logging.")    
    router: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable router event logging.")    
    wireless_activity: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable wireless event logging.")    
    wan_opt: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable WAN optimization event logging.")    
    endpoint: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable endpoint event logging.")    
    ha: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable ha event logging.")    
    security_rating: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Security Rating result logging.")    
    fortiextender: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiExtender logging.")    
    connector: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SDN connector logging.")    
    sdwan: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SD-WAN logging.")    
    cifs: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable CIFS logging.")    
    switch_controller: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Switch-Controller logging.")    
    rest_api: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable REST API logging.")    
    web_svc: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable web-svc performance logging.")    
    webproxy: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable web proxy event logging.")    
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
    "EventfilterModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:41.535290Z
# ============================================================================
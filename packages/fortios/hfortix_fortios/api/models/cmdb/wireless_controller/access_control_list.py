"""
Pydantic Models for CMDB - wireless_controller/access_control_list

Runtime validation models for wireless_controller/access_control_list configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class AccessControlListLayer3Ipv4Rules(BaseModel):
    """
    Child table model for layer3-ipv4-rules.
    
    AP ACL layer3 ipv4 rule list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    rule_id: int | None = Field(ge=1, le=65535, default=0, description="Rule ID (1 - 65535).")    
    comment: str | None = Field(max_length=63, default="", description="Description.")    
    srcaddr: str | None = Field(default="", description="Source IP address (any | local-LAN | IPv4 address[/<network mask | mask length>], default = any).")    
    srcport: int | None = Field(ge=0, le=65535, default=0, description="Source port (0 - 65535, default = 0, meaning any).")    
    dstaddr: str | None = Field(default="", description="Destination IP address (any | local-LAN | IPv4 address[/<network mask | mask length>], default = any).")    
    dstport: int | None = Field(ge=0, le=65535, default=0, description="Destination port (0 - 65535, default = 0, meaning any).")    
    protocol: int | None = Field(ge=0, le=255, default=255, description="Protocol type as defined by IANA (0 - 255, default = 255, meaning any).")    
    action: Literal["allow", "deny"] | None = Field(default="", description="Policy action (allow | deny).")
class AccessControlListLayer3Ipv6Rules(BaseModel):
    """
    Child table model for layer3-ipv6-rules.
    
    AP ACL layer3 ipv6 rule list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    rule_id: int | None = Field(ge=1, le=65535, default=0, description="Rule ID (1 - 65535).")    
    comment: str | None = Field(max_length=63, default="", description="Description.")    
    srcaddr: str | None = Field(default="", description="Source IPv6 address (any | local-LAN | IPv6 address[/prefix length]), default = any.")    
    srcport: int | None = Field(ge=0, le=65535, default=0, description="Source port (0 - 65535, default = 0, meaning any).")    
    dstaddr: str | None = Field(default="", description="Destination IPv6 address (any | local-LAN | IPv6 address[/prefix length]), default = any.")    
    dstport: int | None = Field(ge=0, le=65535, default=0, description="Destination port (0 - 65535, default = 0, meaning any).")    
    protocol: int | None = Field(ge=0, le=255, default=255, description="Protocol type as defined by IANA (0 - 255, default = 255, meaning any).")    
    action: Literal["allow", "deny"] | None = Field(default="", description="Policy action (allow | deny).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AccessControlListModel(BaseModel):
    """
    Pydantic model for wireless_controller/access_control_list configuration.
    
    Configure WiFi bridge access control list.
    
    Validation Rules:        - name: max_length=35 pattern=        - comment: max_length=63 pattern=        - layer3_ipv4_rules: pattern=        - layer3_ipv6_rules: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="AP access control list name.")    
    comment: str | None = Field(max_length=63, default="", description="Description.")    
    layer3_ipv4_rules: list[Layer3Ipv4Rules] = Field(default=None, description="AP ACL layer3 ipv4 rule list.")    
    layer3_ipv6_rules: list[Layer3Ipv6Rules] = Field(default=None, description="AP ACL layer3 ipv6 rule list.")    
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
    "AccessControlListModel",    "AccessControlListLayer3Ipv4Rules",    "AccessControlListLayer3Ipv6Rules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.753894Z
# ============================================================================
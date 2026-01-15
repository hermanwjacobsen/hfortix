"""
Pydantic Models for CMDB - vpn/l2tp

Runtime validation models for vpn/l2tp configuration.
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

class L2tpModel(BaseModel):
    """
    Pydantic model for vpn/l2tp configuration.
    
    Configure L2TP.
    
    Validation Rules:        - status: pattern=        - eip: pattern=        - sip: pattern=        - usrgrp: max_length=35 pattern=        - enforce_ipsec: pattern=        - lcp_echo_interval: min=0 max=32767 pattern=        - lcp_max_echo_fails: min=0 max=32767 pattern=        - hello_interval: min=0 max=3600 pattern=        - compress: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable FortiGate as a L2TP gateway.")    
    eip: str = Field(default="0.0.0.0", description="End IP.")    
    sip: str = Field(default="0.0.0.0", description="Start IP.")    
    usrgrp: str = Field(max_length=35, default="", description="User group.")  # datasource: ['user.group.name']    
    enforce_ipsec: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable IPsec enforcement.")    
    lcp_echo_interval: int | None = Field(ge=0, le=32767, default=5, description="Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.")    
    lcp_max_echo_fails: int | None = Field(ge=0, le=32767, default=3, description="Maximum number of missed LCP echo messages before disconnect.")    
    hello_interval: int | None = Field(ge=0, le=3600, default=60, description="L2TP hello message interval in seconds (0 - 3600 sec, default = 60).")    
    compress: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable data compression.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('usrgrp')
    @classmethod
    def validate_usrgrp(cls, v: Any) -> Any:
        """
        Validate usrgrp field.
        
        Datasource: ['user.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    # ========================================================================
    # Datasource Validation Methods
    # ========================================================================    
    async def validate_usrgrp_references(self, client: Any) -> list[str]:
        """
        Validate usrgrp references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = L2tpModel(
            ...     usrgrp="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_usrgrp_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.l2tp.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "usrgrp", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Usrgrp '{value}' not found in "
                "user/group"
            )        
        return errors    
    async def validate_all_references(self, client: Any) -> list[str]:
        """
        Validate ALL datasource references in this model.
        
        Convenience method that runs all validate_*_references() methods
        and aggregates the results.
        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of all validation errors found
            
        Example:
            >>> errors = await policy.validate_all_references(fgt._client)
            >>> if errors:
            ...     for error in errors:
            ...         print(f"  - {error}")
        """
        all_errors = []
        
        errors = await self.validate_usrgrp_references(client)
        all_errors.extend(errors)        
        return all_errors

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "L2tpModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.425045Z
# ============================================================================
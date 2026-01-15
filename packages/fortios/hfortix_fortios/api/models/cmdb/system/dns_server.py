"""
Pydantic Models for CMDB - system/dns_server

Runtime validation models for system/dns_server configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class DnsServerModeEnum(str, Enum):
    """Allowed values for mode field."""
    RECURSIVE = "recursive"    NON_RECURSIVE = "non-recursive"    FORWARD_ONLY = "forward-only"    RESOLVER = "resolver"

# ============================================================================
# Main Model
# ============================================================================

class DnsServerModel(BaseModel):
    """
    Pydantic model for system/dns_server configuration.
    
    Configure DNS servers.
    
    Validation Rules:        - name: max_length=15 pattern=        - mode: pattern=        - dnsfilter_profile: max_length=47 pattern=        - doh: pattern=        - doh3: pattern=        - doq: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="DNS server name.")  # datasource: ['system.interface.name']    
    mode: ModeEnum | None = Field(default="recursive", description="DNS server mode.")    
    dnsfilter_profile: str | None = Field(max_length=47, default="", description="DNS filter profile.")  # datasource: ['dnsfilter.profile.name']    
    doh: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DNS over HTTPS/443 (default = disable).")    
    doh3: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DNS over QUIC/HTTP3/443 (default = disable).")    
    doq: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DNS over QUIC/853 (default = disable).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: Any) -> Any:
        """
        Validate name field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dnsfilter_profile')
    @classmethod
    def validate_dnsfilter_profile(cls, v: Any) -> Any:
        """
        Validate dnsfilter_profile field.
        
        Datasource: ['dnsfilter.profile.name']
        
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
    async def validate_name_references(self, client: Any) -> list[str]:
        """
        Validate name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DnsServerModel(
            ...     name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dns_server.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Name '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_dnsfilter_profile_references(self, client: Any) -> list[str]:
        """
        Validate dnsfilter_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dnsfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DnsServerModel(
            ...     dnsfilter_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dnsfilter_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dns_server.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dnsfilter_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dnsfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dnsfilter-Profile '{value}' not found in "
                "dnsfilter/profile"
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
        
        errors = await self.validate_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dnsfilter_profile_references(client)
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
    "DnsServerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:58.091837Z
# ============================================================================
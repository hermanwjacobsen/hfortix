"""
Pydantic Models for CMDB - webfilter/urlfilter

Runtime validation models for webfilter/urlfilter configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class UrlfilterEntries(BaseModel):
    """
    Child table model for entries.
    
    URL filter entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Id.")    
    url: str | None = Field(max_length=511, default="", description="URL to be filtered.")    
    type: Literal["simple", "regex", "wildcard"] | None = Field(default="simple", description="Filter type (simple, regex, or wildcard).")    
    action: ActionEnum | None = Field(default="exempt", description="Action to take for URL filter matches.")    
    antiphish_action: Literal["block", "log"] | None = Field(default="block", description="Action to take for AntiPhishing matches.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this URL filter.")    
    exempt: list[Exempt] = Field(default="av web-content activex-java-cookie dlp fortiguard range-block antiphish all", description="If action is set to exempt, select the security profile operations that exempt URLs skip. Separate multiple options with a space.")    
    web_proxy_profile: str | None = Field(max_length=63, default="", description="Web proxy profile.")  # datasource: ['web-proxy.profile.name']    
    referrer_host: str | None = Field(max_length=255, default="", description="Referrer host name.")    
    dns_address_family: Literal["ipv4", "ipv6", "both"] | None = Field(default="ipv4", description="Resolve IPv4 address, IPv6 address, or both from DNS server.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class UrlfilterModel(BaseModel):
    """
    Pydantic model for webfilter/urlfilter configuration.
    
    Configure URL filter lists.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - name: max_length=63 pattern=        - comment: max_length=255 pattern=        - one_arm_ips_urlfilter: pattern=        - ip_addr_block: pattern=        - ip4_mapped_ip6: pattern=        - include_subdomains: pattern=        - entries: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    name: str = Field(max_length=63, default="", description="Name of URL filter list.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    one_arm_ips_urlfilter: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DNS resolver for one-arm IPS URL filter operation.")    
    ip_addr_block: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable blocking URLs when the hostname appears as an IP address.")    
    ip4_mapped_ip6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable matching of IPv4 mapped IPv6 URLs.")    
    include_subdomains: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable matching subdomains. Applies only to simple type (default = enable).")    
    entries: list[Entries] = Field(description="URL filter entries.")    
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
    # ========================================================================
    # Datasource Validation Methods
    # ========================================================================    
    async def validate_entries_references(self, client: Any) -> list[str]:
        """
        Validate entries references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - web-proxy/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = UrlfilterModel(
            ...     entries=[{"web-proxy-profile": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_entries_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.urlfilter.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "entries", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("web-proxy-profile")
            else:
                value = getattr(item, "web-proxy-profile", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.web-proxy.profile.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Entries '{value}' not found in "
                    "web-proxy/profile"
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
        
        errors = await self.validate_entries_references(client)
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
    "UrlfilterModel",    "UrlfilterEntries",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.551063Z
# ============================================================================
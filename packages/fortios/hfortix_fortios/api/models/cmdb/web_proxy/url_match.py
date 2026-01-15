"""
Pydantic Models for CMDB - web_proxy/url_match

Runtime validation models for web_proxy/url_match configuration.
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

class UrlMatchModel(BaseModel):
    """
    Pydantic model for web_proxy/url_match configuration.
    
    Exempt URLs from web proxy forwarding, caching and fast-fallback.
    
    Validation Rules:        - name: max_length=63 pattern=        - status: pattern=        - url_pattern: max_length=511 pattern=        - forward_server: max_length=63 pattern=        - fast_fallback: max_length=63 pattern=        - cache_exemption: pattern=        - comment: max_length=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Configure a name for the URL to be exempted.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable exempting the URLs matching the URL pattern from web proxy forwarding, caching and fast-fallback.")    
    url_pattern: str = Field(max_length=511, default="", description="URL pattern to be exempted from web proxy forwarding, caching and fast-fallback.")    
    forward_server: str | None = Field(max_length=63, default="", description="Forward server name.")  # datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']    
    fast_fallback: str | None = Field(max_length=63, default="", description="Fast fallback configuration entry name.")  # datasource: ['web-proxy.fast-fallback.name']    
    cache_exemption: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable exempting this URL pattern from caching.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('forward_server')
    @classmethod
    def validate_forward_server(cls, v: Any) -> Any:
        """
        Validate forward_server field.
        
        Datasource: ['web-proxy.forward-server.name', 'web-proxy.forward-server-group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fast_fallback')
    @classmethod
    def validate_fast_fallback(cls, v: Any) -> Any:
        """
        Validate fast_fallback field.
        
        Datasource: ['web-proxy.fast-fallback.name']
        
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
    async def validate_forward_server_references(self, client: Any) -> list[str]:
        """
        Validate forward_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - web-proxy/forward-server        - web-proxy/forward-server-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = UrlMatchModel(
            ...     forward_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_forward_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.web_proxy.url_match.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "forward_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.web-proxy.forward-server.exists(value):
            found = True
        elif await client.api.cmdb.web-proxy.forward-server-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Forward-Server '{value}' not found in "
                "web-proxy/forward-server or web-proxy/forward-server-group"
            )        
        return errors    
    async def validate_fast_fallback_references(self, client: Any) -> list[str]:
        """
        Validate fast_fallback references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - web-proxy/fast-fallback        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = UrlMatchModel(
            ...     fast_fallback="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fast_fallback_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.web_proxy.url_match.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fast_fallback", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.web-proxy.fast-fallback.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fast-Fallback '{value}' not found in "
                "web-proxy/fast-fallback"
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
        
        errors = await self.validate_forward_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fast_fallback_references(client)
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
    "UrlMatchModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.616037Z
# ============================================================================
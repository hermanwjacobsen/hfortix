"""
Pydantic Models for CMDB - firewall/auth_portal

Runtime validation models for firewall/auth_portal configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class AuthPortalGroups(BaseModel):
    """
    Child table model for groups.
    
    Firewall user groups permitted to authenticate through this portal. Separate group names with spaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AuthPortalModel(BaseModel):
    """
    Pydantic model for firewall/auth_portal configuration.
    
    Configure firewall authentication portals.
    
    Validation Rules:        - groups: pattern=        - portal_addr: max_length=63 pattern=        - portal_addr6: max_length=63 pattern=        - identity_based_route: max_length=35 pattern=        - proxy_auth: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    groups: list[Groups] = Field(default=None, description="Firewall user groups permitted to authenticate through this portal. Separate group names with spaces.")    
    portal_addr: str | None = Field(max_length=63, default="", description="Address (or FQDN) of the authentication portal.")    
    portal_addr6: str | None = Field(max_length=63, default="", description="IPv6 address (or FQDN) of authentication portal.")    
    identity_based_route: str | None = Field(max_length=35, default="", description="Name of the identity-based route that applies to this portal.")  # datasource: ['firewall.identity-based-route.name']    
    proxy_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication by proxy daemon (default = disable).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('identity_based_route')
    @classmethod
    def validate_identity_based_route(cls, v: Any) -> Any:
        """
        Validate identity_based_route field.
        
        Datasource: ['firewall.identity-based-route.name']
        
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
    async def validate_groups_references(self, client: Any) -> list[str]:
        """
        Validate groups references exist in FortiGate.
        
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
            >>> policy = AuthPortalModel(
            ...     groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.auth_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "groups", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Groups '{value}' not found in "
                    "user/group"
                )        
        return errors    
    async def validate_identity_based_route_references(self, client: Any) -> list[str]:
        """
        Validate identity_based_route references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/identity-based-route        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AuthPortalModel(
            ...     identity_based_route="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_identity_based_route_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.auth_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "identity_based_route", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.identity-based-route.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Identity-Based-Route '{value}' not found in "
                "firewall/identity-based-route"
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
        
        errors = await self.validate_groups_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_identity_based_route_references(client)
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
    "AuthPortalModel",    "AuthPortalGroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.437496Z
# ============================================================================
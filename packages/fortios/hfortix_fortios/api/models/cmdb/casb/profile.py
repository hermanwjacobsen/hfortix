"""
Pydantic Models for CMDB - casb/profile

Runtime validation models for casb/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileSaasApplication(BaseModel):
    """
    Child table model for saas-application.
    
    CASB profile SaaS application.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="CASB profile SaaS application name.")  # datasource: ['casb.saas-application.name']    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable setting.")    
    safe_search: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable safe search.")    
    safe_search_control: list[SafeSearchControl] = Field(description="CASB profile safe search control.")    
    tenant_control: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable tenant control.")    
    tenant_control_tenants: list[TenantControlTenants] = Field(description="CASB profile tenant control tenants.")    
    advanced_tenant_control: list[AdvancedTenantControl] = Field(default=None, description="CASB profile advanced tenant control.")    
    domain_control: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable domain control.")    
    domain_control_domains: list[DomainControlDomains] = Field(description="CASB profile domain control domains.")    
    log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable log settings.")    
    access_rule: list[AccessRule] = Field(default=None, description="CASB profile access rule.")    
    custom_control: list[CustomControl] = Field(default=None, description="CASB profile custom control.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for casb/profile configuration.
    
    Configure CASB profile.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - saas_application: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=47, default="", description="CASB profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    saas_application: list[SaasApplication] = Field(default=None, description="CASB profile SaaS application.")    
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
    async def validate_saas_application_references(self, client: Any) -> list[str]:
        """
        Validate saas_application references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - casb/saas-application        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     saas_application=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_saas_application_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.casb.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "saas_application", [])
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
            if await client.api.cmdb.casb.saas-application.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Saas-Application '{value}' not found in "
                    "casb/saas-application"
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
        
        errors = await self.validate_saas_application_references(client)
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
    "ProfileModel",    "ProfileSaasApplication",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.374014Z
# ============================================================================
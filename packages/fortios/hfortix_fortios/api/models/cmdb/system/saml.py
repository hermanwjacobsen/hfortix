"""
Pydantic Models for CMDB - system/saml

Runtime validation models for system/saml configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class SamlServiceProviders(BaseModel):
    """
    Child table model for service-providers.
    
    Authorized service providers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Name.")    
    prefix: str = Field(max_length=35, default="", description="Prefix.")    
    sp_binding_protocol: Literal["post", "redirect"] | None = Field(default="post", description="SP binding protocol.")    
    sp_cert: str | None = Field(max_length=35, default="", description="SP certificate name.")  # datasource: ['certificate.remote.name']    
    sp_entity_id: str = Field(max_length=255, default="", description="SP entity ID.")    
    sp_single_sign_on_url: str = Field(max_length=255, default="", description="SP single sign-on URL.")    
    sp_single_logout_url: str | None = Field(max_length=255, default="", description="SP single logout URL.")    
    sp_portal_url: str | None = Field(max_length=255, default="", description="SP portal URL.")    
    idp_entity_id: str | None = Field(max_length=255, default="", description="IDP entity ID.")    
    idp_single_sign_on_url: str | None = Field(max_length=255, default="", description="IDP single sign-on URL.")    
    idp_single_logout_url: str | None = Field(max_length=255, default="", description="IDP single logout URL.")    
    assertion_attributes: list[AssertionAttributes] = Field(default=None, description="Customized SAML attributes to send along with assertion.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SamlModel(BaseModel):
    """
    Pydantic model for system/saml configuration.
    
    Global settings for SAML authentication.
    
    Validation Rules:        - status: pattern=        - role: pattern=        - default_login_page: pattern=        - default_profile: max_length=35 pattern=        - cert: max_length=35 pattern=        - binding_protocol: pattern=        - portal_url: max_length=255 pattern=        - entity_id: max_length=255 pattern=        - single_sign_on_url: max_length=255 pattern=        - single_logout_url: max_length=255 pattern=        - idp_entity_id: max_length=255 pattern=        - idp_single_sign_on_url: max_length=255 pattern=        - idp_single_logout_url: max_length=255 pattern=        - idp_cert: max_length=35 pattern=        - server_address: max_length=63 pattern=        - require_signed_resp_and_asrt: pattern=        - tolerance: min=0 max=4294967295 pattern=        - life: min=0 max=4294967295 pattern=        - service_providers: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SAML authentication (default = disable).")    
    role: Literal["identity-provider", "service-provider"] | None = Field(default="service-provider", description="SAML role.")    
    default_login_page: Literal["normal", "sso"] = Field(default="normal", description="Choose default login page.")    
    default_profile: str = Field(max_length=35, default="", description="Default profile for new SSO admin.")  # datasource: ['system.accprofile.name']    
    cert: str | None = Field(max_length=35, default="", description="Certificate to sign SAML messages.")  # datasource: ['certificate.local.name']    
    binding_protocol: Literal["post", "redirect"] | None = Field(default="redirect", description="IdP Binding protocol.")    
    portal_url: str | None = Field(max_length=255, default="", description="SP portal URL.")    
    entity_id: str = Field(max_length=255, default="", description="SP entity ID.")    
    single_sign_on_url: str | None = Field(max_length=255, default="", description="SP single sign-on URL.")    
    single_logout_url: str | None = Field(max_length=255, default="", description="SP single logout URL.")    
    idp_entity_id: str | None = Field(max_length=255, default="", description="IDP entity ID.")    
    idp_single_sign_on_url: str | None = Field(max_length=255, default="", description="IDP single sign-on URL.")    
    idp_single_logout_url: str | None = Field(max_length=255, default="", description="IDP single logout URL.")    
    idp_cert: str = Field(max_length=35, default="", description="IDP certificate name.")  # datasource: ['certificate.remote.name']    
    server_address: str = Field(max_length=63, default="", description="Server address.")    
    require_signed_resp_and_asrt: Literal["enable", "disable"] | None = Field(default="disable", description="Require both response and assertion from IDP to be signed when FGT acts as SP (default = disable).")    
    tolerance: int | None = Field(ge=0, le=4294967295, default=5, description="Tolerance to the range of time when the assertion is valid (in minutes).")    
    life: int | None = Field(ge=0, le=4294967295, default=30, description="Length of the range of time when the assertion is valid (in minutes).")    
    service_providers: list[ServiceProviders] = Field(default=None, description="Authorized service providers.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('default_profile')
    @classmethod
    def validate_default_profile(cls, v: Any) -> Any:
        """
        Validate default_profile field.
        
        Datasource: ['system.accprofile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('cert')
    @classmethod
    def validate_cert(cls, v: Any) -> Any:
        """
        Validate cert field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('idp_cert')
    @classmethod
    def validate_idp_cert(cls, v: Any) -> Any:
        """
        Validate idp_cert field.
        
        Datasource: ['certificate.remote.name']
        
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
    async def validate_default_profile_references(self, client: Any) -> list[str]:
        """
        Validate default_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/accprofile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SamlModel(
            ...     default_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_default_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.saml.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "default_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.accprofile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Default-Profile '{value}' not found in "
                "system/accprofile"
            )        
        return errors    
    async def validate_cert_references(self, client: Any) -> list[str]:
        """
        Validate cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SamlModel(
            ...     cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.saml.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Cert '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_idp_cert_references(self, client: Any) -> list[str]:
        """
        Validate idp_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/remote        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SamlModel(
            ...     idp_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_idp_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.saml.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "idp_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.remote.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Idp-Cert '{value}' not found in "
                "certificate/remote"
            )        
        return errors    
    async def validate_service_providers_references(self, client: Any) -> list[str]:
        """
        Validate service_providers references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/remote        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SamlModel(
            ...     service_providers=[{"sp-cert": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_service_providers_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.saml.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "service_providers", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("sp-cert")
            else:
                value = getattr(item, "sp-cert", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.certificate.remote.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Service-Providers '{value}' not found in "
                    "certificate/remote"
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
        
        errors = await self.validate_default_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_idp_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_service_providers_references(client)
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
    "SamlModel",    "SamlServiceProviders",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.241575Z
# ============================================================================
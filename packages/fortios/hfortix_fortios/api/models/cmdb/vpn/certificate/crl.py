"""
Pydantic Models for CMDB - vpn/certificate/crl

Runtime validation models for vpn/certificate/crl configuration.
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

class CrlModel(BaseModel):
    """
    Pydantic model for vpn/certificate/crl configuration.
    
    Certificate Revocation List as a PEM file.
    
    Validation Rules:        - name: max_length=35 pattern=        - crl: pattern=        - range: pattern=        - source: pattern=        - update_vdom: max_length=31 pattern=        - ldap_server: max_length=35 pattern=        - ldap_username: max_length=63 pattern=        - ldap_password: max_length=128 pattern=        - http_url: max_length=255 pattern=        - scep_url: max_length=255 pattern=        - scep_cert: max_length=35 pattern=        - update_interval: min=0 max=4294967295 pattern=        - source_ip: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name.")    
    crl: str | None = Field(default="", description="Certificate Revocation List as a PEM file.")    
    range: Literal["global", "vdom"] | None = Field(default="vdom", description="Either global or VDOM IP address range for the certificate.")    
    source: Literal["factory", "user", "bundle"] | None = Field(default="user", description="Certificate source type.")    
    update_vdom: str | None = Field(max_length=31, default="root", description="VDOM for CRL update.")  # datasource: ['system.vdom.name']    
    ldap_server: str | None = Field(max_length=35, default="", description="LDAP server name for CRL auto-update.")    
    ldap_username: str | None = Field(max_length=63, default="", description="LDAP server user name.")    
    ldap_password: Any = Field(max_length=128, default=None, description="LDAP server user password.")    
    http_url: str | None = Field(max_length=255, default="", description="HTTP server URL for CRL auto-update.")    
    scep_url: str | None = Field(max_length=255, default="", description="SCEP server URL for CRL auto-update.")    
    scep_cert: str | None = Field(max_length=35, default="Fortinet_CA_SSL", description="Local certificate for SCEP communication for CRL auto-update.")  # datasource: ['vpn.certificate.local.name']    
    update_interval: int | None = Field(ge=0, le=4294967295, default=0, description="Time in seconds before the FortiGate checks for an updated CRL. Set to 0 to update only when it expires.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address for communications to a HTTP or SCEP CA server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('update_vdom')
    @classmethod
    def validate_update_vdom(cls, v: Any) -> Any:
        """
        Validate update_vdom field.
        
        Datasource: ['system.vdom.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('scep_cert')
    @classmethod
    def validate_scep_cert(cls, v: Any) -> Any:
        """
        Validate scep_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
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
    async def validate_update_vdom_references(self, client: Any) -> list[str]:
        """
        Validate update_vdom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/vdom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CrlModel(
            ...     update_vdom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_update_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.certificate.crl.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "update_vdom", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.vdom.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Update-Vdom '{value}' not found in "
                "system/vdom"
            )        
        return errors    
    async def validate_scep_cert_references(self, client: Any) -> list[str]:
        """
        Validate scep_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CrlModel(
            ...     scep_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_scep_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.certificate.crl.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "scep_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Scep-Cert '{value}' not found in "
                "vpn/certificate/local"
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
        
        errors = await self.validate_update_vdom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_scep_cert_references(client)
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
    "CrlModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.727905Z
# ============================================================================
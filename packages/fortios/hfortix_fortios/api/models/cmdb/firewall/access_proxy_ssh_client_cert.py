"""
Pydantic Models for CMDB - firewall/access_proxy_ssh_client_cert

Runtime validation models for firewall/access_proxy_ssh_client_cert configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class AccessProxySshClientCertCertExtension(BaseModel):
    """
    Child table model for cert-extension.
    
    Configure certificate extension for user certificate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=127, default="", description="Name of certificate extension.")    
    critical: Literal["no", "yes"] | None = Field(default="no", description="Critical option.")    
    type: Literal["fixed", "user"] | None = Field(default="fixed", description="Type of certificate extension.")    
    data: str | None = Field(max_length=127, default="", description="Data of certificate extension.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AccessProxySshClientCertModel(BaseModel):
    """
    Pydantic model for firewall/access_proxy_ssh_client_cert configuration.
    
    Configure Access Proxy SSH client certificate.
    
    Validation Rules:        - name: max_length=79 pattern=        - source_address: pattern=        - permit_x11_forwarding: pattern=        - permit_agent_forwarding: pattern=        - permit_port_forwarding: pattern=        - permit_pty: pattern=        - permit_user_rc: pattern=        - cert_extension: pattern=        - auth_ca: max_length=79 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="SSH client certificate name.")    
    source_address: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable appending source-address certificate critical option. This option ensure certificate only accepted from FortiGate source address.")    
    permit_x11_forwarding: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable appending permit-x11-forwarding certificate extension.")    
    permit_agent_forwarding: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable appending permit-agent-forwarding certificate extension.")    
    permit_port_forwarding: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable appending permit-port-forwarding certificate extension.")    
    permit_pty: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable appending permit-pty certificate extension.")    
    permit_user_rc: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable appending permit-user-rc certificate extension.")    
    cert_extension: list[CertExtension] = Field(default=None, description="Configure certificate extension for user certificate.")    
    auth_ca: str = Field(max_length=79, default="", description="Name of the SSH server public key authentication CA.")  # datasource: ['firewall.ssh.local-ca.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('auth_ca')
    @classmethod
    def validate_auth_ca(cls, v: Any) -> Any:
        """
        Validate auth_ca field.
        
        Datasource: ['firewall.ssh.local-ca.name']
        
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
    async def validate_auth_ca_references(self, client: Any) -> list[str]:
        """
        Validate auth_ca references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AccessProxySshClientCertModel(
            ...     auth_ca="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_ca_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.access_proxy_ssh_client_cert.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_ca", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Ca '{value}' not found in "
                "firewall/ssh/local-ca"
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
        
        errors = await self.validate_auth_ca_references(client)
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
    "AccessProxySshClientCertModel",    "AccessProxySshClientCertCertExtension",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.565436Z
# ============================================================================
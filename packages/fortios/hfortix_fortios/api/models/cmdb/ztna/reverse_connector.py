"""
Pydantic Models for CMDB - ztna/reverse_connector

Runtime validation models for ztna/reverse_connector configuration.
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

class ReverseConnectorModel(BaseModel):
    """
    Pydantic model for ztna/reverse_connector configuration.
    
    Configure ZTNA Reverse-Connector.
    
    Validation Rules:        - name: max_length=35 pattern=        - status: pattern=        - address: max_length=255 pattern=        - port: min=0 max=65535 pattern=        - health_check_interval: min=0 max=600 pattern=        - ssl_max_version: pattern=        - certificate: max_length=35 pattern=        - trusted_server_ca: max_length=79 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Reverse-Connector name")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Reverse-Connector status.")    
    address: str = Field(max_length=255, default="", description="Connector service edge adress(IP or FQDN).")    
    port: int | None = Field(ge=0, le=65535, default=0, description="Port number that traffic uses to connect to connector service edge(0 - 65535;).")    
    health_check_interval: int | None = Field(ge=0, le=600, default=60, description="Health check interval in seconds (0 - 600, default = 60, 0 = disable).")    
    ssl_max_version: Literal["tls-1.1", "tls-1.2", "tls-1.3"] | None = Field(default="tls-1.3", description="Highest TLS version acceptable from a server.")    
    certificate: str | None = Field(max_length=35, default="", description="The name of the certificate to use for SSL handshake.")  # datasource: ['vpn.certificate.local.name']    
    trusted_server_ca: str | None = Field(max_length=79, default="", description="Trusted Server CA certificate used by SSL connection.")  # datasource: ['vpn.certificate.ca.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('certificate')
    @classmethod
    def validate_certificate(cls, v: Any) -> Any:
        """
        Validate certificate field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('trusted_server_ca')
    @classmethod
    def validate_trusted_server_ca(cls, v: Any) -> Any:
        """
        Validate trusted_server_ca field.
        
        Datasource: ['vpn.certificate.ca.name']
        
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
    async def validate_certificate_references(self, client: Any) -> list[str]:
        """
        Validate certificate references exist in FortiGate.
        
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
            >>> policy = ReverseConnectorModel(
            ...     certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.reverse_connector.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Certificate '{value}' not found in "
                "vpn/certificate/local"
            )        
        return errors    
    async def validate_trusted_server_ca_references(self, client: Any) -> list[str]:
        """
        Validate trusted_server_ca references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ReverseConnectorModel(
            ...     trusted_server_ca="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_trusted_server_ca_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.reverse_connector.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "trusted_server_ca", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Trusted-Server-Ca '{value}' not found in "
                "vpn/certificate/ca"
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
        
        errors = await self.validate_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_trusted_server_ca_references(client)
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
    "ReverseConnectorModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.311987Z
# ============================================================================
"""
Pydantic Models for CMDB - vpn/certificate/ocsp_server

Runtime validation models for vpn/certificate/ocsp_server configuration.
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

class OcspServerModel(BaseModel):
    """
    Pydantic model for vpn/certificate/ocsp_server configuration.
    
    OCSP server configuration.
    
    Validation Rules:        - name: max_length=35 pattern=        - url: max_length=127 pattern=        - cert: max_length=127 pattern=        - secondary_url: max_length=127 pattern=        - secondary_cert: max_length=127 pattern=        - unavail_action: pattern=        - source_ip: max_length=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="OCSP server entry name.")    
    url: str | None = Field(max_length=127, default="", description="OCSP server URL.")    
    cert: str | None = Field(max_length=127, default="", description="OCSP server certificate.")  # datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']    
    secondary_url: str | None = Field(max_length=127, default="", description="Secondary OCSP server URL.")    
    secondary_cert: str | None = Field(max_length=127, default="", description="Secondary OCSP server certificate.")  # datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']    
    unavail_action: Literal["revoke", "ignore"] | None = Field(default="revoke", description="Action when server is unavailable (revoke the certificate or ignore the result of the check).")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for dynamic AIA and OCSP queries.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('cert')
    @classmethod
    def validate_cert(cls, v: Any) -> Any:
        """
        Validate cert field.
        
        Datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('secondary_cert')
    @classmethod
    def validate_secondary_cert(cls, v: Any) -> Any:
        """
        Validate secondary_cert field.
        
        Datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']
        
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
    async def validate_cert_references(self, client: Any) -> list[str]:
        """
        Validate cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/remote        - vpn/certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = OcspServerModel(
            ...     cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.certificate.ocsp_server.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.remote.exists(value):
            found = True
        elif await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Cert '{value}' not found in "
                "vpn/certificate/remote or vpn/certificate/ca"
            )        
        return errors    
    async def validate_secondary_cert_references(self, client: Any) -> list[str]:
        """
        Validate secondary_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/remote        - vpn/certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = OcspServerModel(
            ...     secondary_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_secondary_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.certificate.ocsp_server.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "secondary_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.remote.exists(value):
            found = True
        elif await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Secondary-Cert '{value}' not found in "
                "vpn/certificate/remote or vpn/certificate/ca"
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
        
        errors = await self.validate_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_secondary_cert_references(client)
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
    "OcspServerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.759498Z
# ============================================================================
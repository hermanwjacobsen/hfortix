"""
Pydantic Models for CMDB - icap/server

Runtime validation models for icap/server configuration.
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

class ServerModel(BaseModel):
    """
    Pydantic model for icap/server configuration.
    
    Configure ICAP servers.
    
    Validation Rules:        - name: max_length=63 pattern=        - addr_type: pattern=        - ip_address: pattern=        - ip6_address: pattern=        - fqdn: max_length=255 pattern=        - port: min=1 max=65535 pattern=        - max_connections: min=0 max=4294967295 pattern=        - secure: pattern=        - ssl_cert: max_length=79 pattern=        - healthcheck: pattern=        - healthcheck_service: max_length=127 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Server name.")    
    addr_type: Literal["ip4", "ip6", "fqdn"] | None = Field(default="ip4", description="Address type of the remote ICAP server: IPv4, IPv6 or FQDN.")    
    ip_address: str = Field(default="0.0.0.0", description="IPv4 address of the ICAP server.")    
    ip6_address: str = Field(default="::", description="IPv6 address of the ICAP server.")    
    fqdn: str | None = Field(max_length=255, default="", description="ICAP remote server Fully Qualified Domain Name (FQDN).")    
    port: int | None = Field(ge=1, le=65535, default=1344, description="ICAP server port.")    
    max_connections: int | None = Field(ge=0, le=4294967295, default=100, description="Maximum number of concurrent connections to ICAP server (unlimited = 0, default = 100). Must not be less than wad-worker-count.")    
    secure: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable secure connection to ICAP server.")    
    ssl_cert: str | None = Field(max_length=79, default="", description="CA certificate name.")  # datasource: ['certificate.ca.name']    
    healthcheck: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable ICAP remote server health checking. Attempts to connect to the remote ICAP server to verify that the server is operating normally.")    
    healthcheck_service: str = Field(max_length=127, default="", description="ICAP Service name to use for health checks.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ssl_cert')
    @classmethod
    def validate_ssl_cert(cls, v: Any) -> Any:
        """
        Validate ssl_cert field.
        
        Datasource: ['certificate.ca.name']
        
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
    async def validate_ssl_cert_references(self, client: Any) -> list[str]:
        """
        Validate ssl_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ServerModel(
            ...     ssl_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.icap.server.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssl_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssl-Cert '{value}' not found in "
                "certificate/ca"
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
        
        errors = await self.validate_ssl_cert_references(client)
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
    "ServerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.654144Z
# ============================================================================
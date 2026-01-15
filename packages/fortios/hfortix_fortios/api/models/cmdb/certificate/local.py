"""
Pydantic Models for CMDB - certificate/local

Runtime validation models for certificate/local configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class LocalDetails(BaseModel):
    """
    Child table model for details.
    
    Print local certificate detailed information.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    <certficate name>: Any = Field(default=None, description="Local certificate name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LocalEnroll_protocolEnum(str, Enum):
    """Allowed values for enroll_protocol field."""
    NONE = "none"    SCEP = "scep"    CMPV2 = "cmpv2"    ACME2 = "acme2"    EST = "est"

# ============================================================================
# Main Model
# ============================================================================

class LocalModel(BaseModel):
    """
    Pydantic model for certificate/local configuration.
    
    Local keys and certificates.
    
    Validation Rules:        - name: max_length=35 pattern=        - password: max_length=128 pattern=        - comments: max_length=511 pattern=        - private_key: pattern=        - certificate: pattern=        - csr: pattern=        - state: pattern=        - scep_url: max_length=255 pattern=        - range: pattern=        - source: pattern=        - auto_regenerate_days: min=0 max=4294967295 pattern=        - auto_regenerate_days_warning: min=0 max=4294967295 pattern=        - scep_password: max_length=128 pattern=        - ca_identifier: max_length=255 pattern=        - name_encoding: pattern=        - source_ip: pattern=        - ike_localid: max_length=63 pattern=        - ike_localid_type: pattern=        - enroll_protocol: pattern=        - private_key_retain: pattern=        - cmp_server: max_length=63 pattern=        - cmp_path: max_length=255 pattern=        - cmp_server_cert: max_length=79 pattern=        - cmp_regeneration_method: pattern=        - acme_ca_url: max_length=255 pattern=        - acme_domain: max_length=255 pattern=        - acme_email: max_length=255 pattern=        - acme_eab_key_id: max_length=255 pattern=        - acme_eab_key_hmac: max_length=128 pattern=        - acme_rsa_key_size: min=2048 max=4096 pattern=        - acme_renew_window: min=1 max=60 pattern=        - est_server: max_length=255 pattern=        - est_ca_id: max_length=255 pattern=        - est_http_username: max_length=63 pattern=        - est_http_password: max_length=128 pattern=        - est_client_cert: max_length=79 pattern=        - est_server_cert: max_length=79 pattern=        - est_srp_username: max_length=63 pattern=        - est_srp_password: max_length=128 pattern=        - est_regeneration_method: pattern=        - details: pattern=    """
    
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
    password: Any = Field(max_length=128, default=None, description="Password as a PEM file.")    
    comments: str | None = Field(max_length=511, default="", description="Comment.")    
    private_key: str = Field(default="", description="PEM format key encrypted with a password.")    
    certificate: str | None = Field(default="", description="PEM format certificate.")    
    csr: str | None = Field(default="", description="Certificate Signing Request.")    
    state: str | None = Field(default="", description="Certificate Signing Request State.")    
    scep_url: str | None = Field(max_length=255, default="", description="SCEP server URL.")    
    range: Literal["global", "vdom"] | None = Field(default="global", description="Either a global or VDOM IP address range for the certificate.")    
    source: Literal["factory", "user", "bundle"] | None = Field(default="user", description="Certificate source type.")    
    auto_regenerate_days: int | None = Field(ge=0, le=4294967295, default=0, description="Number of days to wait before expiry of an updated local certificate is requested (0 = disabled).")    
    auto_regenerate_days_warning: int | None = Field(ge=0, le=4294967295, default=0, description="Number of days to wait before an expiry warning message is generated (0 = disabled).")    
    scep_password: Any = Field(max_length=128, default=None, description="SCEP server challenge password for auto-regeneration.")    
    ca_identifier: str | None = Field(max_length=255, default="", description="CA identifier of the CA server for signing via SCEP.")    
    name_encoding: Literal["printable", "utf8"] | None = Field(default="printable", description="Name encoding method for auto-regeneration.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address for communications to the SCEP server.")    
    ike_localid: str | None = Field(max_length=63, default="", description="Local ID the FortiGate uses for authentication as a VPN client.")    
    ike_localid_type: Literal["asn1dn", "fqdn"] | None = Field(default="asn1dn", description="IKE local ID type.")    
    enroll_protocol: EnrollProtocolEnum | None = Field(default="none", description="Certificate enrollment protocol.")    
    private_key_retain: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable retention of private key during SCEP renewal (default = disable).")    
    cmp_server: str | None = Field(max_length=63, default="", description="Address and port for CMP server (format = address:port).")    
    cmp_path: str | None = Field(max_length=255, default="", description="Path location inside CMP server.")    
    cmp_server_cert: str | None = Field(max_length=79, default="", description="CMP server certificate.")  # datasource: ['certificate.ca.name', 'certificate.remote.name']    
    cmp_regeneration_method: Literal["keyupate", "renewal"] | None = Field(default="keyupate", description="CMP auto-regeneration method.")    
    acme_ca_url: str = Field(max_length=255, default="https://acme-v02.api.letsencrypt.org/directory", description="The URL for the ACME CA server (Let's Encrypt is the default provider).")    
    acme_domain: str = Field(max_length=255, default="", description="A valid domain that resolves to this FortiGate unit.")    
    acme_email: str = Field(max_length=255, default="", description="Contact email address that is required by some CAs like LetsEncrypt.")    
    acme_eab_key_id: str | None = Field(max_length=255, default=None, description="External Account Binding Key ID (optional setting).")    
    acme_eab_key_hmac: Any = Field(max_length=128, default=None, description="External Account Binding HMAC Key (URL-encoded base64).")    
    acme_rsa_key_size: int | None = Field(ge=2048, le=4096, default=2048, description="Length of the RSA private key of the generated cert (Minimum 2048 bits).")    
    acme_renew_window: int | None = Field(ge=1, le=60, default=30, description="Beginning of the renewal window (in days before certificate expiration, 30 by default).")    
    est_server: str | None = Field(max_length=255, default="", description="Address and port for EST server (e.g. https://example.com:1234).")    
    est_ca_id: str | None = Field(max_length=255, default="", description="CA identifier of the CA server for signing via EST.")    
    est_http_username: str | None = Field(max_length=63, default="", description="HTTP Authentication username for signing via EST.")    
    est_http_password: Any = Field(max_length=128, default=None, description="HTTP Authentication password for signing via EST.")    
    est_client_cert: str | None = Field(max_length=79, default="", description="Certificate used to authenticate this FortiGate to EST server.")  # datasource: ['certificate.local.name']    
    est_server_cert: str | None = Field(max_length=79, default="", description="EST server's certificate must be verifiable by this certificate to be authenticated.")  # datasource: ['certificate.ca.name', 'certificate.remote.name']    
    est_srp_username: str | None = Field(max_length=63, default="", description="EST SRP authentication username.")    
    est_srp_password: Any = Field(max_length=128, default=None, description="EST SRP authentication password.")    
    est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = Field(default="create-new-key", description="EST behavioral options during re-enrollment.")    
    details: list[Details] = Field(default=None, description="Print local certificate detailed information.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('cmp_server_cert')
    @classmethod
    def validate_cmp_server_cert(cls, v: Any) -> Any:
        """
        Validate cmp_server_cert field.
        
        Datasource: ['certificate.ca.name', 'certificate.remote.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('est_client_cert')
    @classmethod
    def validate_est_client_cert(cls, v: Any) -> Any:
        """
        Validate est_client_cert field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('est_server_cert')
    @classmethod
    def validate_est_server_cert(cls, v: Any) -> Any:
        """
        Validate est_server_cert field.
        
        Datasource: ['certificate.ca.name', 'certificate.remote.name']
        
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
    async def validate_cmp_server_cert_references(self, client: Any) -> list[str]:
        """
        Validate cmp_server_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/ca        - certificate/remote        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     cmp_server_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_cmp_server_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.certificate.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "cmp_server_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.ca.exists(value):
            found = True
        elif await client.api.cmdb.certificate.remote.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Cmp-Server-Cert '{value}' not found in "
                "certificate/ca or certificate/remote"
            )        
        return errors    
    async def validate_est_client_cert_references(self, client: Any) -> list[str]:
        """
        Validate est_client_cert references exist in FortiGate.
        
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
            >>> policy = LocalModel(
            ...     est_client_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_est_client_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.certificate.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "est_client_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Est-Client-Cert '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_est_server_cert_references(self, client: Any) -> list[str]:
        """
        Validate est_server_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/ca        - certificate/remote        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     est_server_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_est_server_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.certificate.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "est_server_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.ca.exists(value):
            found = True
        elif await client.api.cmdb.certificate.remote.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Est-Server-Cert '{value}' not found in "
                "certificate/ca or certificate/remote"
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
        
        errors = await self.validate_cmp_server_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_est_client_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_est_server_cert_references(client)
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
    "LocalModel",    "LocalDetails",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.038032Z
# ============================================================================
"""
Pydantic Models for CMDB - user/peer

Runtime validation models for user/peer configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class PeerCn_typeEnum(str, Enum):
    """Allowed values for cn_type field."""
    STRING = "string"    EMAIL = "email"    FQDN = "FQDN"    IPV4 = "ipv4"    IPV6 = "ipv6"

# ============================================================================
# Main Model
# ============================================================================

class PeerModel(BaseModel):
    """
    Pydantic model for user/peer configuration.
    
    Configure peer users.
    
    Validation Rules:        - name: max_length=35 pattern=        - mandatory_ca_verify: pattern=        - ca: max_length=127 pattern=        - subject: max_length=255 pattern=        - cn: max_length=255 pattern=        - cn_type: pattern=        - mfa_mode: pattern=        - mfa_server: max_length=35 pattern=        - mfa_username: max_length=35 pattern=        - mfa_password: max_length=128 pattern=        - ocsp_override_server: max_length=35 pattern=        - two_factor: pattern=        - passwd: max_length=128 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Peer name.")    
    mandatory_ca_verify: Literal["enable", "disable"] | None = Field(default="enable", description="Determine what happens to the peer if the CA certificate is not installed. Disable to automatically consider the peer certificate as valid.")    
    ca: str | None = Field(max_length=127, default="", description="Name of the CA certificate.")  # datasource: ['vpn.certificate.ca.name']    
    subject: str | None = Field(max_length=255, default="", description="Peer certificate name constraints.")    
    cn: str | None = Field(max_length=255, default="", description="Peer certificate common name.")    
    cn_type: CnTypeEnum | None = Field(default="string", description="Peer certificate common name type.")    
    mfa_mode: Literal["none", "password", "subject-identity"] | None = Field(default="none", description="MFA mode for remote peer authentication/authorization.")    
    mfa_server: str | None = Field(max_length=35, default="", description="Name of a remote authenticator. Performs client access right check.")  # datasource: ['user.radius.name', 'user.ldap.name']    
    mfa_username: str | None = Field(max_length=35, default="", description="Unified username for remote authentication.")    
    mfa_password: Any = Field(max_length=128, default=None, description="Unified password for remote authentication. This field may be left empty when RADIUS authentication is used, in which case the FortiGate will use the RADIUS username as a password. ")    
    ocsp_override_server: str | None = Field(max_length=35, default="", description="Online Certificate Status Protocol (OCSP) server for certificate retrieval.")  # datasource: ['vpn.certificate.ocsp-server.name']    
    two_factor: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable two-factor authentication, applying certificate and password-based authentication.")    
    passwd: Any = Field(max_length=128, default=None, description="Peer's password used for two-factor authentication.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ca')
    @classmethod
    def validate_ca(cls, v: Any) -> Any:
        """
        Validate ca field.
        
        Datasource: ['vpn.certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('mfa_server')
    @classmethod
    def validate_mfa_server(cls, v: Any) -> Any:
        """
        Validate mfa_server field.
        
        Datasource: ['user.radius.name', 'user.ldap.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ocsp_override_server')
    @classmethod
    def validate_ocsp_override_server(cls, v: Any) -> Any:
        """
        Validate ocsp_override_server field.
        
        Datasource: ['vpn.certificate.ocsp-server.name']
        
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
    async def validate_ca_references(self, client: Any) -> list[str]:
        """
        Validate ca references exist in FortiGate.
        
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
            >>> policy = PeerModel(
            ...     ca="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ca_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.peer.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ca", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ca '{value}' not found in "
                "vpn/certificate/ca"
            )        
        return errors    
    async def validate_mfa_server_references(self, client: Any) -> list[str]:
        """
        Validate mfa_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/radius        - user/ldap        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PeerModel(
            ...     mfa_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_mfa_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.peer.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "mfa_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.radius.exists(value):
            found = True
        elif await client.api.cmdb.user.ldap.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Mfa-Server '{value}' not found in "
                "user/radius or user/ldap"
            )        
        return errors    
    async def validate_ocsp_override_server_references(self, client: Any) -> list[str]:
        """
        Validate ocsp_override_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/ocsp-server        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PeerModel(
            ...     ocsp_override_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ocsp_override_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.peer.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ocsp_override_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.ocsp-server.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ocsp-Override-Server '{value}' not found in "
                "vpn/certificate/ocsp-server"
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
        
        errors = await self.validate_ca_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_mfa_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ocsp_override_server_references(client)
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
    "PeerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.633531Z
# ============================================================================
"""
Pydantic Models for CMDB - authentication/scheme

Runtime validation models for authentication/scheme configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SchemeUserDatabase(BaseModel):
    """
    Child table model for user-database.
    
    Authentication server to contain user information; "local-user-db" (default) or "123" (for LDAP).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Authentication server name.")  # datasource: ['system.datasource.name', 'user.radius.name', 'user.tacacs+.name', 'user.ldap.name', 'user.group.name', 'user.scim.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SchemeMethodEnum(str, Enum):
    """Allowed values for method field."""
    NTLM = "ntlm"    BASIC = "basic"    DIGEST = "digest"    FORM = "form"    NEGOTIATE = "negotiate"    FSSO = "fsso"    RSSO = "rsso"    SSH_PUBLICKEY = "ssh-publickey"    CERT = "cert"    SAML = "saml"    ENTRA_SSO = "entra-sso"

# ============================================================================
# Main Model
# ============================================================================

class SchemeModel(BaseModel):
    """
    Pydantic model for authentication/scheme configuration.
    
    Configure Authentication Schemes.
    
    Validation Rules:        - name: max_length=35 pattern=        - method: pattern=        - negotiate_ntlm: pattern=        - kerberos_keytab: max_length=35 pattern=        - domain_controller: max_length=35 pattern=        - saml_server: max_length=35 pattern=        - saml_timeout: min=30 max=1200 pattern=        - fsso_agent_for_ntlm: max_length=35 pattern=        - require_tfa: pattern=        - fsso_guest: pattern=        - user_cert: pattern=        - cert_http_header: pattern=        - user_database: pattern=        - ssh_ca: max_length=35 pattern=        - external_idp: max_length=35 pattern=        - group_attr_type: pattern=        - digest_algo: pattern=        - digest_rfc2069: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Authentication scheme name.")    
    method: list[Method] = Field(default="", description="Authentication methods (default = basic).")    
    negotiate_ntlm: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable negotiate authentication for NTLM (default = disable).")    
    kerberos_keytab: str | None = Field(max_length=35, default="", description="Kerberos keytab setting.")  # datasource: ['user.krb-keytab.name']    
    domain_controller: str | None = Field(max_length=35, default="", description="Domain controller setting.")  # datasource: ['user.domain-controller.name']    
    saml_server: str | None = Field(max_length=35, default="", description="SAML configuration.")  # datasource: ['user.saml.name']    
    saml_timeout: int | None = Field(ge=30, le=1200, default=120, description="SAML authentication timeout in seconds.")    
    fsso_agent_for_ntlm: str | None = Field(max_length=35, default="", description="FSSO agent to use for NTLM authentication.")  # datasource: ['user.fsso.name']    
    require_tfa: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable two-factor authentication (default = disable).")    
    fsso_guest: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable user fsso-guest authentication (default = disable).")    
    user_cert: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication with user certificate (default = disable).")    
    cert_http_header: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication with user certificate in Client-Cert HTTP header (default = disable).")    
    user_database: list[UserDatabase] = Field(default=None, description="Authentication server to contain user information; \"local-user-db\" (default) or \"123\" (for LDAP).")    
    ssh_ca: str | None = Field(max_length=35, default="", description="SSH CA name.")  # datasource: ['firewall.ssh.local-ca.name']    
    external_idp: str | None = Field(max_length=35, default="", description="External identity provider configuration.")  # datasource: ['user.external-identity-provider.name']    
    group_attr_type: Literal["display-name", "external-id"] | None = Field(default="display-name", description="Group attribute type used to match SCIM groups (default = display-name).")    
    digest_algo: list[DigestAlgo] = Field(default="md5 sha-256", description="Digest Authentication Algorithms.")    
    digest_rfc2069: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable support for the deprecated RFC2069 Digest Client (no cnonce field, default = disable).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('kerberos_keytab')
    @classmethod
    def validate_kerberos_keytab(cls, v: Any) -> Any:
        """
        Validate kerberos_keytab field.
        
        Datasource: ['user.krb-keytab.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('domain_controller')
    @classmethod
    def validate_domain_controller(cls, v: Any) -> Any:
        """
        Validate domain_controller field.
        
        Datasource: ['user.domain-controller.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('saml_server')
    @classmethod
    def validate_saml_server(cls, v: Any) -> Any:
        """
        Validate saml_server field.
        
        Datasource: ['user.saml.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fsso_agent_for_ntlm')
    @classmethod
    def validate_fsso_agent_for_ntlm(cls, v: Any) -> Any:
        """
        Validate fsso_agent_for_ntlm field.
        
        Datasource: ['user.fsso.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssh_ca')
    @classmethod
    def validate_ssh_ca(cls, v: Any) -> Any:
        """
        Validate ssh_ca field.
        
        Datasource: ['firewall.ssh.local-ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('external_idp')
    @classmethod
    def validate_external_idp(cls, v: Any) -> Any:
        """
        Validate external_idp field.
        
        Datasource: ['user.external-identity-provider.name']
        
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
    async def validate_kerberos_keytab_references(self, client: Any) -> list[str]:
        """
        Validate kerberos_keytab references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/krb-keytab        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SchemeModel(
            ...     kerberos_keytab="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_kerberos_keytab_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.scheme.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "kerberos_keytab", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.krb-keytab.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Kerberos-Keytab '{value}' not found in "
                "user/krb-keytab"
            )        
        return errors    
    async def validate_domain_controller_references(self, client: Any) -> list[str]:
        """
        Validate domain_controller references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/domain-controller        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SchemeModel(
            ...     domain_controller="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_domain_controller_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.scheme.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "domain_controller", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.domain-controller.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Domain-Controller '{value}' not found in "
                "user/domain-controller"
            )        
        return errors    
    async def validate_saml_server_references(self, client: Any) -> list[str]:
        """
        Validate saml_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/saml        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SchemeModel(
            ...     saml_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_saml_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.scheme.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "saml_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.saml.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Saml-Server '{value}' not found in "
                "user/saml"
            )        
        return errors    
    async def validate_fsso_agent_for_ntlm_references(self, client: Any) -> list[str]:
        """
        Validate fsso_agent_for_ntlm references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/fsso        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SchemeModel(
            ...     fsso_agent_for_ntlm="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fsso_agent_for_ntlm_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.scheme.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fsso_agent_for_ntlm", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.fsso.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fsso-Agent-For-Ntlm '{value}' not found in "
                "user/fsso"
            )        
        return errors    
    async def validate_user_database_references(self, client: Any) -> list[str]:
        """
        Validate user_database references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/datasource        - user/radius        - user/tacacs+        - user/ldap        - user/group        - user/scim        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SchemeModel(
            ...     user_database=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_user_database_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.scheme.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "user_database", [])
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
            if await client.api.cmdb.system.datasource.exists(value):
                found = True
            elif await client.api.cmdb.user.radius.exists(value):
                found = True
            elif await client.api.cmdb.user.tacacs+.exists(value):
                found = True
            elif await client.api.cmdb.user.ldap.exists(value):
                found = True
            elif await client.api.cmdb.user.group.exists(value):
                found = True
            elif await client.api.cmdb.user.scim.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"User-Database '{value}' not found in "
                    "system/datasource or user/radius or user/tacacs+ or user/ldap or user/group or user/scim"
                )        
        return errors    
    async def validate_ssh_ca_references(self, client: Any) -> list[str]:
        """
        Validate ssh_ca references exist in FortiGate.
        
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
            >>> policy = SchemeModel(
            ...     ssh_ca="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssh_ca_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.scheme.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssh_ca", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssh-Ca '{value}' not found in "
                "firewall/ssh/local-ca"
            )        
        return errors    
    async def validate_external_idp_references(self, client: Any) -> list[str]:
        """
        Validate external_idp references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/external-identity-provider        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SchemeModel(
            ...     external_idp="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_external_idp_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.scheme.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "external_idp", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.external-identity-provider.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"External-Idp '{value}' not found in "
                "user/external-identity-provider"
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
        
        errors = await self.validate_kerberos_keytab_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_domain_controller_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_saml_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fsso_agent_for_ntlm_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_user_database_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssh_ca_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_external_idp_references(client)
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
    "SchemeModel",    "SchemeUserDatabase",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.104302Z
# ============================================================================
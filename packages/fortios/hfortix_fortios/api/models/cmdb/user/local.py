"""
Pydantic Models for CMDB - user/local

Runtime validation models for user/local configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LocalTypeEnum(str, Enum):
    """Allowed values for type field."""
    PASSWORD = "password"    RADIUS = "radius"    TACACS = "tacacs+"    LDAP = "ldap"    SAML = "saml"
class LocalTwo_factorEnum(str, Enum):
    """Allowed values for two_factor field."""
    DISABLE = "disable"    FORTITOKEN = "fortitoken"    FORTITOKEN_CLOUD = "fortitoken-cloud"    EMAIL = "email"    SMS = "sms"

# ============================================================================
# Main Model
# ============================================================================

class LocalModel(BaseModel):
    """
    Pydantic model for user/local configuration.
    
    Configure local users.
    
    Validation Rules:        - name: max_length=64 pattern=        - id: min=0 max=4294967295 pattern=        - status: pattern=        - type: pattern=        - passwd: max_length=128 pattern=        - ldap_server: max_length=35 pattern=        - radius_server: max_length=35 pattern=        - tacacs+_server: max_length=35 pattern=        - saml_server: max_length=35 pattern=        - two_factor: pattern=        - two_factor_authentication: pattern=        - two_factor_notification: pattern=        - fortitoken: max_length=16 pattern=        - email_to: max_length=63 pattern=        - sms_server: pattern=        - sms_custom_server: max_length=35 pattern=        - sms_phone: max_length=15 pattern=        - passwd_policy: max_length=35 pattern=        - passwd_time: pattern=        - authtimeout: min=0 max=1440 pattern=        - workstation: max_length=35 pattern=        - auth_concurrent_override: pattern=        - auth_concurrent_value: min=0 max=100 pattern=        - ppk_secret: pattern=        - ppk_identity: max_length=35 pattern=        - qkd_profile: max_length=35 pattern=        - username_sensitivity: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=64, default="", description="Local user name.")    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="User ID.")    
    status: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable allowing the local user to authenticate with the FortiGate unit.")    
    type: TypeEnum = Field(default="password", description="Authentication method.")    
    passwd: Any = Field(max_length=128, description="User's password.")    
    ldap_server: str = Field(max_length=35, default="", description="Name of LDAP server with which the user must authenticate.")  # datasource: ['user.ldap.name']    
    radius_server: str = Field(max_length=35, default="", description="Name of RADIUS server with which the user must authenticate.")  # datasource: ['user.radius.name']    
    tacacs+_server: str = Field(max_length=35, default="", description="Name of TACACS+ server with which the user must authenticate.")  # datasource: ['user.tacacs+.name']    
    saml_server: str = Field(max_length=35, default="", description="Name of SAML server with which the user must authenticate.")  # datasource: ['user.saml.name']    
    two_factor: TwoFactorEnum | None = Field(default="disable", description="Enable/disable two-factor authentication.")    
    two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = Field(default="", description="Authentication method by FortiToken Cloud.")    
    two_factor_notification: Literal["email", "sms"] | None = Field(default="", description="Notification method for user activation by FortiToken Cloud.")    
    fortitoken: str | None = Field(max_length=16, default="", description="Two-factor recipient's FortiToken serial number.")  # datasource: ['user.fortitoken.serial-number']    
    email_to: str | None = Field(max_length=63, default="", description="Two-factor recipient's email address.")    
    sms_server: Literal["fortiguard", "custom"] | None = Field(default="fortiguard", description="Send SMS through FortiGuard or other external server.")    
    sms_custom_server: str | None = Field(max_length=35, default="", description="Two-factor recipient's SMS server.")  # datasource: ['system.sms-server.name']    
    sms_phone: str | None = Field(max_length=15, default="", description="Two-factor recipient's mobile phone number.")    
    passwd_policy: str | None = Field(max_length=35, default="", description="Password policy to apply to this user, as defined in config user password-policy.")  # datasource: ['user.password-policy.name']    
    passwd_time: str | None = Field(default="", description="Time of the last password update.")    
    authtimeout: int | None = Field(ge=0, le=1440, default=0, description="Time in minutes before the authentication timeout for a user is reached.")    
    workstation: str | None = Field(max_length=35, default="", description="Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation.")    
    auth_concurrent_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable overriding the policy-auth-concurrent under config system global.")    
    auth_concurrent_value: int | None = Field(ge=0, le=100, default=0, description="Maximum number of concurrent logins permitted from the same user.")    
    ppk_secret: Any = Field(default=None, description="IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).")    
    ppk_identity: str | None = Field(max_length=35, default="", description="IKEv2 Postquantum Preshared Key Identity.")    
    qkd_profile: str | None = Field(max_length=35, default="", description="Quantum Key Distribution (QKD) profile.")  # datasource: ['vpn.qkd.name']    
    username_sensitivity: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable case and accent sensitivity when performing username matching (accents are stripped and case is ignored when disabled).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ldap_server')
    @classmethod
    def validate_ldap_server(cls, v: Any) -> Any:
        """
        Validate ldap_server field.
        
        Datasource: ['user.ldap.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('radius_server')
    @classmethod
    def validate_radius_server(cls, v: Any) -> Any:
        """
        Validate radius_server field.
        
        Datasource: ['user.radius.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('tacacs+_server')
    @classmethod
    def validate_tacacs+_server(cls, v: Any) -> Any:
        """
        Validate tacacs+_server field.
        
        Datasource: ['user.tacacs+.name']
        
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
    @field_validator('fortitoken')
    @classmethod
    def validate_fortitoken(cls, v: Any) -> Any:
        """
        Validate fortitoken field.
        
        Datasource: ['user.fortitoken.serial-number']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sms_custom_server')
    @classmethod
    def validate_sms_custom_server(cls, v: Any) -> Any:
        """
        Validate sms_custom_server field.
        
        Datasource: ['system.sms-server.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('passwd_policy')
    @classmethod
    def validate_passwd_policy(cls, v: Any) -> Any:
        """
        Validate passwd_policy field.
        
        Datasource: ['user.password-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('qkd_profile')
    @classmethod
    def validate_qkd_profile(cls, v: Any) -> Any:
        """
        Validate qkd_profile field.
        
        Datasource: ['vpn.qkd.name']
        
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
    async def validate_ldap_server_references(self, client: Any) -> list[str]:
        """
        Validate ldap_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/ldap        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     ldap_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ldap_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ldap_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.ldap.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ldap-Server '{value}' not found in "
                "user/ldap"
            )        
        return errors    
    async def validate_radius_server_references(self, client: Any) -> list[str]:
        """
        Validate radius_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/radius        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     radius_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_radius_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "radius_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.radius.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Radius-Server '{value}' not found in "
                "user/radius"
            )        
        return errors    
    async def validate_tacacs+_server_references(self, client: Any) -> list[str]:
        """
        Validate tacacs+_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/tacacs+        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     tacacs+_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tacacs+_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "tacacs+_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.tacacs+.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Tacacs+-Server '{value}' not found in "
                "user/tacacs+"
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
            >>> policy = LocalModel(
            ...     saml_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_saml_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
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
    async def validate_fortitoken_references(self, client: Any) -> list[str]:
        """
        Validate fortitoken references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/fortitoken        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     fortitoken="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fortitoken_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fortitoken", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.fortitoken.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fortitoken '{value}' not found in "
                "user/fortitoken"
            )        
        return errors    
    async def validate_sms_custom_server_references(self, client: Any) -> list[str]:
        """
        Validate sms_custom_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sms-server        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     sms_custom_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sms_custom_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "sms_custom_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.sms-server.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Sms-Custom-Server '{value}' not found in "
                "system/sms-server"
            )        
        return errors    
    async def validate_passwd_policy_references(self, client: Any) -> list[str]:
        """
        Validate passwd_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/password-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     passwd_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_passwd_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "passwd_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.password-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Passwd-Policy '{value}' not found in "
                "user/password-policy"
            )        
        return errors    
    async def validate_qkd_profile_references(self, client: Any) -> list[str]:
        """
        Validate qkd_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/qkd        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LocalModel(
            ...     qkd_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_qkd_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "qkd_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.qkd.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Qkd-Profile '{value}' not found in "
                "vpn/qkd"
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
        
        errors = await self.validate_ldap_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_radius_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_tacacs+_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_saml_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fortitoken_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sms_custom_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_passwd_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_qkd_profile_references(client)
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
    "LocalModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.129617Z
# ============================================================================
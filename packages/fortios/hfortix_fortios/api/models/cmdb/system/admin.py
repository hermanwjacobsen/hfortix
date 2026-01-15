"""
Pydantic Models for CMDB - system/admin

Runtime validation models for system/admin configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class AdminVdom(BaseModel):
    """
    Child table model for vdom.
    
    Virtual domain(s) that the administrator can access.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Virtual domain name.")  # datasource: ['system.vdom.name']
class AdminGuestUsergroups(BaseModel):
    """
    Child table model for guest-usergroups.
    
    Select guest user groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Select guest user groups.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class AdminTwo_factorEnum(str, Enum):
    """Allowed values for two_factor field."""
    DISABLE = "disable"    FORTITOKEN = "fortitoken"    FORTITOKEN_CLOUD = "fortitoken-cloud"    EMAIL = "email"    SMS = "sms"

# ============================================================================
# Main Model
# ============================================================================

class AdminModel(BaseModel):
    """
    Pydantic model for system/admin configuration.
    
    Configure admin users.
    
    Validation Rules:        - name: max_length=64 pattern=        - vdom: pattern=        - remote_auth: pattern=        - remote_group: max_length=35 pattern=        - wildcard: pattern=        - password: max_length=128 pattern=        - peer_auth: pattern=        - peer_group: max_length=35 pattern=        - trusthost1: pattern=        - trusthost2: pattern=        - trusthost3: pattern=        - trusthost4: pattern=        - trusthost5: pattern=        - trusthost6: pattern=        - trusthost7: pattern=        - trusthost8: pattern=        - trusthost9: pattern=        - trusthost10: pattern=        - ip6_trusthost1: pattern=        - ip6_trusthost2: pattern=        - ip6_trusthost3: pattern=        - ip6_trusthost4: pattern=        - ip6_trusthost5: pattern=        - ip6_trusthost6: pattern=        - ip6_trusthost7: pattern=        - ip6_trusthost8: pattern=        - ip6_trusthost9: pattern=        - ip6_trusthost10: pattern=        - accprofile: max_length=35 pattern=        - allow_remove_admin_session: pattern=        - comments: max_length=255 pattern=        - ssh_public_key1: pattern=        - ssh_public_key2: pattern=        - ssh_public_key3: pattern=        - ssh_certificate: max_length=35 pattern=        - schedule: max_length=35 pattern=        - accprofile_override: pattern=        - vdom_override: pattern=        - password_expire: pattern=        - force_password_change: pattern=        - two_factor: pattern=        - two_factor_authentication: pattern=        - two_factor_notification: pattern=        - fortitoken: max_length=16 pattern=        - email_to: max_length=63 pattern=        - sms_server: pattern=        - sms_custom_server: max_length=35 pattern=        - sms_phone: max_length=15 pattern=        - guest_auth: pattern=        - guest_usergroups: pattern=        - guest_lang: max_length=35 pattern=        - status: pattern=        - list: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=64, default="", description="User name.")    
    vdom: list[Vdom] = Field(default=None, description="Virtual domain(s) that the administrator can access.")    
    remote_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication using a remote RADIUS, LDAP, or TACACS+ server.")    
    remote_group: str = Field(max_length=35, default="", description="User group name used for remote auth.")    
    wildcard: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable wildcard RADIUS authentication.")    
    password: Any = Field(max_length=128, description="Admin user password.")    
    peer_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Set to enable peer certificate authentication (for HTTPS admin access).")    
    peer_group: str = Field(max_length=35, default="", description="Name of peer group defined under config user group which has PKI members. Used for peer certificate authentication (for HTTPS admin access).")    
    trusthost1: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost2: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost3: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost4: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost5: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost6: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost7: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost8: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost9: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    trusthost10: str | None = Field(default="0.0.0.0 0.0.0.0", description="Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address.")    
    ip6_trusthost1: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost2: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost3: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost4: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost5: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost6: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost7: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost8: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost9: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    ip6_trusthost10: str | None = Field(default="::/0", description="Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address.")    
    accprofile: str | None = Field(max_length=35, default="", description="Access profile for this administrator. Access profiles control administrator access to FortiGate features.")  # datasource: ['system.accprofile.name']    
    allow_remove_admin_session: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allow admin session to be removed by privileged admin users.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    ssh_public_key1: str | None = Field(default="", description="Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.")    
    ssh_public_key2: str | None = Field(default="", description="Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.")    
    ssh_public_key3: str | None = Field(default="", description="Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application.")    
    ssh_certificate: str | None = Field(max_length=35, default="", description="Select the certificate to be used by the FortiGate for authentication with an SSH client.")  # datasource: ['certificate.remote.name']    
    schedule: str | None = Field(max_length=35, default="", description="Firewall schedule used to restrict when the administrator can log in. No schedule means no restrictions.")    
    accprofile_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use the name of an access profile provided by the remote authentication server to control the FortiGate features that this administrator can access.")    
    vdom_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to use the names of VDOMs provided by the remote authentication server to control the VDOMs that this administrator can access.")    
    password_expire: Any = Field(default="0000-00-00 00:00:00", description="Password expire time.")    
    force_password_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable force password change on next login.")    
    two_factor: TwoFactorEnum | None = Field(default="disable", description="Enable/disable two-factor authentication.")    
    two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = Field(default="", description="Authentication method by FortiToken Cloud.")    
    two_factor_notification: Literal["email", "sms"] | None = Field(default="", description="Notification method for user activation by FortiToken Cloud.")    
    fortitoken: str | None = Field(max_length=16, default="", description="This administrator's FortiToken serial number.")    
    email_to: str | None = Field(max_length=63, default="", description="This administrator's email address.")    
    sms_server: Literal["fortiguard", "custom"] | None = Field(default="fortiguard", description="Send SMS messages using the FortiGuard SMS server or a custom server.")    
    sms_custom_server: str | None = Field(max_length=35, default="", description="Custom SMS server to send SMS messages to.")  # datasource: ['system.sms-server.name']    
    sms_phone: str | None = Field(max_length=15, default="", description="Phone number on which the administrator receives SMS messages.")    
    guest_auth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable guest authentication.")    
    guest_usergroups: list[GuestUsergroups] = Field(default=None, description="Select guest user groups.")    
    guest_lang: str | None = Field(max_length=35, default="", description="Guest management portal language.")  # datasource: ['system.custom-language.name']    
    status: Any = Field(default=None, description="print admin status information")    
    list: Any = Field(default=None, description="print admin list information")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('accprofile')
    @classmethod
    def validate_accprofile(cls, v: Any) -> Any:
        """
        Validate accprofile field.
        
        Datasource: ['system.accprofile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssh_certificate')
    @classmethod
    def validate_ssh_certificate(cls, v: Any) -> Any:
        """
        Validate ssh_certificate field.
        
        Datasource: ['certificate.remote.name']
        
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
    @field_validator('guest_lang')
    @classmethod
    def validate_guest_lang(cls, v: Any) -> Any:
        """
        Validate guest_lang field.
        
        Datasource: ['system.custom-language.name']
        
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
    async def validate_vdom_references(self, client: Any) -> list[str]:
        """
        Validate vdom references exist in FortiGate.
        
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
            >>> policy = AdminModel(
            ...     vdom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.admin.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "vdom", [])
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
            if await client.api.cmdb.system.vdom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Vdom '{value}' not found in "
                    "system/vdom"
                )        
        return errors    
    async def validate_accprofile_references(self, client: Any) -> list[str]:
        """
        Validate accprofile references exist in FortiGate.
        
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
            >>> policy = AdminModel(
            ...     accprofile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_accprofile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.admin.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "accprofile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.accprofile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Accprofile '{value}' not found in "
                "system/accprofile"
            )        
        return errors    
    async def validate_ssh_certificate_references(self, client: Any) -> list[str]:
        """
        Validate ssh_certificate references exist in FortiGate.
        
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
            >>> policy = AdminModel(
            ...     ssh_certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssh_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.admin.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssh_certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.remote.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssh-Certificate '{value}' not found in "
                "certificate/remote"
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
            >>> policy = AdminModel(
            ...     sms_custom_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sms_custom_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.admin.post(policy.to_fortios_dict())
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
    async def validate_guest_lang_references(self, client: Any) -> list[str]:
        """
        Validate guest_lang references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/custom-language        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AdminModel(
            ...     guest_lang="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_guest_lang_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.admin.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "guest_lang", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.custom-language.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Guest-Lang '{value}' not found in "
                "system/custom-language"
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
        
        errors = await self.validate_vdom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_accprofile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssh_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sms_custom_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_guest_lang_references(client)
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
    "AdminModel",    "AdminVdom",    "AdminGuestUsergroups",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.142910Z
# ============================================================================
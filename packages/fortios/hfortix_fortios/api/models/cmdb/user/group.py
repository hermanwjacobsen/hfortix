"""
Pydantic Models for CMDB - user/group

Runtime validation models for user/group configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class GroupMember(BaseModel):
    """
    Child table model for member.
    
    Names of users, peers, LDAP severs, RADIUS servers or external idp servers to add to the user group.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=511, default="", description="Group member name.")  # datasource: ['user.peer.name', 'user.local.name', 'user.radius.name', 'user.tacacs+.name', 'user.ldap.name', 'user.saml.name', 'user.external-identity-provider.name', 'user.adgrp.name', 'user.pop3.name', 'user.certificate.name']
class GroupMatch(BaseModel):
    """
    Child table model for match.
    
    Group matches.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    server_name: str = Field(max_length=35, default="", description="Name of remote auth server.")  # datasource: ['user.radius.name', 'user.ldap.name', 'user.tacacs+.name', 'user.saml.name', 'user.external-identity-provider.name']    
    group_name: str = Field(max_length=511, default="", description="Name of matching user or group on remote authentication server or SCIM.")
class GroupGuest(BaseModel):
    """
    Child table model for guest.
    
    Guest User.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Guest ID.")    
    user_id: str | None = Field(max_length=64, default="", description="Guest ID.")    
    name: str | None = Field(max_length=64, default="", description="Guest name.")    
    password: Any = Field(max_length=128, default=None, description="Guest password.")    
    mobile_phone: str | None = Field(max_length=35, default="", description="Mobile phone.")    
    sponsor: str | None = Field(max_length=35, default="", description="Set the action for the sponsor guest user field.")    
    company: str | None = Field(max_length=35, default="", description="Set the action for the company guest user field.")    
    email: str | None = Field(max_length=64, default="", description="Email.")    
    expiration: str | None = Field(default="", description="Expire time.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class GroupGroup_typeEnum(str, Enum):
    """Allowed values for group_type field."""
    FIREWALL = "firewall"    FSSO_SERVICE = "fsso-service"    RSSO = "rsso"    GUEST = "guest"

# ============================================================================
# Main Model
# ============================================================================

class GroupModel(BaseModel):
    """
    Pydantic model for user/group configuration.
    
    Configure user groups.
    
    Validation Rules:        - name: max_length=35 pattern=        - id: min=0 max=4294967295 pattern=        - group_type: pattern=        - authtimeout: min=0 max=43200 pattern=        - auth_concurrent_override: pattern=        - auth_concurrent_value: min=0 max=100 pattern=        - http_digest_realm: max_length=35 pattern=        - sso_attribute_value: max_length=511 pattern=        - member: pattern=        - match: pattern=        - user_id: pattern=        - password: pattern=        - user_name: pattern=        - sponsor: pattern=        - company: pattern=        - email: pattern=        - mobile_phone: pattern=        - sms_server: pattern=        - sms_custom_server: max_length=35 pattern=        - expire_type: pattern=        - expire: min=1 max=31536000 pattern=        - max_accounts: min=0 max=500 pattern=        - multiple_guest_add: pattern=        - guest: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Group name.")    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Group ID.")    
    group_type: GroupTypeEnum | None = Field(default="firewall", description="Set the group to be for firewall authentication, FSSO, RSSO, or guest users.")    
    authtimeout: int | None = Field(ge=0, le=43200, default=0, description="Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout.")    
    auth_concurrent_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable overriding the global number of concurrent authentication sessions for this user group.")    
    auth_concurrent_value: int | None = Field(ge=0, le=100, default=0, description="Maximum number of concurrent authenticated connections per user (0 - 100).")    
    http_digest_realm: str | None = Field(max_length=35, default="", description="Realm attribute for MD5-digest authentication.")    
    sso_attribute_value: str | None = Field(max_length=511, default="", description="RADIUS attribute value.")    
    member: list[Member] = Field(default=None, description="Names of users, peers, LDAP severs, RADIUS servers or external idp servers to add to the user group.")    
    match: list[Match] = Field(default=None, description="Group matches.")    
    user_id: Literal["email", "auto-generate", "specify"] | None = Field(default="email", description="Guest user ID type.")    
    password: Literal["auto-generate", "specify", "disable"] | None = Field(default="auto-generate", description="Guest user password type.")    
    user_name: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable the guest user name entry.")    
    sponsor: Literal["optional", "mandatory", "disabled"] | None = Field(default="optional", description="Set the action for the sponsor guest user field.")    
    company: Literal["optional", "mandatory", "disabled"] | None = Field(default="optional", description="Set the action for the company guest user field.")    
    email: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable the guest user email address field.")    
    mobile_phone: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable the guest user mobile phone number field.")    
    sms_server: Literal["fortiguard", "custom"] | None = Field(default="fortiguard", description="Send SMS through FortiGuard or other external server.")    
    sms_custom_server: str | None = Field(max_length=35, default="", description="SMS server.")  # datasource: ['system.sms-server.name']    
    expire_type: Literal["immediately", "first-successful-login"] | None = Field(default="immediately", description="Determine when the expiration countdown begins.")    
    expire: int | None = Field(ge=1, le=31536000, default=14400, description="Time in seconds before guest user accounts expire (1 - 31536000).")    
    max_accounts: int | None = Field(ge=0, le=500, default=0, description="Maximum number of guest accounts that can be created for this group (0 means unlimited).")    
    multiple_guest_add: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable addition of multiple guests.")    
    guest: list[Guest] = Field(default=None, description="Guest User.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    async def validate_member_references(self, client: Any) -> list[str]:
        """
        Validate member references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/peer        - user/local        - user/radius        - user/tacacs+        - user/ldap        - user/saml        - user/external-identity-provider        - user/adgrp        - user/pop3        - user/certificate        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GroupModel(
            ...     member=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_member_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "member", [])
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
            if await client.api.cmdb.user.peer.exists(value):
                found = True
            elif await client.api.cmdb.user.local.exists(value):
                found = True
            elif await client.api.cmdb.user.radius.exists(value):
                found = True
            elif await client.api.cmdb.user.tacacs+.exists(value):
                found = True
            elif await client.api.cmdb.user.ldap.exists(value):
                found = True
            elif await client.api.cmdb.user.saml.exists(value):
                found = True
            elif await client.api.cmdb.user.external-identity-provider.exists(value):
                found = True
            elif await client.api.cmdb.user.adgrp.exists(value):
                found = True
            elif await client.api.cmdb.user.pop3.exists(value):
                found = True
            elif await client.api.cmdb.user.certificate.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Member '{value}' not found in "
                    "user/peer or user/local or user/radius or user/tacacs+ or user/ldap or user/saml or user/external-identity-provider or user/adgrp or user/pop3 or user/certificate"
                )        
        return errors    
    async def validate_match_references(self, client: Any) -> list[str]:
        """
        Validate match references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/radius        - user/ldap        - user/tacacs+        - user/saml        - user/external-identity-provider        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GroupModel(
            ...     match=[{"server-name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_match_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "match", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("server-name")
            else:
                value = getattr(item, "server-name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.radius.exists(value):
                found = True
            elif await client.api.cmdb.user.ldap.exists(value):
                found = True
            elif await client.api.cmdb.user.tacacs+.exists(value):
                found = True
            elif await client.api.cmdb.user.saml.exists(value):
                found = True
            elif await client.api.cmdb.user.external-identity-provider.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Match '{value}' not found in "
                    "user/radius or user/ldap or user/tacacs+ or user/saml or user/external-identity-provider"
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
            >>> policy = GroupModel(
            ...     sms_custom_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sms_custom_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.group.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_member_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_match_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sms_custom_server_references(client)
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
    "GroupModel",    "GroupMember",    "GroupMatch",    "GroupGuest",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.590515Z
# ============================================================================
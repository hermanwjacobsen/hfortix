"""
Pydantic Models for CMDB - user/ldap

Runtime validation models for user/ldap configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LdapSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"
class LdapAccount_key_cert_fieldEnum(str, Enum):
    """Allowed values for account_key_cert_field field."""
    OTHERNAME = "othername"    RFC822NAME = "rfc822name"    DNSNAME = "dnsname"    CN = "cn"

# ============================================================================
# Main Model
# ============================================================================

class LdapModel(BaseModel):
    """
    Pydantic model for user/ldap configuration.
    
    Configure LDAP server entries.
    
    Validation Rules:        - name: max_length=35 pattern=        - server: max_length=63 pattern=        - secondary_server: max_length=63 pattern=        - tertiary_server: max_length=63 pattern=        - status_ttl: min=0 max=600 pattern=        - server_identity_check: pattern=        - source_ip: max_length=63 pattern=        - source_ip_interface: max_length=15 pattern=        - source_port: min=0 max=65535 pattern=        - cnid: max_length=20 pattern=        - dn: max_length=511 pattern=        - type: pattern=        - two_factor: pattern=        - two_factor_authentication: pattern=        - two_factor_notification: pattern=        - two_factor_filter: max_length=2047 pattern=        - username: max_length=511 pattern=        - password: max_length=128 pattern=        - group_member_check: pattern=        - group_search_base: max_length=511 pattern=        - group_object_filter: max_length=2047 pattern=        - group_filter: max_length=2047 pattern=        - secure: pattern=        - ssl_min_proto_version: pattern=        - ca_cert: max_length=79 pattern=        - port: min=1 max=65535 pattern=        - password_expiry_warning: pattern=        - password_renewal: pattern=        - member_attr: max_length=63 pattern=        - account_key_processing: pattern=        - account_key_cert_field: pattern=        - account_key_filter: max_length=2047 pattern=        - search_type: pattern=        - client_cert_auth: pattern=        - client_cert: max_length=79 pattern=        - obtain_user_info: pattern=        - user_info_exchange_server: max_length=35 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - antiphish: pattern=        - password_attr: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="LDAP server entry name.")    
    server: str = Field(max_length=63, default="", description="LDAP server CN domain name or IP.")    
    secondary_server: str | None = Field(max_length=63, default="", description="Secondary LDAP server CN domain name or IP.")    
    tertiary_server: str | None = Field(max_length=63, default="", description="Tertiary LDAP server CN domain name or IP.")    
    status_ttl: int | None = Field(ge=0, le=600, default=300, description="Time for which server reachability is cached so that when a server is unreachable, it will not be retried for at least this period of time (0 = cache disabled, default = 300).")    
    server_identity_check: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate).")    
    source_ip: str | None = Field(max_length=63, default="", description="FortiGate IP address to be used for communication with the LDAP server.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="Source interface for communication with the LDAP server.")  # datasource: ['system.interface.name']    
    source_port: int | None = Field(ge=0, le=65535, default=0, description="Source port to be used for communication with the LDAP server.")    
    cnid: str | None = Field(max_length=20, default="cn", description="Common name identifier for the LDAP server. The common name identifier for most LDAP servers is \"cn\".")    
    dn: str = Field(max_length=511, default="", description="Distinguished name used to look up entries on the LDAP server.")    
    type: Literal["simple", "anonymous", "regular"] | None = Field(default="simple", description="Authentication type for LDAP searches.")    
    two_factor: Literal["disable", "fortitoken-cloud"] | None = Field(default="disable", description="Enable/disable two-factor authentication.")    
    two_factor_authentication: Literal["fortitoken", "email", "sms"] | None = Field(default="", description="Authentication method by FortiToken Cloud.")    
    two_factor_notification: Literal["email", "sms"] | None = Field(default="", description="Notification method for user activation by FortiToken Cloud.")    
    two_factor_filter: str | None = Field(max_length=2047, default="", description="Filter used to synchronize users to FortiToken Cloud.")    
    username: str = Field(max_length=511, default="", description="Username (full DN) for initial binding.")    
    password: Any = Field(max_length=128, default=None, description="Password for initial binding.")    
    group_member_check: Literal["user-attr", "group-object", "posix-group-object"] | None = Field(default="user-attr", description="Group member checking methods.")    
    group_search_base: str | None = Field(max_length=511, default="", description="Search base used for group searching.")    
    group_object_filter: str | None = Field(max_length=2047, default="(&(objectcategory=group)(member=*))", description="Filter used for group searching.")    
    group_filter: str | None = Field(max_length=2047, default="", description="Filter used for group matching.")    
    secure: Literal["disable", "starttls", "ldaps"] | None = Field(default="disable", description="Port to be used for authentication.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    ca_cert: str | None = Field(max_length=79, default="", description="CA certificate name.")  # datasource: ['vpn.certificate.ca.name']    
    port: int | None = Field(ge=1, le=65535, default=389, description="Port to be used for communication with the LDAP server (default = 389).")    
    password_expiry_warning: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable password expiry warnings.")    
    password_renewal: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable online password renewal.")    
    member_attr: str | None = Field(max_length=63, default="memberOf", description="Name of attribute from which to get group membership.")    
    account_key_processing: Literal["same", "strip"] | None = Field(default="same", description="Account key processing operation. The FortiGate will keep either the whole domain or strip the domain from the subject identity.")    
    account_key_cert_field: AccountKeyCertFieldEnum | None = Field(default="othername", description="Define subject identity field in certificate for user access right checking.")    
    account_key_filter: str | None = Field(max_length=2047, default="(&(userPrincipalName=%s)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))", description="Account key filter, using the UPN as the search filter.")    
    search_type: list[SearchType] = Field(default="", description="Search type.")    
    client_cert_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable using client certificate for TLS authentication.")    
    client_cert: str | None = Field(max_length=79, default="", description="Client certificate name.")  # datasource: ['vpn.certificate.local.name']    
    obtain_user_info: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable obtaining of user information.")    
    user_info_exchange_server: str | None = Field(max_length=35, default="", description="MS Exchange server from which to fetch user information.")  # datasource: ['user.exchange.name']    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    antiphish: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AntiPhishing credential backend.")    
    password_attr: str | None = Field(max_length=35, default="userPassword", description="Name of attribute to get password hash.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('source_ip_interface')
    @classmethod
    def validate_source_ip_interface(cls, v: Any) -> Any:
        """
        Validate source_ip_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ca_cert')
    @classmethod
    def validate_ca_cert(cls, v: Any) -> Any:
        """
        Validate ca_cert field.
        
        Datasource: ['vpn.certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('client_cert')
    @classmethod
    def validate_client_cert(cls, v: Any) -> Any:
        """
        Validate client_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('user_info_exchange_server')
    @classmethod
    def validate_user_info_exchange_server(cls, v: Any) -> Any:
        """
        Validate user_info_exchange_server field.
        
        Datasource: ['user.exchange.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.interface.name']
        
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
    async def validate_source_ip_interface_references(self, client: Any) -> list[str]:
        """
        Validate source_ip_interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LdapModel(
            ...     source_ip_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_source_ip_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.ldap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "source_ip_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Source-Ip-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_ca_cert_references(self, client: Any) -> list[str]:
        """
        Validate ca_cert references exist in FortiGate.
        
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
            >>> policy = LdapModel(
            ...     ca_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ca_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.ldap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ca_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ca-Cert '{value}' not found in "
                "vpn/certificate/ca"
            )        
        return errors    
    async def validate_client_cert_references(self, client: Any) -> list[str]:
        """
        Validate client_cert references exist in FortiGate.
        
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
            >>> policy = LdapModel(
            ...     client_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_client_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.ldap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "client_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Client-Cert '{value}' not found in "
                "vpn/certificate/local"
            )        
        return errors    
    async def validate_user_info_exchange_server_references(self, client: Any) -> list[str]:
        """
        Validate user_info_exchange_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/exchange        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LdapModel(
            ...     user_info_exchange_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_user_info_exchange_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.ldap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "user_info_exchange_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.exchange.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"User-Info-Exchange-Server '{value}' not found in "
                "user/exchange"
            )        
        return errors    
    async def validate_interface_references(self, client: Any) -> list[str]:
        """
        Validate interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LdapModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.ldap.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Interface '{value}' not found in "
                "system/interface"
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
        
        errors = await self.validate_source_ip_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ca_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_client_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_user_info_exchange_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_interface_references(client)
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
    "LdapModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.631116Z
# ============================================================================
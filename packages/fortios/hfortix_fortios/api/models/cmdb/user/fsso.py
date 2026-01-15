"""
Pydantic Models for CMDB - user/fsso

Runtime validation models for user/fsso configuration.
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

class FssoModel(BaseModel):
    """
    Pydantic model for user/fsso configuration.
    
    Configure Fortinet Single Sign On (FSSO) agents.
    
    Validation Rules:        - name: max_length=35 pattern=        - type: pattern=        - server: max_length=63 pattern=        - port: min=1 max=65535 pattern=        - password: max_length=128 pattern=        - server2: max_length=63 pattern=        - port2: min=1 max=65535 pattern=        - password2: max_length=128 pattern=        - server3: max_length=63 pattern=        - port3: min=1 max=65535 pattern=        - password3: max_length=128 pattern=        - server4: max_length=63 pattern=        - port4: min=1 max=65535 pattern=        - password4: max_length=128 pattern=        - server5: max_length=63 pattern=        - port5: min=1 max=65535 pattern=        - password5: max_length=128 pattern=        - logon_timeout: min=1 max=2880 pattern=        - ldap_server: max_length=35 pattern=        - group_poll_interval: min=1 max=2880 pattern=        - ldap_poll: pattern=        - ldap_poll_interval: min=1 max=2880 pattern=        - ldap_poll_filter: max_length=2047 pattern=        - user_info_server: max_length=35 pattern=        - ssl: pattern=        - sni: max_length=255 pattern=        - ssl_server_host_ip_check: pattern=        - ssl_trusted_cert: max_length=79 pattern=        - source_ip: pattern=        - source_ip6: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
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
    type: Literal["default", "fortinac"] | None = Field(default="default", description="Server type.")    
    server: str = Field(max_length=63, default="", description="Domain name or IP address of the first FSSO collector agent.")    
    port: int = Field(ge=1, le=65535, default=8000, description="Port of the first FSSO collector agent.")    
    password: Any = Field(max_length=128, default=None, description="Password of the first FSSO collector agent.")    
    server2: str | None = Field(max_length=63, default="", description="Domain name or IP address of the second FSSO collector agent.")    
    port2: int | None = Field(ge=1, le=65535, default=8000, description="Port of the second FSSO collector agent.")    
    password2: Any = Field(max_length=128, default=None, description="Password of the second FSSO collector agent.")    
    server3: str | None = Field(max_length=63, default="", description="Domain name or IP address of the third FSSO collector agent.")    
    port3: int | None = Field(ge=1, le=65535, default=8000, description="Port of the third FSSO collector agent.")    
    password3: Any = Field(max_length=128, default=None, description="Password of the third FSSO collector agent.")    
    server4: str | None = Field(max_length=63, default="", description="Domain name or IP address of the fourth FSSO collector agent.")    
    port4: int | None = Field(ge=1, le=65535, default=8000, description="Port of the fourth FSSO collector agent.")    
    password4: Any = Field(max_length=128, default=None, description="Password of the fourth FSSO collector agent.")    
    server5: str | None = Field(max_length=63, default="", description="Domain name or IP address of the fifth FSSO collector agent.")    
    port5: int | None = Field(ge=1, le=65535, default=8000, description="Port of the fifth FSSO collector agent.")    
    password5: Any = Field(max_length=128, default=None, description="Password of the fifth FSSO collector agent.")    
    logon_timeout: int | None = Field(ge=1, le=2880, default=5, description="Interval in minutes to keep logons after FSSO server down.")    
    ldap_server: str | None = Field(max_length=35, default="", description="LDAP server to get group information.")  # datasource: ['user.ldap.name']    
    group_poll_interval: int | None = Field(ge=1, le=2880, default=0, description="Interval in minutes within to fetch groups from FSSO server, or unset to disable.")    
    ldap_poll: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic fetching of groups from LDAP server.")    
    ldap_poll_interval: int | None = Field(ge=1, le=2880, default=180, description="Interval in minutes within to fetch groups from LDAP server.")    
    ldap_poll_filter: str | None = Field(max_length=2047, default="(objectCategory=group)", description="Filter used to fetch groups.")    
    user_info_server: str | None = Field(max_length=35, default="", description="LDAP server to get user information.")  # datasource: ['user.ldap.name']    
    ssl: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of SSL.")    
    sni: str | None = Field(max_length=255, default="", description="Server Name Indication.")    
    ssl_server_host_ip_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable server host/IP verification.")    
    ssl_trusted_cert: str | None = Field(max_length=79, default="", description="Trusted server certificate or CA certificate.")  # datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP for communications to FSSO agent.")    
    source_ip6: str | None = Field(default="::", description="IPv6 source for communications to FSSO agent.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
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
    @field_validator('user_info_server')
    @classmethod
    def validate_user_info_server(cls, v: Any) -> Any:
        """
        Validate user_info_server field.
        
        Datasource: ['user.ldap.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssl_trusted_cert')
    @classmethod
    def validate_ssl_trusted_cert(cls, v: Any) -> Any:
        """
        Validate ssl_trusted_cert field.
        
        Datasource: ['vpn.certificate.remote.name', 'vpn.certificate.ca.name']
        
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
            >>> policy = FssoModel(
            ...     ldap_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ldap_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.fsso.post(policy.to_fortios_dict())
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
    async def validate_user_info_server_references(self, client: Any) -> list[str]:
        """
        Validate user_info_server references exist in FortiGate.
        
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
            >>> policy = FssoModel(
            ...     user_info_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_user_info_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.fsso.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "user_info_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.ldap.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"User-Info-Server '{value}' not found in "
                "user/ldap"
            )        
        return errors    
    async def validate_ssl_trusted_cert_references(self, client: Any) -> list[str]:
        """
        Validate ssl_trusted_cert references exist in FortiGate.
        
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
            >>> policy = FssoModel(
            ...     ssl_trusted_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_trusted_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.fsso.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssl_trusted_cert", None)
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
                f"Ssl-Trusted-Cert '{value}' not found in "
                "vpn/certificate/remote or vpn/certificate/ca"
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
            >>> policy = FssoModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.fsso.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_ldap_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_user_info_server_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssl_trusted_cert_references(client)
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
    "FssoModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.910056Z
# ============================================================================
"""
Pydantic Models for CMDB - user/domain_controller

Runtime validation models for user/domain_controller configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class DomainControllerExtraServer(BaseModel):
    """
    Child table model for extra-server.
    
    Extra servers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=100, default=0, description="Server ID.")    
    ip_address: str = Field(default="0.0.0.0", description="Domain controller IP address.")    
    port: int | None = Field(ge=0, le=65535, default=445, description="Port to be used for communication with the domain controller (default = 445).")    
    source_ip_address: str = Field(default="0.0.0.0", description="FortiGate IPv4 address to be used for communication with the domain controller.")    
    source_port: int | None = Field(ge=0, le=65535, default=0, description="Source port to be used for communication with the domain controller.")
class DomainControllerLdapServer(BaseModel):
    """
    Child table model for ldap-server.
    
    LDAP server name(s).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="LDAP server name.")  # datasource: ['user.ldap.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class DomainControllerModel(BaseModel):
    """
    Pydantic model for user/domain_controller configuration.
    
    Configure domain controller entries.
    
    Validation Rules:        - name: max_length=35 pattern=        - ad_mode: pattern=        - hostname: max_length=255 pattern=        - username: max_length=64 pattern=        - password: max_length=128 pattern=        - ip_address: pattern=        - ip6: pattern=        - port: min=0 max=65535 pattern=        - source_ip_address: pattern=        - source_ip6: pattern=        - source_port: min=0 max=65535 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - extra_server: pattern=        - domain_name: max_length=255 pattern=        - replication_port: min=0 max=65535 pattern=        - ldap_server: pattern=        - change_detection: pattern=        - change_detection_period: min=5 max=10080 pattern=        - dns_srv_lookup: pattern=        - adlds_dn: max_length=255 pattern=        - adlds_ip_address: pattern=        - adlds_ip6: pattern=        - adlds_port: min=0 max=65535 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Domain controller entry name.")    
    ad_mode: Literal["none", "ds", "lds"] | None = Field(default="none", description="Set Active Directory mode.")    
    hostname: str = Field(max_length=255, default="", description="Hostname of the server to connect to.")    
    username: str = Field(max_length=64, default="", description="User name to sign in with. Must have proper permissions for service.")    
    password: Any = Field(max_length=128, description="Password for specified username.")    
    ip_address: str | None = Field(default="0.0.0.0", description="Domain controller IPv4 address.")    
    ip6: str | None = Field(default="::", description="Domain controller IPv6 address.")    
    port: int | None = Field(ge=0, le=65535, default=445, description="Port to be used for communication with the domain controller (default = 445).")    
    source_ip_address: str | None = Field(default="0.0.0.0", description="FortiGate IPv4 address to be used for communication with the domain controller.")    
    source_ip6: str | None = Field(default="::", description="FortiGate IPv6 address to be used for communication with the domain controller.")    
    source_port: int | None = Field(ge=0, le=65535, default=0, description="Source port to be used for communication with the domain controller.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    extra_server: list[ExtraServer] = Field(default=None, description="Extra servers.")    
    domain_name: str | None = Field(max_length=255, default="", description="Domain DNS name.")    
    replication_port: int | None = Field(ge=0, le=65535, default=0, description="Port to be used for communication with the domain controller for replication service. Port number 0 indicates automatic discovery.")    
    ldap_server: list[LdapServer] = Field(default=None, description="LDAP server name(s).")    
    change_detection: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable detection of a configuration change in the Active Directory server.")    
    change_detection_period: int | None = Field(ge=5, le=10080, default=60, description="Minutes to detect a configuration change in the Active Directory server (5 - 10080 minutes (7 days), default = 60).")    
    dns_srv_lookup: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DNS service lookup.")    
    adlds_dn: str = Field(max_length=255, default="", description="AD LDS distinguished name.")    
    adlds_ip_address: str | None = Field(default="0.0.0.0", description="AD LDS IPv4 address.")    
    adlds_ip6: str | None = Field(default="::", description="AD LDS IPv6 address.")    
    adlds_port: int | None = Field(ge=0, le=65535, default=389, description="Port number of AD LDS service (default = 389).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
            >>> policy = DomainControllerModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.domain_controller.post(policy.to_fortios_dict())
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
            >>> policy = DomainControllerModel(
            ...     ldap_server=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ldap_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.domain_controller.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ldap_server", [])
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
            if await client.api.cmdb.user.ldap.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ldap-Server '{value}' not found in "
                    "user/ldap"
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
        
        errors = await self.validate_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ldap_server_references(client)
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
    "DomainControllerModel",    "DomainControllerExtraServer",    "DomainControllerLdapServer",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.857304Z
# ============================================================================
"""
Pydantic Models for CMDB - system/central_management

Runtime validation models for system/central_management configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class CentralManagementServerList(BaseModel):
    """
    Child table model for server-list.
    
    Additional severs that the FortiGate can use for updates (for AV, IPS, updates) and ratings (for web filter and antispam ratings) servers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    server_type: list[ServerType] = Field(default="", description="FortiGuard service type.")    
    addr_type: Literal["ipv4", "ipv6", "fqdn"] | None = Field(default="ipv4", description="Indicate whether the FortiGate communicates with the override server using an IPv4 address, an IPv6 address or a FQDN.")    
    server_address: str = Field(default="0.0.0.0", description="IPv4 address of override server.")    
    server_address6: str = Field(default="::", description="IPv6 address of override server.")    
    fqdn: str = Field(max_length=255, default="", description="FQDN address of override server.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class CentralManagementModel(BaseModel):
    """
    Pydantic model for system/central_management configuration.
    
    Configure central management.
    
    Validation Rules:        - mode: pattern=        - type: pattern=        - fortigate_cloud_sso_default_profile: max_length=35 pattern=        - schedule_config_restore: pattern=        - schedule_script_restore: pattern=        - allow_push_configuration: pattern=        - allow_push_firmware: pattern=        - allow_remote_firmware_upgrade: pattern=        - allow_monitor: pattern=        - serial_number: pattern=        - fmg: pattern=        - fmg_source_ip: pattern=        - fmg_source_ip6: pattern=        - local_cert: max_length=35 pattern=        - ca_cert: pattern=        - vdom: max_length=31 pattern=        - server_list: pattern=        - fmg_update_port: pattern=        - fmg_update_http_header: pattern=        - include_default_servers: pattern=        - enc_algorithm: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    mode: Literal["normal", "backup"] | None = Field(default="normal", description="Central management mode.")    
    type: Literal["fortimanager", "fortiguard", "none"] | None = Field(default="fortiguard", description="Central management type.")    
    fortigate_cloud_sso_default_profile: str | None = Field(max_length=35, default="", description="Override access profile. Permission is set to read-only without a FortiGate Cloud Central Management license.")  # datasource: ['system.accprofile.name']    
    schedule_config_restore: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allowing the central management server to restore the configuration of this FortiGate.")    
    schedule_script_restore: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allowing the central management server to restore the scripts stored on this FortiGate.")    
    allow_push_configuration: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allowing the central management server to push configuration changes to this FortiGate.")    
    allow_push_firmware: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allowing the central management server to push firmware updates to this FortiGate.")    
    allow_remote_firmware_upgrade: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable remotely upgrading the firmware on this FortiGate from the central management server.")    
    allow_monitor: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allowing the central management server to remotely monitor this FortiGate unit.")    
    serial_number: str | None = Field(default="", description="Serial number.")    
    fmg: str | None = Field(default="", description="IP address or FQDN of the FortiManager.")    
    fmg_source_ip: str | None = Field(default="0.0.0.0", description="IPv4 source address that this FortiGate uses when communicating with FortiManager.")    
    fmg_source_ip6: str | None = Field(default="::", description="IPv6 source address that this FortiGate uses when communicating with FortiManager.")    
    local_cert: str | None = Field(max_length=35, default="", description="Certificate to be used by FGFM protocol.")  # datasource: ['certificate.local.name']    
    ca_cert: str | None = Field(default="", description="CA certificate to be used by FGFM protocol.")  # datasource: ['certificate.ca.name']    
    vdom: str | None = Field(max_length=31, default="root", description="Virtual domain (VDOM) name to use when communicating with FortiManager.")  # datasource: ['system.vdom.name']    
    server_list: list[ServerList] = Field(default=None, description="Additional severs that the FortiGate can use for updates (for AV, IPS, updates) and ratings (for web filter and antispam ratings) servers.")    
    fmg_update_port: Literal["8890", "443"] | None = Field(default="8890", description="Port used to communicate with FortiManager that is acting as a FortiGuard update server.")    
    fmg_update_http_header: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable inclusion of HTTP header in update request.")    
    include_default_servers: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable inclusion of public FortiGuard servers in the override server list.")    
    enc_algorithm: Literal["default", "high", "low"] | None = Field(default="high", description="Encryption strength for communications between the FortiGate and central management.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('fortigate_cloud_sso_default_profile')
    @classmethod
    def validate_fortigate_cloud_sso_default_profile(cls, v: Any) -> Any:
        """
        Validate fortigate_cloud_sso_default_profile field.
        
        Datasource: ['system.accprofile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('local_cert')
    @classmethod
    def validate_local_cert(cls, v: Any) -> Any:
        """
        Validate local_cert field.
        
        Datasource: ['certificate.local.name']
        
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
        
        Datasource: ['certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('vdom')
    @classmethod
    def validate_vdom(cls, v: Any) -> Any:
        """
        Validate vdom field.
        
        Datasource: ['system.vdom.name']
        
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
    async def validate_fortigate_cloud_sso_default_profile_references(self, client: Any) -> list[str]:
        """
        Validate fortigate_cloud_sso_default_profile references exist in FortiGate.
        
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
            >>> policy = CentralManagementModel(
            ...     fortigate_cloud_sso_default_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fortigate_cloud_sso_default_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.central_management.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fortigate_cloud_sso_default_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.accprofile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fortigate-Cloud-Sso-Default-Profile '{value}' not found in "
                "system/accprofile"
            )        
        return errors    
    async def validate_local_cert_references(self, client: Any) -> list[str]:
        """
        Validate local_cert references exist in FortiGate.
        
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
            >>> policy = CentralManagementModel(
            ...     local_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_local_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.central_management.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "local_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Local-Cert '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_ca_cert_references(self, client: Any) -> list[str]:
        """
        Validate ca_cert references exist in FortiGate.
        
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
            >>> policy = CentralManagementModel(
            ...     ca_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ca_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.central_management.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ca_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ca-Cert '{value}' not found in "
                "certificate/ca"
            )        
        return errors    
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
            >>> policy = CentralManagementModel(
            ...     vdom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.central_management.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vdom", None)
        if not value:
            return errors
        
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
            >>> policy = CentralManagementModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.central_management.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_fortigate_cloud_sso_default_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_local_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ca_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vdom_references(client)
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
    "CentralManagementModel",    "CentralManagementServerList",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.106359Z
# ============================================================================
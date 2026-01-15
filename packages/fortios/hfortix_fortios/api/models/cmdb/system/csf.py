"""
Pydantic Models for CMDB - system/csf

Runtime validation models for system/csf configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class CsfTrustedList(BaseModel):
    """
    Child table model for trusted-list.
    
    Pre-authorized and blocked security fabric nodes.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="", description="Name.")    
    authorization_type: Literal["serial", "certificate"] | None = Field(default="serial", description="Authorization type.")    
    serial: str | None = Field(max_length=19, default="", description="Serial.")    
    certificate: str | None = Field(max_length=32767, default=None, description="Certificate.")    
    action: Literal["accept", "deny"] | None = Field(default="accept", description="Security fabric authorization action.")    
    ha_members: list[HaMembers] = Field(max_length=19, default="", description="HA members.")    
    downstream_authorization: Literal["enable", "disable"] | None = Field(default="disable", description="Trust authorizations by this node's administrator.")    
    index: int | None = Field(ge=1, le=1024, default=0, description="Index of the downstream in tree.")
class CsfFabricConnector(BaseModel):
    """
    Child table model for fabric-connector.
    
    Fabric connector configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    serial: str | None = Field(max_length=19, default="", description="Serial.")    
    accprofile: str | None = Field(max_length=35, default="", description="Override access profile.")  # datasource: ['system.accprofile.name']    
    configuration_write_access: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable downstream device write access to configuration.")    
    vdom: list[Vdom] = Field(default=None, description="Virtual domains that the connector has access to. If none are set, the connector will only have access to the VDOM that it joins the Security Fabric through.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class CsfModel(BaseModel):
    """
    Pydantic model for system/csf configuration.
    
    Add this FortiGate to a Security Fabric or set up a new Security Fabric on this FortiGate.
    
    Validation Rules:        - status: pattern=        - uid: max_length=35 pattern=        - upstream: max_length=255 pattern=        - source_ip: pattern=        - upstream_interface_select_method: pattern=        - upstream_interface: max_length=15 pattern=        - upstream_port: min=1 max=65535 pattern=        - group_name: max_length=35 pattern=        - group_password: max_length=128 pattern=        - accept_auth_by_cert: pattern=        - log_unification: pattern=        - authorization_request_type: pattern=        - certificate: max_length=35 pattern=        - fabric_workers: min=1 max=4 pattern=        - downstream_access: pattern=        - legacy_authentication: pattern=        - downstream_accprofile: max_length=35 pattern=        - configuration_sync: pattern=        - fabric_object_unification: pattern=        - saml_configuration_sync: pattern=        - trusted_list: pattern=        - fabric_connector: pattern=        - forticloud_account_enforcement: pattern=        - file_mgmt: pattern=        - file_quota: min=0 max=4294967295 pattern=        - file_quota_warning: min=1 max=99 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable Security Fabric.")    
    uid: str | None = Field(max_length=35, default="", description="Unique ID of the current CSF node")    
    upstream: str | None = Field(max_length=255, default="", description="IP/FQDN of the FortiGate upstream from this FortiGate in the Security Fabric.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address for communication with the upstream FortiGate.")    
    upstream_interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    upstream_interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    upstream_port: int | None = Field(ge=1, le=65535, default=8013, description="The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric (default = 8013).")    
    group_name: str | None = Field(max_length=35, default="", description="Security Fabric group name. All FortiGates in a Security Fabric must have the same group name.")    
    group_password: Any = Field(max_length=128, default=None, description="Security Fabric group password. For legacy authentication, fabric members must have the same group password.")    
    accept_auth_by_cert: Literal["disable", "enable"] | None = Field(default="enable", description="Accept connections with unknown certificates and ask admin for approval.")    
    log_unification: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable broadcast of discovery messages for log unification.")    
    authorization_request_type: Literal["serial", "certificate"] | None = Field(default="serial", description="Authorization request type.")    
    certificate: str | None = Field(max_length=35, default="", description="Certificate.")  # datasource: ['certificate.local.name']    
    fabric_workers: int | None = Field(ge=1, le=4, default=2, description="Number of worker processes for Security Fabric daemon.")    
    downstream_access: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable downstream device access to this device's configuration and data.")    
    legacy_authentication: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable legacy authentication.")    
    downstream_accprofile: str = Field(max_length=35, default="", description="Default access profile for requests from downstream devices.")  # datasource: ['system.accprofile.name']    
    configuration_sync: Literal["default", "local"] = Field(default="default", description="Configuration sync mode.")    
    fabric_object_unification: Literal["default", "local"] | None = Field(default="default", description="Fabric CMDB Object Unification.")    
    saml_configuration_sync: Literal["default", "local"] | None = Field(default="default", description="SAML setting configuration synchronization.")    
    trusted_list: list[TrustedList] = Field(default=None, description="Pre-authorized and blocked security fabric nodes.")    
    fabric_connector: list[FabricConnector] = Field(default=None, description="Fabric connector configuration.")    
    forticloud_account_enforcement: Literal["enable", "disable"] | None = Field(default="enable", description="Fabric FortiCloud account unification.")    
    file_mgmt: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Security Fabric daemon file management.")    
    file_quota: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum amount of memory that can be used by the daemon files (in bytes).")    
    file_quota_warning: int | None = Field(ge=1, le=99, default=90, description="Warn when the set percentage of quota has been used.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('upstream_interface')
    @classmethod
    def validate_upstream_interface(cls, v: Any) -> Any:
        """
        Validate upstream_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certificate')
    @classmethod
    def validate_certificate(cls, v: Any) -> Any:
        """
        Validate certificate field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('downstream_accprofile')
    @classmethod
    def validate_downstream_accprofile(cls, v: Any) -> Any:
        """
        Validate downstream_accprofile field.
        
        Datasource: ['system.accprofile.name']
        
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
    async def validate_upstream_interface_references(self, client: Any) -> list[str]:
        """
        Validate upstream_interface references exist in FortiGate.
        
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
            >>> policy = CsfModel(
            ...     upstream_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_upstream_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.csf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "upstream_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Upstream-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_certificate_references(self, client: Any) -> list[str]:
        """
        Validate certificate references exist in FortiGate.
        
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
            >>> policy = CsfModel(
            ...     certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.csf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Certificate '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_downstream_accprofile_references(self, client: Any) -> list[str]:
        """
        Validate downstream_accprofile references exist in FortiGate.
        
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
            >>> policy = CsfModel(
            ...     downstream_accprofile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_downstream_accprofile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.csf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "downstream_accprofile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.accprofile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Downstream-Accprofile '{value}' not found in "
                "system/accprofile"
            )        
        return errors    
    async def validate_fabric_connector_references(self, client: Any) -> list[str]:
        """
        Validate fabric_connector references exist in FortiGate.
        
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
            >>> policy = CsfModel(
            ...     fabric_connector=[{"accprofile": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fabric_connector_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.csf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "fabric_connector", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("accprofile")
            else:
                value = getattr(item, "accprofile", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.accprofile.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Fabric-Connector '{value}' not found in "
                    "system/accprofile"
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
        
        errors = await self.validate_upstream_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_downstream_accprofile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fabric_connector_references(client)
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
    "CsfModel",    "CsfTrustedList",    "CsfFabricConnector",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.524260Z
# ============================================================================
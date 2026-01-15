"""
Pydantic Models for CMDB - endpoint_control/fctems

Runtime validation models for endpoint_control/fctems configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class FctemsCapabilitiesEnum(str, Enum):
    """Allowed values for capabilities field."""
    FABRIC_AUTH = "fabric-auth"    SILENT_APPROVAL = "silent-approval"    WEBSOCKET = "websocket"    WEBSOCKET_MALWARE = "websocket-malware"    PUSH_CA_CERTS = "push-ca-certs"    COMMON_TAGS_API = "common-tags-api"    TENANT_ID = "tenant-id"    CLIENT_AVATARS = "client-avatars"    SINGLE_VDOM_CONNECTOR = "single-vdom-connector"    FGT_SYSINFO_API = "fgt-sysinfo-api"    ZTNA_SERVER_INFO = "ztna-server-info"    USED_TAGS = "used-tags"

# ============================================================================
# Main Model
# ============================================================================

class FctemsModel(BaseModel):
    """
    Pydantic model for endpoint_control/fctems configuration.
    
    Configure FortiClient Enterprise Management Server (EMS) entries.
    
    Validation Rules:        - ems_id: min=1 max=7 pattern=        - status: pattern=        - name: max_length=35 pattern=        - dirty_reason: pattern=        - fortinetone_cloud_authentication: pattern=        - cloud_authentication_access_key: max_length=20 pattern=        - server: max_length=255 pattern=        - https_port: min=1 max=65535 pattern=        - serial_number: max_length=16 pattern=        - tenant_id: max_length=32 pattern=        - source_ip: pattern=        - pull_sysinfo: pattern=        - pull_vulnerabilities: pattern=        - pull_tags: pattern=        - pull_malware_hash: pattern=        - capabilities: pattern=        - call_timeout: min=1 max=180 pattern=        - out_of_sync_threshold: min=10 max=3600 pattern=        - send_tags_to_all_vdoms: pattern=        - websocket_override: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - trust_ca_cn: pattern=        - verifying_ca: max_length=79 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    ems_id: int | None = Field(ge=1, le=7, default=0, description="EMS ID in order (1 - 7).")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable or disable this EMS configuration.")    
    name: str | None = Field(max_length=35, default="", description="FortiClient Enterprise Management Server (EMS) name.")    
    dirty_reason: Literal["none", "mismatched-ems-sn"] | None = Field(default="none", description="Dirty Reason for FortiClient EMS.")    
    fortinetone_cloud_authentication: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.")    
    cloud_authentication_access_key: Any = Field(max_length=20, default=None, description="FortiClient EMS Cloud multitenancy access key")    
    server: str | None = Field(max_length=255, default="", description="FortiClient EMS FQDN or IPv4 address.")    
    https_port: int | None = Field(ge=1, le=65535, default=443, description="FortiClient EMS HTTPS access port number. (1 - 65535, default: 443).")    
    serial_number: str | None = Field(max_length=16, default="", description="EMS Serial Number.")    
    tenant_id: str | None = Field(max_length=32, default="", description="EMS Tenant ID.")    
    source_ip: str | None = Field(default="0.0.0.0", description="REST API call source IP.")    
    pull_sysinfo: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable pulling SysInfo from EMS.")    
    pull_vulnerabilities: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable pulling vulnerabilities from EMS.")    
    pull_tags: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable pulling FortiClient user tags from EMS.")    
    pull_malware_hash: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable pulling FortiClient malware hash from EMS.")    
    capabilities: list[Capabilities] = Field(default="", description="List of EMS capabilities.")    
    call_timeout: int | None = Field(ge=1, le=180, default=30, description="FortiClient EMS call timeout in seconds (1 - 180 seconds, default = 30).")    
    out_of_sync_threshold: int | None = Field(ge=10, le=3600, default=180, description="Outdated resource threshold in seconds (10 - 3600, default = 180).")    
    send_tags_to_all_vdoms: Literal["enable", "disable"] | None = Field(default="disable", description="Relax restrictions on tags to send all EMS tags to all VDOMs")    
    websocket_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable override behavior for how this FortiGate unit connects to EMS using a WebSocket connection.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    trust_ca_cn: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable trust of the EMS certificate issuer(CA) and common name(CN) for certificate auto-renewal.")    
    verifying_ca: str | None = Field(max_length=79, default="", description="Lowest CA cert on Fortigate in verified EMS cert chain.")  # datasource: ['certificate.ca.name', 'vpn.certificate.ca.name']    
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
    @field_validator('verifying_ca')
    @classmethod
    def validate_verifying_ca(cls, v: Any) -> Any:
        """
        Validate verifying_ca field.
        
        Datasource: ['certificate.ca.name', 'vpn.certificate.ca.name']
        
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
            >>> policy = FctemsModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.endpoint_control.fctems.post(policy.to_fortios_dict())
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
    async def validate_verifying_ca_references(self, client: Any) -> list[str]:
        """
        Validate verifying_ca references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/ca        - vpn/certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FctemsModel(
            ...     verifying_ca="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_verifying_ca_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.endpoint_control.fctems.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "verifying_ca", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.ca.exists(value):
            found = True
        elif await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Verifying-Ca '{value}' not found in "
                "certificate/ca or vpn/certificate/ca"
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
        errors = await self.validate_verifying_ca_references(client)
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
    "FctemsModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.247614Z
# ============================================================================
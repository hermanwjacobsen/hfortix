"""
Pydantic Models for CMDB - system/external_resource

Runtime validation models for system/external_resource configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum
from uuid import UUID

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExternalResourceTypeEnum(str, Enum):
    """Allowed values for type field."""
    CATEGORY = "category"    DOMAIN = "domain"    MALWARE = "malware"    ADDRESS = "address"    MAC_ADDRESS = "mac-address"    DATA = "data"    GENERIC_ADDRESS = "generic-address"

# ============================================================================
# Main Model
# ============================================================================

class ExternalResourceModel(BaseModel):
    """
    Pydantic model for system/external_resource configuration.
    
    Configure external resource.
    
    Validation Rules:        - name: max_length=35 pattern=        - uuid: pattern=        - status: pattern=        - type: pattern=        - namespace: max_length=15 pattern=        - object_array_path: max_length=511 pattern=        - address_name_field: max_length=511 pattern=        - address_data_field: max_length=511 pattern=        - address_comment_field: max_length=511 pattern=        - update_method: pattern=        - category: min=192 max=221 pattern=        - username: max_length=64 pattern=        - password: pattern=        - client_cert_auth: pattern=        - client_cert: max_length=79 pattern=        - comments: max_length=255 pattern=        - resource: max_length=511 pattern=        - user_agent: max_length=255 pattern=        - server_identity_check: pattern=        - refresh_rate: min=1 max=43200 pattern=        - source_ip: pattern=        - source_ip_interface: max_length=15 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="External resource name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable user resource.")    
    type: TypeEnum | None = Field(default="category", description="User resource type.")    
    namespace: str | None = Field(max_length=15, default="", description="Generic external connector address namespace.")    
    object_array_path: str | None = Field(max_length=511, default="$.addresses", description="JSON Path to array of generic addresses in resource.")    
    address_name_field: str | None = Field(max_length=511, default="$.name", description="JSON Path to address name in generic address entry.")    
    address_data_field: str | None = Field(max_length=511, default="$.value", description="JSON Path to address data in generic address entry.")    
    address_comment_field: str | None = Field(max_length=511, default="$.description", description="JSON Path to address description in generic address entry.")    
    update_method: Literal["feed", "push"] | None = Field(default="feed", description="External resource update method.")    
    category: int | None = Field(ge=192, le=221, default=0, description="User resource category.")    
    username: str | None = Field(max_length=64, default="", description="HTTP basic authentication user name.")    
    password: Any = Field(default=None, description="HTTP basic authentication password.")    
    client_cert_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable using client certificate for TLS authentication.")    
    client_cert: str | None = Field(max_length=79, default="", description="Client certificate name.")  # datasource: ['vpn.certificate.local.name']    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    resource: str = Field(max_length=511, default="", description="URL of external resource.")    
    user_agent: str | None = Field(max_length=255, default=None, description="HTTP User-Agent header (default = 'curl/7.58.0').")    
    server_identity_check: Literal["none", "basic", "full"] | None = Field(default="none", description="Certificate verification option.")    
    refresh_rate: int = Field(ge=1, le=43200, default=5, description="Time interval to refresh external resource (1 - 43200 min, default = 5 min).")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IPv4 address used to communicate with server.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="IPv4 Source interface for communication with the server.")  # datasource: ['system.interface.name']    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
            >>> policy = ExternalResourceModel(
            ...     client_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_client_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.external_resource.post(policy.to_fortios_dict())
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
            >>> policy = ExternalResourceModel(
            ...     source_ip_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_source_ip_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.external_resource.post(policy.to_fortios_dict())
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
            >>> policy = ExternalResourceModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.external_resource.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_client_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_source_ip_interface_references(client)
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
    "ExternalResourceModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.367920Z
# ============================================================================
"""
Pydantic Models for CMDB - system/fortisandbox

Runtime validation models for system/fortisandbox configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class FortisandboxSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"

# ============================================================================
# Main Model
# ============================================================================

class FortisandboxModel(BaseModel):
    """
    Pydantic model for system/fortisandbox configuration.
    
    Configure FortiSandbox.
    
    Validation Rules:        - status: pattern=        - forticloud: pattern=        - inline_scan: pattern=        - server: max_length=63 pattern=        - source_ip: max_length=63 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - enc_algorithm: pattern=        - ssl_min_proto_version: pattern=        - email: max_length=63 pattern=        - ca: max_length=79 pattern=        - cn: max_length=127 pattern=        - certificate_verification: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiSandbox.")    
    forticloud: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiSandbox Cloud.")    
    inline_scan: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiSandbox inline scan.")    
    server: str = Field(max_length=63, default="", description="Server IP address or FQDN of the remote FortiSandbox.")    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address for communications to FortiSandbox.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    enc_algorithm: Literal["default", "high", "low"] | None = Field(default="default", description="Configure the level of SSL protection for secure communication with FortiSandbox.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    email: str | None = Field(max_length=63, default="", description="Notifier email address.")    
    ca: str | None = Field(max_length=79, default="", description="The CA that signs remote FortiSandbox certificate, empty for no check.")  # datasource: ['vpn.certificate.ca.name']    
    cn: str | None = Field(max_length=127, default="", description="The CN of remote server certificate, case sensitive, empty for no check.")    
    certificate_verification: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable identity verification of FortiSandbox by use of certificate.")    
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
    @field_validator('ca')
    @classmethod
    def validate_ca(cls, v: Any) -> Any:
        """
        Validate ca field.
        
        Datasource: ['vpn.certificate.ca.name']
        
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
            >>> policy = FortisandboxModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fortisandbox.post(policy.to_fortios_dict())
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
    async def validate_ca_references(self, client: Any) -> list[str]:
        """
        Validate ca references exist in FortiGate.
        
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
            >>> policy = FortisandboxModel(
            ...     ca="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ca_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fortisandbox.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ca", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ca '{value}' not found in "
                "vpn/certificate/ca"
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
        errors = await self.validate_ca_references(client)
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
    "FortisandboxModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.399657Z
# ============================================================================
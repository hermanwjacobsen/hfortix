"""
Pydantic Models for CMDB - system/sdn_vpn

Runtime validation models for system/sdn_vpn configuration.
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

class SdnVpnModel(BaseModel):
    """
    Pydantic model for system/sdn_vpn configuration.
    
    Configure public cloud VPN service.
    
    Validation Rules:        - name: max_length=35 pattern=        - sdn: max_length=35 pattern=        - remote_type: pattern=        - routing_type: pattern=        - vgw_id: max_length=63 pattern=        - tgw_id: max_length=63 pattern=        - subnet_id: max_length=63 pattern=        - bgp_as: min=1 max=4294967295 pattern=        - cgw_gateway: pattern=        - nat_traversal: pattern=        - tunnel_interface: max_length=15 pattern=        - internal_interface: max_length=15 pattern=        - local_cidr: pattern=        - remote_cidr: pattern=        - cgw_name: max_length=35 pattern=        - psksecret: pattern=        - type: min=0 max=65535 pattern=        - status: min=0 max=255 pattern=        - code: min=0 max=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Public cloud VPN name.")    
    sdn: str = Field(max_length=35, default="", description="SDN connector name.")  # datasource: ['system.sdn-connector.name']    
    remote_type: Literal["vgw", "tgw"] = Field(default="vgw", description="Type of remote device.")    
    routing_type: Literal["static", "dynamic"] = Field(default="dynamic", description="Type of routing.")    
    vgw_id: str = Field(max_length=63, default="", description="Virtual private gateway id.")    
    tgw_id: str = Field(max_length=63, default="", description="Transit gateway id.")    
    subnet_id: str | None = Field(max_length=63, default="", description="AWS subnet id for TGW route propagation.")    
    bgp_as: int = Field(ge=1, le=4294967295, default=65000, description="BGP Router AS number.")    
    cgw_gateway: str = Field(default="0.0.0.0", description="Public IP address of the customer gateway.")    
    nat_traversal: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable use for NAT traversal. Please enable if your FortiGate device is behind a NAT/PAT device.")    
    tunnel_interface: str = Field(max_length=15, default="", description="Tunnel interface with public IP.")  # datasource: ['system.interface.name']    
    internal_interface: str = Field(max_length=15, default="", description="Internal interface with local subnet.")  # datasource: ['system.interface.name']    
    local_cidr: str = Field(default="0.0.0.0 0.0.0.0", description="Local subnet address and subnet mask.")    
    remote_cidr: str = Field(default="0.0.0.0 0.0.0.0", description="Remote subnet address and subnet mask.")    
    cgw_name: str | None = Field(max_length=35, default="", description="AWS customer gateway name to be created.")    
    psksecret: Any = Field(default=None, description="Pre-shared secret for PSK authentication. Auto-generated if not specified")    
    type: int | None = Field(ge=0, le=65535, default=0, description="SDN VPN type.")    
    status: int | None = Field(ge=0, le=255, default=0, description="SDN VPN status.")    
    code: int | None = Field(ge=0, le=255, default=0, description="SDN VPN error code.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('sdn')
    @classmethod
    def validate_sdn(cls, v: Any) -> Any:
        """
        Validate sdn field.
        
        Datasource: ['system.sdn-connector.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('tunnel_interface')
    @classmethod
    def validate_tunnel_interface(cls, v: Any) -> Any:
        """
        Validate tunnel_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('internal_interface')
    @classmethod
    def validate_internal_interface(cls, v: Any) -> Any:
        """
        Validate internal_interface field.
        
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
    async def validate_sdn_references(self, client: Any) -> list[str]:
        """
        Validate sdn references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdn-connector        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SdnVpnModel(
            ...     sdn="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sdn_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdn_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "sdn", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.sdn-connector.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Sdn '{value}' not found in "
                "system/sdn-connector"
            )        
        return errors    
    async def validate_tunnel_interface_references(self, client: Any) -> list[str]:
        """
        Validate tunnel_interface references exist in FortiGate.
        
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
            >>> policy = SdnVpnModel(
            ...     tunnel_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tunnel_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdn_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "tunnel_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Tunnel-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_internal_interface_references(self, client: Any) -> list[str]:
        """
        Validate internal_interface references exist in FortiGate.
        
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
            >>> policy = SdnVpnModel(
            ...     internal_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_internal_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.sdn_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "internal_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Internal-Interface '{value}' not found in "
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
        
        errors = await self.validate_sdn_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_tunnel_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_internal_interface_references(client)
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
    "SdnVpnModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.360784Z
# ============================================================================
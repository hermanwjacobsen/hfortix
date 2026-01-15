"""
Pydantic Models for CMDB - web_proxy/isolator_server

Runtime validation models for web_proxy/isolator_server configuration.
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

class IsolatorServerModel(BaseModel):
    """
    Pydantic model for web_proxy/isolator_server configuration.
    
    Configure forward-server addresses.
    
    Validation Rules:        - name: max_length=63 pattern=        - addr_type: pattern=        - ip: pattern=        - ipv6: pattern=        - fqdn: max_length=255 pattern=        - port: min=1 max=65535 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - comment: max_length=63 pattern=        - masquerade: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Server name.")    
    addr_type: Literal["ip", "ipv6", "fqdn"] | None = Field(default="ip", description="Address type of the forwarding proxy server: IP or FQDN.")    
    ip: str | None = Field(default="0.0.0.0", description="Forward proxy server IP address.")    
    ipv6: str | None = Field(default="::", description="Forward proxy server IPv6 address.")    
    fqdn: str | None = Field(max_length=255, default="", description="Forward server Fully Qualified Domain Name (FQDN).")    
    port: int | None = Field(ge=1, le=65535, default=3128, description="Port number that the forwarding server expects to receive HTTP sessions on (1 - 65535, default = 3128).")    
    interface_select_method: Literal["sdwan", "specify"] | None = Field(default="sdwan", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=-1, description="VRF ID used for connection to server.")    
    comment: str | None = Field(max_length=63, default="", description="Comment.")    
    masquerade: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of the IP address of the outgoing interface as the client IP address (default = enable)")    
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
            >>> policy = IsolatorServerModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.web_proxy.isolator_server.post(policy.to_fortios_dict())
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
    "IsolatorServerModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.835580Z
# ============================================================================
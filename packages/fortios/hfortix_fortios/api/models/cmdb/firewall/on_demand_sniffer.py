"""
Pydantic Models for CMDB - firewall/on_demand_sniffer

Runtime validation models for firewall/on_demand_sniffer configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class OnDemandSnifferHosts(BaseModel):
    """
    Child table model for hosts.
    
    IPv4 or IPv6 hosts to filter in this traffic sniffer.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    host: str = Field(max_length=255, default="", description="IPv4 or IPv6 host.")
class OnDemandSnifferPorts(BaseModel):
    """
    Child table model for ports.
    
    Ports to filter for in this traffic sniffer.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    port: int = Field(ge=1, le=65536, default=0, description="Port to filter in this traffic sniffer.")
class OnDemandSnifferProtocols(BaseModel):
    """
    Child table model for protocols.
    
    Protocols to filter in this traffic sniffer.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    protocol: int = Field(ge=0, le=255, default=0, description="Integer value for the protocol type as defined by IANA (0 - 255).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class OnDemandSnifferModel(BaseModel):
    """
    Pydantic model for firewall/on_demand_sniffer configuration.
    
    Configure on-demand packet sniffer.
    
    Validation Rules:        - name: max_length=35 pattern=        - interface: max_length=35 pattern=        - max_packet_count: min=1 max=20000 pattern=        - hosts: pattern=        - ports: pattern=        - protocols: pattern=        - non_ip_packet: pattern=        - advanced_filter: max_length=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="On-demand packet sniffer name.")    
    interface: str = Field(max_length=35, default="", description="Interface name that on-demand packet sniffer will take place.")  # datasource: ['system.interface.name']    
    max_packet_count: int = Field(ge=1, le=20000, default=0, description="Maximum number of packets to capture per on-demand packet sniffer.")    
    hosts: list[Hosts] = Field(default=None, description="IPv4 or IPv6 hosts to filter in this traffic sniffer.")    
    ports: list[Ports] = Field(default=None, description="Ports to filter for in this traffic sniffer.")    
    protocols: list[Protocols] = Field(default=None, description="Protocols to filter in this traffic sniffer.")    
    non_ip_packet: Literal["enable", "disable"] | None = Field(default="disable", description="Include non-IP packets.")    
    advanced_filter: str | None = Field(max_length=255, default=None, description="Advanced freeform filter that will be used over existing filter settings if set. Can only be used by super admin.")    
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
            >>> policy = OnDemandSnifferModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.on_demand_sniffer.post(policy.to_fortios_dict())
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
    "OnDemandSnifferModel",    "OnDemandSnifferHosts",    "OnDemandSnifferPorts",    "OnDemandSnifferProtocols",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.766937Z
# ============================================================================
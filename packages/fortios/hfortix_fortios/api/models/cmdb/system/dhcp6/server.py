"""
Pydantic Models for CMDB - system/dhcp6/server

Runtime validation models for system/dhcp6/server configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ServerOptions(BaseModel):
    """
    Child table model for options.
    
    DHCPv6 options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    code: int = Field(ge=0, le=255, default=0, description="DHCPv6 option code.")    
    type: TypeEnum | None = Field(default="hex", description="DHCPv6 option type.")    
    value: str | None = Field(max_length=312, default="", description="DHCPv6 option value (hexadecimal value must be even).")    
    ip6: list[Ip6] = Field(default="", description="DHCP option IP6s.")    
    vci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable vendor class option matching. When enabled only DHCP requests with a matching VCI are served with this option.")    
    vci_string: list[VciString] = Field(default=None, description="One or more VCI strings in quotes separated by spaces.")
class ServerPrefixRange(BaseModel):
    """
    Child table model for prefix-range.
    
    DHCP prefix configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    start_prefix: str = Field(default="::", description="Start of prefix range.")    
    end_prefix: str = Field(default="::", description="End of prefix range.")    
    prefix_length: int = Field(ge=1, le=128, default=0, description="Prefix length.")
class ServerIpRange(BaseModel):
    """
    Child table model for ip-range.
    
    DHCP IP range configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    start_ip: str = Field(default="::", description="Start of IP range.")    
    end_ip: str = Field(default="::", description="End of IP range.")    
    vci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable vendor class option matching. When enabled only DHCP requests with a matching VC are served with this range.")    
    vci_string: list[VciString] = Field(default=None, description="One or more VCI strings in quotes separated by spaces.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ServerModel(BaseModel):
    """
    Pydantic model for system/dhcp6/server configuration.
    
    Configure DHCPv6 servers.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - status: pattern=        - rapid_commit: pattern=        - lease_time: min=300 max=8640000 pattern=        - dns_service: pattern=        - dns_search_list: pattern=        - dns_server1: pattern=        - dns_server2: pattern=        - dns_server3: pattern=        - dns_server4: pattern=        - domain: max_length=35 pattern=        - subnet: pattern=        - interface: max_length=15 pattern=        - delegated_prefix_route: pattern=        - options: pattern=        - upstream_interface: max_length=15 pattern=        - delegated_prefix_iaid: min=0 max=4294967295 pattern=        - ip_mode: pattern=        - prefix_mode: pattern=        - prefix_range: pattern=        - ip_range: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable this DHCPv6 configuration.")    
    rapid_commit: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allow/disallow rapid commit.")    
    lease_time: int | None = Field(ge=300, le=8640000, default=604800, description="Lease time in seconds, 0 means unlimited.")    
    dns_service: Literal["delegated", "default", "specify"] | None = Field(default="specify", description="Options for assigning DNS servers to DHCPv6 clients.")    
    dns_search_list: Literal["delegated", "specify"] | None = Field(default="specify", description="DNS search list options.")    
    dns_server1: str | None = Field(default="::", description="DNS server 1.")    
    dns_server2: str | None = Field(default="::", description="DNS server 2.")    
    dns_server3: str | None = Field(default="::", description="DNS server 3.")    
    dns_server4: str | None = Field(default="::", description="DNS server 4.")    
    domain: str | None = Field(max_length=35, default="", description="Domain name suffix for the IP addresses that the DHCP server assigns to clients.")    
    subnet: str = Field(default="::/0", description="Subnet or subnet-id if the IP mode is delegated.")    
    interface: str = Field(max_length=15, default="", description="DHCP server can assign IP configurations to clients connected to this interface.")  # datasource: ['system.interface.name']    
    delegated_prefix_route: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable automatically adding of routing for delegated prefix.")    
    options: list[Options] = Field(default=None, description="DHCPv6 options.")    
    upstream_interface: str = Field(max_length=15, default="", description="Interface name from where delegated information is provided.")  # datasource: ['system.interface.name']    
    delegated_prefix_iaid: int = Field(ge=0, le=4294967295, default=0, description="IAID of obtained delegated-prefix from the upstream interface.")    
    ip_mode: Literal["range", "delegated"] | None = Field(default="range", description="Method used to assign client IP.")    
    prefix_mode: Literal["dhcp6", "ra"] | None = Field(default="dhcp6", description="Assigning a prefix from a DHCPv6 client or RA.")    
    prefix_range: list[PrefixRange] = Field(default=None, description="DHCP prefix configuration.")    
    ip_range: list[IpRange] = Field(default=None, description="DHCP IP range configuration.")    
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
            >>> policy = ServerModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dhcp6.server.post(policy.to_fortios_dict())
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
            >>> policy = ServerModel(
            ...     upstream_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_upstream_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dhcp6.server.post(policy.to_fortios_dict())
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
        errors = await self.validate_upstream_interface_references(client)
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
    "ServerModel",    "ServerOptions",    "ServerPrefixRange",    "ServerIpRange",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.799931Z
# ============================================================================
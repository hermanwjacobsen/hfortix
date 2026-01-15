"""
Pydantic Models for CMDB - firewall/ippool

Runtime validation models for firewall/ippool configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class IppoolTypeEnum(str, Enum):
    """Allowed values for type field."""
    OVERLOAD = "overload"    ONE_TO_ONE = "one-to-one"    FIXED_PORT_RANGE = "fixed-port-range"    PORT_BLOCK_ALLOCATION = "port-block-allocation"

# ============================================================================
# Main Model
# ============================================================================

class IppoolModel(BaseModel):
    """
    Pydantic model for firewall/ippool configuration.
    
    Configure IPv4 IP pools.
    
    Validation Rules:        - name: max_length=79 pattern=        - type: pattern=        - startip: pattern=        - endip: pattern=        - startport: min=1024 max=65535 pattern=        - endport: min=1024 max=65535 pattern=        - source_startip: pattern=        - source_endip: pattern=        - block_size: min=64 max=4096 pattern=        - port_per_user: min=32 max=60417 pattern=        - num_blocks_per_user: min=1 max=128 pattern=        - pba_timeout: min=3 max=86400 pattern=        - pba_interim_log: min=600 max=86400 pattern=        - permit_any_host: pattern=        - arp_reply: pattern=        - arp_intf: max_length=15 pattern=        - associated_interface: max_length=15 pattern=        - comments: max_length=255 pattern=        - nat64: pattern=        - add_nat64_route: pattern=        - source_prefix6: pattern=        - client_prefix_length: min=1 max=128 pattern=        - tcp_session_quota: min=0 max=2097000 pattern=        - udp_session_quota: min=0 max=2097000 pattern=        - icmp_session_quota: min=0 max=2097000 pattern=        - privileged_port_use_pba: pattern=        - subnet_broadcast_in_ippool: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="IP pool name.")    
    type: TypeEnum | None = Field(default="overload", description="IP pool type: overload, one-to-one, fixed-port-range, port-block-allocation, cgn-resource-allocation (hyperscale vdom only)")    
    startip: str = Field(default="0.0.0.0", description="First IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).")    
    endip: str = Field(default="0.0.0.0", description="Final IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).")    
    startport: int = Field(ge=1024, le=65535, default=5117, description="First port number (inclusive) in the range for the address pool (1024 - 65535, Default: 5117).")    
    endport: int = Field(ge=1024, le=65535, default=65533, description="Final port number (inclusive) in the range for the address pool (1024 - 65535, Default: 65533).")    
    source_startip: str = Field(default="0.0.0.0", description="First IPv4 address (inclusive) in the range of the source addresses to be translated (format = xxx.xxx.xxx.xxx, default = 0.0.0.0).")    
    source_endip: str = Field(default="0.0.0.0", description="Final IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).")    
    block_size: int = Field(ge=64, le=4096, default=128, description="Number of addresses in a block (64 - 4096, default = 128).")    
    port_per_user: int = Field(ge=32, le=60417, default=0, description="Number of port for each user (32 - 60416, default = 0, which is auto).")    
    num_blocks_per_user: int = Field(ge=1, le=128, default=8, description="Number of addresses blocks that can be used by a user (1 to 128, default = 8).")    
    pba_timeout: int | None = Field(ge=3, le=86400, default=30, description="Port block allocation timeout (seconds).")    
    pba_interim_log: int | None = Field(ge=600, le=86400, default=0, description="Port block allocation interim logging interval (600 - 86400 seconds, default = 0 which disables interim logging).")    
    permit_any_host: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable fullcone NAT. Accept UDP packets from any host.")    
    arp_reply: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable replying to ARP requests when an IP Pool is added to a policy (default = enable).")    
    arp_intf: str | None = Field(max_length=15, default="", description="Select an interface from available options that will reply to ARP requests. (If blank, any is selected).")  # datasource: ['system.interface.name']    
    associated_interface: str | None = Field(max_length=15, default="", description="Associated interface name.")  # datasource: ['system.interface.name']    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    nat64: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable NAT64.")    
    add_nat64_route: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable adding NAT64 route.")    
    source_prefix6: str = Field(default="::/0", description="Source IPv6 network to be translated (format = xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx, default = ::/0).")    
    client_prefix_length: int = Field(ge=1, le=128, default=64, description="Subnet length of a single deterministic NAT64 client (1 - 128, default = 64).")    
    tcp_session_quota: int | None = Field(ge=0, le=2097000, default=0, description="Maximum number of concurrent TCP sessions allowed per client (0 - 2097000, default = 0 which means no limit).")    
    udp_session_quota: int | None = Field(ge=0, le=2097000, default=0, description="Maximum number of concurrent UDP sessions allowed per client (0 - 2097000, default = 0 which means no limit).")    
    icmp_session_quota: int | None = Field(ge=0, le=2097000, default=0, description="Maximum number of concurrent ICMP sessions allowed per client (0 - 2097000, default = 0 which means no limit).")    
    privileged_port_use_pba: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable selection of the external port from the port block allocation for NAT'ing privileged ports (deafult = disable).")    
    subnet_broadcast_in_ippool: Literal["disable"] | None = Field(default="", description="Enable/disable inclusion of the subnetwork address and broadcast IP address in the NAT64 IP pool.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('arp_intf')
    @classmethod
    def validate_arp_intf(cls, v: Any) -> Any:
        """
        Validate arp_intf field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('associated_interface')
    @classmethod
    def validate_associated_interface(cls, v: Any) -> Any:
        """
        Validate associated_interface field.
        
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
    async def validate_arp_intf_references(self, client: Any) -> list[str]:
        """
        Validate arp_intf references exist in FortiGate.
        
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
            >>> policy = IppoolModel(
            ...     arp_intf="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_arp_intf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ippool.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "arp_intf", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Arp-Intf '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_associated_interface_references(self, client: Any) -> list[str]:
        """
        Validate associated_interface references exist in FortiGate.
        
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
            >>> policy = IppoolModel(
            ...     associated_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_associated_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ippool.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "associated_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Associated-Interface '{value}' not found in "
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
        
        errors = await self.validate_arp_intf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_associated_interface_references(client)
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
    "IppoolModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.956527Z
# ============================================================================
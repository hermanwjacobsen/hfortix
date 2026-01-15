"""
Pydantic Models for CMDB - system/mobile_tunnel

Runtime validation models for system/mobile_tunnel configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class MobileTunnelNetwork(BaseModel):
    """
    Child table model for network.
    
    NEMO network configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Network entry ID.")    
    interface: str | None = Field(max_length=15, default="", description="Select the associated interface name from available options.")  # datasource: ['system.interface.name']    
    prefix: str | None = Field(default="0.0.0.0 0.0.0.0", description="Class IP and Netmask with correction (Format:xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx or xxx.xxx.xxx.xxx/x).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class MobileTunnelModel(BaseModel):
    """
    Pydantic model for system/mobile_tunnel configuration.
    
    Configure Mobile tunnels, an implementation of Network Mobility (NEMO) extensions for Mobile IPv4 RFC5177.
    
    Validation Rules:        - name: max_length=15 pattern=        - status: pattern=        - roaming_interface: max_length=15 pattern=        - home_agent: pattern=        - home_address: pattern=        - renew_interval: min=5 max=60 pattern=        - lifetime: min=180 max=65535 pattern=        - reg_interval: min=5 max=300 pattern=        - reg_retry: min=1 max=30 pattern=        - n_mhae_spi: min=0 max=4294967295 pattern=        - n_mhae_key_type: pattern=        - n_mhae_key: pattern=        - hash_algorithm: pattern=        - tunnel_mode: pattern=        - network: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="Tunnel name.")    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable this mobile tunnel.")    
    roaming_interface: str = Field(max_length=15, default="", description="Select the associated interface name from available options.")  # datasource: ['system.interface.name']    
    home_agent: str = Field(default="0.0.0.0", description="IPv4 address of the NEMO HA (Format: xxx.xxx.xxx.xxx).")    
    home_address: str | None = Field(default="0.0.0.0", description="Home IP address (Format: xxx.xxx.xxx.xxx).")    
    renew_interval: int = Field(ge=5, le=60, default=60, description="Time before lifetime expiration to send NMMO HA re-registration (5 - 60, default = 60).")    
    lifetime: int = Field(ge=180, le=65535, default=65535, description="NMMO HA registration request lifetime (180 - 65535 sec, default = 65535).")    
    reg_interval: int = Field(ge=5, le=300, default=5, description="NMMO HA registration interval (5 - 300, default = 5).")    
    reg_retry: int = Field(ge=1, le=30, default=3, description="Maximum number of NMMO HA registration retries (1 to 30, default = 3).")    
    n_mhae_spi: int = Field(ge=0, le=4294967295, default=256, description="NEMO authentication SPI (default: 256).")    
    n_mhae_key_type: Literal["ascii", "base64"] = Field(default="ascii", description="NEMO authentication key type (ASCII or base64).")    
    n_mhae_key: Any = Field(default=None, description="NEMO authentication key.")    
    hash_algorithm: Literal["hmac-md5"] = Field(default="hmac-md5", description="Hash Algorithm (Keyed MD5).")    
    tunnel_mode: Literal["gre"] = Field(default="gre", description="NEMO tunnel mode (GRE tunnel).")    
    network: list[Network] = Field(default=None, description="NEMO network configuration.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('roaming_interface')
    @classmethod
    def validate_roaming_interface(cls, v: Any) -> Any:
        """
        Validate roaming_interface field.
        
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
    async def validate_roaming_interface_references(self, client: Any) -> list[str]:
        """
        Validate roaming_interface references exist in FortiGate.
        
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
            >>> policy = MobileTunnelModel(
            ...     roaming_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_roaming_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.mobile_tunnel.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "roaming_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Roaming-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_network_references(self, client: Any) -> list[str]:
        """
        Validate network references exist in FortiGate.
        
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
            >>> policy = MobileTunnelModel(
            ...     network=[{"interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_network_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.mobile_tunnel.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "network", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("interface")
            else:
                value = getattr(item, "interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Network '{value}' not found in "
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
        
        errors = await self.validate_roaming_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_network_references(client)
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
    "MobileTunnelModel",    "MobileTunnelNetwork",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.677563Z
# ============================================================================
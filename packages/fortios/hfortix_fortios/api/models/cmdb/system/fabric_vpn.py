"""
Pydantic Models for CMDB - system/fabric_vpn

Runtime validation models for system/fabric_vpn configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class FabricVpnOverlays(BaseModel):
    """
    Child table model for overlays.
    
    Local overlay interfaces table.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Overlay name.")    
    ipsec_network_id: int | None = Field(ge=0, le=255, default=0, description="VPN gateway network ID.")    
    overlay_tunnel_block: Any = Field(default="0.0.0.0 0.0.0.0", description="IPv4 address and subnet mask for the overlay tunnel , syntax: X.X.X.X/24.")    
    remote_gw: str | None = Field(default="0.0.0.0", description="IP address of the hub gateway (Set by hub).")    
    interface: str | None = Field(max_length=15, default="", description="Underlying interface name.")  # datasource: ['system.interface.name']    
    bgp_neighbor: str | None = Field(max_length=45, default="", description="Underlying BGP neighbor entry.")  # datasource: ['router.bgp.neighbor.ip']    
    overlay_policy: int | None = Field(ge=0, le=4294967295, default=0, description="The overlay policy to allow ADVPN thru traffic.")  # datasource: ['firewall.policy.policyid']    
    bgp_network: int | None = Field(ge=0, le=4294967295, default=0, description="Underlying BGP network.")  # datasource: ['router.bgp.network.id']    
    route_policy: int | None = Field(ge=0, le=4294967295, default=0, description="Underlying router policy.")  # datasource: ['router.policy.seq-num']    
    bgp_neighbor_group: str | None = Field(max_length=45, default="", description="Underlying BGP neighbor group entry.")  # datasource: ['router.bgp.neighbor-group.name']    
    bgp_neighbor_range: int | None = Field(ge=0, le=4294967295, default=0, description="Underlying BGP neighbor range entry.")  # datasource: ['router.bgp.neighbor-range.id']    
    ipsec_phase1: str | None = Field(max_length=35, default="", description="IPsec interface.")  # datasource: ['vpn.ipsec.phase1-interface.name']    
    sdwan_member: int | None = Field(ge=0, le=4294967295, default=0, description="Reference to SD-WAN member entry.")  # datasource: ['system.sdwan.members.seq-num']
class FabricVpnAdvertisedSubnets(BaseModel):
    """
    Child table model for advertised-subnets.
    
    Local advertised subnets.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967294, default=0, description="ID.")    
    prefix: str = Field(default="0.0.0.0 0.0.0.0", description="Network prefix.")    
    access: Literal["inbound", "bidirectional"] = Field(default="inbound", description="Access policy direction.")    
    bgp_network: int | None = Field(ge=0, le=4294967295, default=0, description="Underlying BGP network.")  # datasource: ['router.bgp.network.id']    
    firewall_address: str | None = Field(max_length=79, default="", description="Underlying firewall address.")  # datasource: ['firewall.address.name']    
    policies: list[Policies] = Field(ge=0, le=4294967295, default="", description="Underlying policies.")  # datasource: ['firewall.policy.policyid']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class FabricVpnModel(BaseModel):
    """
    Pydantic model for system/fabric_vpn configuration.
    
    Setup for self orchestrated fabric auto discovery VPN.
    
    Validation Rules:        - status: pattern=        - sync_mode: pattern=        - branch_name: max_length=35 pattern=        - policy_rule: pattern=        - vpn_role: pattern=        - overlays: pattern=        - advertised_subnets: pattern=        - loopback_address_block: pattern=        - loopback_interface: max_length=15 pattern=        - loopback_advertised_subnet: min=0 max=4294967295 pattern=        - psksecret: pattern=        - bgp_as: pattern=        - sdwan_zone: max_length=35 pattern=        - health_checks: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable Fabric VPN.")    
    sync_mode: Literal["enable", "disable"] = Field(default="enable", description="Setting synchronized by fabric or manual.")    
    branch_name: str | None = Field(max_length=35, default="", description="Branch name.")    
    policy_rule: Literal["health-check", "manual", "auto"] | None = Field(default="health-check", description="Policy creation rule.")    
    vpn_role: Literal["hub", "spoke"] = Field(default="hub", description="Fabric VPN role.")    
    overlays: list[Overlays] = Field(default=None, description="Local overlay interfaces table.")    
    advertised_subnets: list[AdvertisedSubnets] = Field(default=None, description="Local advertised subnets.")    
    loopback_address_block: Any = Field(default="0.0.0.0 0.0.0.0", description="IPv4 address and subnet mask for hub's loopback address, syntax: X.X.X.X/24.")    
    loopback_interface: str | None = Field(max_length=15, default="", description="Loopback interface.")  # datasource: ['system.interface.name']    
    loopback_advertised_subnet: int | None = Field(ge=0, le=4294967295, default=0, description="Loopback advertised subnet reference.")  # datasource: ['system.fabric-vpn.advertised-subnets.id']    
    psksecret: Any = Field(description="Pre-shared secret for ADVPN.")    
    bgp_as: str = Field(default="", description="BGP Router AS number, asplain/asdot/asdot+ format.")    
    sdwan_zone: str | None = Field(max_length=35, default="", description="Reference to created SD-WAN zone.")  # datasource: ['system.sdwan.zone.name']    
    health_checks: list[HealthChecks] = Field(max_length=35, default="", description="Underlying health checks.")  # datasource: ['system.sdwan.health-check.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('loopback_interface')
    @classmethod
    def validate_loopback_interface(cls, v: Any) -> Any:
        """
        Validate loopback_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('loopback_advertised_subnet')
    @classmethod
    def validate_loopback_advertised_subnet(cls, v: Any) -> Any:
        """
        Validate loopback_advertised_subnet field.
        
        Datasource: ['system.fabric-vpn.advertised-subnets.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sdwan_zone')
    @classmethod
    def validate_sdwan_zone(cls, v: Any) -> Any:
        """
        Validate sdwan_zone field.
        
        Datasource: ['system.sdwan.zone.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('health_checks')
    @classmethod
    def validate_health_checks(cls, v: Any) -> Any:
        """
        Validate health_checks field.
        
        Datasource: ['system.sdwan.health-check.name']
        
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
    async def validate_overlays_references(self, client: Any) -> list[str]:
        """
        Validate overlays references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdwan/members        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FabricVpnModel(
            ...     overlays=[{"sdwan-member": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_overlays_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fabric_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "overlays", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("sdwan-member")
            else:
                value = getattr(item, "sdwan-member", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.sdwan.members.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Overlays '{value}' not found in "
                    "system/sdwan/members"
                )        
        return errors    
    async def validate_advertised_subnets_references(self, client: Any) -> list[str]:
        """
        Validate advertised_subnets references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FabricVpnModel(
            ...     advertised_subnets=[{"policies": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_advertised_subnets_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fabric_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "advertised_subnets", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("policies")
            else:
                value = getattr(item, "policies", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.policy.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Advertised-Subnets '{value}' not found in "
                    "firewall/policy"
                )        
        return errors    
    async def validate_loopback_interface_references(self, client: Any) -> list[str]:
        """
        Validate loopback_interface references exist in FortiGate.
        
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
            >>> policy = FabricVpnModel(
            ...     loopback_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_loopback_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fabric_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "loopback_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Loopback-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_loopback_advertised_subnet_references(self, client: Any) -> list[str]:
        """
        Validate loopback_advertised_subnet references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/fabric-vpn/advertised-subnets        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FabricVpnModel(
            ...     loopback_advertised_subnet="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_loopback_advertised_subnet_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fabric_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "loopback_advertised_subnet", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.fabric-vpn.advertised-subnets.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Loopback-Advertised-Subnet '{value}' not found in "
                "system/fabric-vpn/advertised-subnets"
            )        
        return errors    
    async def validate_sdwan_zone_references(self, client: Any) -> list[str]:
        """
        Validate sdwan_zone references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdwan/zone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FabricVpnModel(
            ...     sdwan_zone="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sdwan_zone_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fabric_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "sdwan_zone", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.sdwan.zone.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Sdwan-Zone '{value}' not found in "
                "system/sdwan/zone"
            )        
        return errors    
    async def validate_health_checks_references(self, client: Any) -> list[str]:
        """
        Validate health_checks references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/sdwan/health-check        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FabricVpnModel(
            ...     health_checks="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_health_checks_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fabric_vpn.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "health_checks", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.sdwan.health-check.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Health-Checks '{value}' not found in "
                "system/sdwan/health-check"
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
        
        errors = await self.validate_overlays_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_advertised_subnets_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_loopback_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_loopback_advertised_subnet_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sdwan_zone_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_health_checks_references(client)
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
    "FabricVpnModel",    "FabricVpnOverlays",    "FabricVpnAdvertisedSubnets",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.910254Z
# ============================================================================
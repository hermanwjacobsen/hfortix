"""
Pydantic Models for CMDB - firewall/multicast_policy

Runtime validation models for firewall/multicast_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class MulticastPolicySrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Source address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Source address objects.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class MulticastPolicyDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Destination address objects.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Destination address objects.")  # datasource: ['firewall.multicast-address.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class MulticastPolicyModel(BaseModel):
    """
    Pydantic model for firewall/multicast_policy configuration.
    
    Configure multicast NAT policies.
    
    Validation Rules:        - id: min=0 max=4294967294 pattern=        - uuid: pattern=        - name: max_length=35 pattern=        - comments: max_length=1023 pattern=        - status: pattern=        - srcintf: max_length=35 pattern=        - dstintf: max_length=35 pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - snat: pattern=        - snat_ip: pattern=        - dnat: pattern=        - action: pattern=        - protocol: min=0 max=255 pattern=        - start_port: min=0 max=65535 pattern=        - end_port: min=0 max=65535 pattern=        - utm_status: pattern=        - ips_sensor: max_length=47 pattern=        - logtraffic: pattern=        - auto_asic_offload: pattern=        - traffic_shaper: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967294, default=0, description="Policy ID ((0 - 4294967294).")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    name: str | None = Field(max_length=35, default="", description="Policy name.")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this policy.")    
    srcintf: str = Field(max_length=35, default="", description="Source interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']    
    dstintf: str = Field(max_length=35, default="", description="Destination interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']    
    srcaddr: list[Srcaddr] = Field(description="Source address objects.")    
    dstaddr: list[Dstaddr] = Field(description="Destination address objects.")    
    snat: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable substitution of the outgoing interface IP address for the original source IP address (called source NAT or SNAT).")    
    snat_ip: str | None = Field(default="0.0.0.0", description="IPv4 address to be used as the source address for NATed traffic.")    
    dnat: str | None = Field(default="0.0.0.0", description="IPv4 DNAT address used for multicast destination addresses.")    
    action: Literal["accept", "deny"] | None = Field(default="accept", description="Accept or deny traffic matching the policy.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Integer value for the protocol type as defined by IANA (0 - 255, default = 0).")    
    start_port: int | None = Field(ge=0, le=65535, default=1, description="Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535, default = 1).")    
    end_port: int | None = Field(ge=0, le=65535, default=65535, description="Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535, default = 1).")    
    utm_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to add an IPS security profile to the policy.")    
    ips_sensor: str | None = Field(max_length=47, default="", description="Name of an existing IPS sensor.")  # datasource: ['ips.sensor.name']    
    logtraffic: Literal["all", "utm", "disable"] | None = Field(default="utm", description="Enable or disable logging. Log all sessions or security profile sessions.")    
    auto_asic_offload: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable offloading policy traffic for hardware acceleration.")    
    traffic_shaper: str | None = Field(max_length=35, default="", description="Traffic shaper to apply to traffic forwarded by the multicast policy.")  # datasource: ['firewall.shaper.traffic-shaper.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('srcintf')
    @classmethod
    def validate_srcintf(cls, v: Any) -> Any:
        """
        Validate srcintf field.
        
        Datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dstintf')
    @classmethod
    def validate_dstintf(cls, v: Any) -> Any:
        """
        Validate dstintf field.
        
        Datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ips_sensor')
    @classmethod
    def validate_ips_sensor(cls, v: Any) -> Any:
        """
        Validate ips_sensor field.
        
        Datasource: ['ips.sensor.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('traffic_shaper')
    @classmethod
    def validate_traffic_shaper(cls, v: Any) -> Any:
        """
        Validate traffic_shaper field.
        
        Datasource: ['firewall.shaper.traffic-shaper.name']
        
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
    async def validate_srcintf_references(self, client: Any) -> list[str]:
        """
        Validate srcintf references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        - system/zone        - system/sdwan/zone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastPolicyModel(
            ...     srcintf="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "srcintf", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        elif await client.api.cmdb.system.zone.exists(value):
            found = True
        elif await client.api.cmdb.system.sdwan.zone.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Srcintf '{value}' not found in "
                "system/interface or system/zone or system/sdwan/zone"
            )        
        return errors    
    async def validate_dstintf_references(self, client: Any) -> list[str]:
        """
        Validate dstintf references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        - system/zone        - system/sdwan/zone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastPolicyModel(
            ...     dstintf="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dstintf", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        elif await client.api.cmdb.system.zone.exists(value):
            found = True
        elif await client.api.cmdb.system.sdwan.zone.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dstintf '{value}' not found in "
                "system/interface or system/zone or system/sdwan/zone"
            )        
        return errors    
    async def validate_srcaddr_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastPolicyModel(
            ...     srcaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "srcaddr", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
                )        
        return errors    
    async def validate_dstaddr_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/multicast-address        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastPolicyModel(
            ...     dstaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dstaddr", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.multicast-address.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dstaddr '{value}' not found in "
                    "firewall/multicast-address"
                )        
        return errors    
    async def validate_ips_sensor_references(self, client: Any) -> list[str]:
        """
        Validate ips_sensor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - ips/sensor        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastPolicyModel(
            ...     ips_sensor="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ips_sensor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ips_sensor", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.ips.sensor.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ips-Sensor '{value}' not found in "
                "ips/sensor"
            )        
        return errors    
    async def validate_traffic_shaper_references(self, client: Any) -> list[str]:
        """
        Validate traffic_shaper references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/shaper/traffic-shaper        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastPolicyModel(
            ...     traffic_shaper="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_shaper_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "traffic_shaper", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.shaper.traffic-shaper.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Traffic-Shaper '{value}' not found in "
                "firewall/shaper/traffic-shaper"
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
        
        errors = await self.validate_srcintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ips_sensor_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_traffic_shaper_references(client)
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
    "MulticastPolicyModel",    "MulticastPolicySrcaddr",    "MulticastPolicyDstaddr",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.351056Z
# ============================================================================
"""
Pydantic Models for CMDB - firewall/central_snat_map

Runtime validation models for firewall/central_snat_map configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class CentralSnatMapSrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Source interface name from available interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class CentralSnatMapDstintf(BaseModel):
    """
    Child table model for dstintf.
    
    Destination interface name from available interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class CentralSnatMapOrigAddr(BaseModel):
    """
    Child table model for orig-addr.
    
    IPv4 Original address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'system.external-resource.name']
class CentralSnatMapOrigAddr6(BaseModel):
    """
    Child table model for orig-addr6.
    
    IPv6 Original address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name', 'system.external-resource.name']
class CentralSnatMapDstAddr(BaseModel):
    """
    Child table model for dst-addr.
    
    IPv4 Destination address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
class CentralSnatMapDstAddr6(BaseModel):
    """
    Child table model for dst-addr6.
    
    IPv6 Destination address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class CentralSnatMapNatIppool(BaseModel):
    """
    Child table model for nat-ippool.
    
    Name of the IP pools to be used to translate addresses from available IP Pools.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IP pool name.")  # datasource: ['firewall.ippool.name']
class CentralSnatMapNatIppool6(BaseModel):
    """
    Child table model for nat-ippool6.
    
    IPv6 pools to be used for source NAT.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="IPv6 pool name.")  # datasource: ['firewall.ippool6.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class CentralSnatMapModel(BaseModel):
    """
    Pydantic model for firewall/central_snat_map configuration.
    
    Configure IPv4 and IPv6 central SNAT policies.
    
    Validation Rules:        - policyid: min=0 max=4294967295 pattern=        - uuid: pattern=        - status: pattern=        - type: pattern=        - srcintf: pattern=        - dstintf: pattern=        - orig_addr: pattern=        - orig_addr6: pattern=        - dst_addr: pattern=        - dst_addr6: pattern=        - protocol: min=0 max=255 pattern=        - orig_port: pattern=        - nat: pattern=        - nat46: pattern=        - nat64: pattern=        - nat_ippool: pattern=        - nat_ippool6: pattern=        - port_preserve: pattern=        - port_random: pattern=        - nat_port: pattern=        - dst_port: pattern=        - comments: max_length=1023 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    policyid: int | None = Field(ge=0, le=4294967295, default=0, description="Policy ID.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of this policy.")    
    type: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="IPv4/IPv6 source NAT.")    
    srcintf: list[Srcintf] = Field(description="Source interface name from available interfaces.")    
    dstintf: list[Dstintf] = Field(description="Destination interface name from available interfaces.")    
    orig_addr: list[OrigAddr] = Field(description="IPv4 Original address.")    
    orig_addr6: list[OrigAddr6] = Field(description="IPv6 Original address.")    
    dst_addr: list[DstAddr] = Field(description="IPv4 Destination address.")    
    dst_addr6: list[DstAddr6] = Field(description="IPv6 Destination address.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Integer value for the protocol type (0 - 255).")    
    orig_port: str | None = Field(default="", description="Original TCP port (1 to 65535, 0 means any port).")    
    nat: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable source NAT.")    
    nat46: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT46.")    
    nat64: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable NAT64.")    
    nat_ippool: list[NatIppool] = Field(default=None, description="Name of the IP pools to be used to translate addresses from available IP Pools.")    
    nat_ippool6: list[NatIppool6] = Field(default=None, description="IPv6 pools to be used for source NAT.")    
    port_preserve: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable preservation of the original source port from source NAT if it has not been used.")    
    port_random: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable random source port selection for source NAT.")    
    nat_port: str | None = Field(default="", description="Translated port or port range (1 to 65535, 0 means any port).")    
    dst_port: str | None = Field(default="", description="Destination port or port range (1 to 65535, 0 means any port).")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
            >>> policy = CentralSnatMapModel(
            ...     srcintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "srcintf", [])
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
            >>> policy = CentralSnatMapModel(
            ...     dstintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dstintf", [])
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
    async def validate_orig_addr_references(self, client: Any) -> list[str]:
        """
        Validate orig_addr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CentralSnatMapModel(
            ...     orig_addr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_orig_addr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "orig_addr", [])
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
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Orig-Addr '{value}' not found in "
                    "firewall/address or firewall/addrgrp or system/external-resource"
                )        
        return errors    
    async def validate_orig_addr6_references(self, client: Any) -> list[str]:
        """
        Validate orig_addr6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CentralSnatMapModel(
            ...     orig_addr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_orig_addr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "orig_addr6", [])
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
            if await client.api.cmdb.firewall.address6.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp6.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Orig-Addr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6 or system/external-resource"
                )        
        return errors    
    async def validate_dst_addr_references(self, client: Any) -> list[str]:
        """
        Validate dst_addr references exist in FortiGate.
        
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
            >>> policy = CentralSnatMapModel(
            ...     dst_addr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dst_addr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dst_addr", [])
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
                    f"Dst-Addr '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
                )        
        return errors    
    async def validate_dst_addr6_references(self, client: Any) -> list[str]:
        """
        Validate dst_addr6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CentralSnatMapModel(
            ...     dst_addr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dst_addr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dst_addr6", [])
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
            if await client.api.cmdb.firewall.address6.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dst-Addr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6"
                )        
        return errors    
    async def validate_nat_ippool_references(self, client: Any) -> list[str]:
        """
        Validate nat_ippool references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ippool        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CentralSnatMapModel(
            ...     nat_ippool=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_nat_ippool_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "nat_ippool", [])
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
            if await client.api.cmdb.firewall.ippool.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Nat-Ippool '{value}' not found in "
                    "firewall/ippool"
                )        
        return errors    
    async def validate_nat_ippool6_references(self, client: Any) -> list[str]:
        """
        Validate nat_ippool6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ippool6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CentralSnatMapModel(
            ...     nat_ippool6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_nat_ippool6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.central_snat_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "nat_ippool6", [])
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
            if await client.api.cmdb.firewall.ippool6.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Nat-Ippool6 '{value}' not found in "
                    "firewall/ippool6"
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
        errors = await self.validate_orig_addr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_orig_addr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dst_addr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dst_addr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_nat_ippool_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_nat_ippool6_references(client)
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
    "CentralSnatMapModel",    "CentralSnatMapSrcintf",    "CentralSnatMapDstintf",    "CentralSnatMapOrigAddr",    "CentralSnatMapOrigAddr6",    "CentralSnatMapDstAddr",    "CentralSnatMapDstAddr6",    "CentralSnatMapNatIppool",    "CentralSnatMapNatIppool6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.708836Z
# ============================================================================
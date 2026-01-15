"""
Pydantic Models for CMDB - firewall/address6

Runtime validation models for firewall/address6 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class Address6Macaddr(BaseModel):
    """
    Child table model for macaddr.
    
    Multiple MAC address ranges.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    macaddr: str = Field(max_length=127, default="", description="MAC address ranges <start>[-<end>] separated by space.")
class Address6Tagging(BaseModel):
    """
    Child table model for tagging.
    
    Config object tagging.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Tagging entry name.")    
    category: str | None = Field(max_length=63, default="", description="Tag category.")  # datasource: ['system.object-tagging.category']    
    tags: list[Tags] = Field(default=None, description="Tags.")
class Address6SubnetSegment(BaseModel):
    """
    Child table model for subnet-segment.
    
    IPv6 subnet segments.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=63, default="", description="Name.")    
    type: Literal["any", "specific"] = Field(default="any", description="Subnet segment type.")    
    value: str = Field(max_length=35, default="", description="Subnet segment value.")
class Address6List(BaseModel):
    """
    Child table model for list.
    
    IP address list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ip: str = Field(max_length=89, default="", description="IP.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class Address6TypeEnum(str, Enum):
    """Allowed values for type field."""
    IPPREFIX = "ipprefix"    IPRANGE = "iprange"    FQDN = "fqdn"    GEOGRAPHY = "geography"    DYNAMIC = "dynamic"    TEMPLATE = "template"    MAC = "mac"    ROUTE_TAG = "route-tag"    WILDCARD = "wildcard"

# ============================================================================
# Main Model
# ============================================================================

class Address6Model(BaseModel):
    """
    Pydantic model for firewall/address6 configuration.
    
    Configure IPv6 firewall addresses.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: pattern=        - type: pattern=        - route_tag: min=1 max=4294967295 pattern=        - macaddr: pattern=        - sdn: max_length=35 pattern=        - ip6: pattern=        - wildcard: pattern=        - start_ip: pattern=        - end_ip: pattern=        - fqdn: max_length=255 pattern=        - country: max_length=2 pattern=        - cache_ttl: min=0 max=86400 pattern=        - color: min=0 max=32 pattern=        - obj_id: max_length=255 pattern=        - tagging: pattern=        - comment: max_length=255 pattern=        - template: max_length=63 pattern=        - subnet_segment: pattern=        - host_type: pattern=        - host: pattern=        - tenant: max_length=35 pattern=        - epg_name: max_length=255 pattern=        - sdn_tag: max_length=15 pattern=        - filter: max_length=2047 pattern=        - list: pattern=        - sdn_addr_type: pattern=        - passive_fqdn_learning: pattern=        - fabric_object: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Address name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    type: TypeEnum | None = Field(default="ipprefix", description="Type of IPv6 address object (default = ipprefix).")    
    route_tag: int | None = Field(ge=1, le=4294967295, default=0, description="route-tag address.")    
    macaddr: list[Macaddr] = Field(default=None, description="Multiple MAC address ranges.")    
    sdn: str | None = Field(max_length=35, default="", description="SDN.")  # datasource: ['system.sdn-connector.name']    
    ip6: str | None = Field(default="::/0", description="IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx).")    
    wildcard: Any = Field(default=":: ::", description="IPv6 address and wildcard netmask.")    
    start_ip: str | None = Field(default="::", description="First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).")    
    end_ip: str | None = Field(default="::", description="Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx).")    
    fqdn: str | None = Field(max_length=255, default="", description="Fully qualified domain name.")    
    country: str | None = Field(max_length=2, default="", description="IPv6 addresses associated to a specific country.")    
    cache_ttl: int | None = Field(ge=0, le=86400, default=0, description="Minimal TTL of individual IPv6 addresses in FQDN cache.")    
    color: int | None = Field(ge=0, le=32, default=0, description="Integer value to determine the color of the icon in the GUI (range 1 to 32, default = 0, which sets the value to 1).")    
    obj_id: str | None = Field(max_length=255, default=None, description="Object ID for NSX.")    
    tagging: list[Tagging] = Field(default=None, description="Config object tagging.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    template: str = Field(max_length=63, default="", description="IPv6 address template.")  # datasource: ['firewall.address6-template.name']    
    subnet_segment: list[SubnetSegment] = Field(default=None, description="IPv6 subnet segments.")    
    host_type: Literal["any", "specific"] | None = Field(default="any", description="Host type.")    
    host: str | None = Field(default="::", description="Host Address.")    
    tenant: str | None = Field(max_length=35, default="", description="Tenant.")    
    epg_name: str | None = Field(max_length=255, default="", description="Endpoint group name.")    
    sdn_tag: str | None = Field(max_length=15, default="", description="SDN Tag.")    
    filter: str = Field(max_length=2047, description="Match criteria filter.")    
    list: list[List] = Field(default=None, description="IP address list.")    
    sdn_addr_type: Literal["private", "public", "all"] | None = Field(default="private", description="Type of addresses to collect.")    
    passive_fqdn_learning: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable passive learning of FQDNs.  When enabled, the FortiGate learns, trusts, and saves FQDNs from endpoint DNS queries (default = enable).")    
    fabric_object: Literal["enable", "disable"] | None = Field(default="disable", description="Security Fabric global object setting.")    
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
    @field_validator('template')
    @classmethod
    def validate_template(cls, v: Any) -> Any:
        """
        Validate template field.
        
        Datasource: ['firewall.address6-template.name']
        
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
            >>> policy = Address6Model(
            ...     sdn="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sdn_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.address6.post(policy.to_fortios_dict())
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
    async def validate_tagging_references(self, client: Any) -> list[str]:
        """
        Validate tagging references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/object-tagging        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Address6Model(
            ...     tagging=[{"category": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tagging_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.address6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "tagging", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("category")
            else:
                value = getattr(item, "category", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.object-tagging.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Tagging '{value}' not found in "
                    "system/object-tagging"
                )        
        return errors    
    async def validate_template_references(self, client: Any) -> list[str]:
        """
        Validate template references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6-template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Address6Model(
            ...     template="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_template_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.address6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "template", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address6-template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Template '{value}' not found in "
                "firewall/address6-template"
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
        errors = await self.validate_tagging_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_template_references(client)
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
    "Address6Model",    "Address6Macaddr",    "Address6Tagging",    "Address6SubnetSegment",    "Address6List",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.809590Z
# ============================================================================
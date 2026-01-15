"""
Pydantic Models for CMDB - system/dns_database

Runtime validation models for system/dns_database configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class DnsDatabaseDnsEntry(BaseModel):
    """
    Child table model for dns-entry.
    
    DNS entry.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="DNS entry ID.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable resource record status.")    
    type: TypeEnum = Field(default="A", description="Resource record type.")    
    ttl: int | None = Field(ge=0, le=2147483647, default=0, description="Time-to-live for this entry (0 to 2147483647 sec, default = 0).")    
    preference: int | None = Field(ge=0, le=65535, default=10, description="DNS entry preference (0 - 65535, highest preference = 0, default = 10).")    
    ip: str | None = Field(default="0.0.0.0", description="IPv4 address of the host.")    
    ipv6: str | None = Field(default="::", description="IPv6 address of the host.")    
    hostname: str = Field(max_length=255, default="", description="Name of the host.")    
    canonical_name: str | None = Field(max_length=255, default="", description="Canonical name of the host.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class DnsDatabaseViewEnum(str, Enum):
    """Allowed values for view field."""
    SHADOW = "shadow"    PUBLIC = "public"    SHADOW_ZTNA = "shadow-ztna"    PROXY = "proxy"

# ============================================================================
# Main Model
# ============================================================================

class DnsDatabaseModel(BaseModel):
    """
    Pydantic model for system/dns_database configuration.
    
    Configure DNS databases.
    
    Validation Rules:        - name: max_length=35 pattern=        - status: pattern=        - domain: max_length=255 pattern=        - allow_transfer: pattern=        - type: pattern=        - view: pattern=        - ip_primary: pattern=        - primary_name: max_length=255 pattern=        - contact: max_length=255 pattern=        - ttl: min=0 max=2147483647 pattern=        - authoritative: pattern=        - forwarder: pattern=        - forwarder6: pattern=        - source_ip: pattern=        - source_ip6: pattern=        - source_ip_interface: max_length=15 pattern=        - rr_max: min=10 max=65536 pattern=        - dns_entry: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Zone name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this DNS zone.")    
    domain: str = Field(max_length=255, default="", description="Domain name.")    
    allow_transfer: list[AllowTransfer] = Field(default="", description="DNS zone transfer IP address list.")    
    type: Literal["primary", "secondary"] = Field(default="primary", description="Zone type (primary to manage entries directly, secondary to import entries from other zones).")    
    view: ViewEnum = Field(default="shadow", description="Zone view (public to serve public clients, shadow to serve internal clients).")    
    ip_primary: str | None = Field(default="0.0.0.0", description="IP address of primary DNS server. Entries in this primary DNS server and imported into the DNS zone.")    
    primary_name: str | None = Field(max_length=255, default="dns", description="Domain name of the default DNS server for this zone.")    
    contact: str | None = Field(max_length=255, default="host", description="Email address of the administrator for this zone. You can specify only the username, such as admin or the full email address, such as admin@test.com When using only a username, the domain of the email will be this zone.")    
    ttl: int = Field(ge=0, le=2147483647, default=86400, description="Default time-to-live value for the entries of this DNS zone (0 - 2147483647 sec, default = 86400).")    
    authoritative: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable authoritative zone.")    
    forwarder: list[Forwarder] = Field(default="", description="DNS zone forwarder IP address list.")    
    forwarder6: str | None = Field(default="::", description="Forwarder IPv6 address.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP for forwarding to DNS server.")    
    source_ip6: str | None = Field(default="::", description="IPv6 source IP address for forwarding to DNS server.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="IP address of the specified interface as the source IP address.")  # datasource: ['system.interface.name']    
    rr_max: int | None = Field(ge=10, le=65536, default=16384, description="Maximum number of resource records (10 - 65536, 0 means infinite).")    
    dns_entry: list[DnsEntry] = Field(description="DNS entry.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('source_ip_interface')
    @classmethod
    def validate_source_ip_interface(cls, v: Any) -> Any:
        """
        Validate source_ip_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    async def validate_source_ip_interface_references(self, client: Any) -> list[str]:
        """
        Validate source_ip_interface references exist in FortiGate.
        
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
            >>> policy = DnsDatabaseModel(
            ...     source_ip_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_source_ip_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dns_database.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "source_ip_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Source-Ip-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
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
            >>> policy = DnsDatabaseModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dns_database.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_source_ip_interface_references(client)
        all_errors.extend(errors)        
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
    "DnsDatabaseModel",    "DnsDatabaseDnsEntry",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.780730Z
# ============================================================================
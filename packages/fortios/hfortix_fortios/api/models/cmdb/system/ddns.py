"""
Pydantic Models for CMDB - system/ddns

Runtime validation models for system/ddns configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class DdnsDdnsServerAddr(BaseModel):
    """
    Child table model for ddns-server-addr.
    
    Generic DDNS server IP/FQDN list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    addr: str = Field(max_length=256, default="", description="IP address or FQDN of the server.")
class DdnsMonitorInterface(BaseModel):
    """
    Child table model for monitor-interface.
    
    Monitored interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_name: str = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class DdnsDdns_serverEnum(str, Enum):
    """Allowed values for ddns_server field."""
    DYNDNS_ORG = "dyndns.org"    DYNS_NET = "dyns.net"    TZO_COM = "tzo.com"    VAVIC_COM = "vavic.com"    DIPDNS_NET = "dipdns.net"    NOW_NET_CN = "now.net.cn"    DHS_ORG = "dhs.org"    EASYDNS_COM = "easydns.com"    GENERICDDNS = "genericDDNS"    FORTIGUARDDDNS = "FortiGuardDDNS"    NOIP_COM = "noip.com"

# ============================================================================
# Main Model
# ============================================================================

class DdnsModel(BaseModel):
    """
    Pydantic model for system/ddns configuration.
    
    Configure DDNS.
    
    Validation Rules:        - ddnsid: min=0 max=4294967295 pattern=        - ddns_server: pattern=        - addr_type: pattern=        - server_type: pattern=        - ddns_server_addr: pattern=        - ddns_zone: max_length=64 pattern=        - ddns_ttl: min=60 max=86400 pattern=        - ddns_auth: pattern=        - ddns_keyname: max_length=64 pattern=        - ddns_key: pattern=        - ddns_domain: max_length=64 pattern=        - ddns_username: max_length=64 pattern=        - ddns_sn: max_length=64 pattern=        - ddns_password: max_length=128 pattern=        - use_public_ip: pattern=        - update_interval: min=60 max=2592000 pattern=        - clear_text: pattern=        - ssl_certificate: max_length=35 pattern=        - bound_ip: max_length=46 pattern=        - monitor_interface: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    ddnsid: int | None = Field(ge=0, le=4294967295, default=0, description="DDNS ID.")    
    ddns_server: DdnsServerEnum = Field(default="", description="Select a DDNS service provider.")    
    addr_type: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address type of interface address in DDNS update.")    
    server_type: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address type of the DDNS server.")    
    ddns_server_addr: list[DdnsServerAddr] = Field(default=None, description="Generic DDNS server IP/FQDN list.")    
    ddns_zone: str | None = Field(max_length=64, default="", description="Zone of your domain name (for example, DDNS.com).")    
    ddns_ttl: int | None = Field(ge=60, le=86400, default=300, description="Time-to-live for DDNS packets.")    
    ddns_auth: Literal["disable", "tsig"] | None = Field(default="disable", description="Enable/disable TSIG authentication for your DDNS server.")    
    ddns_keyname: str | None = Field(max_length=64, default="", description="DDNS update key name.")    
    ddns_key: Any = Field(default=None, description="DDNS update key (base 64 encoding).")    
    ddns_domain: str | None = Field(max_length=64, default="", description="Your fully qualified domain name. For example, yourname.ddns.com.")    
    ddns_username: str | None = Field(max_length=64, default="", description="DDNS user name.")    
    ddns_sn: str | None = Field(max_length=64, default="", description="DDNS Serial Number.")    
    ddns_password: Any = Field(max_length=128, default=None, description="DDNS password.")    
    use_public_ip: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of public IP address.")    
    update_interval: int | None = Field(ge=60, le=2592000, default=0, description="DDNS update interval (60 - 2592000 sec, 0 means default).")    
    clear_text: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of clear text connections.")    
    ssl_certificate: str | None = Field(max_length=35, default="Fortinet_Factory", description="Name of local certificate for SSL connections.")  # datasource: ['certificate.local.name']    
    bound_ip: str | None = Field(max_length=46, default="", description="Bound IP address.")    
    monitor_interface: list[MonitorInterface] = Field(description="Monitored interface.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ssl_certificate')
    @classmethod
    def validate_ssl_certificate(cls, v: Any) -> Any:
        """
        Validate ssl_certificate field.
        
        Datasource: ['certificate.local.name']
        
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
    async def validate_ssl_certificate_references(self, client: Any) -> list[str]:
        """
        Validate ssl_certificate references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DdnsModel(
            ...     ssl_certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ddns.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssl_certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssl-Certificate '{value}' not found in "
                "certificate/local"
            )        
        return errors    
    async def validate_monitor_interface_references(self, client: Any) -> list[str]:
        """
        Validate monitor_interface references exist in FortiGate.
        
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
            >>> policy = DdnsModel(
            ...     monitor_interface=[{"interface-name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_monitor_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.ddns.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "monitor_interface", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("interface-name")
            else:
                value = getattr(item, "interface-name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Monitor-Interface '{value}' not found in "
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
        
        errors = await self.validate_ssl_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_monitor_interface_references(client)
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
    "DdnsModel",    "DdnsDdnsServerAddr",    "DdnsMonitorInterface",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.529062Z
# ============================================================================
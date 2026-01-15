"""
Pydantic Models for CMDB - system/dns

Runtime validation models for system/dns configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class DnsServerHostname(BaseModel):
    """
    Child table model for server-hostname.
    
    DNS server host name list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    hostname: str = Field(max_length=127, default="", description="DNS server host name list separated by space (maximum 4 domains).")
class DnsDomain(BaseModel):
    """
    Child table model for domain.
    
    Search suffix list for hostname lookup.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    domain: str = Field(max_length=127, default="", description="DNS search domain list separated by space (maximum 8 domains).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class DnsModel(BaseModel):
    """
    Pydantic model for system/dns configuration.
    
    Configure DNS.
    
    Validation Rules:        - primary: pattern=        - secondary: pattern=        - protocol: pattern=        - ssl_certificate: max_length=35 pattern=        - server_hostname: pattern=        - domain: pattern=        - ip6_primary: pattern=        - ip6_secondary: pattern=        - timeout: min=1 max=10 pattern=        - retry: min=0 max=5 pattern=        - dns_cache_limit: min=0 max=4294967295 pattern=        - dns_cache_ttl: min=60 max=86400 pattern=        - cache_notfound_responses: pattern=        - source_ip: pattern=        - source_ip_interface: max_length=15 pattern=        - root_servers: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - server_select_method: pattern=        - alt_primary: pattern=        - alt_secondary: pattern=        - log: pattern=        - fqdn_cache_ttl: min=0 max=86400 pattern=        - fqdn_max_refresh: min=3600 max=86400 pattern=        - fqdn_min_refresh: min=10 max=3600 pattern=        - hostname_ttl: min=60 max=86400 pattern=        - hostname_limit: min=0 max=50000 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    primary: str = Field(default="0.0.0.0", description="Primary DNS server IP address.")    
    secondary: str | None = Field(default="0.0.0.0", description="Secondary DNS server IP address.")    
    protocol: list[Protocol] = Field(default="cleartext", description="DNS transport protocols.")    
    ssl_certificate: str | None = Field(max_length=35, default="Fortinet_Factory", description="Name of local certificate for SSL connections.")  # datasource: ['certificate.local.name']    
    server_hostname: list[ServerHostname] = Field(default=None, description="DNS server host name list.")    
    domain: list[Domain] = Field(default=None, description="Search suffix list for hostname lookup.")    
    ip6_primary: str | None = Field(default="::", description="Primary DNS server IPv6 address.")    
    ip6_secondary: str | None = Field(default="::", description="Secondary DNS server IPv6 address.")    
    timeout: int | None = Field(ge=1, le=10, default=5, description="DNS query timeout interval in seconds (1 - 10).")    
    retry: int | None = Field(ge=0, le=5, default=2, description="Number of times to retry (0 - 5).")    
    dns_cache_limit: int | None = Field(ge=0, le=4294967295, default=5000, description="Maximum number of records in the DNS cache.")    
    dns_cache_ttl: int | None = Field(ge=60, le=86400, default=1800, description="Duration in seconds that the DNS cache retains information.")    
    cache_notfound_responses: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable response from the DNS server when a record is not in cache.")    
    source_ip: str | None = Field(default="0.0.0.0", description="IP address used by the DNS server as its source IP.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="IP address of the specified interface as the source IP address.")  # datasource: ['system.interface.name']    
    root_servers: list[RootServers] = Field(default="", description="Configure up to two preferred servers that serve the DNS root zone (default uses all 13 root servers).")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    server_select_method: Literal["least-rtt", "failover"] | None = Field(default="least-rtt", description="Specify how configured servers are prioritized.")    
    alt_primary: str | None = Field(default="0.0.0.0", description="Alternate primary DNS server. This is not used as a failover DNS server.")    
    alt_secondary: str | None = Field(default="0.0.0.0", description="Alternate secondary DNS server. This is not used as a failover DNS server.")    
    log: Literal["disable", "error", "all"] | None = Field(default="disable", description="Local DNS log setting.")    
    fqdn_cache_ttl: int | None = Field(ge=0, le=86400, default=0, description="FQDN cache time to live in seconds (0 - 86400, default = 0).")    
    fqdn_max_refresh: int | None = Field(ge=3600, le=86400, default=3600, description="FQDN cache maximum refresh time in seconds (3600 - 86400, default = 3600).")    
    fqdn_min_refresh: int | None = Field(ge=10, le=3600, default=60, description="FQDN cache minimum refresh time in seconds (10 - 3600, default = 60).")    
    hostname_ttl: int | None = Field(ge=60, le=86400, default=86400, description="TTL of hostname table entries (60 - 86400).")    
    hostname_limit: int | None = Field(ge=0, le=50000, default=5000, description="Limit of the number of hostname table entries (0 - 50000).")    
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
            >>> policy = DnsModel(
            ...     ssl_certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dns.post(policy.to_fortios_dict())
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
            >>> policy = DnsModel(
            ...     source_ip_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_source_ip_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dns.post(policy.to_fortios_dict())
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
            >>> policy = DnsModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dns.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_ssl_certificate_references(client)
        all_errors.extend(errors)        
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
    "DnsModel",    "DnsServerHostname",    "DnsDomain",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.213861Z
# ============================================================================
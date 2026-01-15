"""
Pydantic Models for CMDB - dnsfilter/profile

Runtime validation models for dnsfilter/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileDomainFilter(BaseModel):
    """
    Child table model for domain-filter.
    
    Domain filter settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    domain_filter_table: int | None = Field(ge=0, le=4294967295, default=0, description="DNS domain filter table ID.")  # datasource: ['dnsfilter.domain-filter.id']
class ProfileFtgdDns(BaseModel):
    """
    Child table model for ftgd-dns.
    
    FortiGuard DNS Filter settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    options: list[Options] = Field(default="", description="FortiGuard DNS filter options.")    
    filters: list[Filters] = Field(default=None, description="FortiGuard DNS domain filters.")
class ProfileExternalIpBlocklist(BaseModel):
    """
    Child table model for external-ip-blocklist.
    
    One or more external IP block lists.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="External domain block list name.")  # datasource: ['system.external-resource.name']
class ProfileDnsTranslation(BaseModel):
    """
    Child table model for dns-translation.
    
    DNS translation settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    addr_type: Literal["ipv4", "ipv6"] = Field(default="ipv4", description="DNS translation type (IPv4 or IPv6).")    
    src: str | None = Field(default="0.0.0.0", description="IPv4 address or subnet on the internal network to compare with the resolved address in DNS query replies. If the resolved address matches, the resolved address is substituted with dst.")    
    dst: str | None = Field(default="0.0.0.0", description="IPv4 address or subnet on the external network to substitute for the resolved address in DNS query replies. Can be single IP address or subnet on the external network, but number of addresses must equal number of mapped IP addresses in src.")    
    netmask: str | None = Field(default="255.255.255.255", description="If src and dst are subnets rather than single IP addresses, enter the netmask for both src and dst.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this DNS translation entry.")    
    src6: str | None = Field(default="::", description="IPv6 address or subnet on the internal network to compare with the resolved address in DNS query replies. If the resolved address matches, the resolved address is substituted with dst6.")    
    dst6: str | None = Field(default="::", description="IPv6 address or subnet on the external network to substitute for the resolved address in DNS query replies. Can be single IP address or subnet on the external network, but number of addresses must equal number of mapped IP addresses in src6.")    
    prefix: int | None = Field(ge=1, le=128, default=128, description="If src6 and dst6 are subnets rather than single IP addresses, enter the prefix for both src6 and dst6 (1 - 128, default = 128).")
class ProfileTransparentDnsDatabase(BaseModel):
    """
    Child table model for transparent-dns-database.
    
    Transparent DNS database zones.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="DNS database zone name.")  # datasource: ['system.dns-database.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for dnsfilter/profile configuration.
    
    Configure DNS domain filter profile.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - domain_filter: pattern=        - ftgd_dns: pattern=        - log_all_domain: pattern=        - sdns_ftgd_err_log: pattern=        - sdns_domain_log: pattern=        - block_action: pattern=        - redirect_portal: pattern=        - redirect_portal6: pattern=        - block_botnet: pattern=        - safe_search: pattern=        - youtube_restrict: pattern=        - external_ip_blocklist: pattern=        - dns_translation: pattern=        - transparent_dns_database: pattern=        - strip_ech: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Profile name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    domain_filter: list[DomainFilter] = Field(default=None, description="Domain filter settings.")    
    ftgd_dns: list[FtgdDns] = Field(default=None, description="FortiGuard DNS Filter settings.")    
    log_all_domain: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging of all domains visited (detailed DNS logging).")    
    sdns_ftgd_err_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiGuard SDNS rating error logging.")    
    sdns_domain_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable domain filtering and botnet domain logging.")    
    block_action: Literal["block", "redirect", "block-sevrfail"] | None = Field(default="redirect", description="Action to take for blocked domains.")    
    redirect_portal: str | None = Field(default="0.0.0.0", description="IPv4 address of the SDNS redirect portal.")    
    redirect_portal6: str | None = Field(default="::", description="IPv6 address of the SDNS redirect portal.")    
    block_botnet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable blocking botnet C&C DNS lookups.")    
    safe_search: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable Google, Bing, YouTube, Qwant, DuckDuckGo safe search.")    
    youtube_restrict: Literal["strict", "moderate", "none"] | None = Field(default="strict", description="Set safe search for YouTube restriction level.")    
    external_ip_blocklist: list[ExternalIpBlocklist] = Field(default=None, description="One or more external IP block lists.")    
    dns_translation: list[DnsTranslation] = Field(default=None, description="DNS translation settings.")    
    transparent_dns_database: list[TransparentDnsDatabase] = Field(default=None, description="Transparent DNS database zones.")    
    strip_ech: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable removal of the encrypted client hello service parameter from supporting DNS RRs.")    
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
    async def validate_domain_filter_references(self, client: Any) -> list[str]:
        """
        Validate domain_filter references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dnsfilter/domain-filter        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     domain_filter=[{"domain-filter-table": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_domain_filter_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dnsfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "domain_filter", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("domain-filter-table")
            else:
                value = getattr(item, "domain-filter-table", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.dnsfilter.domain-filter.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Domain-Filter '{value}' not found in "
                    "dnsfilter/domain-filter"
                )        
        return errors    
    async def validate_external_ip_blocklist_references(self, client: Any) -> list[str]:
        """
        Validate external_ip_blocklist references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     external_ip_blocklist=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_external_ip_blocklist_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dnsfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "external_ip_blocklist", [])
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
            if await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"External-Ip-Blocklist '{value}' not found in "
                    "system/external-resource"
                )        
        return errors    
    async def validate_transparent_dns_database_references(self, client: Any) -> list[str]:
        """
        Validate transparent_dns_database references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/dns-database        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     transparent_dns_database=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_transparent_dns_database_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dnsfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "transparent_dns_database", [])
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
            if await client.api.cmdb.system.dns-database.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Transparent-Dns-Database '{value}' not found in "
                    "system/dns-database"
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
        
        errors = await self.validate_domain_filter_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_external_ip_blocklist_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_transparent_dns_database_references(client)
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
    "ProfileModel",    "ProfileDomainFilter",    "ProfileFtgdDns",    "ProfileExternalIpBlocklist",    "ProfileDnsTranslation",    "ProfileTransparentDnsDatabase",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.795555Z
# ============================================================================
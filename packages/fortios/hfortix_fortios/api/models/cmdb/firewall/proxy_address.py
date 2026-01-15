"""
Pydantic Models for CMDB - firewall/proxy_address

Runtime validation models for firewall/proxy_address configuration.
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

class ProxyAddressCategory(BaseModel):
    """
    Child table model for category.
    
    FortiGuard category ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="FortiGuard category ID.")
class ProxyAddressHeaderGroup(BaseModel):
    """
    Child table model for header-group.
    
    HTTP header group.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    header_name: str = Field(max_length=79, default="", description="HTTP header.")    
    header: str = Field(max_length=255, default="", description="HTTP header regular expression.")    
    case_sensitivity: Literal["disable", "enable"] | None = Field(default="disable", description="Case sensitivity in pattern.")
class ProxyAddressTagging(BaseModel):
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
class ProxyAddressApplication(BaseModel):
    """
    Child table model for application.
    
    SaaS application.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="SaaS application name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProxyAddressTypeEnum(str, Enum):
    """Allowed values for type field."""
    HOST_REGEX = "host-regex"    URL = "url"    CATEGORY = "category"    METHOD = "method"    UA = "ua"    HEADER = "header"    SRC_ADVANCED = "src-advanced"    DST_ADVANCED = "dst-advanced"    SAAS = "saas"
class ProxyAddressMethodEnum(str, Enum):
    """Allowed values for method field."""
    GET = "get"    POST = "post"    PUT = "put"    HEAD = "head"    CONNECT = "connect"    TRACE = "trace"    OPTIONS = "options"    DELETE = "delete"    UPDATE = "update"    PATCH = "patch"    OTHER = "other"
class ProxyAddressUaEnum(str, Enum):
    """Allowed values for ua field."""
    CHROME = "chrome"    MS = "ms"    FIREFOX = "firefox"    SAFARI = "safari"    IE = "ie"    EDGE = "edge"    OTHER = "other"

# ============================================================================
# Main Model
# ============================================================================

class ProxyAddressModel(BaseModel):
    """
    Pydantic model for firewall/proxy_address configuration.
    
    Configure web proxy address.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: pattern=        - type: pattern=        - host: max_length=79 pattern=        - host_regex: max_length=255 pattern=        - path: max_length=255 pattern=        - query: max_length=255 pattern=        - referrer: pattern=        - category: pattern=        - method: pattern=        - ua: pattern=        - ua_min_ver: max_length=63 pattern=        - ua_max_ver: max_length=63 pattern=        - header_name: max_length=79 pattern=        - header: max_length=255 pattern=        - case_sensitivity: pattern=        - header_group: pattern=        - color: min=0 max=32 pattern=        - tagging: pattern=        - comment: max_length=255 pattern=        - application: pattern=    """
    
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
    type: TypeEnum | None = Field(default="url", description="Proxy address type.")    
    host: str = Field(max_length=79, default="", description="Address object for the host.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.vipgrp.name', 'firewall.vip.name']    
    host_regex: str | None = Field(max_length=255, default="", description="Host name as a regular expression.")    
    path: str | None = Field(max_length=255, default="", description="URL path as a regular expression.")    
    query: str | None = Field(max_length=255, default="", description="Match the query part of the URL as a regular expression.")    
    referrer: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of referrer field in the HTTP header to match the address.")    
    category: list[Category] = Field(default=None, description="FortiGuard category ID.")    
    method: list[Method] = Field(default="", description="HTTP request methods to be used.")    
    ua: list[Ua] = Field(default="", description="Names of browsers to be used as user agent.")    
    ua_min_ver: str | None = Field(max_length=63, default="", description="Minimum version of the user agent specified in dotted notation. For example, use 90.0.1 with the ua field set to \"chrome\" to require Google Chrome's minimum version must be 90.0.1.")    
    ua_max_ver: str | None = Field(max_length=63, default="", description="Maximum version of the user agent specified in dotted notation. For example, use 120 with the ua field set to \"chrome\" to require Google Chrome's maximum version must be 120.")    
    header_name: str | None = Field(max_length=79, default="", description="Name of HTTP header.")    
    header: str | None = Field(max_length=255, default="", description="HTTP header name as a regular expression.")    
    case_sensitivity: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to make the pattern case sensitive.")    
    header_group: list[HeaderGroup] = Field(default=None, description="HTTP header group.")    
    color: int | None = Field(ge=0, le=32, default=0, description="Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1).")    
    tagging: list[Tagging] = Field(default=None, description="Config object tagging.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    application: list[Application] = Field(description="SaaS application.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('host')
    @classmethod
    def validate_host(cls, v: Any) -> Any:
        """
        Validate host field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.vipgrp.name', 'firewall.vip.name']
        
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
    async def validate_host_references(self, client: Any) -> list[str]:
        """
        Validate host references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - firewall/proxy-address        - firewall/vipgrp        - firewall/vip        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProxyAddressModel(
            ...     host="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_host_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_address.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "host", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        elif await client.api.cmdb.firewall.proxy-address.exists(value):
            found = True
        elif await client.api.cmdb.firewall.vipgrp.exists(value):
            found = True
        elif await client.api.cmdb.firewall.vip.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Host '{value}' not found in "
                "firewall/address or firewall/addrgrp or firewall/proxy-address or firewall/vipgrp or firewall/vip"
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
            >>> policy = ProxyAddressModel(
            ...     tagging=[{"category": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tagging_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.proxy_address.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_host_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_tagging_references(client)
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
    "ProxyAddressModel",    "ProxyAddressCategory",    "ProxyAddressHeaderGroup",    "ProxyAddressTagging",    "ProxyAddressApplication",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.382019Z
# ============================================================================
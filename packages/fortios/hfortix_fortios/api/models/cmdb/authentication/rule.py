"""
Pydantic Models for CMDB - authentication/rule

Runtime validation models for authentication/rule configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class RuleSrcintf(BaseModel):
    """
    Child table model for srcintf.
    
    Incoming (ingress) interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Interface name.")  # datasource: ['system.interface.name', 'system.zone.name', 'system.sdwan.zone.name']
class RuleSrcaddr(BaseModel):
    """
    Child table model for srcaddr.
    
    Authentication is required for the selected IPv4 source address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'system.external-resource.name']
class RuleDstaddr(BaseModel):
    """
    Child table model for dstaddr.
    
    Select an IPv4 destination address from available options. Required for web proxy authentication.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name', 'firewall.proxy-address.name', 'firewall.proxy-addrgrp.name', 'system.external-resource.name']
class RuleSrcaddr6(BaseModel):
    """
    Child table model for srcaddr6.
    
    Authentication is required for the selected IPv6 source address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
class RuleDstaddr6(BaseModel):
    """
    Child table model for dstaddr6.
    
    Select an IPv6 destination address from available options. Required for web proxy authentication.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class RuleProtocolEnum(str, Enum):
    """Allowed values for protocol field."""
    HTTP = "http"    FTP = "ftp"    SOCKS = "socks"    SSH = "ssh"    ZTNA_PORTAL = "ztna-portal"

# ============================================================================
# Main Model
# ============================================================================

class RuleModel(BaseModel):
    """
    Pydantic model for authentication/rule configuration.
    
    Configure Authentication Rules.
    
    Validation Rules:        - name: max_length=35 pattern=        - status: pattern=        - protocol: pattern=        - srcintf: pattern=        - srcaddr: pattern=        - dstaddr: pattern=        - srcaddr6: pattern=        - dstaddr6: pattern=        - ip_based: pattern=        - active_auth_method: max_length=35 pattern=        - sso_auth_method: max_length=35 pattern=        - web_auth_cookie: pattern=        - cors_stateful: pattern=        - cors_depth: min=1 max=8 pattern=        - cert_auth_cookie: pattern=        - transaction_based: pattern=        - web_portal: pattern=        - comments: max_length=1023 pattern=        - session_logout: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Authentication rule name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this authentication rule.")    
    protocol: ProtocolEnum | None = Field(default="http", description="Authentication is required for the selected protocol (default = HTTP).")    
    srcintf: list[Srcintf] = Field(default=None, description="Incoming (ingress) interface.")    
    srcaddr: list[Srcaddr] = Field(default=None, description="Authentication is required for the selected IPv4 source address.")    
    dstaddr: list[Dstaddr] = Field(default=None, description="Select an IPv4 destination address from available options. Required for web proxy authentication.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Authentication is required for the selected IPv6 source address.")    
    dstaddr6: list[Dstaddr6] = Field(default=None, description="Select an IPv6 destination address from available options. Required for web proxy authentication.")    
    ip_based: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IP-based authentication. When enabled, previously authenticated users from the same IP address will be exempted.")    
    active_auth_method: str | None = Field(max_length=35, default="", description="Select an active authentication method.")  # datasource: ['authentication.scheme.name']    
    sso_auth_method: str | None = Field(max_length=35, default="", description="Select a single-sign on (SSO) authentication method.")  # datasource: ['authentication.scheme.name']    
    web_auth_cookie: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Web authentication cookies (default = disable).")    
    cors_stateful: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowance of CORS access (default = disable).")    
    cors_depth: int | None = Field(ge=1, le=8, default=3, description="Depth to allow CORS access (default = 3).")    
    cert_auth_cookie: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable to use device certificate as authentication cookie (default = enable).")    
    transaction_based: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable transaction based authentication (default = disable).")    
    web_portal: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable web portal for proxy transparent policy (default = enable).")    
    comments: str | None = Field(max_length=1023, default=None, description="Comment.")    
    session_logout: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logout of a user from the current session.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('active_auth_method')
    @classmethod
    def validate_active_auth_method(cls, v: Any) -> Any:
        """
        Validate active_auth_method field.
        
        Datasource: ['authentication.scheme.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sso_auth_method')
    @classmethod
    def validate_sso_auth_method(cls, v: Any) -> Any:
        """
        Validate sso_auth_method field.
        
        Datasource: ['authentication.scheme.name']
        
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
            >>> policy = RuleModel(
            ...     srcintf=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.rule.post(policy.to_fortios_dict())
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
    async def validate_srcaddr_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - firewall/proxy-address        - firewall/proxy-addrgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RuleModel(
            ...     srcaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.rule.post(policy.to_fortios_dict())
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
            elif await client.api.cmdb.firewall.proxy-address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.proxy-addrgrp.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Srcaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp or firewall/proxy-address or firewall/proxy-addrgrp or system/external-resource"
                )        
        return errors    
    async def validate_dstaddr_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        - firewall/proxy-address        - firewall/proxy-addrgrp        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RuleModel(
            ...     dstaddr=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.rule.post(policy.to_fortios_dict())
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
            if await client.api.cmdb.firewall.address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.addrgrp.exists(value):
                found = True
            elif await client.api.cmdb.firewall.proxy-address.exists(value):
                found = True
            elif await client.api.cmdb.firewall.proxy-addrgrp.exists(value):
                found = True
            elif await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Dstaddr '{value}' not found in "
                    "firewall/address or firewall/addrgrp or firewall/proxy-address or firewall/proxy-addrgrp or system/external-resource"
                )        
        return errors    
    async def validate_srcaddr6_references(self, client: Any) -> list[str]:
        """
        Validate srcaddr6 references exist in FortiGate.
        
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
            >>> policy = RuleModel(
            ...     srcaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.rule.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "srcaddr6", [])
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
                    f"Srcaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6"
                )        
        return errors    
    async def validate_dstaddr6_references(self, client: Any) -> list[str]:
        """
        Validate dstaddr6 references exist in FortiGate.
        
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
            >>> policy = RuleModel(
            ...     dstaddr6=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dstaddr6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.rule.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dstaddr6", [])
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
                    f"Dstaddr6 '{value}' not found in "
                    "firewall/address6 or firewall/addrgrp6"
                )        
        return errors    
    async def validate_active_auth_method_references(self, client: Any) -> list[str]:
        """
        Validate active_auth_method references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - authentication/scheme        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RuleModel(
            ...     active_auth_method="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_active_auth_method_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.rule.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "active_auth_method", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.authentication.scheme.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Active-Auth-Method '{value}' not found in "
                "authentication/scheme"
            )        
        return errors    
    async def validate_sso_auth_method_references(self, client: Any) -> list[str]:
        """
        Validate sso_auth_method references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - authentication/scheme        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RuleModel(
            ...     sso_auth_method="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sso_auth_method_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.rule.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "sso_auth_method", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.authentication.scheme.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Sso-Auth-Method '{value}' not found in "
                "authentication/scheme"
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
        errors = await self.validate_srcaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_srcaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dstaddr6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_active_auth_method_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sso_auth_method_references(client)
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
    "RuleModel",    "RuleSrcintf",    "RuleSrcaddr",    "RuleDstaddr",    "RuleSrcaddr6",    "RuleDstaddr6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.279566Z
# ============================================================================
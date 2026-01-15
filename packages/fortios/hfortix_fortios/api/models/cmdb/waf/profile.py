"""
Pydantic Models for CMDB - waf/profile

Runtime validation models for waf/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileSignature(BaseModel):
    """
    Child table model for signature.
    
    WAF signatures.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    main_class: list[MainClass] = Field(default=None, description="Main signature class.")    
    disabled_sub_class: list[DisabledSubClass] = Field(default=None, description="Disabled signature subclasses.")    
    disabled_signature: list[DisabledSignature] = Field(default=None, description="Disabled signatures.")    
    credit_card_detection_threshold: int | None = Field(ge=0, le=128, default=3, description="The minimum number of Credit cards to detect violation.")    
    custom_signature: list[CustomSignature] = Field(default=None, description="Custom signature.")
class ProfileConstraint(BaseModel):
    """
    Child table model for constraint.
    
    WAF HTTP protocol restrictions.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    header_length: list[HeaderLength] = Field(default=None, description="HTTP header length in request.")    
    content_length: list[ContentLength] = Field(default=None, description="HTTP content length in request.")    
    param_length: list[ParamLength] = Field(default=None, description="Maximum length of parameter in URL, HTTP POST request or HTTP body.")    
    line_length: list[LineLength] = Field(default=None, description="HTTP line length in request.")    
    url_param_length: list[UrlParamLength] = Field(default=None, description="Maximum length of parameter in URL.")    
    version: list[Version] = Field(default=None, description="Enable/disable HTTP version check.")    
    method: list[Method] = Field(default=None, description="Enable/disable HTTP method check.")    
    hostname: list[Hostname] = Field(default=None, description="Enable/disable hostname check.")    
    malformed: list[Malformed] = Field(default=None, description="Enable/disable malformed HTTP request check.")    
    max_cookie: list[MaxCookie] = Field(default=None, description="Maximum number of cookies in HTTP request.")    
    max_header_line: list[MaxHeaderLine] = Field(default=None, description="Maximum number of HTTP header line.")    
    max_url_param: list[MaxUrlParam] = Field(default=None, description="Maximum number of parameters in URL.")    
    max_range_segment: list[MaxRangeSegment] = Field(default=None, description="Maximum number of range segments in HTTP range line.")    
    exception: list[Exception] = Field(default=None, description="HTTP constraint exception.")
class ProfileMethod(BaseModel):
    """
    Child table model for method.
    
    Method restriction.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging.")    
    severity: Literal["high", "medium", "low"] | None = Field(default="medium", description="Severity.")    
    default_allowed_methods: list[DefaultAllowedMethods] = Field(default="", description="Methods.")    
    method_policy: list[MethodPolicy] = Field(default=None, description="HTTP method policy.")
class ProfileAddressList(BaseModel):
    """
    Child table model for address-list.
    
    Address block and allow lists.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    blocked_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging on blocked addresses.")    
    severity: Literal["high", "medium", "low"] | None = Field(default="medium", description="Severity.")    
    trusted_address: list[TrustedAddress] = Field(default=None, description="Trusted address.")    
    blocked_address: list[BlockedAddress] = Field(default=None, description="Blocked address.")
class ProfileUrlAccess(BaseModel):
    """
    Child table model for url-access.
    
    URL access list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="URL access ID.")    
    address: str = Field(max_length=79, default="", description="Host address.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    action: Literal["bypass", "permit", "block"] | None = Field(default="permit", description="Action.")    
    log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging.")    
    severity: Literal["high", "medium", "low"] | None = Field(default="medium", description="Severity.")    
    access_pattern: list[AccessPattern] = Field(default=None, description="URL access pattern.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for waf/profile configuration.
    
    Configure Web application firewall configuration.
    
    Validation Rules:        - name: max_length=47 pattern=        - external: pattern=        - extended_log: pattern=        - signature: pattern=        - constraint: pattern=        - method: pattern=        - address_list: pattern=        - url_access: pattern=        - comment: max_length=1023 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=47, default="", description="WAF Profile name.")    
    external: Literal["disable", "enable"] | None = Field(default="disable", description="Disable/Enable external HTTP Inspection.")    
    extended_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended logging.")    
    signature: list[Signature] = Field(default=None, description="WAF signatures.")    
    constraint: list[Constraint] = Field(default=None, description="WAF HTTP protocol restrictions.")    
    method: list[Method] = Field(default=None, description="Method restriction.")    
    address_list: list[AddressList] = Field(default=None, description="Address block and allow lists.")    
    url_access: list[UrlAccess] = Field(default=None, description="URL access list.")    
    comment: str | None = Field(max_length=1023, default=None, description="Comment.")    
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
    async def validate_url_access_references(self, client: Any) -> list[str]:
        """
        Validate url_access references exist in FortiGate.
        
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
            >>> policy = ProfileModel(
            ...     url_access=[{"address": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_url_access_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.waf.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "url_access", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("address")
            else:
                value = getattr(item, "address", None)
            
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
                    f"Url-Access '{value}' not found in "
                    "firewall/address or firewall/addrgrp"
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
        
        errors = await self.validate_url_access_references(client)
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
    "ProfileModel",    "ProfileSignature",    "ProfileConstraint",    "ProfileMethod",    "ProfileAddressList",    "ProfileUrlAccess",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.535633Z
# ============================================================================
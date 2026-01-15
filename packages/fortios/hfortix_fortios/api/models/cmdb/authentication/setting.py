"""
Pydantic Models for CMDB - authentication/setting

Runtime validation models for authentication/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class SettingUserCertCa(BaseModel):
    """
    Child table model for user-cert-ca.
    
    CA certificate used for client certificate verification.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="CA certificate list.")  # datasource: ['vpn.certificate.ca.name', 'vpn.certificate.local.name']
class SettingDevRange(BaseModel):
    """
    Child table model for dev-range.
    
    Address range for the IP based device query.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Address name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for authentication/setting configuration.
    
    Configure authentication setting.
    
    Validation Rules:        - active_auth_scheme: max_length=35 pattern=        - sso_auth_scheme: max_length=35 pattern=        - update_time: pattern=        - persistent_cookie: pattern=        - ip_auth_cookie: pattern=        - cookie_max_age: min=30 max=10080 pattern=        - cookie_refresh_div: min=2 max=4 pattern=        - captive_portal_type: pattern=        - captive_portal_ip: pattern=        - captive_portal_ip6: pattern=        - captive_portal: max_length=255 pattern=        - captive_portal6: max_length=255 pattern=        - cert_auth: pattern=        - cert_captive_portal: max_length=255 pattern=        - cert_captive_portal_ip: pattern=        - cert_captive_portal_port: min=1 max=65535 pattern=        - captive_portal_port: min=1 max=65535 pattern=        - auth_https: pattern=        - captive_portal_ssl_port: min=1 max=65535 pattern=        - user_cert_ca: pattern=        - dev_range: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    active_auth_scheme: str | None = Field(max_length=35, default="", description="Active authentication method (scheme name).")  # datasource: ['authentication.scheme.name']    
    sso_auth_scheme: str | None = Field(max_length=35, default="", description="Single-Sign-On authentication method (scheme name).")  # datasource: ['authentication.scheme.name']    
    update_time: str | None = Field(default="", description="Time of the last update.")    
    persistent_cookie: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable persistent cookie on web portal authentication (default = enable).")    
    ip_auth_cookie: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable persistent cookie on IP based web portal authentication (default = disable).")    
    cookie_max_age: int | None = Field(ge=30, le=10080, default=480, description="Persistent web portal cookie maximum age in minutes (30 - 10080 (1 week), default = 480 (8 hours)).")    
    cookie_refresh_div: int | None = Field(ge=2, le=4, default=2, description="Refresh rate divider of persistent web portal cookie (default = 2). Refresh value = cookie-max-age/cookie-refresh-div.")    
    captive_portal_type: Literal["fqdn", "ip"] | None = Field(default="fqdn", description="Captive portal type.")    
    captive_portal_ip: str | None = Field(default="0.0.0.0", description="Captive portal IP address.")    
    captive_portal_ip6: str | None = Field(default="::", description="Captive portal IPv6 address.")    
    captive_portal: str | None = Field(max_length=255, default="", description="Captive portal host name.")  # datasource: ['firewall.address.name']    
    captive_portal6: str | None = Field(max_length=255, default="", description="IPv6 captive portal host name.")  # datasource: ['firewall.address6.name']    
    cert_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redirecting certificate authentication to HTTPS portal.")    
    cert_captive_portal: str | None = Field(max_length=255, default="", description="Certificate captive portal host name.")  # datasource: ['firewall.address.name']    
    cert_captive_portal_ip: str | None = Field(default="0.0.0.0", description="Certificate captive portal IP address.")    
    cert_captive_portal_port: int | None = Field(ge=1, le=65535, default=7832, description="Certificate captive portal port number (1 - 65535, default = 7832).")    
    captive_portal_port: int | None = Field(ge=1, le=65535, default=7830, description="Captive portal port number (1 - 65535, default = 7830).")    
    auth_https: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable redirecting HTTP user authentication to HTTPS.")    
    captive_portal_ssl_port: int | None = Field(ge=1, le=65535, default=7831, description="Captive portal SSL port number (1 - 65535, default = 7831).")    
    user_cert_ca: list[UserCertCa] = Field(default=None, description="CA certificate used for client certificate verification.")    
    dev_range: list[DevRange] = Field(default=None, description="Address range for the IP based device query.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('active_auth_scheme')
    @classmethod
    def validate_active_auth_scheme(cls, v: Any) -> Any:
        """
        Validate active_auth_scheme field.
        
        Datasource: ['authentication.scheme.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('sso_auth_scheme')
    @classmethod
    def validate_sso_auth_scheme(cls, v: Any) -> Any:
        """
        Validate sso_auth_scheme field.
        
        Datasource: ['authentication.scheme.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('captive_portal')
    @classmethod
    def validate_captive_portal(cls, v: Any) -> Any:
        """
        Validate captive_portal field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('captive_portal6')
    @classmethod
    def validate_captive_portal6(cls, v: Any) -> Any:
        """
        Validate captive_portal6 field.
        
        Datasource: ['firewall.address6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('cert_captive_portal')
    @classmethod
    def validate_cert_captive_portal(cls, v: Any) -> Any:
        """
        Validate cert_captive_portal field.
        
        Datasource: ['firewall.address.name']
        
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
    async def validate_active_auth_scheme_references(self, client: Any) -> list[str]:
        """
        Validate active_auth_scheme references exist in FortiGate.
        
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
            >>> policy = SettingModel(
            ...     active_auth_scheme="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_active_auth_scheme_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "active_auth_scheme", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.authentication.scheme.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Active-Auth-Scheme '{value}' not found in "
                "authentication/scheme"
            )        
        return errors    
    async def validate_sso_auth_scheme_references(self, client: Any) -> list[str]:
        """
        Validate sso_auth_scheme references exist in FortiGate.
        
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
            >>> policy = SettingModel(
            ...     sso_auth_scheme="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sso_auth_scheme_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "sso_auth_scheme", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.authentication.scheme.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Sso-Auth-Scheme '{value}' not found in "
                "authentication/scheme"
            )        
        return errors    
    async def validate_captive_portal_references(self, client: Any) -> list[str]:
        """
        Validate captive_portal references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     captive_portal="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_captive_portal_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "captive_portal", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Captive-Portal '{value}' not found in "
                "firewall/address"
            )        
        return errors    
    async def validate_captive_portal6_references(self, client: Any) -> list[str]:
        """
        Validate captive_portal6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     captive_portal6="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_captive_portal6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "captive_portal6", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Captive-Portal6 '{value}' not found in "
                "firewall/address6"
            )        
        return errors    
    async def validate_cert_captive_portal_references(self, client: Any) -> list[str]:
        """
        Validate cert_captive_portal references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     cert_captive_portal="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_cert_captive_portal_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "cert_captive_portal", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Cert-Captive-Portal '{value}' not found in "
                "firewall/address"
            )        
        return errors    
    async def validate_user_cert_ca_references(self, client: Any) -> list[str]:
        """
        Validate user_cert_ca references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/ca        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     user_cert_ca=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_user_cert_ca_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "user_cert_ca", [])
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
            if await client.api.cmdb.vpn.certificate.ca.exists(value):
                found = True
            elif await client.api.cmdb.vpn.certificate.local.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"User-Cert-Ca '{value}' not found in "
                    "vpn/certificate/ca or vpn/certificate/local"
                )        
        return errors    
    async def validate_dev_range_references(self, client: Any) -> list[str]:
        """
        Validate dev_range references exist in FortiGate.
        
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
            >>> policy = SettingModel(
            ...     dev_range=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dev_range_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.authentication.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "dev_range", [])
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
                    f"Dev-Range '{value}' not found in "
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
        
        errors = await self.validate_active_auth_scheme_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_sso_auth_scheme_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_captive_portal_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_captive_portal6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_cert_captive_portal_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_user_cert_ca_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dev_range_references(client)
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
    "SettingModel",    "SettingUserCertCa",    "SettingDevRange",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.783039Z
# ============================================================================
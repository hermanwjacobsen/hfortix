"""
Pydantic Models for CMDB - user/setting

Runtime validation models for user/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SettingAuthPorts(BaseModel):
    """
    Child table model for auth-ports.
    
    Set up non-standard ports for authentication with HTTP, HTTPS, FTP, and TELNET.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    type: TypeEnum | None = Field(default="http", description="Service type.")    
    port: int | None = Field(ge=1, le=65535, default=1024, description="Non-standard port for firewall user authentication.")
class SettingCorsAllowedOrigins(BaseModel):
    """
    Child table model for cors-allowed-origins.
    
    Allowed origins white list for CORS.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Allowed origin for CORS.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingAuth_typeEnum(str, Enum):
    """Allowed values for auth_type field."""
    HTTP = "http"    HTTPS = "https"    FTP = "ftp"    TELNET = "telnet"
class SettingAuth_ssl_min_proto_versionEnum(str, Enum):
    """Allowed values for auth_ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"
class SettingAuth_ssl_max_proto_versionEnum(str, Enum):
    """Allowed values for auth_ssl_max_proto_version field."""
    SSLV3 = "sslv3"    TLSV1 = "tlsv1"    TLSV1_1 = "tlsv1-1"    TLSV1_2 = "tlsv1-2"    TLSV1_3 = "tlsv1-3"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for user/setting configuration.
    
    Configure user authentication setting.
    
    Validation Rules:        - auth_type: pattern=        - auth_cert: max_length=35 pattern=        - auth_ca_cert: max_length=35 pattern=        - auth_secure_http: pattern=        - auth_http_basic: pattern=        - auth_ssl_allow_renegotiation: pattern=        - auth_src_mac: pattern=        - auth_on_demand: pattern=        - auth_timeout: min=1 max=1440 pattern=        - auth_timeout_type: pattern=        - auth_portal_timeout: min=1 max=30 pattern=        - radius_ses_timeout_act: pattern=        - auth_blackout_time: min=0 max=3600 pattern=        - auth_invalid_max: min=1 max=100 pattern=        - auth_lockout_threshold: min=1 max=10 pattern=        - auth_lockout_duration: min=0 max=4294967295 pattern=        - per_policy_disclaimer: pattern=        - auth_ports: pattern=        - auth_ssl_min_proto_version: pattern=        - auth_ssl_max_proto_version: pattern=        - auth_ssl_sigalgs: pattern=        - default_user_password_policy: max_length=35 pattern=        - cors: pattern=        - cors_allowed_origins: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    auth_type: list[AuthType] = Field(default="http https ftp telnet", description="Supported firewall policy authentication protocols/methods.")    
    auth_cert: str | None = Field(max_length=35, default="", description="HTTPS server certificate for policy authentication.")  # datasource: ['vpn.certificate.local.name']    
    auth_ca_cert: str | None = Field(max_length=35, default="", description="HTTPS CA certificate for policy authentication.")  # datasource: ['vpn.certificate.local.name']    
    auth_secure_http: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redirecting HTTP user authentication to more secure HTTPS.")    
    auth_http_basic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of HTTP basic authentication for identity-based firewall policies.")    
    auth_ssl_allow_renegotiation: Literal["enable", "disable"] | None = Field(default="disable", description="Allow/forbid SSL re-negotiation for HTTPS authentication.")    
    auth_src_mac: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable source MAC for user identity.")    
    auth_on_demand: Literal["always", "implicitly"] | None = Field(default="implicitly", description="Always/implicitly trigger firewall authentication on demand.")    
    auth_timeout: int | None = Field(ge=1, le=1440, default=5, description="Time in minutes before the firewall user authentication timeout requires the user to re-authenticate.")    
    auth_timeout_type: Literal["idle-timeout", "hard-timeout", "new-session"] | None = Field(default="idle-timeout", description="Control if authenticated users have to login again after a hard timeout, after an idle timeout, or after a session timeout.")    
    auth_portal_timeout: int | None = Field(ge=1, le=30, default=3, description="Time in minutes before captive portal user have to re-authenticate (1 - 30 min, default 3 min).")    
    radius_ses_timeout_act: Literal["hard-timeout", "ignore-timeout"] | None = Field(default="hard-timeout", description="Set the RADIUS session timeout to a hard timeout or to ignore RADIUS server session timeouts.")    
    auth_blackout_time: int | None = Field(ge=0, le=3600, default=0, description="Time in seconds an IP address is denied access after failing to authenticate five times within one minute.")    
    auth_invalid_max: int | None = Field(ge=1, le=100, default=5, description="Maximum number of failed authentication attempts before the user is blocked.")    
    auth_lockout_threshold: int | None = Field(ge=1, le=10, default=3, description="Maximum number of failed login attempts before login lockout is triggered.")    
    auth_lockout_duration: int | None = Field(ge=0, le=4294967295, default=0, description="Lockout period in seconds after too many login failures.")    
    per_policy_disclaimer: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable per policy disclaimer.")    
    auth_ports: list[AuthPorts] = Field(default=None, description="Set up non-standard ports for authentication with HTTP, HTTPS, FTP, and TELNET.")    
    auth_ssl_min_proto_version: AuthSslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    auth_ssl_max_proto_version: AuthSslMaxProtoVersionEnum | None = Field(default="", description="Maximum supported protocol version for SSL/TLS connections (default is no limit).")    
    auth_ssl_sigalgs: Literal["no-rsa-pss", "all"] | None = Field(default="all", description="Set signature algorithms related to HTTPS authentication (affects TLS version <= 1.2 only, default is to enable all).")    
    default_user_password_policy: str | None = Field(max_length=35, default="", description="Default password policy to apply to all local users unless otherwise specified, as defined in config user password-policy.")  # datasource: ['user.password-policy.name']    
    cors: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable allowed origins white list for CORS.")    
    cors_allowed_origins: list[CorsAllowedOrigins] = Field(default=None, description="Allowed origins white list for CORS.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('auth_cert')
    @classmethod
    def validate_auth_cert(cls, v: Any) -> Any:
        """
        Validate auth_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_ca_cert')
    @classmethod
    def validate_auth_ca_cert(cls, v: Any) -> Any:
        """
        Validate auth_ca_cert field.
        
        Datasource: ['vpn.certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('default_user_password_policy')
    @classmethod
    def validate_default_user_password_policy(cls, v: Any) -> Any:
        """
        Validate default_user_password_policy field.
        
        Datasource: ['user.password-policy.name']
        
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
    async def validate_auth_cert_references(self, client: Any) -> list[str]:
        """
        Validate auth_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     auth_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Cert '{value}' not found in "
                "vpn/certificate/local"
            )        
        return errors    
    async def validate_auth_ca_cert_references(self, client: Any) -> list[str]:
        """
        Validate auth_ca_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     auth_ca_cert="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_ca_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_ca_cert", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Ca-Cert '{value}' not found in "
                "vpn/certificate/local"
            )        
        return errors    
    async def validate_default_user_password_policy_references(self, client: Any) -> list[str]:
        """
        Validate default_user_password_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/password-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     default_user_password_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_default_user_password_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "default_user_password_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.password-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Default-User-Password-Policy '{value}' not found in "
                "user/password-policy"
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
        
        errors = await self.validate_auth_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_ca_cert_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_default_user_password_policy_references(client)
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
    "SettingModel",    "SettingAuthPorts",    "SettingCorsAllowedOrigins",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.968442Z
# ============================================================================
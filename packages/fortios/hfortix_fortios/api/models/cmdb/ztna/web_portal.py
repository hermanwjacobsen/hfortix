"""
Pydantic Models for CMDB - ztna/web_portal

Runtime validation models for ztna/web_portal configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class WebPortalThemeEnum(str, Enum):
    """Allowed values for theme field."""
    JADE = "jade"    NEUTRINO = "neutrino"    MARINER = "mariner"    GRAPHITE = "graphite"    MELONGENE = "melongene"    JET_STREAM = "jet-stream"    SECURITY_FABRIC = "security-fabric"    DARK_MATTER = "dark-matter"    ONYX = "onyx"    ECLIPSE = "eclipse"

# ============================================================================
# Main Model
# ============================================================================

class WebPortalModel(BaseModel):
    """
    Pydantic model for ztna/web_portal configuration.
    
    Configure ztna web-portal.
    
    Validation Rules:        - name: max_length=79 pattern=        - vip: max_length=79 pattern=        - host: max_length=79 pattern=        - decrypted_traffic_mirror: max_length=35 pattern=        - log_blocked_traffic: pattern=        - auth_portal: pattern=        - auth_virtual_host: max_length=79 pattern=        - vip6: max_length=79 pattern=        - auth_rule: max_length=35 pattern=        - display_bookmark: pattern=        - focus_bookmark: pattern=        - display_status: pattern=        - display_history: pattern=        - policy_auth_sso: pattern=        - heading: max_length=31 pattern=        - theme: pattern=        - clipboard: pattern=        - default_window_width: min=0 max=65535 pattern=        - default_window_height: min=0 max=65535 pattern=        - cookie_age: min=0 max=525600 pattern=        - forticlient_download: pattern=        - customize_forticlient_download_url: pattern=        - windows_forticlient_download_url: max_length=1023 pattern=        - macos_forticlient_download_url: max_length=1023 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="ZTNA proxy name.")    
    vip: str | None = Field(max_length=79, default="", description="Virtual IP name.")  # datasource: ['firewall.vip.name']    
    host: str | None = Field(max_length=79, default="", description="Virtual or real host name.")  # datasource: ['firewall.access-proxy-virtual-host.name']    
    decrypted_traffic_mirror: str | None = Field(max_length=35, default="", description="Decrypted traffic mirror.")  # datasource: ['firewall.decrypted-traffic-mirror.name']    
    log_blocked_traffic: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable logging of blocked traffic.")    
    auth_portal: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable authentication portal.")    
    auth_virtual_host: str | None = Field(max_length=79, default="", description="Virtual host for authentication portal.")  # datasource: ['firewall.access-proxy-virtual-host.name']    
    vip6: str | None = Field(max_length=79, default="", description="Virtual IPv6 name.")  # datasource: ['firewall.vip6.name']    
    auth_rule: str | None = Field(max_length=35, default="", description="Authentication Rule.")  # datasource: ['authentication.rule.name']    
    display_bookmark: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to display the web portal bookmark widget.")    
    focus_bookmark: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to prioritize the placement of the bookmark section over the quick-connection section in the ztna web-portal.")    
    display_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to display the web portal status widget.")    
    display_history: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to display the web portal user login history widget.")    
    policy_auth_sso: Literal["enable", "disable"] | None = Field(default="enable", description="Enable policy sso authentication.")    
    heading: str | None = Field(max_length=31, default="ZTNA Portal", description="Web portal heading message.")    
    theme: ThemeEnum | None = Field(default="security-fabric", description="Web portal color scheme.")    
    clipboard: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to support RDP/VPC clipboard functionality.")    
    default_window_width: int | None = Field(ge=0, le=65535, default=1024, description="Screen width (range from 0 - 65535, default = 1024).")    
    default_window_height: int | None = Field(ge=0, le=65535, default=768, description="Screen height (range from 0 - 65535, default = 768).")    
    cookie_age: int | None = Field(ge=0, le=525600, default=60, description="Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.")    
    forticlient_download: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable download option for FortiClient.")    
    customize_forticlient_download_url: Literal["enable", "disable"] | None = Field(default="disable", description="Enable support of customized download URL for FortiClient.")    
    windows_forticlient_download_url: str | None = Field(max_length=1023, default=None, description="Download URL for Windows FortiClient.")    
    macos_forticlient_download_url: str | None = Field(max_length=1023, default=None, description="Download URL for Mac FortiClient.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vip')
    @classmethod
    def validate_vip(cls, v: Any) -> Any:
        """
        Validate vip field.
        
        Datasource: ['firewall.vip.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('host')
    @classmethod
    def validate_host(cls, v: Any) -> Any:
        """
        Validate host field.
        
        Datasource: ['firewall.access-proxy-virtual-host.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('decrypted_traffic_mirror')
    @classmethod
    def validate_decrypted_traffic_mirror(cls, v: Any) -> Any:
        """
        Validate decrypted_traffic_mirror field.
        
        Datasource: ['firewall.decrypted-traffic-mirror.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_virtual_host')
    @classmethod
    def validate_auth_virtual_host(cls, v: Any) -> Any:
        """
        Validate auth_virtual_host field.
        
        Datasource: ['firewall.access-proxy-virtual-host.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('vip6')
    @classmethod
    def validate_vip6(cls, v: Any) -> Any:
        """
        Validate vip6 field.
        
        Datasource: ['firewall.vip6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_rule')
    @classmethod
    def validate_auth_rule(cls, v: Any) -> Any:
        """
        Validate auth_rule field.
        
        Datasource: ['authentication.rule.name']
        
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
    async def validate_vip_references(self, client: Any) -> list[str]:
        """
        Validate vip references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/vip        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalModel(
            ...     vip="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vip_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vip", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.vip.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Vip '{value}' not found in "
                "firewall/vip"
            )        
        return errors    
    async def validate_host_references(self, client: Any) -> list[str]:
        """
        Validate host references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/access-proxy-virtual-host        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalModel(
            ...     host="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_host_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "host", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.access-proxy-virtual-host.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Host '{value}' not found in "
                "firewall/access-proxy-virtual-host"
            )        
        return errors    
    async def validate_decrypted_traffic_mirror_references(self, client: Any) -> list[str]:
        """
        Validate decrypted_traffic_mirror references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/decrypted-traffic-mirror        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalModel(
            ...     decrypted_traffic_mirror="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_decrypted_traffic_mirror_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "decrypted_traffic_mirror", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.decrypted-traffic-mirror.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Decrypted-Traffic-Mirror '{value}' not found in "
                "firewall/decrypted-traffic-mirror"
            )        
        return errors    
    async def validate_auth_virtual_host_references(self, client: Any) -> list[str]:
        """
        Validate auth_virtual_host references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/access-proxy-virtual-host        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalModel(
            ...     auth_virtual_host="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_virtual_host_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_virtual_host", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.access-proxy-virtual-host.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Virtual-Host '{value}' not found in "
                "firewall/access-proxy-virtual-host"
            )        
        return errors    
    async def validate_vip6_references(self, client: Any) -> list[str]:
        """
        Validate vip6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/vip6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalModel(
            ...     vip6="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vip6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vip6", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.vip6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Vip6 '{value}' not found in "
                "firewall/vip6"
            )        
        return errors    
    async def validate_auth_rule_references(self, client: Any) -> list[str]:
        """
        Validate auth_rule references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - authentication/rule        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalModel(
            ...     auth_rule="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_rule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_rule", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.authentication.rule.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Rule '{value}' not found in "
                "authentication/rule"
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
        
        errors = await self.validate_vip_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_host_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_decrypted_traffic_mirror_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_virtual_host_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vip6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_rule_references(client)
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
    "WebPortalModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:58.063542Z
# ============================================================================
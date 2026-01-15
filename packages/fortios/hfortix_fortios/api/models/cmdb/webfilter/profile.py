"""
Pydantic Models for CMDB - webfilter/profile

Runtime validation models for webfilter/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileOverride(BaseModel):
    """
    Child table model for override.
    
    Web Filter override settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ovrd_cookie: Literal["allow", "deny"] | None = Field(default="deny", description="Allow/deny browser-based (cookie) overrides.")    
    ovrd_scope: OvrdScopeEnum | None = Field(default="user", description="Override scope.")    
    profile_type: Literal["list", "radius"] | None = Field(default="list", description="Override profile type.")    
    ovrd_dur_mode: Literal["constant", "ask"] | None = Field(default="constant", description="Override duration mode.")    
    ovrd_dur: str | None = Field(default="15m", description="Override duration.")    
    profile_attribute: ProfileAttributeEnum | None = Field(default="Login-LAT-Service", description="Profile attribute to retrieve from the RADIUS server.")    
    ovrd_user_group: list[OvrdUserGroup] = Field(default=None, description="User groups with permission to use the override.")    
    profile: list[Profile] = Field(default=None, description="Web filter profile with permission to create overrides.")
class ProfileWeb(BaseModel):
    """
    Child table model for web.
    
    Web content filtering settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    bword_threshold: int | None = Field(ge=0, le=2147483647, default=10, description="Banned word score threshold.")    
    bword_table: int | None = Field(ge=0, le=4294967295, default=0, description="Banned word table ID.")  # datasource: ['webfilter.content.id']    
    urlfilter_table: int | None = Field(ge=0, le=4294967295, default=0, description="URL filter table ID.")  # datasource: ['webfilter.urlfilter.id']    
    content_header_list: int | None = Field(ge=0, le=4294967295, default=0, description="Content header list.")  # datasource: ['webfilter.content-header.id']    
    blocklist: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic addition of URLs detected by FortiSandbox to blocklist.")    
    allowlist: list[Allowlist] = Field(default="", description="FortiGuard allowlist settings.")    
    safe_search: list[SafeSearch] = Field(default="", description="Safe search type.")    
    youtube_restrict: Literal["none", "strict", "moderate"] | None = Field(default="none", description="YouTube EDU filter level.")    
    vimeo_restrict: str | None = Field(max_length=63, default="", description="Set Vimeo-restrict (\"7\" = don't show mature content, \"134\" = don't show unrated and mature content). A value of cookie \"content_rating\".")    
    log_search: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging all search phrases.")    
    keyword_match: list[KeywordMatch] = Field(default=None, description="Search keywords to log when match is found.")
class ProfileFtgdWf(BaseModel):
    """
    Child table model for ftgd-wf.
    
    FortiGuard Web Filter settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    options: list[Options] = Field(default="ftgd-disable", description="Options for FortiGuard Web Filter.")    
    exempt_quota: list[ExemptQuota] = Field(default="17", description="Do not stop quota for these categories.")    
    ovrd: list[Ovrd] = Field(default="", description="Allow web filter profile overrides.")    
    filters: list[Filters] = Field(default=None, description="FortiGuard filters.")    
    risk: list[Risk] = Field(default=None, description="FortiGuard risk level settings.")    
    quota: list[Quota] = Field(default=None, description="FortiGuard traffic quota settings.")    
    max_quota_timeout: int | None = Field(ge=1, le=86400, default=300, description="Maximum FortiGuard quota used by single page view in seconds (excludes streams).")    
    rate_javascript_urls: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable rating JavaScript by URL.")    
    rate_css_urls: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable rating CSS by URL.")    
    rate_crl_urls: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable rating CRL by URL.")
class ProfileAntiphish(BaseModel):
    """
    Child table model for antiphish.
    
    AntiPhishing profile.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Toggle AntiPhishing functionality.")    
    default_action: Literal["exempt", "log", "block"] | None = Field(default="exempt", description="Action to be taken when there is no matching rule.")    
    check_uri: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable checking of GET URI parameters for known credentials.")    
    check_basic_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable checking of HTTP Basic Auth field for known credentials.")    
    check_username_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable username only matching of credentials. Action will be taken for valid usernames regardless of password validity.")    
    max_body_len: int | None = Field(ge=0, le=4294967295, default=1024, description="Maximum size of a POST body to check for credentials.")    
    inspection_entries: list[InspectionEntries] = Field(default=None, description="AntiPhishing entries.")    
    custom_patterns: list[CustomPatterns] = Field(default=None, description="Custom username and password regex patterns.")    
    authentication: Literal["domain-controller", "ldap"] = Field(default="domain-controller", description="Authentication methods.")    
    domain_controller: str | None = Field(max_length=63, default="", description="Domain for which to verify received credentials against.")  # datasource: ['user.domain-controller.name', 'credential-store.domain-controller.server-name']    
    ldap: str | None = Field(max_length=63, default="", description="LDAP server for which to verify received credentials against.")  # datasource: ['user.ldap.name']
class ProfileWispServers(BaseModel):
    """
    Child table model for wisp-servers.
    
    WISP servers.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Server name.")  # datasource: ['web-proxy.wisp.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ProfileOptionsEnum(str, Enum):
    """Allowed values for options field."""
    ACTIVEXFILTER = "activexfilter"    COOKIEFILTER = "cookiefilter"    JAVAFILTER = "javafilter"    BLOCK_INVALID_URL = "block-invalid-url"    JSCRIPT = "jscript"    JS = "js"    VBS = "vbs"    UNKNOWN = "unknown"    INTRINSIC = "intrinsic"    WF_REFERER = "wf-referer"    WF_COOKIE = "wf-cookie"    PER_USER_BAL = "per-user-bal"
class ProfileOvrd_permEnum(str, Enum):
    """Allowed values for ovrd_perm field."""
    BANNEDWORD_OVERRIDE = "bannedword-override"    URLFILTER_OVERRIDE = "urlfilter-override"    FORTIGUARD_WF_OVERRIDE = "fortiguard-wf-override"    CONTENTTYPE_CHECK_OVERRIDE = "contenttype-check-override"

# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for webfilter/profile configuration.
    
    Configure Web filter profiles.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - feature_set: pattern=        - replacemsg_group: max_length=35 pattern=        - options: pattern=        - https_replacemsg: pattern=        - web_flow_log_encoding: pattern=        - ovrd_perm: pattern=        - post_action: pattern=        - override: pattern=        - web: pattern=        - ftgd_wf: pattern=        - antiphish: pattern=        - wisp: pattern=        - wisp_servers: pattern=        - wisp_algorithm: pattern=        - log_all_url: pattern=        - web_content_log: pattern=        - web_filter_activex_log: pattern=        - web_filter_command_block_log: pattern=        - web_filter_cookie_log: pattern=        - web_filter_applet_log: pattern=        - web_filter_jscript_log: pattern=        - web_filter_js_log: pattern=        - web_filter_vbs_log: pattern=        - web_filter_unknown_log: pattern=        - web_filter_referer_log: pattern=        - web_filter_cookie_removal_log: pattern=        - web_url_log: pattern=        - web_invalid_domain_log: pattern=        - web_ftgd_err_log: pattern=        - web_ftgd_quota_usage: pattern=        - extended_log: pattern=        - web_extended_all_action_log: pattern=        - web_antiphishing_log: pattern=    """
    
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
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    feature_set: Literal["flow", "proxy"] | None = Field(default="flow", description="Flow/proxy feature set.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
    options: list[Options] = Field(default="", description="Options.")    
    https_replacemsg: Literal["enable", "disable"] | None = Field(default="enable", description="Enable replacement messages for HTTPS.")    
    web_flow_log_encoding: Literal["utf-8", "punycode"] | None = Field(default="utf-8", description="Log encoding in flow mode.")    
    ovrd_perm: list[OvrdPerm] = Field(default="", description="Permitted override types.")    
    post_action: Literal["normal", "block"] | None = Field(default="normal", description="Action taken for HTTP POST traffic.")    
    override: list[Override] = Field(default=None, description="Web Filter override settings.")    
    web: list[Web] = Field(default=None, description="Web content filtering settings.")    
    ftgd_wf: list[FtgdWf] = Field(default=None, description="FortiGuard Web Filter settings.")    
    antiphish: list[Antiphish] = Field(default=None, description="AntiPhishing profile.")    
    wisp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web proxy WISP.")    
    wisp_servers: list[WispServers] = Field(default=None, description="WISP servers.")    
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = Field(default="auto-learning", description="WISP server selection algorithm.")    
    log_all_url: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging all URLs visited.")    
    web_content_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging logging blocked web content.")    
    web_filter_activex_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging ActiveX.")    
    web_filter_command_block_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging blocked commands.")    
    web_filter_cookie_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging cookie filtering.")    
    web_filter_applet_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging Java applets.")    
    web_filter_jscript_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging JScripts.")    
    web_filter_js_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging Java scripts.")    
    web_filter_vbs_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging VBS scripts.")    
    web_filter_unknown_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging unknown scripts.")    
    web_filter_referer_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging referrers.")    
    web_filter_cookie_removal_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging blocked cookies.")    
    web_url_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging URL filtering.")    
    web_invalid_domain_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging invalid domain names.")    
    web_ftgd_err_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging rating errors.")    
    web_ftgd_quota_usage: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging daily quota usage.")    
    extended_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended logging for web filtering.")    
    web_extended_all_action_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended any filter action logging for web filtering.")    
    web_antiphishing_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging of AntiPhishing checks.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('replacemsg_group')
    @classmethod
    def validate_replacemsg_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
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
    async def validate_replacemsg_group_references(self, client: Any) -> list[str]:
        """
        Validate replacemsg_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/replacemsg-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     replacemsg_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_replacemsg_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "replacemsg_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.replacemsg-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Replacemsg-Group '{value}' not found in "
                "system/replacemsg-group"
            )        
        return errors    
    async def validate_web_references(self, client: Any) -> list[str]:
        """
        Validate web references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - webfilter/content-header        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     web=[{"content-header-list": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_web_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "web", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("content-header-list")
            else:
                value = getattr(item, "content-header-list", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.webfilter.content-header.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Web '{value}' not found in "
                    "webfilter/content-header"
                )        
        return errors    
    async def validate_antiphish_references(self, client: Any) -> list[str]:
        """
        Validate antiphish references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/ldap        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     antiphish=[{"ldap": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_antiphish_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "antiphish", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("ldap")
            else:
                value = getattr(item, "ldap", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.ldap.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Antiphish '{value}' not found in "
                    "user/ldap"
                )        
        return errors    
    async def validate_wisp_servers_references(self, client: Any) -> list[str]:
        """
        Validate wisp_servers references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - web-proxy/wisp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     wisp_servers=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wisp_servers_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "wisp_servers", [])
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
            if await client.api.cmdb.web-proxy.wisp.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Wisp-Servers '{value}' not found in "
                    "web-proxy/wisp"
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
        
        errors = await self.validate_replacemsg_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_web_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_antiphish_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_wisp_servers_references(client)
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
    "ProfileModel",    "ProfileOverride",    "ProfileWeb",    "ProfileFtgdWf",    "ProfileAntiphish",    "ProfileWispServers",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:41.508011Z
# ============================================================================
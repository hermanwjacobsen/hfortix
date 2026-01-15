"""
Pydantic Models for CMDB - ztna/web_portal_bookmark

Runtime validation models for ztna/web_portal_bookmark configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class WebPortalBookmarkUsers(BaseModel):
    """
    Child table model for users.
    
    User name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="User name.")  # datasource: ['user.local.name', 'user.certificate.name']
class WebPortalBookmarkGroups(BaseModel):
    """
    Child table model for groups.
    
    User groups.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
class WebPortalBookmarkBookmarks(BaseModel):
    """
    Child table model for bookmarks.
    
    Bookmark table.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="", description="Bookmark name.")    
    apptype: ApptypeEnum = Field(default="web", description="Application type.")    
    url: str = Field(max_length=128, description="URL parameter.")    
    host: str = Field(max_length=128, description="Host name/IP parameter.")    
    folder: str = Field(max_length=128, description="Network shared file folder parameter.")    
    domain: str | None = Field(max_length=128, default=None, description="Login domain.")    
    description: str | None = Field(max_length=128, default=None, description="Description.")    
    keyboard_layout: KeyboardLayoutEnum | None = Field(default="en-us", description="Keyboard layout.")    
    security: SecurityEnum | None = Field(default="any", description="Security mode for RDP connection (default = any).")    
    send_preconnection_id: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable sending of preconnection ID.")    
    preconnection_id: int | None = Field(ge=0, le=4294967295, default=0, description="The numeric ID of the RDP source (0-4294967295).")    
    preconnection_blob: str | None = Field(max_length=511, default=None, description="An arbitrary string which identifies the RDP source.")    
    load_balancing_info: str | None = Field(max_length=511, default=None, description="The load balancing information or cookie which should be provided to the connection broker.")    
    restricted_admin: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable restricted admin mode for RDP.")    
    port: int | None = Field(ge=0, le=65535, default=0, description="Remote port.")    
    logon_user: str | None = Field(max_length=35, default=None, description="Logon user.")    
    logon_password: Any = Field(max_length=128, default=None, description="Logon password.")    
    color_depth: Literal["32", "16", "8"] | None = Field(default="16", description="Color depth per pixel.")    
    sso: Literal["disable", "enable"] | None = Field(default="disable", description="Single sign-on.")    
    width: int | None = Field(ge=0, le=65535, default=0, description="Screen width (range from 0 - 65535, default = 0).")    
    height: int | None = Field(ge=0, le=65535, default=0, description="Screen height (range from 0 - 65535, default = 0).")    
    vnc_keyboard_layout: VncKeyboardLayoutEnum | None = Field(default="default", description="Keyboard layout.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class WebPortalBookmarkModel(BaseModel):
    """
    Pydantic model for ztna/web_portal_bookmark configuration.
    
    Configure ztna web-portal bookmark.
    
    Validation Rules:        - name: max_length=35 pattern=        - users: pattern=        - groups: pattern=        - bookmarks: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Bookmark name.")    
    users: list[Users] = Field(default=None, description="User name.")    
    groups: list[Groups] = Field(default=None, description="User groups.")    
    bookmarks: list[Bookmarks] = Field(default=None, description="Bookmark table.")    
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
    async def validate_users_references(self, client: Any) -> list[str]:
        """
        Validate users references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/local        - user/certificate        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalBookmarkModel(
            ...     users=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_users_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal_bookmark.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "users", [])
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
            if await client.api.cmdb.user.local.exists(value):
                found = True
            elif await client.api.cmdb.user.certificate.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Users '{value}' not found in "
                    "user/local or user/certificate"
                )        
        return errors    
    async def validate_groups_references(self, client: Any) -> list[str]:
        """
        Validate groups references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WebPortalBookmarkModel(
            ...     groups=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ztna.web_portal_bookmark.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "groups", [])
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
            if await client.api.cmdb.user.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Groups '{value}' not found in "
                    "user/group"
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
        
        errors = await self.validate_users_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_groups_references(client)
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
    "WebPortalBookmarkModel",    "WebPortalBookmarkUsers",    "WebPortalBookmarkGroups",    "WebPortalBookmarkBookmarks",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.083491Z
# ============================================================================
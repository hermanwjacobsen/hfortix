"""
Pydantic Models for CMDB - webfilter/override

Runtime validation models for webfilter/override configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class OverrideScopeEnum(str, Enum):
    """Allowed values for scope field."""
    USER = "user"    USER_GROUP = "user-group"    IP = "ip"    IP6 = "ip6"

# ============================================================================
# Main Model
# ============================================================================

class OverrideModel(BaseModel):
    """
    Pydantic model for webfilter/override configuration.
    
    Configure FortiGuard Web Filter administrative overrides.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - status: pattern=        - scope: pattern=        - ip: pattern=        - user: max_length=64 pattern=        - user_group: max_length=63 pattern=        - old_profile: max_length=47 pattern=        - new_profile: max_length=47 pattern=        - ip6: pattern=        - expires: pattern=        - initiator: max_length=64 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Override rule ID.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable override rule.")    
    scope: ScopeEnum | None = Field(default="user", description="Override either the specific user, user group, IPv4 address, or IPv6 address.")    
    ip: str = Field(default="0.0.0.0", description="IPv4 address which the override applies.")    
    user: str = Field(max_length=64, default="", description="Name of the user which the override applies.")    
    user_group: str = Field(max_length=63, default="", description="Specify the user group for which the override applies.")  # datasource: ['user.group.name']    
    old_profile: str = Field(max_length=47, default="", description="Name of the web filter profile which the override applies.")  # datasource: ['webfilter.profile.name']    
    new_profile: str = Field(max_length=47, default="", description="Name of the new web filter profile used by the override.")  # datasource: ['webfilter.profile.name']    
    ip6: str = Field(default="::", description="IPv6 address which the override applies.")    
    expires: str = Field(default="1970/01/01 00:00:00", description="Override expiration date and time, from 5 minutes to 365 from now (format: yyyy/mm/dd hh:mm:ss).")    
    initiator: str | None = Field(max_length=64, default="", description="Initiating user of override (read-only setting).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('user_group')
    @classmethod
    def validate_user_group(cls, v: Any) -> Any:
        """
        Validate user_group field.
        
        Datasource: ['user.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('old_profile')
    @classmethod
    def validate_old_profile(cls, v: Any) -> Any:
        """
        Validate old_profile field.
        
        Datasource: ['webfilter.profile.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('new_profile')
    @classmethod
    def validate_new_profile(cls, v: Any) -> Any:
        """
        Validate new_profile field.
        
        Datasource: ['webfilter.profile.name']
        
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
    async def validate_user_group_references(self, client: Any) -> list[str]:
        """
        Validate user_group references exist in FortiGate.
        
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
            >>> policy = OverrideModel(
            ...     user_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_user_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.override.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "user_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"User-Group '{value}' not found in "
                "user/group"
            )        
        return errors    
    async def validate_old_profile_references(self, client: Any) -> list[str]:
        """
        Validate old_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - webfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = OverrideModel(
            ...     old_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_old_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.override.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "old_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.webfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Old-Profile '{value}' not found in "
                "webfilter/profile"
            )        
        return errors    
    async def validate_new_profile_references(self, client: Any) -> list[str]:
        """
        Validate new_profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - webfilter/profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = OverrideModel(
            ...     new_profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_new_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.webfilter.override.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "new_profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.webfilter.profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"New-Profile '{value}' not found in "
                "webfilter/profile"
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
        
        errors = await self.validate_user_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_old_profile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_new_profile_references(client)
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
    "OverrideModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.611288Z
# ============================================================================
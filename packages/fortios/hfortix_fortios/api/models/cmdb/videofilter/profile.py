"""
Pydantic Models for CMDB - videofilter/profile

Runtime validation models for videofilter/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileFilters(BaseModel):
    """
    Child table model for filters.
    
    YouTube filter entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    type: TypeEnum = Field(default="category", description="Filter type.")    
    keyword: int = Field(ge=0, le=4294967295, default=0, description="Video filter keyword ID.")  # datasource: ['videofilter.keyword.id']    
    category: str = Field(max_length=7, default="", description="FortiGuard category ID.")    
    channel: str = Field(max_length=255, default="", description="Channel ID.")    
    action: Literal["allow", "monitor", "block"] | None = Field(default="monitor", description="Video filter action.")    
    log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable logging.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for videofilter/profile configuration.
    
    Configure VideoFilter profile.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - filters: pattern=        - youtube: pattern=        - vimeo: pattern=        - dailymotion: pattern=        - replacemsg_group: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    filters: list[Filters] = Field(description="YouTube filter entries.")    
    youtube: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable YouTube video source.")    
    vimeo: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Vimeo video source.")    
    dailymotion: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Dailymotion video source.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group.")  # datasource: ['system.replacemsg-group.name']    
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
    async def validate_filters_references(self, client: Any) -> list[str]:
        """
        Validate filters references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - videofilter/keyword        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     filters=[{"keyword": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_filters_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.videofilter.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "filters", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("keyword")
            else:
                value = getattr(item, "keyword", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.videofilter.keyword.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Filters '{value}' not found in "
                    "videofilter/keyword"
                )        
        return errors    
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
            ...     result = await fgt.api.cmdb.videofilter.profile.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_filters_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_replacemsg_group_references(client)
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
    "ProfileModel",    "ProfileFilters",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.369083Z
# ============================================================================
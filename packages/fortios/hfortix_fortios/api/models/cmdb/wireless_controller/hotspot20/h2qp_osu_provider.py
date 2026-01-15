"""
Pydantic Models for CMDB - wireless_controller/hotspot20/h2qp_osu_provider

Runtime validation models for wireless_controller/hotspot20/h2qp_osu_provider configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class H2qpOsuProviderFriendlyName(BaseModel):
    """
    Child table model for friendly-name.
    
    OSU provider friendly name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    index: int | None = Field(ge=1, le=10, default=0, description="OSU provider friendly name index.")    
    lang: str = Field(max_length=3, default="eng", description="Language code.")    
    friendly_name: str = Field(max_length=252, default="", description="OSU provider friendly name.")
class H2qpOsuProviderServiceDescription(BaseModel):
    """
    Child table model for service-description.
    
    OSU service name.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    service_id: int | None = Field(ge=0, le=4294967295, default=0, description="OSU service ID.")    
    lang: str = Field(max_length=3, default="eng", description="Language code.")    
    service_description: str = Field(max_length=252, default="", description="Service description.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class H2qpOsuProviderModel(BaseModel):
    """
    Pydantic model for wireless_controller/hotspot20/h2qp_osu_provider configuration.
    
    Configure online sign up (OSU) provider list.
    
    Validation Rules:        - name: max_length=35 pattern=        - friendly_name: pattern=        - server_uri: max_length=255 pattern=        - osu_method: pattern=        - osu_nai: max_length=255 pattern=        - service_description: pattern=        - icon: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="OSU provider ID.")    
    friendly_name: list[FriendlyName] = Field(default=None, description="OSU provider friendly name.")    
    server_uri: str | None = Field(max_length=255, default="", description="Server URI.")    
    osu_method: list[OsuMethod] = Field(default="", description="OSU method list.")    
    osu_nai: str | None = Field(max_length=255, default="", description="OSU NAI.")    
    service_description: list[ServiceDescription] = Field(default=None, description="OSU service name.")    
    icon: str | None = Field(max_length=35, default="", description="OSU provider icon.")  # datasource: ['wireless-controller.hotspot20.icon.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('icon')
    @classmethod
    def validate_icon(cls, v: Any) -> Any:
        """
        Validate icon field.
        
        Datasource: ['wireless-controller.hotspot20.icon.name']
        
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
    async def validate_icon_references(self, client: Any) -> list[str]:
        """
        Validate icon references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/hotspot20/icon        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = H2qpOsuProviderModel(
            ...     icon="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_icon_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.hotspot20.h2qp_osu_provider.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "icon", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.hotspot20.icon.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Icon '{value}' not found in "
                "wireless-controller/hotspot20/icon"
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
        
        errors = await self.validate_icon_references(client)
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
    "H2qpOsuProviderModel",    "H2qpOsuProviderFriendlyName",    "H2qpOsuProviderServiceDescription",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.955337Z
# ============================================================================
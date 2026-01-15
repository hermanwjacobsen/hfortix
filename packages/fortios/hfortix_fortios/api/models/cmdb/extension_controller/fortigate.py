"""
Pydantic Models for CMDB - extension_controller/fortigate

Runtime validation models for extension_controller/fortigate configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class FortigateModel(BaseModel):
    """
    Pydantic model for extension_controller/fortigate configuration.
    
    FortiGate controller configuration.
    
    Validation Rules:        - name: max_length=19 pattern=        - id: max_length=19 pattern=        - authorized: pattern=        - hostname: max_length=31 pattern=        - description: max_length=255 pattern=        - vdom: min=0 max=4294967295 pattern=        - device_id: min=0 max=4294967295 pattern=        - profile: max_length=31 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=19, default="", description="FortiGate entry name.")    
    id: str = Field(max_length=19, default="", description="FortiGate serial number.")    
    authorized: Literal["discovered", "disable", "enable"] = Field(default="discovered", description="Enable/disable FortiGate administration.")    
    hostname: str | None = Field(max_length=31, default="", description="FortiGate hostname.")    
    description: str | None = Field(max_length=255, default="", description="Description.")    
    vdom: int | None = Field(ge=0, le=4294967295, default=0, description="VDOM.")    
    device_id: int | None = Field(ge=0, le=4294967295, default=1026, description="Device ID.")    
    profile: str | None = Field(max_length=31, default="", description="FortiGate profile configuration.")  # datasource: ['extension-controller.fortigate-profile.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('profile')
    @classmethod
    def validate_profile(cls, v: Any) -> Any:
        """
        Validate profile field.
        
        Datasource: ['extension-controller.fortigate-profile.name']
        
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
    async def validate_profile_references(self, client: Any) -> list[str]:
        """
        Validate profile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - extension-controller/fortigate-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FortigateModel(
            ...     profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.extension_controller.fortigate.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.extension-controller.fortigate-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Profile '{value}' not found in "
                "extension-controller/fortigate-profile"
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
        
        errors = await self.validate_profile_references(client)
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
    "FortigateModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.281518Z
# ============================================================================
"""
Pydantic Models for CMDB - dlp/settings

Runtime validation models for dlp/settings configuration.
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

class SettingsModel(BaseModel):
    """
    Pydantic model for dlp/settings configuration.
    
    Configure settings for DLP.
    
    Validation Rules:        - storage_device: max_length=35 pattern=        - size: min=16 max=4294967295 pattern=        - db_mode: pattern=        - cache_mem_percent: min=1 max=15 pattern=        - chunk_size: min=100 max=100000 pattern=        - config_builder_timeout: min=10 max=100000 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    storage_device: str | None = Field(max_length=35, default="", description="Storage device name.")  # datasource: ['system.storage.name']    
    size: int | None = Field(ge=16, le=4294967295, default=16, description="Maximum total size of files within the DLP fingerprint database (MB).")    
    db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = Field(default="stop-adding", description="Behavior when the maximum size is reached in the DLP fingerprint database.")    
    cache_mem_percent: int | None = Field(ge=1, le=15, default=2, description="Maximum percentage of available memory allocated to caching DLP fingerprints (1 - 15).")    
    chunk_size: int | None = Field(ge=100, le=100000, default=2800, description="Maximum fingerprint chunk size. Caution, changing this setting will flush the entire database.")    
    config_builder_timeout: int | None = Field(ge=10, le=100000, default=60, description="Maximum time allowed for building a single DLP profile (default 60 seconds).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('storage_device')
    @classmethod
    def validate_storage_device(cls, v: Any) -> Any:
        """
        Validate storage_device field.
        
        Datasource: ['system.storage.name']
        
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
    async def validate_storage_device_references(self, client: Any) -> list[str]:
        """
        Validate storage_device references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/storage        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingsModel(
            ...     storage_device="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_storage_device_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dlp.settings.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "storage_device", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.storage.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Storage-Device '{value}' not found in "
                "system/storage"
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
        
        errors = await self.validate_storage_device_references(client)
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
    "SettingsModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.969558Z
# ============================================================================
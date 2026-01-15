"""
Pydantic Models for CMDB - dlp/data_type

Runtime validation models for dlp/data_type configuration.
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

class DataTypeModel(BaseModel):
    """
    Pydantic model for dlp/data_type configuration.
    
    Configure predefined data type used by DLP blocking.
    
    Validation Rules:        - name: max_length=35 pattern=        - pattern: max_length=255 pattern=        - verify: max_length=255 pattern=        - verify2: max_length=255 pattern=        - match_around: max_length=35 pattern=        - look_back: min=1 max=255 pattern=        - look_ahead: min=1 max=255 pattern=        - match_back: min=1 max=4096 pattern=        - match_ahead: min=1 max=4096 pattern=        - transform: max_length=255 pattern=        - verify_transformed_pattern: pattern=        - comment: max_length=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name of table containing the data type.")    
    pattern: str | None = Field(max_length=255, default="", description="Regular expression pattern string without look around.")    
    verify: str | None = Field(max_length=255, default="", description="Regular expression pattern string used to verify the data type.")    
    verify2: str | None = Field(max_length=255, default="", description="Extra regular expression pattern string used to verify the data type.")    
    match_around: str | None = Field(max_length=35, default="", description="Dictionary to check whether it has a match around (Only support match-any and basic types, no repeat supported).")  # datasource: ['dlp.dictionary.name']    
    look_back: int = Field(ge=1, le=255, default=1, description="Number of characters required to save for verification (1 - 255, default = 1).")    
    look_ahead: int = Field(ge=1, le=255, default=1, description="Number of characters to obtain in advance for verification (1 - 255, default = 1).")    
    match_back: int = Field(ge=1, le=4096, default=1, description="Number of characters in front for match-around (1 - 4096, default = 1).")    
    match_ahead: int = Field(ge=1, le=4096, default=1, description="Number of characters behind for match-around (1 - 4096, default = 1).")    
    transform: str | None = Field(max_length=255, default="", description="Template to transform user input to a pattern using capture group from 'pattern'.")    
    verify_transformed_pattern: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable verification for transformed pattern.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('match_around')
    @classmethod
    def validate_match_around(cls, v: Any) -> Any:
        """
        Validate match_around field.
        
        Datasource: ['dlp.dictionary.name']
        
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
    async def validate_match_around_references(self, client: Any) -> list[str]:
        """
        Validate match_around references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dlp/dictionary        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DataTypeModel(
            ...     match_around="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_match_around_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dlp.data_type.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "match_around", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dlp.dictionary.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Match-Around '{value}' not found in "
                "dlp/dictionary"
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
        
        errors = await self.validate_match_around_references(client)
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
    "DataTypeModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.933543Z
# ============================================================================
"""
Pydantic Models for CMDB - dlp/sensor

Runtime validation models for dlp/sensor configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class SensorEntries(BaseModel):
    """
    Child table model for entries.
    
    DLP sensor entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=1, le=32, default=0, description="ID.")    
    dictionary: str = Field(max_length=35, default="", description="Select a DLP dictionary or exact-data-match.")  # datasource: ['dlp.dictionary.name', 'dlp.exact-data-match.name']    
    count: int = Field(ge=1, le=255, default=1, description="Count of dictionary matches to trigger sensor entry match (Dictionary might not be able to trigger more than once based on its 'repeat' option, 1 - 255, default = 1).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this entry.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SensorModel(BaseModel):
    """
    Pydantic model for dlp/sensor configuration.
    
    Configure sensors used by DLP blocking.
    
    Validation Rules:        - name: max_length=35 pattern=        - match_type: pattern=        - eval: max_length=255 pattern=        - comment: max_length=255 pattern=        - entries: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name of table containing the sensor.")    
    match_type: Literal["match-all", "match-any", "match-eval"] = Field(default="match-any", description="Logical relation between entries (default = match-any).")    
    eval: str | None = Field(max_length=255, default="", description="Expression to evaluate.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    entries: list[Entries] = Field(description="DLP sensor entries.")    
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
    async def validate_entries_references(self, client: Any) -> list[str]:
        """
        Validate entries references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dlp/dictionary        - dlp/exact-data-match        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SensorModel(
            ...     entries=[{"dictionary": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_entries_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dlp.sensor.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "entries", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("dictionary")
            else:
                value = getattr(item, "dictionary", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.dlp.dictionary.exists(value):
                found = True
            elif await client.api.cmdb.dlp.exact-data-match.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Entries '{value}' not found in "
                    "dlp/dictionary or dlp/exact-data-match"
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
        
        errors = await self.validate_entries_references(client)
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
    "SensorModel",    "SensorEntries",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.991588Z
# ============================================================================
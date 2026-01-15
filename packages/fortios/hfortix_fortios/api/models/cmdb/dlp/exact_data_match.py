"""
Pydantic Models for CMDB - dlp/exact_data_match

Runtime validation models for dlp/exact_data_match configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any

# ============================================================================
# Child Table Models
# ============================================================================

class ExactDataMatchColumns(BaseModel):
    """
    Child table model for columns.
    
    DLP exact-data-match column types.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    index: int | None = Field(ge=1, le=32, default=0, description="Column index.")    
    type: str = Field(max_length=35, default="", description="Data-type for this column.")  # datasource: ['dlp.data-type.name']    
    optional: Literal["enable", "disable"] = Field(default="disable", description="Enable/disable optional match.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ExactDataMatchModel(BaseModel):
    """
    Pydantic model for dlp/exact_data_match configuration.
    
    Configure exact-data-match template used by DLP scan.
    
    Validation Rules:        - name: max_length=35 pattern=        - optional: min=0 max=32 pattern=        - data: max_length=35 pattern=        - columns: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name of table containing the exact-data-match template.")    
    optional: int = Field(ge=0, le=32, default=0, description="Number of optional columns need to match.")    
    data: str = Field(max_length=35, default="", description="External resource for exact data match.")  # datasource: ['system.external-resource.name']    
    columns: list[Columns] = Field(description="DLP exact-data-match column types.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('data')
    @classmethod
    def validate_data(cls, v: Any) -> Any:
        """
        Validate data field.
        
        Datasource: ['system.external-resource.name']
        
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
    async def validate_data_references(self, client: Any) -> list[str]:
        """
        Validate data references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ExactDataMatchModel(
            ...     data="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_data_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dlp.exact_data_match.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "data", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.external-resource.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Data '{value}' not found in "
                "system/external-resource"
            )        
        return errors    
    async def validate_columns_references(self, client: Any) -> list[str]:
        """
        Validate columns references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dlp/data-type        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ExactDataMatchModel(
            ...     columns=[{"type": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_columns_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.dlp.exact_data_match.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "columns", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("type")
            else:
                value = getattr(item, "type", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.dlp.data-type.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Columns '{value}' not found in "
                    "dlp/data-type"
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
        
        errors = await self.validate_data_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_columns_references(client)
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
    "ExactDataMatchModel",    "ExactDataMatchColumns",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.884878Z
# ============================================================================
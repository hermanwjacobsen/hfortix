"""
Pydantic Models for CMDB - firewall/shaping_profile

Runtime validation models for firewall/shaping_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ShapingProfileShapingEntries(BaseModel):
    """
    Child table model for shaping-entries.
    
    Define shaping entries of this shaping profile.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID number.")    
    class_id: int = Field(ge=0, le=4294967295, default=0, description="Class ID.")  # datasource: ['firewall.traffic-class.class-id']    
    priority: PriorityEnum | None = Field(default="high", description="Priority.")    
    guaranteed_bandwidth_percentage: int | None = Field(ge=0, le=100, default=0, description="Guaranteed bandwidth in percentage.")    
    maximum_bandwidth_percentage: int | None = Field(ge=1, le=100, default=1, description="Maximum bandwidth in percentage.")    
    limit: int | None = Field(ge=5, le=10000, default=100, description="Hard limit on the real queue size in packets.")    
    burst_in_msec: int | None = Field(ge=0, le=2000, default=0, description="Number of bytes that can be burst at maximum-bandwidth speed. Formula: burst = maximum-bandwidth*burst-in-msec.")    
    cburst_in_msec: int | None = Field(ge=0, le=2000, default=0, description="Number of bytes that can be burst as fast as the interface can transmit. Formula: cburst = maximum-bandwidth*cburst-in-msec.")    
    red_probability: int | None = Field(ge=0, le=20, default=0, description="Maximum probability (in percentage) for RED marking.")    
    min: int | None = Field(ge=3, le=3000, default=83, description="Average queue size in packets at which RED drop becomes a possibility.")    
    max: int | None = Field(ge=3, le=3000, default=250, description="Average queue size in packets at which RED drop probability is maximal.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ShapingProfileModel(BaseModel):
    """
    Pydantic model for firewall/shaping_profile configuration.
    
    Configure shaping profiles.
    
    Validation Rules:        - profile_name: max_length=35 pattern=        - comment: max_length=1023 pattern=        - type: pattern=        - npu_offloading: pattern=        - default_class_id: min=0 max=4294967295 pattern=        - shaping_entries: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    profile_name: str = Field(max_length=35, default="", description="Shaping profile name.")    
    comment: str | None = Field(max_length=1023, default=None, description="Comment.")    
    type: Literal["policing", "queuing"] | None = Field(default="policing", description="Select shaping profile type: policing / queuing.")    
    npu_offloading: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable NPU offloading.")    
    default_class_id: int = Field(ge=0, le=4294967295, default=0, description="Default class ID to handle unclassified packets (including all local traffic).")  # datasource: ['firewall.traffic-class.class-id']    
    shaping_entries: list[ShapingEntries] = Field(default=None, description="Define shaping entries of this shaping profile.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('default_class_id')
    @classmethod
    def validate_default_class_id(cls, v: Any) -> Any:
        """
        Validate default_class_id field.
        
        Datasource: ['firewall.traffic-class.class-id']
        
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
    async def validate_default_class_id_references(self, client: Any) -> list[str]:
        """
        Validate default_class_id references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/traffic-class        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ShapingProfileModel(
            ...     default_class_id="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_default_class_id_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "default_class_id", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.traffic-class.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Default-Class-Id '{value}' not found in "
                "firewall/traffic-class"
            )        
        return errors    
    async def validate_shaping_entries_references(self, client: Any) -> list[str]:
        """
        Validate shaping_entries references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/traffic-class        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ShapingProfileModel(
            ...     shaping_entries=[{"class-id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_shaping_entries_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaping_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "shaping_entries", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("class-id")
            else:
                value = getattr(item, "class-id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.traffic-class.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Shaping-Entries '{value}' not found in "
                    "firewall/traffic-class"
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
        
        errors = await self.validate_default_class_id_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_shaping_entries_references(client)
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
    "ShapingProfileModel",    "ShapingProfileShapingEntries",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.101548Z
# ============================================================================
"""
Pydantic Models for CMDB - firewall/internet_service_addition

Runtime validation models for firewall/internet_service_addition configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class InternetServiceAdditionEntry(BaseModel):
    """
    Child table model for entry.
    
    Entries added to the Internet Service addition database.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=255, default=0, description="Entry ID(1-255).")    
    addr_mode: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address mode (IPv4 or IPv6).")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Integer value for the protocol type as defined by IANA (0 - 255).")    
    port_range: list[PortRange] = Field(default=None, description="Port ranges in the custom entry.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class InternetServiceAdditionModel(BaseModel):
    """
    Pydantic model for firewall/internet_service_addition configuration.
    
    Configure Internet Services Addition.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - comment: max_length=255 pattern=        - entry: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Internet Service ID in the Internet Service database.")  # datasource: ['firewall.internet-service.id']    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    entry: list[Entry] = Field(default=None, description="Entries added to the Internet Service addition database.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('id')
    @classmethod
    def validate_id(cls, v: Any) -> Any:
        """
        Validate id field.
        
        Datasource: ['firewall.internet-service.id']
        
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
    async def validate_id_references(self, client: Any) -> list[str]:
        """
        Validate id references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/internet-service        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = InternetServiceAdditionModel(
            ...     id="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_id_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.internet_service_addition.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "id", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.internet-service.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Id '{value}' not found in "
                "firewall/internet-service"
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
        
        errors = await self.validate_id_references(client)
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
    "InternetServiceAdditionModel",    "InternetServiceAdditionEntry",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.601613Z
# ============================================================================
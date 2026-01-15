"""
Pydantic Models for CMDB - firewall/multicast_address

Runtime validation models for firewall/multicast_address configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class MulticastAddressTagging(BaseModel):
    """
    Child table model for tagging.
    
    Config object tagging.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Tagging entry name.")    
    category: str | None = Field(max_length=63, default="", description="Tag category.")  # datasource: ['system.object-tagging.category']    
    tags: list[Tags] = Field(default=None, description="Tags.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class MulticastAddressModel(BaseModel):
    """
    Pydantic model for firewall/multicast_address configuration.
    
    Configure multicast addresses.
    
    Validation Rules:        - name: max_length=79 pattern=        - type: pattern=        - subnet: pattern=        - start_ip: pattern=        - end_ip: pattern=        - comment: max_length=255 pattern=        - associated_interface: max_length=35 pattern=        - color: min=0 max=32 pattern=        - tagging: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Multicast address name.")    
    type: Literal["multicastrange", "broadcastmask"] | None = Field(default="multicastrange", description="Type of address object: multicast IP address range or broadcast IP/mask to be treated as a multicast address.")    
    subnet: Any = Field(default="0.0.0.0 0.0.0.0", description="Broadcast address and subnet.")    
    start_ip: str = Field(default="0.0.0.0", description="First IPv4 address (inclusive) in the range for the address.")    
    end_ip: str = Field(default="0.0.0.0", description="Final IPv4 address (inclusive) in the range for the address.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    associated_interface: str | None = Field(max_length=35, default="", description="Interface associated with the address object. When setting up a policy, only addresses associated with this interface are available.")  # datasource: ['system.interface.name']    
    color: int | None = Field(ge=0, le=32, default=0, description="Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1).")    
    tagging: list[Tagging] = Field(default=None, description="Config object tagging.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('associated_interface')
    @classmethod
    def validate_associated_interface(cls, v: Any) -> Any:
        """
        Validate associated_interface field.
        
        Datasource: ['system.interface.name']
        
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
    async def validate_associated_interface_references(self, client: Any) -> list[str]:
        """
        Validate associated_interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastAddressModel(
            ...     associated_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_associated_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_address.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "associated_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Associated-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_tagging_references(self, client: Any) -> list[str]:
        """
        Validate tagging references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/object-tagging        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastAddressModel(
            ...     tagging=[{"category": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tagging_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.multicast_address.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "tagging", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("category")
            else:
                value = getattr(item, "category", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.object-tagging.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Tagging '{value}' not found in "
                    "system/object-tagging"
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
        
        errors = await self.validate_associated_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_tagging_references(client)
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
    "MulticastAddressModel",    "MulticastAddressTagging",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.336801Z
# ============================================================================
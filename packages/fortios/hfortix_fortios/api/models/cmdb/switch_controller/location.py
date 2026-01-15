"""
Pydantic Models for CMDB - switch_controller/location

Runtime validation models for switch_controller/location configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class LocationAddressCivic(BaseModel):
    """
    Child table model for address-civic.
    
    Configure location civic address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    additional: str | None = Field(max_length=47, default="", description="Location additional details.")    
    additional_code: str | None = Field(max_length=47, default="", description="Location additional code details.")    
    block: str | None = Field(max_length=47, default="", description="Location block details.")    
    branch_road: str | None = Field(max_length=47, default="", description="Location branch road details.")    
    building: str | None = Field(max_length=47, default="", description="Location building details.")    
    city: str | None = Field(max_length=47, default="", description="Location city details.")    
    city_division: str | None = Field(max_length=47, default="", description="Location city division details.")    
    country: str = Field(max_length=47, default="", description="The two-letter ISO 3166 country code in capital ASCII letters eg. US, CA, DK, DE.")    
    country_subdivision: str | None = Field(max_length=47, default="", description="National subdivisions (state, canton, region, province, or prefecture).")    
    county: str | None = Field(max_length=47, default="", description="County, parish, gun (JP), or district (IN).")    
    direction: str | None = Field(max_length=47, default="", description="Leading street direction.")    
    floor: str | None = Field(max_length=47, default="", description="Floor.")    
    landmark: str | None = Field(max_length=47, default="", description="Landmark or vanity address.")    
    language: str | None = Field(max_length=47, default="", description="Language.")    
    name: str | None = Field(max_length=47, default="", description="Name (residence and office occupant).")    
    number: str | None = Field(max_length=47, default="", description="House number.")    
    number_suffix: str | None = Field(max_length=47, default="", description="House number suffix.")    
    place_type: str | None = Field(max_length=47, default="", description="Place type.")    
    post_office_box: str | None = Field(max_length=47, default="", description="Post office box.")    
    postal_community: str | None = Field(max_length=47, default="", description="Postal community name.")    
    primary_road: str | None = Field(max_length=47, default="", description="Primary road name.")    
    road_section: str | None = Field(max_length=47, default="", description="Road section.")    
    room: str | None = Field(max_length=47, default="", description="Room number.")    
    script: str | None = Field(max_length=47, default="", description="Script used to present the address information.")    
    seat: str | None = Field(max_length=47, default="", description="Seat number.")    
    street: str | None = Field(max_length=47, default="", description="Street.")    
    street_name_post_mod: str | None = Field(max_length=47, default="", description="Street name post modifier.")    
    street_name_pre_mod: str | None = Field(max_length=47, default="", description="Street name pre modifier.")    
    street_suffix: str | None = Field(max_length=47, default="", description="Street suffix.")    
    sub_branch_road: str | None = Field(max_length=47, default="", description="Sub branch road name.")    
    trailing_str_suffix: str | None = Field(max_length=47, default="", description="Trailing street suffix.")    
    unit: str | None = Field(max_length=47, default="", description="Unit (apartment, suite).")    
    zip: str | None = Field(max_length=47, default="", description="Postal/zip code.")    
    parent_key: str | None = Field(max_length=63, default="", description="Parent key name.")
class LocationCoordinates(BaseModel):
    """
    Child table model for coordinates.
    
    Configure location GPS coordinates.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    altitude: str = Field(max_length=15, default="", description="Plus or minus floating point number. For example, 117.47.")    
    altitude_unit: Literal["m", "f"] = Field(default="m", description="Configure the unit for which the altitude is to (m = meters, f = floors of a building).")    
    datum: Literal["WGS84", "NAD83", "NAD83/MLLW"] = Field(default="WGS84", description="WGS84, NAD83, NAD83/MLLW.")    
    latitude: str = Field(max_length=15, default="", description="Floating point starting with +/- or ending with (N or S). For example, +/-16.67 or 16.67N.")    
    longitude: str = Field(max_length=15, default="", description="Floating point starting with +/- or ending with (N or S). For example, +/-26.789 or 26.789E.")    
    parent_key: str | None = Field(max_length=63, default="", description="Parent key name.")
class LocationElinNumber(BaseModel):
    """
    Child table model for elin-number.
    
    Configure location ELIN number.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    elin_num: str | None = Field(max_length=31, default="", description="Configure ELIN callback number.")    
    parent_key: str | None = Field(max_length=63, default="", description="Parent key name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class LocationModel(BaseModel):
    """
    Pydantic model for switch_controller/location configuration.
    
    Configure FortiSwitch location services.
    
    Validation Rules:        - name: max_length=63 pattern=        - address_civic: pattern=        - coordinates: pattern=        - elin_number: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Unique location item name.")    
    address_civic: list[AddressCivic] = Field(default=None, description="Configure location civic address.")    
    coordinates: list[Coordinates] = Field(default=None, description="Configure location GPS coordinates.")    
    elin_number: list[ElinNumber] = Field(default=None, description="Configure location ELIN number.")    
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

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "LocationModel",    "LocationAddressCivic",    "LocationCoordinates",    "LocationElinNumber",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.337825Z
# ============================================================================
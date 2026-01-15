"""
Pydantic Models for CMDB - wireless_controller/wtp_group

Runtime validation models for wireless_controller/wtp_group configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class WtpGroupWtps(BaseModel):
    """
    Child table model for wtps.
    
    WTP list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    wtp_id: str = Field(max_length=35, default="", description="WTP ID.")  # datasource: ['wireless-controller.wtp.wtp-id']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class WtpGroupPlatform_typeEnum(str, Enum):
    """Allowed values for platform_type field."""
    AP_11N = "AP-11N"    C24JE = "C24JE"    421E = "421E"    423E = "423E"    221E = "221E"    222E = "222E"    223E = "223E"    224E = "224E"    231E = "231E"    321E = "321E"    431F = "431F"    431FL = "431FL"    432F = "432F"    432FR = "432FR"    433F = "433F"    433FL = "433FL"    231F = "231F"    231FL = "231FL"    234F = "234F"    23JF = "23JF"    831F = "831F"    231G = "231G"    233G = "233G"    234G = "234G"    431G = "431G"    432G = "432G"    433G = "433G"    231K = "231K"    231KD = "231KD"    23JK = "23JK"    222KL = "222KL"    241K = "241K"    243K = "243K"    244K = "244K"    441K = "441K"    432K = "432K"    443K = "443K"    U421E = "U421E"    U422EV = "U422EV"    U423E = "U423E"    U221EV = "U221EV"    U223EV = "U223EV"    U24JEV = "U24JEV"    U321EV = "U321EV"    U323EV = "U323EV"    U431F = "U431F"    U433F = "U433F"    U231F = "U231F"    U234F = "U234F"    U432F = "U432F"    U231G = "U231G"    MVP = "MVP"

# ============================================================================
# Main Model
# ============================================================================

class WtpGroupModel(BaseModel):
    """
    Pydantic model for wireless_controller/wtp_group configuration.
    
    Configure WTP groups.
    
    Validation Rules:        - name: max_length=35 pattern=        - platform_type: pattern=        - ble_major_id: min=0 max=65535 pattern=        - wtps: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="WTP group name.")    
    platform_type: PlatformTypeEnum | None = Field(default="", description="FortiAP models to define the WTP group platform type.")    
    ble_major_id: int | None = Field(ge=0, le=65535, default=0, description="Override BLE Major ID.")    
    wtps: list[Wtps] = Field(default=None, description="WTP list.")    
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
    async def validate_wtps_references(self, client: Any) -> list[str]:
        """
        Validate wtps references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/wtp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = WtpGroupModel(
            ...     wtps=[{"wtp-id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wtps_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.wireless_controller.wtp_group.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "wtps", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("wtp-id")
            else:
                value = getattr(item, "wtp-id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.wireless-controller.wtp.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Wtps '{value}' not found in "
                    "wireless-controller/wtp"
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
        
        errors = await self.validate_wtps_references(client)
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
    "WtpGroupModel",    "WtpGroupWtps",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.261369Z
# ============================================================================
"""
Pydantic Models for CMDB - extension_controller/extender

Runtime validation models for extension_controller/extender configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ExtenderWanExtension(BaseModel):
    """
    Child table model for wan-extension.
    
    FortiExtender wan extension configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    modem1_extension: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_extension: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn1_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn2_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn3_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem1_pdn4_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn1_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn2_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn3_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']    
    modem2_pdn4_interface: str | None = Field(max_length=31, default="", description="FortiExtender interface name.")  # datasource: ['system.interface.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExtenderAllowaccessEnum(str, Enum):
    """Allowed values for allowaccess field."""
    PING = "ping"    TELNET = "telnet"    HTTP = "http"    HTTPS = "https"    SSH = "ssh"    SNMP = "snmp"

# ============================================================================
# Main Model
# ============================================================================

class ExtenderModel(BaseModel):
    """
    Pydantic model for extension_controller/extender configuration.
    
    Extender controller configuration.
    
    Validation Rules:        - name: max_length=19 pattern=        - id: max_length=19 pattern=        - authorized: pattern=        - ext_name: max_length=31 pattern=        - description: max_length=255 pattern=        - vdom: min=0 max=4294967295 pattern=        - device_id: min=0 max=4294967295 pattern=        - extension_type: pattern=        - profile: max_length=31 pattern=        - override_allowaccess: pattern=        - allowaccess: pattern=        - override_login_password_change: pattern=        - login_password_change: pattern=        - login_password: max_length=27 pattern=        - override_enforce_bandwidth: pattern=        - enforce_bandwidth: pattern=        - bandwidth_limit: min=1 max=16776000 pattern=        - wan_extension: pattern=        - firmware_provision_latest: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=19, default="", description="FortiExtender entry name.")    
    id: str = Field(max_length=19, default="", description="FortiExtender serial number.")    
    authorized: Literal["discovered", "disable", "enable"] = Field(default="discovered", description="FortiExtender Administration (enable or disable).")    
    ext_name: str | None = Field(max_length=31, default="", description="FortiExtender name.")    
    description: str | None = Field(max_length=255, default="", description="Description.")    
    vdom: int | None = Field(ge=0, le=4294967295, default=1, description="VDOM.")    
    device_id: int | None = Field(ge=0, le=4294967295, default=1026, description="Device ID.")    
    extension_type: Literal["wan-extension", "lan-extension"] = Field(default="", description="Extension type for this FortiExtender.")    
    profile: str | None = Field(max_length=31, default="", description="FortiExtender profile configuration.")  # datasource: ['extension-controller.extender-profile.name']    
    override_allowaccess: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to override the extender profile management access configuration.")    
    allowaccess: list[Allowaccess] = Field(default="", description="Control management access to the managed extender. Separate entries with a space.")    
    override_login_password_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to override the extender profile login-password (administrator password) setting.")    
    login_password_change: Literal["yes", "default", "no"] | None = Field(default="no", description="Change or reset the administrator password of a managed extender (yes, default, or no, default = no).")    
    login_password: Any = Field(max_length=27, description="Set the managed extender's administrator password.")    
    override_enforce_bandwidth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to override the extender profile enforce-bandwidth setting.")    
    enforce_bandwidth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable enforcement of bandwidth on LAN extension interface.")    
    bandwidth_limit: int = Field(ge=1, le=16776000, default=1024, description="FortiExtender LAN extension bandwidth limit (Mbps).")    
    wan_extension: list[WanExtension] = Field(default=None, description="FortiExtender wan extension configuration.")    
    firmware_provision_latest: Literal["disable", "once"] | None = Field(default="disable", description="Enable/disable one-time automatic provisioning of the latest firmware version.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('profile')
    @classmethod
    def validate_profile(cls, v: Any) -> Any:
        """
        Validate profile field.
        
        Datasource: ['extension-controller.extender-profile.name']
        
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
        - extension-controller/extender-profile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ExtenderModel(
            ...     profile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_profile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.extension_controller.extender.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "profile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.extension-controller.extender-profile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Profile '{value}' not found in "
                "extension-controller/extender-profile"
            )        
        return errors    
    async def validate_wan_extension_references(self, client: Any) -> list[str]:
        """
        Validate wan_extension references exist in FortiGate.
        
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
            >>> policy = ExtenderModel(
            ...     wan_extension=[{"modem2-pdn4-interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_wan_extension_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.extension_controller.extender.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "wan_extension", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("modem2-pdn4-interface")
            else:
                value = getattr(item, "modem2-pdn4-interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Wan-Extension '{value}' not found in "
                    "system/interface"
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
        errors = await self.validate_wan_extension_references(client)
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
    "ExtenderModel",    "ExtenderWanExtension",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.745546Z
# ============================================================================
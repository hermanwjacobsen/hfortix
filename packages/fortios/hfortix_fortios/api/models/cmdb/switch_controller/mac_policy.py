"""
Pydantic Models for CMDB - switch_controller/mac_policy

Runtime validation models for switch_controller/mac_policy configuration.
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

class MacPolicyModel(BaseModel):
    """
    Pydantic model for switch_controller/mac_policy configuration.
    
    Configure MAC policy to be applied on the managed FortiSwitch devices through NAC device.
    
    Validation Rules:        - name: max_length=63 pattern=        - description: max_length=63 pattern=        - fortilink: max_length=15 pattern=        - vlan: max_length=15 pattern=        - traffic_policy: max_length=63 pattern=        - count: pattern=        - bounce_port_link: pattern=        - bounce_port_duration: min=1 max=30 pattern=        - poe_reset: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="MAC policy name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the MAC policy.")    
    fortilink: str = Field(max_length=15, default="", description="FortiLink interface for which this MAC policy belongs to.")  # datasource: ['system.interface.name']    
    vlan: str | None = Field(max_length=15, default="", description="Ingress traffic VLAN assignment for the MAC address matching this MAC policy.")  # datasource: ['system.interface.name']    
    traffic_policy: str | None = Field(max_length=63, default="", description="Traffic policy to be applied when using this MAC policy.")  # datasource: ['switch-controller.traffic-policy.name']    
    count: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable packet count on the NAC device.")    
    bounce_port_link: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable bouncing (administratively bring the link down, up) of a switch port where this mac-policy is applied.")    
    bounce_port_duration: int | None = Field(ge=1, le=30, default=5, description="Bounce duration in seconds of a switch port where this mac-policy is applied.")    
    poe_reset: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable POE reset of a switch port where this mac-policy is applied.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('fortilink')
    @classmethod
    def validate_fortilink(cls, v: Any) -> Any:
        """
        Validate fortilink field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('vlan')
    @classmethod
    def validate_vlan(cls, v: Any) -> Any:
        """
        Validate vlan field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('traffic_policy')
    @classmethod
    def validate_traffic_policy(cls, v: Any) -> Any:
        """
        Validate traffic_policy field.
        
        Datasource: ['switch-controller.traffic-policy.name']
        
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
    async def validate_fortilink_references(self, client: Any) -> list[str]:
        """
        Validate fortilink references exist in FortiGate.
        
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
            >>> policy = MacPolicyModel(
            ...     fortilink="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fortilink_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.mac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fortilink", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fortilink '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_vlan_references(self, client: Any) -> list[str]:
        """
        Validate vlan references exist in FortiGate.
        
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
            >>> policy = MacPolicyModel(
            ...     vlan="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vlan_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.mac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vlan", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Vlan '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_traffic_policy_references(self, client: Any) -> list[str]:
        """
        Validate traffic_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/traffic-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MacPolicyModel(
            ...     traffic_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.mac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "traffic_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.traffic-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Traffic-Policy '{value}' not found in "
                "switch-controller/traffic-policy"
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
        
        errors = await self.validate_fortilink_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vlan_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_traffic_policy_references(client)
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
    "MacPolicyModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.872917Z
# ============================================================================
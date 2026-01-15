"""
Pydantic Models for CMDB - switch_controller/dynamic_port_policy

Runtime validation models for switch_controller/dynamic_port_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class DynamicPortPolicyPolicy(BaseModel):
    """
    Child table model for policy.
    
    Port policies with matching criteria and actions.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=63, default="", description="Policy name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the policy.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable policy.")    
    category: Literal["device", "interface-tag"] | None = Field(default="device", description="Category of Dynamic port policy.")    
    match_type: Literal["dynamic", "override"] | None = Field(default="dynamic", description="Match and retain the devices based on the type.")    
    match_period: int | None = Field(ge=0, le=120, default=0, description="Number of days the matched devices will be retained (0 - 120, 0 = always retain).")    
    match_remove: Literal["default", "link-down"] | None = Field(default="default", description="Options to remove the matched override devices.")    
    interface_tags: list[InterfaceTags] = Field(default=None, description="Match policy based on the FortiSwitch interface object tags.")    
    mac: str | None = Field(max_length=17, default="", description="Match policy based on MAC address.")    
    hw_vendor: str | None = Field(max_length=15, default="", description="Match policy based on hardware vendor.")    
    type: str | None = Field(max_length=15, default="", description="Match policy based on type.")    
    family: str | None = Field(max_length=31, default="", description="Match policy based on family.")    
    host: str | None = Field(max_length=64, default="", description="Match policy based on host.")    
    lldp_profile: str | None = Field(max_length=63, default="", description="LLDP profile to be applied when using this policy.")  # datasource: ['switch-controller.lldp-profile.name']    
    qos_policy: str | None = Field(max_length=63, default="", description="QoS policy to be applied when using this policy.")  # datasource: ['switch-controller.qos.qos-policy.name']    
    802_1x: str | None = Field(max_length=31, default="", description="802.1x security policy to be applied when using this policy.")  # datasource: ['switch-controller.security-policy.802-1X.name', 'switch-controller.security-policy.captive-portal.name']    
    vlan_policy: str | None = Field(max_length=63, default="", description="VLAN policy to be applied when using this policy.")  # datasource: ['switch-controller.vlan-policy.name']    
    bounce_port_link: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable bouncing (administratively bring the link down, up) of a switch port where this policy is applied. Helps to clear and reassign VLAN from lldp-profile.")    
    bounce_port_duration: int | None = Field(ge=1, le=30, default=5, description="Bounce duration in seconds of a switch port where this policy is applied.")    
    poe_reset: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable POE reset of a switch port where this policy is applied.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class DynamicPortPolicyModel(BaseModel):
    """
    Pydantic model for switch_controller/dynamic_port_policy configuration.
    
    Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
    
    Validation Rules:        - name: max_length=63 pattern=        - description: max_length=63 pattern=        - fortilink: max_length=15 pattern=        - policy: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Dynamic port policy name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the Dynamic port policy.")    
    fortilink: str = Field(max_length=15, default="", description="FortiLink interface for which this Dynamic port policy belongs to.")  # datasource: ['system.interface.name']    
    policy: list[Policy] = Field(default=None, description="Port policies with matching criteria and actions.")    
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
            >>> policy = DynamicPortPolicyModel(
            ...     fortilink="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fortilink_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.dynamic_port_policy.post(policy.to_fortios_dict())
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
    async def validate_policy_references(self, client: Any) -> list[str]:
        """
        Validate policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/vlan-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DynamicPortPolicyModel(
            ...     policy=[{"vlan-policy": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.dynamic_port_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "policy", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("vlan-policy")
            else:
                value = getattr(item, "vlan-policy", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.switch-controller.vlan-policy.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Policy '{value}' not found in "
                    "switch-controller/vlan-policy"
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
        errors = await self.validate_policy_references(client)
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
    "DynamicPortPolicyModel",    "DynamicPortPolicyPolicy",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.898742Z
# ============================================================================
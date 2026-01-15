"""
Pydantic Models for CMDB - switch_controller/auto_config/policy

Runtime validation models for switch_controller/auto_config/policy configuration.
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

class PolicyModel(BaseModel):
    """
    Pydantic model for switch_controller/auto_config/policy configuration.
    
    Policy definitions which can define the behavior on auto configured interfaces.
    
    Validation Rules:        - name: max_length=63 pattern=        - qos_policy: max_length=63 pattern=        - storm_control_policy: max_length=63 pattern=        - poe_status: pattern=        - igmp_flood_report: pattern=        - igmp_flood_traffic: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=63, default="", description="Auto-config policy name.")    
    qos_policy: str | None = Field(max_length=63, default="default", description="Auto-Config QoS policy.")  # datasource: ['switch-controller.qos.qos-policy.name']    
    storm_control_policy: str | None = Field(max_length=63, default="auto-config", description="Auto-Config storm control policy.")  # datasource: ['switch-controller.storm-control-policy.name']    
    poe_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable PoE status.")    
    igmp_flood_report: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IGMP flood report.")    
    igmp_flood_traffic: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IGMP flood traffic.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('qos_policy')
    @classmethod
    def validate_qos_policy(cls, v: Any) -> Any:
        """
        Validate qos_policy field.
        
        Datasource: ['switch-controller.qos.qos-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('storm_control_policy')
    @classmethod
    def validate_storm_control_policy(cls, v: Any) -> Any:
        """
        Validate storm_control_policy field.
        
        Datasource: ['switch-controller.storm-control-policy.name']
        
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
    async def validate_qos_policy_references(self, client: Any) -> list[str]:
        """
        Validate qos_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/qos/qos-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     qos_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_qos_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.auto_config.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "qos_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.qos.qos-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Qos-Policy '{value}' not found in "
                "switch-controller/qos/qos-policy"
            )        
        return errors    
    async def validate_storm_control_policy_references(self, client: Any) -> list[str]:
        """
        Validate storm_control_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/storm-control-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = PolicyModel(
            ...     storm_control_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_storm_control_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.auto_config.policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "storm_control_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.storm-control-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Storm-Control-Policy '{value}' not found in "
                "switch-controller/storm-control-policy"
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
        
        errors = await self.validate_qos_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_storm_control_policy_references(client)
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
    "PolicyModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.606489Z
# ============================================================================
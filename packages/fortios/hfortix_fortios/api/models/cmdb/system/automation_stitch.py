"""
Pydantic Models for CMDB - system/automation_stitch

Runtime validation models for system/automation_stitch configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class AutomationStitchCondition(BaseModel):
    """
    Child table model for condition.
    
    Automation conditions.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Condition name.")  # datasource: ['system.automation-condition.name']
class AutomationStitchActions(BaseModel):
    """
    Child table model for actions.
    
    Configure stitch actions.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    action: str = Field(max_length=64, default="", description="Action name.")  # datasource: ['system.automation-action.name']    
    delay: int | None = Field(ge=0, le=3600, default=0, description="Delay before execution (in seconds).")    
    required: Literal["enable", "disable"] | None = Field(default="disable", description="Required in action chain.")
class AutomationStitchDestination(BaseModel):
    """
    Child table model for destination.
    
    Serial number/HA group-name of destination devices.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Destination name.")  # datasource: ['system.automation-destination.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class AutomationStitchModel(BaseModel):
    """
    Pydantic model for system/automation_stitch configuration.
    
    Automation stitches.
    
    Validation Rules:        - name: max_length=35 pattern=        - description: max_length=255 pattern=        - status: pattern=        - trigger: max_length=35 pattern=        - condition: pattern=        - condition_logic: pattern=        - actions: pattern=        - destination: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Name.")    
    description: str | None = Field(max_length=255, default=None, description="Description.")    
    status: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable this stitch.")    
    trigger: str = Field(max_length=35, default="", description="Trigger name.")  # datasource: ['system.automation-trigger.name']    
    condition: list[Condition] = Field(default=None, description="Automation conditions.")    
    condition_logic: Literal["and", "or"] = Field(default="and", description="Apply AND/OR logic to the specified automation conditions.")    
    actions: list[Actions] = Field(default=None, description="Configure stitch actions.")    
    destination: list[Destination] = Field(default=None, description="Serial number/HA group-name of destination devices.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('trigger')
    @classmethod
    def validate_trigger(cls, v: Any) -> Any:
        """
        Validate trigger field.
        
        Datasource: ['system.automation-trigger.name']
        
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
    async def validate_trigger_references(self, client: Any) -> list[str]:
        """
        Validate trigger references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/automation-trigger        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationStitchModel(
            ...     trigger="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_trigger_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_stitch.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "trigger", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.automation-trigger.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Trigger '{value}' not found in "
                "system/automation-trigger"
            )        
        return errors    
    async def validate_condition_references(self, client: Any) -> list[str]:
        """
        Validate condition references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/automation-condition        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationStitchModel(
            ...     condition=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_condition_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_stitch.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "condition", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.automation-condition.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Condition '{value}' not found in "
                    "system/automation-condition"
                )        
        return errors    
    async def validate_actions_references(self, client: Any) -> list[str]:
        """
        Validate actions references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/automation-action        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationStitchModel(
            ...     actions=[{"action": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_actions_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_stitch.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "actions", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("action")
            else:
                value = getattr(item, "action", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.automation-action.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Actions '{value}' not found in "
                    "system/automation-action"
                )        
        return errors    
    async def validate_destination_references(self, client: Any) -> list[str]:
        """
        Validate destination references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/automation-destination        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationStitchModel(
            ...     destination=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_destination_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_stitch.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "destination", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.automation-destination.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Destination '{value}' not found in "
                    "system/automation-destination"
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
        
        errors = await self.validate_trigger_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_condition_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_actions_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_destination_references(client)
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
    "AutomationStitchModel",    "AutomationStitchCondition",    "AutomationStitchActions",    "AutomationStitchDestination",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.321814Z
# ============================================================================
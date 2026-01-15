"""
Pydantic Models for CMDB - switch_controller/auto_config/default

Runtime validation models for switch_controller/auto_config/default configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class DefaultModel(BaseModel):
    """
    Pydantic model for switch_controller/auto_config/default configuration.
    
    Policies which are applied automatically to all ISL/ICL/FortiLink interfaces.
    
    Validation Rules:        - fgt_policy: max_length=63 pattern=        - isl_policy: max_length=63 pattern=        - icl_policy: max_length=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    fgt_policy: str | None = Field(max_length=63, default="default", description="Default FortiLink auto-config policy.")  # datasource: ['switch-controller.auto-config.policy.name']    
    isl_policy: str | None = Field(max_length=63, default="default", description="Default ISL auto-config policy.")  # datasource: ['switch-controller.auto-config.policy.name']    
    icl_policy: str | None = Field(max_length=63, default="default-icl", description="Default ICL auto-config policy.")  # datasource: ['switch-controller.auto-config.policy.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('fgt_policy')
    @classmethod
    def validate_fgt_policy(cls, v: Any) -> Any:
        """
        Validate fgt_policy field.
        
        Datasource: ['switch-controller.auto-config.policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('isl_policy')
    @classmethod
    def validate_isl_policy(cls, v: Any) -> Any:
        """
        Validate isl_policy field.
        
        Datasource: ['switch-controller.auto-config.policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('icl_policy')
    @classmethod
    def validate_icl_policy(cls, v: Any) -> Any:
        """
        Validate icl_policy field.
        
        Datasource: ['switch-controller.auto-config.policy.name']
        
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
    async def validate_fgt_policy_references(self, client: Any) -> list[str]:
        """
        Validate fgt_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/auto-config/policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DefaultModel(
            ...     fgt_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fgt_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.auto_config.default.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fgt_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.auto-config.policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fgt-Policy '{value}' not found in "
                "switch-controller/auto-config/policy"
            )        
        return errors    
    async def validate_isl_policy_references(self, client: Any) -> list[str]:
        """
        Validate isl_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/auto-config/policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DefaultModel(
            ...     isl_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_isl_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.auto_config.default.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "isl_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.auto-config.policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Isl-Policy '{value}' not found in "
                "switch-controller/auto-config/policy"
            )        
        return errors    
    async def validate_icl_policy_references(self, client: Any) -> list[str]:
        """
        Validate icl_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/auto-config/policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = DefaultModel(
            ...     icl_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_icl_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.auto_config.default.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "icl_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.auto-config.policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Icl-Policy '{value}' not found in "
                "switch-controller/auto-config/policy"
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
        
        errors = await self.validate_fgt_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_isl_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_icl_policy_references(client)
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
    "DefaultModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.316534Z
# ============================================================================
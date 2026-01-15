"""
Pydantic Models for CMDB - switch_controller/initial_config/vlans

Runtime validation models for switch_controller/initial_config/vlans configuration.
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

class VlansModel(BaseModel):
    """
    Pydantic model for switch_controller/initial_config/vlans configuration.
    
    Configure initial template for auto-generated VLAN interfaces.
    
    Validation Rules:        - optional_vlans: pattern=        - default_vlan: max_length=63 pattern=        - quarantine: max_length=63 pattern=        - rspan: max_length=63 pattern=        - voice: max_length=63 pattern=        - video: max_length=63 pattern=        - nac: max_length=63 pattern=        - nac_segment: max_length=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    optional_vlans: Literal["enable", "disable"] | None = Field(default="enable", description="Auto-generate pre-configured VLANs upon switch discovery.")    
    default_vlan: str | None = Field(max_length=63, default="_default", description="Default VLAN (native) assigned to all switch ports upon discovery.")  # datasource: ['switch-controller.initial-config.template.name']    
    quarantine: str | None = Field(max_length=63, default="quarantine", description="VLAN for quarantined traffic.")  # datasource: ['switch-controller.initial-config.template.name']    
    rspan: str | None = Field(max_length=63, default="rspan", description="VLAN for RSPAN/ERSPAN mirrored traffic.")  # datasource: ['switch-controller.initial-config.template.name']    
    voice: str | None = Field(max_length=63, default="voice", description="VLAN dedicated for voice devices.")  # datasource: ['switch-controller.initial-config.template.name']    
    video: str | None = Field(max_length=63, default="video", description="VLAN dedicated for video devices.")  # datasource: ['switch-controller.initial-config.template.name']    
    nac: str | None = Field(max_length=63, default="onboarding", description="VLAN for NAC onboarding devices.")  # datasource: ['switch-controller.initial-config.template.name']    
    nac_segment: str | None = Field(max_length=63, default="nac_segment", description="VLAN for NAC segment primary interface.")  # datasource: ['switch-controller.initial-config.template.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('default_vlan')
    @classmethod
    def validate_default_vlan(cls, v: Any) -> Any:
        """
        Validate default_vlan field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('quarantine')
    @classmethod
    def validate_quarantine(cls, v: Any) -> Any:
        """
        Validate quarantine field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('rspan')
    @classmethod
    def validate_rspan(cls, v: Any) -> Any:
        """
        Validate rspan field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('voice')
    @classmethod
    def validate_voice(cls, v: Any) -> Any:
        """
        Validate voice field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('video')
    @classmethod
    def validate_video(cls, v: Any) -> Any:
        """
        Validate video field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('nac')
    @classmethod
    def validate_nac(cls, v: Any) -> Any:
        """
        Validate nac field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('nac_segment')
    @classmethod
    def validate_nac_segment(cls, v: Any) -> Any:
        """
        Validate nac_segment field.
        
        Datasource: ['switch-controller.initial-config.template.name']
        
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
    async def validate_default_vlan_references(self, client: Any) -> list[str]:
        """
        Validate default_vlan references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/initial-config/template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VlansModel(
            ...     default_vlan="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_default_vlan_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.initial_config.vlans.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "default_vlan", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.initial-config.template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Default-Vlan '{value}' not found in "
                "switch-controller/initial-config/template"
            )        
        return errors    
    async def validate_quarantine_references(self, client: Any) -> list[str]:
        """
        Validate quarantine references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/initial-config/template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VlansModel(
            ...     quarantine="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_quarantine_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.initial_config.vlans.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "quarantine", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.initial-config.template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Quarantine '{value}' not found in "
                "switch-controller/initial-config/template"
            )        
        return errors    
    async def validate_rspan_references(self, client: Any) -> list[str]:
        """
        Validate rspan references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/initial-config/template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VlansModel(
            ...     rspan="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_rspan_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.initial_config.vlans.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "rspan", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.initial-config.template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Rspan '{value}' not found in "
                "switch-controller/initial-config/template"
            )        
        return errors    
    async def validate_voice_references(self, client: Any) -> list[str]:
        """
        Validate voice references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/initial-config/template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VlansModel(
            ...     voice="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_voice_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.initial_config.vlans.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "voice", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.initial-config.template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Voice '{value}' not found in "
                "switch-controller/initial-config/template"
            )        
        return errors    
    async def validate_video_references(self, client: Any) -> list[str]:
        """
        Validate video references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/initial-config/template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VlansModel(
            ...     video="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_video_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.initial_config.vlans.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "video", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.initial-config.template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Video '{value}' not found in "
                "switch-controller/initial-config/template"
            )        
        return errors    
    async def validate_nac_references(self, client: Any) -> list[str]:
        """
        Validate nac references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/initial-config/template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VlansModel(
            ...     nac="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_nac_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.initial_config.vlans.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "nac", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.initial-config.template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Nac '{value}' not found in "
                "switch-controller/initial-config/template"
            )        
        return errors    
    async def validate_nac_segment_references(self, client: Any) -> list[str]:
        """
        Validate nac_segment references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/initial-config/template        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = VlansModel(
            ...     nac_segment="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_nac_segment_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.initial_config.vlans.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "nac_segment", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.initial-config.template.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Nac-Segment '{value}' not found in "
                "switch-controller/initial-config/template"
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
        
        errors = await self.validate_default_vlan_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_quarantine_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_rspan_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_voice_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_video_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_nac_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_nac_segment_references(client)
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
    "VlansModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.946624Z
# ============================================================================
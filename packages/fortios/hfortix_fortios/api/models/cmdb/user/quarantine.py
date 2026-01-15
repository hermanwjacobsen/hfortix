"""
Pydantic Models for CMDB - user/quarantine

Runtime validation models for user/quarantine configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class QuarantineTargets(BaseModel):
    """
    Child table model for targets.
    
    Quarantine entry to hold multiple MACs.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    entry: str = Field(max_length=63, default="", description="Quarantine entry name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the quarantine entry.")    
    macs: list[Macs] = Field(default=None, description="Quarantine MACs.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class QuarantineModel(BaseModel):
    """
    Pydantic model for user/quarantine configuration.
    
    Configure quarantine support.
    
    Validation Rules:        - quarantine: pattern=        - traffic_policy: max_length=63 pattern=        - firewall_groups: max_length=79 pattern=        - targets: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    quarantine: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable quarantine.")    
    traffic_policy: str | None = Field(max_length=63, default="", description="Traffic policy for quarantined MACs.")  # datasource: ['switch-controller.traffic-policy.name']    
    firewall_groups: str | None = Field(max_length=79, default="", description="Firewall address group which includes all quarantine MAC address.")  # datasource: ['firewall.addrgrp.name']    
    targets: list[Targets] = Field(default=None, description="Quarantine entry to hold multiple MACs.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    @field_validator('firewall_groups')
    @classmethod
    def validate_firewall_groups(cls, v: Any) -> Any:
        """
        Validate firewall_groups field.
        
        Datasource: ['firewall.addrgrp.name']
        
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
            >>> policy = QuarantineModel(
            ...     traffic_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.quarantine.post(policy.to_fortios_dict())
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
    async def validate_firewall_groups_references(self, client: Any) -> list[str]:
        """
        Validate firewall_groups references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = QuarantineModel(
            ...     firewall_groups="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_firewall_groups_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.quarantine.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "firewall_groups", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Firewall-Groups '{value}' not found in "
                "firewall/addrgrp"
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
        
        errors = await self.validate_traffic_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_firewall_groups_references(client)
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
    "QuarantineModel",    "QuarantineTargets",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.031338Z
# ============================================================================
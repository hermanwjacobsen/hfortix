"""
Pydantic Models for CMDB - system/cloud_service

Runtime validation models for system/cloud_service configuration.
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

class CloudServiceModel(BaseModel):
    """
    Pydantic model for system/cloud_service configuration.
    
    Configure system cloud service.
    
    Validation Rules:        - name: max_length=35 pattern=        - vendor: pattern=        - traffic_vdom: max_length=31 pattern=        - gck_service_account: max_length=285 pattern=        - gck_private_key: max_length=8191 pattern=        - gck_keyid: max_length=127 pattern=        - gck_access_token_lifetime: min=1 max=3600 pattern=    """
    
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
    vendor: Literal["unknown", "google-cloud-kms"] | None = Field(default="unknown", description="Cloud service vendor.")    
    traffic_vdom: str | None = Field(max_length=31, default="", description="Vdom used to communicate with cloud service.")  # datasource: ['system.vdom.name']    
    gck_service_account: str | None = Field(max_length=285, default="", description="Service account (e.g. \"account-id@sampledomain.com\").")    
    gck_private_key: str | None = Field(max_length=8191, default="", description="Service account private key in PEM format (e.g. \"-----BEGIN PRIVATE KEY-----\\ ...\").")    
    gck_keyid: str | None = Field(max_length=127, default="", description="Key id, also referred as \"kid\".")    
    gck_access_token_lifetime: int | None = Field(ge=1, le=3600, default=60, description="Lifetime of automatically generated access tokens in minutes (default is 60 minutes).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('traffic_vdom')
    @classmethod
    def validate_traffic_vdom(cls, v: Any) -> Any:
        """
        Validate traffic_vdom field.
        
        Datasource: ['system.vdom.name']
        
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
    async def validate_traffic_vdom_references(self, client: Any) -> list[str]:
        """
        Validate traffic_vdom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/vdom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CloudServiceModel(
            ...     traffic_vdom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_traffic_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.cloud_service.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "traffic_vdom", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.vdom.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Traffic-Vdom '{value}' not found in "
                "system/vdom"
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
        
        errors = await self.validate_traffic_vdom_references(client)
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
    "CloudServiceModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.778093Z
# ============================================================================
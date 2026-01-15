"""
Pydantic Models for CMDB - system/api_user

Runtime validation models for system/api_user configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ApiUserVdom(BaseModel):
    """
    Child table model for vdom.
    
    Virtual domains.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Virtual domain name.")  # datasource: ['system.vdom.name']
class ApiUserTrusthost(BaseModel):
    """
    Child table model for trusthost.
    
    Trusthost.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ID.")    
    type: Literal["ipv4-trusthost", "ipv6-trusthost"] | None = Field(default="ipv4-trusthost", description="Trusthost type.")    
    ipv4_trusthost: str | None = Field(default="0.0.0.0 0.0.0.0", description="IPv4 trusted host address.")    
    ipv6_trusthost: str | None = Field(default="::/0", description="IPv6 trusted host address.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ApiUserModel(BaseModel):
    """
    Pydantic model for system/api_user configuration.
    
    Configure API users.
    
    Validation Rules:        - name: max_length=35 pattern=        - comments: max_length=255 pattern=        - api_key: max_length=128 pattern=        - accprofile: max_length=35 pattern=        - vdom: pattern=        - schedule: max_length=35 pattern=        - cors_allow_origin: max_length=269 pattern=        - peer_auth: pattern=        - peer_group: max_length=35 pattern=        - trusthost: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="User name.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    api_key: Any = Field(max_length=128, default=None, description="Admin user password.")    
    accprofile: str = Field(max_length=35, default="", description="Admin user access profile.")  # datasource: ['system.accprofile.name']    
    vdom: list[Vdom] = Field(default=None, description="Virtual domains.")    
    schedule: str | None = Field(max_length=35, default="", description="Schedule name.")    
    cors_allow_origin: str | None = Field(max_length=269, default="", description="Value for Access-Control-Allow-Origin on API responses. Avoid using '*' if possible.")    
    peer_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable peer authentication.")    
    peer_group: str = Field(max_length=35, default="", description="Peer group name.")    
    trusthost: list[Trusthost] = Field(default=None, description="Trusthost.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('accprofile')
    @classmethod
    def validate_accprofile(cls, v: Any) -> Any:
        """
        Validate accprofile field.
        
        Datasource: ['system.accprofile.name']
        
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
    async def validate_accprofile_references(self, client: Any) -> list[str]:
        """
        Validate accprofile references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/accprofile        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ApiUserModel(
            ...     accprofile="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_accprofile_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.api_user.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "accprofile", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.accprofile.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Accprofile '{value}' not found in "
                "system/accprofile"
            )        
        return errors    
    async def validate_vdom_references(self, client: Any) -> list[str]:
        """
        Validate vdom references exist in FortiGate.
        
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
            >>> policy = ApiUserModel(
            ...     vdom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.api_user.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "vdom", [])
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
            if await client.api.cmdb.system.vdom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Vdom '{value}' not found in "
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
        
        errors = await self.validate_accprofile_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vdom_references(client)
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
    "ApiUserModel",    "ApiUserVdom",    "ApiUserTrusthost",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.223975Z
# ============================================================================
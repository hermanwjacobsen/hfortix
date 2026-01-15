"""
Pydantic Models for CMDB - user/fsso_polling

Runtime validation models for user/fsso_polling configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class FssoPollingAdgrp(BaseModel):
    """
    Child table model for adgrp.
    
    LDAP Group Info.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=511, default="", description="Name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class FssoPollingModel(BaseModel):
    """
    Pydantic model for user/fsso_polling configuration.
    
    Configure FSSO active directory servers for polling mode.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - status: pattern=        - server: max_length=63 pattern=        - default_domain: max_length=35 pattern=        - port: min=0 max=65535 pattern=        - user: max_length=35 pattern=        - password: max_length=128 pattern=        - ldap_server: max_length=35 pattern=        - logon_history: min=0 max=48 pattern=        - polling_frequency: min=1 max=30 pattern=        - adgrp: pattern=        - smbv1: pattern=        - smb_ntlmv1_auth: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Active Directory server ID.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable polling for the status of this Active Directory server.")    
    server: str = Field(max_length=63, default="", description="Host name or IP address of the Active Directory server.")    
    default_domain: str | None = Field(max_length=35, default="", description="Default domain managed by this Active Directory server.")    
    port: int | None = Field(ge=0, le=65535, default=0, description="Port to communicate with this Active Directory server.")    
    user: str = Field(max_length=35, default="", description="User name required to log into this Active Directory server.")    
    password: Any = Field(max_length=128, default=None, description="Password required to log into this Active Directory server.")    
    ldap_server: str = Field(max_length=35, default="", description="LDAP server name used in LDAP connection strings.")  # datasource: ['user.ldap.name']    
    logon_history: int | None = Field(ge=0, le=48, default=8, description="Number of hours of logon history to keep, 0 means keep all history.")    
    polling_frequency: int | None = Field(ge=1, le=30, default=10, description="Polling frequency (every 1 to 30 seconds).")    
    adgrp: list[Adgrp] = Field(default=None, description="LDAP Group Info.")    
    smbv1: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable support of SMBv1 for Samba.")    
    smb_ntlmv1_auth: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable support of NTLMv1 for Samba authentication.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ldap_server')
    @classmethod
    def validate_ldap_server(cls, v: Any) -> Any:
        """
        Validate ldap_server field.
        
        Datasource: ['user.ldap.name']
        
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
    async def validate_ldap_server_references(self, client: Any) -> list[str]:
        """
        Validate ldap_server references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/ldap        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = FssoPollingModel(
            ...     ldap_server="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ldap_server_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.fsso_polling.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ldap_server", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.user.ldap.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ldap-Server '{value}' not found in "
                "user/ldap"
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
        
        errors = await self.validate_ldap_server_references(client)
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
    "FssoPollingModel",    "FssoPollingAdgrp",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.491383Z
# ============================================================================
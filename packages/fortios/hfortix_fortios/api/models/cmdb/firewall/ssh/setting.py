"""
Pydantic Models for CMDB - firewall/ssh/setting

Runtime validation models for firewall/ssh/setting configuration.
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

class SettingModel(BaseModel):
    """
    Pydantic model for firewall/ssh/setting configuration.
    
    SSH proxy settings.
    
    Validation Rules:        - caname: max_length=35 pattern=        - untrusted_caname: max_length=35 pattern=        - hostkey_rsa2048: max_length=35 pattern=        - hostkey_dsa1024: max_length=35 pattern=        - hostkey_ecdsa256: max_length=35 pattern=        - hostkey_ecdsa384: max_length=35 pattern=        - hostkey_ecdsa521: max_length=35 pattern=        - hostkey_ed25519: max_length=35 pattern=        - host_trusted_checking: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    caname: str | None = Field(max_length=35, default="", description="CA certificate used by SSH Inspection.")  # datasource: ['firewall.ssh.local-ca.name']    
    untrusted_caname: str | None = Field(max_length=35, default="", description="Untrusted CA certificate used by SSH Inspection.")  # datasource: ['firewall.ssh.local-ca.name']    
    hostkey_rsa2048: str | None = Field(max_length=35, default="", description="RSA certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_dsa1024: str | None = Field(max_length=35, default="", description="DSA certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ecdsa256: str | None = Field(max_length=35, default="", description="ECDSA nid256 certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ecdsa384: str | None = Field(max_length=35, default="", description="ECDSA nid384 certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ecdsa521: str | None = Field(max_length=35, default="", description="ECDSA nid384 certificate used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    hostkey_ed25519: str | None = Field(max_length=35, default="", description="ED25519 hostkey used by SSH proxy.")  # datasource: ['firewall.ssh.local-key.name']    
    host_trusted_checking: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable host trusted checking.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('caname')
    @classmethod
    def validate_caname(cls, v: Any) -> Any:
        """
        Validate caname field.
        
        Datasource: ['firewall.ssh.local-ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('untrusted_caname')
    @classmethod
    def validate_untrusted_caname(cls, v: Any) -> Any:
        """
        Validate untrusted_caname field.
        
        Datasource: ['firewall.ssh.local-ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_rsa2048')
    @classmethod
    def validate_hostkey_rsa2048(cls, v: Any) -> Any:
        """
        Validate hostkey_rsa2048 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_dsa1024')
    @classmethod
    def validate_hostkey_dsa1024(cls, v: Any) -> Any:
        """
        Validate hostkey_dsa1024 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ecdsa256')
    @classmethod
    def validate_hostkey_ecdsa256(cls, v: Any) -> Any:
        """
        Validate hostkey_ecdsa256 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ecdsa384')
    @classmethod
    def validate_hostkey_ecdsa384(cls, v: Any) -> Any:
        """
        Validate hostkey_ecdsa384 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ecdsa521')
    @classmethod
    def validate_hostkey_ecdsa521(cls, v: Any) -> Any:
        """
        Validate hostkey_ecdsa521 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('hostkey_ed25519')
    @classmethod
    def validate_hostkey_ed25519(cls, v: Any) -> Any:
        """
        Validate hostkey_ed25519 field.
        
        Datasource: ['firewall.ssh.local-key.name']
        
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
    async def validate_caname_references(self, client: Any) -> list[str]:
        """
        Validate caname references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     caname="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_caname_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "caname", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Caname '{value}' not found in "
                "firewall/ssh/local-ca"
            )        
        return errors    
    async def validate_untrusted_caname_references(self, client: Any) -> list[str]:
        """
        Validate untrusted_caname references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     untrusted_caname="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_untrusted_caname_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "untrusted_caname", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Untrusted-Caname '{value}' not found in "
                "firewall/ssh/local-ca"
            )        
        return errors    
    async def validate_hostkey_rsa2048_references(self, client: Any) -> list[str]:
        """
        Validate hostkey_rsa2048 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-key        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     hostkey_rsa2048="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_hostkey_rsa2048_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "hostkey_rsa2048", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-key.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Hostkey-Rsa2048 '{value}' not found in "
                "firewall/ssh/local-key"
            )        
        return errors    
    async def validate_hostkey_dsa1024_references(self, client: Any) -> list[str]:
        """
        Validate hostkey_dsa1024 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-key        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     hostkey_dsa1024="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_hostkey_dsa1024_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "hostkey_dsa1024", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-key.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Hostkey-Dsa1024 '{value}' not found in "
                "firewall/ssh/local-key"
            )        
        return errors    
    async def validate_hostkey_ecdsa256_references(self, client: Any) -> list[str]:
        """
        Validate hostkey_ecdsa256 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-key        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     hostkey_ecdsa256="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_hostkey_ecdsa256_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "hostkey_ecdsa256", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-key.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Hostkey-Ecdsa256 '{value}' not found in "
                "firewall/ssh/local-key"
            )        
        return errors    
    async def validate_hostkey_ecdsa384_references(self, client: Any) -> list[str]:
        """
        Validate hostkey_ecdsa384 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-key        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     hostkey_ecdsa384="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_hostkey_ecdsa384_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "hostkey_ecdsa384", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-key.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Hostkey-Ecdsa384 '{value}' not found in "
                "firewall/ssh/local-key"
            )        
        return errors    
    async def validate_hostkey_ecdsa521_references(self, client: Any) -> list[str]:
        """
        Validate hostkey_ecdsa521 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-key        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     hostkey_ecdsa521="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_hostkey_ecdsa521_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "hostkey_ecdsa521", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-key.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Hostkey-Ecdsa521 '{value}' not found in "
                "firewall/ssh/local-key"
            )        
        return errors    
    async def validate_hostkey_ed25519_references(self, client: Any) -> list[str]:
        """
        Validate hostkey_ed25519 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ssh/local-key        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     hostkey_ed25519="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_hostkey_ed25519_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssh.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "hostkey_ed25519", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.ssh.local-key.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Hostkey-Ed25519 '{value}' not found in "
                "firewall/ssh/local-key"
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
        
        errors = await self.validate_caname_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_untrusted_caname_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_hostkey_rsa2048_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_hostkey_dsa1024_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_hostkey_ecdsa256_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_hostkey_ecdsa384_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_hostkey_ecdsa521_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_hostkey_ed25519_references(client)
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
    "SettingModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:58.047591Z
# ============================================================================
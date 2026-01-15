"""
Pydantic Models for CMDB - switch_controller/security_policy/x802_1x

Runtime validation models for switch_controller/security_policy/x802_1x configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class X8021xUserGroup(BaseModel):
    """
    Child table model for user-group.
    
    Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Group name.")  # datasource: ['user.group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class X8021xModel(BaseModel):
    """
    Pydantic model for switch_controller/security_policy/x802_1x configuration.
    
    Configure 802.1x MAC Authentication Bypass (MAB) policies.
    
    Validation Rules:        - name: max_length=31 pattern=        - security_mode: pattern=        - user_group: pattern=        - mac_auth_bypass: pattern=        - auth_order: pattern=        - auth_priority: pattern=        - open_auth: pattern=        - eap_passthru: pattern=        - eap_auto_untagged_vlans: pattern=        - guest_vlan: pattern=        - guest_vlan_id: max_length=15 pattern=        - guest_auth_delay: min=1 max=900 pattern=        - auth_fail_vlan: pattern=        - auth_fail_vlan_id: max_length=15 pattern=        - framevid_apply: pattern=        - radius_timeout_overwrite: pattern=        - policy_type: pattern=        - authserver_timeout_period: min=3 max=15 pattern=        - authserver_timeout_vlan: pattern=        - authserver_timeout_vlanid: max_length=15 pattern=        - authserver_timeout_tagged: pattern=        - authserver_timeout_tagged_vlanid: max_length=15 pattern=        - dacl: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=31, default="", description="Policy name.")    
    security_mode: Literal["802.1X", "802.1X-mac-based"] | None = Field(default="802.1X", description="Port or MAC based 802.1X security mode.")    
    user_group: list[UserGroup] = Field(description="Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.")    
    mac_auth_bypass: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable MAB for this policy.")    
    auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = Field(default="mab-dot1x", description="Configure authentication order.")    
    auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = Field(default="legacy", description="Configure authentication priority.")    
    open_auth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable open authentication for this policy.")    
    eap_passthru: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication.")    
    eap_auto_untagged_vlans: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable automatic inclusion of untagged VLANs.")    
    guest_vlan: Literal["disable", "enable"] | None = Field(default="disable", description="Enable the guest VLAN feature to allow limited access to non-802.1X-compliant clients.")    
    guest_vlan_id: str = Field(max_length=15, default="", description="Guest VLAN name.")  # datasource: ['system.interface.name']    
    guest_auth_delay: int | None = Field(ge=1, le=900, default=30, description="Guest authentication delay (1 - 900  sec, default = 30).")    
    auth_fail_vlan: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to allow limited access to clients that cannot authenticate.")    
    auth_fail_vlan_id: str = Field(max_length=15, default="", description="VLAN ID on which authentication failed.")  # datasource: ['system.interface.name']    
    framevid_apply: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable the capability to apply the EAP/MAB frame VLAN to the port native VLAN.")    
    radius_timeout_overwrite: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to override the global RADIUS session timeout.")    
    policy_type: Literal["802.1X"] | None = Field(default="802.1X", description="Policy type.")    
    authserver_timeout_period: int | None = Field(ge=3, le=15, default=3, description="Authentication server timeout period (3 - 15 sec, default = 3).")    
    authserver_timeout_vlan: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable the authentication server timeout VLAN to allow limited access when RADIUS is unavailable.")    
    authserver_timeout_vlanid: str = Field(max_length=15, default="", description="Authentication server timeout VLAN name.")  # datasource: ['system.interface.name']    
    authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = Field(default="disable", description="Configure timeout option for the tagged VLAN which allows limited access when the authentication server is unavailable.")    
    authserver_timeout_tagged_vlanid: str = Field(max_length=15, default="", description="Tagged VLAN name for which the timeout option is applied to (only one VLAN ID).")  # datasource: ['system.interface.name']    
    dacl: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable dynamic access control list on this interface.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('guest_vlan_id')
    @classmethod
    def validate_guest_vlan_id(cls, v: Any) -> Any:
        """
        Validate guest_vlan_id field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_fail_vlan_id')
    @classmethod
    def validate_auth_fail_vlan_id(cls, v: Any) -> Any:
        """
        Validate auth_fail_vlan_id field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('authserver_timeout_vlanid')
    @classmethod
    def validate_authserver_timeout_vlanid(cls, v: Any) -> Any:
        """
        Validate authserver_timeout_vlanid field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('authserver_timeout_tagged_vlanid')
    @classmethod
    def validate_authserver_timeout_tagged_vlanid(cls, v: Any) -> Any:
        """
        Validate authserver_timeout_tagged_vlanid field.
        
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
    async def validate_user_group_references(self, client: Any) -> list[str]:
        """
        Validate user_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = X8021xModel(
            ...     user_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_user_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.security_policy.x802_1x.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "user_group", [])
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
            if await client.api.cmdb.user.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"User-Group '{value}' not found in "
                    "user/group"
                )        
        return errors    
    async def validate_guest_vlan_id_references(self, client: Any) -> list[str]:
        """
        Validate guest_vlan_id references exist in FortiGate.
        
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
            >>> policy = X8021xModel(
            ...     guest_vlan_id="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_guest_vlan_id_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.security_policy.x802_1x.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "guest_vlan_id", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Guest-Vlan-Id '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_auth_fail_vlan_id_references(self, client: Any) -> list[str]:
        """
        Validate auth_fail_vlan_id references exist in FortiGate.
        
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
            >>> policy = X8021xModel(
            ...     auth_fail_vlan_id="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_fail_vlan_id_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.security_policy.x802_1x.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_fail_vlan_id", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Fail-Vlan-Id '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_authserver_timeout_vlanid_references(self, client: Any) -> list[str]:
        """
        Validate authserver_timeout_vlanid references exist in FortiGate.
        
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
            >>> policy = X8021xModel(
            ...     authserver_timeout_vlanid="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_authserver_timeout_vlanid_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.security_policy.x802_1x.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "authserver_timeout_vlanid", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Authserver-Timeout-Vlanid '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_authserver_timeout_tagged_vlanid_references(self, client: Any) -> list[str]:
        """
        Validate authserver_timeout_tagged_vlanid references exist in FortiGate.
        
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
            >>> policy = X8021xModel(
            ...     authserver_timeout_tagged_vlanid="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_authserver_timeout_tagged_vlanid_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.security_policy.x802_1x.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "authserver_timeout_tagged_vlanid", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Authserver-Timeout-Tagged-Vlanid '{value}' not found in "
                "system/interface"
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
        
        errors = await self.validate_user_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_guest_vlan_id_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_fail_vlan_id_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_authserver_timeout_vlanid_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_authserver_timeout_tagged_vlanid_references(client)
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
    "X8021xModel",    "X8021xUserGroup",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.109616Z
# ============================================================================
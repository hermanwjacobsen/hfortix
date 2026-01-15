"""
Pydantic Models for CMDB - user/nac_policy

Runtime validation models for user/nac_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class NacPolicySeverity(BaseModel):
    """
    Child table model for severity.
    
    NAC policy matching devices vulnerability severity lists.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    severity_num: int = Field(ge=0, le=4, default=0, description="Enter multiple severity levels, where 0 = Info, 1 = Low, ..., 4 = Critical")
class NacPolicySwitchGroup(BaseModel):
    """
    Child table model for switch-group.
    
    List of managed FortiSwitch groups on which NAC policy can be applied.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Managed FortiSwitch group name from available options.")  # datasource: ['switch-controller.switch-group.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class NacPolicyCategoryEnum(str, Enum):
    """Allowed values for category field."""
    DEVICE = "device"    FIREWALL_USER = "firewall-user"    EMS_TAG = "ems-tag"    FORTIVOICE_TAG = "fortivoice-tag"    VULNERABILITY = "vulnerability"

# ============================================================================
# Main Model
# ============================================================================

class NacPolicyModel(BaseModel):
    """
    Pydantic model for user/nac_policy configuration.
    
    Configure NAC policy matching pattern to identify matching NAC devices.
    
    Validation Rules:        - name: max_length=63 pattern=        - description: max_length=63 pattern=        - category: pattern=        - status: pattern=        - match_type: pattern=        - match_period: min=0 max=120 pattern=        - match_remove: pattern=        - mac: max_length=17 pattern=        - hw_vendor: max_length=15 pattern=        - type: max_length=15 pattern=        - family: max_length=31 pattern=        - os: max_length=31 pattern=        - hw_version: max_length=15 pattern=        - sw_version: max_length=15 pattern=        - host: max_length=64 pattern=        - user: max_length=64 pattern=        - src: max_length=15 pattern=        - user_group: max_length=35 pattern=        - ems_tag: max_length=79 pattern=        - fortivoice_tag: max_length=79 pattern=        - severity: pattern=        - switch_fortilink: max_length=15 pattern=        - switch_group: pattern=        - switch_mac_policy: max_length=63 pattern=        - firewall_address: max_length=79 pattern=        - ssid_policy: max_length=35 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="NAC policy name.")    
    description: str | None = Field(max_length=63, default="", description="Description for the NAC policy matching pattern.")    
    category: CategoryEnum | None = Field(default="device", description="Category of NAC policy.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable NAC policy.")    
    match_type: Literal["dynamic", "override"] | None = Field(default="dynamic", description="Match and retain the devices based on the type.")    
    match_period: int | None = Field(ge=0, le=120, default=0, description="Number of days the matched devices will be retained (0 - always retain)")    
    match_remove: Literal["default", "link-down"] | None = Field(default="default", description="Options to remove the matched override devices.")    
    mac: str | None = Field(max_length=17, default="", description="NAC policy matching MAC address.")    
    hw_vendor: str | None = Field(max_length=15, default="", description="NAC policy matching hardware vendor.")    
    type: str | None = Field(max_length=15, default="", description="NAC policy matching type.")    
    family: str | None = Field(max_length=31, default="", description="NAC policy matching family.")    
    os: str | None = Field(max_length=31, default="", description="NAC policy matching operating system.")    
    hw_version: str | None = Field(max_length=15, default="", description="NAC policy matching hardware version.")    
    sw_version: str | None = Field(max_length=15, default="", description="NAC policy matching software version.")    
    host: str | None = Field(max_length=64, default="", description="NAC policy matching host.")    
    user: str | None = Field(max_length=64, default="", description="NAC policy matching user.")    
    src: str | None = Field(max_length=15, default="", description="NAC policy matching source.")    
    user_group: str | None = Field(max_length=35, default="", description="NAC policy matching user group.")  # datasource: ['user.group.name']    
    ems_tag: str | None = Field(max_length=79, default="", description="NAC policy matching EMS tag.")  # datasource: ['firewall.address.name']    
    fortivoice_tag: str | None = Field(max_length=79, default="", description="NAC policy matching FortiVoice tag.")  # datasource: ['firewall.address.name']    
    severity: list[Severity] = Field(default=None, description="NAC policy matching devices vulnerability severity lists.")    
    switch_fortilink: str | None = Field(max_length=15, default="", description="FortiLink interface for which this NAC policy belongs to.")  # datasource: ['system.interface.name']    
    switch_group: list[SwitchGroup] = Field(default=None, description="List of managed FortiSwitch groups on which NAC policy can be applied.")    
    switch_mac_policy: str | None = Field(max_length=63, default="", description="Switch MAC policy action to be applied on the matched NAC policy.")  # datasource: ['switch-controller.mac-policy.name']    
    firewall_address: str | None = Field(max_length=79, default="", description="Dynamic firewall address to associate MAC which match this policy.")  # datasource: ['firewall.address.name']    
    ssid_policy: str | None = Field(max_length=35, default="", description="SSID policy to be applied on the matched NAC policy.")  # datasource: ['wireless-controller.ssid-policy.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('user_group')
    @classmethod
    def validate_user_group(cls, v: Any) -> Any:
        """
        Validate user_group field.
        
        Datasource: ['user.group.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ems_tag')
    @classmethod
    def validate_ems_tag(cls, v: Any) -> Any:
        """
        Validate ems_tag field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('fortivoice_tag')
    @classmethod
    def validate_fortivoice_tag(cls, v: Any) -> Any:
        """
        Validate fortivoice_tag field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('switch_fortilink')
    @classmethod
    def validate_switch_fortilink(cls, v: Any) -> Any:
        """
        Validate switch_fortilink field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('switch_mac_policy')
    @classmethod
    def validate_switch_mac_policy(cls, v: Any) -> Any:
        """
        Validate switch_mac_policy field.
        
        Datasource: ['switch-controller.mac-policy.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('firewall_address')
    @classmethod
    def validate_firewall_address(cls, v: Any) -> Any:
        """
        Validate firewall_address field.
        
        Datasource: ['firewall.address.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssid_policy')
    @classmethod
    def validate_ssid_policy(cls, v: Any) -> Any:
        """
        Validate ssid_policy field.
        
        Datasource: ['wireless-controller.ssid-policy.name']
        
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
            >>> policy = NacPolicyModel(
            ...     user_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_user_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "user_group", None)
        if not value:
            return errors
        
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
    async def validate_ems_tag_references(self, client: Any) -> list[str]:
        """
        Validate ems_tag references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = NacPolicyModel(
            ...     ems_tag="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ems_tag_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ems_tag", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ems-Tag '{value}' not found in "
                "firewall/address"
            )        
        return errors    
    async def validate_fortivoice_tag_references(self, client: Any) -> list[str]:
        """
        Validate fortivoice_tag references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = NacPolicyModel(
            ...     fortivoice_tag="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_fortivoice_tag_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "fortivoice_tag", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Fortivoice-Tag '{value}' not found in "
                "firewall/address"
            )        
        return errors    
    async def validate_switch_fortilink_references(self, client: Any) -> list[str]:
        """
        Validate switch_fortilink references exist in FortiGate.
        
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
            >>> policy = NacPolicyModel(
            ...     switch_fortilink="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_switch_fortilink_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "switch_fortilink", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Switch-Fortilink '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_switch_group_references(self, client: Any) -> list[str]:
        """
        Validate switch_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/switch-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = NacPolicyModel(
            ...     switch_group=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_switch_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "switch_group", [])
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
            if await client.api.cmdb.switch-controller.switch-group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Switch-Group '{value}' not found in "
                    "switch-controller/switch-group"
                )        
        return errors    
    async def validate_switch_mac_policy_references(self, client: Any) -> list[str]:
        """
        Validate switch_mac_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/mac-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = NacPolicyModel(
            ...     switch_mac_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_switch_mac_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "switch_mac_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.mac-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Switch-Mac-Policy '{value}' not found in "
                "switch-controller/mac-policy"
            )        
        return errors    
    async def validate_firewall_address_references(self, client: Any) -> list[str]:
        """
        Validate firewall_address references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = NacPolicyModel(
            ...     firewall_address="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_firewall_address_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "firewall_address", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Firewall-Address '{value}' not found in "
                "firewall/address"
            )        
        return errors    
    async def validate_ssid_policy_references(self, client: Any) -> list[str]:
        """
        Validate ssid_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - wireless-controller/ssid-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = NacPolicyModel(
            ...     ssid_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssid_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.user.nac_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssid_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.wireless-controller.ssid-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssid-Policy '{value}' not found in "
                "wireless-controller/ssid-policy"
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
        errors = await self.validate_ems_tag_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_fortivoice_tag_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_switch_fortilink_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_switch_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_switch_mac_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_firewall_address_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssid_policy_references(client)
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
    "NacPolicyModel",    "NacPolicySeverity",    "NacPolicySwitchGroup",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.939813Z
# ============================================================================
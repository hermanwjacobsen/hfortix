"""
Pydantic Models for CMDB - switch_controller/lldp_profile

Runtime validation models for switch_controller/lldp_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class LldpProfileMedNetworkPolicy(BaseModel):
    """
    Child table model for med-network-policy.
    
    Configuration method to edit Media Endpoint Discovery (MED) network policy type-length-value (TLV) categories.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Policy type name.")    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable or disable this TLV.")    
    vlan_intf: str | None = Field(max_length=15, default="", description="VLAN interface to advertise; if configured on port.")  # datasource: ['system.interface.name']    
    assign_vlan: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable VLAN assignment when this profile is applied on managed FortiSwitch port.")    
    priority: int | None = Field(ge=0, le=7, default=0, description="Advertised Layer 2 priority (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=0, description="Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service requested for traffic, such as high priority or best effort delivery.")
class LldpProfileMedLocationService(BaseModel):
    """
    Child table model for med-location-service.
    
    Configuration method to edit Media Endpoint Discovery (MED) location service type-length-value (TLV) categories.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Location service type name.")    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable or disable this TLV.")    
    sys_location_id: str | None = Field(max_length=63, default="", description="Location service ID.")  # datasource: ['switch-controller.location.name']
class LldpProfileCustomTlvs(BaseModel):
    """
    Child table model for custom-tlvs.
    
    Configuration method to edit custom TLV entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="TLV name (not sent).")    
    oui: str = Field(default="000000", description="Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV.")    
    subtype: int | None = Field(ge=0, le=255, default=0, description="Organizationally defined subtype (0 - 255).")    
    information_string: str | None = Field(default="", description="Organizationally defined information string (0 - 507 hexadecimal bytes).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LldpProfileMed_tlvsEnum(str, Enum):
    """Allowed values for med_tlvs field."""
    INVENTORY_MANAGEMENT = "inventory-management"    NETWORK_POLICY = "network-policy"    POWER_MANAGEMENT = "power-management"    LOCATION_IDENTIFICATION = "location-identification"

# ============================================================================
# Main Model
# ============================================================================

class LldpProfileModel(BaseModel):
    """
    Pydantic model for switch_controller/lldp_profile configuration.
    
    Configure FortiSwitch LLDP profiles.
    
    Validation Rules:        - name: max_length=63 pattern=        - med_tlvs: pattern=        - 802.1_tlvs: pattern=        - 802.3_tlvs: pattern=        - auto_isl: pattern=        - auto_isl_hello_timer: min=1 max=30 pattern=        - auto_isl_receive_timeout: min=0 max=90 pattern=        - auto_isl_port_group: min=0 max=9 pattern=        - auto_mclag_icl: pattern=        - auto_isl_auth: pattern=        - auto_isl_auth_user: max_length=63 pattern=        - auto_isl_auth_identity: max_length=63 pattern=        - auto_isl_auth_reauth: min=180 max=3600 pattern=        - auto_isl_auth_encrypt: pattern=        - auto_isl_auth_macsec_profile: max_length=63 pattern=        - med_network_policy: pattern=        - med_location_service: pattern=        - custom_tlvs: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=63, default="", description="Profile name.")    
    med_tlvs: list[MedTlvs] = Field(default="", description="Transmitted LLDP-MED TLVs (type-length-value descriptions).")    
    802.1_tlvs: list[802.1Tlvs] = Field(default="", description="Transmitted IEEE 802.1 TLVs.")    
    802.3_tlvs: list[802.3Tlvs] = Field(default="", description="Transmitted IEEE 802.3 TLVs.")    
    auto_isl: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable auto inter-switch LAG.")    
    auto_isl_hello_timer: int | None = Field(ge=1, le=30, default=3, description="Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3).")    
    auto_isl_receive_timeout: int | None = Field(ge=0, le=90, default=60, description="Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 9).")    
    auto_isl_port_group: int | None = Field(ge=0, le=9, default=0, description="Auto inter-switch LAG port group ID (0 - 9).")    
    auto_mclag_icl: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable MCLAG inter chassis link.")    
    auto_isl_auth: Literal["legacy", "strict", "relax"] | None = Field(default="legacy", description="Auto inter-switch LAG authentication mode.")    
    auto_isl_auth_user: str | None = Field(max_length=63, default="", description="Auto inter-switch LAG authentication user certificate.")    
    auto_isl_auth_identity: str | None = Field(max_length=63, default="", description="Auto inter-switch LAG authentication identity.")    
    auto_isl_auth_reauth: int | None = Field(ge=180, le=3600, default=3600, description="Auto inter-switch LAG authentication reauth period in seconds(10 - 3600, default = 3600).")    
    auto_isl_auth_encrypt: Literal["none", "mixed", "must"] | None = Field(default="none", description="Auto inter-switch LAG encryption mode.")    
    auto_isl_auth_macsec_profile: str | None = Field(max_length=63, default="", description="Auto inter-switch LAG macsec profile for encryption.")    
    med_network_policy: list[MedNetworkPolicy] = Field(default=None, description="Configuration method to edit Media Endpoint Discovery (MED) network policy type-length-value (TLV) categories.")    
    med_location_service: list[MedLocationService] = Field(default=None, description="Configuration method to edit Media Endpoint Discovery (MED) location service type-length-value (TLV) categories.")    
    custom_tlvs: list[CustomTlvs] = Field(default=None, description="Configuration method to edit custom TLV entries.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    async def validate_med_network_policy_references(self, client: Any) -> list[str]:
        """
        Validate med_network_policy references exist in FortiGate.
        
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
            >>> policy = LldpProfileModel(
            ...     med_network_policy=[{"vlan-intf": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_med_network_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.lldp_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "med_network_policy", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("vlan-intf")
            else:
                value = getattr(item, "vlan-intf", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Med-Network-Policy '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_med_location_service_references(self, client: Any) -> list[str]:
        """
        Validate med_location_service references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/location        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LldpProfileModel(
            ...     med_location_service=[{"sys-location-id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_med_location_service_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.lldp_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "med_location_service", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("sys-location-id")
            else:
                value = getattr(item, "sys-location-id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.switch-controller.location.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Med-Location-Service '{value}' not found in "
                    "switch-controller/location"
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
        
        errors = await self.validate_med_network_policy_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_med_location_service_references(client)
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
    "LldpProfileModel",    "LldpProfileMedNetworkPolicy",    "LldpProfileMedLocationService",    "LldpProfileCustomTlvs",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.237497Z
# ============================================================================
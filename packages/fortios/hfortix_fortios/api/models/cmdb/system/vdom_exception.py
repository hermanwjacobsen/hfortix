"""
Pydantic Models for CMDB - system/vdom_exception

Runtime validation models for system/vdom_exception configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class VdomExceptionVdom(BaseModel):
    """
    Child table model for vdom.
    
    Names of the VDOMs.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="VDOM name.")  # datasource: ['system.vdom.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class VdomExceptionObjectEnum(str, Enum):
    """Allowed values for object field."""
    LOG_FORTIANALYZER_SETTING = "log.fortianalyzer.setting"    LOG_FORTIANALYZER_OVERRIDE_SETTING = "log.fortianalyzer.override-setting"    LOG_FORTIANALYZER2_SETTING = "log.fortianalyzer2.setting"    LOG_FORTIANALYZER2_OVERRIDE_SETTING = "log.fortianalyzer2.override-setting"    LOG_FORTIANALYZER3_SETTING = "log.fortianalyzer3.setting"    LOG_FORTIANALYZER3_OVERRIDE_SETTING = "log.fortianalyzer3.override-setting"    LOG_FORTIANALYZER_CLOUD_SETTING = "log.fortianalyzer-cloud.setting"    LOG_FORTIANALYZER_CLOUD_OVERRIDE_SETTING = "log.fortianalyzer-cloud.override-setting"    LOG_SYSLOGD_SETTING = "log.syslogd.setting"    LOG_SYSLOGD_OVERRIDE_SETTING = "log.syslogd.override-setting"    LOG_SYSLOGD2_SETTING = "log.syslogd2.setting"    LOG_SYSLOGD2_OVERRIDE_SETTING = "log.syslogd2.override-setting"    LOG_SYSLOGD3_SETTING = "log.syslogd3.setting"    LOG_SYSLOGD3_OVERRIDE_SETTING = "log.syslogd3.override-setting"    LOG_SYSLOGD4_SETTING = "log.syslogd4.setting"    LOG_SYSLOGD4_OVERRIDE_SETTING = "log.syslogd4.override-setting"    SYSTEM_GRE_TUNNEL = "system.gre-tunnel"    SYSTEM_CENTRAL_MANAGEMENT = "system.central-management"    SYSTEM_CSF = "system.csf"    USER_RADIUS = "user.radius"    SYSTEM_INTERFACE = "system.interface"    VPN_IPSEC_PHASE1_INTERFACE = "vpn.ipsec.phase1-interface"    VPN_IPSEC_PHASE2_INTERFACE = "vpn.ipsec.phase2-interface"    ROUTER_BGP = "router.bgp"    ROUTER_ROUTE_MAP = "router.route-map"    ROUTER_PREFIX_LIST = "router.prefix-list"    FIREWALL_IPPOOL = "firewall.ippool"    FIREWALL_IPPOOL6 = "firewall.ippool6"    ROUTER_STATIC = "router.static"    ROUTER_STATIC6 = "router.static6"    FIREWALL_VIP = "firewall.vip"    FIREWALL_VIP6 = "firewall.vip6"    SYSTEM_SDWAN = "system.sdwan"    SYSTEM_SAML = "system.saml"    ROUTER_POLICY = "router.policy"    ROUTER_POLICY6 = "router.policy6"    LOG_SYSLOGD_SETTING = "log.syslogd.setting"    LOG_SYSLOGD_OVERRIDE_SETTING = "log.syslogd.override-setting"    FIREWALL_ADDRESS = "firewall.address"

# ============================================================================
# Main Model
# ============================================================================

class VdomExceptionModel(BaseModel):
    """
    Pydantic model for system/vdom_exception configuration.
    
    Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
    
    Validation Rules:        - id: min=1 max=4096 pattern=        - object: pattern=        - scope: pattern=        - vdom: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int | None = Field(ge=1, le=4096, default=0, description="Index (1 - 4096).")    
    object: ObjectEnum = Field(default="", description="Name of the configuration object that can be configured independently for all VDOMs.")    
    scope: Literal["all", "inclusive", "exclusive"] | None = Field(default="all", description="Determine whether the configuration object can be configured separately for all VDOMs or if some VDOMs share the same configuration.")    
    vdom: list[Vdom] = Field(default=None, description="Names of the VDOMs.")    
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
            >>> policy = VdomExceptionModel(
            ...     vdom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.vdom_exception.post(policy.to_fortios_dict())
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
    "VdomExceptionModel",    "VdomExceptionVdom",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.578300Z
# ============================================================================
"""
Pydantic Models for CMDB - switch_controller/global_

Runtime validation models for switch_controller/global_ configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class GlobalDisableDiscovery(BaseModel):
    """
    Child table model for disable-discovery.
    
    Prevent this FortiSwitch from discovering.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="FortiSwitch Serial-number.")
class GlobalCustomCommand(BaseModel):
    """
    Child table model for custom-command.
    
    List of custom commands to be pushed to all FortiSwitches in the VDOM.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    command_entry: str | None = Field(max_length=35, default="", description="List of FortiSwitch commands.")    
    command_name: str = Field(max_length=35, default="", description="Name of custom command to push to all FortiSwitches in VDOM.")  # datasource: ['switch-controller.custom-command.command-name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class GlobalDhcp_option82_circuit_idEnum(str, Enum):
    """Allowed values for dhcp_option82_circuit_id field."""
    INTFNAME = "intfname"    VLAN = "vlan"    HOSTNAME = "hostname"    MODE = "mode"    DESCRIPTION = "description"
class GlobalUpdate_user_deviceEnum(str, Enum):
    """Allowed values for update_user_device field."""
    MAC_CACHE = "mac-cache"    LLDP = "lldp"    DHCP_SNOOPING = "dhcp-snooping"    L2_DB = "l2-db"    L3_DB = "l3-db"

# ============================================================================
# Main Model
# ============================================================================

class GlobalModel(BaseModel):
    """
    Pydantic model for switch_controller/global_ configuration.
    
    Configure FortiSwitch global settings.
    
    Validation Rules:        - mac_aging_interval: min=10 max=1000000 pattern=        - https_image_push: pattern=        - vlan_all_mode: pattern=        - vlan_optimization: pattern=        - vlan_identity: pattern=        - disable_discovery: pattern=        - mac_retention_period: min=0 max=168 pattern=        - default_virtual_switch_vlan: max_length=15 pattern=        - dhcp_server_access_list: pattern=        - dhcp_option82_format: pattern=        - dhcp_option82_circuit_id: pattern=        - dhcp_option82_remote_id: pattern=        - dhcp_snoop_client_req: pattern=        - dhcp_snoop_client_db_exp: min=300 max=259200 pattern=        - dhcp_snoop_db_per_port_learn_limit: min=0 max=2048 pattern=        - log_mac_limit_violations: pattern=        - mac_violation_timer: min=0 max=4294967295 pattern=        - sn_dns_resolution: pattern=        - mac_event_logging: pattern=        - bounce_quarantined_link: pattern=        - quarantine_mode: pattern=        - update_user_device: pattern=        - custom_command: pattern=        - fips_enforce: pattern=        - firmware_provision_on_authorization: pattern=        - switch_on_deauth: pattern=        - firewall_auth_user_hold_period: min=5 max=1440 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    mac_aging_interval: int | None = Field(ge=10, le=1000000, default=300, description="Time after which an inactive MAC is aged out (10 - 1000000 sec, default = 300, 0 = disable).")    
    https_image_push: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable image push to FortiSwitch using HTTPS.")    
    vlan_all_mode: Literal["all", "defined"] | None = Field(default="defined", description="VLAN configuration mode, user-defined-vlans or all-possible-vlans.")    
    vlan_optimization: Literal["prune", "configured", "none"] | None = Field(default="configured", description="FortiLink VLAN optimization.")    
    vlan_identity: Literal["description", "name"] | None = Field(default="name", description="Identity of the VLAN. Commonly used for RADIUS Tunnel-Private-Group-Id.")    
    disable_discovery: list[DisableDiscovery] = Field(default=None, description="Prevent this FortiSwitch from discovering.")    
    mac_retention_period: int | None = Field(ge=0, le=168, default=24, description="Time in hours after which an inactive MAC is removed from client DB (0 = aged out based on mac-aging-interval).")    
    default_virtual_switch_vlan: str | None = Field(max_length=15, default="", description="Default VLAN for ports when added to the virtual-switch.")  # datasource: ['system.interface.name']    
    dhcp_server_access_list: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DHCP snooping server access list.")    
    dhcp_option82_format: Literal["ascii", "legacy"] | None = Field(default="ascii", description="DHCP option-82 format string.")    
    dhcp_option82_circuit_id: list[DhcpOption82CircuitId] = Field(default="intfname vlan mode", description="List the parameters to be included to inform about client identification.")    
    dhcp_option82_remote_id: list[DhcpOption82RemoteId] = Field(default="mac", description="List the parameters to be included to inform about client identification.")    
    dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = Field(default="drop-untrusted", description="Client DHCP packet broadcast mode.")    
    dhcp_snoop_client_db_exp: int | None = Field(ge=300, le=259200, default=86400, description="Expiry time for DHCP snooping server database entries (300 - 259200 sec, default = 86400 sec).")    
    dhcp_snoop_db_per_port_learn_limit: int | None = Field(ge=0, le=2048, default=64, description="Per Interface dhcp-server entries learn limit (0 - 1024, default = 64).")    
    log_mac_limit_violations: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logs for Learning Limit Violations.")    
    mac_violation_timer: int | None = Field(ge=0, le=4294967295, default=0, description="Set timeout for Learning Limit Violations (0 = disabled).")    
    sn_dns_resolution: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable DNS resolution of the FortiSwitch unit's IP address with switch name.")    
    mac_event_logging: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable MAC address event logging.")    
    bounce_quarantined_link: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last. Helps to re-initiate the DHCP process for a device.")    
    quarantine_mode: Literal["by-vlan", "by-redirect"] | None = Field(default="by-vlan", description="Quarantine mode.")    
    update_user_device: list[UpdateUserDevice] = Field(default="mac-cache lldp dhcp-snooping l2-db l3-db", description="Control which sources update the device user list.")    
    custom_command: list[CustomCommand] = Field(default=None, description="List of custom commands to be pushed to all FortiSwitches in the VDOM.")    
    fips_enforce: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable enforcement of FIPS on managed FortiSwitch devices.")    
    firmware_provision_on_authorization: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable automatic provisioning of latest firmware on authorization.")    
    switch_on_deauth: Literal["no-op", "factory-reset"] | None = Field(default="no-op", description="No-operation/Factory-reset the managed FortiSwitch on deauthorization.")    
    firewall_auth_user_hold_period: int | None = Field(ge=5, le=1440, default=5, description="Time period in minutes to hold firewall authenticated MAC users (5 - 1440, default = 5, disable = 0).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('default_virtual_switch_vlan')
    @classmethod
    def validate_default_virtual_switch_vlan(cls, v: Any) -> Any:
        """
        Validate default_virtual_switch_vlan field.
        
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
    async def validate_default_virtual_switch_vlan_references(self, client: Any) -> list[str]:
        """
        Validate default_virtual_switch_vlan references exist in FortiGate.
        
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
            >>> policy = GlobalModel(
            ...     default_virtual_switch_vlan="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_default_virtual_switch_vlan_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "default_virtual_switch_vlan", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Default-Virtual-Switch-Vlan '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_custom_command_references(self, client: Any) -> list[str]:
        """
        Validate custom_command references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/custom-command        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = GlobalModel(
            ...     custom_command=[{"command-name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_custom_command_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "custom_command", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("command-name")
            else:
                value = getattr(item, "command-name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.switch-controller.custom-command.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Custom-Command '{value}' not found in "
                    "switch-controller/custom-command"
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
        
        errors = await self.validate_default_virtual_switch_vlan_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_custom_command_references(client)
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
    "GlobalModel",    "GlobalDisableDiscovery",    "GlobalCustomCommand",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.559411Z
# ============================================================================
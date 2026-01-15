"""
Pydantic Models for CMDB - system/vdom_property

Runtime validation models for system/vdom_property configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class VdomPropertyModel(BaseModel):
    """
    Pydantic model for system/vdom_property configuration.
    
    Configure VDOM property.
    
    Validation Rules:        - name: max_length=31 pattern=        - description: max_length=127 pattern=        - snmp_index: min=1 max=2147483647 pattern=        - session: pattern=        - ipsec_phase1: pattern=        - ipsec_phase2: pattern=        - ipsec_phase1_interface: pattern=        - ipsec_phase2_interface: pattern=        - dialup_tunnel: pattern=        - firewall_policy: pattern=        - firewall_address: pattern=        - firewall_addrgrp: pattern=        - custom_service: pattern=        - service_group: pattern=        - onetime_schedule: pattern=        - recurring_schedule: pattern=        - user: pattern=        - user_group: pattern=        - sslvpn: pattern=        - proxy: pattern=        - log_disk_quota: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=31, default="", description="VDOM name.")  # datasource: ['system.vdom.name']    
    description: str | None = Field(max_length=127, default="", description="Description.")    
    snmp_index: int | None = Field(ge=1, le=2147483647, default=0, description="Permanent SNMP Index of the virtual domain (1 - 2147483647).")    
    session: list[Session] = Field(default="", description="Maximum guaranteed number of sessions.")    
    ipsec_phase1: list[IpsecPhase1] = Field(default="", description="Maximum guaranteed number of VPN IPsec phase 1 tunnels.")    
    ipsec_phase2: list[IpsecPhase2] = Field(default="", description="Maximum guaranteed number of VPN IPsec phase 2 tunnels.")    
    ipsec_phase1_interface: list[IpsecPhase1Interface] = Field(default="", description="Maximum guaranteed number of VPN IPsec phase1 interface tunnels.")    
    ipsec_phase2_interface: list[IpsecPhase2Interface] = Field(default="", description="Maximum guaranteed number of VPN IPsec phase2 interface tunnels.")    
    dialup_tunnel: list[DialupTunnel] = Field(default="", description="Maximum guaranteed number of dial-up tunnels.")    
    firewall_policy: list[FirewallPolicy] = Field(default="", description="Maximum guaranteed number of firewall policies (policy, DoS-policy4, DoS-policy6, multicast).")    
    firewall_address: list[FirewallAddress] = Field(default="", description="Maximum guaranteed number of firewall addresses (IPv4, IPv6, multicast).")    
    firewall_addrgrp: list[FirewallAddrgrp] = Field(default="", description="Maximum guaranteed number of firewall address groups (IPv4, IPv6).")    
    custom_service: list[CustomService] = Field(default="", description="Maximum guaranteed number of firewall custom services.")    
    service_group: list[ServiceGroup] = Field(default="", description="Maximum guaranteed number of firewall service groups.")    
    onetime_schedule: list[OnetimeSchedule] = Field(default="", description="Maximum guaranteed number of firewall one-time schedules..")    
    recurring_schedule: list[RecurringSchedule] = Field(default="", description="Maximum guaranteed number of firewall recurring schedules.")    
    user: list[User] = Field(default="", description="Maximum guaranteed number of local users.")    
    user_group: list[UserGroup] = Field(default="", description="Maximum guaranteed number of user groups.")    
    sslvpn: list[Sslvpn] = Field(default="", description="Maximum guaranteed number of Agentless VPNs.")    
    proxy: list[Proxy] = Field(default="", description="Maximum guaranteed number of concurrent proxy users.")    
    log_disk_quota: list[LogDiskQuota] = Field(default="", description="Log disk quota in megabytes (MB). Range depends on how much disk space is available.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: Any) -> Any:
        """
        Validate name field.
        
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
    async def validate_name_references(self, client: Any) -> list[str]:
        """
        Validate name references exist in FortiGate.
        
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
            >>> policy = VdomPropertyModel(
            ...     name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.vdom_property.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.vdom.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Name '{value}' not found in "
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
        
        errors = await self.validate_name_references(client)
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
    "VdomPropertyModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.379704Z
# ============================================================================
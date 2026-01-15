"""
Pydantic Models for CMDB - router/multicast

Runtime validation models for router/multicast configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class MulticastPimSmGlobal(BaseModel):
    """
    Child table model for pim-sm-global.
    
    PIM sparse-mode global settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    message_interval: int | None = Field(ge=1, le=65535, default=60, description="Period of time between sending periodic PIM join/prune messages in seconds (1 - 65535, default = 60).")    
    join_prune_holdtime: int | None = Field(ge=1, le=65535, default=210, description="Join/prune holdtime (1 - 65535, default = 210).")    
    accept_register_list: str | None = Field(max_length=35, default="", description="Sources allowed to register packets with this Rendezvous Point (RP).")  # datasource: ['router.access-list.name']    
    accept_source_list: str | None = Field(max_length=35, default="", description="Sources allowed to send multicast traffic.")  # datasource: ['router.access-list.name']    
    bsr_candidate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowing this router to become a bootstrap router (BSR).")    
    bsr_interface: str | None = Field(max_length=15, default="", description="Interface to advertise as candidate BSR.")  # datasource: ['system.interface.name']    
    bsr_priority: int | None = Field(ge=0, le=255, default=0, description="BSR priority (0 - 255, default = 0).")    
    bsr_hash: int | None = Field(ge=0, le=32, default=10, description="BSR hash length (0 - 32, default = 10).")    
    bsr_allow_quick_refresh: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable accept BSR quick refresh packets from neighbors.")    
    cisco_crp_prefix: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable making candidate RP compatible with old Cisco IOS.")    
    cisco_register_checksum: Literal["enable", "disable"] | None = Field(default="disable", description="Checksum entire register packet(for old Cisco IOS compatibility).")    
    cisco_register_checksum_group: str | None = Field(max_length=35, default="", description="Cisco register checksum only these groups.")  # datasource: ['router.access-list.name']    
    cisco_ignore_rp_set_priority: Literal["enable", "disable"] | None = Field(default="disable", description="Use only hash for RP selection (compatibility with old Cisco IOS).")    
    register_rp_reachability: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable check RP is reachable before registering packets.")    
    register_source: Literal["disable", "interface", "ip-address"] | None = Field(default="disable", description="Override source address in register packets.")    
    register_source_interface: str | None = Field(max_length=15, default="", description="Override with primary interface address.")  # datasource: ['system.interface.name']    
    register_source_ip: str | None = Field(default="0.0.0.0", description="Override with local IP address.")    
    register_supression: int | None = Field(ge=1, le=65535, default=60, description="Period of time to honor register-stop message (1 - 65535 sec, default = 60).")    
    null_register_retries: int | None = Field(ge=1, le=20, default=1, description="Maximum retries of null register (1 - 20, default = 1).")    
    rp_register_keepalive: int | None = Field(ge=1, le=65535, default=185, description="Timeout for RP receiving data on (S,G) tree (1 - 65535 sec, default = 185).")    
    spt_threshold: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable switching to source specific trees.")    
    spt_threshold_group: str | None = Field(max_length=35, default="", description="Groups allowed to switch to source tree.")  # datasource: ['router.access-list.name']    
    ssm: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable source specific multicast.")    
    ssm_range: str | None = Field(max_length=35, default="", description="Groups allowed to source specific multicast.")  # datasource: ['router.access-list.name']    
    register_rate_limit: int | None = Field(ge=0, le=65535, default=0, description="Limit of packets/sec per source registered through this RP (0 - 65535, default = 0 which means unlimited).")    
    pim_use_sdwan: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of SDWAN when checking RPF neighbor and sending of REG packet.")    
    rp_address: list[RpAddress] = Field(default=None, description="Statically configure RP addresses.")
class MulticastPimSmGlobalVrf(BaseModel):
    """
    Child table model for pim-sm-global-vrf.
    
    per-VRF PIM sparse-mode global settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    vrf: int | None = Field(ge=1, le=511, default=0, description="VRF ID.")    
    bsr_candidate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowing this router to become a bootstrap router (BSR).")    
    bsr_interface: str | None = Field(max_length=15, default="", description="Interface to advertise as candidate BSR.")  # datasource: ['system.interface.name']    
    bsr_priority: int | None = Field(ge=0, le=255, default=0, description="BSR priority (0 - 255, default = 0).")    
    bsr_hash: int | None = Field(ge=0, le=32, default=10, description="BSR hash length (0 - 32, default = 10).")    
    bsr_allow_quick_refresh: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable accept BSR quick refresh packets from neighbors.")    
    cisco_crp_prefix: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable making candidate RP compatible with old Cisco IOS.")    
    rp_address: list[RpAddress] = Field(default=None, description="Statically configure RP addresses.")
class MulticastInterface(BaseModel):
    """
    Child table model for interface.
    
    PIM interfaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=15, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    ttl_threshold: int | None = Field(ge=1, le=255, default=1, description="Minimum TTL of multicast packets that will be forwarded (applied only to new multicast routes) (1 - 255, default = 1).")    
    pim_mode: Literal["sparse-mode", "dense-mode"] | None = Field(default="sparse-mode", description="PIM operation mode.")    
    passive: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable listening to IGMP but not participating in PIM.")    
    bfd: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Protocol Independent Multicast (PIM) Bidirectional Forwarding Detection (BFD).")    
    neighbour_filter: str | None = Field(max_length=35, default="", description="Routers acknowledged as neighbor routers.")  # datasource: ['router.access-list.name']    
    hello_interval: int | None = Field(ge=1, le=65535, default=30, description="Interval between sending PIM hello messages (0 - 65535 sec, default = 30).")    
    hello_holdtime: int | None = Field(ge=1, le=65535, default=105, description="Time before old neighbor information expires (0 - 65535 sec, default = 105).")    
    cisco_exclude_genid: Literal["enable", "disable"] | None = Field(default="disable", description="Exclude GenID from hello packets (compatibility with old Cisco IOS).")    
    dr_priority: int | None = Field(ge=1, le=4294967295, default=1, description="DR election priority.")    
    propagation_delay: int | None = Field(ge=100, le=5000, default=500, description="Delay flooding packets on this interface (100 - 5000 msec, default = 500).")    
    state_refresh_interval: int | None = Field(ge=1, le=100, default=60, description="Interval between sending state-refresh packets (1 - 100 sec, default = 60).")    
    rp_candidate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable compete to become RP in elections.")    
    rp_candidate_group: str | None = Field(max_length=35, default="", description="Multicast groups managed by this RP.")  # datasource: ['router.access-list.name']    
    rp_candidate_priority: int | None = Field(ge=0, le=255, default=192, description="Router's priority as RP.")    
    rp_candidate_interval: int | None = Field(ge=1, le=16383, default=60, description="RP candidate advertisement interval (1 - 16383 sec, default = 60).")    
    multicast_flow: str | None = Field(max_length=35, default="", description="Acceptable source for multicast group.")  # datasource: ['router.multicast-flow.name']    
    static_group: str | None = Field(max_length=35, default="", description="Statically set multicast groups to forward out.")  # datasource: ['router.multicast-flow.name']    
    rpf_nbr_fail_back: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fail back for RPF neighbor query.")    
    rpf_nbr_fail_back_filter: str | None = Field(max_length=35, default="", description="Filter for fail back RPF neighbors.")  # datasource: ['router.access-list.name']    
    join_group: list[JoinGroup] = Field(default=None, description="Join multicast groups.")    
    igmp: list[Igmp] = Field(default=None, description="IGMP configuration options.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class MulticastModel(BaseModel):
    """
    Pydantic model for router/multicast configuration.
    
    Configure router multicast.
    
    Validation Rules:        - route_threshold: min=1 max=2147483647 pattern=        - route_limit: min=1 max=2147483647 pattern=        - multicast_routing: pattern=        - pim_sm_global: pattern=        - pim_sm_global_vrf: pattern=        - interface: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    route_threshold: int | None = Field(ge=1, le=2147483647, default="", description="Generate warnings when the number of multicast routes exceeds this number, must not be greater than route-limit.")    
    route_limit: int | None = Field(ge=1, le=2147483647, default=2147483647, description="Maximum number of multicast routes.")    
    multicast_routing: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IP multicast routing.")    
    pim_sm_global: list[PimSmGlobal] = Field(default=None, description="PIM sparse-mode global settings.")    
    pim_sm_global_vrf: list[PimSmGlobalVrf] = Field(default=None, description="per-VRF PIM sparse-mode global settings.")    
    interface: list[Interface] = Field(default=None, description="PIM interfaces.")    
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
    async def validate_pim_sm_global_references(self, client: Any) -> list[str]:
        """
        Validate pim_sm_global references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/access-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastModel(
            ...     pim_sm_global=[{"ssm-range": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_pim_sm_global_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.multicast.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "pim_sm_global", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("ssm-range")
            else:
                value = getattr(item, "ssm-range", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.access-list.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Pim-Sm-Global '{value}' not found in "
                    "router/access-list"
                )        
        return errors    
    async def validate_pim_sm_global_vrf_references(self, client: Any) -> list[str]:
        """
        Validate pim_sm_global_vrf references exist in FortiGate.
        
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
            >>> policy = MulticastModel(
            ...     pim_sm_global_vrf=[{"bsr-interface": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_pim_sm_global_vrf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.multicast.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "pim_sm_global_vrf", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("bsr-interface")
            else:
                value = getattr(item, "bsr-interface", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Pim-Sm-Global-Vrf '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_interface_references(self, client: Any) -> list[str]:
        """
        Validate interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/access-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = MulticastModel(
            ...     interface=[{"rpf-nbr-fail-back-filter": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.multicast.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "interface", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("rpf-nbr-fail-back-filter")
            else:
                value = getattr(item, "rpf-nbr-fail-back-filter", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.access-list.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Interface '{value}' not found in "
                    "router/access-list"
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
        
        errors = await self.validate_pim_sm_global_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_pim_sm_global_vrf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_interface_references(client)
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
    "MulticastModel",    "MulticastPimSmGlobal",    "MulticastPimSmGlobalVrf",    "MulticastInterface",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.264944Z
# ============================================================================
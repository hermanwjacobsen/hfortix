"""
Pydantic Models for CMDB - system/snmp/user

Runtime validation models for system/snmp/user configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class UserVdoms(BaseModel):
    """
    Child table model for vdoms.
    
    SNMP access control VDOMs.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="VDOM name.")  # datasource: ['system.vdom.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class UserEventsEnum(str, Enum):
    """Allowed values for events field."""
    CPU_HIGH = "cpu-high"    MEM_LOW = "mem-low"    LOG_FULL = "log-full"    INTF_IP = "intf-ip"    VPN_TUN_UP = "vpn-tun-up"    VPN_TUN_DOWN = "vpn-tun-down"    HA_SWITCH = "ha-switch"    HA_HB_FAILURE = "ha-hb-failure"    IPS_SIGNATURE = "ips-signature"    IPS_ANOMALY = "ips-anomaly"    AV_VIRUS = "av-virus"    AV_OVERSIZE = "av-oversize"    AV_PATTERN = "av-pattern"    AV_FRAGMENTED = "av-fragmented"    FM_IF_CHANGE = "fm-if-change"    FM_CONF_CHANGE = "fm-conf-change"    BGP_ESTABLISHED = "bgp-established"    BGP_BACKWARD_TRANSITION = "bgp-backward-transition"    HA_MEMBER_UP = "ha-member-up"    HA_MEMBER_DOWN = "ha-member-down"    ENT_CONF_CHANGE = "ent-conf-change"    AV_CONSERVE = "av-conserve"    AV_BYPASS = "av-bypass"    AV_OVERSIZE_PASSED = "av-oversize-passed"    AV_OVERSIZE_BLOCKED = "av-oversize-blocked"    IPS_PKG_UPDATE = "ips-pkg-update"    IPS_FAIL_OPEN = "ips-fail-open"    FAZ_DISCONNECT = "faz-disconnect"    FAZ = "faz"    WC_AP_UP = "wc-ap-up"    WC_AP_DOWN = "wc-ap-down"    FSWCTL_SESSION_UP = "fswctl-session-up"    FSWCTL_SESSION_DOWN = "fswctl-session-down"    LOAD_BALANCE_REAL_SERVER_DOWN = "load-balance-real-server-down"    DEVICE_NEW = "device-new"    PER_CPU_HIGH = "per-cpu-high"    DHCP = "dhcp"    POOL_USAGE = "pool-usage"    IPPOOL = "ippool"    INTERFACE = "interface"    OSPF_NBR_STATE_CHANGE = "ospf-nbr-state-change"    OSPF_VIRTNBR_STATE_CHANGE = "ospf-virtnbr-state-change"    BFD = "bfd"
class UserAuth_protoEnum(str, Enum):
    """Allowed values for auth_proto field."""
    MD5 = "md5"    SHA = "sha"    SHA224 = "sha224"    SHA256 = "sha256"    SHA384 = "sha384"    SHA512 = "sha512"
class UserPriv_protoEnum(str, Enum):
    """Allowed values for priv_proto field."""
    AES = "aes"    DES = "des"    AES256 = "aes256"    AES256CISCO = "aes256cisco"

# ============================================================================
# Main Model
# ============================================================================

class UserModel(BaseModel):
    """
    Pydantic model for system/snmp/user configuration.
    
    SNMP user configuration.
    
    Validation Rules:        - name: max_length=32 pattern=        - status: pattern=        - trap_status: pattern=        - trap_lport: min=1 max=65535 pattern=        - trap_rport: min=1 max=65535 pattern=        - queries: pattern=        - query_port: min=1 max=65535 pattern=        - notify_hosts: pattern=        - notify_hosts6: pattern=        - source_ip: pattern=        - source_ipv6: pattern=        - ha_direct: pattern=        - events: pattern=        - mib_view: max_length=32 pattern=        - vdoms: pattern=        - security_level: pattern=        - auth_proto: pattern=        - auth_pwd: max_length=128 pattern=        - priv_proto: pattern=        - priv_pwd: max_length=128 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=32, default="", description="SNMP user name.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this SNMP user.")    
    trap_status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable traps for this SNMP user.")    
    trap_lport: int | None = Field(ge=1, le=65535, default=162, description="SNMPv3 local trap port (default = 162).")    
    trap_rport: int | None = Field(ge=1, le=65535, default=162, description="SNMPv3 trap remote port (default = 162).")    
    queries: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable SNMP queries for this user.")    
    query_port: int | None = Field(ge=1, le=65535, default=161, description="SNMPv3 query port (default = 161).")    
    notify_hosts: list[NotifyHosts] = Field(default="", description="SNMP managers to send notifications (traps) to.")    
    notify_hosts6: list[NotifyHosts6] = Field(default="", description="IPv6 SNMP managers to send notifications (traps) to.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP for SNMP trap.")    
    source_ipv6: str | None = Field(default="::", description="Source IPv6 for SNMP trap.")    
    ha_direct: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable direct management of HA cluster members.")    
    events: list[Events] = Field(default="cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open faz-disconnect faz wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down load-balance-real-server-down per-cpu-high dhcp pool-usage ippool interface ospf-nbr-state-change ospf-virtnbr-state-change bfd", description="SNMP notifications (traps) to send.")    
    mib_view: str | None = Field(max_length=32, default="", description="SNMP access control MIB view.")  # datasource: ['system.snmp.mib-view.name']    
    vdoms: list[Vdoms] = Field(default=None, description="SNMP access control VDOMs.")    
    security_level: Literal["no-auth-no-priv", "auth-no-priv", "auth-priv"] | None = Field(default="no-auth-no-priv", description="Security level for message authentication and encryption.")    
    auth_proto: AuthProtoEnum | None = Field(default="sha", description="Authentication protocol.")    
    auth_pwd: Any = Field(max_length=128, description="Password for authentication protocol.")    
    priv_proto: PrivProtoEnum | None = Field(default="aes", description="Privacy (encryption) protocol.")    
    priv_pwd: Any = Field(max_length=128, description="Password for privacy (encryption) protocol.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('mib_view')
    @classmethod
    def validate_mib_view(cls, v: Any) -> Any:
        """
        Validate mib_view field.
        
        Datasource: ['system.snmp.mib-view.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
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
    async def validate_mib_view_references(self, client: Any) -> list[str]:
        """
        Validate mib_view references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/snmp/mib-view        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = UserModel(
            ...     mib_view="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_mib_view_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.snmp.user.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "mib_view", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.snmp.mib-view.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Mib-View '{value}' not found in "
                "system/snmp/mib-view"
            )        
        return errors    
    async def validate_vdoms_references(self, client: Any) -> list[str]:
        """
        Validate vdoms references exist in FortiGate.
        
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
            >>> policy = UserModel(
            ...     vdoms=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdoms_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.snmp.user.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "vdoms", [])
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
                    f"Vdoms '{value}' not found in "
                    "system/vdom"
                )        
        return errors    
    async def validate_interface_references(self, client: Any) -> list[str]:
        """
        Validate interface references exist in FortiGate.
        
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
            >>> policy = UserModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.snmp.user.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Interface '{value}' not found in "
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
        
        errors = await self.validate_mib_view_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_vdoms_references(client)
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
    "UserModel",    "UserVdoms",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.390956Z
# ============================================================================
"""
Pydantic Models for CMDB - system/fortiguard

Runtime validation models for system/fortiguard configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class FortiguardPortEnum(str, Enum):
    """Allowed values for port field."""
    8888 = "8888"    53 = "53"    80 = "80"    443 = "443"
class FortiguardAuto_firmware_upgrade_dayEnum(str, Enum):
    """Allowed values for auto_firmware_upgrade_day field."""
    SUNDAY = "sunday"    MONDAY = "monday"    TUESDAY = "tuesday"    WEDNESDAY = "wednesday"    THURSDAY = "thursday"    FRIDAY = "friday"    SATURDAY = "saturday"

# ============================================================================
# Main Model
# ============================================================================

class FortiguardModel(BaseModel):
    """
    Pydantic model for system/fortiguard configuration.
    
    Configure FortiGuard services.
    
    Validation Rules:        - fortiguard_anycast: pattern=        - fortiguard_anycast_source: pattern=        - protocol: pattern=        - port: pattern=        - load_balance_servers: min=1 max=266 pattern=        - auto_join_forticloud: pattern=        - update_server_location: pattern=        - sandbox_region: max_length=63 pattern=        - sandbox_inline_scan: pattern=        - update_ffdb: pattern=        - update_uwdb: pattern=        - update_dldb: pattern=        - update_extdb: pattern=        - update_build_proxy: pattern=        - persistent_connection: pattern=        - vdom: max_length=31 pattern=        - auto_firmware_upgrade: pattern=        - auto_firmware_upgrade_day: pattern=        - auto_firmware_upgrade_delay: min=0 max=14 pattern=        - auto_firmware_upgrade_start_hour: min=0 max=23 pattern=        - auto_firmware_upgrade_end_hour: min=0 max=23 pattern=        - FDS_license_expiring_days: min=1 max=100 pattern=        - subscribe_update_notification: pattern=        - antispam_force_off: pattern=        - antispam_cache: pattern=        - antispam_cache_ttl: min=300 max=86400 pattern=        - antispam_cache_mpermille: min=1 max=150 pattern=        - antispam_license: min=0 max=4294967295 pattern=        - antispam_expiration: min=0 max=4294967295 pattern=        - antispam_timeout: min=1 max=30 pattern=        - outbreak_prevention_force_off: pattern=        - outbreak_prevention_cache: pattern=        - outbreak_prevention_cache_ttl: min=300 max=86400 pattern=        - outbreak_prevention_cache_mpermille: min=1 max=150 pattern=        - outbreak_prevention_license: min=0 max=4294967295 pattern=        - outbreak_prevention_expiration: min=0 max=4294967295 pattern=        - outbreak_prevention_timeout: min=1 max=30 pattern=        - webfilter_force_off: pattern=        - webfilter_cache: pattern=        - webfilter_cache_ttl: min=300 max=86400 pattern=        - webfilter_license: min=0 max=4294967295 pattern=        - webfilter_expiration: min=0 max=4294967295 pattern=        - webfilter_timeout: min=1 max=30 pattern=        - sdns_server_ip: pattern=        - sdns_server_port: min=1 max=65535 pattern=        - anycast_sdns_server_ip: pattern=        - anycast_sdns_server_port: min=1 max=65535 pattern=        - sdns_options: pattern=        - source_ip: pattern=        - source_ip6: pattern=        - proxy_server_ip: max_length=63 pattern=        - proxy_server_port: min=0 max=65535 pattern=        - proxy_username: max_length=64 pattern=        - proxy_password: max_length=128 pattern=        - ddns_server_ip: pattern=        - ddns_server_ip6: pattern=        - ddns_server_port: min=1 max=65535 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    fortiguard_anycast: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of FortiGuard's Anycast network.")    
    fortiguard_anycast_source: Literal["fortinet", "aws", "debug"] | None = Field(default="fortinet", description="Configure which of Fortinet's servers to provide FortiGuard services in FortiGuard's anycast network. Default is Fortinet.")    
    protocol: Literal["udp", "http", "https"] | None = Field(default="https", description="Protocol used to communicate with the FortiGuard servers.")    
    port: PortEnum | None = Field(default="443", description="Port used to communicate with the FortiGuard servers.")    
    load_balance_servers: int | None = Field(ge=1, le=266, default=1, description="Number of servers to alternate between as first FortiGuard option.")    
    auto_join_forticloud: Literal["enable", "disable"] | None = Field(default="enable", description="Automatically connect to and login to FortiCloud.")    
    update_server_location: Literal["automatic", "usa", "eu"] | None = Field(default="automatic", description="Location from which to receive FortiGuard updates.")    
    sandbox_region: str | None = Field(max_length=63, default="", description="FortiCloud Sandbox region.")    
    sandbox_inline_scan: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FortiCloud Sandbox inline-scan.")    
    update_ffdb: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Internet Service Database update.")    
    update_uwdb: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable allowlist update.")    
    update_dldb: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable DLP signature update.")    
    update_extdb: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable external resource update.")    
    update_build_proxy: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable proxy dictionary rebuild.")    
    persistent_connection: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable use of persistent connection to receive update notification from FortiGuard.")    
    vdom: str | None = Field(max_length=31, default="", description="FortiGuard Service virtual domain name.")  # datasource: ['system.vdom.name']    
    auto_firmware_upgrade: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable automatic patch-level firmware upgrade from FortiGuard. The FortiGate unit searches for new patches only in the same major and minor version.")    
    auto_firmware_upgrade_day: list[AutoFirmwareUpgradeDay] = Field(default="", description="Allowed day(s) of the week to install an automatic patch-level firmware upgrade from FortiGuard (default is none). Disallow any day of the week to use auto-firmware-upgrade-delay instead, which waits for designated days before installing an automatic patch-level firmware upgrade.")    
    auto_firmware_upgrade_delay: int | None = Field(ge=0, le=14, default=3, description="Delay of day(s) before installing an automatic patch-level firmware upgrade from FortiGuard (default = 3). Set it 0 to use auto-firmware-upgrade-day instead, which selects allowed day(s) of the week for installing an automatic patch-level firmware upgrade.")    
    auto_firmware_upgrade_start_hour: int | None = Field(ge=0, le=23, default=1, description="Start time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time (0 ~ 23, default = 2). The actual upgrade time is selected randomly within the time window.")    
    auto_firmware_upgrade_end_hour: int | None = Field(ge=0, le=23, default=4, description="End time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time (0 ~ 23, default = 4). When the end time is smaller than the start time, the end time is interpreted as the next day. The actual upgrade time is selected randomly within the time window.")    
    FDS_license_expiring_days: int | None = Field(ge=1, le=100, default=15, description="Threshold for number of days before FortiGuard license expiration to generate license expiring event log (1 - 100 days, default = 15).")    
    subscribe_update_notification: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable subscription to receive update notification from FortiGuard.")    
    antispam_force_off: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable turning off the FortiGuard antispam service.")    
    antispam_cache: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiGuard antispam request caching. Uses a small amount of memory but improves performance.")    
    antispam_cache_ttl: int | None = Field(ge=300, le=86400, default=1800, description="Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times reduce the cache size. Higher times may improve performance since the cache will have more entries.")    
    antispam_cache_mpermille: int | None = Field(ge=1, le=150, default=1, description="Maximum permille of FortiGate memory the antispam cache is allowed to use (1 - 150).")    
    antispam_license: int | None = Field(ge=0, le=4294967295, default=4294967295, description="Interval of time between license checks for the FortiGuard antispam contract.")    
    antispam_expiration: int | None = Field(ge=0, le=4294967295, default=0, description="Expiration date of the FortiGuard antispam contract.")    
    antispam_timeout: int = Field(ge=1, le=30, default=7, description="Antispam query time out (1 - 30 sec, default = 7).")    
    outbreak_prevention_force_off: Literal["enable", "disable"] | None = Field(default="disable", description="Turn off FortiGuard Virus Outbreak Prevention service.")    
    outbreak_prevention_cache: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiGuard Virus Outbreak Prevention cache.")    
    outbreak_prevention_cache_ttl: int | None = Field(ge=300, le=86400, default=300, description="Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300).")    
    outbreak_prevention_cache_mpermille: int | None = Field(ge=1, le=150, default=1, description="Maximum permille of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 150 permille, default = 1).")    
    outbreak_prevention_license: int | None = Field(ge=0, le=4294967295, default=4294967295, description="Interval of time between license checks for FortiGuard Virus Outbreak Prevention contract.")    
    outbreak_prevention_expiration: int | None = Field(ge=0, le=4294967295, default=0, description="Expiration date of FortiGuard Virus Outbreak Prevention contract.")    
    outbreak_prevention_timeout: int = Field(ge=1, le=30, default=7, description="FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7).")    
    webfilter_force_off: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable turning off the FortiGuard web filtering service.")    
    webfilter_cache: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FortiGuard web filter caching.")    
    webfilter_cache_ttl: int | None = Field(ge=300, le=86400, default=3600, description="Time-to-live for web filter cache entries in seconds (300 - 86400).")    
    webfilter_license: int | None = Field(ge=0, le=4294967295, default=4294967295, description="Interval of time between license checks for the FortiGuard web filter contract.")    
    webfilter_expiration: int | None = Field(ge=0, le=4294967295, default=0, description="Expiration date of the FortiGuard web filter contract.")    
    webfilter_timeout: int = Field(ge=1, le=30, default=15, description="Web filter query time out (1 - 30 sec, default = 15).")    
    sdns_server_ip: list[SdnsServerIp] = Field(default="", description="IP address of the FortiGuard DNS rating server.")    
    sdns_server_port: int | None = Field(ge=1, le=65535, default=53, description="Port to connect to on the FortiGuard DNS rating server.")    
    anycast_sdns_server_ip: str | None = Field(default="0.0.0.0", description="IP address of the FortiGuard anycast DNS rating server.")    
    anycast_sdns_server_port: int | None = Field(ge=1, le=65535, default=853, description="Port to connect to on the FortiGuard anycast DNS rating server.")    
    sdns_options: list[SdnsOptions] = Field(default="", description="Customization options for the FortiGuard DNS service.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IPv4 address used to communicate with FortiGuard.")    
    source_ip6: str | None = Field(default="::", description="Source IPv6 address used to communicate with FortiGuard.")    
    proxy_server_ip: str | None = Field(max_length=63, default="", description="Hostname or IPv4 address of the proxy server.")    
    proxy_server_port: int | None = Field(ge=0, le=65535, default=0, description="Port used to communicate with the proxy server.")    
    proxy_username: str | None = Field(max_length=64, default="", description="Proxy user name.")    
    proxy_password: Any = Field(max_length=128, default=None, description="Proxy user password.")    
    ddns_server_ip: str | None = Field(default="0.0.0.0", description="IP address of the FortiDDNS server.")    
    ddns_server_ip6: str | None = Field(default="::", description="IPv6 address of the FortiDDNS server.")    
    ddns_server_port: int | None = Field(ge=1, le=65535, default=443, description="Port used to communicate with FortiDDNS servers.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('vdom')
    @classmethod
    def validate_vdom(cls, v: Any) -> Any:
        """
        Validate vdom field.
        
        Datasource: ['system.vdom.name']
        
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
            >>> policy = FortiguardModel(
            ...     vdom="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fortiguard.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "vdom", None)
        if not value:
            return errors
        
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
            >>> policy = FortiguardModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.fortiguard.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_vdom_references(client)
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
    "FortiguardModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.345672Z
# ============================================================================
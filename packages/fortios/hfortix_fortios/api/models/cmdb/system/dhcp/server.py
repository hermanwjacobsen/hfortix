"""
Pydantic Models for CMDB - system/dhcp/server

Runtime validation models for system/dhcp/server configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ServerIpRange(BaseModel):
    """
    Child table model for ip-range.
    
    DHCP IP range configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    start_ip: str = Field(default="0.0.0.0", description="Start of IP range.")    
    end_ip: str = Field(default="0.0.0.0", description="End of IP range.")    
    vci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this range.")    
    vci_string: list[VciString] = Field(default=None, description="One or more VCI strings in quotes separated by spaces.")    
    uci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this range.")    
    uci_string: list[UciString] = Field(default=None, description="One or more UCI strings in quotes separated by spaces.")    
    lease_time: int | None = Field(ge=300, le=8640000, default=0, description="Lease time in seconds, 0 means default lease time.")
class ServerTftpServer(BaseModel):
    """
    Child table model for tftp-server.
    
    One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    tftp_server: str = Field(max_length=63, default="", description="TFTP server.")
class ServerOptions(BaseModel):
    """
    Child table model for options.
    
    DHCP options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    code: int = Field(ge=0, le=255, default=0, description="DHCP option code.")    
    type: TypeEnum | None = Field(default="hex", description="DHCP option type.")    
    value: str | None = Field(max_length=312, default="", description="DHCP option value.")    
    ip: list[Ip] = Field(default="", description="DHCP option IPs.")    
    vci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this option.")    
    vci_string: list[VciString] = Field(default=None, description="One or more VCI strings in quotes separated by spaces.")    
    uci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this option.")    
    uci_string: list[UciString] = Field(default=None, description="One or more UCI strings in quotes separated by spaces.")
class ServerVciString(BaseModel):
    """
    Child table model for vci-string.
    
    One or more VCI strings in quotes separated by spaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    vci_string: str = Field(max_length=255, default="", description="VCI strings.")
class ServerExcludeRange(BaseModel):
    """
    Child table model for exclude-range.
    
    Exclude one or more ranges of IP addresses from being assigned to clients.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    start_ip: str = Field(default="0.0.0.0", description="Start of IP range.")    
    end_ip: str = Field(default="0.0.0.0", description="End of IP range.")    
    vci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served with this range.")    
    vci_string: list[VciString] = Field(default=None, description="One or more VCI strings in quotes separated by spaces.")    
    uci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable user class identifier (UCI) matching. When enabled only DHCP requests with a matching UCI are served with this range.")    
    uci_string: list[UciString] = Field(default=None, description="One or more UCI strings in quotes separated by spaces.")    
    lease_time: int | None = Field(ge=300, le=8640000, default=0, description="Lease time in seconds, 0 means default lease time.")
class ServerReservedAddress(BaseModel):
    """
    Child table model for reserved-address.
    
    Options for the DHCP server to assign IP settings to specific MAC addresses.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    type: Literal["mac", "option82"] | None = Field(default="mac", description="DHCP reserved-address type.")    
    ip: str = Field(default="0.0.0.0", description="IP address to be reserved for the MAC address.")    
    mac: str = Field(default="00:00:00:00:00:00", description="MAC address of the client that will get the reserved IP address.")    
    action: Literal["assign", "block", "reserved"] | None = Field(default="reserved", description="Options for the DHCP server to configure the client with the reserved MAC address.")    
    circuit_id_type: Literal["hex", "string"] | None = Field(default="string", description="DHCP option type.")    
    circuit_id: str | None = Field(max_length=312, default="", description="Option 82 circuit-ID of the client that will get the reserved IP address.")    
    remote_id_type: Literal["hex", "string"] | None = Field(default="string", description="DHCP option type.")    
    remote_id: str | None = Field(max_length=312, default="", description="Option 82 remote-ID of the client that will get the reserved IP address.")    
    description: str | None = Field(max_length=255, default=None, description="Description.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ServerModel(BaseModel):
    """
    Pydantic model for system/dhcp/server configuration.
    
    Configure DHCP servers.
    
    Validation Rules:        - id: min=0 max=4294967295 pattern=        - status: pattern=        - lease_time: min=300 max=8640000 pattern=        - mac_acl_default_action: pattern=        - forticlient_on_net_status: pattern=        - dns_service: pattern=        - dns_server1: pattern=        - dns_server2: pattern=        - dns_server3: pattern=        - dns_server4: pattern=        - wifi_ac_service: pattern=        - wifi_ac1: pattern=        - wifi_ac2: pattern=        - wifi_ac3: pattern=        - ntp_service: pattern=        - ntp_server1: pattern=        - ntp_server2: pattern=        - ntp_server3: pattern=        - domain: max_length=35 pattern=        - wins_server1: pattern=        - wins_server2: pattern=        - default_gateway: pattern=        - next_server: pattern=        - netmask: pattern=        - interface: max_length=15 pattern=        - ip_range: pattern=        - timezone_option: pattern=        - timezone: max_length=63 pattern=        - tftp_server: pattern=        - filename: max_length=127 pattern=        - options: pattern=        - server_type: pattern=        - ip_mode: pattern=        - conflicted_ip_timeout: min=60 max=8640000 pattern=        - ipsec_lease_hold: min=0 max=8640000 pattern=        - auto_configuration: pattern=        - dhcp_settings_from_fortiipam: pattern=        - auto_managed_status: pattern=        - ddns_update: pattern=        - ddns_update_override: pattern=        - ddns_server_ip: pattern=        - ddns_zone: max_length=64 pattern=        - ddns_auth: pattern=        - ddns_keyname: max_length=64 pattern=        - ddns_key: pattern=        - ddns_ttl: min=60 max=86400 pattern=        - vci_match: pattern=        - vci_string: pattern=        - exclude_range: pattern=        - shared_subnet: pattern=        - relay_agent: pattern=        - reserved_address: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    id: int = Field(ge=0, le=4294967295, default=0, description="ID.")    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable this DHCP configuration.")    
    lease_time: int | None = Field(ge=300, le=8640000, default=604800, description="Lease time in seconds, 0 means unlimited.")    
    mac_acl_default_action: Literal["assign", "block"] | None = Field(default="assign", description="MAC access control default action (allow or block assigning IP settings).")    
    forticlient_on_net_status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable FortiClient-On-Net service for this DHCP server.")    
    dns_service: Literal["local", "default", "specify"] | None = Field(default="specify", description="Options for assigning DNS servers to DHCP clients.")    
    dns_server1: str | None = Field(default="0.0.0.0", description="DNS server 1.")    
    dns_server2: str | None = Field(default="0.0.0.0", description="DNS server 2.")    
    dns_server3: str | None = Field(default="0.0.0.0", description="DNS server 3.")    
    dns_server4: str | None = Field(default="0.0.0.0", description="DNS server 4.")    
    wifi_ac_service: Literal["specify", "local"] | None = Field(default="specify", description="Options for assigning WiFi access controllers to DHCP clients.")    
    wifi_ac1: str | None = Field(default="0.0.0.0", description="WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).")    
    wifi_ac2: str | None = Field(default="0.0.0.0", description="WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).")    
    wifi_ac3: str | None = Field(default="0.0.0.0", description="WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).")    
    ntp_service: Literal["local", "default", "specify"] | None = Field(default="specify", description="Options for assigning Network Time Protocol (NTP) servers to DHCP clients.")    
    ntp_server1: str | None = Field(default="0.0.0.0", description="NTP server 1.")    
    ntp_server2: str | None = Field(default="0.0.0.0", description="NTP server 2.")    
    ntp_server3: str | None = Field(default="0.0.0.0", description="NTP server 3.")    
    domain: str | None = Field(max_length=35, default="", description="Domain name suffix for the IP addresses that the DHCP server assigns to clients.")    
    wins_server1: str | None = Field(default="0.0.0.0", description="WINS server 1.")    
    wins_server2: str | None = Field(default="0.0.0.0", description="WINS server 2.")    
    default_gateway: str | None = Field(default="0.0.0.0", description="Default gateway IP address assigned by the DHCP server.")    
    next_server: str | None = Field(default="0.0.0.0", description="IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.")    
    netmask: str = Field(default="0.0.0.0", description="Netmask assigned by the DHCP server.")    
    interface: str = Field(max_length=15, default="", description="DHCP server can assign IP configurations to clients connected to this interface.")  # datasource: ['system.interface.name']    
    ip_range: list[IpRange] = Field(default=None, description="DHCP IP range configuration.")    
    timezone_option: Literal["disable", "default", "specify"] | None = Field(default="disable", description="Options for the DHCP server to set the client's time zone.")    
    timezone: str = Field(max_length=63, default="", description="Select the time zone to be assigned to DHCP clients.")  # datasource: ['system.timezone.name']    
    tftp_server: list[TftpServer] = Field(default=None, description="One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces.")    
    filename: str | None = Field(max_length=127, default="", description="Name of the boot file on the TFTP server.")    
    options: list[Options] = Field(default=None, description="DHCP options.")    
    server_type: Literal["regular", "ipsec"] | None = Field(default="regular", description="DHCP server can be a normal DHCP server or an IPsec DHCP server.")    
    ip_mode: Literal["range", "usrgrp"] | None = Field(default="range", description="Method used to assign client IP.")    
    conflicted_ip_timeout: int | None = Field(ge=60, le=8640000, default=1800, description="Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.")    
    ipsec_lease_hold: int | None = Field(ge=0, le=8640000, default=60, description="DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).")    
    auto_configuration: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable auto configuration.")    
    dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable populating of DHCP server settings from FortiIPAM.")    
    auto_managed_status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.")    
    ddns_update: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable DDNS update for DHCP.")    
    ddns_update_override: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable DDNS update override for DHCP.")    
    ddns_server_ip: str | None = Field(default="0.0.0.0", description="DDNS server IP.")    
    ddns_zone: str | None = Field(max_length=64, default="", description="Zone of your domain name (ex. DDNS.com).")    
    ddns_auth: Literal["disable", "tsig"] | None = Field(default="disable", description="DDNS authentication mode.")    
    ddns_keyname: str | None = Field(max_length=64, default="", description="DDNS update key name.")    
    ddns_key: Any = Field(default=None, description="DDNS update key (base 64 encoding).")    
    ddns_ttl: int | None = Field(ge=60, le=86400, default=300, description="TTL.")    
    vci_match: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.")    
    vci_string: list[VciString] = Field(default=None, description="One or more VCI strings in quotes separated by spaces.")    
    exclude_range: list[ExcludeRange] = Field(default=None, description="Exclude one or more ranges of IP addresses from being assigned to clients.")    
    shared_subnet: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable shared subnet.")    
    relay_agent: str | None = Field(default="0.0.0.0", description="Relay agent IP.")    
    reserved_address: list[ReservedAddress] = Field(default=None, description="Options for the DHCP server to assign IP settings to specific MAC addresses.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
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
    @field_validator('timezone')
    @classmethod
    def validate_timezone(cls, v: Any) -> Any:
        """
        Validate timezone field.
        
        Datasource: ['system.timezone.name']
        
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
            >>> policy = ServerModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dhcp.server.post(policy.to_fortios_dict())
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
    async def validate_timezone_references(self, client: Any) -> list[str]:
        """
        Validate timezone references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/timezone        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ServerModel(
            ...     timezone="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_timezone_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.dhcp.server.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "timezone", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.timezone.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Timezone '{value}' not found in "
                "system/timezone"
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
        
        errors = await self.validate_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_timezone_references(client)
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
    "ServerModel",    "ServerIpRange",    "ServerTftpServer",    "ServerOptions",    "ServerVciString",    "ServerExcludeRange",    "ServerReservedAddress",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.216306Z
# ============================================================================
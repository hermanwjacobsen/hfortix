"""
Pydantic Models for CMDB - system/link_monitor

Runtime validation models for system/link_monitor configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class LinkMonitorServer(BaseModel):
    """
    Child table model for server.
    
    IP address of the server(s) to be monitored.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    address: str = Field(max_length=79, default="", description="Server address.")
class LinkMonitorRoute(BaseModel):
    """
    Child table model for route.
    
    Subnet to monitor.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    subnet: str | None = Field(max_length=79, default="", description="IP and netmask (x.x.x.x/y).")
class LinkMonitorServerList(BaseModel):
    """
    Child table model for server-list.
    
    Servers for link-monitor to monitor.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=32, default=0, description="Server ID.")    
    dst: str = Field(max_length=64, default="", description="IP address of the server to be monitored.")    
    protocol: list[Protocol] = Field(default="ping", description="Protocols used to monitor the server.")    
    port: int | None = Field(ge=1, le=65535, default=0, description="Port number of the traffic to be used to monitor the server.")    
    weight: int | None = Field(ge=0, le=255, default=0, description="Weight of the monitor to this dst (0 - 255).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class LinkMonitorProtocolEnum(str, Enum):
    """Allowed values for protocol field."""
    PING = "ping"    TCP_ECHO = "tcp-echo"    UDP_ECHO = "udp-echo"    HTTP = "http"    HTTPS = "https"    TWAMP = "twamp"

# ============================================================================
# Main Model
# ============================================================================

class LinkMonitorModel(BaseModel):
    """
    Pydantic model for system/link_monitor configuration.
    
    Configure Link Health Monitor.
    
    Validation Rules:        - name: max_length=35 pattern=        - addr_mode: pattern=        - srcintf: max_length=15 pattern=        - server_config: pattern=        - server_type: pattern=        - server: pattern=        - protocol: pattern=        - port: min=1 max=65535 pattern=        - gateway_ip: pattern=        - gateway_ip6: pattern=        - route: pattern=        - source_ip: pattern=        - source_ip6: pattern=        - http_get: max_length=1024 pattern=        - http_agent: max_length=1024 pattern=        - http_match: max_length=1024 pattern=        - interval: min=20 max=3600000 pattern=        - probe_timeout: min=20 max=5000 pattern=        - failtime: min=1 max=3600 pattern=        - recoverytime: min=1 max=3600 pattern=        - probe_count: min=5 max=30 pattern=        - security_mode: pattern=        - password: max_length=128 pattern=        - packet_size: min=0 max=65535 pattern=        - ha_priority: min=1 max=50 pattern=        - fail_weight: min=0 max=255 pattern=        - update_cascade_interface: pattern=        - update_static_route: pattern=        - update_policy_route: pattern=        - status: pattern=        - diffservcode: pattern=        - class_id: min=0 max=4294967295 pattern=        - service_detection: pattern=        - server_list: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Link monitor name.")    
    addr_mode: Literal["ipv4", "ipv6"] | None = Field(default="ipv4", description="Address mode (IPv4 or IPv6).")    
    srcintf: str | None = Field(max_length=15, default="", description="Interface that receives the traffic to be monitored.")  # datasource: ['system.interface.name']    
    server_config: Literal["default", "individual"] | None = Field(default="default", description="Mode of server configuration.")    
    server_type: Literal["static", "dynamic"] | None = Field(default="static", description="Server type (static or dynamic).")    
    server: list[Server] = Field(description="IP address of the server(s) to be monitored.")    
    protocol: list[Protocol] = Field(default="ping", description="Protocols used to monitor the server.")    
    port: int | None = Field(ge=1, le=65535, default=0, description="Port number of the traffic to be used to monitor the server.")    
    gateway_ip: str | None = Field(default="0.0.0.0", description="Gateway IP address used to probe the server.")    
    gateway_ip6: str | None = Field(default="::", description="Gateway IPv6 address used to probe the server.")    
    route: list[Route] = Field(default=None, description="Subnet to monitor.")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address used in packet to the server.")    
    source_ip6: str | None = Field(default="::", description="Source IPv6 address used in packet to the server.")    
    http_get: str = Field(max_length=1024, default="/", description="If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string.")    
    http_agent: str | None = Field(max_length=1024, default="Chrome/ Safari/", description="String in the http-agent field in the HTTP header.")    
    http_match: str | None = Field(max_length=1024, default="", description="String that you expect to see in the HTTP-GET requests of the traffic to be monitored.")    
    interval: int | None = Field(ge=20, le=3600000, default=500, description="Detection interval in milliseconds (20 - 3600 * 1000 msec, default = 500).")    
    probe_timeout: int | None = Field(ge=20, le=5000, default=500, description="Time to wait before a probe packet is considered lost (20 - 5000 msec, default = 500).")    
    failtime: int | None = Field(ge=1, le=3600, default=5, description="Number of retry attempts before the server is considered down (1 - 3600, default = 5).")    
    recoverytime: int | None = Field(ge=1, le=3600, default=5, description="Number of successful responses received before server is considered recovered (1 - 3600, default = 5).")    
    probe_count: int | None = Field(ge=5, le=30, default=30, description="Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).")    
    security_mode: Literal["none", "authentication"] | None = Field(default="none", description="Twamp controller security mode.")    
    password: Any = Field(max_length=128, default=None, description="TWAMP controller password in authentication mode.")    
    packet_size: int | None = Field(ge=0, le=65535, default=124, description="Packet size of a TWAMP test session (124/158 - 1024).")    
    ha_priority: int | None = Field(ge=1, le=50, default=1, description="HA election priority (1 - 50).")    
    fail_weight: int | None = Field(ge=0, le=255, default=0, description="Threshold weight to trigger link failure alert.")    
    update_cascade_interface: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable update cascade interface.")    
    update_static_route: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable updating the static route.")    
    update_policy_route: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable updating the policy route.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable this link monitor.")    
    diffservcode: str | None = Field(default="", description="Differentiated services code point (DSCP) in the IP header of the probe packet.")    
    class_id: int | None = Field(ge=0, le=4294967295, default=0, description="Traffic class ID.")  # datasource: ['firewall.traffic-class.class-id']    
    service_detection: Literal["enable", "disable"] | None = Field(default="disable", description="Only use monitor to read quality values. If enabled, static routes and cascade interfaces will not be updated.")    
    server_list: list[ServerList] = Field(default=None, description="Servers for link-monitor to monitor.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('srcintf')
    @classmethod
    def validate_srcintf(cls, v: Any) -> Any:
        """
        Validate srcintf field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('class_id')
    @classmethod
    def validate_class_id(cls, v: Any) -> Any:
        """
        Validate class_id field.
        
        Datasource: ['firewall.traffic-class.class-id']
        
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
    async def validate_srcintf_references(self, client: Any) -> list[str]:
        """
        Validate srcintf references exist in FortiGate.
        
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
            >>> policy = LinkMonitorModel(
            ...     srcintf="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_srcintf_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.link_monitor.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "srcintf", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Srcintf '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_class_id_references(self, client: Any) -> list[str]:
        """
        Validate class_id references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/traffic-class        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = LinkMonitorModel(
            ...     class_id="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_class_id_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.link_monitor.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "class_id", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.traffic-class.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Class-Id '{value}' not found in "
                "firewall/traffic-class"
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
        
        errors = await self.validate_srcintf_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_class_id_references(client)
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
    "LinkMonitorModel",    "LinkMonitorServer",    "LinkMonitorRoute",    "LinkMonitorServerList",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:44.396918Z
# ============================================================================
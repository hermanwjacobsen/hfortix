"""
Pydantic Models for CMDB - firewall/service/custom

Runtime validation models for firewall/service/custom configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum
from uuid import UUID

# ============================================================================
# Child Table Models
# ============================================================================

class CustomAppCategory(BaseModel):
    """
    Child table model for app-category.
    
    Application category ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Application category id.")
class CustomApplication(BaseModel):
    """
    Child table model for application.
    
    Application ID.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Application id.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class CustomProtocolEnum(str, Enum):
    """Allowed values for protocol field."""
    TCPUDPUDP_LITESCTP = "TCP/UDP/UDP-Lite/SCTP"    ICMP = "ICMP"    ICMP6 = "ICMP6"    IP = "IP"    HTTP = "HTTP"    FTP = "FTP"    CONNECT = "CONNECT"    SOCKS_TCP = "SOCKS-TCP"    SOCKS_UDP = "SOCKS-UDP"    ALL = "ALL"
class CustomHelperEnum(str, Enum):
    """Allowed values for helper field."""
    AUTO = "auto"    DISABLE = "disable"    FTP = "ftp"    TFTP = "tftp"    RAS = "ras"    H323 = "h323"    TNS = "tns"    MMS = "mms"    SIP = "sip"    PPTP = "pptp"    RTSP = "rtsp"    DNS_UDP = "dns-udp"    DNS_TCP = "dns-tcp"    PMAP = "pmap"    RSH = "rsh"    DCERPC = "dcerpc"    MGCP = "mgcp"

# ============================================================================
# Main Model
# ============================================================================

class CustomModel(BaseModel):
    """
    Pydantic model for firewall/service/custom configuration.
    
    Configure custom services.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: pattern=        - proxy: pattern=        - category: max_length=63 pattern=        - protocol: pattern=        - helper: pattern=        - iprange: pattern=        - fqdn: max_length=255 pattern=        - protocol_number: min=0 max=254 pattern=        - icmptype: min=0 max=4294967295 pattern=        - icmpcode: min=0 max=255 pattern=        - tcp_portrange: pattern=        - udp_portrange: pattern=        - udplite_portrange: pattern=        - sctp_portrange: pattern=        - tcp_halfclose_timer: min=0 max=86400 pattern=        - tcp_halfopen_timer: min=0 max=86400 pattern=        - tcp_timewait_timer: min=0 max=300 pattern=        - tcp_rst_timer: min=5 max=300 pattern=        - udp_idle_timer: min=0 max=86400 pattern=        - session_ttl: pattern=        - check_reset_range: pattern=        - comment: max_length=255 pattern=        - color: min=0 max=32 pattern=        - app_service_type: pattern=        - app_category: pattern=        - application: pattern=        - fabric_object: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Custom service name.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    proxy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web proxy service.")    
    category: str | None = Field(max_length=63, default="", description="Service category.")  # datasource: ['firewall.service.category.name']    
    protocol: ProtocolEnum | None = Field(default="TCP/UDP/UDP-Lite/SCTP", description="Protocol type based on IANA numbers.")    
    helper: HelperEnum | None = Field(default="auto", description="Helper name.")    
    iprange: str | None = Field(default="", description="Start and end of the IP range associated with service.")    
    fqdn: str | None = Field(max_length=255, default="", description="Fully qualified domain name.")    
    protocol_number: int | None = Field(ge=0, le=254, default=0, description="IP protocol number.")    
    icmptype: int | None = Field(ge=0, le=4294967295, default="", description="ICMP type.")    
    icmpcode: int | None = Field(ge=0, le=255, default="", description="ICMP code.")    
    tcp_portrange: str | None = Field(default="", description="Multiple TCP port ranges.")    
    udp_portrange: str | None = Field(default="", description="Multiple UDP port ranges.")    
    udplite_portrange: str | None = Field(default="", description="Multiple UDP-Lite port ranges.")    
    sctp_portrange: str | None = Field(default="", description="Multiple SCTP port ranges.")    
    tcp_halfclose_timer: int | None = Field(ge=0, le=86400, default=0, description="Wait time to close a TCP session waiting for an unanswered FIN packet (1 - 86400 sec, 0 = default).")    
    tcp_halfopen_timer: int | None = Field(ge=0, le=86400, default=0, description="Wait time to close a TCP session waiting for an unanswered open session packet (1 - 86400 sec, 0 = default).")    
    tcp_timewait_timer: int | None = Field(ge=0, le=300, default=0, description="Set the length of the TCP TIME-WAIT state in seconds (1 - 300 sec, 0 = default).")    
    tcp_rst_timer: int | None = Field(ge=5, le=300, default=0, description="Set the length of the TCP CLOSE state in seconds (5 - 300 sec, 0 = default).")    
    udp_idle_timer: int | None = Field(ge=0, le=86400, default=0, description="Number of seconds before an idle UDP/UDP-Lite connection times out (0 - 86400 sec, 0 = default).")    
    session_ttl: str | None = Field(default="", description="Session TTL (300 - 2764800, 0 = default).")    
    check_reset_range: Literal["disable", "strict", "default"] | None = Field(default="default", description="Configure the type of ICMP error message verification.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    color: int | None = Field(ge=0, le=32, default=0, description="Color of icon on the GUI.")    
    app_service_type: Literal["disable", "app-id", "app-category"] | None = Field(default="disable", description="Application service type.")    
    app_category: list[AppCategory] = Field(default=None, description="Application category ID.")    
    application: list[Application] = Field(default=None, description="Application ID.")    
    fabric_object: Literal["enable", "disable"] | None = Field(default="disable", description="Security Fabric global object setting.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('category')
    @classmethod
    def validate_category(cls, v: Any) -> Any:
        """
        Validate category field.
        
        Datasource: ['firewall.service.category.name']
        
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
    async def validate_category_references(self, client: Any) -> list[str]:
        """
        Validate category references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/service/category        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = CustomModel(
            ...     category="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_category_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.service.custom.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "category", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.service.category.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Category '{value}' not found in "
                "firewall/service/category"
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
        
        errors = await self.validate_category_references(client)
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
    "CustomModel",    "CustomAppCategory",    "CustomApplication",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.791076Z
# ============================================================================
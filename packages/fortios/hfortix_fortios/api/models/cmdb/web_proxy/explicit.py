"""
Pydantic Models for CMDB - web_proxy/explicit

Runtime validation models for web_proxy/explicit configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ExplicitSecureWebProxyCert(BaseModel):
    """
    Child table model for secure-web-proxy-cert.
    
    Name of certificates for secure web proxy.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="Fortinet_SSL", description="Certificate list.")  # datasource: ['vpn.certificate.local.name']
class ExplicitPacPolicy(BaseModel):
    """
    Child table model for pac-policy.
    
    PAC policies.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    policyid: int = Field(ge=1, le=100, default=0, description="Policy ID.")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable policy.")    
    srcaddr: list[Srcaddr] = Field(description="Source address objects.")    
    srcaddr6: list[Srcaddr6] = Field(default=None, description="Source address6 objects.")    
    dstaddr: list[Dstaddr] = Field(description="Destination address objects.")    
    pac_file_name: str = Field(max_length=63, default="proxy.pac", description="Pac file name.")    
    pac_file_data: str | None = Field(default="", description="PAC file contents enclosed in quotes (maximum of 256K bytes).")    
    comments: str | None = Field(max_length=1023, default=None, description="Optional comments.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExplicitSsl_dh_bitsEnum(str, Enum):
    """Allowed values for ssl_dh_bits field."""
    768 = "768"    1024 = "1024"    1536 = "1536"    2048 = "2048"
class ExplicitPref_dns_resultEnum(str, Enum):
    """Allowed values for pref_dns_result field."""
    IPV4 = "ipv4"    IPV6 = "ipv6"    IPV4_STRICT = "ipv4-strict"    IPV6_STRICT = "ipv6-strict"

# ============================================================================
# Main Model
# ============================================================================

class ExplicitModel(BaseModel):
    """
    Pydantic model for web_proxy/explicit configuration.
    
    Configure explicit Web proxy settings.
    
    Validation Rules:        - status: pattern=        - secure_web_proxy: pattern=        - ftp_over_http: pattern=        - socks: pattern=        - http_incoming_port: pattern=        - http_connection_mode: pattern=        - https_incoming_port: pattern=        - secure_web_proxy_cert: pattern=        - client_cert: pattern=        - user_agent_detect: pattern=        - empty_cert_action: pattern=        - ssl_dh_bits: pattern=        - ftp_incoming_port: pattern=        - socks_incoming_port: pattern=        - incoming_ip: pattern=        - outgoing_ip: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=        - ipv6_status: pattern=        - incoming_ip6: pattern=        - outgoing_ip6: pattern=        - strict_guest: pattern=        - pref_dns_result: pattern=        - unknown_http_version: pattern=        - realm: max_length=63 pattern=        - sec_default_action: pattern=        - https_replacement_message: pattern=        - message_upon_server_error: pattern=        - pac_file_server_status: pattern=        - pac_file_url: pattern=        - pac_file_server_port: pattern=        - pac_file_through_https: pattern=        - pac_file_name: max_length=63 pattern=        - pac_file_data: pattern=        - pac_policy: pattern=        - ssl_algorithm: pattern=        - trace_auth_no_rsp: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the explicit Web proxy for HTTP and HTTPS session.")    
    secure_web_proxy: Literal["disable", "enable", "secure"] | None = Field(default="disable", description="Enable/disable/require the secure web proxy for HTTP and HTTPS session.")    
    ftp_over_http: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to proxy FTP-over-HTTP sessions sent from a web browser.")    
    socks: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the SOCKS proxy.")    
    http_incoming_port: str | None = Field(default="", description="Accept incoming HTTP requests on one or more ports (0 - 65535, default = 8080).")    
    http_connection_mode: Literal["static", "multiplex", "serverpool"] | None = Field(default="static", description="HTTP connection mode (default = static).")    
    https_incoming_port: str | None = Field(default="", description="Accept incoming HTTPS requests on one or more ports (0 - 65535, default = 0, use the same as HTTP).")    
    secure_web_proxy_cert: list[SecureWebProxyCert] = Field(default=None, description="Name of certificates for secure web proxy.")    
    client_cert: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable to request client certificate.")    
    user_agent_detect: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable to detect device type by HTTP user-agent if no client certificate provided.")    
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = Field(default="block", description="Action of an empty client certificate.")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).")    
    ftp_incoming_port: str | None = Field(default="", description="Accept incoming FTP-over-HTTP requests on one or more ports (0 - 65535, default = 0; use the same as HTTP).")    
    socks_incoming_port: str | None = Field(default="", description="Accept incoming SOCKS proxy requests on one or more ports (0 - 65535, default = 0; use the same as HTTP).")    
    incoming_ip: str | None = Field(default="0.0.0.0", description="Restrict the explicit HTTP proxy to only accept sessions from this IP address. An interface must have this IP address.")    
    outgoing_ip: list[OutgoingIp] = Field(default="", description="Outgoing HTTP requests will have this IP address as their source address. An interface must have this IP address.")    
    interface_select_method: Literal["sdwan", "specify"] | None = Field(default="sdwan", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=-1, description="VRF ID used for connection to server.")    
    ipv6_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable allowing an IPv6 web proxy destination in policies and all IPv6 related entries in this command.")    
    incoming_ip6: str | None = Field(default="::", description="Restrict the explicit web proxy to only accept sessions from this IPv6 address. An interface must have this IPv6 address.")    
    outgoing_ip6: list[OutgoingIp6] = Field(default="", description="Outgoing HTTP requests will leave this IPv6. Multiple interfaces can be specified. Interfaces must have these IPv6 addresses.")    
    strict_guest: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable strict guest user checking by the explicit web proxy.")    
    pref_dns_result: PrefDnsResultEnum | None = Field(default="ipv4", description="Prefer resolving addresses using the configured IPv4 or IPv6 DNS server (default = ipv4).")    
    unknown_http_version: Literal["reject", "best-effort"] | None = Field(default="reject", description="How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.")    
    realm: str = Field(max_length=63, default="default", description="Authentication realm used to identify the explicit web proxy (maximum of 63 characters).")    
    sec_default_action: Literal["accept", "deny"] | None = Field(default="deny", description="Accept or deny explicit web proxy sessions when no web proxy firewall policy exists.")    
    https_replacement_message: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending the client a replacement message for HTTPS requests.")    
    message_upon_server_error: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable displaying a replacement message when a server error is detected.")    
    pac_file_server_status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable Proxy Auto-Configuration (PAC) for users of this explicit proxy profile.")    
    pac_file_url: str | None = Field(default="", description="PAC file access URL.")    
    pac_file_server_port: str | None = Field(default="", description="Port number that PAC traffic from client web browsers uses to connect to the explicit web proxy (0 - 65535, default = 0; use the same as HTTP).")    
    pac_file_through_https: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable to get Proxy Auto-Configuration (PAC) through HTTPS.")    
    pac_file_name: str = Field(max_length=63, default="proxy.pac", description="Pac file name.")    
    pac_file_data: str | None = Field(default="", description="PAC file contents enclosed in quotes (maximum of 256K bytes).")    
    pac_policy: list[PacPolicy] = Field(default=None, description="PAC policies.")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="low", description="Relative strength of encryption algorithms accepted in HTTPS deep scan: high, medium, or low.")    
    trace_auth_no_rsp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logging timed-out authentication requests.")    
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
    async def validate_secure_web_proxy_cert_references(self, client: Any) -> list[str]:
        """
        Validate secure_web_proxy_cert references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ExplicitModel(
            ...     secure_web_proxy_cert=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_secure_web_proxy_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.web_proxy.explicit.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "secure_web_proxy_cert", [])
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
            if await client.api.cmdb.vpn.certificate.local.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Secure-Web-Proxy-Cert '{value}' not found in "
                    "vpn/certificate/local"
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
            >>> policy = ExplicitModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.web_proxy.explicit.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_secure_web_proxy_cert_references(client)
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
    "ExplicitModel",    "ExplicitSecureWebProxyCert",    "ExplicitPacPolicy",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:57.458492Z
# ============================================================================
"""
Pydantic Models for CMDB - user/exchange

Runtime validation models for user/exchange configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ExchangeKdcIp(BaseModel):
    """
    Child table model for kdc-ip.
    
    KDC IPv4 addresses for Kerberos authentication.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ipv4: str = Field(max_length=79, default="", description="KDC IPv4 addresses for Kerberos authentication.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ExchangeAuth_levelEnum(str, Enum):
    """Allowed values for auth_level field."""
    CONNECT = "connect"    CALL = "call"    PACKET = "packet"    INTEGRITY = "integrity"    PRIVACY = "privacy"
class ExchangeSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"

# ============================================================================
# Main Model
# ============================================================================

class ExchangeModel(BaseModel):
    """
    Pydantic model for user/exchange configuration.
    
    Configure MS Exchange server entries.
    
    Validation Rules:        - name: max_length=35 pattern=        - server_name: max_length=63 pattern=        - domain_name: max_length=79 pattern=        - username: max_length=64 pattern=        - password: max_length=128 pattern=        - ip: pattern=        - connect_protocol: pattern=        - validate_server_certificate: pattern=        - auth_type: pattern=        - auth_level: pattern=        - http_auth_type: pattern=        - ssl_min_proto_version: pattern=        - auto_discover_kdc: pattern=        - kdc_ip: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="MS Exchange server entry name.")    
    server_name: str = Field(max_length=63, default="", description="MS Exchange server hostname.")    
    domain_name: str = Field(max_length=79, default="", description="MS Exchange server fully qualified domain name.")    
    username: str = Field(max_length=64, default="", description="User name used to sign in to the server. Must have proper permissions for service.")    
    password: Any = Field(max_length=128, description="Password for the specified username.")    
    ip: str | None = Field(default="0.0.0.0", description="Server IPv4 address.")    
    connect_protocol: Literal["rpc-over-tcp", "rpc-over-http", "rpc-over-https"] | None = Field(default="rpc-over-https", description="Connection protocol used to connect to MS Exchange service.")    
    validate_server_certificate: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable exchange server certificate validation.")    
    auth_type: Literal["spnego", "ntlm", "kerberos"] | None = Field(default="kerberos", description="Authentication security type used for the RPC protocol layer.")    
    auth_level: AuthLevelEnum | None = Field(default="privacy", description="Authentication security level used for the RPC protocol layer.")    
    http_auth_type: Literal["basic", "ntlm"] | None = Field(default="ntlm", description="Authentication security type used for the HTTP transport.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum SSL/TLS protocol version for HTTPS transport (default is to follow system global setting).")    
    auto_discover_kdc: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable automatic discovery of KDC IP addresses.")    
    kdc_ip: list[KdcIp] = Field(default=None, description="KDC IPv4 addresses for Kerberos authentication.")    
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

# ============================================================================
# Type Aliases for Convenience
# ============================================================================

Dict = dict[str, Any]  # For backward compatibility

# ============================================================================
# Module Exports
# ============================================================================

__all__ = [
    "ExchangeModel",    "ExchangeKdcIp",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.985537Z
# ============================================================================
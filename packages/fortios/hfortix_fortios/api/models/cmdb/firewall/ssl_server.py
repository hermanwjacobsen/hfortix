"""
Pydantic Models for CMDB - firewall/ssl_server

Runtime validation models for firewall/ssl_server configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SslServerSslCert(BaseModel):
    """
    Child table model for ssl-cert.
    
    List of certificate names to use for SSL connections to this server. (default = "Fortinet_SSL").
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="Fortinet_SSL", description="Certificate list.")  # datasource: ['vpn.certificate.local.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SslServerSsl_dh_bitsEnum(str, Enum):
    """Allowed values for ssl_dh_bits field."""
    768 = "768"    1024 = "1024"    1536 = "1536"    2048 = "2048"
class SslServerSsl_min_versionEnum(str, Enum):
    """Allowed values for ssl_min_version field."""
    TLS_1_0 = "tls-1.0"    TLS_1_1 = "tls-1.1"    TLS_1_2 = "tls-1.2"    TLS_1_3 = "tls-1.3"
class SslServerSsl_max_versionEnum(str, Enum):
    """Allowed values for ssl_max_version field."""
    TLS_1_0 = "tls-1.0"    TLS_1_1 = "tls-1.1"    TLS_1_2 = "tls-1.2"    TLS_1_3 = "tls-1.3"

# ============================================================================
# Main Model
# ============================================================================

class SslServerModel(BaseModel):
    """
    Pydantic model for firewall/ssl_server configuration.
    
    Configure SSL servers.
    
    Validation Rules:        - name: max_length=35 pattern=        - ip: pattern=        - port: min=1 max=65535 pattern=        - ssl_mode: pattern=        - add_header_x_forwarded_proto: pattern=        - mapped_port: min=1 max=65535 pattern=        - ssl_cert: pattern=        - ssl_dh_bits: pattern=        - ssl_algorithm: pattern=        - ssl_client_renegotiation: pattern=        - ssl_min_version: pattern=        - ssl_max_version: pattern=        - ssl_send_empty_frags: pattern=        - url_rewrite: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Server name.")    
    ip: str = Field(default="0.0.0.0", description="IPv4 address of the SSL server.")    
    port: int = Field(ge=1, le=65535, default=443, description="Server service port (1 - 65535, default = 443).")    
    ssl_mode: Literal["half", "full"] | None = Field(default="full", description="SSL/TLS mode for encryption and decryption of traffic.")    
    add_header_x_forwarded_proto: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable adding an X-Forwarded-Proto header to forwarded requests.")    
    mapped_port: int = Field(ge=1, le=65535, default=80, description="Mapped server service port (1 - 65535, default = 80).")    
    ssl_cert: list[SslCert] = Field(default=None, description="List of certificate names to use for SSL connections to this server. (default = \"Fortinet_SSL\").")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048).")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="high", description="Relative strength of encryption algorithms accepted in negotiation.")    
    ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = Field(default="allow", description="Allow or block client renegotiation by server.")    
    ssl_min_version: SslMinVersionEnum | None = Field(default="tls-1.1", description="Lowest SSL/TLS version to negotiate.")    
    ssl_max_version: SslMaxVersionEnum | None = Field(default="tls-1.3", description="Highest SSL/TLS version to negotiate.")    
    ssl_send_empty_frags: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending empty fragments to avoid attack on CBC IV.")    
    url_rewrite: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable rewriting the URL.")    
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
    async def validate_ssl_cert_references(self, client: Any) -> list[str]:
        """
        Validate ssl_cert references exist in FortiGate.
        
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
            >>> policy = SslServerModel(
            ...     ssl_cert=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssl_server.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ssl_cert", [])
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
                    f"Ssl-Cert '{value}' not found in "
                    "vpn/certificate/local"
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
        
        errors = await self.validate_ssl_cert_references(client)
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
    "SslServerModel",    "SslServerSslCert",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:41.960600Z
# ============================================================================
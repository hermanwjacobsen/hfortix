"""
Pydantic Models for CMDB - firewall/ssl_ssh_profile

Runtime validation models for firewall/ssl_ssh_profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SslSshProfileSsl(BaseModel):
    """
    Child table model for ssl.
    
    Configure SSL options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    inspect_all: Literal["disable", "certificate-inspection", "deep-inspection"] | None = Field(default="disable", description="Level of SSL inspection.")    
    client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate.")    
    unsupported_ssl_version: Literal["allow", "block"] | None = Field(default="block", description="Action based on the SSL version used being unsupported.")    
    unsupported_ssl_cipher: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL cipher used being unsupported.")    
    unsupported_ssl_negotiation: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL negotiation used being unsupported.")    
    expired_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is expired.")    
    revoked_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is revoked.")    
    untrusted_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on server certificate is not issued by a trusted CA.")    
    cert_validation_timeout: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on certificate validation timeout.")    
    cert_validation_failure: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on certificate validation failure.")    
    sni_server_cert_check: Literal["enable", "strict", "disable"] | None = Field(default="enable", description="Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.")    
    cert_probe_failure: Literal["allow", "block"] | None = Field(default="allow", description="Action based on certificate probe failure.")    
    encrypted_client_hello: Literal["allow", "block"] | None = Field(default="block", description="Block/allow session based on existence of encrypted-client-hello.")    
    min_allowed_ssl_version: MinAllowedSslVersionEnum | None = Field(default="tls-1.1", description="Minimum SSL version to be allowed.")
class SslSshProfileHttps(BaseModel):
    """
    Child table model for https.
    
    Configure HTTPS options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to use for scanning (1 - 65535, default = 443).")    
    status: Literal["disable", "certificate-inspection", "deep-inspection"] | None = Field(default="deep-inspection", description="Configure protocol inspection status.")    
    quic: Literal["inspect", "bypass", "block"] | None = Field(default="inspect", description="QUIC inspection status (default = inspect).")    
    udp_not_quic: Literal["allow", "block"] | None = Field(default="allow", description="Action to be taken when matched UDP packet is not QUIC.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate.")    
    unsupported_ssl_version: Literal["allow", "block"] | None = Field(default="block", description="Action based on the SSL version used being unsupported.")    
    unsupported_ssl_cipher: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL cipher used being unsupported.")    
    unsupported_ssl_negotiation: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL negotiation used being unsupported.")    
    expired_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is expired.")    
    revoked_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is revoked.")    
    untrusted_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on server certificate is not issued by a trusted CA.")    
    cert_validation_timeout: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on certificate validation timeout.")    
    cert_validation_failure: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on certificate validation failure.")    
    sni_server_cert_check: Literal["enable", "strict", "disable"] | None = Field(default="enable", description="Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.")    
    cert_probe_failure: Literal["allow", "block"] | None = Field(default="allow", description="Action based on certificate probe failure.")    
    encrypted_client_hello: Literal["allow", "block"] | None = Field(default="block", description="Block/allow session based on existence of encrypted-client-hello.")    
    min_allowed_ssl_version: MinAllowedSslVersionEnum | None = Field(default="tls-1.1", description="Minimum SSL version to be allowed.")
class SslSshProfileFtps(BaseModel):
    """
    Child table model for ftps.
    
    Configure FTPS options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to use for scanning (1 - 65535, default = 443).")    
    status: Literal["disable", "deep-inspection"] | None = Field(default="deep-inspection", description="Configure protocol inspection status.")    
    client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate.")    
    unsupported_ssl_version: Literal["allow", "block"] | None = Field(default="block", description="Action based on the SSL version used being unsupported.")    
    unsupported_ssl_cipher: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL cipher used being unsupported.")    
    unsupported_ssl_negotiation: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL negotiation used being unsupported.")    
    expired_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is expired.")    
    revoked_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is revoked.")    
    untrusted_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on server certificate is not issued by a trusted CA.")    
    cert_validation_timeout: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on certificate validation timeout.")    
    cert_validation_failure: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on certificate validation failure.")    
    sni_server_cert_check: Literal["enable", "strict", "disable"] | None = Field(default="enable", description="Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.")    
    min_allowed_ssl_version: MinAllowedSslVersionEnum | None = Field(default="tls-1.1", description="Minimum SSL version to be allowed.")
class SslSshProfileImaps(BaseModel):
    """
    Child table model for imaps.
    
    Configure IMAPS options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to use for scanning (1 - 65535, default = 443).")    
    status: Literal["disable", "deep-inspection"] | None = Field(default="deep-inspection", description="Configure protocol inspection status.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="inspect", description="Action based on received client certificate.")    
    unsupported_ssl_version: Literal["allow", "block"] | None = Field(default="block", description="Action based on the SSL version used being unsupported.")    
    unsupported_ssl_cipher: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL cipher used being unsupported.")    
    unsupported_ssl_negotiation: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL negotiation used being unsupported.")    
    expired_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is expired.")    
    revoked_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is revoked.")    
    untrusted_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on server certificate is not issued by a trusted CA.")    
    cert_validation_timeout: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on certificate validation timeout.")    
    cert_validation_failure: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on certificate validation failure.")    
    sni_server_cert_check: Literal["enable", "strict", "disable"] | None = Field(default="enable", description="Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.")
class SslSshProfilePop3s(BaseModel):
    """
    Child table model for pop3s.
    
    Configure POP3S options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to use for scanning (1 - 65535, default = 443).")    
    status: Literal["disable", "deep-inspection"] | None = Field(default="deep-inspection", description="Configure protocol inspection status.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="inspect", description="Action based on received client certificate.")    
    unsupported_ssl_version: Literal["allow", "block"] | None = Field(default="block", description="Action based on the SSL version used being unsupported.")    
    unsupported_ssl_cipher: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL cipher used being unsupported.")    
    unsupported_ssl_negotiation: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL negotiation used being unsupported.")    
    expired_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is expired.")    
    revoked_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is revoked.")    
    untrusted_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on server certificate is not issued by a trusted CA.")    
    cert_validation_timeout: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on certificate validation timeout.")    
    cert_validation_failure: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on certificate validation failure.")    
    sni_server_cert_check: Literal["enable", "strict", "disable"] | None = Field(default="enable", description="Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.")
class SslSshProfileSmtps(BaseModel):
    """
    Child table model for smtps.
    
    Configure SMTPS options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to use for scanning (1 - 65535, default = 443).")    
    status: Literal["disable", "deep-inspection"] | None = Field(default="deep-inspection", description="Configure protocol inspection status.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="inspect", description="Action based on received client certificate.")    
    unsupported_ssl_version: Literal["allow", "block"] | None = Field(default="block", description="Action based on the SSL version used being unsupported.")    
    unsupported_ssl_cipher: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL cipher used being unsupported.")    
    unsupported_ssl_negotiation: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL negotiation used being unsupported.")    
    expired_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is expired.")    
    revoked_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is revoked.")    
    untrusted_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on server certificate is not issued by a trusted CA.")    
    cert_validation_timeout: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on certificate validation timeout.")    
    cert_validation_failure: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on certificate validation failure.")    
    sni_server_cert_check: Literal["enable", "strict", "disable"] | None = Field(default="enable", description="Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.")
class SslSshProfileSsh(BaseModel):
    """
    Child table model for ssh.
    
    Configure SSH options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to use for scanning (1 - 65535, default = 443).")    
    status: Literal["disable", "deep-inspection"] | None = Field(default="disable", description="Configure protocol inspection status.")    
    inspect_all: Literal["disable", "deep-inspection"] | None = Field(default="disable", description="Level of SSL inspection.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    unsupported_version: Literal["bypass", "block"] | None = Field(default="bypass", description="Action based on SSH version being unsupported.")    
    ssh_tun_policy_check: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable SSH tunnel policy check.")    
    ssh_algorithm: Literal["compatible", "high-encryption"] | None = Field(default="compatible", description="Relative strength of encryption algorithms accepted during negotiation.")
class SslSshProfileDot(BaseModel):
    """
    Child table model for dot.
    
    Configure DNS over TLS options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "deep-inspection"] | None = Field(default="disable", description="Configure protocol inspection status.")    
    quic: Literal["inspect", "bypass", "block"] | None = Field(default="inspect", description="QUIC inspection status (default = inspect).")    
    udp_not_quic: Literal["allow", "block"] | None = Field(default="allow", description="Action to be taken when matched UDP packet is not QUIC.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate.")    
    unsupported_ssl_version: Literal["allow", "block"] | None = Field(default="block", description="Action based on the SSL version used being unsupported.")    
    unsupported_ssl_cipher: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL cipher used being unsupported.")    
    unsupported_ssl_negotiation: Literal["allow", "block"] | None = Field(default="allow", description="Action based on the SSL negotiation used being unsupported.")    
    expired_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is expired.")    
    revoked_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on server certificate is revoked.")    
    untrusted_server_cert: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on server certificate is not issued by a trusted CA.")    
    cert_validation_timeout: Literal["allow", "block", "ignore"] | None = Field(default="allow", description="Action based on certificate validation timeout.")    
    cert_validation_failure: Literal["allow", "block", "ignore"] | None = Field(default="block", description="Action based on certificate validation failure.")    
    sni_server_cert_check: Literal["enable", "strict", "disable"] | None = Field(default="enable", description="Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.")
class SslSshProfileSslExempt(BaseModel):
    """
    Child table model for ssl-exempt.
    
    Servers to exempt from SSL inspection.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=512, default=0, description="ID number.")    
    type: TypeEnum = Field(default="fortiguard-category", description="Type of address object (IPv4 or IPv6) or FortiGuard category.")    
    fortiguard_category: int | None = Field(ge=0, le=255, default=0, description="FortiGuard category ID.")    
    address: str | None = Field(max_length=79, default="", description="IPv4 address object.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    address6: str | None = Field(max_length=79, default="", description="IPv6 address object.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']    
    wildcard_fqdn: str | None = Field(max_length=79, default="", description="Exempt servers by wildcard FQDN.")  # datasource: ['firewall.wildcard-fqdn.custom.name', 'firewall.wildcard-fqdn.group.name']    
    regex: str | None = Field(max_length=255, default="", description="Exempt servers by regular expression.")
class SslSshProfileEchOuterSni(BaseModel):
    """
    Child table model for ech-outer-sni.
    
    ClientHelloOuter SNIs to be blocked.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="ClientHelloOuter SNI name.")    
    sni: str = Field(max_length=255, default="", description="ClientHelloOuter SNI to be blocked.")
class SslSshProfileServerCert(BaseModel):
    """
    Child table model for server-cert.
    
    Certificate used by SSL Inspection to replace server certificate.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="Fortinet_SSL", description="Certificate list.")  # datasource: ['vpn.certificate.local.name']
class SslSshProfileSslServer(BaseModel):
    """
    Child table model for ssl-server.
    
    SSL server settings used for client certificate request.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="SSL server ID.")    
    ip: str = Field(default="0.0.0.0", description="IPv4 address of the SSL server.")    
    https_client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate during the HTTPS handshake.")    
    smtps_client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate during the SMTPS handshake.")    
    pop3s_client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate during the POP3S handshake.")    
    imaps_client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate during the IMAPS handshake.")    
    ftps_client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate during the FTPS handshake.")    
    ssl_other_client_certificate: Literal["bypass", "inspect", "block"] | None = Field(default="bypass", description="Action based on received client certificate during an SSL protocol handshake.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SslSshProfileSupported_alpnEnum(str, Enum):
    """Allowed values for supported_alpn field."""
    HTTP1_1 = "http1-1"    HTTP2 = "http2"    ALL = "all"    NONE = "none"

# ============================================================================
# Main Model
# ============================================================================

class SslSshProfileModel(BaseModel):
    """
    Pydantic model for firewall/ssl_ssh_profile configuration.
    
    Configure SSL/SSH protocol options.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - ssl: pattern=        - https: pattern=        - ftps: pattern=        - imaps: pattern=        - pop3s: pattern=        - smtps: pattern=        - ssh: pattern=        - dot: pattern=        - allowlist: pattern=        - block_blocklisted_certificates: pattern=        - ssl_exempt: pattern=        - ech_outer_sni: pattern=        - server_cert_mode: pattern=        - use_ssl_server: pattern=        - caname: max_length=35 pattern=        - untrusted_caname: max_length=35 pattern=        - server_cert: pattern=        - ssl_server: pattern=        - ssl_exemption_ip_rating: pattern=        - ssl_exemption_log: pattern=        - ssl_anomaly_log: pattern=        - ssl_negotiation_log: pattern=        - ssl_server_cert_log: pattern=        - ssl_handshake_log: pattern=        - rpc_over_https: pattern=        - mapi_over_https: pattern=        - supported_alpn: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Name.")    
    comment: str | None = Field(max_length=255, default=None, description="Optional comments.")    
    ssl: list[Ssl] = Field(default=None, description="Configure SSL options.")    
    https: list[Https] = Field(default=None, description="Configure HTTPS options.")    
    ftps: list[Ftps] = Field(default=None, description="Configure FTPS options.")    
    imaps: list[Imaps] = Field(default=None, description="Configure IMAPS options.")    
    pop3s: list[Pop3S] = Field(default=None, description="Configure POP3S options.")    
    smtps: list[Smtps] = Field(default=None, description="Configure SMTPS options.")    
    ssh: list[Ssh] = Field(default=None, description="Configure SSH options.")    
    dot: list[Dot] = Field(default=None, description="Configure DNS over TLS options.")    
    allowlist: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable exempting servers by FortiGuard allowlist.")    
    block_blocklisted_certificates: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blocklist.")    
    ssl_exempt: list[SslExempt] = Field(default=None, description="Servers to exempt from SSL inspection.")    
    ech_outer_sni: list[EchOuterSni] = Field(default=None, description="ClientHelloOuter SNIs to be blocked.")    
    server_cert_mode: Literal["re-sign", "replace"] = Field(default="re-sign", description="Re-sign or replace the server's certificate.")    
    use_ssl_server: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable the use of SSL server table for SSL offloading.")    
    caname: str = Field(max_length=35, default="Fortinet_CA_SSL", description="CA certificate used by SSL Inspection.")  # datasource: ['vpn.certificate.local.name', 'vpn.certificate.hsm-local.name']    
    untrusted_caname: str = Field(max_length=35, default="Fortinet_CA_Untrusted", description="Untrusted CA certificate used by SSL Inspection.")  # datasource: ['vpn.certificate.local.name', 'vpn.certificate.hsm-local.name']    
    server_cert: list[ServerCert] = Field(default=None, description="Certificate used by SSL Inspection to replace server certificate.")    
    ssl_server: list[SslServer] = Field(description="SSL server settings used for client certificate request.")    
    ssl_exemption_ip_rating: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IP based URL rating.")    
    ssl_exemption_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of SSL exemptions.")    
    ssl_anomaly_log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable logging of SSL anomalies.")    
    ssl_negotiation_log: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable logging of SSL negotiation events.")    
    ssl_server_cert_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of server certificate information.")    
    ssl_handshake_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of TLS handshakes.")    
    rpc_over_https: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable inspection of RPC over HTTPS.")    
    mapi_over_https: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable inspection of MAPI over HTTPS.")    
    supported_alpn: SupportedAlpnEnum | None = Field(default="all", description="Configure ALPN option.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('caname')
    @classmethod
    def validate_caname(cls, v: Any) -> Any:
        """
        Validate caname field.
        
        Datasource: ['vpn.certificate.local.name', 'vpn.certificate.hsm-local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('untrusted_caname')
    @classmethod
    def validate_untrusted_caname(cls, v: Any) -> Any:
        """
        Validate untrusted_caname field.
        
        Datasource: ['vpn.certificate.local.name', 'vpn.certificate.hsm-local.name']
        
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
    async def validate_ssl_exempt_references(self, client: Any) -> list[str]:
        """
        Validate ssl_exempt references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/wildcard-fqdn/custom        - firewall/wildcard-fqdn/group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SslSshProfileModel(
            ...     ssl_exempt=[{"wildcard-fqdn": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_exempt_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssl_ssh_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ssl_exempt", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("wildcard-fqdn")
            else:
                value = getattr(item, "wildcard-fqdn", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.firewall.wildcard-fqdn.custom.exists(value):
                found = True
            elif await client.api.cmdb.firewall.wildcard-fqdn.group.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ssl-Exempt '{value}' not found in "
                    "firewall/wildcard-fqdn/custom or firewall/wildcard-fqdn/group"
                )        
        return errors    
    async def validate_caname_references(self, client: Any) -> list[str]:
        """
        Validate caname references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        - vpn/certificate/hsm-local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SslSshProfileModel(
            ...     caname="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_caname_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssl_ssh_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "caname", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        elif await client.api.cmdb.vpn.certificate.hsm-local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Caname '{value}' not found in "
                "vpn/certificate/local or vpn/certificate/hsm-local"
            )        
        return errors    
    async def validate_untrusted_caname_references(self, client: Any) -> list[str]:
        """
        Validate untrusted_caname references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        - vpn/certificate/hsm-local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SslSshProfileModel(
            ...     untrusted_caname="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_untrusted_caname_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssl_ssh_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "untrusted_caname", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        elif await client.api.cmdb.vpn.certificate.hsm-local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Untrusted-Caname '{value}' not found in "
                "vpn/certificate/local or vpn/certificate/hsm-local"
            )        
        return errors    
    async def validate_server_cert_references(self, client: Any) -> list[str]:
        """
        Validate server_cert references exist in FortiGate.
        
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
            >>> policy = SslSshProfileModel(
            ...     server_cert=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_server_cert_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.ssl_ssh_profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "server_cert", [])
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
                    f"Server-Cert '{value}' not found in "
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
        
        errors = await self.validate_ssl_exempt_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_caname_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_untrusted_caname_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_server_cert_references(client)
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
    "SslSshProfileModel",    "SslSshProfileSsl",    "SslSshProfileHttps",    "SslSshProfileFtps",    "SslSshProfileImaps",    "SslSshProfilePop3s",    "SslSshProfileSmtps",    "SslSshProfileSsh",    "SslSshProfileDot",    "SslSshProfileSslExempt",    "SslSshProfileEchOuterSni",    "SslSshProfileServerCert",    "SslSshProfileSslServer",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.538761Z
# ============================================================================
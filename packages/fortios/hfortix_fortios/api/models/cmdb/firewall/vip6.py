"""
Pydantic Models for CMDB - firewall/vip6

Runtime validation models for firewall/vip6 configuration.
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

class Vip6SrcFilter(BaseModel):
    """
    Child table model for src-filter.
    
    Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses with spaces.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    range: str = Field(max_length=79, default="", description="Source-filter range.")
class Vip6Quic(BaseModel):
    """
    Child table model for quic.
    
    QUIC setting.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    max_idle_timeout: int | None = Field(ge=1, le=60000, default=30000, description="Maximum idle timeout milliseconds (1 - 60000, default = 30000).")    
    max_udp_payload_size: int | None = Field(ge=1200, le=1500, default=1500, description="Maximum UDP payload size in bytes (1200 - 1500, default = 1500).")    
    active_connection_id_limit: int | None = Field(ge=1, le=8, default=2, description="Active connection ID limit (1 - 8, default = 2).")    
    ack_delay_exponent: int | None = Field(ge=1, le=20, default=3, description="ACK delay exponent (1 - 20, default = 3).")    
    max_ack_delay: int | None = Field(ge=1, le=16383, default=25, description="Maximum ACK delay in milliseconds (1 - 16383, default = 25).")    
    max_datagram_frame_size: int | None = Field(ge=1, le=1500, default=1500, description="Maximum datagram frame size in bytes (1 - 1500, default = 1500).")    
    active_migration: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable active migration (default = disable).")    
    grease_quic_bit: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable grease QUIC bit (default = enable).")
class Vip6Realservers(BaseModel):
    """
    Child table model for realservers.
    
    Select the real servers that this server load balancing VIP will distribute traffic to.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Real server ID.")    
    ip: str = Field(default="", description="IP address of the real server.")    
    port: int | None = Field(ge=1, le=65535, default=0, description="Port for communicating with the real server. Required if port forwarding is enabled.")    
    status: Literal["active", "standby", "disable"] | None = Field(default="active", description="Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.")    
    weight: int | None = Field(ge=1, le=255, default=1, description="Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections.")    
    holddown_interval: int | None = Field(ge=30, le=65535, default=300, description="Time in seconds that the system waits before re-activating a previously down active server in the active-standby mode. This is to prevent any flapping issues.")    
    healthcheck: Literal["disable", "enable", "vip"] | None = Field(default="vip", description="Enable to check the responsiveness of the real server before forwarding traffic.")    
    http_host: str | None = Field(max_length=63, default="", description="HTTP server domain name in HTTP header.")    
    translate_host: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable translation of hostname/IP from virtual server to real server.")    
    max_connections: int | None = Field(ge=0, le=2147483647, default=0, description="Max number of active connections that can directed to the real server. When reached, sessions are sent to other real servers.")    
    monitor: list[Monitor] = Field(default=None, description="Name of the health check monitor to use when polling to determine a virtual server's connectivity status.")    
    client_ip: str | None = Field(default="", description="Only clients in this IP range can connect to this real server.")    
    verify_cert: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable certificate verification of the real server.")
class Vip6SslCertificate(BaseModel):
    """
    Child table model for ssl-certificate.
    
    Name of the certificate to use for SSL handshake.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Certificate list.")  # datasource: ['vpn.certificate.local.name']
class Vip6SslCipherSuites(BaseModel):
    """
    Child table model for ssl-cipher-suites.
    
    SSL/TLS cipher suites acceptable from a client, ordered by priority.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    priority: int | None = Field(ge=0, le=4294967295, default=0, description="SSL/TLS cipher suites priority.")    
    cipher: CipherEnum = Field(default="", description="Cipher suite name.")    
    versions: list[Versions] = Field(default="ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3", description="SSL/TLS versions that the cipher suite can be used with.")
class Vip6SslServerCipherSuites(BaseModel):
    """
    Child table model for ssl-server-cipher-suites.
    
    SSL/TLS cipher suites to offer to a server, ordered by priority.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    priority: int | None = Field(ge=0, le=4294967295, default=0, description="SSL/TLS cipher suites priority.")    
    cipher: CipherEnum = Field(default="", description="Cipher suite name.")    
    versions: list[Versions] = Field(default="ssl-3.0 tls-1.0 tls-1.1 tls-1.2 tls-1.3", description="SSL/TLS versions that the cipher suite can be used with.")
class Vip6Monitor(BaseModel):
    """
    Child table model for monitor.
    
    Name of the health check monitor to use when polling to determine a virtual server's connectivity status.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Health monitor name.")  # datasource: ['firewall.ldb-monitor.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class Vip6Ldb_methodEnum(str, Enum):
    """Allowed values for ldb_method field."""
    STATIC = "static"    ROUND_ROBIN = "round-robin"    WEIGHTED = "weighted"    LEAST_SESSION = "least-session"    LEAST_RTT = "least-rtt"    FIRST_ALIVE = "first-alive"    HTTP_HOST = "http-host"
class Vip6Server_typeEnum(str, Enum):
    """Allowed values for server_type field."""
    HTTP = "http"    HTTPS = "https"    IMAPS = "imaps"    POP3S = "pop3s"    SMTPS = "smtps"    SSL = "ssl"    TCP = "tcp"    UDP = "udp"    IP = "ip"
class Vip6Ssl_dh_bitsEnum(str, Enum):
    """Allowed values for ssl_dh_bits field."""
    768 = "768"    1024 = "1024"    1536 = "1536"    2048 = "2048"    3072 = "3072"    4096 = "4096"
class Vip6Ssl_algorithmEnum(str, Enum):
    """Allowed values for ssl_algorithm field."""
    HIGH = "high"    MEDIUM = "medium"    LOW = "low"    CUSTOM = "custom"
class Vip6Ssl_server_algorithmEnum(str, Enum):
    """Allowed values for ssl_server_algorithm field."""
    HIGH = "high"    MEDIUM = "medium"    LOW = "low"    CUSTOM = "custom"    CLIENT = "client"
class Vip6Ssl_min_versionEnum(str, Enum):
    """Allowed values for ssl_min_version field."""
    SSL_3_0 = "ssl-3.0"    TLS_1_0 = "tls-1.0"    TLS_1_1 = "tls-1.1"    TLS_1_2 = "tls-1.2"    TLS_1_3 = "tls-1.3"
class Vip6Ssl_max_versionEnum(str, Enum):
    """Allowed values for ssl_max_version field."""
    SSL_3_0 = "ssl-3.0"    TLS_1_0 = "tls-1.0"    TLS_1_1 = "tls-1.1"    TLS_1_2 = "tls-1.2"    TLS_1_3 = "tls-1.3"
class Vip6Ssl_server_min_versionEnum(str, Enum):
    """Allowed values for ssl_server_min_version field."""
    SSL_3_0 = "ssl-3.0"    TLS_1_0 = "tls-1.0"    TLS_1_1 = "tls-1.1"    TLS_1_2 = "tls-1.2"    TLS_1_3 = "tls-1.3"    CLIENT = "client"
class Vip6Ssl_server_max_versionEnum(str, Enum):
    """Allowed values for ssl_server_max_version field."""
    SSL_3_0 = "ssl-3.0"    TLS_1_0 = "tls-1.0"    TLS_1_1 = "tls-1.1"    TLS_1_2 = "tls-1.2"    TLS_1_3 = "tls-1.3"    CLIENT = "client"
class Vip6Ssl_client_session_state_typeEnum(str, Enum):
    """Allowed values for ssl_client_session_state_type field."""
    DISABLE = "disable"    TIME = "time"    COUNT = "count"    BOTH = "both"
class Vip6Ssl_server_session_state_typeEnum(str, Enum):
    """Allowed values for ssl_server_session_state_type field."""
    DISABLE = "disable"    TIME = "time"    COUNT = "count"    BOTH = "both"

# ============================================================================
# Main Model
# ============================================================================

class Vip6Model(BaseModel):
    """
    Pydantic model for firewall/vip6 configuration.
    
    Configure virtual IP for IPv6.
    
    Validation Rules:        - name: max_length=79 pattern=        - id: min=0 max=65535 pattern=        - uuid: pattern=        - comment: max_length=255 pattern=        - type: pattern=        - src_filter: pattern=        - src_vip_filter: pattern=        - extip: pattern=        - mappedip: pattern=        - nat_source_vip: pattern=        - ndp_reply: pattern=        - portforward: pattern=        - protocol: pattern=        - extport: pattern=        - mappedport: pattern=        - color: min=0 max=32 pattern=        - ldb_method: pattern=        - server_type: pattern=        - http_redirect: pattern=        - persistence: pattern=        - h2_support: pattern=        - h3_support: pattern=        - quic: pattern=        - nat66: pattern=        - nat64: pattern=        - add_nat64_route: pattern=        - empty_cert_action: pattern=        - user_agent_detect: pattern=        - client_cert: pattern=        - realservers: pattern=        - http_cookie_domain_from_host: pattern=        - http_cookie_domain: max_length=35 pattern=        - http_cookie_path: max_length=35 pattern=        - http_cookie_generation: min=0 max=4294967295 pattern=        - http_cookie_age: min=0 max=525600 pattern=        - http_cookie_share: pattern=        - https_cookie_secure: pattern=        - http_multiplex: pattern=        - http_ip_header: pattern=        - http_ip_header_name: max_length=35 pattern=        - outlook_web_access: pattern=        - weblogic_server: pattern=        - websphere_server: pattern=        - ssl_mode: pattern=        - ssl_certificate: pattern=        - ssl_dh_bits: pattern=        - ssl_algorithm: pattern=        - ssl_cipher_suites: pattern=        - ssl_server_renegotiation: pattern=        - ssl_server_algorithm: pattern=        - ssl_server_cipher_suites: pattern=        - ssl_pfs: pattern=        - ssl_min_version: pattern=        - ssl_max_version: pattern=        - ssl_server_min_version: pattern=        - ssl_server_max_version: pattern=        - ssl_accept_ffdhe_groups: pattern=        - ssl_send_empty_frags: pattern=        - ssl_client_fallback: pattern=        - ssl_client_renegotiation: pattern=        - ssl_client_session_state_type: pattern=        - ssl_client_session_state_timeout: min=1 max=14400 pattern=        - ssl_client_session_state_max: min=1 max=10000 pattern=        - ssl_client_rekey_count: min=200 max=1048576 pattern=        - ssl_server_session_state_type: pattern=        - ssl_server_session_state_timeout: min=1 max=14400 pattern=        - ssl_server_session_state_max: min=1 max=10000 pattern=        - ssl_http_location_conversion: pattern=        - ssl_http_match_host: pattern=        - ssl_hpkp: pattern=        - ssl_hpkp_primary: max_length=79 pattern=        - ssl_hpkp_backup: max_length=79 pattern=        - ssl_hpkp_age: min=60 max=157680000 pattern=        - ssl_hpkp_report_uri: max_length=255 pattern=        - ssl_hpkp_include_subdomains: pattern=        - ssl_hsts: pattern=        - ssl_hsts_age: min=60 max=157680000 pattern=        - ssl_hsts_include_subdomains: pattern=        - monitor: pattern=        - max_embryonic_connections: min=0 max=100000 pattern=        - embedded_ipv4_address: pattern=        - ipv4_mappedip: pattern=        - ipv4_mappedport: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="Virtual ip6 name.")    
    id: int | None = Field(ge=0, le=65535, default=0, description="Custom defined ID.")    
    uuid: str | None = Field(default="00000000-0000-0000-0000-000000000000", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = Field(default="static-nat", description="Configure a static NAT server load balance VIP or access proxy.")    
    src_filter: list[SrcFilter] = Field(default=None, description="Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses with spaces.")    
    src_vip_filter: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of 'src-filter' to match destinations for the reverse SNAT rule.")    
    extip: str = Field(default="", description="IPv6 address or address range on the external interface that you want to map to an address or address range on the destination network.")    
    mappedip: str = Field(default="", description="Mapped IPv6 address range in the format startIP-endIP.")    
    nat_source_vip: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to perform SNAT on traffic from mappedip to the extip for all egress interfaces.")    
    ndp_reply: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable this FortiGate unit's ability to respond to NDP requests for this virtual IP address (default = enable).")    
    portforward: Literal["disable", "enable"] | None = Field(default="disable", description="Enable port forwarding.")    
    protocol: Literal["tcp", "udp", "sctp"] | None = Field(default="tcp", description="Protocol to use when forwarding packets.")    
    extport: str = Field(default="", description="Incoming port number range that you want to map to a port number range on the destination network.")    
    mappedport: str | None = Field(default="", description="Port number range on the destination network to which the external port number range is mapped.")    
    color: int | None = Field(ge=0, le=32, default=0, description="Color of icon on the GUI.")    
    ldb_method: LdbMethodEnum | None = Field(default="static", description="Method used to distribute sessions to real servers.")    
    server_type: ServerTypeEnum = Field(default="", description="Protocol to be load balanced by the virtual server (also called the server load balance virtual IP).")    
    http_redirect: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redirection of HTTP to HTTPS.")    
    persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = Field(default="none", description="Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.")    
    h2_support: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable HTTP2 support (default = enable).")    
    h3_support: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP3/QUIC support (default = disable).")    
    quic: list[Quic] = Field(default=None, description="QUIC setting.")    
    nat66: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable DNAT66.")    
    nat64: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable DNAT64.")    
    add_nat64_route: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable adding NAT64 route.")    
    empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = Field(default="block", description="Action for an empty client certificate.")    
    user_agent_detect: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable detecting device type by HTTP user-agent if no client certificate is provided.")    
    client_cert: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable requesting client certificate.")    
    realservers: list[Realservers] = Field(default=None, description="Select the real servers that this server load balancing VIP will distribute traffic to.")    
    http_cookie_domain_from_host: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of HTTP cookie domain from host field in HTTP.")    
    http_cookie_domain: str | None = Field(max_length=35, default="", description="Domain that HTTP cookie persistence should apply to.")    
    http_cookie_path: str | None = Field(max_length=35, default="", description="Limit HTTP cookie persistence to the specified path.")    
    http_cookie_generation: int | None = Field(ge=0, le=4294967295, default=0, description="Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.")    
    http_cookie_age: int | None = Field(ge=0, le=525600, default=60, description="Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.")    
    http_cookie_share: Literal["disable", "same-ip"] | None = Field(default="same-ip", description="Control sharing of cookies across virtual servers. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.")    
    https_cookie_secure: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable verification that inserted HTTPS cookies are secure.")    
    http_multiplex: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable HTTP multiplexing.")    
    http_ip_header: Literal["enable", "disable"] | None = Field(default="disable", description="For HTTP multiplexing, enable to add the original client IP address in the X-Forwarded-For HTTP header.")    
    http_ip_header_name: str | None = Field(max_length=35, default="", description="For HTTP multiplexing, enter a custom HTTPS header name. The original client IP address is added to this header. If empty, X-Forwarded-For is used.")    
    outlook_web_access: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to add the Front-End-Https header for Microsoft Outlook Web Access.")    
    weblogic_server: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.")    
    websphere_server: Literal["disable", "enable"] | None = Field(default="disable", description="Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.")    
    ssl_mode: Literal["half", "full"] | None = Field(default="half", description="Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full).")    
    ssl_certificate: list[SslCertificate] = Field(description="Name of the certificate to use for SSL handshake.")    
    ssl_dh_bits: SslDhBitsEnum | None = Field(default="2048", description="Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.")    
    ssl_algorithm: SslAlgorithmEnum | None = Field(default="high", description="Permitted encryption algorithms for SSL sessions according to encryption strength.")    
    ssl_cipher_suites: list[SslCipherSuites] = Field(default=None, description="SSL/TLS cipher suites acceptable from a client, ordered by priority.")    
    ssl_server_renegotiation: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable secure renegotiation to comply with RFC 5746.")    
    ssl_server_algorithm: SslServerAlgorithmEnum | None = Field(default="client", description="Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.")    
    ssl_server_cipher_suites: list[SslServerCipherSuites] = Field(default=None, description="SSL/TLS cipher suites to offer to a server, ordered by priority.")    
    ssl_pfs: Literal["require", "deny", "allow"] | None = Field(default="require", description="Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). Applies to both client and server sessions.")    
    ssl_min_version: SslMinVersionEnum | None = Field(default="tls-1.1", description="Lowest SSL/TLS version acceptable from a client.")    
    ssl_max_version: SslMaxVersionEnum | None = Field(default="tls-1.3", description="Highest SSL/TLS version acceptable from a client.")    
    ssl_server_min_version: SslServerMinVersionEnum | None = Field(default="client", description="Lowest SSL/TLS version acceptable from a server. Use the client setting by default.")    
    ssl_server_max_version: SslServerMaxVersionEnum | None = Field(default="client", description="Highest SSL/TLS version acceptable from a server. Use the client setting by default.")    
    ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable FFDHE cipher suite for SSL key exchange.")    
    ssl_send_empty_frags: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be disabled for compatibility with older systems.")    
    ssl_client_fallback: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507).")    
    ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = Field(default="secure", description="Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746.")    
    ssl_client_session_state_type: SslClientSessionStateTypeEnum | None = Field(default="both", description="How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate.")    
    ssl_client_session_state_timeout: int | None = Field(ge=1, le=14400, default=30, description="Number of minutes to keep client to FortiGate SSL session state.")    
    ssl_client_session_state_max: int | None = Field(ge=1, le=10000, default=1000, description="Maximum number of client to FortiGate SSL session states to keep.")    
    ssl_client_rekey_count: int | None = Field(ge=200, le=1048576, default=0, description="Maximum length of data in MB before triggering a client rekey (0 = disable).")    
    ssl_server_session_state_type: SslServerSessionStateTypeEnum | None = Field(default="both", description="How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate.")    
    ssl_server_session_state_timeout: int | None = Field(ge=1, le=14400, default=60, description="Number of minutes to keep FortiGate to Server SSL session state.")    
    ssl_server_session_state_max: int | None = Field(ge=1, le=10000, default=100, description="Maximum number of FortiGate to Server SSL session states to keep.")    
    ssl_http_location_conversion: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to replace HTTP with HTTPS in the reply's Location HTTP header field.")    
    ssl_http_match_host: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable HTTP host matching for location conversion.")    
    ssl_hpkp: Literal["disable", "enable", "report-only"] | None = Field(default="disable", description="Enable/disable including HPKP header in response.")    
    ssl_hpkp_primary: str | None = Field(max_length=79, default="", description="Certificate to generate primary HPKP pin from.")  # datasource: ['vpn.certificate.local.name', 'vpn.certificate.ca.name']    
    ssl_hpkp_backup: str | None = Field(max_length=79, default="", description="Certificate to generate backup HPKP pin from.")  # datasource: ['vpn.certificate.local.name', 'vpn.certificate.ca.name']    
    ssl_hpkp_age: int | None = Field(ge=60, le=157680000, default=5184000, description="Number of minutes the web browser should keep HPKP.")    
    ssl_hpkp_report_uri: str | None = Field(max_length=255, default=None, description="URL to report HPKP violations to.")    
    ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = Field(default="disable", description="Indicate that HPKP header applies to all subdomains.")    
    ssl_hsts: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable including HSTS header in response.")    
    ssl_hsts_age: int | None = Field(ge=60, le=157680000, default=5184000, description="Number of seconds the client should honor the HSTS setting.")    
    ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = Field(default="disable", description="Indicate that HSTS header applies to all subdomains.")    
    monitor: list[Monitor] = Field(default=None, description="Name of the health check monitor to use when polling to determine a virtual server's connectivity status.")    
    max_embryonic_connections: int | None = Field(ge=0, le=100000, default=1000, description="Maximum number of incomplete connections.")    
    embedded_ipv4_address: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of the lower 32 bits of the external IPv6 address as mapped IPv4 address.")    
    ipv4_mappedip: str | None = Field(default="", description="Range of mapped IP addresses. Specify the start IP address followed by a space and the end IP address.")    
    ipv4_mappedport: str | None = Field(default="", description="IPv4 port number range on the destination network to which the external port number range is mapped.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('ssl_hpkp_primary')
    @classmethod
    def validate_ssl_hpkp_primary(cls, v: Any) -> Any:
        """
        Validate ssl_hpkp_primary field.
        
        Datasource: ['vpn.certificate.local.name', 'vpn.certificate.ca.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('ssl_hpkp_backup')
    @classmethod
    def validate_ssl_hpkp_backup(cls, v: Any) -> Any:
        """
        Validate ssl_hpkp_backup field.
        
        Datasource: ['vpn.certificate.local.name', 'vpn.certificate.ca.name']
        
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
    async def validate_ssl_certificate_references(self, client: Any) -> list[str]:
        """
        Validate ssl_certificate references exist in FortiGate.
        
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
            >>> policy = Vip6Model(
            ...     ssl_certificate=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.vip6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ssl_certificate", [])
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
                    f"Ssl-Certificate '{value}' not found in "
                    "vpn/certificate/local"
                )        
        return errors    
    async def validate_ssl_hpkp_primary_references(self, client: Any) -> list[str]:
        """
        Validate ssl_hpkp_primary references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        - vpn/certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Vip6Model(
            ...     ssl_hpkp_primary="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_hpkp_primary_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.vip6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssl_hpkp_primary", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        elif await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssl-Hpkp-Primary '{value}' not found in "
                "vpn/certificate/local or vpn/certificate/ca"
            )        
        return errors    
    async def validate_ssl_hpkp_backup_references(self, client: Any) -> list[str]:
        """
        Validate ssl_hpkp_backup references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/certificate/local        - vpn/certificate/ca        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Vip6Model(
            ...     ssl_hpkp_backup="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ssl_hpkp_backup_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.vip6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "ssl_hpkp_backup", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.certificate.local.exists(value):
            found = True
        elif await client.api.cmdb.vpn.certificate.ca.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Ssl-Hpkp-Backup '{value}' not found in "
                "vpn/certificate/local or vpn/certificate/ca"
            )        
        return errors    
    async def validate_monitor_references(self, client: Any) -> list[str]:
        """
        Validate monitor references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/ldb-monitor        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Vip6Model(
            ...     monitor=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_monitor_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.vip6.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "monitor", [])
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
            if await client.api.cmdb.firewall.ldb-monitor.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Monitor '{value}' not found in "
                    "firewall/ldb-monitor"
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
        
        errors = await self.validate_ssl_certificate_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssl_hpkp_primary_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ssl_hpkp_backup_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_monitor_references(client)
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
    "Vip6Model",    "Vip6SrcFilter",    "Vip6Quic",    "Vip6Realservers",    "Vip6SslCertificate",    "Vip6SslCipherSuites",    "Vip6SslServerCipherSuites",    "Vip6Monitor",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.445029Z
# ============================================================================
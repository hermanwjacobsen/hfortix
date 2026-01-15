"""
Pydantic Models for CMDB - firewall/profile_protocol_options

Runtime validation models for firewall/profile_protocol_options configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileProtocolOptionsHttp(BaseModel):
    """
    Child table model for http.
    
    Configure HTTP protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 80).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    inspect_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the inspection of all ports for the protocol.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    comfort_interval: int | None = Field(ge=1, le=900, default=10, description="Interval between successive transmissions of data for client comforting (seconds).")    
    comfort_amount: int | None = Field(ge=1, le=65535, default=1, description="Number of bytes to send in each transmission for client comforting (bytes).")    
    range_block: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable blocking of partial downloads.")    
    strip_x_forwarded_for: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable stripping of HTTP X-Forwarded-For header.")    
    post_lang: list[PostLang] = Field(default="", description="ID codes for character sets to be used to convert to UTF-8 for banned words and DLP on HTTP posts (maximum of 5 character sets).")    
    streaming_content_bypass: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable bypassing of streaming content from buffering.")    
    switching_protocols: Literal["bypass", "block"] | None = Field(default="bypass", description="Bypass from scanning, or block a connection that attempts to switch protocol.")    
    unknown_http_version: Literal["reject", "tunnel", "best-effort"] | None = Field(default="reject", description="How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.")    
    http_0.9: Literal["allow", "block"] | None = Field(default="allow", description="Configure action to take upon receipt of HTTP 0.9 request.")    
    tunnel_non_http: Literal["enable", "disable"] | None = Field(default="enable", description="Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. Can occur if an application sends non-HTTP traffic using an HTTP destination port.")    
    h2c: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable h2c HTTP connection upgrade.")    
    unknown_content_encoding: Literal["block", "inspect", "bypass"] | None = Field(default="block", description="Configure the action the FortiGate unit will take on unknown content-encoding.")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    stream_based_uncompressed_limit: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0, default = 0).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")    
    verify_dns_for_policy_matching: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable verification of DNS for policy matching.")    
    block_page_status_code: int | None = Field(ge=100, le=599, default=403, description="Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403).")    
    retry_count: int | None = Field(ge=0, le=100, default=0, description="Number of attempts to retry HTTP connection (0 - 100, default = 0).")    
    domain_fronting: DomainFrontingEnum | None = Field(default="block", description="Configure HTTP domain fronting (default = block).")    
    tcp_window_type: TcpWindowTypeEnum | None = Field(default="auto-tuning", description="TCP window type to use for this protocol.")    
    tcp_window_minimum: int | None = Field(ge=65536, le=1048576, default=131072, description="Minimum dynamic TCP window size.")    
    tcp_window_maximum: int | None = Field(ge=1048576, le=16777216, default=8388608, description="Maximum dynamic TCP window size.")    
    tcp_window_size: int | None = Field(ge=65536, le=16777216, default=262144, description="Set TCP static window size.")    
    ssl_offloaded: Literal["no", "yes"] | None = Field(default="no", description="SSL decryption and encryption performed by an external device.")    
    address_ip_rating: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IP based URL rating.")
class ProfileProtocolOptionsFtp(BaseModel):
    """
    Child table model for ftp.
    
    Configure FTP protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 21).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    inspect_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the inspection of all ports for the protocol.")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    comfort_interval: int | None = Field(ge=1, le=900, default=10, description="Interval between successive transmissions of data for client comforting (seconds).")    
    comfort_amount: int | None = Field(ge=1, le=65535, default=1, description="Number of bytes to send in each transmission for client comforting (bytes).")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    stream_based_uncompressed_limit: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0, default = 0).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")    
    tcp_window_type: TcpWindowTypeEnum | None = Field(default="auto-tuning", description="TCP window type to use for this protocol.")    
    tcp_window_minimum: int | None = Field(ge=65536, le=1048576, default=131072, description="Minimum dynamic TCP window size.")    
    tcp_window_maximum: int | None = Field(ge=1048576, le=16777216, default=8388608, description="Maximum dynamic TCP window size.")    
    tcp_window_size: int | None = Field(ge=65536, le=16777216, default=262144, description="Set TCP static window size.")    
    ssl_offloaded: Literal["no", "yes"] | None = Field(default="no", description="SSL decryption and encryption performed by an external device.")    
    explicit_ftp_tls: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable FTP redirection for explicit FTPS.")
class ProfileProtocolOptionsImap(BaseModel):
    """
    Child table model for imap.
    
    Configure IMAP protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 143).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    inspect_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the inspection of all ports for the protocol.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")    
    ssl_offloaded: Literal["no", "yes"] | None = Field(default="no", description="SSL decryption and encryption performed by an external device.")
class ProfileProtocolOptionsMapi(BaseModel):
    """
    Child table model for mapi.
    
    Configure MAPI protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 135).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")
class ProfileProtocolOptionsPop3(BaseModel):
    """
    Child table model for pop3.
    
    Configure POP3 protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 110).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    inspect_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the inspection of all ports for the protocol.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")    
    ssl_offloaded: Literal["no", "yes"] | None = Field(default="no", description="SSL decryption and encryption performed by an external device.")
class ProfileProtocolOptionsSmtp(BaseModel):
    """
    Child table model for smtp.
    
    Configure SMTP protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 25).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    inspect_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the inspection of all ports for the protocol.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")    
    server_busy: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable SMTP server busy when server not available.")    
    ssl_offloaded: Literal["no", "yes"] | None = Field(default="no", description="SSL decryption and encryption performed by an external device.")
class ProfileProtocolOptionsNntp(BaseModel):
    """
    Child table model for nntp.
    
    Configure NNTP protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 119).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    inspect_all: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable the inspection of all ports for the protocol.")    
    proxy_after_tcp_handshake: Literal["enable", "disable"] | None = Field(default="disable", description="Proxy traffic after the TCP 3-way handshake has been established (not before).")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")
class ProfileProtocolOptionsSsh(BaseModel):
    """
    Child table model for ssh.
    
    Configure SFTP and SCP protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    comfort_interval: int | None = Field(ge=1, le=900, default=10, description="Interval between successive transmissions of data for client comforting (seconds).")    
    comfort_amount: int | None = Field(ge=1, le=65535, default=1, description="Number of bytes to send in each transmission for client comforting (bytes).")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    stream_based_uncompressed_limit: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0, default = 0).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")    
    tcp_window_type: TcpWindowTypeEnum | None = Field(default="auto-tuning", description="TCP window type to use for this protocol.")    
    tcp_window_minimum: int | None = Field(ge=65536, le=1048576, default=131072, description="Minimum dynamic TCP window size.")    
    tcp_window_maximum: int | None = Field(ge=1048576, le=16777216, default=8388608, description="Maximum dynamic TCP window size.")    
    tcp_window_size: int | None = Field(ge=65536, le=16777216, default=262144, description="Set TCP static window size.")    
    ssl_offloaded: Literal["no", "yes"] | None = Field(default="no", description="SSL decryption and encryption performed by an external device.")
class ProfileProtocolOptionsDns(BaseModel):
    """
    Child table model for dns.
    
    Configure DNS protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 53).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")
class ProfileProtocolOptionsCifs(BaseModel):
    """
    Child table model for cifs.
    
    Configure CIFS protocol options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    ports: list[Ports] = Field(ge=1, le=65535, default="", description="Ports to scan for content (1 - 65535, default = 445).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the active status of scanning for this protocol.")    
    options: list[Options] = Field(default="", description="One or more options that can be applied to the session.")    
    oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory file size that can be scanned (MB).")    
    uncompressed_oversize_limit: int | None = Field(ge=1, le=4095, default=10, description="Maximum in-memory uncompressed file size that can be scanned (MB).")    
    uncompressed_nest_limit: int | None = Field(ge=2, le=100, default=12, description="Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).")    
    scan_bzip2: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable scanning of BZip2 compressed files.")    
    tcp_window_type: TcpWindowTypeEnum | None = Field(default="auto-tuning", description="TCP window type to use for this protocol.")    
    tcp_window_minimum: int | None = Field(ge=65536, le=1048576, default=131072, description="Minimum dynamic TCP window size.")    
    tcp_window_maximum: int | None = Field(ge=1048576, le=16777216, default=8388608, description="Maximum dynamic TCP window size.")    
    tcp_window_size: int | None = Field(ge=65536, le=16777216, default=262144, description="Set TCP static window size.")    
    server_credential_type: Literal["none", "credential-replication", "credential-keytab"] = Field(default="none", description="CIFS server credential type.")    
    domain_controller: str = Field(max_length=63, default="", description="Domain for which to decrypt CIFS traffic.")  # datasource: ['user.domain-controller.name', 'credential-store.domain-controller.server-name']    
    server_keytab: list[ServerKeytab] = Field(default=None, description="Server keytab.")
class ProfileProtocolOptionsMailSignature(BaseModel):
    """
    Child table model for mail-signature.
    
    Configure Mail signature.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable adding an email signature to SMTP email messages as they pass through the FortiGate.")    
    signature: str | None = Field(max_length=1023, default="", description="Email signature to be added to outgoing email (if the signature contains spaces, enclose with quotation marks).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileProtocolOptionsModel(BaseModel):
    """
    Pydantic model for firewall/profile_protocol_options configuration.
    
    Configure protocol options.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - replacemsg_group: max_length=35 pattern=        - oversize_log: pattern=        - switching_protocols_log: pattern=        - http: pattern=        - ftp: pattern=        - imap: pattern=        - mapi: pattern=        - pop3: pattern=        - smtp: pattern=        - nntp: pattern=        - ssh: pattern=        - dns: pattern=        - cifs: pattern=        - mail_signature: pattern=        - rpc_over_http: pattern=    """
    
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
    replacemsg_group: str | None = Field(max_length=35, default="", description="Name of the replacement message group to be used.")  # datasource: ['system.replacemsg-group.name']    
    oversize_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging for antivirus oversize file blocking.")    
    switching_protocols_log: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging for HTTP/HTTPS switching protocols.")    
    http: list[Http] = Field(default=None, description="Configure HTTP protocol options.")    
    ftp: list[Ftp] = Field(default=None, description="Configure FTP protocol options.")    
    imap: list[Imap] = Field(default=None, description="Configure IMAP protocol options.")    
    mapi: list[Mapi] = Field(default=None, description="Configure MAPI protocol options.")    
    pop3: list[Pop3] = Field(default=None, description="Configure POP3 protocol options.")    
    smtp: list[Smtp] = Field(default=None, description="Configure SMTP protocol options.")    
    nntp: list[Nntp] = Field(default=None, description="Configure NNTP protocol options.")    
    ssh: list[Ssh] = Field(default=None, description="Configure SFTP and SCP protocol options.")    
    dns: list[Dns] = Field(default=None, description="Configure DNS protocol options.")    
    cifs: list[Cifs] = Field(default=None, description="Configure CIFS protocol options.")    
    mail_signature: list[MailSignature] = Field(default=None, description="Configure Mail signature.")    
    rpc_over_http: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable inspection of RPC over HTTP.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('replacemsg_group')
    @classmethod
    def validate_replacemsg_group(cls, v: Any) -> Any:
        """
        Validate replacemsg_group field.
        
        Datasource: ['system.replacemsg-group.name']
        
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
    async def validate_replacemsg_group_references(self, client: Any) -> list[str]:
        """
        Validate replacemsg_group references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/replacemsg-group        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileProtocolOptionsModel(
            ...     replacemsg_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_replacemsg_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_protocol_options.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "replacemsg_group", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.replacemsg-group.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Replacemsg-Group '{value}' not found in "
                "system/replacemsg-group"
            )        
        return errors    
    async def validate_cifs_references(self, client: Any) -> list[str]:
        """
        Validate cifs references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/domain-controller        - credential-store/domain-controller        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileProtocolOptionsModel(
            ...     cifs=[{"domain-controller": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_cifs_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.profile_protocol_options.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "cifs", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("domain-controller")
            else:
                value = getattr(item, "domain-controller", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.domain-controller.exists(value):
                found = True
            elif await client.api.cmdb.credential-store.domain-controller.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Cifs '{value}' not found in "
                    "user/domain-controller or credential-store/domain-controller"
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
        
        errors = await self.validate_replacemsg_group_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_cifs_references(client)
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
    "ProfileProtocolOptionsModel",    "ProfileProtocolOptionsHttp",    "ProfileProtocolOptionsFtp",    "ProfileProtocolOptionsImap",    "ProfileProtocolOptionsMapi",    "ProfileProtocolOptionsPop3",    "ProfileProtocolOptionsSmtp",    "ProfileProtocolOptionsNntp",    "ProfileProtocolOptionsSsh",    "ProfileProtocolOptionsDns",    "ProfileProtocolOptionsCifs",    "ProfileProtocolOptionsMailSignature",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.127425Z
# ============================================================================
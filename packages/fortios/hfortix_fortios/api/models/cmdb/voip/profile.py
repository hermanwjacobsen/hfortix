"""
Pydantic Models for CMDB - voip/profile

Runtime validation models for voip/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileSip(BaseModel):
    """
    Child table model for sip.
    
    SIP.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SIP.")    
    rtp: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable create pinholes for RTP traffic to traverse firewall.")    
    nat_port_range: str | None = Field(default="5117-65533", description="RTP NAT port range.")    
    open_register_pinhole: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable open pinhole for REGISTER Contact port.")    
    open_contact_pinhole: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable open pinhole for non-REGISTER Contact port.")    
    strict_register: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable only allow the registrar to connect.")    
    register_rate: int | None = Field(ge=0, le=4294967295, default=0, description="REGISTER request rate limit (per second, per policy).")    
    register_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    invite_rate: int | None = Field(ge=0, le=4294967295, default=0, description="INVITE request rate limit (per second, per policy).")    
    invite_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    max_dialogs: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number of concurrent calls/dialogs (per policy).")    
    max_line_length: int | None = Field(ge=78, le=4096, default=998, description="Maximum SIP header line length (78-4096).")    
    block_long_lines: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable block requests with headers exceeding max-line-length.")    
    block_unknown: Literal["disable", "enable"] | None = Field(default="enable", description="Block unrecognized SIP requests (enabled by default).")    
    call_keepalive: int | None = Field(ge=0, le=10080, default=0, description="Continue tracking calls with no RTP for this many minutes.")    
    block_ack: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block ACK requests.")    
    block_bye: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block BYE requests.")    
    block_cancel: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block CANCEL requests.")    
    block_info: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block INFO requests.")    
    block_invite: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block INVITE requests.")    
    block_message: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block MESSAGE requests.")    
    block_notify: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block NOTIFY requests.")    
    block_options: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.")    
    block_prack: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block prack requests.")    
    block_publish: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block PUBLISH requests.")    
    block_refer: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block REFER requests.")    
    block_register: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block REGISTER requests.")    
    block_subscribe: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block SUBSCRIBE requests.")    
    block_update: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block UPDATE requests.")    
    register_contact_trace: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable trace original IP/port within the contact header of REGISTER requests.")    
    open_via_pinhole: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable open pinhole for Via port.")    
    open_record_route_pinhole: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable open pinhole for Record-Route port.")    
    rfc2543_branch: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable support via branch compliant with RFC 2543.")    
    log_violations: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of SIP violations.")    
    log_call_summary: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable logging of SIP call summary.")    
    nat_trace: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable preservation of original IP in SDP i line.")    
    subscribe_rate: int | None = Field(ge=0, le=4294967295, default=0, description="SUBSCRIBE request rate limit (per second, per policy).")    
    subscribe_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    message_rate: int | None = Field(ge=0, le=4294967295, default=0, description="MESSAGE request rate limit (per second, per policy).")    
    message_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    notify_rate: int | None = Field(ge=0, le=4294967295, default=0, description="NOTIFY request rate limit (per second, per policy).")    
    notify_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    refer_rate: int | None = Field(ge=0, le=4294967295, default=0, description="REFER request rate limit (per second, per policy).")    
    refer_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    update_rate: int | None = Field(ge=0, le=4294967295, default=0, description="UPDATE request rate limit (per second, per policy).")    
    update_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    options_rate: int | None = Field(ge=0, le=4294967295, default=0, description="OPTIONS request rate limit (per second, per policy).")    
    options_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    ack_rate: int | None = Field(ge=0, le=4294967295, default=0, description="ACK request rate limit (per second, per policy).")    
    ack_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    prack_rate: int | None = Field(ge=0, le=4294967295, default=0, description="PRACK request rate limit (per second, per policy).")    
    prack_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    info_rate: int | None = Field(ge=0, le=4294967295, default=0, description="INFO request rate limit (per second, per policy).")    
    info_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    publish_rate: int | None = Field(ge=0, le=4294967295, default=0, description="PUBLISH request rate limit (per second, per policy).")    
    publish_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    bye_rate: int | None = Field(ge=0, le=4294967295, default=0, description="BYE request rate limit (per second, per policy).")    
    bye_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    cancel_rate: int | None = Field(ge=0, le=4294967295, default=0, description="CANCEL request rate limit (per second, per policy).")    
    cancel_rate_track: Literal["none", "src-ip", "dest-ip"] | None = Field(default="none", description="Track the packet protocol field.")    
    preserve_override: Literal["disable", "enable"] | None = Field(default="disable", description="Override i line to preserve original IPs (default: append).")    
    no_sdp_fixup: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable no SDP fix-up.")    
    contact_fixup: Literal["disable", "enable"] | None = Field(default="enable", description="Fixup contact anyway even if contact's IP:port doesn't match session's IP:port.")    
    max_idle_dialogs: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum number established but idle dialogs to retain (per policy).")    
    block_geo_red_options: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.")    
    hosted_nat_traversal: Literal["disable", "enable"] | None = Field(default="disable", description="Hosted NAT Traversal (HNT).")    
    hnt_restrict_source_ip: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.")    
    call_id_regex: str | None = Field(max_length=511, default=None, description="Validate PCRE regular expression for Call-Id header value.")    
    content_type_regex: str | None = Field(max_length=511, default=None, description="Validate PCRE regular expression for Content-Type header value.")    
    max_body_length: int | None = Field(ge=0, le=4294967295, default=0, description="Maximum SIP message body length (0 meaning no limit).")    
    unknown_header: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for unknown SIP header.")    
    malformed_request_line: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed request line.")    
    malformed_header_via: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed VIA header.")    
    malformed_header_from: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed From header.")    
    malformed_header_to: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed To header.")    
    malformed_header_call_id: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Call-ID header.")    
    malformed_header_cseq: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed CSeq header.")    
    malformed_header_rack: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed RAck header.")    
    malformed_header_rseq: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed RSeq header.")    
    malformed_header_contact: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Contact header.")    
    malformed_header_record_route: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Record-Route header.")    
    malformed_header_route: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Route header.")    
    malformed_header_expires: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Expires header.")    
    malformed_header_content_type: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Content-Type header.")    
    malformed_header_content_length: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Content-Length header.")    
    malformed_header_max_forwards: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Max-Forwards header.")    
    malformed_header_allow: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed Allow header.")    
    malformed_header_p_asserted_identity: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed P-Asserted-Identity header.")    
    malformed_header_no_require: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SIP messages without Require header.")    
    malformed_header_no_proxy_require: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SIP messages without Proxy-Require header.")    
    malformed_header_sdp_v: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP v line.")    
    malformed_header_sdp_o: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP o line.")    
    malformed_header_sdp_s: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP s line.")    
    malformed_header_sdp_i: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP i line.")    
    malformed_header_sdp_c: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP c line.")    
    malformed_header_sdp_b: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP b line.")    
    malformed_header_sdp_z: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP z line.")    
    malformed_header_sdp_k: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP k line.")    
    malformed_header_sdp_a: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP a line.")    
    malformed_header_sdp_t: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP t line.")    
    malformed_header_sdp_r: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP r line.")    
    malformed_header_sdp_m: Literal["discard", "pass", "respond"] | None = Field(default="pass", description="Action for malformed SDP m line.")    
    provisional_invite_expiry_time: int | None = Field(ge=10, le=3600, default=210, description="Expiry time (10-3600, in seconds) for provisional INVITE.")    
    ips_rtp: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable allow IPS on RTP.")    
    ssl_mode: Literal["off", "full"] | None = Field(default="off", description="SSL/TLS mode for encryption & decryption of traffic.")    
    ssl_send_empty_frags: Literal["enable", "disable"] | None = Field(default="enable", description="Send empty fragments to avoid attack on CBC IV (SSL 3.0 & TLS 1.0 only).")    
    ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = Field(default="allow", description="Allow/block client renegotiation by server.")    
    ssl_algorithm: Literal["high", "medium", "low"] | None = Field(default="high", description="Relative strength of encryption algorithms accepted in negotiation.")    
    ssl_pfs: Literal["require", "deny", "allow"] | None = Field(default="allow", description="SSL Perfect Forward Secrecy.")    
    ssl_min_version: SslMinVersionEnum | None = Field(default="tls-1.1", description="Lowest SSL/TLS version to negotiate.")    
    ssl_max_version: SslMaxVersionEnum | None = Field(default="tls-1.3", description="Highest SSL/TLS version to negotiate.")    
    ssl_client_certificate: str | None = Field(max_length=35, default="", description="Name of Certificate to offer to server if requested.")  # datasource: ['vpn.certificate.local.name']    
    ssl_server_certificate: str = Field(max_length=35, default="", description="Name of Certificate return to the client in every SSL connection.")  # datasource: ['vpn.certificate.local.name']    
    ssl_auth_client: str | None = Field(max_length=35, default="", description="Require a client certificate and authenticate it with the peer/peergrp.")  # datasource: ['user.peer.name', 'user.peergrp.name']    
    ssl_auth_server: str | None = Field(max_length=35, default="", description="Authenticate the server's certificate with the peer/peergrp.")  # datasource: ['user.peer.name', 'user.peergrp.name']
class ProfileSccp(BaseModel):
    """
    Child table model for sccp.
    
    SCCP.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable SCCP.")    
    block_mcast: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable block multicast RTP connections.")    
    verify_header: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable verify SCCP header content.")    
    log_call_summary: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable log summary of SCCP calls.")    
    log_violations: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable logging of SCCP violations.")    
    max_calls: int | None = Field(ge=0, le=65535, default=0, description="Maximum calls per minute per SCCP client (max 65535).")
class ProfileMsrp(BaseModel):
    """
    Child table model for msrp.
    
    MSRP.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable MSRP.")    
    log_violations: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable logging of MSRP violations.")    
    max_msg_size: int | None = Field(ge=0, le=65535, default=0, description="Maximum allowable MSRP message size (1-65535).")    
    max_msg_size_action: MaxMsgSizeActionEnum | None = Field(default="pass", description="Action for violation of max-msg-size.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for voip/profile configuration.
    
    Configure VoIP profiles.
    
    Validation Rules:        - name: max_length=47 pattern=        - feature_set: pattern=        - comment: max_length=255 pattern=        - sip: pattern=        - sccp: pattern=        - msrp: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=47, default="", description="Profile name.")    
    feature_set: Literal["ips", "voipd"] | None = Field(default="voipd", description="IPS or voipd (SIP-ALG) inspection feature set.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    sip: list[Sip] = Field(default=None, description="SIP.")    
    sccp: list[Sccp] = Field(default=None, description="SCCP.")    
    msrp: list[Msrp] = Field(default=None, description="MSRP.")    
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
    async def validate_sip_references(self, client: Any) -> list[str]:
        """
        Validate sip references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - user/peer        - user/peergrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     sip=[{"ssl-auth-server": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_sip_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.voip.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "sip", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("ssl-auth-server")
            else:
                value = getattr(item, "ssl-auth-server", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.user.peer.exists(value):
                found = True
            elif await client.api.cmdb.user.peergrp.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Sip '{value}' not found in "
                    "user/peer or user/peergrp"
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
        
        errors = await self.validate_sip_references(client)
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
    "ProfileModel",    "ProfileSip",    "ProfileSccp",    "ProfileMsrp",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.739410Z
# ============================================================================
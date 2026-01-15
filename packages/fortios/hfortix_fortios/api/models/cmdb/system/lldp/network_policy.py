"""
Pydantic Models for CMDB - system/lldp/network_policy

Runtime validation models for system/lldp/network_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class NetworkPolicyVoice(BaseModel):
    """
    Child table model for voice.
    
    Voice.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
class NetworkPolicyVoiceSignaling(BaseModel):
    """
    Child table model for voice-signaling.
    
    Voice signaling.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
class NetworkPolicyGuest(BaseModel):
    """
    Child table model for guest.
    
    Guest.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
class NetworkPolicyGuestVoiceSignaling(BaseModel):
    """
    Child table model for guest-voice-signaling.
    
    Guest Voice Signaling.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
class NetworkPolicySoftphone(BaseModel):
    """
    Child table model for softphone.
    
    Softphone.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
class NetworkPolicyVideoConferencing(BaseModel):
    """
    Child table model for video-conferencing.
    
    Video Conferencing.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
class NetworkPolicyStreamingVideo(BaseModel):
    """
    Child table model for streaming-video.
    
    Streaming Video.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
class NetworkPolicyVideoSignaling(BaseModel):
    """
    Child table model for video-signaling.
    
    Video Signaling.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    status: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable advertising this policy.")    
    tag: Literal["none", "dot1q", "dot1p"] | None = Field(default="none", description="Advertise tagged or untagged traffic.")    
    vlan: int = Field(ge=1, le=4094, default=0, description="802.1Q VLAN ID to advertise (1 - 4094).")    
    priority: int | None = Field(ge=0, le=7, default=5, description="802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).")    
    dscp: int | None = Field(ge=0, le=63, default=46, description="Differentiated Services Code Point (DSCP) value to advertise.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class NetworkPolicyModel(BaseModel):
    """
    Pydantic model for system/lldp/network_policy configuration.
    
    Configure LLDP network policy.
    
    Validation Rules:        - name: max_length=35 pattern=        - comment: max_length=1023 pattern=        - voice: pattern=        - voice_signaling: pattern=        - guest: pattern=        - guest_voice_signaling: pattern=        - softphone: pattern=        - video_conferencing: pattern=        - streaming_video: pattern=        - video_signaling: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="LLDP network policy name.")    
    comment: str | None = Field(max_length=1023, default=None, description="Comment.")    
    voice: list[Voice] = Field(default=None, description="Voice.")    
    voice_signaling: list[VoiceSignaling] = Field(default=None, description="Voice signaling.")    
    guest: list[Guest] = Field(default=None, description="Guest.")    
    guest_voice_signaling: list[GuestVoiceSignaling] = Field(default=None, description="Guest Voice Signaling.")    
    softphone: list[Softphone] = Field(default=None, description="Softphone.")    
    video_conferencing: list[VideoConferencing] = Field(default=None, description="Video Conferencing.")    
    streaming_video: list[StreamingVideo] = Field(default=None, description="Streaming Video.")    
    video_signaling: list[VideoSignaling] = Field(default=None, description="Video Signaling.")    
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
    "NetworkPolicyModel",    "NetworkPolicyVoice",    "NetworkPolicyVoiceSignaling",    "NetworkPolicyGuest",    "NetworkPolicyGuestVoiceSignaling",    "NetworkPolicySoftphone",    "NetworkPolicyVideoConferencing",    "NetworkPolicyStreamingVideo",    "NetworkPolicyVideoSignaling",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:18.093925Z
# ============================================================================
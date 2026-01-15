"""
Pydantic Models for CMDB - system/replacemsg_group

Runtime validation models for system/replacemsg_group configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ReplacemsgGroupMail(BaseModel):
    """
    Child table model for mail.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupHttp(BaseModel):
    """
    Child table model for http.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupWebproxy(BaseModel):
    """
    Child table model for webproxy.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupFtp(BaseModel):
    """
    Child table model for ftp.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupFortiguardWf(BaseModel):
    """
    Child table model for fortiguard-wf.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupSpam(BaseModel):
    """
    Child table model for spam.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupAlertmail(BaseModel):
    """
    Child table model for alertmail.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupAdmin(BaseModel):
    """
    Child table model for admin.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupAuth(BaseModel):
    """
    Child table model for auth.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupSslvpn(BaseModel):
    """
    Child table model for sslvpn.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupNacQuar(BaseModel):
    """
    Child table model for nac-quar.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupTrafficQuota(BaseModel):
    """
    Child table model for traffic-quota.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupUtm(BaseModel):
    """
    Child table model for utm.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupCustomMessage(BaseModel):
    """
    Child table model for custom-message.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupIcap(BaseModel):
    """
    Child table model for icap.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
class ReplacemsgGroupAutomation(BaseModel):
    """
    Child table model for automation.
    
    Replacement message table entries.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    msg_type: str = Field(max_length=28, default="", description="Message type.")    
    buffer: str | None = Field(max_length=32768, default=None, description="Message string.")    
    header: Literal["none", "http", "8bit"] | None = Field(default="none", description="Header flag.")    
    format: Literal["none", "text", "html"] | None = Field(default="none", description="Format flag.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ReplacemsgGroupModel(BaseModel):
    """
    Pydantic model for system/replacemsg_group configuration.
    
    Configure replacement message groups.
    
    Validation Rules:        - name: max_length=35 pattern=        - comment: max_length=255 pattern=        - group_type: pattern=        - mail: pattern=        - http: pattern=        - webproxy: pattern=        - ftp: pattern=        - fortiguard_wf: pattern=        - spam: pattern=        - alertmail: pattern=        - admin: pattern=        - auth: pattern=        - sslvpn: pattern=        - nac_quar: pattern=        - traffic_quota: pattern=        - utm: pattern=        - custom_message: pattern=        - icap: pattern=        - automation: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Group name.")    
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    group_type: Literal["default", "utm", "auth"] = Field(default="default", description="Group type.")    
    mail: list[Mail] = Field(default=None, description="Replacement message table entries.")    
    http: list[Http] = Field(default=None, description="Replacement message table entries.")    
    webproxy: list[Webproxy] = Field(default=None, description="Replacement message table entries.")    
    ftp: list[Ftp] = Field(default=None, description="Replacement message table entries.")    
    fortiguard_wf: list[FortiguardWf] = Field(default=None, description="Replacement message table entries.")    
    spam: list[Spam] = Field(default=None, description="Replacement message table entries.")    
    alertmail: list[Alertmail] = Field(default=None, description="Replacement message table entries.")    
    admin: list[Admin] = Field(default=None, description="Replacement message table entries.")    
    auth: list[Auth] = Field(default=None, description="Replacement message table entries.")    
    sslvpn: list[Sslvpn] = Field(default=None, description="Replacement message table entries.")    
    nac_quar: list[NacQuar] = Field(default=None, description="Replacement message table entries.")    
    traffic_quota: list[TrafficQuota] = Field(default=None, description="Replacement message table entries.")    
    utm: list[Utm] = Field(default=None, description="Replacement message table entries.")    
    custom_message: list[CustomMessage] = Field(default=None, description="Replacement message table entries.")    
    icap: list[Icap] = Field(default=None, description="Replacement message table entries.")    
    automation: list[Automation] = Field(default=None, description="Replacement message table entries.")    
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
    "ReplacemsgGroupModel",    "ReplacemsgGroupMail",    "ReplacemsgGroupHttp",    "ReplacemsgGroupWebproxy",    "ReplacemsgGroupFtp",    "ReplacemsgGroupFortiguardWf",    "ReplacemsgGroupSpam",    "ReplacemsgGroupAlertmail",    "ReplacemsgGroupAdmin",    "ReplacemsgGroupAuth",    "ReplacemsgGroupSslvpn",    "ReplacemsgGroupNacQuar",    "ReplacemsgGroupTrafficQuota",    "ReplacemsgGroupUtm",    "ReplacemsgGroupCustomMessage",    "ReplacemsgGroupIcap",    "ReplacemsgGroupAutomation",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.072886Z
# ============================================================================
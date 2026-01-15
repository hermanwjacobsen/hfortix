"""
Pydantic Models for CMDB - log/threat_weight

Runtime validation models for log/threat_weight configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class ThreatWeightLevel(BaseModel):
    """
    Child table model for level.
    
    Score mapping for threat weight levels.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    low: int | None = Field(ge=1, le=100, default=5, description="Low level score value (1 - 100).")    
    medium: int | None = Field(ge=1, le=100, default=10, description="Medium level score value (1 - 100).")    
    high: int | None = Field(ge=1, le=100, default=30, description="High level score value (1 - 100).")    
    critical: int | None = Field(ge=1, le=100, default=50, description="Critical level score value (1 - 100).")
class ThreatWeightMalware(BaseModel):
    """
    Child table model for malware.
    
    Anti-virus malware threat weight settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    virus_infected: VirusInfectedEnum | None = Field(default="critical", description="Threat weight score for virus (infected) detected.")    
    inline_block: InlineBlockEnum | None = Field(default="critical", description="Threat weight score for malware detected by inline block.")    
    file_blocked: FileBlockedEnum | None = Field(default="low", description="Threat weight score for blocked file detected.")    
    command_blocked: CommandBlockedEnum | None = Field(default="disable", description="Threat weight score for blocked command detected.")    
    oversized: OversizedEnum | None = Field(default="disable", description="Threat weight score for oversized file detected.")    
    virus_scan_error: VirusScanErrorEnum | None = Field(default="high", description="Threat weight score for virus (scan error) detected.")    
    switch_proto: SwitchProtoEnum | None = Field(default="disable", description="Threat weight score for switch proto detected.")    
    mimefragmented: MimefragmentedEnum | None = Field(default="disable", description="Threat weight score for mimefragmented detected.")    
    virus_file_type_executable: VirusFileTypeExecutableEnum | None = Field(default="medium", description="Threat weight score for virus (file type executable) detected.")    
    virus_outbreak_prevention: VirusOutbreakPreventionEnum | None = Field(default="critical", description="Threat weight score for virus (outbreak prevention) event.")    
    content_disarm: ContentDisarmEnum | None = Field(default="medium", description="Threat weight score for virus (content disarm) detected.")    
    malware_list: MalwareListEnum | None = Field(default="medium", description="Threat weight score for virus (malware list) detected.")    
    ems_threat_feed: EmsThreatFeedEnum | None = Field(default="medium", description="Threat weight score for virus (EMS threat feed) detected.")    
    fsa_malicious: FsaMaliciousEnum | None = Field(default="critical", description="Threat weight score for FortiSandbox malicious malware detected.")    
    fsa_high_risk: FsaHighRiskEnum | None = Field(default="high", description="Threat weight score for FortiSandbox high risk malware detected.")    
    fsa_medium_risk: FsaMediumRiskEnum | None = Field(default="medium", description="Threat weight score for FortiSandbox medium risk malware detected.")
class ThreatWeightIps(BaseModel):
    """
    Child table model for ips.
    
    IPS threat weight settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    info_severity: InfoSeverityEnum | None = Field(default="disable", description="Threat weight score for IPS info severity events.")    
    low_severity: LowSeverityEnum | None = Field(default="low", description="Threat weight score for IPS low severity events.")    
    medium_severity: MediumSeverityEnum | None = Field(default="medium", description="Threat weight score for IPS medium severity events.")    
    high_severity: HighSeverityEnum | None = Field(default="high", description="Threat weight score for IPS high severity events.")    
    critical_severity: CriticalSeverityEnum | None = Field(default="critical", description="Threat weight score for IPS critical severity events.")
class ThreatWeightWeb(BaseModel):
    """
    Child table model for web.
    
    Web filtering threat weight settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=255, default=0, description="Entry ID.")    
    category: int = Field(ge=0, le=255, default=0, description="Threat weight score for web category filtering matches.")    
    level: LevelEnum | None = Field(default="low", description="Threat weight score for web category filtering matches.")
class ThreatWeightGeolocation(BaseModel):
    """
    Child table model for geolocation.
    
    Geolocation-based threat weight settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=255, default=0, description="Entry ID.")    
    country: str = Field(max_length=2, default="", description="Country code.")    
    level: LevelEnum | None = Field(default="low", description="Threat weight score for Geolocation-based events.")
class ThreatWeightApplication(BaseModel):
    """
    Child table model for application.
    
    Application-control threat weight settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=255, default=0, description="Entry ID.")    
    category: int = Field(ge=0, le=65535, default=0, description="Application category.")    
    level: LevelEnum | None = Field(default="low", description="Threat weight score for Application events.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class ThreatWeightBlocked_connectionEnum(str, Enum):
    """Allowed values for blocked_connection field."""
    DISABLE = "disable"    LOW = "low"    MEDIUM = "medium"    HIGH = "high"    CRITICAL = "critical"
class ThreatWeightFailed_connectionEnum(str, Enum):
    """Allowed values for failed_connection field."""
    DISABLE = "disable"    LOW = "low"    MEDIUM = "medium"    HIGH = "high"    CRITICAL = "critical"
class ThreatWeightUrl_block_detectedEnum(str, Enum):
    """Allowed values for url_block_detected field."""
    DISABLE = "disable"    LOW = "low"    MEDIUM = "medium"    HIGH = "high"    CRITICAL = "critical"
class ThreatWeightBotnet_connection_detectedEnum(str, Enum):
    """Allowed values for botnet_connection_detected field."""
    DISABLE = "disable"    LOW = "low"    MEDIUM = "medium"    HIGH = "high"    CRITICAL = "critical"

# ============================================================================
# Main Model
# ============================================================================

class ThreatWeightModel(BaseModel):
    """
    Pydantic model for log/threat_weight configuration.
    
    Configure threat weight settings.
    
    Validation Rules:        - status: pattern=        - level: pattern=        - blocked_connection: pattern=        - failed_connection: pattern=        - url_block_detected: pattern=        - botnet_connection_detected: pattern=        - malware: pattern=        - ips: pattern=        - web: pattern=        - geolocation: pattern=        - application: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the threat weight feature.")    
    level: list[Level] = Field(default=None, description="Score mapping for threat weight levels.")    
    blocked_connection: BlockedConnectionEnum | None = Field(default="high", description="Threat weight score for blocked connections.")    
    failed_connection: FailedConnectionEnum | None = Field(default="low", description="Threat weight score for failed connections.")    
    url_block_detected: UrlBlockDetectedEnum | None = Field(default="high", description="Threat weight score for URL blocking.")    
    botnet_connection_detected: BotnetConnectionDetectedEnum | None = Field(default="critical", description="Threat weight score for detected botnet connections.")    
    malware: list[Malware] = Field(default=None, description="Anti-virus malware threat weight settings.")    
    ips: list[Ips] = Field(default=None, description="IPS threat weight settings.")    
    web: list[Web] = Field(default=None, description="Web filtering threat weight settings.")    
    geolocation: list[Geolocation] = Field(default=None, description="Geolocation-based threat weight settings.")    
    application: list[Application] = Field(default=None, description="Application-control threat weight settings.")    
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
    "ThreatWeightModel",    "ThreatWeightLevel",    "ThreatWeightMalware",    "ThreatWeightIps",    "ThreatWeightWeb",    "ThreatWeightGeolocation",    "ThreatWeightApplication",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.516288Z
# ============================================================================
"""
Pydantic Models for CMDB - antivirus/quarantine

Runtime validation models for antivirus/quarantine configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class QuarantineDrop_infectedEnum(str, Enum):
    """Allowed values for drop_infected field."""
    IMAP = "imap"    SMTP = "smtp"    POP3 = "pop3"    HTTP = "http"    FTP = "ftp"    NNTP = "nntp"    IMAPS = "imaps"    SMTPS = "smtps"    POP3S = "pop3s"    HTTPS = "https"    FTPS = "ftps"    MAPI = "mapi"    CIFS = "cifs"    SSH = "ssh"
class QuarantineStore_infectedEnum(str, Enum):
    """Allowed values for store_infected field."""
    IMAP = "imap"    SMTP = "smtp"    POP3 = "pop3"    HTTP = "http"    FTP = "ftp"    NNTP = "nntp"    IMAPS = "imaps"    SMTPS = "smtps"    POP3S = "pop3s"    HTTPS = "https"    FTPS = "ftps"    MAPI = "mapi"    CIFS = "cifs"    SSH = "ssh"
class QuarantineDrop_machine_learningEnum(str, Enum):
    """Allowed values for drop_machine_learning field."""
    IMAP = "imap"    SMTP = "smtp"    POP3 = "pop3"    HTTP = "http"    FTP = "ftp"    NNTP = "nntp"    IMAPS = "imaps"    SMTPS = "smtps"    POP3S = "pop3s"    HTTPS = "https"    FTPS = "ftps"    MAPI = "mapi"    CIFS = "cifs"    SSH = "ssh"
class QuarantineStore_machine_learningEnum(str, Enum):
    """Allowed values for store_machine_learning field."""
    IMAP = "imap"    SMTP = "smtp"    POP3 = "pop3"    HTTP = "http"    FTP = "ftp"    NNTP = "nntp"    IMAPS = "imaps"    SMTPS = "smtps"    POP3S = "pop3s"    HTTPS = "https"    FTPS = "ftps"    MAPI = "mapi"    CIFS = "cifs"    SSH = "ssh"

# ============================================================================
# Main Model
# ============================================================================

class QuarantineModel(BaseModel):
    """
    Pydantic model for antivirus/quarantine configuration.
    
    Configure quarantine options.
    
    Validation Rules:        - agelimit: min=0 max=479 pattern=        - maxfilesize: min=0 max=500 pattern=        - quarantine_quota: min=0 max=4294967295 pattern=        - drop_infected: pattern=        - store_infected: pattern=        - drop_machine_learning: pattern=        - store_machine_learning: pattern=        - lowspace: pattern=        - destination: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    agelimit: int | None = Field(ge=0, le=479, default=0, description="Age limit for quarantined files (0 - 479 hours, 0 means forever).")    
    maxfilesize: int | None = Field(ge=0, le=500, default=0, description="Maximum file size to quarantine (0 - 500 Mbytes, 0 means unlimited).")    
    quarantine_quota: int | None = Field(ge=0, le=4294967295, default=0, description="The amount of disk space to reserve for quarantining files (0 - 4294967295 Mbytes, 0 means unlimited and depends on disk space).")    
    drop_infected: list[DropInfected] = Field(default="", description="Do not quarantine infected files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.")    
    store_infected: list[StoreInfected] = Field(default="imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh", description="Quarantine infected files found in sessions using the selected protocols.")    
    drop_machine_learning: list[DropMachineLearning] = Field(default="", description="Do not quarantine files detected by machine learning found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.")    
    store_machine_learning: list[StoreMachineLearning] = Field(default="imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh", description="Quarantine files detected by machine learning found in sessions using the selected protocols.")    
    lowspace: Literal["drop-new", "ovrw-old"] | None = Field(default="ovrw-old", description="Select the method for handling additional files when running low on disk space.")    
    destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = Field(default="disk", description="Choose whether to quarantine files to the FortiGate disk or to FortiAnalyzer or to delete them instead of quarantining them.")    
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
    "QuarantineModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.477055Z
# ============================================================================
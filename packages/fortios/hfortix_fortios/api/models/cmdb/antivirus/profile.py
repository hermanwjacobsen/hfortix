"""
Pydantic Models for CMDB - antivirus/profile

Runtime validation models for antivirus/profile configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class ProfileHttp(BaseModel):
    """
    Child table model for http.
    
    Configure HTTP AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")    
    content_disarm: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.")
class ProfileFtp(BaseModel):
    """
    Child table model for ftp.
    
    Configure FTP AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")
class ProfileImap(BaseModel):
    """
    Child table model for imap.
    
    Configure IMAP AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")    
    executables: Literal["default", "virus"] | None = Field(default="default", description="Treat Windows executable files as viruses for the purpose of blocking or monitoring.")    
    content_disarm: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.")
class ProfilePop3(BaseModel):
    """
    Child table model for pop3.
    
    Configure POP3 AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")    
    executables: Literal["default", "virus"] | None = Field(default="default", description="Treat Windows executable files as viruses for the purpose of blocking or monitoring.")    
    content_disarm: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.")
class ProfileSmtp(BaseModel):
    """
    Child table model for smtp.
    
    Configure SMTP AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")    
    executables: Literal["default", "virus"] | None = Field(default="default", description="Treat Windows executable files as viruses for the purpose of blocking or monitoring.")    
    content_disarm: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.")
class ProfileMapi(BaseModel):
    """
    Child table model for mapi.
    
    Configure MAPI AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")    
    executables: Literal["default", "virus"] | None = Field(default="default", description="Treat Windows executable files as viruses for the purpose of blocking or monitoring.")
class ProfileNntp(BaseModel):
    """
    Child table model for nntp.
    
    Configure NNTP AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")
class ProfileCifs(BaseModel):
    """
    Child table model for cifs.
    
    Configure CIFS AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")
class ProfileSsh(BaseModel):
    """
    Child table model for ssh.
    
    Configure SFTP and SCP AntiVirus options.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    av_scan: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable AntiVirus scan service.")    
    outbreak_prevention: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable virus outbreak prevention service.")    
    external_blocklist: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable external-blocklist. Analyzes files including the content of archives.")    
    malware_stream: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable 0-day malware-stream scanning. Analyzes files including the content of archives.")    
    fortindr: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiNDR.")    
    fortisandbox: Literal["disable", "block", "monitor"] | None = Field(default="disable", description="Enable scanning of files by FortiSandbox.")    
    quarantine: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable quarantine for infected files.")    
    archive_block: list[ArchiveBlock] = Field(default="", description="Select the archive types to block.")    
    archive_log: list[ArchiveLog] = Field(default="", description="Select the archive types to log.")    
    emulator: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable the virus emulator.")
class ProfileNacQuar(BaseModel):
    """
    Child table model for nac-quar.
    
    Configure AntiVirus quarantine settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    infected: Literal["none", "quar-src-ip"] | None = Field(default="none", description="Enable/Disable quarantining infected hosts to the banned user list.")    
    expiry: str | None = Field(default="5m", description="Duration of quarantine.")    
    log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable AntiVirus quarantine logging.")
class ProfileContentDisarm(BaseModel):
    """
    Child table model for content-disarm.
    
    AV Content Disarm and Reconstruction settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    analytics_suspicious: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable using CDR as a secondary method for determining suspicous files for analytics.")    
    original_file_destination: Literal["fortisandbox", "quarantine", "discard"] | None = Field(default="discard", description="Destination to send original file if active content is removed.")    
    error_action: Literal["block", "log-only", "ignore"] | None = Field(default="log-only", description="Action to be taken if CDR engine encounters an unrecoverable error.")    
    office_macro: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable stripping of macros in Microsoft Office documents.")    
    office_hylink: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable stripping of hyperlinks in Microsoft Office documents.")    
    office_linked: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of linked objects in Microsoft Office documents.")    
    office_embed: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable stripping of embedded objects in Microsoft Office documents.")    
    office_dde: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of Dynamic Data Exchange events in Microsoft Office documents.")    
    office_action: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable stripping of PowerPoint action events in Microsoft Office documents.")    
    pdf_javacode: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of JavaScript code in PDF documents.")    
    pdf_embedfile: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable stripping of embedded files in PDF documents.")    
    pdf_hyperlink: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of hyperlinks from PDF documents.")    
    pdf_act_gotor: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable stripping of PDF document actions that access other PDF documents.")    
    pdf_act_launch: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable stripping of PDF document actions that launch other applications.")    
    pdf_act_sound: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of PDF document actions that play a sound.")    
    pdf_act_movie: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of PDF document actions that play a movie.")    
    pdf_act_java: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of PDF document actions that execute JavaScript code.")    
    pdf_act_form: Literal["disable", "enable"] | None = Field(default="", description="Enable/disable stripping of PDF document actions that submit data to other targets.")    
    cover_page: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable inserting a cover page into the disarmed document.")    
    detect_only: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable only detect disarmable files, do not alter content.")
class ProfileExternalBlocklist(BaseModel):
    """
    Child table model for external-blocklist.
    
    One or more external malware block lists.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="External blocklist.")  # datasource: ['system.external-resource.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class ProfileModel(BaseModel):
    """
    Pydantic model for antivirus/profile configuration.
    
    Configure AntiVirus profiles.
    
    Validation Rules:        - name: max_length=47 pattern=        - comment: max_length=255 pattern=        - replacemsg_group: max_length=35 pattern=        - feature_set: pattern=        - fortisandbox_mode: pattern=        - fortisandbox_max_upload: min=1 max=4095 pattern=        - analytics_ignore_filetype: min=0 max=4294967295 pattern=        - analytics_accept_filetype: min=0 max=4294967295 pattern=        - analytics_db: pattern=        - mobile_malware_db: pattern=        - http: pattern=        - ftp: pattern=        - imap: pattern=        - pop3: pattern=        - smtp: pattern=        - mapi: pattern=        - nntp: pattern=        - cifs: pattern=        - ssh: pattern=        - nac_quar: pattern=        - content_disarm: pattern=        - outbreak_prevention_archive_scan: pattern=        - external_blocklist_enable_all: pattern=        - external_blocklist: pattern=        - ems_threat_feed: pattern=        - fortindr_error_action: pattern=        - fortindr_timeout_action: pattern=        - fortisandbox_scan_timeout: min=30 max=180 pattern=        - fortisandbox_error_action: pattern=        - fortisandbox_timeout_action: pattern=        - av_virus_log: pattern=        - extended_log: pattern=        - scan_mode: pattern=    """
    
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
    comment: str | None = Field(max_length=255, default=None, description="Comment.")    
    replacemsg_group: str | None = Field(max_length=35, default="", description="Replacement message group customized for this profile.")  # datasource: ['system.replacemsg-group.name']    
    feature_set: Literal["flow", "proxy"] | None = Field(default="flow", description="Flow/proxy feature set.")    
    fortisandbox_mode: Literal["inline", "analytics-suspicious", "analytics-everything"] | None = Field(default="analytics-everything", description="FortiSandbox scan modes.")    
    fortisandbox_max_upload: int | None = Field(ge=1, le=4095, default=10, description="Maximum size of files that can be uploaded to FortiSandbox in Mbytes.")    
    analytics_ignore_filetype: int | None = Field(ge=0, le=4294967295, default=0, description="Do not submit files matching this DLP file-pattern to FortiSandbox (post-transfer scan only).")  # datasource: ['dlp.filepattern.id']    
    analytics_accept_filetype: int | None = Field(ge=0, le=4294967295, default=0, description="Only submit files matching this DLP file-pattern to FortiSandbox (post-transfer scan only).")  # datasource: ['dlp.filepattern.id']    
    analytics_db: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable using the FortiSandbox signature database to supplement the AV signature databases.")    
    mobile_malware_db: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable using the mobile malware signature database.")    
    http: list[Http] = Field(default=None, description="Configure HTTP AntiVirus options.")    
    ftp: list[Ftp] = Field(default=None, description="Configure FTP AntiVirus options.")    
    imap: list[Imap] = Field(default=None, description="Configure IMAP AntiVirus options.")    
    pop3: list[Pop3] = Field(default=None, description="Configure POP3 AntiVirus options.")    
    smtp: list[Smtp] = Field(default=None, description="Configure SMTP AntiVirus options.")    
    mapi: list[Mapi] = Field(default=None, description="Configure MAPI AntiVirus options.")    
    nntp: list[Nntp] = Field(default=None, description="Configure NNTP AntiVirus options.")    
    cifs: list[Cifs] = Field(default=None, description="Configure CIFS AntiVirus options.")    
    ssh: list[Ssh] = Field(default=None, description="Configure SFTP and SCP AntiVirus options.")    
    nac_quar: list[NacQuar] = Field(default=None, description="Configure AntiVirus quarantine settings.")    
    content_disarm: list[ContentDisarm] = Field(default=None, description="AV Content Disarm and Reconstruction settings.")    
    outbreak_prevention_archive_scan: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable outbreak-prevention archive scanning.")    
    external_blocklist_enable_all: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable all external blocklists.")    
    external_blocklist: list[ExternalBlocklist] = Field(default=None, description="One or more external malware block lists.")    
    ems_threat_feed: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable use of EMS threat feed when performing AntiVirus scan. Analyzes files including the content of archives.")    
    fortindr_error_action: Literal["log-only", "block", "ignore"] | None = Field(default="log-only", description="Action to take if FortiNDR encounters an error.")    
    fortindr_timeout_action: Literal["log-only", "block", "ignore"] | None = Field(default="log-only", description="Action to take if FortiNDR encounters a scan timeout.")    
    fortisandbox_scan_timeout: int | None = Field(ge=30, le=180, default=60, description="FortiSandbox inline scan timeout in seconds (30 - 180, default = 60).")    
    fortisandbox_error_action: Literal["log-only", "block", "ignore"] | None = Field(default="log-only", description="Action to take if FortiSandbox inline scan encounters an error.")    
    fortisandbox_timeout_action: Literal["log-only", "block", "ignore"] | None = Field(default="log-only", description="Action to take if FortiSandbox inline scan encounters a scan timeout.")    
    av_virus_log: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable AntiVirus logging.")    
    extended_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended logging for antivirus.")    
    scan_mode: Literal["default", "legacy"] | None = Field(default="default", description="Configure scan mode (default or legacy).")    
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
    @field_validator('analytics_ignore_filetype')
    @classmethod
    def validate_analytics_ignore_filetype(cls, v: Any) -> Any:
        """
        Validate analytics_ignore_filetype field.
        
        Datasource: ['dlp.filepattern.id']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('analytics_accept_filetype')
    @classmethod
    def validate_analytics_accept_filetype(cls, v: Any) -> Any:
        """
        Validate analytics_accept_filetype field.
        
        Datasource: ['dlp.filepattern.id']
        
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
            >>> policy = ProfileModel(
            ...     replacemsg_group="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_replacemsg_group_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.antivirus.profile.post(policy.to_fortios_dict())
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
    async def validate_analytics_ignore_filetype_references(self, client: Any) -> list[str]:
        """
        Validate analytics_ignore_filetype references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dlp/filepattern        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     analytics_ignore_filetype="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_analytics_ignore_filetype_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.antivirus.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "analytics_ignore_filetype", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dlp.filepattern.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Analytics-Ignore-Filetype '{value}' not found in "
                "dlp/filepattern"
            )        
        return errors    
    async def validate_analytics_accept_filetype_references(self, client: Any) -> list[str]:
        """
        Validate analytics_accept_filetype references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - dlp/filepattern        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     analytics_accept_filetype="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_analytics_accept_filetype_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.antivirus.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "analytics_accept_filetype", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.dlp.filepattern.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Analytics-Accept-Filetype '{value}' not found in "
                "dlp/filepattern"
            )        
        return errors    
    async def validate_external_blocklist_references(self, client: Any) -> list[str]:
        """
        Validate external_blocklist references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/external-resource        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = ProfileModel(
            ...     external_blocklist=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_external_blocklist_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.antivirus.profile.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "external_blocklist", [])
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
            if await client.api.cmdb.system.external-resource.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"External-Blocklist '{value}' not found in "
                    "system/external-resource"
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
        errors = await self.validate_analytics_ignore_filetype_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_analytics_accept_filetype_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_external_blocklist_references(client)
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
    "ProfileModel",    "ProfileHttp",    "ProfileFtp",    "ProfileImap",    "ProfilePop3",    "ProfileSmtp",    "ProfileMapi",    "ProfileNntp",    "ProfileCifs",    "ProfileSsh",    "ProfileNacQuar",    "ProfileContentDisarm",    "ProfileExternalBlocklist",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.073868Z
# ============================================================================
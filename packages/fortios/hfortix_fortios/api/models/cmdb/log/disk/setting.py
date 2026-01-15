"""
Pydantic Models for CMDB - log/disk/setting

Runtime validation models for log/disk/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingRoll_dayEnum(str, Enum):
    """Allowed values for roll_day field."""
    SUNDAY = "sunday"    MONDAY = "monday"    TUESDAY = "tuesday"    WEDNESDAY = "wednesday"    THURSDAY = "thursday"    FRIDAY = "friday"    SATURDAY = "saturday"
class SettingUploadtypeEnum(str, Enum):
    """Allowed values for uploadtype field."""
    TRAFFIC = "traffic"    EVENT = "event"    VIRUS = "virus"    WEBFILTER = "webfilter"    IPS = "IPS"    EMAILFILTER = "emailfilter"    DLP_ARCHIVE = "dlp-archive"    ANOMALY = "anomaly"    VOIP = "voip"    DLP = "dlp"    APP_CTRL = "app-ctrl"    WAF = "waf"    GTP = "gtp"    DNS = "dns"    SSH = "ssh"    SSL = "ssl"    FILE_FILTER = "file-filter"    ICAP = "icap"    VIRTUAL_PATCH = "virtual-patch"    DEBUG = "debug"
class SettingUpload_ssl_connEnum(str, Enum):
    """Allowed values for upload_ssl_conn field."""
    DEFAULT = "default"    HIGH = "high"    LOW = "low"    DISABLE = "disable"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for log/disk/setting configuration.
    
    Settings for local disk logging.
    
    Validation Rules:        - status: pattern=        - ips_archive: pattern=        - max_log_file_size: min=1 max=100 pattern=        - max_policy_packet_capture_size: min=0 max=4294967295 pattern=        - roll_schedule: pattern=        - roll_day: pattern=        - roll_time: pattern=        - diskfull: pattern=        - log_quota: min=0 max=4294967295 pattern=        - dlp_archive_quota: min=0 max=4294967295 pattern=        - report_quota: min=0 max=4294967295 pattern=        - maximum_log_age: min=0 max=3650 pattern=        - upload: pattern=        - upload_destination: pattern=        - uploadip: pattern=        - uploadport: min=0 max=65535 pattern=        - source_ip: pattern=        - uploaduser: max_length=35 pattern=        - uploadpass: max_length=128 pattern=        - uploaddir: max_length=63 pattern=        - uploadtype: pattern=        - uploadsched: pattern=        - uploadtime: pattern=        - upload_delete_files: pattern=        - upload_ssl_conn: pattern=        - full_first_warning_threshold: min=1 max=98 pattern=        - full_second_warning_threshold: min=2 max=99 pattern=        - full_final_warning_threshold: min=3 max=100 pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] = Field(default="enable", description="Enable/disable local disk logging.")    
    ips_archive: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable IPS packet archiving to the local disk.")    
    max_log_file_size: int | None = Field(ge=1, le=100, default=20, description="Maximum log file size before rolling (1 - 100 Mbytes).")    
    max_policy_packet_capture_size: int | None = Field(ge=0, le=4294967295, default=100, description="Maximum size of policy sniffer in MB (0 means unlimited).")    
    roll_schedule: Literal["daily", "weekly"] | None = Field(default="daily", description="Frequency to check log file for rolling.")    
    roll_day: list[RollDay] = Field(default="sunday", description="Day of week on which to roll log file.")    
    roll_time: str | None = Field(default="", description="Time of day to roll the log file (hh:mm).")    
    diskfull: Literal["overwrite", "nolog"] | None = Field(default="overwrite", description="Action to take when disk is full. The system can overwrite the oldest log messages or stop logging when the disk is full (default = overwrite).")    
    log_quota: int | None = Field(ge=0, le=4294967295, default=0, description="Disk log quota (MB).")    
    dlp_archive_quota: int | None = Field(ge=0, le=4294967295, default=0, description="DLP archive quota (MB).")    
    report_quota: int | None = Field(ge=0, le=4294967295, default=0, description="Report db quota (MB).")    
    maximum_log_age: int | None = Field(ge=0, le=3650, default=7, description="Delete log files older than (days).")    
    upload: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable uploading log files when they are rolled.")    
    upload_destination: Literal["ftp-server"] | None = Field(default="ftp-server", description="The type of server to upload log files to. Only FTP is currently supported.")    
    uploadip: str = Field(default="0.0.0.0", description="IP address of the FTP server to upload log files to.")    
    uploadport: int | None = Field(ge=0, le=65535, default=21, description="TCP port to use for communicating with the FTP server (default = 21).")    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address to use for uploading disk log files.")    
    uploaduser: str = Field(max_length=35, default="", description="Username required to log into the FTP server to upload disk log files.")    
    uploadpass: Any = Field(max_length=128, default=None, description="Password required to log into the FTP server to upload disk log files.")    
    uploaddir: str | None = Field(max_length=63, default="", description="The remote directory on the FTP server to upload log files to.")    
    uploadtype: list[Uploadtype] = Field(default="traffic event virus webfilter IPS emailfilter dlp-archive anomaly voip dlp app-ctrl waf gtp dns ssh ssl", description="Types of log files to upload. Separate multiple entries with a space.")    
    uploadsched: Literal["disable", "enable"] | None = Field(default="disable", description="Set the schedule for uploading log files to the FTP server (default = disable = upload when rolling).")    
    uploadtime: str | None = Field(default="", description="Time of day at which log files are uploaded if uploadsched is enabled (hh:mm or hh).")    
    upload_delete_files: Literal["enable", "disable"] | None = Field(default="enable", description="Delete log files after uploading (default = enable).")    
    upload_ssl_conn: UploadSslConnEnum | None = Field(default="default", description="Enable/disable encrypted FTPS communication to upload log files.")    
    full_first_warning_threshold: int | None = Field(ge=1, le=98, default=75, description="Log full first warning threshold as a percent (1 - 98, default = 75).")    
    full_second_warning_threshold: int | None = Field(ge=2, le=99, default=90, description="Log full second warning threshold as a percent (2 - 99, default = 90).")    
    full_final_warning_threshold: int | None = Field(ge=3, le=100, default=95, description="Log full final warning threshold as a percent (3 - 100, default = 95).")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('interface')
    @classmethod
    def validate_interface(cls, v: Any) -> Any:
        """
        Validate interface field.
        
        Datasource: ['system.interface.name']
        
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
    async def validate_interface_references(self, client: Any) -> list[str]:
        """
        Validate interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.log.disk.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Interface '{value}' not found in "
                "system/interface"
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
        
        errors = await self.validate_interface_references(client)
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
    "SettingModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:56.944930Z
# ============================================================================
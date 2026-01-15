"""
Pydantic Models for CMDB - log/syslogd2/setting

Runtime validation models for log/syslogd2/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SettingCustomFieldName(BaseModel):
    """
    Child table model for custom-field-name.
    
    Custom field name for CEF format logging.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=255, default=0, description="Entry ID.")    
    name: str = Field(max_length=35, default="", description="Field name [A-Za-z0-9_].")    
    custom: str = Field(max_length=35, default="", description="Field custom name [A-Za-z0-9_].")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SettingFacilityEnum(str, Enum):
    """Allowed values for facility field."""
    KERNEL = "kernel"    USER = "user"    MAIL = "mail"    DAEMON = "daemon"    AUTH = "auth"    SYSLOG = "syslog"    LPR = "lpr"    NEWS = "news"    UUCP = "uucp"    CRON = "cron"    AUTHPRIV = "authpriv"    FTP = "ftp"    NTP = "ntp"    AUDIT = "audit"    ALERT = "alert"    CLOCK = "clock"    LOCAL0 = "local0"    LOCAL1 = "local1"    LOCAL2 = "local2"    LOCAL3 = "local3"    LOCAL4 = "local4"    LOCAL5 = "local5"    LOCAL6 = "local6"    LOCAL7 = "local7"
class SettingFormatEnum(str, Enum):
    """Allowed values for format field."""
    DEFAULT = "default"    CSV = "csv"    CEF = "cef"    RFC5424 = "rfc5424"    JSON = "json"
class SettingEnc_algorithmEnum(str, Enum):
    """Allowed values for enc_algorithm field."""
    HIGH_MEDIUM = "high-medium"    HIGH = "high"    LOW = "low"    DISABLE = "disable"
class SettingSsl_min_proto_versionEnum(str, Enum):
    """Allowed values for ssl_min_proto_version field."""
    DEFAULT = "default"    SSLV3 = "SSLv3"    TLSV1 = "TLSv1"    TLSV1_1 = "TLSv1-1"    TLSV1_2 = "TLSv1-2"    TLSV1_3 = "TLSv1-3"

# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for log/syslogd2/setting configuration.
    
    Global settings for remote syslog server.
    
    Validation Rules:        - status: pattern=        - server: max_length=127 pattern=        - mode: pattern=        - port: min=0 max=65535 pattern=        - facility: pattern=        - source_ip_interface: max_length=15 pattern=        - source_ip: max_length=63 pattern=        - format: pattern=        - priority: pattern=        - max_log_rate: min=0 max=100000 pattern=        - enc_algorithm: pattern=        - ssl_min_proto_version: pattern=        - certificate: max_length=35 pattern=        - custom_field_name: pattern=        - interface_select_method: pattern=        - interface: max_length=15 pattern=        - vrf_select: min=0 max=511 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable remote syslog logging.")    
    server: str = Field(max_length=127, default="", description="Address of remote syslog server.")    
    mode: Literal["udp", "legacy-reliable", "reliable"] | None = Field(default="udp", description="Remote syslog logging over UDP/Reliable TCP.")    
    port: int | None = Field(ge=0, le=65535, default=514, description="Server listen port.")    
    facility: FacilityEnum | None = Field(default="local7", description="Remote syslog facility.")    
    source_ip_interface: str | None = Field(max_length=15, default="", description="Source interface of syslog.")  # datasource: ['system.interface.name']    
    source_ip: str | None = Field(max_length=63, default="", description="Source IP address of syslog.")    
    format: FormatEnum | None = Field(default="default", description="Log format.")    
    priority: Literal["default", "low"] | None = Field(default="default", description="Set log transmission priority.")    
    max_log_rate: int | None = Field(ge=0, le=100000, default=0, description="Syslog maximum log rate in MBps (0 = unlimited).")    
    enc_algorithm: EncAlgorithmEnum | None = Field(default="disable", description="Enable/disable reliable syslogging with TLS encryption.")    
    ssl_min_proto_version: SslMinProtoVersionEnum | None = Field(default="default", description="Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).")    
    certificate: str | None = Field(max_length=35, default="", description="Certificate used to communicate with Syslog server.")  # datasource: ['certificate.local.name']    
    custom_field_name: list[CustomFieldName] = Field(default=None, description="Custom field name for CEF format logging.")    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vrf_select: int | None = Field(ge=0, le=511, default=0, description="VRF ID used for connection to server.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('source_ip_interface')
    @classmethod
    def validate_source_ip_interface(cls, v: Any) -> Any:
        """
        Validate source_ip_interface field.
        
        Datasource: ['system.interface.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('certificate')
    @classmethod
    def validate_certificate(cls, v: Any) -> Any:
        """
        Validate certificate field.
        
        Datasource: ['certificate.local.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
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
    async def validate_source_ip_interface_references(self, client: Any) -> list[str]:
        """
        Validate source_ip_interface references exist in FortiGate.
        
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
            ...     source_ip_interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_source_ip_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.log.syslogd2.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "source_ip_interface", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Source-Ip-Interface '{value}' not found in "
                "system/interface"
            )        
        return errors    
    async def validate_certificate_references(self, client: Any) -> list[str]:
        """
        Validate certificate references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - certificate/local        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     certificate="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_certificate_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.log.syslogd2.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "certificate", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.certificate.local.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Certificate '{value}' not found in "
                "certificate/local"
            )        
        return errors    
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
            ...     result = await fgt.api.cmdb.log.syslogd2.setting.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_source_ip_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_certificate_references(client)
        all_errors.extend(errors)        
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
    "SettingModel",    "SettingCustomFieldName",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:43.613824Z
# ============================================================================
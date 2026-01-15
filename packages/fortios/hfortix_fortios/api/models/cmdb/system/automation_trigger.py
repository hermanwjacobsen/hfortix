"""
Pydantic Models for CMDB - system/automation_trigger

Runtime validation models for system/automation_trigger configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class AutomationTriggerVdom(BaseModel):
    """
    Child table model for vdom.
    
    Virtual domain(s) that this trigger is valid for.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="Virtual domain name.")  # datasource: ['system.vdom.name']
class AutomationTriggerLogid(BaseModel):
    """
    Child table model for logid.
    
    Log IDs to trigger event.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=1, le=65535, default=0, description="Log ID.")
class AutomationTriggerFields(BaseModel):
    """
    Child table model for fields.
    
    Customized trigger field settings.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Entry ID.")    
    name: str | None = Field(max_length=35, default="", description="Name.")    
    value: str | None = Field(max_length=63, default=None, description="Value.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class AutomationTriggerEvent_typeEnum(str, Enum):
    """Allowed values for event_type field."""
    IOC = "ioc"    EVENT_LOG = "event-log"    REBOOT = "reboot"    LOW_MEMORY = "low-memory"    HIGH_CPU = "high-cpu"    LICENSE_NEAR_EXPIRY = "license-near-expiry"    LOCAL_CERT_NEAR_EXPIRY = "local-cert-near-expiry"    HA_FAILOVER = "ha-failover"    CONFIG_CHANGE = "config-change"    SECURITY_RATING_SUMMARY = "security-rating-summary"    VIRUS_IPS_DB_UPDATED = "virus-ips-db-updated"    FAZ_EVENT = "faz-event"    INCOMING_WEBHOOK = "incoming-webhook"    FABRIC_EVENT = "fabric-event"    IPS_LOGS = "ips-logs"    ANOMALY_LOGS = "anomaly-logs"    VIRUS_LOGS = "virus-logs"    SSH_LOGS = "ssh-logs"    WEBFILTER_VIOLATION = "webfilter-violation"    TRAFFIC_VIOLATION = "traffic-violation"    STITCH = "stitch"
class AutomationTriggerLicense_typeEnum(str, Enum):
    """Allowed values for license_type field."""
    FORTICARE_SUPPORT = "forticare-support"    FORTIGUARD_WEBFILTER = "fortiguard-webfilter"    FORTIGUARD_ANTISPAM = "fortiguard-antispam"    FORTIGUARD_ANTIVIRUS = "fortiguard-antivirus"    FORTIGUARD_IPS = "fortiguard-ips"    FORTIGUARD_MANAGEMENT = "fortiguard-management"    FORTICLOUD = "forticloud"    ANY = "any"
class AutomationTriggerReport_typeEnum(str, Enum):
    """Allowed values for report_type field."""
    POSTURE = "posture"    COVERAGE = "coverage"    OPTIMIZATION = "optimization"    ANY = "any"
class AutomationTriggerTrigger_frequencyEnum(str, Enum):
    """Allowed values for trigger_frequency field."""
    HOURLY = "hourly"    DAILY = "daily"    WEEKLY = "weekly"    MONTHLY = "monthly"    ONCE = "once"
class AutomationTriggerTrigger_weekdayEnum(str, Enum):
    """Allowed values for trigger_weekday field."""
    SUNDAY = "sunday"    MONDAY = "monday"    TUESDAY = "tuesday"    WEDNESDAY = "wednesday"    THURSDAY = "thursday"    FRIDAY = "friday"    SATURDAY = "saturday"

# ============================================================================
# Main Model
# ============================================================================

class AutomationTriggerModel(BaseModel):
    """
    Pydantic model for system/automation_trigger configuration.
    
    Trigger for automation stitches.
    
    Validation Rules:        - name: max_length=35 pattern=        - description: max_length=255 pattern=        - trigger_type: pattern=        - event_type: pattern=        - vdom: pattern=        - license_type: pattern=        - report_type: pattern=        - stitch_name: max_length=35 pattern=        - logid: pattern=        - trigger_frequency: pattern=        - trigger_weekday: pattern=        - trigger_day: min=1 max=31 pattern=        - trigger_hour: min=0 max=23 pattern=        - trigger_minute: min=0 max=59 pattern=        - trigger_datetime: pattern=        - fields: pattern=        - faz_event_name: max_length=255 pattern=        - faz_event_severity: max_length=255 pattern=        - faz_event_tags: max_length=255 pattern=        - serial: max_length=255 pattern=        - fabric_event_name: max_length=255 pattern=        - fabric_event_severity: max_length=255 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Name.")    
    description: str | None = Field(max_length=255, default=None, description="Description.")    
    trigger_type: Literal["event-based", "scheduled"] | None = Field(default="event-based", description="Trigger type.")    
    event_type: EventTypeEnum | None = Field(default="ioc", description="Event type.")    
    vdom: list[Vdom] = Field(default=None, description="Virtual domain(s) that this trigger is valid for.")    
    license_type: LicenseTypeEnum | None = Field(default="forticare-support", description="License type.")    
    report_type: ReportTypeEnum | None = Field(default="posture", description="Security Rating report.")    
    stitch_name: str = Field(max_length=35, default="", description="Triggering stitch name.")  # datasource: ['system.automation-stitch.name']    
    logid: list[Logid] = Field(default=None, description="Log IDs to trigger event.")    
    trigger_frequency: TriggerFrequencyEnum | None = Field(default="daily", description="Scheduled trigger frequency (default = daily).")    
    trigger_weekday: TriggerWeekdayEnum | None = Field(default="", description="Day of week for trigger.")    
    trigger_day: int | None = Field(ge=1, le=31, default=1, description="Day within a month to trigger.")    
    trigger_hour: int | None = Field(ge=0, le=23, default=0, description="Hour of the day on which to trigger (0 - 23, default = 1).")    
    trigger_minute: int | None = Field(ge=0, le=59, default=0, description="Minute of the hour on which to trigger (0 - 59, default = 0).")    
    trigger_datetime: Any = Field(default="0000-00-00 00:00:00", description="Trigger date and time (YYYY-MM-DD HH:MM:SS).")    
    fields: list[Fields] = Field(default=None, description="Customized trigger field settings.")    
    faz_event_name: str = Field(max_length=255, description="FortiAnalyzer event handler name.")    
    faz_event_severity: str | None = Field(max_length=255, default=None, description="FortiAnalyzer event severity.")    
    faz_event_tags: str | None = Field(max_length=255, default=None, description="FortiAnalyzer event tags.")    
    serial: str = Field(max_length=255, description="Fabric connector serial number.")    
    fabric_event_name: str = Field(max_length=255, description="Fabric connector event handler name.")    
    fabric_event_severity: str | None = Field(max_length=255, default=None, description="Fabric connector event severity.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('stitch_name')
    @classmethod
    def validate_stitch_name(cls, v: Any) -> Any:
        """
        Validate stitch_name field.
        
        Datasource: ['system.automation-stitch.name']
        
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
    async def validate_vdom_references(self, client: Any) -> list[str]:
        """
        Validate vdom references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/vdom        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationTriggerModel(
            ...     vdom=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_vdom_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_trigger.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "vdom", [])
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
            if await client.api.cmdb.system.vdom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Vdom '{value}' not found in "
                    "system/vdom"
                )        
        return errors    
    async def validate_stitch_name_references(self, client: Any) -> list[str]:
        """
        Validate stitch_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/automation-stitch        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = AutomationTriggerModel(
            ...     stitch_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_stitch_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.automation_trigger.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "stitch_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.automation-stitch.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Stitch-Name '{value}' not found in "
                "system/automation-stitch"
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
        
        errors = await self.validate_vdom_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_stitch_name_references(client)
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
    "AutomationTriggerModel",    "AutomationTriggerVdom",    "AutomationTriggerLogid",    "AutomationTriggerFields",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.591426Z
# ============================================================================
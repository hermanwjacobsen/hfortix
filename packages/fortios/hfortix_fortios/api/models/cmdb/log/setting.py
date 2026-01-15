"""
Pydantic Models for CMDB - log/setting

Runtime validation models for log/setting configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class SettingCustomLogFields(BaseModel):
    """
    Child table model for custom-log-fields.
    
    Custom fields to append to all log messages.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    field_id: str | None = Field(max_length=35, default="", description="Custom log field.")  # datasource: ['log.custom-field.id']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SettingModel(BaseModel):
    """
    Pydantic model for log/setting configuration.
    
    Configure general log settings.
    
    Validation Rules:        - resolve_ip: pattern=        - resolve_port: pattern=        - log_user_in_upper: pattern=        - fwpolicy_implicit_log: pattern=        - fwpolicy6_implicit_log: pattern=        - extended_log: pattern=        - local_in_allow: pattern=        - local_in_deny_unicast: pattern=        - local_in_deny_broadcast: pattern=        - local_in_policy_log: pattern=        - local_out: pattern=        - local_out_ioc_detection: pattern=        - daemon_log: pattern=        - neighbor_event: pattern=        - brief_traffic_format: pattern=        - user_anonymize: pattern=        - expolicy_implicit_log: pattern=        - log_policy_comment: pattern=        - faz_override: pattern=        - syslog_override: pattern=        - rest_api_set: pattern=        - rest_api_get: pattern=        - rest_api_performance: pattern=        - long_live_session_stat: pattern=        - extended_utm_log: pattern=        - zone_name: pattern=        - web_svc_perf: pattern=        - custom_log_fields: pattern=        - anonymization_hash: max_length=32 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    resolve_ip: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adding resolved domain names to traffic logs if possible.")    
    resolve_port: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable adding resolved service names to traffic logs.")    
    log_user_in_upper: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable logs with user-in-upper.")    
    fwpolicy_implicit_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable implicit firewall policy logging.")    
    fwpolicy6_implicit_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable implicit firewall policy6 logging.")    
    extended_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended traffic logging.")    
    local_in_allow: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-allow logging.")    
    local_in_deny_unicast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-deny-unicast logging.")    
    local_in_deny_broadcast: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-deny-broadcast logging.")    
    local_in_policy_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable local-in-policy logging.")    
    local_out: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable local-out logging.")    
    local_out_ioc_detection: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable local-out traffic IoC detection. Requires local-out to be enabled.")    
    daemon_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable daemon logging.")    
    neighbor_event: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable neighbor event logging.")    
    brief_traffic_format: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable brief format traffic logging.")    
    user_anonymize: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable anonymizing user names in log messages.")    
    expolicy_implicit_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable proxy firewall implicit policy logging.")    
    log_policy_comment: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable inserting policy comments into traffic logs.")    
    faz_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable override FortiAnalyzer settings.")    
    syslog_override: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable override Syslog settings.")    
    rest_api_set: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable REST API POST/PUT/DELETE request logging.")    
    rest_api_get: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable REST API GET request logging.")    
    rest_api_performance: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable REST API memory and performance stats in rest-api-get/set logs.")    
    long_live_session_stat: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable long-live-session statistics logging.")    
    extended_utm_log: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable extended UTM logging.")    
    zone_name: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable zone name logging.")    
    web_svc_perf: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable web-svc performance logging.")    
    custom_log_fields: list[CustomLogFields] = Field(default=None, description="Custom fields to append to all log messages.")    
    anonymization_hash: str | None = Field(max_length=32, default="", description="User name anonymization hash salt.")    
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
    async def validate_custom_log_fields_references(self, client: Any) -> list[str]:
        """
        Validate custom_log_fields references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - log/custom-field        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SettingModel(
            ...     custom_log_fields=[{"field-id": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_custom_log_fields_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.log.setting.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "custom_log_fields", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("field-id")
            else:
                value = getattr(item, "field-id", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.log.custom-field.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Custom-Log-Fields '{value}' not found in "
                    "log/custom-field"
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
        
        errors = await self.validate_custom_log_fields_references(client)
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
    "SettingModel",    "SettingCustomLogFields",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.417293Z
# ============================================================================
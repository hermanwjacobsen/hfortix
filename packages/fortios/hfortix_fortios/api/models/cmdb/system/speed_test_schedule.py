"""
Pydantic Models for CMDB - system/speed_test_schedule

Runtime validation models for system/speed_test_schedule configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class SpeedTestScheduleSchedules(BaseModel):
    """
    Child table model for schedules.
    
    Schedules for the interface.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=31, default="", description="Name of a firewall recurring schedule.")  # datasource: ['firewall.schedule.recurring.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SpeedTestScheduleUpdate_shaperEnum(str, Enum):
    """Allowed values for update_shaper field."""
    DISABLE = "disable"    LOCAL = "local"    REMOTE = "remote"    BOTH = "both"

# ============================================================================
# Main Model
# ============================================================================

class SpeedTestScheduleModel(BaseModel):
    """
    Pydantic model for system/speed_test_schedule configuration.
    
    Speed test schedule for each interface.
    
    Validation Rules:        - interface: max_length=35 pattern=        - status: pattern=        - diffserv: pattern=        - server_name: max_length=35 pattern=        - mode: pattern=        - schedules: pattern=        - dynamic_server: pattern=        - ctrl_port: min=1 max=65535 pattern=        - server_port: min=1 max=65535 pattern=        - update_shaper: pattern=        - update_inbandwidth: pattern=        - update_outbandwidth: pattern=        - update_interface_shaping: pattern=        - update_inbandwidth_maximum: min=0 max=16776000 pattern=        - update_inbandwidth_minimum: min=0 max=16776000 pattern=        - update_outbandwidth_maximum: min=0 max=16776000 pattern=        - update_outbandwidth_minimum: min=0 max=16776000 pattern=        - expected_inbandwidth_minimum: min=0 max=16776000 pattern=        - expected_inbandwidth_maximum: min=0 max=16776000 pattern=        - expected_outbandwidth_minimum: min=0 max=16776000 pattern=        - expected_outbandwidth_maximum: min=0 max=16776000 pattern=        - retries: min=1 max=10 pattern=        - retry_pause: min=60 max=3600 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    interface: str | None = Field(max_length=35, default="", description="Interface name.")  # datasource: ['system.interface.name']    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable scheduled speed test.")    
    diffserv: str | None = Field(default="", description="DSCP used for speed test.")    
    server_name: str | None = Field(max_length=35, default="", description="Speed test server name in system.speed-test-server list or leave it as empty to choose default server \"FTNT_Auto\".")  # datasource: ['system.speed-test-server.name']    
    mode: Literal["UDP", "TCP", "Auto"] | None = Field(default="Auto", description="Protocol Auto(default), TCP or UDP used for speed test.")    
    schedules: list[Schedules] = Field(description="Schedules for the interface.")    
    dynamic_server: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable dynamic server option.")    
    ctrl_port: int | None = Field(ge=1, le=65535, default=5200, description="Port of the controller to get access token.")    
    server_port: int | None = Field(ge=1, le=65535, default=5201, description="Port of the server to run speed test.")    
    update_shaper: UpdateShaperEnum | None = Field(default="disable", description="Set egress shaper based on the test result.")    
    update_inbandwidth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bypassing interface's inbound bandwidth setting.")    
    update_outbandwidth: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable bypassing interface's outbound bandwidth setting.")    
    update_interface_shaping: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable using the speedtest results as reference for interface shaping (overriding configured in/outbandwidth).")    
    update_inbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Maximum downloading bandwidth (kbps) to be used in a speed test.")    
    update_inbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Minimum downloading bandwidth (kbps) to be considered effective.")    
    update_outbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Maximum uploading bandwidth (kbps) to be used in a speed test.")    
    update_outbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Minimum uploading bandwidth (kbps) to be considered effective.")    
    expected_inbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Set the minimum inbandwidth threshold for applying speedtest results on shaping-profile.")    
    expected_inbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Set the maximum inbandwidth threshold for applying speedtest results on shaping-profile.")    
    expected_outbandwidth_minimum: int | None = Field(ge=0, le=16776000, default=0, description="Set the minimum outbandwidth threshold for applying speedtest results on shaping-profile.")    
    expected_outbandwidth_maximum: int | None = Field(ge=0, le=16776000, default=0, description="Set the maximum outbandwidth threshold for applying speedtest results on shaping-profile.")    
    retries: int | None = Field(ge=1, le=10, default=5, description="Maximum number of times the FortiGate unit will attempt to contact the same server before considering the speed test has failed (1 - 10, default = 5).")    
    retry_pause: int | None = Field(ge=60, le=3600, default=300, description="Number of seconds the FortiGate pauses between successive speed tests before trying a different server (60 - 3600, default = 300).")    
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
    @field_validator('server_name')
    @classmethod
    def validate_server_name(cls, v: Any) -> Any:
        """
        Validate server_name field.
        
        Datasource: ['system.speed-test-server.name']
        
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
            >>> policy = SpeedTestScheduleModel(
            ...     interface="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.speed_test_schedule.post(policy.to_fortios_dict())
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
    async def validate_server_name_references(self, client: Any) -> list[str]:
        """
        Validate server_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/speed-test-server        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SpeedTestScheduleModel(
            ...     server_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_server_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.speed_test_schedule.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "server_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.speed-test-server.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Server-Name '{value}' not found in "
                "system/speed-test-server"
            )        
        return errors    
    async def validate_schedules_references(self, client: Any) -> list[str]:
        """
        Validate schedules references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/schedule/recurring        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = SpeedTestScheduleModel(
            ...     schedules=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_schedules_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.speed_test_schedule.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "schedules", [])
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
            if await client.api.cmdb.firewall.schedule.recurring.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Schedules '{value}' not found in "
                    "firewall/schedule/recurring"
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
        errors = await self.validate_server_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_schedules_references(client)
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
    "SpeedTestScheduleModel",    "SpeedTestScheduleSchedules",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:14.693744Z
# ============================================================================
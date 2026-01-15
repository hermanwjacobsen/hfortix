"""
Pydantic Models for CMDB - system/pppoe_interface

Runtime validation models for system/pppoe_interface configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class PppoeInterfacePppoe_egress_cosEnum(str, Enum):
    """Allowed values for pppoe_egress_cos field."""
    COS0 = "cos0"    COS1 = "cos1"    COS2 = "cos2"    COS3 = "cos3"    COS4 = "cos4"    COS5 = "cos5"    COS6 = "cos6"    COS7 = "cos7"
class PppoeInterfaceAuth_typeEnum(str, Enum):
    """Allowed values for auth_type field."""
    AUTO = "auto"    PAP = "pap"    CHAP = "chap"    MSCHAPV1 = "mschapv1"    MSCHAPV2 = "mschapv2"

# ============================================================================
# Main Model
# ============================================================================

class PppoeInterfaceModel(BaseModel):
    """
    Pydantic model for system/pppoe_interface configuration.
    
    Configure the PPPoE interfaces.
    
    Validation Rules:        - name: max_length=15 pattern=        - dial_on_demand: pattern=        - ipv6: pattern=        - device: max_length=15 pattern=        - username: max_length=64 pattern=        - password: max_length=128 pattern=        - pppoe_egress_cos: pattern=        - auth_type: pattern=        - ipunnumbered: pattern=        - pppoe_unnumbered_negotiate: pattern=        - idle_timeout: min=0 max=4294967295 pattern=        - multilink: pattern=        - mrru: min=296 max=65535 pattern=        - disc_retry_timeout: min=0 max=4294967295 pattern=        - padt_retry_timeout: min=0 max=4294967295 pattern=        - service_name: max_length=63 pattern=        - ac_name: max_length=63 pattern=        - lcp_echo_interval: min=0 max=32767 pattern=        - lcp_max_echo_fails: min=0 max=32767 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=15, default="", description="Name of the PPPoE interface.")    
    dial_on_demand: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dial on demand to dial the PPPoE interface when packets are routed to the PPPoE interface.")    
    ipv6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 Control Protocol (IPv6CP).")    
    device: str = Field(max_length=15, default="", description="Name for the physical interface.")  # datasource: ['system.interface.name']    
    username: str | None = Field(max_length=64, default="", description="User name.")    
    password: Any = Field(max_length=128, default=None, description="Enter the password.")    
    pppoe_egress_cos: PppoeEgressCosEnum | None = Field(default="cos0", description="CoS in VLAN tag for outgoing PPPoE/PPP packets.")    
    auth_type: AuthTypeEnum | None = Field(default="auto", description="PPP authentication type to use.")    
    ipunnumbered: str | None = Field(default="0.0.0.0", description="PPPoE unnumbered IP.")    
    pppoe_unnumbered_negotiate: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable PPPoE unnumbered negotiation.")    
    idle_timeout: int | None = Field(ge=0, le=4294967295, default=0, description="PPPoE auto disconnect after idle timeout (0-4294967295 sec).")    
    multilink: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable PPP multilink support.")    
    mrru: int | None = Field(ge=296, le=65535, default=1500, description="PPP MRRU (296 - 65535, default = 1500).")    
    disc_retry_timeout: int | None = Field(ge=0, le=4294967295, default=1, description="PPPoE discovery init timeout value in (0-4294967295 sec).")    
    padt_retry_timeout: int | None = Field(ge=0, le=4294967295, default=1, description="PPPoE terminate timeout value in (0-4294967295 sec).")    
    service_name: str | None = Field(max_length=63, default="", description="PPPoE service name.")    
    ac_name: str | None = Field(max_length=63, default="", description="PPPoE AC name.")    
    lcp_echo_interval: int | None = Field(ge=0, le=32767, default=5, description="Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.")    
    lcp_max_echo_fails: int | None = Field(ge=0, le=32767, default=3, description="Maximum missed LCP echo messages before disconnect.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('device')
    @classmethod
    def validate_device(cls, v: Any) -> Any:
        """
        Validate device field.
        
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
    async def validate_device_references(self, client: Any) -> list[str]:
        """
        Validate device references exist in FortiGate.
        
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
            >>> policy = PppoeInterfaceModel(
            ...     device="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_device_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.system.pppoe_interface.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "device", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.interface.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Device '{value}' not found in "
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
        
        errors = await self.validate_device_references(client)
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
    "PppoeInterfaceModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.421933Z
# ============================================================================
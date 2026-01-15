"""
Pydantic Models for CMDB - switch_controller/flow_tracking

Runtime validation models for switch_controller/flow_tracking configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class FlowTrackingCollectors(BaseModel):
    """
    Child table model for collectors.
    
    Configure collectors for the flow.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=63, default="", description="Collector name.")    
    ip: str | None = Field(default="0.0.0.0", description="Collector IP address.")    
    port: int | None = Field(ge=0, le=65535, default=0, description="Collector port number(0-65535, default:0, netflow:2055, ipfix:4739).")    
    transport: Literal["udp", "tcp", "sctp"] | None = Field(default="udp", description="Collector L4 transport protocol for exporting packets.")
class FlowTrackingAggregates(BaseModel):
    """
    Child table model for aggregates.
    
    Configure aggregates in which all traffic sessions matching the IP Address will be grouped into the same flow.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Aggregate id.")    
    ip: str = Field(default="0.0.0.0 0.0.0.0", description="IP address to group all matching traffic sessions to a flow.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class FlowTrackingFormatEnum(str, Enum):
    """Allowed values for format field."""
    NETFLOW1 = "netflow1"    NETFLOW5 = "netflow5"    NETFLOW9 = "netflow9"    IPFIX = "ipfix"
class FlowTrackingLevelEnum(str, Enum):
    """Allowed values for level field."""
    VLAN = "vlan"    IP = "ip"    PORT = "port"    PROTO = "proto"    MAC = "mac"

# ============================================================================
# Main Model
# ============================================================================

class FlowTrackingModel(BaseModel):
    """
    Pydantic model for switch_controller/flow_tracking configuration.
    
    Configure FortiSwitch flow tracking and export via ipfix/netflow.
    
    Validation Rules:        - sample_mode: pattern=        - sample_rate: min=0 max=99999 pattern=        - format: pattern=        - collectors: pattern=        - level: pattern=        - max_export_pkt_size: min=512 max=9216 pattern=        - template_export_period: min=1 max=60 pattern=        - timeout_general: min=60 max=604800 pattern=        - timeout_icmp: min=60 max=604800 pattern=        - timeout_max: min=60 max=604800 pattern=        - timeout_tcp: min=60 max=604800 pattern=        - timeout_tcp_fin: min=60 max=604800 pattern=        - timeout_tcp_rst: min=60 max=604800 pattern=        - timeout_udp: min=60 max=604800 pattern=        - aggregates: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    sample_mode: Literal["local", "perimeter", "device-ingress"] | None = Field(default="perimeter", description="Configure sample mode for the flow tracking.")    
    sample_rate: int | None = Field(ge=0, le=99999, default=512, description="Configure sample rate for the perimeter and device-ingress sampling(0 - 99999).")    
    format: FormatEnum | None = Field(default="netflow9", description="Configure flow tracking protocol.")    
    collectors: list[Collectors] = Field(default=None, description="Configure collectors for the flow.")    
    level: LevelEnum | None = Field(default="ip", description="Configure flow tracking level.")    
    max_export_pkt_size: int | None = Field(ge=512, le=9216, default=512, description="Configure flow max export packet size (512-9216, default=512 bytes).")    
    template_export_period: int | None = Field(ge=1, le=60, default=5, description="Configure template export period (1-60, default=5 minutes).")    
    timeout_general: int | None = Field(ge=60, le=604800, default=3600, description="Configure flow session general timeout (60-604800, default=3600 seconds).")    
    timeout_icmp: int | None = Field(ge=60, le=604800, default=300, description="Configure flow session ICMP timeout (60-604800, default=300 seconds).")    
    timeout_max: int | None = Field(ge=60, le=604800, default=604800, description="Configure flow session max timeout (60-604800, default=604800 seconds).")    
    timeout_tcp: int | None = Field(ge=60, le=604800, default=3600, description="Configure flow session TCP timeout (60-604800, default=3600 seconds).")    
    timeout_tcp_fin: int | None = Field(ge=60, le=604800, default=300, description="Configure flow session TCP FIN timeout (60-604800, default=300 seconds).")    
    timeout_tcp_rst: int | None = Field(ge=60, le=604800, default=120, description="Configure flow session TCP RST timeout (60-604800, default=120 seconds).")    
    timeout_udp: int | None = Field(ge=60, le=604800, default=300, description="Configure flow session UDP timeout (60-604800, default=300 seconds).")    
    aggregates: list[Aggregates] = Field(default=None, description="Configure aggregates in which all traffic sessions matching the IP Address will be grouped into the same flow.")    
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
    "FlowTrackingModel",    "FlowTrackingCollectors",    "FlowTrackingAggregates",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:53.396344Z
# ============================================================================
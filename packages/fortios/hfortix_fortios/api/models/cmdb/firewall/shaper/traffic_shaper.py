"""
Pydantic Models for CMDB - firewall/shaper/traffic_shaper

Runtime validation models for firewall/shaper/traffic_shaper configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class TrafficShaperModel(BaseModel):
    """
    Pydantic model for firewall/shaper/traffic_shaper configuration.
    
    Configure shared traffic shaper.
    
    Validation Rules:        - name: max_length=35 pattern=        - guaranteed_bandwidth: min=0 max=80000000 pattern=        - maximum_bandwidth: min=0 max=80000000 pattern=        - bandwidth_unit: pattern=        - priority: pattern=        - per_policy: pattern=        - diffserv: pattern=        - diffservcode: pattern=        - dscp_marking_method: pattern=        - exceed_bandwidth: min=0 max=80000000 pattern=        - exceed_dscp: pattern=        - maximum_dscp: pattern=        - cos_marking: pattern=        - cos_marking_method: pattern=        - cos: pattern=        - exceed_cos: pattern=        - maximum_cos: pattern=        - overhead: min=0 max=100 pattern=        - exceed_class_id: min=0 max=4294967295 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="Traffic shaper name.")    
    guaranteed_bandwidth: int | None = Field(ge=0, le=80000000, default=0, description="Amount of bandwidth guaranteed for this shaper (0 - 80000000). Units depend on the bandwidth-unit setting.")    
    maximum_bandwidth: int | None = Field(ge=0, le=80000000, default=0, description="Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting.")    
    bandwidth_unit: Literal["kbps", "mbps", "gbps"] | None = Field(default="kbps", description="Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps).")    
    priority: Literal["low", "medium", "high"] | None = Field(default="high", description="Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth.")    
    per_policy: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable applying a separate shaper for each policy. For example, if enabled the guaranteed bandwidth is applied separately for each policy.")    
    diffserv: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable changing the DiffServ setting applied to traffic accepted by this shaper.")    
    diffservcode: str | None = Field(default="", description="DiffServ setting to be applied to traffic accepted by this shaper.")    
    dscp_marking_method: Literal["multi-stage", "static"] | None = Field(default="static", description="Select DSCP marking method.")    
    exceed_bandwidth: int | None = Field(ge=0, le=80000000, default=0, description="Exceed bandwidth used for DSCP/VLAN CoS multi-stage marking. Units depend on the bandwidth-unit setting.")    
    exceed_dscp: str | None = Field(default="", description="DSCP mark for traffic in guaranteed-bandwidth and exceed-bandwidth.")    
    maximum_dscp: str | None = Field(default="", description="DSCP mark for traffic in exceed-bandwidth and maximum-bandwidth.")    
    cos_marking: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable VLAN CoS marking.")    
    cos_marking_method: Literal["multi-stage", "static"] | None = Field(default="static", description="Select VLAN CoS marking method.")    
    cos: str | None = Field(default="", description="VLAN CoS mark.")    
    exceed_cos: str | None = Field(default="", description="VLAN CoS mark for traffic in [guaranteed-bandwidth, exceed-bandwidth].")    
    maximum_cos: str | None = Field(default="", description="VLAN CoS mark for traffic in [exceed-bandwidth, maximum-bandwidth].")    
    overhead: int | None = Field(ge=0, le=100, default=0, description="Per-packet size overhead used in rate computations.")    
    exceed_class_id: int | None = Field(ge=0, le=4294967295, default=0, description="Class ID for traffic in guaranteed-bandwidth and maximum-bandwidth.")  # datasource: ['firewall.traffic-class.class-id']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('exceed_class_id')
    @classmethod
    def validate_exceed_class_id(cls, v: Any) -> Any:
        """
        Validate exceed_class_id field.
        
        Datasource: ['firewall.traffic-class.class-id']
        
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
    async def validate_exceed_class_id_references(self, client: Any) -> list[str]:
        """
        Validate exceed_class_id references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/traffic-class        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = TrafficShaperModel(
            ...     exceed_class_id="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_exceed_class_id_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.firewall.shaper.traffic_shaper.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "exceed_class_id", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.traffic-class.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Exceed-Class-Id '{value}' not found in "
                "firewall/traffic-class"
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
        
        errors = await self.validate_exceed_class_id_references(client)
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
    "TrafficShaperModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:45.131730Z
# ============================================================================
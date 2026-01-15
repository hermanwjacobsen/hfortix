"""
Pydantic Models for CMDB - ips/global_

Runtime validation models for ips/global_ configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class GlobalTlsActiveProbe(BaseModel):
    """
    Child table model for tls-active-probe.
    
    TLS active probe configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    interface_select_method: Literal["auto", "sdwan", "specify"] | None = Field(default="auto", description="Specify how to select outgoing interface to reach server.")    
    interface: str = Field(max_length=15, default="", description="Specify outgoing interface to reach server.")  # datasource: ['system.interface.name']    
    vdom: str = Field(max_length=31, default="", description="Virtual domain name for TLS active probe.")  # datasource: ['system.vdom.name']    
    source_ip: str | None = Field(default="0.0.0.0", description="Source IP address used for TLS active probe.")    
    source_ip6: str | None = Field(default="::", description="Source IPv6 address used for TLS active probe.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class GlobalModel(BaseModel):
    """
    Pydantic model for ips/global_ configuration.
    
    Configure IPS global parameter.
    
    Validation Rules:        - fail_open: pattern=        - database: pattern=        - traffic_submit: pattern=        - anomaly_mode: pattern=        - session_limit_mode: pattern=        - socket_size: min=0 max=512 pattern=        - engine_count: min=0 max=255 pattern=        - sync_session_ttl: pattern=        - deep_app_insp_timeout: min=0 max=2147483647 pattern=        - deep_app_insp_db_limit: min=0 max=2147483647 pattern=        - exclude_signatures: pattern=        - packet_log_queue_depth: min=128 max=4096 pattern=        - ngfw_max_scan_range: min=0 max=4294967295 pattern=        - av_mem_limit: min=10 max=50 pattern=        - machine_learning_detection: pattern=        - tls_active_probe: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    fail_open: Literal["enable", "disable"] | None = Field(default="disable", description="Enable to allow traffic if the IPS buffer is full. Default is disable and IPS traffic is blocked when the IPS buffer is full.")    
    database: Literal["regular", "extended"] | None = Field(default="extended", description="Regular or extended IPS database. Regular protects against the latest common and in-the-wild attacks. Extended includes protection from legacy attacks.")    
    traffic_submit: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable submitting attack data found by this FortiGate to FortiGuard.")    
    anomaly_mode: Literal["periodical", "continuous"] | None = Field(default="continuous", description="Global blocking mode for rate-based anomalies.")    
    session_limit_mode: Literal["accurate", "heuristic"] | None = Field(default="heuristic", description="Method of counting concurrent sessions used by session limit anomalies. Choose between greater accuracy (accurate) or improved performance (heuristics).")    
    socket_size: int | None = Field(ge=0, le=512, default=256, description="IPS socket buffer size. Max and default value depend on available memory. Can be changed to tune performance.")    
    engine_count: int | None = Field(ge=0, le=255, default=0, description="Number of IPS engines running. If set to the default value of 0, FortiOS sets the number to optimize performance depending on the number of CPU cores.")    
    sync_session_ttl: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable use of kernel session TTL for IPS sessions.")    
    deep_app_insp_timeout: int | None = Field(ge=0, le=2147483647, default=0, description="Timeout for Deep application inspection (1 - 2147483647 sec., 0 = use recommended setting).")    
    deep_app_insp_db_limit: int | None = Field(ge=0, le=2147483647, default=0, description="Limit on number of entries in deep application inspection database (1 - 2147483647, use recommended setting = 0).")    
    exclude_signatures: Literal["none", "ot"] | None = Field(default="ot", description="Excluded signatures.")    
    packet_log_queue_depth: int | None = Field(ge=128, le=4096, default=128, description="Packet/pcap log queue depth per IPS engine.")    
    ngfw_max_scan_range: int | None = Field(ge=0, le=4294967295, default=4096, description="NGFW policy-mode app detection threshold.")    
    av_mem_limit: int | None = Field(ge=10, le=50, default=0, description="Maximum percentage of system memory allowed for use on AV scanning (10 - 50, default = zero). To disable set to zero. When disabled, there is no limit on the AV memory usage.")    
    machine_learning_detection: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable machine learning detection.")    
    tls_active_probe: list[TlsActiveProbe] = Field(default=None, description="TLS active probe configuration.")    
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
    async def validate_tls_active_probe_references(self, client: Any) -> list[str]:
        """
        Validate tls_active_probe references exist in FortiGate.
        
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
            >>> policy = GlobalModel(
            ...     tls_active_probe=[{"vdom": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_tls_active_probe_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.ips.global_.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "tls_active_probe", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("vdom")
            else:
                value = getattr(item, "vdom", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.vdom.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Tls-Active-Probe '{value}' not found in "
                    "system/vdom"
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
        
        errors = await self.validate_tls_active_probe_references(client)
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
    "GlobalModel",    "GlobalTlsActiveProbe",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:58.097249Z
# ============================================================================
"""
Pydantic Models for CMDB - switch_controller/qos/qos_policy

Runtime validation models for switch_controller/qos/qos_policy configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class QosPolicyModel(BaseModel):
    """
    Pydantic model for switch_controller/qos/qos_policy configuration.
    
    Configure FortiSwitch QoS policy.
    
    Validation Rules:        - name: max_length=63 pattern=        - default_cos: min=0 max=7 pattern=        - trust_dot1p_map: max_length=63 pattern=        - trust_ip_dscp_map: max_length=63 pattern=        - queue_policy: max_length=63 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=63, default="", description="QoS policy name.")    
    default_cos: int = Field(ge=0, le=7, default=0, description="Default cos queue for untagged packets.")    
    trust_dot1p_map: str | None = Field(max_length=63, default="", description="QoS trust 802.1p map.")  # datasource: ['switch-controller.qos.dot1p-map.name']    
    trust_ip_dscp_map: str | None = Field(max_length=63, default="", description="QoS trust ip dscp map.")  # datasource: ['switch-controller.qos.ip-dscp-map.name']    
    queue_policy: str | None = Field(max_length=63, default="default", description="QoS egress queue policy.")  # datasource: ['switch-controller.qos.queue-policy.name']    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('trust_dot1p_map')
    @classmethod
    def validate_trust_dot1p_map(cls, v: Any) -> Any:
        """
        Validate trust_dot1p_map field.
        
        Datasource: ['switch-controller.qos.dot1p-map.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('trust_ip_dscp_map')
    @classmethod
    def validate_trust_ip_dscp_map(cls, v: Any) -> Any:
        """
        Validate trust_ip_dscp_map field.
        
        Datasource: ['switch-controller.qos.ip-dscp-map.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('queue_policy')
    @classmethod
    def validate_queue_policy(cls, v: Any) -> Any:
        """
        Validate queue_policy field.
        
        Datasource: ['switch-controller.qos.queue-policy.name']
        
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
    async def validate_trust_dot1p_map_references(self, client: Any) -> list[str]:
        """
        Validate trust_dot1p_map references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/qos/dot1p-map        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = QosPolicyModel(
            ...     trust_dot1p_map="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_trust_dot1p_map_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.qos.qos_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "trust_dot1p_map", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.qos.dot1p-map.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Trust-Dot1P-Map '{value}' not found in "
                "switch-controller/qos/dot1p-map"
            )        
        return errors    
    async def validate_trust_ip_dscp_map_references(self, client: Any) -> list[str]:
        """
        Validate trust_ip_dscp_map references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/qos/ip-dscp-map        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = QosPolicyModel(
            ...     trust_ip_dscp_map="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_trust_ip_dscp_map_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.qos.qos_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "trust_ip_dscp_map", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.qos.ip-dscp-map.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Trust-Ip-Dscp-Map '{value}' not found in "
                "switch-controller/qos/ip-dscp-map"
            )        
        return errors    
    async def validate_queue_policy_references(self, client: Any) -> list[str]:
        """
        Validate queue_policy references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - switch-controller/qos/queue-policy        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = QosPolicyModel(
            ...     queue_policy="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_queue_policy_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.switch_controller.qos.qos_policy.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "queue_policy", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.switch-controller.qos.queue-policy.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Queue-Policy '{value}' not found in "
                "switch-controller/qos/queue-policy"
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
        
        errors = await self.validate_trust_dot1p_map_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_trust_ip_dscp_map_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_queue_policy_references(client)
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
    "QosPolicyModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.766857Z
# ============================================================================
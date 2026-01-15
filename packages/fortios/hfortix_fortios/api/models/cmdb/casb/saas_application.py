"""
Pydantic Models for CMDB - casb/saas_application

Runtime validation models for casb/saas_application configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class SaasApplicationDomains(BaseModel):
    """
    Child table model for domains.
    
    SaaS application domain list.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    domain: str = Field(max_length=127, default="", description="Domain list separated by space.")
class SaasApplicationOutputAttributes(BaseModel):
    """
    Child table model for output-attributes.
    
    SaaS application output attributes.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="CASB attribute name.")    
    description: str | None = Field(max_length=63, default="", description="CASB attribute description.")    
    type: TypeEnum | None = Field(default="string", description="CASB attribute format type.")    
    optional: Literal["enable", "disable"] | None = Field(default="disable", description="CASB output attribute optional.")
class SaasApplicationInputAttributes(BaseModel):
    """
    Child table model for input-attributes.
    
    SaaS application input attributes.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=79, default="", description="CASB attribute name.")    
    description: str | None = Field(max_length=63, default="", description="CASB attribute description.")    
    type: Literal["string"] | None = Field(default="string", description="CASB attribute format type.")    
    required: Literal["enable", "disable"] | None = Field(default="enable", description="CASB input attribute required.")    
    default: Literal["string", "string-list"] | None = Field(default="string", description="CASB attribute default value.")    
    fallback_input: Literal["enable", "disable"] | None = Field(default="disable", description="CASB attribute legacy input.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class SaasApplicationModel(BaseModel):
    """
    Pydantic model for casb/saas_application configuration.
    
    Configure CASB SaaS application.
    
    Validation Rules:        - name: max_length=79 pattern=        - uuid: max_length=36 pattern=        - status: pattern=        - type: pattern=        - casb_name: max_length=79 pattern=        - description: max_length=63 pattern=        - domains: pattern=        - output_attributes: pattern=        - input_attributes: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=79, default="", description="SaaS application name.")    
    uuid: str | None = Field(max_length=36, default="", description="Universally Unique Identifier (UUID; automatically assigned but can be manually reset).")    
    status: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable setting.")    
    type: Literal["built-in", "customized"] | None = Field(default="customized", description="SaaS application type.")    
    casb_name: str | None = Field(max_length=79, default="", description="SaaS application signature name.")    
    description: str | None = Field(max_length=63, default="", description="SaaS application description.")    
    domains: list[Domains] = Field(default=None, description="SaaS application domain list.")    
    output_attributes: list[OutputAttributes] = Field(default=None, description="SaaS application output attributes.")    
    input_attributes: list[InputAttributes] = Field(default=None, description="SaaS application input attributes.")    
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
    "SaasApplicationModel",    "SaasApplicationDomains",    "SaasApplicationOutputAttributes",    "SaasApplicationInputAttributes",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.011219Z
# ============================================================================
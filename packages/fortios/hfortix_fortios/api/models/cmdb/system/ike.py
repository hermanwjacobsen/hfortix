"""
Pydantic Models for CMDB - system/ike

Runtime validation models for system/ike configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class IkeDhGroup1(BaseModel):
    """
    Child table model for dh-group-1.
    
    Diffie-Hellman group 1 (MODP-768).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup2(BaseModel):
    """
    Child table model for dh-group-2.
    
    Diffie-Hellman group 2 (MODP-1024).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup5(BaseModel):
    """
    Child table model for dh-group-5.
    
    Diffie-Hellman group 5 (MODP-1536).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup14(BaseModel):
    """
    Child table model for dh-group-14.
    
    Diffie-Hellman group 14 (MODP-2048).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup15(BaseModel):
    """
    Child table model for dh-group-15.
    
    Diffie-Hellman group 15 (MODP-3072).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup16(BaseModel):
    """
    Child table model for dh-group-16.
    
    Diffie-Hellman group 16 (MODP-4096).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup17(BaseModel):
    """
    Child table model for dh-group-17.
    
    Diffie-Hellman group 17 (MODP-6144).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup18(BaseModel):
    """
    Child table model for dh-group-18.
    
    Diffie-Hellman group 18 (MODP-8192).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup19(BaseModel):
    """
    Child table model for dh-group-19.
    
    Diffie-Hellman group 19 (EC-P256).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup20(BaseModel):
    """
    Child table model for dh-group-20.
    
    Diffie-Hellman group 20 (EC-P384).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup21(BaseModel):
    """
    Child table model for dh-group-21.
    
    Diffie-Hellman group 21 (EC-P521).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup27(BaseModel):
    """
    Child table model for dh-group-27.
    
    Diffie-Hellman group 27 (EC-P224BP).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup28(BaseModel):
    """
    Child table model for dh-group-28.
    
    Diffie-Hellman group 28 (EC-P256BP).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup29(BaseModel):
    """
    Child table model for dh-group-29.
    
    Diffie-Hellman group 29 (EC-P384BP).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup30(BaseModel):
    """
    Child table model for dh-group-30.
    
    Diffie-Hellman group 30 (EC-P512BP).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup31(BaseModel):
    """
    Child table model for dh-group-31.
    
    Diffie-Hellman group 31 (EC-X25519).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
class IkeDhGroup32(BaseModel):
    """
    Child table model for dh-group-32.
    
    Diffie-Hellman group 32 (EC-X448).
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    mode: Literal["software", "hardware", "global"] | None = Field(default="global", description="Use software (CPU) or hardware (CPX) to perform calculations for this Diffie-Hellman group.")    
    keypair_cache: Literal["global", "custom"] | None = Field(default="global", description="Configure custom key pair cache size for this Diffie-Hellman group.")    
    keypair_count: int | None = Field(ge=0, le=50000, default=0, description="Number of key pairs to pre-generate for this Diffie-Hellman group (per-worker).")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class IkeModel(BaseModel):
    """
    Pydantic model for system/ike configuration.
    
    Configure IKE global attributes.
    
    Validation Rules:        - embryonic_limit: min=50 max=20000 pattern=        - dh_multiprocess: pattern=        - dh_worker_count: min=1 max=2 pattern=        - dh_mode: pattern=        - dh_keypair_cache: pattern=        - dh_keypair_count: min=0 max=50000 pattern=        - dh_keypair_throttle: pattern=        - dh_group_1: pattern=        - dh_group_2: pattern=        - dh_group_5: pattern=        - dh_group_14: pattern=        - dh_group_15: pattern=        - dh_group_16: pattern=        - dh_group_17: pattern=        - dh_group_18: pattern=        - dh_group_19: pattern=        - dh_group_20: pattern=        - dh_group_21: pattern=        - dh_group_27: pattern=        - dh_group_28: pattern=        - dh_group_29: pattern=        - dh_group_30: pattern=        - dh_group_31: pattern=        - dh_group_32: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    embryonic_limit: int | None = Field(ge=50, le=20000, default=10000, description="Maximum number of IPsec tunnels to negotiate simultaneously.")    
    dh_multiprocess: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable multiprocess Diffie-Hellman daemon for IKE.")    
    dh_worker_count: int | None = Field(ge=1, le=2, default=0, description="Number of Diffie-Hellman workers to start.")    
    dh_mode: Literal["software", "hardware"] | None = Field(default="software", description="Use software (CPU) or hardware (CPX) to perform Diffie-Hellman calculations.")    
    dh_keypair_cache: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Diffie-Hellman key pair cache.")    
    dh_keypair_count: int | None = Field(ge=0, le=50000, default=100, description="Number of key pairs to pre-generate for each Diffie-Hellman group (per-worker).")    
    dh_keypair_throttle: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable Diffie-Hellman key pair cache CPU throttling.")    
    dh_group_1: list[DhGroup1] = Field(default=None, description="Diffie-Hellman group 1 (MODP-768).")    
    dh_group_2: list[DhGroup2] = Field(default=None, description="Diffie-Hellman group 2 (MODP-1024).")    
    dh_group_5: list[DhGroup5] = Field(default=None, description="Diffie-Hellman group 5 (MODP-1536).")    
    dh_group_14: list[DhGroup14] = Field(default=None, description="Diffie-Hellman group 14 (MODP-2048).")    
    dh_group_15: list[DhGroup15] = Field(default=None, description="Diffie-Hellman group 15 (MODP-3072).")    
    dh_group_16: list[DhGroup16] = Field(default=None, description="Diffie-Hellman group 16 (MODP-4096).")    
    dh_group_17: list[DhGroup17] = Field(default=None, description="Diffie-Hellman group 17 (MODP-6144).")    
    dh_group_18: list[DhGroup18] = Field(default=None, description="Diffie-Hellman group 18 (MODP-8192).")    
    dh_group_19: list[DhGroup19] = Field(default=None, description="Diffie-Hellman group 19 (EC-P256).")    
    dh_group_20: list[DhGroup20] = Field(default=None, description="Diffie-Hellman group 20 (EC-P384).")    
    dh_group_21: list[DhGroup21] = Field(default=None, description="Diffie-Hellman group 21 (EC-P521).")    
    dh_group_27: list[DhGroup27] = Field(default=None, description="Diffie-Hellman group 27 (EC-P224BP).")    
    dh_group_28: list[DhGroup28] = Field(default=None, description="Diffie-Hellman group 28 (EC-P256BP).")    
    dh_group_29: list[DhGroup29] = Field(default=None, description="Diffie-Hellman group 29 (EC-P384BP).")    
    dh_group_30: list[DhGroup30] = Field(default=None, description="Diffie-Hellman group 30 (EC-P512BP).")    
    dh_group_31: list[DhGroup31] = Field(default=None, description="Diffie-Hellman group 31 (EC-X25519).")    
    dh_group_32: list[DhGroup32] = Field(default=None, description="Diffie-Hellman group 32 (EC-X448).")    
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
    "IkeModel",    "IkeDhGroup1",    "IkeDhGroup2",    "IkeDhGroup5",    "IkeDhGroup14",    "IkeDhGroup15",    "IkeDhGroup16",    "IkeDhGroup17",    "IkeDhGroup18",    "IkeDhGroup19",    "IkeDhGroup20",    "IkeDhGroup21",    "IkeDhGroup27",    "IkeDhGroup28",    "IkeDhGroup29",    "IkeDhGroup30",    "IkeDhGroup31",    "IkeDhGroup32",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:54.461615Z
# ============================================================================
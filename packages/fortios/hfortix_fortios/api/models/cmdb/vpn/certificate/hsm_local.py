"""
Pydantic Models for CMDB - vpn/certificate/hsm_local

Runtime validation models for vpn/certificate/hsm_local configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class HsmLocalDetails(BaseModel):
    """
    Child table model for details.
    
    Print hsm-local certificate detailed information.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    <certficate name>: Any = Field(default=None, description="Hsm-local certificate name.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class HsmLocalGch_cryptokey_algorithmEnum(str, Enum):
    """Allowed values for gch_cryptokey_algorithm field."""
    RSA_SIGN_PKCS1_2048_SHA256 = "rsa-sign-pkcs1-2048-sha256"    RSA_SIGN_PKCS1_3072_SHA256 = "rsa-sign-pkcs1-3072-sha256"    RSA_SIGN_PKCS1_4096_SHA256 = "rsa-sign-pkcs1-4096-sha256"    RSA_SIGN_PKCS1_4096_SHA512 = "rsa-sign-pkcs1-4096-sha512"    RSA_SIGN_PSS_2048_SHA256 = "rsa-sign-pss-2048-sha256"    RSA_SIGN_PSS_3072_SHA256 = "rsa-sign-pss-3072-sha256"    RSA_SIGN_PSS_4096_SHA256 = "rsa-sign-pss-4096-sha256"    RSA_SIGN_PSS_4096_SHA512 = "rsa-sign-pss-4096-sha512"    EC_SIGN_P256_SHA256 = "ec-sign-p256-sha256"    EC_SIGN_P384_SHA384 = "ec-sign-p384-sha384"    EC_SIGN_SECP256K1_SHA256 = "ec-sign-secp256k1-sha256"

# ============================================================================
# Main Model
# ============================================================================

class HsmLocalModel(BaseModel):
    """
    Pydantic model for vpn/certificate/hsm_local configuration.
    
    Local certificates whose keys are stored on HSM.
    
    Validation Rules:        - name: max_length=35 pattern=        - comments: max_length=511 pattern=        - vendor: pattern=        - api_version: pattern=        - certificate: pattern=        - range: pattern=        - source: pattern=        - gch_url: max_length=1024 pattern=        - gch_project: max_length=31 pattern=        - gch_location: max_length=63 pattern=        - gch_keyring: max_length=63 pattern=        - gch_cryptokey: max_length=63 pattern=        - gch_cryptokey_version: max_length=31 pattern=        - gch_cloud_service_name: max_length=35 pattern=        - gch_cryptokey_algorithm: pattern=        - details: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str = Field(max_length=35, default="", description="Name.")    
    comments: str | None = Field(max_length=511, default="", description="Comment.")    
    vendor: Literal["unknown", "gch"] = Field(default="unknown", description="HSM vendor.")    
    api_version: Literal["unknown", "gch-default"] | None = Field(default="unknown", description="API version for communicating with HSM.")    
    certificate: str | None = Field(default="", description="PEM format certificate.")    
    range: Literal["global", "vdom"] | None = Field(default="vdom", description="Either a global or VDOM IP address range for the certificate.")    
    source: Literal["factory", "user", "bundle"] | None = Field(default="user", description="Certificate source type.")    
    gch_url: str | None = Field(max_length=1024, default="", description="Google Cloud HSM key URL (e.g. \"https://cloudkms.googleapis.com/v1/projects/sampleproject/locations/samplelocation/keyRings/samplekeyring/cryptoKeys/sampleKeyName/cryptoKeyVersions/1\").")    
    gch_project: str | None = Field(max_length=31, default="", description="Google Cloud HSM project ID.")    
    gch_location: str | None = Field(max_length=63, default="", description="Google Cloud HSM location.")    
    gch_keyring: str | None = Field(max_length=63, default="", description="Google Cloud HSM keyring.")    
    gch_cryptokey: str | None = Field(max_length=63, default="", description="Google Cloud HSM cryptokey.")    
    gch_cryptokey_version: str | None = Field(max_length=31, default="", description="Google Cloud HSM cryptokey version.")    
    gch_cloud_service_name: str | None = Field(max_length=35, default="", description="Cloud service config name to generate access token.")  # datasource: ['system.cloud-service.name']    
    gch_cryptokey_algorithm: GchCryptokeyAlgorithmEnum | None = Field(default="rsa-sign-pkcs1-2048-sha256", description="Google Cloud HSM cryptokey algorithm.")    
    details: list[Details] = Field(default=None, description="Print hsm-local certificate detailed information.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('gch_cloud_service_name')
    @classmethod
    def validate_gch_cloud_service_name(cls, v: Any) -> Any:
        """
        Validate gch_cloud_service_name field.
        
        Datasource: ['system.cloud-service.name']
        
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
    async def validate_gch_cloud_service_name_references(self, client: Any) -> list[str]:
        """
        Validate gch_cloud_service_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/cloud-service        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = HsmLocalModel(
            ...     gch_cloud_service_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_gch_cloud_service_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.certificate.hsm_local.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "gch_cloud_service_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.system.cloud-service.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Gch-Cloud-Service-Name '{value}' not found in "
                "system/cloud-service"
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
        
        errors = await self.validate_gch_cloud_service_name_references(client)
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
    "HsmLocalModel",    "HsmLocalDetails",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:16.270585Z
# ============================================================================
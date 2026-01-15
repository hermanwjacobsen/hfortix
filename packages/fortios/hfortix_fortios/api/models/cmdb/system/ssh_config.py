"""
Pydantic Models for CMDB - system/ssh_config

Runtime validation models for system/ssh_config configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class SshConfigSsh_kex_algoEnum(str, Enum):
    """Allowed values for ssh_kex_algo field."""
    DIFFIE_HELLMAN_GROUP1_SHA1 = "diffie-hellman-group1-sha1"    DIFFIE_HELLMAN_GROUP14_SHA1 = "diffie-hellman-group14-sha1"    DIFFIE_HELLMAN_GROUP14_SHA256 = "diffie-hellman-group14-sha256"    DIFFIE_HELLMAN_GROUP16_SHA512 = "diffie-hellman-group16-sha512"    DIFFIE_HELLMAN_GROUP18_SHA512 = "diffie-hellman-group18-sha512"    DIFFIE_HELLMAN_GROUP_EXCHANGE_SHA1 = "diffie-hellman-group-exchange-sha1"    DIFFIE_HELLMAN_GROUP_EXCHANGE_SHA256 = "diffie-hellman-group-exchange-sha256"    CURVE25519_SHA256LIBSSH_ORG = "curve25519-sha256@libssh.org"    ECDH_SHA2_NISTP256 = "ecdh-sha2-nistp256"    ECDH_SHA2_NISTP384 = "ecdh-sha2-nistp384"    ECDH_SHA2_NISTP521 = "ecdh-sha2-nistp521"
class SshConfigSsh_enc_algoEnum(str, Enum):
    """Allowed values for ssh_enc_algo field."""
    CHACHA20_POLY1305OPENSSH_COM = "chacha20-poly1305@openssh.com"    AES128_CTR = "aes128-ctr"    AES192_CTR = "aes192-ctr"    AES256_CTR = "aes256-ctr"    ARCFOUR256 = "arcfour256"    ARCFOUR128 = "arcfour128"    AES128_CBC = "aes128-cbc"    3DES_CBC = "3des-cbc"    BLOWFISH_CBC = "blowfish-cbc"    CAST128_CBC = "cast128-cbc"    AES192_CBC = "aes192-cbc"    AES256_CBC = "aes256-cbc"    ARCFOUR = "arcfour"    RIJNDAEL_CBCLYSATOR_LIU_SE = "rijndael-cbc@lysator.liu.se"    AES128_GCMOPENSSH_COM = "aes128-gcm@openssh.com"    AES256_GCMOPENSSH_COM = "aes256-gcm@openssh.com"
class SshConfigSsh_mac_algoEnum(str, Enum):
    """Allowed values for ssh_mac_algo field."""
    HMAC_MD5 = "hmac-md5"    HMAC_MD5_ETMOPENSSH_COM = "hmac-md5-etm@openssh.com"    HMAC_MD5_96 = "hmac-md5-96"    HMAC_MD5_96_ETMOPENSSH_COM = "hmac-md5-96-etm@openssh.com"    HMAC_SHA1 = "hmac-sha1"    HMAC_SHA1_ETMOPENSSH_COM = "hmac-sha1-etm@openssh.com"    HMAC_SHA2_256 = "hmac-sha2-256"    HMAC_SHA2_256_ETMOPENSSH_COM = "hmac-sha2-256-etm@openssh.com"    HMAC_SHA2_512 = "hmac-sha2-512"    HMAC_SHA2_512_ETMOPENSSH_COM = "hmac-sha2-512-etm@openssh.com"    HMAC_RIPEMD160 = "hmac-ripemd160"    HMAC_RIPEMD160OPENSSH_COM = "hmac-ripemd160@openssh.com"    HMAC_RIPEMD160_ETMOPENSSH_COM = "hmac-ripemd160-etm@openssh.com"    UMAC_64OPENSSH_COM = "umac-64@openssh.com"    UMAC_128OPENSSH_COM = "umac-128@openssh.com"    UMAC_64_ETMOPENSSH_COM = "umac-64-etm@openssh.com"    UMAC_128_ETMOPENSSH_COM = "umac-128-etm@openssh.com"
class SshConfigSsh_hsk_algoEnum(str, Enum):
    """Allowed values for ssh_hsk_algo field."""
    SSH_RSA = "ssh-rsa"    ECDSA_SHA2_NISTP521 = "ecdsa-sha2-nistp521"    ECDSA_SHA2_NISTP384 = "ecdsa-sha2-nistp384"    ECDSA_SHA2_NISTP256 = "ecdsa-sha2-nistp256"    RSA_SHA2_256 = "rsa-sha2-256"    RSA_SHA2_512 = "rsa-sha2-512"    SSH_ED25519 = "ssh-ed25519"

# ============================================================================
# Main Model
# ============================================================================

class SshConfigModel(BaseModel):
    """
    Pydantic model for system/ssh_config configuration.
    
    Configure SSH config.
    
    Validation Rules:        - ssh_kex_algo: pattern=        - ssh_enc_algo: pattern=        - ssh_mac_algo: pattern=        - ssh_hsk_algo: pattern=        - ssh_hsk_override: pattern=        - ssh_hsk_password: max_length=128 pattern=        - ssh_hsk: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    ssh_kex_algo: list[SshKexAlgo] = Field(default="diffie-hellman-group14-sha256 diffie-hellman-group16-sha512 diffie-hellman-group18-sha512 diffie-hellman-group-exchange-sha256 curve25519-sha256@libssh.org ecdh-sha2-nistp256 ecdh-sha2-nistp384 ecdh-sha2-nistp521", description="Select one or more SSH kex algorithms.")    
    ssh_enc_algo: list[SshEncAlgo] = Field(default="aes256-ctr aes256-gcm@openssh.com", description="Select one or more SSH ciphers.")    
    ssh_mac_algo: list[SshMacAlgo] = Field(default="hmac-sha2-256 hmac-sha2-256-etm@openssh.com hmac-sha2-512 hmac-sha2-512-etm@openssh.com", description="Select one or more SSH MAC algorithms.")    
    ssh_hsk_algo: list[SshHskAlgo] = Field(default="ecdsa-sha2-nistp521 ecdsa-sha2-nistp384 ecdsa-sha2-nistp256 rsa-sha2-256 rsa-sha2-512 ssh-ed25519", description="Select one or more SSH hostkey algorithms.")    
    ssh_hsk_override: Literal["disable", "enable"] | None = Field(default="disable", description="Enable/disable SSH host key override in SSH daemon.")    
    ssh_hsk_password: Any = Field(max_length=128, default=None, description="Password for ssh-hostkey.")    
    ssh_hsk: str = Field(default="", description="Config SSH host key.")    
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
    "SshConfigModel",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T15:11:42.554491Z
# ============================================================================
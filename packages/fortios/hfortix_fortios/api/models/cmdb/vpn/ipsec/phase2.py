"""
Pydantic Models for CMDB - vpn/ipsec/phase2

Runtime validation models for vpn/ipsec/phase2 configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class Phase2ProposalEnum(str, Enum):
    """Allowed values for proposal field."""
    NULL_MD5 = "null-md5"    NULL_SHA1 = "null-sha1"    NULL_SHA256 = "null-sha256"    NULL_SHA384 = "null-sha384"    NULL_SHA512 = "null-sha512"    DES_NULL = "des-null"    DES_MD5 = "des-md5"    DES_SHA1 = "des-sha1"    DES_SHA256 = "des-sha256"    DES_SHA384 = "des-sha384"    DES_SHA512 = "des-sha512"    3DES_NULL = "3des-null"    3DES_MD5 = "3des-md5"    3DES_SHA1 = "3des-sha1"    3DES_SHA256 = "3des-sha256"    3DES_SHA384 = "3des-sha384"    3DES_SHA512 = "3des-sha512"    AES128_NULL = "aes128-null"    AES128_MD5 = "aes128-md5"    AES128_SHA1 = "aes128-sha1"    AES128_SHA256 = "aes128-sha256"    AES128_SHA384 = "aes128-sha384"    AES128_SHA512 = "aes128-sha512"    AES128GCM = "aes128gcm"    AES192_NULL = "aes192-null"    AES192_MD5 = "aes192-md5"    AES192_SHA1 = "aes192-sha1"    AES192_SHA256 = "aes192-sha256"    AES192_SHA384 = "aes192-sha384"    AES192_SHA512 = "aes192-sha512"    AES256_NULL = "aes256-null"    AES256_MD5 = "aes256-md5"    AES256_SHA1 = "aes256-sha1"    AES256_SHA256 = "aes256-sha256"    AES256_SHA384 = "aes256-sha384"    AES256_SHA512 = "aes256-sha512"    AES256GCM = "aes256gcm"    CHACHA20POLY1305 = "chacha20poly1305"    ARIA128_NULL = "aria128-null"    ARIA128_MD5 = "aria128-md5"    ARIA128_SHA1 = "aria128-sha1"    ARIA128_SHA256 = "aria128-sha256"    ARIA128_SHA384 = "aria128-sha384"    ARIA128_SHA512 = "aria128-sha512"    ARIA192_NULL = "aria192-null"    ARIA192_MD5 = "aria192-md5"    ARIA192_SHA1 = "aria192-sha1"    ARIA192_SHA256 = "aria192-sha256"    ARIA192_SHA384 = "aria192-sha384"    ARIA192_SHA512 = "aria192-sha512"    ARIA256_NULL = "aria256-null"    ARIA256_MD5 = "aria256-md5"    ARIA256_SHA1 = "aria256-sha1"    ARIA256_SHA256 = "aria256-sha256"    ARIA256_SHA384 = "aria256-sha384"    ARIA256_SHA512 = "aria256-sha512"    SEED_NULL = "seed-null"    SEED_MD5 = "seed-md5"    SEED_SHA1 = "seed-sha1"    SEED_SHA256 = "seed-sha256"    SEED_SHA384 = "seed-sha384"    SEED_SHA512 = "seed-sha512"
class Phase2DhgrpEnum(str, Enum):
    """Allowed values for dhgrp field."""
    1 = "1"    2 = "2"    5 = "5"    14 = "14"    15 = "15"    16 = "16"    17 = "17"    18 = "18"    19 = "19"    20 = "20"    21 = "21"    27 = "27"    28 = "28"    29 = "29"    30 = "30"    31 = "31"    32 = "32"
class Phase2Addke1Enum(str, Enum):
    """Allowed values for addke1 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase2Addke2Enum(str, Enum):
    """Allowed values for addke2 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase2Addke3Enum(str, Enum):
    """Allowed values for addke3 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase2Addke4Enum(str, Enum):
    """Allowed values for addke4 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase2Addke5Enum(str, Enum):
    """Allowed values for addke5 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase2Addke6Enum(str, Enum):
    """Allowed values for addke6 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase2Addke7Enum(str, Enum):
    """Allowed values for addke7 field."""
    0 = "0"    35 = "35"    36 = "36"    37 = "37"    1080 = "1080"    1081 = "1081"    1082 = "1082"    1083 = "1083"    1084 = "1084"    1085 = "1085"    1089 = "1089"    1090 = "1090"    1091 = "1091"    1092 = "1092"    1093 = "1093"    1094 = "1094"
class Phase2Src_addr_typeEnum(str, Enum):
    """Allowed values for src_addr_type field."""
    SUBNET = "subnet"    RANGE = "range"    IP = "ip"    NAME = "name"
class Phase2Dst_addr_typeEnum(str, Enum):
    """Allowed values for dst_addr_type field."""
    SUBNET = "subnet"    RANGE = "range"    IP = "ip"    NAME = "name"

# ============================================================================
# Main Model
# ============================================================================

class Phase2Model(BaseModel):
    """
    Pydantic model for vpn/ipsec/phase2 configuration.
    
    Configure VPN autokey tunnel.
    
    Validation Rules:        - name: max_length=35 pattern=        - phase1name: max_length=35 pattern=        - dhcp_ipsec: pattern=        - use_natip: pattern=        - selector_match: pattern=        - proposal: pattern=        - pfs: pattern=        - dhgrp: pattern=        - addke1: pattern=        - addke2: pattern=        - addke3: pattern=        - addke4: pattern=        - addke5: pattern=        - addke6: pattern=        - addke7: pattern=        - replay: pattern=        - keepalive: pattern=        - auto_negotiate: pattern=        - add_route: pattern=        - inbound_dscp_copy: pattern=        - keylifeseconds: min=120 max=172800 pattern=        - keylifekbs: min=5120 max=4294967295 pattern=        - keylife_type: pattern=        - single_source: pattern=        - route_overlap: pattern=        - encapsulation: pattern=        - l2tp: pattern=        - comments: max_length=255 pattern=        - initiator_ts_narrow: pattern=        - diffserv: pattern=        - diffservcode: pattern=        - protocol: min=0 max=255 pattern=        - src_name: max_length=79 pattern=        - src_name6: max_length=79 pattern=        - src_addr_type: pattern=        - src_start_ip: pattern=        - src_start_ip6: pattern=        - src_end_ip: pattern=        - src_end_ip6: pattern=        - src_subnet: pattern=        - src_subnet6: pattern=        - src_port: min=0 max=65535 pattern=        - dst_name: max_length=79 pattern=        - dst_name6: max_length=79 pattern=        - dst_addr_type: pattern=        - dst_start_ip: pattern=        - dst_start_ip6: pattern=        - dst_end_ip: pattern=        - dst_end_ip6: pattern=        - dst_subnet: pattern=        - dst_subnet6: pattern=        - dst_port: min=0 max=65535 pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    name: str | None = Field(max_length=35, default="", description="IPsec tunnel name.")    
    phase1name: str = Field(max_length=35, default="", description="Phase 1 determines the options required for phase 2.")  # datasource: ['vpn.ipsec.phase1.name']    
    dhcp_ipsec: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable DHCP-IPsec.")    
    use_natip: Literal["enable", "disable"] | None = Field(default="enable", description="Enable to use the FortiGate public IP as the source selector when outbound NAT is used.")    
    selector_match: Literal["exact", "subset", "auto"] | None = Field(default="auto", description="Match type to use when comparing selectors.")    
    proposal: list[Proposal] = Field(default="", description="Phase2 proposal.")    
    pfs: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable PFS feature.")    
    dhgrp: list[Dhgrp] = Field(default="20", description="Phase2 DH group.")    
    addke1: list[Addke1] = Field(default="", description="phase2 ADDKE1 group.")    
    addke2: list[Addke2] = Field(default="", description="phase2 ADDKE2 group.")    
    addke3: list[Addke3] = Field(default="", description="phase2 ADDKE3 group.")    
    addke4: list[Addke4] = Field(default="", description="phase2 ADDKE4 group.")    
    addke5: list[Addke5] = Field(default="", description="phase2 ADDKE5 group.")    
    addke6: list[Addke6] = Field(default="", description="phase2 ADDKE6 group.")    
    addke7: list[Addke7] = Field(default="", description="phase2 ADDKE7 group.")    
    replay: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable replay detection.")    
    keepalive: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable keep alive.")    
    auto_negotiate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPsec SA auto-negotiation.")    
    add_route: Literal["phase1", "enable", "disable"] | None = Field(default="phase1", description="Enable/disable automatic route addition.")    
    inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = Field(default="phase1", description="Enable/disable copying of the DSCP in the ESP header to the inner IP header.")    
    keylifeseconds: int | None = Field(ge=120, le=172800, default=43200, description="Phase2 key life in time in seconds (120 - 172800).")    
    keylifekbs: int | None = Field(ge=5120, le=4294967295, default=5120, description="Phase2 key life in number of kilobytes of traffic (5120 - 4294967295).")    
    keylife_type: Literal["seconds", "kbs", "both"] | None = Field(default="seconds", description="Keylife type.")    
    single_source: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable single source IP restriction.")    
    route_overlap: Literal["use-old", "use-new", "allow"] | None = Field(default="use-new", description="Action for overlapping routes.")    
    encapsulation: Literal["tunnel-mode", "transport-mode"] | None = Field(default="tunnel-mode", description="ESP encapsulation mode.")    
    l2tp: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable L2TP over IPsec.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    initiator_ts_narrow: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable traffic selector narrowing for IKEv2 initiator.")    
    diffserv: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable applying DSCP value to the IPsec tunnel outer IP header.")    
    diffservcode: str | None = Field(default="", description="DSCP value to be applied to the IPsec tunnel outer IP header.")    
    protocol: int | None = Field(ge=0, le=255, default=0, description="Quick mode protocol selector (1 - 255 or 0 for all).")    
    src_name: str = Field(max_length=79, default="", description="Local proxy ID name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    src_name6: str = Field(max_length=79, default="", description="Local proxy ID name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']    
    src_addr_type: SrcAddrTypeEnum | None = Field(default="subnet", description="Local proxy ID type.")    
    src_start_ip: str | None = Field(default="0.0.0.0", description="Local proxy ID start.")    
    src_start_ip6: str | None = Field(default="::", description="Local proxy ID IPv6 start.")    
    src_end_ip: str | None = Field(default="0.0.0.0", description="Local proxy ID end.")    
    src_end_ip6: str | None = Field(default="::", description="Local proxy ID IPv6 end.")    
    src_subnet: Any = Field(default="0.0.0.0 0.0.0.0", description="Local proxy ID subnet.")    
    src_subnet6: str | None = Field(default="::/0", description="Local proxy ID IPv6 subnet.")    
    src_port: int | None = Field(ge=0, le=65535, default=0, description="Quick mode source port (1 - 65535 or 0 for all).")    
    dst_name: str = Field(max_length=79, default="", description="Remote proxy ID name.")  # datasource: ['firewall.address.name', 'firewall.addrgrp.name']    
    dst_name6: str = Field(max_length=79, default="", description="Remote proxy ID name.")  # datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']    
    dst_addr_type: DstAddrTypeEnum | None = Field(default="subnet", description="Remote proxy ID type.")    
    dst_start_ip: str | None = Field(default="0.0.0.0", description="Remote proxy ID IPv4 start.")    
    dst_start_ip6: str | None = Field(default="::", description="Remote proxy ID IPv6 start.")    
    dst_end_ip: str | None = Field(default="0.0.0.0", description="Remote proxy ID IPv4 end.")    
    dst_end_ip6: str | None = Field(default="::", description="Remote proxy ID IPv6 end.")    
    dst_subnet: Any = Field(default="0.0.0.0 0.0.0.0", description="Remote proxy ID IPv4 subnet.")    
    dst_subnet6: str | None = Field(default="::/0", description="Remote proxy ID IPv6 subnet.")    
    dst_port: int | None = Field(ge=0, le=65535, default=0, description="Quick mode destination port (1 - 65535 or 0 for all).")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('phase1name')
    @classmethod
    def validate_phase1name(cls, v: Any) -> Any:
        """
        Validate phase1name field.
        
        Datasource: ['vpn.ipsec.phase1.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('src_name')
    @classmethod
    def validate_src_name(cls, v: Any) -> Any:
        """
        Validate src_name field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('src_name6')
    @classmethod
    def validate_src_name6(cls, v: Any) -> Any:
        """
        Validate src_name6 field.
        
        Datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dst_name')
    @classmethod
    def validate_dst_name(cls, v: Any) -> Any:
        """
        Validate dst_name field.
        
        Datasource: ['firewall.address.name', 'firewall.addrgrp.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('dst_name6')
    @classmethod
    def validate_dst_name6(cls, v: Any) -> Any:
        """
        Validate dst_name6 field.
        
        Datasource: ['firewall.address6.name', 'firewall.addrgrp6.name']
        
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
    async def validate_phase1name_references(self, client: Any) -> list[str]:
        """
        Validate phase1name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - vpn/ipsec/phase1        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase2Model(
            ...     phase1name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_phase1name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase2.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "phase1name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.vpn.ipsec.phase1.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Phase1Name '{value}' not found in "
                "vpn/ipsec/phase1"
            )        
        return errors    
    async def validate_src_name_references(self, client: Any) -> list[str]:
        """
        Validate src_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase2Model(
            ...     src_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_src_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase2.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "src_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Src-Name '{value}' not found in "
                "firewall/address or firewall/addrgrp"
            )        
        return errors    
    async def validate_src_name6_references(self, client: Any) -> list[str]:
        """
        Validate src_name6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase2Model(
            ...     src_name6="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_src_name6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase2.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "src_name6", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address6.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Src-Name6 '{value}' not found in "
                "firewall/address6 or firewall/addrgrp6"
            )        
        return errors    
    async def validate_dst_name_references(self, client: Any) -> list[str]:
        """
        Validate dst_name references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address        - firewall/addrgrp        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase2Model(
            ...     dst_name="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dst_name_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase2.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dst_name", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dst-Name '{value}' not found in "
                "firewall/address or firewall/addrgrp"
            )        
        return errors    
    async def validate_dst_name6_references(self, client: Any) -> list[str]:
        """
        Validate dst_name6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - firewall/address6        - firewall/addrgrp6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = Phase2Model(
            ...     dst_name6="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_dst_name6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.vpn.ipsec.phase2.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "dst_name6", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.firewall.address6.exists(value):
            found = True
        elif await client.api.cmdb.firewall.addrgrp6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Dst-Name6 '{value}' not found in "
                "firewall/address6 or firewall/addrgrp6"
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
        
        errors = await self.validate_phase1name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_src_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_src_name6_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dst_name_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_dst_name6_references(client)
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
    "Phase2Model",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:15.106295Z
# ============================================================================
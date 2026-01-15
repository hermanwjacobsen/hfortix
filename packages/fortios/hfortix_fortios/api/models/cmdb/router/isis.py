"""
Pydantic Models for CMDB - router/isis

Runtime validation models for router/isis configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class IsisIsisNet(BaseModel):
    """
    Child table model for isis-net.
    
    IS-IS net configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="ISIS network ID.")    
    net: str | None = Field(default="", description="IS-IS networks (format = xx.xxxx.  .xxxx.xx.).")
class IsisIsisInterface(BaseModel):
    """
    Child table model for isis-interface.
    
    IS-IS interface configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=15, default="", description="IS-IS interface name.")  # datasource: ['system.interface.name']    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable interface for IS-IS.")    
    status6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 interface for IS-IS.")    
    network_type: Literal["broadcast", "point-to-point", "loopback"] | None = Field(default="", description="IS-IS interface's network type.")    
    circuit_type: Literal["level-1-2", "level-1", "level-2"] | None = Field(default="level-1-2", description="IS-IS interface's circuit type.")    
    csnp_interval_l1: int | None = Field(ge=1, le=65535, default=10, description="Level 1 CSNP interval.")    
    csnp_interval_l2: int | None = Field(ge=1, le=65535, default=10, description="Level 2 CSNP interval.")    
    hello_interval_l1: int | None = Field(ge=0, le=65535, default=10, description="Level 1 hello interval.")    
    hello_interval_l2: int | None = Field(ge=0, le=65535, default=10, description="Level 2 hello interval.")    
    hello_multiplier_l1: int | None = Field(ge=2, le=100, default=3, description="Level 1 multiplier for Hello holding time.")    
    hello_multiplier_l2: int | None = Field(ge=2, le=100, default=3, description="Level 2 multiplier for Hello holding time.")    
    hello_padding: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable padding to IS-IS hello packets.")    
    lsp_interval: int | None = Field(ge=1, le=4294967295, default=33, description="LSP transmission interval (milliseconds).")    
    lsp_retransmit_interval: int | None = Field(ge=1, le=65535, default=5, description="LSP retransmission interval (sec).")    
    metric_l1: int | None = Field(ge=1, le=63, default=10, description="Level 1 metric for interface.")    
    metric_l2: int | None = Field(ge=1, le=63, default=10, description="Level 2 metric for interface.")    
    wide_metric_l1: int | None = Field(ge=1, le=16777214, default=10, description="Level 1 wide metric for interface.")    
    wide_metric_l2: int | None = Field(ge=1, le=16777214, default=10, description="Level 2 wide metric for interface.")    
    auth_password_l1: Any = Field(max_length=128, default=None, description="Authentication password for level 1 PDUs.")    
    auth_password_l2: Any = Field(max_length=128, default=None, description="Authentication password for level 2 PDUs.")    
    auth_keychain_l1: str | None = Field(max_length=35, default="", description="Authentication key-chain for level 1 PDUs.")  # datasource: ['router.key-chain.name']    
    auth_keychain_l2: str | None = Field(max_length=35, default="", description="Authentication key-chain for level 2 PDUs.")  # datasource: ['router.key-chain.name']    
    auth_send_only_l1: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication send-only for level 1 PDUs.")    
    auth_send_only_l2: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable authentication send-only for level 2 PDUs.")    
    auth_mode_l1: Literal["md5", "password"] | None = Field(default="password", description="Level 1 authentication mode.")    
    auth_mode_l2: Literal["md5", "password"] | None = Field(default="password", description="Level 2 authentication mode.")    
    priority_l1: int | None = Field(ge=0, le=127, default=64, description="Level 1 priority.")    
    priority_l2: int | None = Field(ge=0, le=127, default=64, description="Level 2 priority.")    
    mesh_group: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IS-IS mesh group.")    
    mesh_group_id: int | None = Field(ge=0, le=4294967295, default=0, description="Mesh group ID <0-4294967295>, 0: mesh-group blocked.")
class IsisSummaryAddress(BaseModel):
    """
    Child table model for summary-address.
    
    IS-IS summary addresses.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Summary address entry ID.")    
    prefix: Any = Field(default="0.0.0.0 0.0.0.0", description="Prefix.")    
    level: Literal["level-1-2", "level-1", "level-2"] | None = Field(default="level-2", description="Level.")
class IsisSummaryAddress6(BaseModel):
    """
    Child table model for summary-address6.
    
    IS-IS IPv6 summary address.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Prefix entry ID.")    
    prefix6: str = Field(default="::/0", description="IPv6 prefix.")    
    level: Literal["level-1-2", "level-1", "level-2"] | None = Field(default="level-2", description="Level.")
class IsisRedistribute(BaseModel):
    """
    Child table model for redistribute.
    
    IS-IS redistribute protocols.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    protocol: str = Field(max_length=35, default="", description="Protocol name.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    metric: int | None = Field(ge=0, le=4261412864, default=0, description="Metric.")    
    metric_type: Literal["external", "internal"] | None = Field(default="internal", description="Metric type.")    
    level: Literal["level-1-2", "level-1", "level-2"] | None = Field(default="level-2", description="Level.")    
    routemap: str | None = Field(max_length=35, default="", description="Route map name.")  # datasource: ['router.route-map.name']
class IsisRedistribute6(BaseModel):
    """
    Child table model for redistribute6.
    
    IS-IS IPv6 redistribution for routing protocols.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    protocol: str = Field(max_length=35, default="", description="Protocol name.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redistribution.")    
    metric: int | None = Field(ge=0, le=4261412864, default=0, description="Metric.")    
    metric_type: Literal["external", "internal"] | None = Field(default="internal", description="Metric type.")    
    level: Literal["level-1-2", "level-1", "level-2"] | None = Field(default="level-2", description="Level.")    
    routemap: str | None = Field(max_length=35, default="", description="Route map name.")  # datasource: ['router.route-map.name']
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class IsisMetric_styleEnum(str, Enum):
    """Allowed values for metric_style field."""
    NARROW = "narrow"    WIDE = "wide"    TRANSITION = "transition"    NARROW_TRANSITION = "narrow-transition"    NARROW_TRANSITION_L1 = "narrow-transition-l1"    NARROW_TRANSITION_L2 = "narrow-transition-l2"    WIDE_L1 = "wide-l1"    WIDE_L2 = "wide-l2"    WIDE_TRANSITION = "wide-transition"    WIDE_TRANSITION_L1 = "wide-transition-l1"    WIDE_TRANSITION_L2 = "wide-transition-l2"    TRANSITION_L1 = "transition-l1"    TRANSITION_L2 = "transition-l2"

# ============================================================================
# Main Model
# ============================================================================

class IsisModel(BaseModel):
    """
    Pydantic model for router/isis configuration.
    
    Configure IS-IS.
    
    Validation Rules:        - is_type: pattern=        - adv_passive_only: pattern=        - adv_passive_only6: pattern=        - auth_mode_l1: pattern=        - auth_mode_l2: pattern=        - auth_password_l1: max_length=128 pattern=        - auth_password_l2: max_length=128 pattern=        - auth_keychain_l1: max_length=35 pattern=        - auth_keychain_l2: max_length=35 pattern=        - auth_sendonly_l1: pattern=        - auth_sendonly_l2: pattern=        - ignore_lsp_errors: pattern=        - lsp_gen_interval_l1: min=1 max=120 pattern=        - lsp_gen_interval_l2: min=1 max=120 pattern=        - lsp_refresh_interval: min=1 max=65535 pattern=        - max_lsp_lifetime: min=350 max=65535 pattern=        - spf_interval_exp_l1: pattern=        - spf_interval_exp_l2: pattern=        - dynamic_hostname: pattern=        - adjacency_check: pattern=        - adjacency_check6: pattern=        - overload_bit: pattern=        - overload_bit_suppress: pattern=        - overload_bit_on_startup: min=5 max=86400 pattern=        - default_originate: pattern=        - default_originate6: pattern=        - metric_style: pattern=        - redistribute_l1: pattern=        - redistribute_l1_list: max_length=35 pattern=        - redistribute_l2: pattern=        - redistribute_l2_list: max_length=35 pattern=        - redistribute6_l1: pattern=        - redistribute6_l1_list: max_length=35 pattern=        - redistribute6_l2: pattern=        - redistribute6_l2_list: max_length=35 pattern=        - isis_net: pattern=        - isis_interface: pattern=        - summary_address: pattern=        - summary_address6: pattern=        - redistribute: pattern=        - redistribute6: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = Field(default="level-1-2", description="IS type.")    
    adv_passive_only: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IS-IS advertisement of passive interfaces only.")    
    adv_passive_only6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 IS-IS advertisement of passive interfaces only.")    
    auth_mode_l1: Literal["password", "md5"] | None = Field(default="password", description="Level 1 authentication mode.")    
    auth_mode_l2: Literal["password", "md5"] | None = Field(default="password", description="Level 2 authentication mode.")    
    auth_password_l1: Any = Field(max_length=128, default=None, description="Authentication password for level 1 PDUs.")    
    auth_password_l2: Any = Field(max_length=128, default=None, description="Authentication password for level 2 PDUs.")    
    auth_keychain_l1: str | None = Field(max_length=35, default="", description="Authentication key-chain for level 1 PDUs.")  # datasource: ['router.key-chain.name']    
    auth_keychain_l2: str | None = Field(max_length=35, default="", description="Authentication key-chain for level 2 PDUs.")  # datasource: ['router.key-chain.name']    
    auth_sendonly_l1: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable level 1 authentication send-only.")    
    auth_sendonly_l2: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable level 2 authentication send-only.")    
    ignore_lsp_errors: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable ignoring of LSP errors with bad checksums.")    
    lsp_gen_interval_l1: int | None = Field(ge=1, le=120, default=30, description="Minimum interval for level 1 LSP regenerating.")    
    lsp_gen_interval_l2: int | None = Field(ge=1, le=120, default=30, description="Minimum interval for level 2 LSP regenerating.")    
    lsp_refresh_interval: int | None = Field(ge=1, le=65535, default=900, description="LSP refresh time in seconds.")    
    max_lsp_lifetime: int | None = Field(ge=350, le=65535, default=1200, description="Maximum LSP lifetime in seconds.")    
    spf_interval_exp_l1: str | None = Field(default="", description="Level 1 SPF calculation delay.")    
    spf_interval_exp_l2: str | None = Field(default="", description="Level 2 SPF calculation delay.")    
    dynamic_hostname: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable dynamic hostname.")    
    adjacency_check: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adjacency check.")    
    adjacency_check6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable IPv6 adjacency check.")    
    overload_bit: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable signal other routers not to use us in SPF.")    
    overload_bit_suppress: list[OverloadBitSuppress] = Field(default="", description="Suppress overload-bit for the specific prefixes.")    
    overload_bit_on_startup: int | None = Field(ge=5, le=86400, default=0, description="Overload-bit only temporarily after reboot.")    
    default_originate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable distribution of default route information.")    
    default_originate6: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable distribution of default IPv6 route information.")    
    metric_style: MetricStyleEnum | None = Field(default="narrow", description="Use old-style (ISO 10589) or new-style packet formats.")    
    redistribute_l1: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redistribution of level 1 routes into level 2.")    
    redistribute_l1_list: str | None = Field(max_length=35, default="", description="Access-list for route redistribution from l1 to l2.")  # datasource: ['router.access-list.name']    
    redistribute_l2: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redistribution of level 2 routes into level 1.")    
    redistribute_l2_list: str | None = Field(max_length=35, default="", description="Access-list for route redistribution from l2 to l1.")  # datasource: ['router.access-list.name']    
    redistribute6_l1: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redistribution of level 1 IPv6 routes into level 2.")    
    redistribute6_l1_list: str | None = Field(max_length=35, default="", description="Access-list for IPv6 route redistribution from l1 to l2.")  # datasource: ['router.access-list6.name']    
    redistribute6_l2: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable redistribution of level 2 IPv6 routes into level 1.")    
    redistribute6_l2_list: str | None = Field(max_length=35, default="", description="Access-list for IPv6 route redistribution from l2 to l1.")  # datasource: ['router.access-list6.name']    
    isis_net: list[IsisNet] = Field(default=None, description="IS-IS net configuration.")    
    isis_interface: list[IsisInterface] = Field(default=None, description="IS-IS interface configuration.")    
    summary_address: list[SummaryAddress] = Field(default=None, description="IS-IS summary addresses.")    
    summary_address6: list[SummaryAddress6] = Field(default=None, description="IS-IS IPv6 summary address.")    
    redistribute: list[Redistribute] = Field(default=None, description="IS-IS redistribute protocols.")    
    redistribute6: list[Redistribute6] = Field(default=None, description="IS-IS IPv6 redistribution for routing protocols.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('auth_keychain_l1')
    @classmethod
    def validate_auth_keychain_l1(cls, v: Any) -> Any:
        """
        Validate auth_keychain_l1 field.
        
        Datasource: ['router.key-chain.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('auth_keychain_l2')
    @classmethod
    def validate_auth_keychain_l2(cls, v: Any) -> Any:
        """
        Validate auth_keychain_l2 field.
        
        Datasource: ['router.key-chain.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('redistribute_l1_list')
    @classmethod
    def validate_redistribute_l1_list(cls, v: Any) -> Any:
        """
        Validate redistribute_l1_list field.
        
        Datasource: ['router.access-list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('redistribute_l2_list')
    @classmethod
    def validate_redistribute_l2_list(cls, v: Any) -> Any:
        """
        Validate redistribute_l2_list field.
        
        Datasource: ['router.access-list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('redistribute6_l1_list')
    @classmethod
    def validate_redistribute6_l1_list(cls, v: Any) -> Any:
        """
        Validate redistribute6_l1_list field.
        
        Datasource: ['router.access-list6.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('redistribute6_l2_list')
    @classmethod
    def validate_redistribute6_l2_list(cls, v: Any) -> Any:
        """
        Validate redistribute6_l2_list field.
        
        Datasource: ['router.access-list6.name']
        
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
    async def validate_auth_keychain_l1_references(self, client: Any) -> list[str]:
        """
        Validate auth_keychain_l1 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/key-chain        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     auth_keychain_l1="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_keychain_l1_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_keychain_l1", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.key-chain.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Keychain-L1 '{value}' not found in "
                "router/key-chain"
            )        
        return errors    
    async def validate_auth_keychain_l2_references(self, client: Any) -> list[str]:
        """
        Validate auth_keychain_l2 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/key-chain        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     auth_keychain_l2="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_auth_keychain_l2_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "auth_keychain_l2", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.key-chain.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Auth-Keychain-L2 '{value}' not found in "
                "router/key-chain"
            )        
        return errors    
    async def validate_redistribute_l1_list_references(self, client: Any) -> list[str]:
        """
        Validate redistribute_l1_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/access-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     redistribute_l1_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_redistribute_l1_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "redistribute_l1_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.access-list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Redistribute-L1-List '{value}' not found in "
                "router/access-list"
            )        
        return errors    
    async def validate_redistribute_l2_list_references(self, client: Any) -> list[str]:
        """
        Validate redistribute_l2_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/access-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     redistribute_l2_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_redistribute_l2_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "redistribute_l2_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.access-list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Redistribute-L2-List '{value}' not found in "
                "router/access-list"
            )        
        return errors    
    async def validate_redistribute6_l1_list_references(self, client: Any) -> list[str]:
        """
        Validate redistribute6_l1_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/access-list6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     redistribute6_l1_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_redistribute6_l1_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "redistribute6_l1_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.access-list6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Redistribute6-L1-List '{value}' not found in "
                "router/access-list6"
            )        
        return errors    
    async def validate_redistribute6_l2_list_references(self, client: Any) -> list[str]:
        """
        Validate redistribute6_l2_list references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/access-list6        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     redistribute6_l2_list="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_redistribute6_l2_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "redistribute6_l2_list", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.access-list6.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Redistribute6-L2-List '{value}' not found in "
                "router/access-list6"
            )        
        return errors    
    async def validate_isis_interface_references(self, client: Any) -> list[str]:
        """
        Validate isis_interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/key-chain        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     isis_interface=[{"auth-keychain-l2": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_isis_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "isis_interface", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("auth-keychain-l2")
            else:
                value = getattr(item, "auth-keychain-l2", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.key-chain.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Isis-Interface '{value}' not found in "
                    "router/key-chain"
                )        
        return errors    
    async def validate_redistribute_references(self, client: Any) -> list[str]:
        """
        Validate redistribute references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/route-map        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     redistribute=[{"routemap": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_redistribute_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "redistribute", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("routemap")
            else:
                value = getattr(item, "routemap", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.route-map.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Redistribute '{value}' not found in "
                    "router/route-map"
                )        
        return errors    
    async def validate_redistribute6_references(self, client: Any) -> list[str]:
        """
        Validate redistribute6 references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/route-map        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = IsisModel(
            ...     redistribute6=[{"routemap": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_redistribute6_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.isis.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "redistribute6", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("routemap")
            else:
                value = getattr(item, "routemap", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.route-map.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Redistribute6 '{value}' not found in "
                    "router/route-map"
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
        
        errors = await self.validate_auth_keychain_l1_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_auth_keychain_l2_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_redistribute_l1_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_redistribute_l2_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_redistribute6_l1_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_redistribute6_l2_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_isis_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_redistribute_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_redistribute6_references(client)
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
    "IsisModel",    "IsisIsisNet",    "IsisIsisInterface",    "IsisSummaryAddress",    "IsisSummaryAddress6",    "IsisRedistribute",    "IsisRedistribute6",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T22:00:17.158210Z
# ============================================================================
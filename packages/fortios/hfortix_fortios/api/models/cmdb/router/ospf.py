"""
Pydantic Models for CMDB - router/ospf

Runtime validation models for router/ospf configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator
from typing import Any, Literal, Optional
from enum import Enum

# ============================================================================
# Child Table Models
# ============================================================================

class OspfArea(BaseModel):
    """
    Child table model for area.
    
    OSPF area configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: str | None = Field(default="0.0.0.0", description="Area entry IP address.")    
    shortcut: Literal["disable", "enable", "default"] | None = Field(default="disable", description="Enable/disable shortcut option.")    
    authentication: Literal["none", "text", "message-digest"] | None = Field(default="none", description="Authentication type.")    
    default_cost: int | None = Field(ge=0, le=4294967295, default=10, description="Summary default cost of stub or NSSA area.")    
    nssa_translator_role: Literal["candidate", "never", "always"] | None = Field(default="candidate", description="NSSA translator role type.")    
    stub_type: Literal["no-summary", "summary"] | None = Field(default="summary", description="Stub summary setting.")    
    type: Literal["regular", "nssa", "stub"] | None = Field(default="regular", description="Area type setting.")    
    nssa_default_information_originate: Literal["enable", "always", "disable"] | None = Field(default="disable", description="Redistribute, advertise, or do not originate Type-7 default route into NSSA area.")    
    nssa_default_information_originate_metric: int | None = Field(ge=0, le=16777214, default=10, description="OSPF default metric.")    
    nssa_default_information_originate_metric_type: Literal["1", "2"] | None = Field(default="2", description="OSPF metric type for default routes.")    
    nssa_redistribution: Literal["enable", "disable"] | None = Field(default="enable", description="Enable/disable redistribute into NSSA area.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    range: list[Range] = Field(default=None, description="OSPF area range configuration.")    
    virtual_link: list[VirtualLink] = Field(default=None, description="OSPF virtual link configuration.")    
    filter_list: list[FilterList] = Field(default=None, description="OSPF area filter-list configuration.")
class OspfOspfInterface(BaseModel):
    """
    Child table model for ospf-interface.
    
    OSPF interface configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str | None = Field(max_length=35, default="", description="Interface entry name.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")    
    interface: str = Field(max_length=15, default="", description="Configuration interface name.")  # datasource: ['system.interface.name']    
    ip: str | None = Field(default="0.0.0.0", description="IP address.")    
    linkdown_fast_failover: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable fast link failover.")    
    authentication: Literal["none", "text", "message-digest"] | None = Field(default="none", description="Authentication type.")    
    authentication_key: Any = Field(max_length=8, default=None, description="Authentication key.")    
    keychain: str | None = Field(max_length=35, default="", description="Message-digest key-chain name.")  # datasource: ['router.key-chain.name']    
    prefix_length: int | None = Field(ge=0, le=32, default=0, description="Prefix length.")    
    retransmit_interval: int | None = Field(ge=1, le=65535, default=5, description="Retransmit interval.")    
    transmit_delay: int | None = Field(ge=1, le=65535, default=1, description="Transmit delay.")    
    cost: int | None = Field(ge=0, le=65535, default=0, description="Cost of the interface, value range from 0 to 65535, 0 means auto-cost.")    
    priority: int | None = Field(ge=0, le=255, default=1, description="Priority.")    
    dead_interval: int | None = Field(ge=0, le=65535, default=0, description="Dead interval.")    
    hello_interval: int | None = Field(ge=0, le=65535, default=0, description="Hello interval.")    
    hello_multiplier: int | None = Field(ge=3, le=10, default=0, description="Number of hello packets within dead interval.")    
    database_filter_out: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable control of flooding out LSAs.")    
    mtu: int | None = Field(ge=576, le=65535, default=0, description="MTU for database description packets.")    
    mtu_ignore: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable ignore MTU.")    
    network_type: NetworkTypeEnum | None = Field(default="broadcast", description="Network type.")    
    bfd: Literal["global", "enable", "disable"] | None = Field(default="global", description="Bidirectional Forwarding Detection (BFD).")    
    status: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable status.")    
    resync_timeout: int | None = Field(ge=1, le=3600, default=40, description="Graceful restart neighbor resynchronization timeout.")    
    md5_keys: list[Md5Keys] = Field(default=None, description="MD5 key.")
class OspfNetwork(BaseModel):
    """
    Child table model for network.
    
    OSPF network configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Network entry ID.")    
    prefix: str = Field(default="0.0.0.0 0.0.0.0", description="Prefix.")    
    area: str = Field(default="0.0.0.0", description="Attach the network to area.")    
    comments: str | None = Field(max_length=255, default=None, description="Comment.")
class OspfNeighbor(BaseModel):
    """
    Child table model for neighbor.
    
    OSPF neighbor configuration are used when OSPF runs on non-broadcast media.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Neighbor entry ID.")    
    ip: str = Field(default="0.0.0.0", description="Interface IP address of the neighbor.")    
    poll_interval: int | None = Field(ge=1, le=65535, default=10, description="Poll interval time in seconds.")    
    cost: int | None = Field(ge=0, le=65535, default=0, description="Cost of the interface, value range from 0 to 65535, 0 means auto-cost.")    
    priority: int | None = Field(ge=0, le=255, default=1, description="Priority.")
class OspfPassiveInterface(BaseModel):
    """
    Child table model for passive-interface.
    
    Passive interface configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=79, default="", description="Passive interface name.")  # datasource: ['system.interface.name']
class OspfSummaryAddress(BaseModel):
    """
    Child table model for summary-address.
    
    IP address summary configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Summary address entry ID.")    
    prefix: str = Field(default="0.0.0.0 0.0.0.0", description="Prefix.")    
    tag: int | None = Field(ge=0, le=4294967295, default=0, description="Tag value.")    
    advertise: Literal["disable", "enable"] | None = Field(default="enable", description="Enable/disable advertise status.")
class OspfDistributeList(BaseModel):
    """
    Child table model for distribute-list.
    
    Distribute list configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int | None = Field(ge=0, le=4294967295, default=0, description="Distribute list entry ID.")    
    access_list: str = Field(max_length=35, default="", description="Access list name.")  # datasource: ['router.access-list.name']    
    protocol: Literal["connected", "static", "rip"] = Field(default="connected", description="Protocol type.")
class OspfRedistribute(BaseModel):
    """
    Child table model for redistribute.
    
    Redistribute configuration.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    name: str = Field(max_length=35, default="", description="Redistribute name.")    
    status: Literal["enable", "disable"] | None = Field(default="disable", description="Status.")    
    metric: int | None = Field(ge=0, le=16777214, default=0, description="Redistribute metric setting.")    
    routemap: str | None = Field(max_length=35, default="", description="Route map name.")  # datasource: ['router.route-map.name']    
    metric_type: Literal["1", "2"] | None = Field(default="2", description="Metric type.")    
    tag: int | None = Field(ge=0, le=4294967295, default=0, description="Tag value.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================

class OspfAbr_typeEnum(str, Enum):
    """Allowed values for abr_type field."""
    CISCO = "cisco"    IBM = "ibm"    SHORTCUT = "shortcut"    STANDARD = "standard"

# ============================================================================
# Main Model
# ============================================================================

class OspfModel(BaseModel):
    """
    Pydantic model for router/ospf configuration.
    
    Configure OSPF.
    
    Validation Rules:        - abr_type: pattern=        - auto_cost_ref_bandwidth: min=1 max=1000000 pattern=        - distance_external: min=1 max=255 pattern=        - distance_inter_area: min=1 max=255 pattern=        - distance_intra_area: min=1 max=255 pattern=        - database_overflow: pattern=        - database_overflow_max_lsas: min=0 max=4294967295 pattern=        - database_overflow_time_to_recover: min=0 max=65535 pattern=        - default_information_originate: pattern=        - default_information_metric: min=1 max=16777214 pattern=        - default_information_metric_type: pattern=        - default_information_route_map: max_length=35 pattern=        - default_metric: min=1 max=16777214 pattern=        - distance: min=1 max=255 pattern=        - lsa_refresh_interval: min=0 max=5 pattern=        - rfc1583_compatible: pattern=        - router_id: pattern=        - spf_timers: pattern=        - bfd: pattern=        - log_neighbour_changes: pattern=        - distribute_list_in: max_length=35 pattern=        - distribute_route_map_in: max_length=35 pattern=        - restart_mode: pattern=        - restart_period: min=1 max=3600 pattern=        - restart_on_topology_change: pattern=        - area: pattern=        - ospf_interface: pattern=        - network: pattern=        - neighbor: pattern=        - passive_interface: pattern=        - summary_address: pattern=        - distribute_list: pattern=        - redistribute: pattern=    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
        validate_assignment = True  # Validate on attribute assignment
        use_enum_values = True  # Use enum values instead of names
    
    # ========================================================================
    # Model Fields
    # ========================================================================
    
    abr_type: AbrTypeEnum | None = Field(default="standard", description="Area border router type.")    
    auto_cost_ref_bandwidth: int | None = Field(ge=1, le=1000000, default=1000, description="Reference bandwidth in terms of megabits per second.")    
    distance_external: int | None = Field(ge=1, le=255, default=110, description="Administrative external distance.")    
    distance_inter_area: int | None = Field(ge=1, le=255, default=110, description="Administrative inter-area distance.")    
    distance_intra_area: int | None = Field(ge=1, le=255, default=110, description="Administrative intra-area distance.")    
    database_overflow: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable database overflow.")    
    database_overflow_max_lsas: int | None = Field(ge=0, le=4294967295, default=10000, description="Database overflow maximum LSAs.")    
    database_overflow_time_to_recover: int | None = Field(ge=0, le=65535, default=300, description="Database overflow time to recover (sec).")    
    default_information_originate: Literal["enable", "always", "disable"] | None = Field(default="disable", description="Enable/disable generation of default route.")    
    default_information_metric: int | None = Field(ge=1, le=16777214, default=10, description="Default information metric.")    
    default_information_metric_type: Literal["1", "2"] | None = Field(default="2", description="Default information metric type.")    
    default_information_route_map: str | None = Field(max_length=35, default="", description="Default information route map.")  # datasource: ['router.route-map.name']    
    default_metric: int | None = Field(ge=1, le=16777214, default=10, description="Default metric of redistribute routes.")    
    distance: int | None = Field(ge=1, le=255, default=110, description="Distance of the route.")    
    lsa_refresh_interval: int | None = Field(ge=0, le=5, default=5, description="The minimal OSPF LSA update time interval")    
    rfc1583_compatible: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable RFC1583 compatibility.")    
    router_id: str = Field(default="0.0.0.0", description="Router ID.")    
    spf_timers: str | None = Field(default="", description="SPF calculation frequency.")    
    bfd: Literal["enable", "disable"] | None = Field(default="disable", description="Bidirectional Forwarding Detection (BFD).")    
    log_neighbour_changes: Literal["enable", "disable"] | None = Field(default="enable", description="Log of OSPF neighbor changes.")    
    distribute_list_in: str | None = Field(max_length=35, default="", description="Filter incoming routes.")  # datasource: ['router.access-list.name', 'router.prefix-list.name']    
    distribute_route_map_in: str | None = Field(max_length=35, default="", description="Filter incoming external routes by route-map.")  # datasource: ['router.route-map.name']    
    restart_mode: Literal["none", "lls", "graceful-restart"] | None = Field(default="none", description="OSPF restart mode (graceful or LLS).")    
    restart_period: int | None = Field(ge=1, le=3600, default=120, description="Graceful restart period.")    
    restart_on_topology_change: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable continuing graceful restart upon topology change.")    
    area: list[Area] = Field(default=None, description="OSPF area configuration.")    
    ospf_interface: list[OspfInterface] = Field(default=None, description="OSPF interface configuration.")    
    network: list[Network] = Field(default=None, description="OSPF network configuration.")    
    neighbor: list[Neighbor] = Field(default=None, description="OSPF neighbor configuration are used when OSPF runs on non-broadcast media.")    
    passive_interface: list[PassiveInterface] = Field(default=None, description="Passive interface configuration.")    
    summary_address: list[SummaryAddress] = Field(default=None, description="IP address summary configuration.")    
    distribute_list: list[DistributeList] = Field(default=None, description="Distribute list configuration.")    
    redistribute: list[Redistribute] = Field(default=None, description="Redistribute configuration.")    
    # ========================================================================
    # Custom Validators
    # ========================================================================
    
    @field_validator('default_information_route_map')
    @classmethod
    def validate_default_information_route_map(cls, v: Any) -> Any:
        """
        Validate default_information_route_map field.
        
        Datasource: ['router.route-map.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('distribute_list_in')
    @classmethod
    def validate_distribute_list_in(cls, v: Any) -> Any:
        """
        Validate distribute_list_in field.
        
        Datasource: ['router.access-list.name', 'router.prefix-list.name']
        
        Note:
            This validator only checks basic constraints.
            To validate that referenced object exists, query the API.
        """
        # Basic validation passed via Field() constraints
        # Additional datasource validation could be added here
        return v    
    @field_validator('distribute_route_map_in')
    @classmethod
    def validate_distribute_route_map_in(cls, v: Any) -> Any:
        """
        Validate distribute_route_map_in field.
        
        Datasource: ['router.route-map.name']
        
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
    async def validate_default_information_route_map_references(self, client: Any) -> list[str]:
        """
        Validate default_information_route_map references exist in FortiGate.
        
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
            >>> policy = OspfModel(
            ...     default_information_route_map="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_default_information_route_map_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.ospf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "default_information_route_map", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.route-map.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Default-Information-Route-Map '{value}' not found in "
                "router/route-map"
            )        
        return errors    
    async def validate_distribute_list_in_references(self, client: Any) -> list[str]:
        """
        Validate distribute_list_in references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/access-list        - router/prefix-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = OspfModel(
            ...     distribute_list_in="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_distribute_list_in_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.ospf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "distribute_list_in", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.access-list.exists(value):
            found = True
        elif await client.api.cmdb.router.prefix-list.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Distribute-List-In '{value}' not found in "
                "router/access-list or router/prefix-list"
            )        
        return errors    
    async def validate_distribute_route_map_in_references(self, client: Any) -> list[str]:
        """
        Validate distribute_route_map_in references exist in FortiGate.
        
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
            >>> policy = OspfModel(
            ...     distribute_route_map_in="invalid-name",
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_distribute_route_map_in_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.ospf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate scalar field
        value = getattr(self, "distribute_route_map_in", None)
        if not value:
            return errors
        
        # Check all datasource endpoints
        found = False
        if await client.api.cmdb.router.route-map.exists(value):
            found = True
        
        if not found:
            errors.append(
                f"Distribute-Route-Map-In '{value}' not found in "
                "router/route-map"
            )        
        return errors    
    async def validate_ospf_interface_references(self, client: Any) -> list[str]:
        """
        Validate ospf_interface references exist in FortiGate.
        
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
            >>> policy = OspfModel(
            ...     ospf_interface=[{"keychain": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_ospf_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.ospf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "ospf_interface", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("keychain")
            else:
                value = getattr(item, "keychain", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.key-chain.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Ospf-Interface '{value}' not found in "
                    "router/key-chain"
                )        
        return errors    
    async def validate_passive_interface_references(self, client: Any) -> list[str]:
        """
        Validate passive_interface references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - system/interface        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = OspfModel(
            ...     passive_interface=[{"name": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_passive_interface_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.ospf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "passive_interface", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("name")
            else:
                value = getattr(item, "name", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.system.interface.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Passive-Interface '{value}' not found in "
                    "system/interface"
                )        
        return errors    
    async def validate_distribute_list_references(self, client: Any) -> list[str]:
        """
        Validate distribute_list references exist in FortiGate.
        
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
            >>> policy = OspfModel(
            ...     distribute_list=[{"access-list": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_distribute_list_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.ospf.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "distribute_list", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("access-list")
            else:
                value = getattr(item, "access-list", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.access-list.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Distribute-List '{value}' not found in "
                    "router/access-list"
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
            >>> policy = OspfModel(
            ...     redistribute=[{"routemap": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_redistribute_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.ospf.post(policy.to_fortios_dict())
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
        
        errors = await self.validate_default_information_route_map_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_distribute_list_in_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_distribute_route_map_in_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_ospf_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_passive_interface_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_distribute_list_references(client)
        all_errors.extend(errors)        
        errors = await self.validate_redistribute_references(client)
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
    "OspfModel",    "OspfArea",    "OspfOspfInterface",    "OspfNetwork",    "OspfNeighbor",    "OspfPassiveInterface",    "OspfSummaryAddress",    "OspfDistributeList",    "OspfRedistribute",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:55.467994Z
# ============================================================================
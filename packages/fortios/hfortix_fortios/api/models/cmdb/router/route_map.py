"""
Pydantic Models for CMDB - router/route_map

Runtime validation models for router/route_map configuration.
Generated from FortiOS schema version unknown.
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any, Optional

# ============================================================================
# Child Table Models
# ============================================================================

class RouteMapRule(BaseModel):
    """
    Child table model for rule.
    
    Rule.
    """
    
    class Config:
        """Pydantic model configuration."""
        extra = "allow"  # Allow additional fields from API
        str_strip_whitespace = True
    
    id: int = Field(ge=0, le=4294967295, default=0, description="Rule ID.")    
    action: Literal["permit", "deny"] | None = Field(default="permit", description="Action.")    
    match_as_path: str | None = Field(max_length=35, default="", description="Match BGP AS path list.")  # datasource: ['router.aspath-list.name']    
    match_community: str | None = Field(max_length=35, default="", description="Match BGP community list.")  # datasource: ['router.community-list.name']    
    match_extcommunity: str | None = Field(max_length=35, default="", description="Match BGP extended community list.")  # datasource: ['router.extcommunity-list.name']    
    match_community_exact: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable exact matching of communities.")    
    match_extcommunity_exact: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable exact matching of extended communities.")    
    match_origin: MatchOriginEnum | None = Field(default="none", description="Match BGP origin code.")    
    match_interface: str | None = Field(max_length=15, default="", description="Match interface configuration.")  # datasource: ['system.interface.name']    
    match_ip_address: str | None = Field(max_length=35, default="", description="Match IP address permitted by access-list or prefix-list.")  # datasource: ['router.access-list.name', 'router.prefix-list.name']    
    match_ip6_address: str | None = Field(max_length=35, default="", description="Match IPv6 address permitted by access-list6 or prefix-list6.")  # datasource: ['router.access-list6.name', 'router.prefix-list6.name']    
    match_ip_nexthop: str | None = Field(max_length=35, default="", description="Match next hop IP address passed by access-list or prefix-list.")  # datasource: ['router.access-list.name', 'router.prefix-list.name']    
    match_ip6_nexthop: str | None = Field(max_length=35, default="", description="Match next hop IPv6 address passed by access-list6 or prefix-list6.")  # datasource: ['router.access-list6.name', 'router.prefix-list6.name']    
    match_metric: int | None = Field(ge=0, le=4294967295, default="", description="Match metric for redistribute routes.")    
    match_route_type: Literal["external-type1", "external-type2", "none"] | None = Field(default="", description="Match route type.")    
    match_tag: int | None = Field(ge=0, le=4294967295, default="", description="Match tag.")    
    match_vrf: int | None = Field(ge=0, le=511, default="", description="Match VRF ID.")    
    match_suppress: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable matching of suppressed original neighbor.")    
    set_aggregator_as: int | None = Field(ge=0, le=4294967295, default=0, description="BGP aggregator AS.")    
    set_aggregator_ip: str = Field(default="0.0.0.0", description="BGP aggregator IP.")    
    set_aspath_action: Literal["prepend", "replace"] | None = Field(default="prepend", description="Specify preferred action of set-aspath.")    
    set_aspath: list[SetAspath] = Field(default=None, description="Prepend BGP AS path attribute.")    
    set_atomic_aggregate: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable BGP atomic aggregate attribute.")    
    set_community_delete: str | None = Field(max_length=35, default="", description="Delete communities matching community list.")  # datasource: ['router.community-list.name']    
    set_community: list[SetCommunity] = Field(default=None, description="BGP community attribute.")    
    set_community_additive: Literal["enable", "disable"] | None = Field(default="disable", description="Enable/disable adding set-community to existing community.")    
    set_dampening_reachability_half_life: int | None = Field(ge=0, le=45, default=0, description="Reachability half-life time for the penalty (1 - 45 min, 0 = unset).")    
    set_dampening_reuse: int | None = Field(ge=0, le=20000, default=0, description="Value to start reusing a route (1 - 20000, 0 = unset).")    
    set_dampening_suppress: int | None = Field(ge=0, le=20000, default=0, description="Value to start suppressing a route (1 - 20000, 0 = unset).")    
    set_dampening_max_suppress: int | None = Field(ge=0, le=255, default=0, description="Maximum duration to suppress a route (1 - 255 min, 0 = unset).")    
    set_dampening_unreachability_half_life: int | None = Field(ge=0, le=45, default=0, description="Unreachability Half-life time for the penalty (1 - 45 min, 0 = unset).")    
    set_extcommunity_rt: list[SetExtcommunityRt] = Field(default=None, description="Route Target extended community.")    
    set_extcommunity_soo: list[SetExtcommunitySoo] = Field(default=None, description="Site-of-Origin extended community.")    
    set_ip_nexthop: str | None = Field(default="", description="IP address of next hop.")    
    set_ip_prefsrc: str | None = Field(default="", description="IP address of preferred source.")    
    set_vpnv4_nexthop: str | None = Field(default="", description="IP address of VPNv4 next-hop.")    
    set_ip6_nexthop: str | None = Field(default="", description="IPv6 global address of next hop.")    
    set_ip6_nexthop_local: str | None = Field(default="", description="IPv6 local address of next hop.")    
    set_vpnv6_nexthop: str | None = Field(default="", description="IPv6 global address of VPNv6 next-hop.")    
    set_vpnv6_nexthop_local: str | None = Field(default="", description="IPv6 link-local address of VPNv6 next-hop.")    
    set_local_preference: int | None = Field(ge=0, le=4294967295, default="", description="BGP local preference path attribute.")    
    set_metric: int | None = Field(ge=0, le=4294967295, default="", description="Metric value.")    
    set_metric_type: Literal["external-type1", "external-type2", "none"] | None = Field(default="", description="Metric type.")    
    set_originator_id: str | None = Field(default="", description="BGP originator ID attribute.")    
    set_origin: SetOriginEnum | None = Field(default="none", description="BGP origin code.")    
    set_tag: int | None = Field(ge=0, le=4294967295, default="", description="Tag value.")    
    set_weight: int | None = Field(ge=0, le=4294967295, default="", description="BGP weight for routing table.")    
    set_route_tag: int | None = Field(ge=0, le=4294967295, default="", description="Route tag for routing table.")    
    set_priority: int | None = Field(ge=1, le=65535, default="", description="Priority for routing table.")
# ============================================================================
# Enum Definitions (for fields with 4+ allowed values)
# ============================================================================


# ============================================================================
# Main Model
# ============================================================================

class RouteMapModel(BaseModel):
    """
    Pydantic model for router/route_map configuration.
    
    Configure route maps.
    
    Validation Rules:        - name: max_length=35 pattern=        - comments: max_length=127 pattern=        - rule: pattern=    """
    
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
    comments: str | None = Field(max_length=127, default="", description="Optional comments.")    
    rule: list[Rule] = Field(default=None, description="Rule.")    
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
    async def validate_rule_references(self, client: Any) -> list[str]:
        """
        Validate rule references exist in FortiGate.
        
        This method checks if referenced objects exist by calling exists() on
        the appropriate API endpoints. This is an OPTIONAL validation step that
        can be called before posting to the API to catch reference errors early.
        
        Datasource endpoints checked:
        - router/community-list        
        Args:
            client: FortiOS client instance (from fgt._client)
            
        Returns:
            List of validation error messages (empty if all valid)
            
        Example:
            >>> from hfortix_fortios import FortiOS
            >>> 
            >>> fgt = FortiOS(host="192.168.1.1", token="your-token")
            >>> policy = RouteMapModel(
            ...     rule=[{"set-community-delete": "invalid-name"}],
            ... )
            >>> 
            >>> # Validate before posting
            >>> errors = await policy.validate_rule_references(fgt._client)
            >>> if errors:
            ...     print("Validation failed:", errors)
            ... else:
            ...     result = await fgt.api.cmdb.router.route_map.post(policy.to_fortios_dict())
        """
        errors = []
        
        # Validate child table items
        values = getattr(self, "rule", [])
        if not values:
            return errors
        
        for item in values:
            if isinstance(item, dict):
                value = item.get("set-community-delete")
            else:
                value = getattr(item, "set-community-delete", None)
            
            if not value:
                continue
            
            # Check all datasource endpoints
            found = False
            if await client.api.cmdb.router.community-list.exists(value):
                found = True
            
            if not found:
                errors.append(
                    f"Rule '{value}' not found in "
                    "router/community-list"
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
        
        errors = await self.validate_rule_references(client)
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
    "RouteMapModel",    "RouteMapRule",]


# ============================================================================
# Generated by hfortix generator v0.6.0
# Schema: 1.7.0
# Generated: 2026-01-15T21:00:58.080234Z
# ============================================================================
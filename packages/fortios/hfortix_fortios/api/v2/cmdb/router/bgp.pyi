from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class BgpPayload(TypedDict, total=False):
    """
    Type hints for router/bgp payload fields.
    
    Configure BGP.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.router.route-map.RouteMapEndpoint` (via: dampening-route-map)

    **Usage:**
        payload: BgpPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    asn: str  # Router AS number, asplain/asdot/asdot+ format, 0 t
    router_id: str  # Router ID.
    keepalive_timer: int  # Frequency to send keep alive requests. | Default: 60 | Min: 0 | Max: 65535
    holdtime_timer: int  # Number of seconds to mark peer as dead. | Default: 180 | Min: 3 | Max: 65535
    always_compare_med: Literal["enable", "disable"]  # Enable/disable always compare MED. | Default: disable
    bestpath_as_path_ignore: Literal["enable", "disable"]  # Enable/disable ignore AS path. | Default: disable
    bestpath_cmp_confed_aspath: Literal["enable", "disable"]  # Enable/disable compare federation AS path length. | Default: disable
    bestpath_cmp_routerid: Literal["enable", "disable"]  # Enable/disable compare router ID for identical EBG | Default: disable
    bestpath_med_confed: Literal["enable", "disable"]  # Enable/disable compare MED among confederation pat | Default: disable
    bestpath_med_missing_as_worst: Literal["enable", "disable"]  # Enable/disable treat missing MED as least preferre | Default: disable
    client_to_client_reflection: Literal["enable", "disable"]  # Enable/disable client-to-client route reflection. | Default: enable
    dampening: Literal["enable", "disable"]  # Enable/disable route-flap dampening. | Default: disable
    deterministic_med: Literal["enable", "disable"]  # Enable/disable enforce deterministic comparison of | Default: disable
    ebgp_multipath: Literal["enable", "disable"]  # Enable/disable EBGP multi-path. | Default: disable
    ibgp_multipath: Literal["enable", "disable"]  # Enable/disable IBGP multi-path. | Default: disable
    enforce_first_as: Literal["enable", "disable"]  # Enable/disable enforce first AS for EBGP routes. | Default: enable
    fast_external_failover: Literal["enable", "disable"]  # Enable/disable reset peer BGP session if link goes | Default: enable
    log_neighbour_changes: Literal["enable", "disable"]  # Log BGP neighbor changes. | Default: enable
    network_import_check: Literal["enable", "disable"]  # Enable/disable ensure BGP network route exists in | Default: enable
    ignore_optional_capability: Literal["enable", "disable"]  # Do not send unknown optional capability notificati | Default: enable
    additional_path: Literal["enable", "disable"]  # Enable/disable selection of BGP IPv4 additional pa | Default: disable
    additional_path6: Literal["enable", "disable"]  # Enable/disable selection of BGP IPv6 additional pa | Default: disable
    additional_path_vpnv4: Literal["enable", "disable"]  # Enable/disable selection of BGP VPNv4 additional p | Default: disable
    additional_path_vpnv6: Literal["enable", "disable"]  # Enable/disable selection of BGP VPNv6 additional p | Default: disable
    multipath_recursive_distance: Literal["enable", "disable"]  # Enable/disable use of recursive distance to select | Default: disable
    recursive_next_hop: Literal["enable", "disable"]  # Enable/disable recursive resolution of next-hop us | Default: disable
    recursive_inherit_priority: Literal["enable", "disable"]  # Enable/disable priority inheritance for recursive | Default: disable
    tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"]  # Configure tag-match mode. Resolves BGP routes with | Default: disable
    cluster_id: str  # Route reflector cluster ID. | Default: 0.0.0.0
    confederation_identifier: int  # Confederation identifier. | Default: 0 | Min: 1 | Max: 4294967295
    confederation_peers: list[dict[str, Any]]  # Confederation peers.
    dampening_route_map: str  # Criteria for dampening. | MaxLen: 35
    dampening_reachability_half_life: int  # Reachability half-life time for penalty (min). | Default: 15 | Min: 1 | Max: 45
    dampening_reuse: int  # Threshold to reuse routes. | Default: 750 | Min: 1 | Max: 20000
    dampening_suppress: int  # Threshold to suppress routes. | Default: 2000 | Min: 1 | Max: 20000
    dampening_max_suppress_time: int  # Maximum minutes a route can be suppressed. | Default: 60 | Min: 1 | Max: 255
    dampening_unreachability_half_life: int  # Unreachability half-life time for penalty (min). | Default: 15 | Min: 1 | Max: 45
    default_local_preference: int  # Default local preference. | Default: 100 | Min: 0 | Max: 4294967295
    scan_time: int  # Background scanner interval (sec), 0 to disable it | Default: 60 | Min: 5 | Max: 60
    distance_external: int  # Distance for routes external to the AS. | Default: 20 | Min: 1 | Max: 255
    distance_internal: int  # Distance for routes internal to the AS. | Default: 200 | Min: 1 | Max: 255
    distance_local: int  # Distance for routes local to the AS. | Default: 200 | Min: 1 | Max: 255
    synchronization: Literal["enable", "disable"]  # Enable/disable only advertise routes from iBGP if | Default: disable
    graceful_restart: Literal["enable", "disable"]  # Enable/disable BGP graceful restart capabilities. | Default: disable
    graceful_restart_time: int  # Time needed for neighbors to restart (sec). | Default: 120 | Min: 1 | Max: 3600
    graceful_stalepath_time: int  # Time to hold stale paths of restarting neighbor | Default: 360 | Min: 1 | Max: 3600
    graceful_update_delay: int  # Route advertisement/selection delay after restart | Default: 120 | Min: 1 | Max: 3600
    graceful_end_on_timer: Literal["enable", "disable"]  # Enable/disable to exit graceful restart on timer o | Default: disable
    additional_path_select: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    additional_path_select6: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    additional_path_select_vpnv4: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    additional_path_select_vpnv6: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    cross_family_conditional_adv: Literal["enable", "disable"]  # Enable/disable cross address family conditional ad | Default: disable
    aggregate_address: list[dict[str, Any]]  # BGP aggregate address table.
    aggregate_address6: list[dict[str, Any]]  # BGP IPv6 aggregate address table.
    neighbor: list[dict[str, Any]]  # BGP neighbor table.
    neighbor_group: list[dict[str, Any]]  # BGP neighbor group table.
    neighbor_range: list[dict[str, Any]]  # BGP neighbor range table.
    neighbor_range6: list[dict[str, Any]]  # BGP IPv6 neighbor range table.
    network: list[dict[str, Any]]  # BGP network table.
    network6: list[dict[str, Any]]  # BGP IPv6 network table.
    redistribute: list[dict[str, Any]]  # BGP IPv4 redistribute table.
    redistribute6: list[dict[str, Any]]  # BGP IPv6 redistribute table.
    admin_distance: list[dict[str, Any]]  # Administrative distance modifications.
    vrf: list[dict[str, Any]]  # BGP VRF leaking table.
    vrf6: list[dict[str, Any]]  # BGP IPv6 VRF leaking table.

# Nested TypedDicts for table field children (dict mode)

class BgpConfederationpeersItem(TypedDict):
    """Type hints for confederation-peers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    peer: str  # Peer ID. | MaxLen: 79


class BgpAggregateaddressItem(TypedDict):
    """Type hints for aggregate-address table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Aggregate prefix. | Default: 0.0.0.0 0.0.0.0
    as_set: Literal["enable", "disable"]  # Enable/disable generate AS set path information. | Default: disable
    summary_only: Literal["enable", "disable"]  # Enable/disable filter more specific routes from up | Default: disable


class BgpAggregateaddress6Item(TypedDict):
    """Type hints for aggregate-address6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix6: str  # Aggregate IPv6 prefix. | Default: ::/0
    as_set: Literal["enable", "disable"]  # Enable/disable generate AS set path information. | Default: disable
    summary_only: Literal["enable", "disable"]  # Enable/disable filter more specific routes from up | Default: disable


class BgpNeighborItem(TypedDict):
    """Type hints for neighbor table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    ip: str  # IP/IPv6 address of neighbor. | MaxLen: 45
    advertisement_interval: int  # Minimum interval (sec) between sending updates. | Default: 30 | Min: 0 | Max: 600
    allowas_in_enable: Literal["enable", "disable"]  # Enable/disable IPv4 Enable to allow my AS in AS pa | Default: disable
    allowas_in_enable6: Literal["enable", "disable"]  # Enable/disable IPv6 Enable to allow my AS in AS pa | Default: disable
    allowas_in_enable_vpnv4: Literal["enable", "disable"]  # Enable/disable to allow my AS in AS path for VPNv4 | Default: disable
    allowas_in_enable_vpnv6: Literal["enable", "disable"]  # Enable/disable use of my AS in AS path for VPNv6 r | Default: disable
    allowas_in_enable_evpn: Literal["enable", "disable"]  # Enable/disable to allow my AS in AS path for L2VPN | Default: disable
    allowas_in: int  # IPv4 The maximum number of occurrence of my AS num | Default: 3 | Min: 1 | Max: 10
    allowas_in6: int  # IPv6 The maximum number of occurrence of my AS num | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv4: int  # The maximum number of occurrence of my AS number a | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv6: int  # The maximum number of occurrence of my AS number a | Default: 3 | Min: 1 | Max: 10
    allowas_in_evpn: int  # The maximum number of occurrence of my AS number a | Default: 3 | Min: 1 | Max: 10
    attribute_unchanged: Literal["as-path", "med", "next-hop"]  # IPv4 List of attributes that should be unchanged.
    attribute_unchanged6: Literal["as-path", "med", "next-hop"]  # IPv6 List of attributes that should be unchanged.
    attribute_unchanged_vpnv4: Literal["as-path", "med", "next-hop"]  # List of attributes that should be unchanged for VP
    attribute_unchanged_vpnv6: Literal["as-path", "med", "next-hop"]  # List of attributes that should not be changed for
    activate: Literal["enable", "disable"]  # Enable/disable address family IPv4 for this neighb | Default: enable
    activate6: Literal["enable", "disable"]  # Enable/disable address family IPv6 for this neighb | Default: enable
    activate_vpnv4: Literal["enable", "disable"]  # Enable/disable address family VPNv4 for this neigh | Default: enable
    activate_vpnv6: Literal["enable", "disable"]  # Enable/disable address family VPNv6 for this neigh | Default: enable
    activate_evpn: Literal["enable", "disable"]  # Enable/disable address family L2VPN EVPN for this | Default: enable
    bfd: Literal["enable", "disable"]  # Enable/disable BFD for this neighbor. | Default: disable
    capability_dynamic: Literal["enable", "disable"]  # Enable/disable advertise dynamic capability to thi | Default: disable
    capability_orf: Literal["none", "receive", "send", "both"]  # Accept/Send IPv4 ORF lists to/from this neighbor. | Default: none
    capability_orf6: Literal["none", "receive", "send", "both"]  # Accept/Send IPv6 ORF lists to/from this neighbor. | Default: none
    capability_graceful_restart: Literal["enable", "disable"]  # Enable/disable advertise IPv4 graceful restart cap | Default: disable
    capability_graceful_restart6: Literal["enable", "disable"]  # Enable/disable advertise IPv6 graceful restart cap | Default: disable
    capability_graceful_restart_vpnv4: Literal["enable", "disable"]  # Enable/disable advertise VPNv4 graceful restart ca | Default: disable
    capability_graceful_restart_vpnv6: Literal["enable", "disable"]  # Enable/disable advertisement of VPNv6 graceful res | Default: disable
    capability_graceful_restart_evpn: Literal["enable", "disable"]  # Enable/disable advertisement of L2VPN EVPN gracefu | Default: disable
    capability_route_refresh: Literal["enable", "disable"]  # Enable/disable advertise route refresh capability | Default: enable
    capability_default_originate: Literal["enable", "disable"]  # Enable/disable advertise default IPv4 route to thi | Default: disable
    capability_default_originate6: Literal["enable", "disable"]  # Enable/disable advertise default IPv6 route to thi | Default: disable
    dont_capability_negotiate: Literal["enable", "disable"]  # Do not negotiate capabilities with this neighbor. | Default: disable
    ebgp_enforce_multihop: Literal["enable", "disable"]  # Enable/disable allow multi-hop EBGP neighbors. | Default: disable
    link_down_failover: Literal["enable", "disable"]  # Enable/disable failover upon link down. | Default: disable
    stale_route: Literal["enable", "disable"]  # Enable/disable stale route after neighbor down. | Default: disable
    next_hop_self: Literal["enable", "disable"]  # Enable/disable IPv4 next-hop calculation for this | Default: disable
    next_hop_self6: Literal["enable", "disable"]  # Enable/disable IPv6 next-hop calculation for this | Default: disable
    next_hop_self_rr: Literal["enable", "disable"]  # Enable/disable setting nexthop's address to interf | Default: disable
    next_hop_self_rr6: Literal["enable", "disable"]  # Enable/disable setting nexthop's address to interf | Default: disable
    next_hop_self_vpnv4: Literal["enable", "disable"]  # Enable/disable setting VPNv4 next-hop to interface | Default: disable
    next_hop_self_vpnv6: Literal["enable", "disable"]  # Enable/disable use of outgoing interface's IP addr | Default: disable
    override_capability: Literal["enable", "disable"]  # Enable/disable override result of capability negot | Default: disable
    passive: Literal["enable", "disable"]  # Enable/disable sending of open messages to this ne | Default: disable
    remove_private_as: Literal["enable", "disable"]  # Enable/disable remove private AS number from IPv4 | Default: disable
    remove_private_as6: Literal["enable", "disable"]  # Enable/disable remove private AS number from IPv6 | Default: disable
    remove_private_as_vpnv4: Literal["enable", "disable"]  # Enable/disable remove private AS number from VPNv4 | Default: disable
    remove_private_as_vpnv6: Literal["enable", "disable"]  # Enable/disable to remove private AS number from VP | Default: disable
    remove_private_as_evpn: Literal["enable", "disable"]  # Enable/disable removing private AS number from L2V | Default: disable
    route_reflector_client: Literal["enable", "disable"]  # Enable/disable IPv4 AS route reflector client. | Default: disable
    route_reflector_client6: Literal["enable", "disable"]  # Enable/disable IPv6 AS route reflector client. | Default: disable
    route_reflector_client_vpnv4: Literal["enable", "disable"]  # Enable/disable VPNv4 AS route reflector client for | Default: disable
    route_reflector_client_vpnv6: Literal["enable", "disable"]  # Enable/disable VPNv6 AS route reflector client for | Default: disable
    route_reflector_client_evpn: Literal["enable", "disable"]  # Enable/disable L2VPN EVPN AS route reflector clien | Default: disable
    route_server_client: Literal["enable", "disable"]  # Enable/disable IPv4 AS route server client. | Default: disable
    route_server_client6: Literal["enable", "disable"]  # Enable/disable IPv6 AS route server client. | Default: disable
    route_server_client_vpnv4: Literal["enable", "disable"]  # Enable/disable VPNv4 AS route server client for th | Default: disable
    route_server_client_vpnv6: Literal["enable", "disable"]  # Enable/disable VPNv6 AS route server client for th | Default: disable
    route_server_client_evpn: Literal["enable", "disable"]  # Enable/disable L2VPN EVPN AS route server client f | Default: disable
    rr_attr_allow_change: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change6: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change_vpnv4: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change_vpnv6: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change_evpn: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    shutdown: Literal["enable", "disable"]  # Enable/disable shutdown this neighbor. | Default: disable
    soft_reconfiguration: Literal["enable", "disable"]  # Enable/disable allow IPv4 inbound soft reconfigura | Default: disable
    soft_reconfiguration6: Literal["enable", "disable"]  # Enable/disable allow IPv6 inbound soft reconfigura | Default: disable
    soft_reconfiguration_vpnv4: Literal["enable", "disable"]  # Enable/disable allow VPNv4 inbound soft reconfigur | Default: disable
    soft_reconfiguration_vpnv6: Literal["enable", "disable"]  # Enable/disable VPNv6 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_evpn: Literal["enable", "disable"]  # Enable/disable L2VPN EVPN inbound soft reconfigura | Default: disable
    as_override: Literal["enable", "disable"]  # Enable/disable replace peer AS with own AS for IPv | Default: disable
    as_override6: Literal["enable", "disable"]  # Enable/disable replace peer AS with own AS for IPv | Default: disable
    strict_capability_match: Literal["enable", "disable"]  # Enable/disable strict capability matching. | Default: disable
    default_originate_routemap: str  # Route map to specify criteria to originate IPv4 de | MaxLen: 35
    default_originate_routemap6: str  # Route map to specify criteria to originate IPv6 de | MaxLen: 35
    description: str  # Description. | MaxLen: 63
    distribute_list_in: str  # Filter for IPv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in6: str  # Filter for IPv6 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv4: str  # Filter for VPNv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv6: str  # Filter for VPNv6 updates from this neighbor. | MaxLen: 35
    distribute_list_out: str  # Filter for IPv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out6: str  # Filter for IPv6 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv4: str  # Filter for VPNv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv6: str  # Filter for VPNv6 updates to this neighbor. | MaxLen: 35
    ebgp_multihop_ttl: int  # EBGP multihop TTL for this peer. | Default: 255 | Min: 1 | Max: 255
    filter_list_in: str  # BGP filter for IPv4 inbound routes. | MaxLen: 35
    filter_list_in6: str  # BGP filter for IPv6 inbound routes. | MaxLen: 35
    filter_list_in_vpnv4: str  # BGP filter for VPNv4 inbound routes. | MaxLen: 35
    filter_list_in_vpnv6: str  # BGP filter for VPNv6 inbound routes. | MaxLen: 35
    filter_list_out: str  # BGP filter for IPv4 outbound routes. | MaxLen: 35
    filter_list_out6: str  # BGP filter for IPv6 outbound routes. | MaxLen: 35
    filter_list_out_vpnv4: str  # BGP filter for VPNv4 outbound routes. | MaxLen: 35
    filter_list_out_vpnv6: str  # BGP filter for VPNv6 outbound routes. | MaxLen: 35
    interface: str  # Specify outgoing interface for peer connection. Fo | MaxLen: 15
    maximum_prefix: int  # Maximum number of IPv4 prefixes to accept from thi | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix6: int  # Maximum number of IPv6 prefixes to accept from thi | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv4: int  # Maximum number of VPNv4 prefixes to accept from th | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv6: int  # Maximum number of VPNv6 prefixes to accept from th | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_evpn: int  # Maximum number of L2VPN EVPN prefixes to accept fr | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_threshold: int  # Maximum IPv4 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold6: int  # Maximum IPv6 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv4: int  # Maximum VPNv4 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv6: int  # Maximum VPNv6 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_evpn: int  # Maximum L2VPN EVPN prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_warning_only: Literal["enable", "disable"]  # Enable/disable IPv4 Only give warning message when | Default: disable
    maximum_prefix_warning_only6: Literal["enable", "disable"]  # Enable/disable IPv6 Only give warning message when | Default: disable
    maximum_prefix_warning_only_vpnv4: Literal["enable", "disable"]  # Enable/disable only giving warning message when li | Default: disable
    maximum_prefix_warning_only_vpnv6: Literal["enable", "disable"]  # Enable/disable warning message when limit is excee | Default: disable
    maximum_prefix_warning_only_evpn: Literal["enable", "disable"]  # Enable/disable only sending warning message when e | Default: disable
    prefix_list_in: str  # IPv4 Inbound filter for updates from this neighbor | MaxLen: 35
    prefix_list_in6: str  # IPv6 Inbound filter for updates from this neighbor | MaxLen: 35
    prefix_list_in_vpnv4: str  # Inbound filter for VPNv4 updates from this neighbo | MaxLen: 35
    prefix_list_in_vpnv6: str  # Inbound filter for VPNv6 updates from this neighbo | MaxLen: 35
    prefix_list_out: str  # IPv4 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out6: str  # IPv6 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out_vpnv4: str  # Outbound filter for VPNv4 updates to this neighbor | MaxLen: 35
    prefix_list_out_vpnv6: str  # Outbound filter for VPNv6 updates to this neighbor | MaxLen: 35
    remote_as: str  # AS number of neighbor.
    local_as: str  # Local AS number of neighbor.
    local_as_no_prepend: Literal["enable", "disable"]  # Do not prepend local-as to incoming updates. | Default: disable
    local_as_replace_as: Literal["enable", "disable"]  # Replace real AS with local-as in outgoing updates. | Default: disable
    retain_stale_time: int  # Time to retain stale routes. | Default: 0 | Min: 0 | Max: 65535
    route_map_in: str  # IPv4 Inbound route map filter. | MaxLen: 35
    route_map_in6: str  # IPv6 Inbound route map filter. | MaxLen: 35
    route_map_in_vpnv4: str  # VPNv4 inbound route map filter. | MaxLen: 35
    route_map_in_vpnv6: str  # VPNv6 inbound route map filter. | MaxLen: 35
    route_map_in_evpn: str  # L2VPN EVPN inbound route map filter. | MaxLen: 35
    route_map_out: str  # IPv4 outbound route map filter. | MaxLen: 35
    route_map_out_preferable: str  # IPv4 outbound route map filter if the peer is pref | MaxLen: 35
    route_map_out6: str  # IPv6 Outbound route map filter. | MaxLen: 35
    route_map_out6_preferable: str  # IPv6 outbound route map filter if the peer is pref | MaxLen: 35
    route_map_out_vpnv4: str  # VPNv4 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv6: str  # VPNv6 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv4_preferable: str  # VPNv4 outbound route map filter if the peer is pre | MaxLen: 35
    route_map_out_vpnv6_preferable: str  # VPNv6 outbound route map filter if this neighbor i | MaxLen: 35
    route_map_out_evpn: str  # L2VPN EVPN outbound route map filter. | MaxLen: 35
    send_community: Literal["standard", "extended", "both", "disable"]  # IPv4 Send community attribute to neighbor. | Default: both
    send_community6: Literal["standard", "extended", "both", "disable"]  # IPv6 Send community attribute to neighbor. | Default: both
    send_community_vpnv4: Literal["standard", "extended", "both", "disable"]  # Send community attribute to neighbor for VPNv4 add | Default: both
    send_community_vpnv6: Literal["standard", "extended", "both", "disable"]  # Enable/disable sending community attribute to this | Default: both
    send_community_evpn: Literal["standard", "extended", "both", "disable"]  # Enable/disable sending community attribute to neig | Default: both
    keep_alive_timer: int  # Keep alive timer interval (sec). | Default: 4294967295 | Min: 0 | Max: 65535
    holdtime_timer: int  # Interval (sec) before peer considered dead. | Default: 4294967295 | Min: 3 | Max: 65535
    connect_timer: int  # Interval (sec) for connect timer. | Default: 4294967295 | Min: 1 | Max: 65535
    unsuppress_map: str  # IPv4 Route map to selectively unsuppress suppresse | MaxLen: 35
    unsuppress_map6: str  # IPv6 Route map to selectively unsuppress suppresse | MaxLen: 35
    update_source: str  # Interface to use as source IP/IPv6 address of TCP | MaxLen: 15
    weight: int  # Neighbor weight. | Default: 4294967295 | Min: 0 | Max: 65535
    restart_time: int  # Graceful restart delay time | Default: 0 | Min: 0 | Max: 3600
    additional_path: Literal["send", "receive", "both", "disable"]  # Enable/disable IPv4 additional-path capability. | Default: disable
    additional_path6: Literal["send", "receive", "both", "disable"]  # Enable/disable IPv6 additional-path capability. | Default: disable
    additional_path_vpnv4: Literal["send", "receive", "both", "disable"]  # Enable/disable VPNv4 additional-path capability. | Default: disable
    additional_path_vpnv6: Literal["send", "receive", "both", "disable"]  # Enable/disable VPNv6 additional-path capability. | Default: disable
    adv_additional_path: int  # Number of IPv4 additional paths that can be advert | Default: 2 | Min: 2 | Max: 255
    adv_additional_path6: int  # Number of IPv6 additional paths that can be advert | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv4: int  # Number of VPNv4 additional paths that can be adver | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv6: int  # Number of VPNv6 additional paths that can be adver | Default: 2 | Min: 2 | Max: 255
    password: str  # Password used in MD5 authentication. | MaxLen: 128
    auth_options: str  # Key-chain name for TCP authentication options. | MaxLen: 35
    conditional_advertise: str  # Conditional advertisement.
    conditional_advertise6: str  # IPv6 conditional advertisement.


class BgpNeighborgroupItem(TypedDict):
    """Type hints for neighbor-group table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Neighbor group name. | MaxLen: 45
    advertisement_interval: int  # Minimum interval (sec) between sending updates. | Default: 30 | Min: 0 | Max: 600
    allowas_in_enable: Literal["enable", "disable"]  # Enable/disable IPv4 Enable to allow my AS in AS pa | Default: disable
    allowas_in_enable6: Literal["enable", "disable"]  # Enable/disable IPv6 Enable to allow my AS in AS pa | Default: disable
    allowas_in_enable_vpnv4: Literal["enable", "disable"]  # Enable/disable to allow my AS in AS path for VPNv4 | Default: disable
    allowas_in_enable_vpnv6: Literal["enable", "disable"]  # Enable/disable use of my AS in AS path for VPNv6 r | Default: disable
    allowas_in_enable_evpn: Literal["enable", "disable"]  # Enable/disable to allow my AS in AS path for L2VPN | Default: disable
    allowas_in: int  # IPv4 The maximum number of occurrence of my AS num | Default: 3 | Min: 1 | Max: 10
    allowas_in6: int  # IPv6 The maximum number of occurrence of my AS num | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv4: int  # The maximum number of occurrence of my AS number a | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv6: int  # The maximum number of occurrence of my AS number a | Default: 3 | Min: 1 | Max: 10
    allowas_in_evpn: int  # The maximum number of occurrence of my AS number a | Default: 3 | Min: 1 | Max: 10
    attribute_unchanged: Literal["as-path", "med", "next-hop"]  # IPv4 List of attributes that should be unchanged.
    attribute_unchanged6: Literal["as-path", "med", "next-hop"]  # IPv6 List of attributes that should be unchanged.
    attribute_unchanged_vpnv4: Literal["as-path", "med", "next-hop"]  # List of attributes that should be unchanged for VP
    attribute_unchanged_vpnv6: Literal["as-path", "med", "next-hop"]  # List of attributes that should not be changed for
    activate: Literal["enable", "disable"]  # Enable/disable address family IPv4 for this neighb | Default: enable
    activate6: Literal["enable", "disable"]  # Enable/disable address family IPv6 for this neighb | Default: enable
    activate_vpnv4: Literal["enable", "disable"]  # Enable/disable address family VPNv4 for this neigh | Default: enable
    activate_vpnv6: Literal["enable", "disable"]  # Enable/disable address family VPNv6 for this neigh | Default: enable
    activate_evpn: Literal["enable", "disable"]  # Enable/disable address family L2VPN EVPN for this | Default: enable
    bfd: Literal["enable", "disable"]  # Enable/disable BFD for this neighbor. | Default: disable
    capability_dynamic: Literal["enable", "disable"]  # Enable/disable advertise dynamic capability to thi | Default: disable
    capability_orf: Literal["none", "receive", "send", "both"]  # Accept/Send IPv4 ORF lists to/from this neighbor. | Default: none
    capability_orf6: Literal["none", "receive", "send", "both"]  # Accept/Send IPv6 ORF lists to/from this neighbor. | Default: none
    capability_graceful_restart: Literal["enable", "disable"]  # Enable/disable advertise IPv4 graceful restart cap | Default: disable
    capability_graceful_restart6: Literal["enable", "disable"]  # Enable/disable advertise IPv6 graceful restart cap | Default: disable
    capability_graceful_restart_vpnv4: Literal["enable", "disable"]  # Enable/disable advertise VPNv4 graceful restart ca | Default: disable
    capability_graceful_restart_vpnv6: Literal["enable", "disable"]  # Enable/disable advertisement of VPNv6 graceful res | Default: disable
    capability_graceful_restart_evpn: Literal["enable", "disable"]  # Enable/disable advertisement of L2VPN EVPN gracefu | Default: disable
    capability_route_refresh: Literal["enable", "disable"]  # Enable/disable advertise route refresh capability | Default: enable
    capability_default_originate: Literal["enable", "disable"]  # Enable/disable advertise default IPv4 route to thi | Default: disable
    capability_default_originate6: Literal["enable", "disable"]  # Enable/disable advertise default IPv6 route to thi | Default: disable
    dont_capability_negotiate: Literal["enable", "disable"]  # Do not negotiate capabilities with this neighbor. | Default: disable
    ebgp_enforce_multihop: Literal["enable", "disable"]  # Enable/disable allow multi-hop EBGP neighbors. | Default: disable
    link_down_failover: Literal["enable", "disable"]  # Enable/disable failover upon link down. | Default: disable
    stale_route: Literal["enable", "disable"]  # Enable/disable stale route after neighbor down. | Default: disable
    next_hop_self: Literal["enable", "disable"]  # Enable/disable IPv4 next-hop calculation for this | Default: disable
    next_hop_self6: Literal["enable", "disable"]  # Enable/disable IPv6 next-hop calculation for this | Default: disable
    next_hop_self_rr: Literal["enable", "disable"]  # Enable/disable setting nexthop's address to interf | Default: disable
    next_hop_self_rr6: Literal["enable", "disable"]  # Enable/disable setting nexthop's address to interf | Default: disable
    next_hop_self_vpnv4: Literal["enable", "disable"]  # Enable/disable setting VPNv4 next-hop to interface | Default: disable
    next_hop_self_vpnv6: Literal["enable", "disable"]  # Enable/disable use of outgoing interface's IP addr | Default: disable
    override_capability: Literal["enable", "disable"]  # Enable/disable override result of capability negot | Default: disable
    passive: Literal["enable", "disable"]  # Enable/disable sending of open messages to this ne | Default: enable
    remove_private_as: Literal["enable", "disable"]  # Enable/disable remove private AS number from IPv4 | Default: disable
    remove_private_as6: Literal["enable", "disable"]  # Enable/disable remove private AS number from IPv6 | Default: disable
    remove_private_as_vpnv4: Literal["enable", "disable"]  # Enable/disable remove private AS number from VPNv4 | Default: disable
    remove_private_as_vpnv6: Literal["enable", "disable"]  # Enable/disable to remove private AS number from VP | Default: disable
    remove_private_as_evpn: Literal["enable", "disable"]  # Enable/disable removing private AS number from L2V | Default: disable
    route_reflector_client: Literal["enable", "disable"]  # Enable/disable IPv4 AS route reflector client. | Default: disable
    route_reflector_client6: Literal["enable", "disable"]  # Enable/disable IPv6 AS route reflector client. | Default: disable
    route_reflector_client_vpnv4: Literal["enable", "disable"]  # Enable/disable VPNv4 AS route reflector client for | Default: disable
    route_reflector_client_vpnv6: Literal["enable", "disable"]  # Enable/disable VPNv6 AS route reflector client for | Default: disable
    route_reflector_client_evpn: Literal["enable", "disable"]  # Enable/disable L2VPN EVPN AS route reflector clien | Default: disable
    route_server_client: Literal["enable", "disable"]  # Enable/disable IPv4 AS route server client. | Default: disable
    route_server_client6: Literal["enable", "disable"]  # Enable/disable IPv6 AS route server client. | Default: disable
    route_server_client_vpnv4: Literal["enable", "disable"]  # Enable/disable VPNv4 AS route server client for th | Default: disable
    route_server_client_vpnv6: Literal["enable", "disable"]  # Enable/disable VPNv6 AS route server client for th | Default: disable
    route_server_client_evpn: Literal["enable", "disable"]  # Enable/disable L2VPN EVPN AS route server client f | Default: disable
    rr_attr_allow_change: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change6: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change_vpnv4: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change_vpnv6: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    rr_attr_allow_change_evpn: Literal["enable", "disable"]  # Enable/disable allowing change of route attributes | Default: disable
    shutdown: Literal["enable", "disable"]  # Enable/disable shutdown this neighbor. | Default: disable
    soft_reconfiguration: Literal["enable", "disable"]  # Enable/disable allow IPv4 inbound soft reconfigura | Default: disable
    soft_reconfiguration6: Literal["enable", "disable"]  # Enable/disable allow IPv6 inbound soft reconfigura | Default: disable
    soft_reconfiguration_vpnv4: Literal["enable", "disable"]  # Enable/disable allow VPNv4 inbound soft reconfigur | Default: disable
    soft_reconfiguration_vpnv6: Literal["enable", "disable"]  # Enable/disable VPNv6 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_evpn: Literal["enable", "disable"]  # Enable/disable L2VPN EVPN inbound soft reconfigura | Default: disable
    as_override: Literal["enable", "disable"]  # Enable/disable replace peer AS with own AS for IPv | Default: disable
    as_override6: Literal["enable", "disable"]  # Enable/disable replace peer AS with own AS for IPv | Default: disable
    strict_capability_match: Literal["enable", "disable"]  # Enable/disable strict capability matching. | Default: disable
    default_originate_routemap: str  # Route map to specify criteria to originate IPv4 de | MaxLen: 35
    default_originate_routemap6: str  # Route map to specify criteria to originate IPv6 de | MaxLen: 35
    description: str  # Description. | MaxLen: 63
    distribute_list_in: str  # Filter for IPv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in6: str  # Filter for IPv6 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv4: str  # Filter for VPNv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv6: str  # Filter for VPNv6 updates from this neighbor. | MaxLen: 35
    distribute_list_out: str  # Filter for IPv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out6: str  # Filter for IPv6 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv4: str  # Filter for VPNv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv6: str  # Filter for VPNv6 updates to this neighbor. | MaxLen: 35
    ebgp_multihop_ttl: int  # EBGP multihop TTL for this peer. | Default: 255 | Min: 1 | Max: 255
    filter_list_in: str  # BGP filter for IPv4 inbound routes. | MaxLen: 35
    filter_list_in6: str  # BGP filter for IPv6 inbound routes. | MaxLen: 35
    filter_list_in_vpnv4: str  # BGP filter for VPNv4 inbound routes. | MaxLen: 35
    filter_list_in_vpnv6: str  # BGP filter for VPNv6 inbound routes. | MaxLen: 35
    filter_list_out: str  # BGP filter for IPv4 outbound routes. | MaxLen: 35
    filter_list_out6: str  # BGP filter for IPv6 outbound routes. | MaxLen: 35
    filter_list_out_vpnv4: str  # BGP filter for VPNv4 outbound routes. | MaxLen: 35
    filter_list_out_vpnv6: str  # BGP filter for VPNv6 outbound routes. | MaxLen: 35
    interface: str  # Specify outgoing interface for peer connection. Fo | MaxLen: 15
    maximum_prefix: int  # Maximum number of IPv4 prefixes to accept from thi | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix6: int  # Maximum number of IPv6 prefixes to accept from thi | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv4: int  # Maximum number of VPNv4 prefixes to accept from th | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv6: int  # Maximum number of VPNv6 prefixes to accept from th | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_evpn: int  # Maximum number of L2VPN EVPN prefixes to accept fr | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_threshold: int  # Maximum IPv4 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold6: int  # Maximum IPv6 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv4: int  # Maximum VPNv4 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv6: int  # Maximum VPNv6 prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_evpn: int  # Maximum L2VPN EVPN prefix threshold value | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_warning_only: Literal["enable", "disable"]  # Enable/disable IPv4 Only give warning message when | Default: disable
    maximum_prefix_warning_only6: Literal["enable", "disable"]  # Enable/disable IPv6 Only give warning message when | Default: disable
    maximum_prefix_warning_only_vpnv4: Literal["enable", "disable"]  # Enable/disable only giving warning message when li | Default: disable
    maximum_prefix_warning_only_vpnv6: Literal["enable", "disable"]  # Enable/disable warning message when limit is excee | Default: disable
    maximum_prefix_warning_only_evpn: Literal["enable", "disable"]  # Enable/disable only sending warning message when e | Default: disable
    prefix_list_in: str  # IPv4 Inbound filter for updates from this neighbor | MaxLen: 35
    prefix_list_in6: str  # IPv6 Inbound filter for updates from this neighbor | MaxLen: 35
    prefix_list_in_vpnv4: str  # Inbound filter for VPNv4 updates from this neighbo | MaxLen: 35
    prefix_list_in_vpnv6: str  # Inbound filter for VPNv6 updates from this neighbo | MaxLen: 35
    prefix_list_out: str  # IPv4 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out6: str  # IPv6 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out_vpnv4: str  # Outbound filter for VPNv4 updates to this neighbor | MaxLen: 35
    prefix_list_out_vpnv6: str  # Outbound filter for VPNv6 updates to this neighbor | MaxLen: 35
    remote_as: str  # AS number of neighbor.
    remote_as_filter: str  # BGP filter for remote AS. | MaxLen: 35
    local_as: str  # Local AS number of neighbor.
    local_as_no_prepend: Literal["enable", "disable"]  # Do not prepend local-as to incoming updates. | Default: disable
    local_as_replace_as: Literal["enable", "disable"]  # Replace real AS with local-as in outgoing updates. | Default: disable
    retain_stale_time: int  # Time to retain stale routes. | Default: 0 | Min: 0 | Max: 65535
    route_map_in: str  # IPv4 Inbound route map filter. | MaxLen: 35
    route_map_in6: str  # IPv6 Inbound route map filter. | MaxLen: 35
    route_map_in_vpnv4: str  # VPNv4 inbound route map filter. | MaxLen: 35
    route_map_in_vpnv6: str  # VPNv6 inbound route map filter. | MaxLen: 35
    route_map_in_evpn: str  # L2VPN EVPN inbound route map filter. | MaxLen: 35
    route_map_out: str  # IPv4 outbound route map filter. | MaxLen: 35
    route_map_out_preferable: str  # IPv4 outbound route map filter if the peer is pref | MaxLen: 35
    route_map_out6: str  # IPv6 Outbound route map filter. | MaxLen: 35
    route_map_out6_preferable: str  # IPv6 outbound route map filter if the peer is pref | MaxLen: 35
    route_map_out_vpnv4: str  # VPNv4 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv6: str  # VPNv6 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv4_preferable: str  # VPNv4 outbound route map filter if the peer is pre | MaxLen: 35
    route_map_out_vpnv6_preferable: str  # VPNv6 outbound route map filter if this neighbor i | MaxLen: 35
    route_map_out_evpn: str  # L2VPN EVPN outbound route map filter. | MaxLen: 35
    send_community: Literal["standard", "extended", "both", "disable"]  # IPv4 Send community attribute to neighbor. | Default: both
    send_community6: Literal["standard", "extended", "both", "disable"]  # IPv6 Send community attribute to neighbor. | Default: both
    send_community_vpnv4: Literal["standard", "extended", "both", "disable"]  # Send community attribute to neighbor for VPNv4 add | Default: both
    send_community_vpnv6: Literal["standard", "extended", "both", "disable"]  # Enable/disable sending community attribute to this | Default: both
    send_community_evpn: Literal["standard", "extended", "both", "disable"]  # Enable/disable sending community attribute to neig | Default: both
    keep_alive_timer: int  # Keep alive timer interval (sec). | Default: 4294967295 | Min: 0 | Max: 65535
    holdtime_timer: int  # Interval (sec) before peer considered dead. | Default: 4294967295 | Min: 3 | Max: 65535
    connect_timer: int  # Interval (sec) for connect timer. | Default: 4294967295 | Min: 1 | Max: 65535
    unsuppress_map: str  # IPv4 Route map to selectively unsuppress suppresse | MaxLen: 35
    unsuppress_map6: str  # IPv6 Route map to selectively unsuppress suppresse | MaxLen: 35
    update_source: str  # Interface to use as source IP/IPv6 address of TCP | MaxLen: 15
    weight: int  # Neighbor weight. | Default: 4294967295 | Min: 0 | Max: 65535
    restart_time: int  # Graceful restart delay time | Default: 0 | Min: 0 | Max: 3600
    additional_path: Literal["send", "receive", "both", "disable"]  # Enable/disable IPv4 additional-path capability. | Default: disable
    additional_path6: Literal["send", "receive", "both", "disable"]  # Enable/disable IPv6 additional-path capability. | Default: disable
    additional_path_vpnv4: Literal["send", "receive", "both", "disable"]  # Enable/disable VPNv4 additional-path capability. | Default: disable
    additional_path_vpnv6: Literal["send", "receive", "both", "disable"]  # Enable/disable VPNv6 additional-path capability. | Default: disable
    adv_additional_path: int  # Number of IPv4 additional paths that can be advert | Default: 2 | Min: 2 | Max: 255
    adv_additional_path6: int  # Number of IPv6 additional paths that can be advert | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv4: int  # Number of VPNv4 additional paths that can be adver | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv6: int  # Number of VPNv6 additional paths that can be adver | Default: 2 | Min: 2 | Max: 255
    password: str  # Password used in MD5 authentication. | MaxLen: 128
    auth_options: str  # Key-chain name for TCP authentication options. | MaxLen: 35


class BgpNeighborrangeItem(TypedDict):
    """Type hints for neighbor-range table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Neighbor range ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Neighbor range prefix. | Default: 0.0.0.0 0.0.0.0
    max_neighbor_num: int  # Maximum number of neighbors. | Default: 0 | Min: 1 | Max: 1000
    neighbor_group: str  # Neighbor group name. | MaxLen: 63


class BgpNeighborrange6Item(TypedDict):
    """Type hints for neighbor-range6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # IPv6 neighbor range ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix6: str  # IPv6 prefix. | Default: ::/0
    max_neighbor_num: int  # Maximum number of neighbors. | Default: 0 | Min: 1 | Max: 1000
    neighbor_group: str  # Neighbor group name. | MaxLen: 63


class BgpNetworkItem(TypedDict):
    """Type hints for network table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix: str  # Network prefix. | Default: 0.0.0.0 0.0.0.0
    network_import_check: Literal["global", "enable", "disable"]  # Configure insurance of BGP network route existence | Default: global
    backdoor: Literal["enable", "disable"]  # Enable/disable route as backdoor. | Default: disable
    route_map: str  # Route map to modify generated route. | MaxLen: 35
    prefix_name: str  # Name of firewall address or address group. | MaxLen: 79


class BgpNetwork6Item(TypedDict):
    """Type hints for network6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    prefix6: str  # Network IPv6 prefix. | Default: ::/0
    network_import_check: Literal["global", "enable", "disable"]  # Configure insurance of BGP network route existence | Default: global
    backdoor: Literal["enable", "disable"]  # Enable/disable route as backdoor. | Default: disable
    route_map: str  # Route map to modify generated route. | MaxLen: 35


class BgpRedistributeItem(TypedDict):
    """Type hints for redistribute table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Distribute list entry name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Status. | Default: disable
    route_map: str  # Route map name. | MaxLen: 35


class BgpRedistribute6Item(TypedDict):
    """Type hints for redistribute6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Distribute list entry name. | MaxLen: 35
    status: Literal["enable", "disable"]  # Status. | Default: disable
    route_map: str  # Route map name. | MaxLen: 35


class BgpAdmindistanceItem(TypedDict):
    """Type hints for admin-distance table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    neighbour_prefix: str  # Neighbor address prefix. | Default: 0.0.0.0 0.0.0.0
    route_list: str  # Access list of routes to apply new distance to. | MaxLen: 35
    distance: int  # Administrative distance to apply (1 - 255). | Default: 0 | Min: 1 | Max: 255


class BgpVrfItem(TypedDict):
    """Type hints for vrf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vrf: str  # Origin VRF ID <0-511>. | MaxLen: 7
    role: Literal["standalone", "ce", "pe"]  # VRF role. | Default: standalone
    rd: str  # Route Distinguisher: AA:NN|A.B.C.D:NN. | MaxLen: 79
    export_rt: str  # List of export route target.
    import_rt: str  # List of import route target.
    import_route_map: str  # Import route map. | MaxLen: 35
    leak_target: str  # Target VRF table.


class BgpVrf6Item(TypedDict):
    """Type hints for vrf6 table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    vrf: str  # Origin VRF ID <0-511>. | MaxLen: 7
    role: Literal["standalone", "ce", "pe"]  # VRF role. | Default: standalone
    rd: str  # Route Distinguisher: AA:NN|A.B.C.D:NN. | MaxLen: 79
    export_rt: str  # List of export route target.
    import_rt: str  # List of import route target.
    import_route_map: str  # Import route map. | MaxLen: 35
    leak_target: str  # Target VRF table.


# Nested classes for table field children (object mode)

@final
class BgpConfederationpeersObject:
    """Typed object for confederation-peers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Peer ID. | MaxLen: 79
    peer: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpAggregateaddressObject:
    """Typed object for aggregate-address table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Aggregate prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Enable/disable generate AS set path information. | Default: disable
    as_set: Literal["enable", "disable"]
    # Enable/disable filter more specific routes from updates. | Default: disable
    summary_only: Literal["enable", "disable"]
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpAggregateaddress6Object:
    """Typed object for aggregate-address6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Aggregate IPv6 prefix. | Default: ::/0
    prefix6: str
    # Enable/disable generate AS set path information. | Default: disable
    as_set: Literal["enable", "disable"]
    # Enable/disable filter more specific routes from updates. | Default: disable
    summary_only: Literal["enable", "disable"]
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpNeighborObject:
    """Typed object for neighbor table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IP/IPv6 address of neighbor. | MaxLen: 45
    ip: str
    # Minimum interval (sec) between sending updates. | Default: 30 | Min: 0 | Max: 600
    advertisement_interval: int
    # Enable/disable IPv4 Enable to allow my AS in AS path. | Default: disable
    allowas_in_enable: Literal["enable", "disable"]
    # Enable/disable IPv6 Enable to allow my AS in AS path. | Default: disable
    allowas_in_enable6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for VPNv4 route. | Default: disable
    allowas_in_enable_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of my AS in AS path for VPNv6 route. | Default: disable
    allowas_in_enable_vpnv6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for L2VPN EVPN rout | Default: disable
    allowas_in_enable_evpn: Literal["enable", "disable"]
    # IPv4 The maximum number of occurrence of my AS number allowe | Default: 3 | Min: 1 | Max: 10
    allowas_in: int
    # IPv6 The maximum number of occurrence of my AS number allowe | Default: 3 | Min: 1 | Max: 10
    allowas_in6: int
    # The maximum number of occurrence of my AS number allowed for | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv4: int
    # The maximum number of occurrence of my AS number allowed for | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv6: int
    # The maximum number of occurrence of my AS number allowed for | Default: 3 | Min: 1 | Max: 10
    allowas_in_evpn: int
    # IPv4 List of attributes that should be unchanged.
    attribute_unchanged: Literal["as-path", "med", "next-hop"]
    # IPv6 List of attributes that should be unchanged.
    attribute_unchanged6: Literal["as-path", "med", "next-hop"]
    # List of attributes that should be unchanged for VPNv4 route.
    attribute_unchanged_vpnv4: Literal["as-path", "med", "next-hop"]
    # List of attributes that should not be changed for VPNv6 rout
    attribute_unchanged_vpnv6: Literal["as-path", "med", "next-hop"]
    # Enable/disable address family IPv4 for this neighbor. | Default: enable
    activate: Literal["enable", "disable"]
    # Enable/disable address family IPv6 for this neighbor. | Default: enable
    activate6: Literal["enable", "disable"]
    # Enable/disable address family VPNv4 for this neighbor. | Default: enable
    activate_vpnv4: Literal["enable", "disable"]
    # Enable/disable address family VPNv6 for this neighbor. | Default: enable
    activate_vpnv6: Literal["enable", "disable"]
    # Enable/disable address family L2VPN EVPN for this neighbor. | Default: enable
    activate_evpn: Literal["enable", "disable"]
    # Enable/disable BFD for this neighbor. | Default: disable
    bfd: Literal["enable", "disable"]
    # Enable/disable advertise dynamic capability to this neighbor | Default: disable
    capability_dynamic: Literal["enable", "disable"]
    # Accept/Send IPv4 ORF lists to/from this neighbor. | Default: none
    capability_orf: Literal["none", "receive", "send", "both"]
    # Accept/Send IPv6 ORF lists to/from this neighbor. | Default: none
    capability_orf6: Literal["none", "receive", "send", "both"]
    # Enable/disable advertise IPv4 graceful restart capability to | Default: disable
    capability_graceful_restart: Literal["enable", "disable"]
    # Enable/disable advertise IPv6 graceful restart capability to | Default: disable
    capability_graceful_restart6: Literal["enable", "disable"]
    # Enable/disable advertise VPNv4 graceful restart capability t | Default: disable
    capability_graceful_restart_vpnv4: Literal["enable", "disable"]
    # Enable/disable advertisement of VPNv6 graceful restart capab | Default: disable
    capability_graceful_restart_vpnv6: Literal["enable", "disable"]
    # Enable/disable advertisement of L2VPN EVPN graceful restart | Default: disable
    capability_graceful_restart_evpn: Literal["enable", "disable"]
    # Enable/disable advertise route refresh capability to this ne | Default: enable
    capability_route_refresh: Literal["enable", "disable"]
    # Enable/disable advertise default IPv4 route to this neighbor | Default: disable
    capability_default_originate: Literal["enable", "disable"]
    # Enable/disable advertise default IPv6 route to this neighbor | Default: disable
    capability_default_originate6: Literal["enable", "disable"]
    # Do not negotiate capabilities with this neighbor. | Default: disable
    dont_capability_negotiate: Literal["enable", "disable"]
    # Enable/disable allow multi-hop EBGP neighbors. | Default: disable
    ebgp_enforce_multihop: Literal["enable", "disable"]
    # Enable/disable failover upon link down. | Default: disable
    link_down_failover: Literal["enable", "disable"]
    # Enable/disable stale route after neighbor down. | Default: disable
    stale_route: Literal["enable", "disable"]
    # Enable/disable IPv4 next-hop calculation for this neighbor. | Default: disable
    next_hop_self: Literal["enable", "disable"]
    # Enable/disable IPv6 next-hop calculation for this neighbor. | Default: disable
    next_hop_self6: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv4 | Default: disable
    next_hop_self_rr: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv6 | Default: disable
    next_hop_self_rr6: Literal["enable", "disable"]
    # Enable/disable setting VPNv4 next-hop to interface's IP addr | Default: disable
    next_hop_self_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of outgoing interface's IP address as VPN | Default: disable
    next_hop_self_vpnv6: Literal["enable", "disable"]
    # Enable/disable override result of capability negotiation. | Default: disable
    override_capability: Literal["enable", "disable"]
    # Enable/disable sending of open messages to this neighbor. | Default: disable
    passive: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv4 outbound u | Default: disable
    remove_private_as: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv6 outbound u | Default: disable
    remove_private_as6: Literal["enable", "disable"]
    # Enable/disable remove private AS number from VPNv4 outbound | Default: disable
    remove_private_as_vpnv4: Literal["enable", "disable"]
    # Enable/disable to remove private AS number from VPNv6 outbou | Default: disable
    remove_private_as_vpnv6: Literal["enable", "disable"]
    # Enable/disable removing private AS number from L2VPN EVPN ou | Default: disable
    remove_private_as_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route reflector client. | Default: disable
    route_reflector_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route reflector client. | Default: disable
    route_reflector_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route reflector client for this neig | Default: disable
    route_reflector_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route reflector client for this neig | Default: disable
    route_reflector_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route reflector client for this | Default: disable
    route_reflector_client_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route server client. | Default: disable
    route_server_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route server client. | Default: disable
    route_server_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route server client for this neighbo | Default: disable
    route_server_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route server client for this neighbo | Default: disable
    route_server_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route server client for this ne | Default: disable
    route_server_client_evpn: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change_vpnv4: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change_vpnv6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change_evpn: Literal["enable", "disable"]
    # Enable/disable shutdown this neighbor. | Default: disable
    shutdown: Literal["enable", "disable"]
    # Enable/disable allow IPv4 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration: Literal["enable", "disable"]
    # Enable/disable allow IPv6 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration6: Literal["enable", "disable"]
    # Enable/disable allow VPNv4 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_evpn: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv4. | Default: disable
    as_override: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv6. | Default: disable
    as_override6: Literal["enable", "disable"]
    # Enable/disable strict capability matching. | Default: disable
    strict_capability_match: Literal["enable", "disable"]
    # Route map to specify criteria to originate IPv4 default. | MaxLen: 35
    default_originate_routemap: str
    # Route map to specify criteria to originate IPv6 default. | MaxLen: 35
    default_originate_routemap6: str
    # Description. | MaxLen: 63
    description: str
    # Filter for IPv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in: str
    # Filter for IPv6 updates from this neighbor. | MaxLen: 35
    distribute_list_in6: str
    # Filter for VPNv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv4: str
    # Filter for VPNv6 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv6: str
    # Filter for IPv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out: str
    # Filter for IPv6 updates to this neighbor. | MaxLen: 35
    distribute_list_out6: str
    # Filter for VPNv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv4: str
    # Filter for VPNv6 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv6: str
    # EBGP multihop TTL for this peer. | Default: 255 | Min: 1 | Max: 255
    ebgp_multihop_ttl: int
    # BGP filter for IPv4 inbound routes. | MaxLen: 35
    filter_list_in: str
    # BGP filter for IPv6 inbound routes. | MaxLen: 35
    filter_list_in6: str
    # BGP filter for VPNv4 inbound routes. | MaxLen: 35
    filter_list_in_vpnv4: str
    # BGP filter for VPNv6 inbound routes. | MaxLen: 35
    filter_list_in_vpnv6: str
    # BGP filter for IPv4 outbound routes. | MaxLen: 35
    filter_list_out: str
    # BGP filter for IPv6 outbound routes. | MaxLen: 35
    filter_list_out6: str
    # BGP filter for VPNv4 outbound routes. | MaxLen: 35
    filter_list_out_vpnv4: str
    # BGP filter for VPNv6 outbound routes. | MaxLen: 35
    filter_list_out_vpnv6: str
    # Specify outgoing interface for peer connection. For IPv6 pee | MaxLen: 15
    interface: str
    # Maximum number of IPv4 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix: int
    # Maximum number of IPv6 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix6: int
    # Maximum number of VPNv4 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv4: int
    # Maximum number of VPNv6 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv6: int
    # Maximum number of L2VPN EVPN prefixes to accept from this pe | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_evpn: int
    # Maximum IPv4 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold: int
    # Maximum IPv6 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold6: int
    # Maximum VPNv4 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv4: int
    # Maximum VPNv6 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv6: int
    # Maximum L2VPN EVPN prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_evpn: int
    # Enable/disable IPv4 Only give warning message when limit is | Default: disable
    maximum_prefix_warning_only: Literal["enable", "disable"]
    # Enable/disable IPv6 Only give warning message when limit is | Default: disable
    maximum_prefix_warning_only6: Literal["enable", "disable"]
    # Enable/disable only giving warning message when limit is exc | Default: disable
    maximum_prefix_warning_only_vpnv4: Literal["enable", "disable"]
    # Enable/disable warning message when limit is exceeded for VP | Default: disable
    maximum_prefix_warning_only_vpnv6: Literal["enable", "disable"]
    # Enable/disable only sending warning message when exceeding l | Default: disable
    maximum_prefix_warning_only_evpn: Literal["enable", "disable"]
    # IPv4 Inbound filter for updates from this neighbor. | MaxLen: 35
    prefix_list_in: str
    # IPv6 Inbound filter for updates from this neighbor. | MaxLen: 35
    prefix_list_in6: str
    # Inbound filter for VPNv4 updates from this neighbor. | MaxLen: 35
    prefix_list_in_vpnv4: str
    # Inbound filter for VPNv6 updates from this neighbor. | MaxLen: 35
    prefix_list_in_vpnv6: str
    # IPv4 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out: str
    # IPv6 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out6: str
    # Outbound filter for VPNv4 updates to this neighbor. | MaxLen: 35
    prefix_list_out_vpnv4: str
    # Outbound filter for VPNv6 updates to this neighbor. | MaxLen: 35
    prefix_list_out_vpnv6: str
    # AS number of neighbor.
    remote_as: str
    # Local AS number of neighbor.
    local_as: str
    # Do not prepend local-as to incoming updates. | Default: disable
    local_as_no_prepend: Literal["enable", "disable"]
    # Replace real AS with local-as in outgoing updates. | Default: disable
    local_as_replace_as: Literal["enable", "disable"]
    # Time to retain stale routes. | Default: 0 | Min: 0 | Max: 65535
    retain_stale_time: int
    # IPv4 Inbound route map filter. | MaxLen: 35
    route_map_in: str
    # IPv6 Inbound route map filter. | MaxLen: 35
    route_map_in6: str
    # VPNv4 inbound route map filter. | MaxLen: 35
    route_map_in_vpnv4: str
    # VPNv6 inbound route map filter. | MaxLen: 35
    route_map_in_vpnv6: str
    # L2VPN EVPN inbound route map filter. | MaxLen: 35
    route_map_in_evpn: str
    # IPv4 outbound route map filter. | MaxLen: 35
    route_map_out: str
    # IPv4 outbound route map filter if the peer is preferred. | MaxLen: 35
    route_map_out_preferable: str
    # IPv6 Outbound route map filter. | MaxLen: 35
    route_map_out6: str
    # IPv6 outbound route map filter if the peer is preferred. | MaxLen: 35
    route_map_out6_preferable: str
    # VPNv4 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv4: str
    # VPNv6 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv6: str
    # VPNv4 outbound route map filter if the peer is preferred. | MaxLen: 35
    route_map_out_vpnv4_preferable: str
    # VPNv6 outbound route map filter if this neighbor is preferre | MaxLen: 35
    route_map_out_vpnv6_preferable: str
    # L2VPN EVPN outbound route map filter. | MaxLen: 35
    route_map_out_evpn: str
    # IPv4 Send community attribute to neighbor. | Default: both
    send_community: Literal["standard", "extended", "both", "disable"]
    # IPv6 Send community attribute to neighbor. | Default: both
    send_community6: Literal["standard", "extended", "both", "disable"]
    # Send community attribute to neighbor for VPNv4 address famil | Default: both
    send_community_vpnv4: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to this neighbor | Default: both
    send_community_vpnv6: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to neighbor for L | Default: both
    send_community_evpn: Literal["standard", "extended", "both", "disable"]
    # Keep alive timer interval (sec). | Default: 4294967295 | Min: 0 | Max: 65535
    keep_alive_timer: int
    # Interval (sec) before peer considered dead. | Default: 4294967295 | Min: 3 | Max: 65535
    holdtime_timer: int
    # Interval (sec) for connect timer. | Default: 4294967295 | Min: 1 | Max: 65535
    connect_timer: int
    # IPv4 Route map to selectively unsuppress suppressed routes. | MaxLen: 35
    unsuppress_map: str
    # IPv6 Route map to selectively unsuppress suppressed routes. | MaxLen: 35
    unsuppress_map6: str
    # Interface to use as source IP/IPv6 address of TCP connection | MaxLen: 15
    update_source: str
    # Neighbor weight. | Default: 4294967295 | Min: 0 | Max: 65535
    weight: int
    # Graceful restart delay time (sec, 0 = global default). | Default: 0 | Min: 0 | Max: 3600
    restart_time: int
    # Enable/disable IPv4 additional-path capability. | Default: disable
    additional_path: Literal["send", "receive", "both", "disable"]
    # Enable/disable IPv6 additional-path capability. | Default: disable
    additional_path6: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv4 additional-path capability. | Default: disable
    additional_path_vpnv4: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv6 additional-path capability. | Default: disable
    additional_path_vpnv6: Literal["send", "receive", "both", "disable"]
    # Number of IPv4 additional paths that can be advertised to th | Default: 2 | Min: 2 | Max: 255
    adv_additional_path: int
    # Number of IPv6 additional paths that can be advertised to th | Default: 2 | Min: 2 | Max: 255
    adv_additional_path6: int
    # Number of VPNv4 additional paths that can be advertised to t | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv4: int
    # Number of VPNv6 additional paths that can be advertised to t | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv6: int
    # Password used in MD5 authentication. | MaxLen: 128
    password: str
    # Key-chain name for TCP authentication options. | MaxLen: 35
    auth_options: str
    # Conditional advertisement.
    conditional_advertise: str
    # IPv6 conditional advertisement.
    conditional_advertise6: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpNeighborgroupObject:
    """Typed object for neighbor-group table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor group name. | MaxLen: 45
    name: str
    # Minimum interval (sec) between sending updates. | Default: 30 | Min: 0 | Max: 600
    advertisement_interval: int
    # Enable/disable IPv4 Enable to allow my AS in AS path. | Default: disable
    allowas_in_enable: Literal["enable", "disable"]
    # Enable/disable IPv6 Enable to allow my AS in AS path. | Default: disable
    allowas_in_enable6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for VPNv4 route. | Default: disable
    allowas_in_enable_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of my AS in AS path for VPNv6 route. | Default: disable
    allowas_in_enable_vpnv6: Literal["enable", "disable"]
    # Enable/disable to allow my AS in AS path for L2VPN EVPN rout | Default: disable
    allowas_in_enable_evpn: Literal["enable", "disable"]
    # IPv4 The maximum number of occurrence of my AS number allowe | Default: 3 | Min: 1 | Max: 10
    allowas_in: int
    # IPv6 The maximum number of occurrence of my AS number allowe | Default: 3 | Min: 1 | Max: 10
    allowas_in6: int
    # The maximum number of occurrence of my AS number allowed for | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv4: int
    # The maximum number of occurrence of my AS number allowed for | Default: 3 | Min: 1 | Max: 10
    allowas_in_vpnv6: int
    # The maximum number of occurrence of my AS number allowed for | Default: 3 | Min: 1 | Max: 10
    allowas_in_evpn: int
    # IPv4 List of attributes that should be unchanged.
    attribute_unchanged: Literal["as-path", "med", "next-hop"]
    # IPv6 List of attributes that should be unchanged.
    attribute_unchanged6: Literal["as-path", "med", "next-hop"]
    # List of attributes that should be unchanged for VPNv4 route.
    attribute_unchanged_vpnv4: Literal["as-path", "med", "next-hop"]
    # List of attributes that should not be changed for VPNv6 rout
    attribute_unchanged_vpnv6: Literal["as-path", "med", "next-hop"]
    # Enable/disable address family IPv4 for this neighbor. | Default: enable
    activate: Literal["enable", "disable"]
    # Enable/disable address family IPv6 for this neighbor. | Default: enable
    activate6: Literal["enable", "disable"]
    # Enable/disable address family VPNv4 for this neighbor. | Default: enable
    activate_vpnv4: Literal["enable", "disable"]
    # Enable/disable address family VPNv6 for this neighbor. | Default: enable
    activate_vpnv6: Literal["enable", "disable"]
    # Enable/disable address family L2VPN EVPN for this neighbor. | Default: enable
    activate_evpn: Literal["enable", "disable"]
    # Enable/disable BFD for this neighbor. | Default: disable
    bfd: Literal["enable", "disable"]
    # Enable/disable advertise dynamic capability to this neighbor | Default: disable
    capability_dynamic: Literal["enable", "disable"]
    # Accept/Send IPv4 ORF lists to/from this neighbor. | Default: none
    capability_orf: Literal["none", "receive", "send", "both"]
    # Accept/Send IPv6 ORF lists to/from this neighbor. | Default: none
    capability_orf6: Literal["none", "receive", "send", "both"]
    # Enable/disable advertise IPv4 graceful restart capability to | Default: disable
    capability_graceful_restart: Literal["enable", "disable"]
    # Enable/disable advertise IPv6 graceful restart capability to | Default: disable
    capability_graceful_restart6: Literal["enable", "disable"]
    # Enable/disable advertise VPNv4 graceful restart capability t | Default: disable
    capability_graceful_restart_vpnv4: Literal["enable", "disable"]
    # Enable/disable advertisement of VPNv6 graceful restart capab | Default: disable
    capability_graceful_restart_vpnv6: Literal["enable", "disable"]
    # Enable/disable advertisement of L2VPN EVPN graceful restart | Default: disable
    capability_graceful_restart_evpn: Literal["enable", "disable"]
    # Enable/disable advertise route refresh capability to this ne | Default: enable
    capability_route_refresh: Literal["enable", "disable"]
    # Enable/disable advertise default IPv4 route to this neighbor | Default: disable
    capability_default_originate: Literal["enable", "disable"]
    # Enable/disable advertise default IPv6 route to this neighbor | Default: disable
    capability_default_originate6: Literal["enable", "disable"]
    # Do not negotiate capabilities with this neighbor. | Default: disable
    dont_capability_negotiate: Literal["enable", "disable"]
    # Enable/disable allow multi-hop EBGP neighbors. | Default: disable
    ebgp_enforce_multihop: Literal["enable", "disable"]
    # Enable/disable failover upon link down. | Default: disable
    link_down_failover: Literal["enable", "disable"]
    # Enable/disable stale route after neighbor down. | Default: disable
    stale_route: Literal["enable", "disable"]
    # Enable/disable IPv4 next-hop calculation for this neighbor. | Default: disable
    next_hop_self: Literal["enable", "disable"]
    # Enable/disable IPv6 next-hop calculation for this neighbor. | Default: disable
    next_hop_self6: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv4 | Default: disable
    next_hop_self_rr: Literal["enable", "disable"]
    # Enable/disable setting nexthop's address to interface's IPv6 | Default: disable
    next_hop_self_rr6: Literal["enable", "disable"]
    # Enable/disable setting VPNv4 next-hop to interface's IP addr | Default: disable
    next_hop_self_vpnv4: Literal["enable", "disable"]
    # Enable/disable use of outgoing interface's IP address as VPN | Default: disable
    next_hop_self_vpnv6: Literal["enable", "disable"]
    # Enable/disable override result of capability negotiation. | Default: disable
    override_capability: Literal["enable", "disable"]
    # Enable/disable sending of open messages to this neighbor. | Default: enable
    passive: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv4 outbound u | Default: disable
    remove_private_as: Literal["enable", "disable"]
    # Enable/disable remove private AS number from IPv6 outbound u | Default: disable
    remove_private_as6: Literal["enable", "disable"]
    # Enable/disable remove private AS number from VPNv4 outbound | Default: disable
    remove_private_as_vpnv4: Literal["enable", "disable"]
    # Enable/disable to remove private AS number from VPNv6 outbou | Default: disable
    remove_private_as_vpnv6: Literal["enable", "disable"]
    # Enable/disable removing private AS number from L2VPN EVPN ou | Default: disable
    remove_private_as_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route reflector client. | Default: disable
    route_reflector_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route reflector client. | Default: disable
    route_reflector_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route reflector client for this neig | Default: disable
    route_reflector_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route reflector client for this neig | Default: disable
    route_reflector_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route reflector client for this | Default: disable
    route_reflector_client_evpn: Literal["enable", "disable"]
    # Enable/disable IPv4 AS route server client. | Default: disable
    route_server_client: Literal["enable", "disable"]
    # Enable/disable IPv6 AS route server client. | Default: disable
    route_server_client6: Literal["enable", "disable"]
    # Enable/disable VPNv4 AS route server client for this neighbo | Default: disable
    route_server_client_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 AS route server client for this neighbo | Default: disable
    route_server_client_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN AS route server client for this ne | Default: disable
    route_server_client_evpn: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change_vpnv4: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change_vpnv6: Literal["enable", "disable"]
    # Enable/disable allowing change of route attributes when adve | Default: disable
    rr_attr_allow_change_evpn: Literal["enable", "disable"]
    # Enable/disable shutdown this neighbor. | Default: disable
    shutdown: Literal["enable", "disable"]
    # Enable/disable allow IPv4 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration: Literal["enable", "disable"]
    # Enable/disable allow IPv6 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration6: Literal["enable", "disable"]
    # Enable/disable allow VPNv4 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_vpnv4: Literal["enable", "disable"]
    # Enable/disable VPNv6 inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_vpnv6: Literal["enable", "disable"]
    # Enable/disable L2VPN EVPN inbound soft reconfiguration. | Default: disable
    soft_reconfiguration_evpn: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv4. | Default: disable
    as_override: Literal["enable", "disable"]
    # Enable/disable replace peer AS with own AS for IPv6. | Default: disable
    as_override6: Literal["enable", "disable"]
    # Enable/disable strict capability matching. | Default: disable
    strict_capability_match: Literal["enable", "disable"]
    # Route map to specify criteria to originate IPv4 default. | MaxLen: 35
    default_originate_routemap: str
    # Route map to specify criteria to originate IPv6 default. | MaxLen: 35
    default_originate_routemap6: str
    # Description. | MaxLen: 63
    description: str
    # Filter for IPv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in: str
    # Filter for IPv6 updates from this neighbor. | MaxLen: 35
    distribute_list_in6: str
    # Filter for VPNv4 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv4: str
    # Filter for VPNv6 updates from this neighbor. | MaxLen: 35
    distribute_list_in_vpnv6: str
    # Filter for IPv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out: str
    # Filter for IPv6 updates to this neighbor. | MaxLen: 35
    distribute_list_out6: str
    # Filter for VPNv4 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv4: str
    # Filter for VPNv6 updates to this neighbor. | MaxLen: 35
    distribute_list_out_vpnv6: str
    # EBGP multihop TTL for this peer. | Default: 255 | Min: 1 | Max: 255
    ebgp_multihop_ttl: int
    # BGP filter for IPv4 inbound routes. | MaxLen: 35
    filter_list_in: str
    # BGP filter for IPv6 inbound routes. | MaxLen: 35
    filter_list_in6: str
    # BGP filter for VPNv4 inbound routes. | MaxLen: 35
    filter_list_in_vpnv4: str
    # BGP filter for VPNv6 inbound routes. | MaxLen: 35
    filter_list_in_vpnv6: str
    # BGP filter for IPv4 outbound routes. | MaxLen: 35
    filter_list_out: str
    # BGP filter for IPv6 outbound routes. | MaxLen: 35
    filter_list_out6: str
    # BGP filter for VPNv4 outbound routes. | MaxLen: 35
    filter_list_out_vpnv4: str
    # BGP filter for VPNv6 outbound routes. | MaxLen: 35
    filter_list_out_vpnv6: str
    # Specify outgoing interface for peer connection. For IPv6 pee | MaxLen: 15
    interface: str
    # Maximum number of IPv4 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix: int
    # Maximum number of IPv6 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix6: int
    # Maximum number of VPNv4 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv4: int
    # Maximum number of VPNv6 prefixes to accept from this peer. | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_vpnv6: int
    # Maximum number of L2VPN EVPN prefixes to accept from this pe | Default: 0 | Min: 1 | Max: 4294967295
    maximum_prefix_evpn: int
    # Maximum IPv4 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold: int
    # Maximum IPv6 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold6: int
    # Maximum VPNv4 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv4: int
    # Maximum VPNv6 prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_vpnv6: int
    # Maximum L2VPN EVPN prefix threshold value (1 - 100 percent). | Default: 75 | Min: 1 | Max: 100
    maximum_prefix_threshold_evpn: int
    # Enable/disable IPv4 Only give warning message when limit is | Default: disable
    maximum_prefix_warning_only: Literal["enable", "disable"]
    # Enable/disable IPv6 Only give warning message when limit is | Default: disable
    maximum_prefix_warning_only6: Literal["enable", "disable"]
    # Enable/disable only giving warning message when limit is exc | Default: disable
    maximum_prefix_warning_only_vpnv4: Literal["enable", "disable"]
    # Enable/disable warning message when limit is exceeded for VP | Default: disable
    maximum_prefix_warning_only_vpnv6: Literal["enable", "disable"]
    # Enable/disable only sending warning message when exceeding l | Default: disable
    maximum_prefix_warning_only_evpn: Literal["enable", "disable"]
    # IPv4 Inbound filter for updates from this neighbor. | MaxLen: 35
    prefix_list_in: str
    # IPv6 Inbound filter for updates from this neighbor. | MaxLen: 35
    prefix_list_in6: str
    # Inbound filter for VPNv4 updates from this neighbor. | MaxLen: 35
    prefix_list_in_vpnv4: str
    # Inbound filter for VPNv6 updates from this neighbor. | MaxLen: 35
    prefix_list_in_vpnv6: str
    # IPv4 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out: str
    # IPv6 Outbound filter for updates to this neighbor. | MaxLen: 35
    prefix_list_out6: str
    # Outbound filter for VPNv4 updates to this neighbor. | MaxLen: 35
    prefix_list_out_vpnv4: str
    # Outbound filter for VPNv6 updates to this neighbor. | MaxLen: 35
    prefix_list_out_vpnv6: str
    # AS number of neighbor.
    remote_as: str
    # BGP filter for remote AS. | MaxLen: 35
    remote_as_filter: str
    # Local AS number of neighbor.
    local_as: str
    # Do not prepend local-as to incoming updates. | Default: disable
    local_as_no_prepend: Literal["enable", "disable"]
    # Replace real AS with local-as in outgoing updates. | Default: disable
    local_as_replace_as: Literal["enable", "disable"]
    # Time to retain stale routes. | Default: 0 | Min: 0 | Max: 65535
    retain_stale_time: int
    # IPv4 Inbound route map filter. | MaxLen: 35
    route_map_in: str
    # IPv6 Inbound route map filter. | MaxLen: 35
    route_map_in6: str
    # VPNv4 inbound route map filter. | MaxLen: 35
    route_map_in_vpnv4: str
    # VPNv6 inbound route map filter. | MaxLen: 35
    route_map_in_vpnv6: str
    # L2VPN EVPN inbound route map filter. | MaxLen: 35
    route_map_in_evpn: str
    # IPv4 outbound route map filter. | MaxLen: 35
    route_map_out: str
    # IPv4 outbound route map filter if the peer is preferred. | MaxLen: 35
    route_map_out_preferable: str
    # IPv6 Outbound route map filter. | MaxLen: 35
    route_map_out6: str
    # IPv6 outbound route map filter if the peer is preferred. | MaxLen: 35
    route_map_out6_preferable: str
    # VPNv4 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv4: str
    # VPNv6 outbound route map filter. | MaxLen: 35
    route_map_out_vpnv6: str
    # VPNv4 outbound route map filter if the peer is preferred. | MaxLen: 35
    route_map_out_vpnv4_preferable: str
    # VPNv6 outbound route map filter if this neighbor is preferre | MaxLen: 35
    route_map_out_vpnv6_preferable: str
    # L2VPN EVPN outbound route map filter. | MaxLen: 35
    route_map_out_evpn: str
    # IPv4 Send community attribute to neighbor. | Default: both
    send_community: Literal["standard", "extended", "both", "disable"]
    # IPv6 Send community attribute to neighbor. | Default: both
    send_community6: Literal["standard", "extended", "both", "disable"]
    # Send community attribute to neighbor for VPNv4 address famil | Default: both
    send_community_vpnv4: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to this neighbor | Default: both
    send_community_vpnv6: Literal["standard", "extended", "both", "disable"]
    # Enable/disable sending community attribute to neighbor for L | Default: both
    send_community_evpn: Literal["standard", "extended", "both", "disable"]
    # Keep alive timer interval (sec). | Default: 4294967295 | Min: 0 | Max: 65535
    keep_alive_timer: int
    # Interval (sec) before peer considered dead. | Default: 4294967295 | Min: 3 | Max: 65535
    holdtime_timer: int
    # Interval (sec) for connect timer. | Default: 4294967295 | Min: 1 | Max: 65535
    connect_timer: int
    # IPv4 Route map to selectively unsuppress suppressed routes. | MaxLen: 35
    unsuppress_map: str
    # IPv6 Route map to selectively unsuppress suppressed routes. | MaxLen: 35
    unsuppress_map6: str
    # Interface to use as source IP/IPv6 address of TCP connection | MaxLen: 15
    update_source: str
    # Neighbor weight. | Default: 4294967295 | Min: 0 | Max: 65535
    weight: int
    # Graceful restart delay time (sec, 0 = global default). | Default: 0 | Min: 0 | Max: 3600
    restart_time: int
    # Enable/disable IPv4 additional-path capability. | Default: disable
    additional_path: Literal["send", "receive", "both", "disable"]
    # Enable/disable IPv6 additional-path capability. | Default: disable
    additional_path6: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv4 additional-path capability. | Default: disable
    additional_path_vpnv4: Literal["send", "receive", "both", "disable"]
    # Enable/disable VPNv6 additional-path capability. | Default: disable
    additional_path_vpnv6: Literal["send", "receive", "both", "disable"]
    # Number of IPv4 additional paths that can be advertised to th | Default: 2 | Min: 2 | Max: 255
    adv_additional_path: int
    # Number of IPv6 additional paths that can be advertised to th | Default: 2 | Min: 2 | Max: 255
    adv_additional_path6: int
    # Number of VPNv4 additional paths that can be advertised to t | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv4: int
    # Number of VPNv6 additional paths that can be advertised to t | Default: 2 | Min: 2 | Max: 255
    adv_additional_path_vpnv6: int
    # Password used in MD5 authentication. | MaxLen: 128
    password: str
    # Key-chain name for TCP authentication options. | MaxLen: 35
    auth_options: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpNeighborrangeObject:
    """Typed object for neighbor-range table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Neighbor range ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Neighbor range prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Maximum number of neighbors. | Default: 0 | Min: 1 | Max: 1000
    max_neighbor_num: int
    # Neighbor group name. | MaxLen: 63
    neighbor_group: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpNeighborrange6Object:
    """Typed object for neighbor-range6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # IPv6 neighbor range ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # IPv6 prefix. | Default: ::/0
    prefix6: str
    # Maximum number of neighbors. | Default: 0 | Min: 1 | Max: 1000
    max_neighbor_num: int
    # Neighbor group name. | MaxLen: 63
    neighbor_group: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpNetworkObject:
    """Typed object for network table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Network prefix. | Default: 0.0.0.0 0.0.0.0
    prefix: str
    # Configure insurance of BGP network route existence in IGP. | Default: global
    network_import_check: Literal["global", "enable", "disable"]
    # Enable/disable route as backdoor. | Default: disable
    backdoor: Literal["enable", "disable"]
    # Route map to modify generated route. | MaxLen: 35
    route_map: str
    # Name of firewall address or address group. | MaxLen: 79
    prefix_name: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpNetwork6Object:
    """Typed object for network6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Network IPv6 prefix. | Default: ::/0
    prefix6: str
    # Configure insurance of BGP network route existence in IGP. | Default: global
    network_import_check: Literal["global", "enable", "disable"]
    # Enable/disable route as backdoor. | Default: disable
    backdoor: Literal["enable", "disable"]
    # Route map to modify generated route. | MaxLen: 35
    route_map: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpRedistributeObject:
    """Typed object for redistribute table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list entry name. | MaxLen: 35
    name: str
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Route map name. | MaxLen: 35
    route_map: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpRedistribute6Object:
    """Typed object for redistribute6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Distribute list entry name. | MaxLen: 35
    name: str
    # Status. | Default: disable
    status: Literal["enable", "disable"]
    # Route map name. | MaxLen: 35
    route_map: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpAdmindistanceObject:
    """Typed object for admin-distance table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Neighbor address prefix. | Default: 0.0.0.0 0.0.0.0
    neighbour_prefix: str
    # Access list of routes to apply new distance to. | MaxLen: 35
    route_list: str
    # Administrative distance to apply (1 - 255). | Default: 0 | Min: 1 | Max: 255
    distance: int
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpVrfObject:
    """Typed object for vrf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Origin VRF ID <0-511>. | MaxLen: 7
    vrf: str
    # VRF role. | Default: standalone
    role: Literal["standalone", "ce", "pe"]
    # Route Distinguisher: AA:NN|A.B.C.D:NN. | MaxLen: 79
    rd: str
    # List of export route target.
    export_rt: str
    # List of import route target.
    import_rt: str
    # Import route map. | MaxLen: 35
    import_route_map: str
    # Target VRF table.
    leak_target: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


@final
class BgpVrf6Object:
    """Typed object for vrf6 table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Origin VRF ID <0-511>. | MaxLen: 7
    vrf: str
    # VRF role. | Default: standalone
    role: Literal["standalone", "ce", "pe"]
    # Route Distinguisher: AA:NN|A.B.C.D:NN. | MaxLen: 79
    rd: str
    # List of export route target.
    export_rt: str
    # List of import route target.
    import_rt: str
    # Import route map. | MaxLen: 35
    import_route_map: str
    # Target VRF table.
    leak_target: str
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class BgpResponse(TypedDict):
    """
    Type hints for router/bgp API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    asn: str  # Router AS number, asplain/asdot/asdot+ format, 0 t
    router_id: str  # Router ID.
    keepalive_timer: int  # Frequency to send keep alive requests. | Default: 60 | Min: 0 | Max: 65535
    holdtime_timer: int  # Number of seconds to mark peer as dead. | Default: 180 | Min: 3 | Max: 65535
    always_compare_med: Literal["enable", "disable"]  # Enable/disable always compare MED. | Default: disable
    bestpath_as_path_ignore: Literal["enable", "disable"]  # Enable/disable ignore AS path. | Default: disable
    bestpath_cmp_confed_aspath: Literal["enable", "disable"]  # Enable/disable compare federation AS path length. | Default: disable
    bestpath_cmp_routerid: Literal["enable", "disable"]  # Enable/disable compare router ID for identical EBG | Default: disable
    bestpath_med_confed: Literal["enable", "disable"]  # Enable/disable compare MED among confederation pat | Default: disable
    bestpath_med_missing_as_worst: Literal["enable", "disable"]  # Enable/disable treat missing MED as least preferre | Default: disable
    client_to_client_reflection: Literal["enable", "disable"]  # Enable/disable client-to-client route reflection. | Default: enable
    dampening: Literal["enable", "disable"]  # Enable/disable route-flap dampening. | Default: disable
    deterministic_med: Literal["enable", "disable"]  # Enable/disable enforce deterministic comparison of | Default: disable
    ebgp_multipath: Literal["enable", "disable"]  # Enable/disable EBGP multi-path. | Default: disable
    ibgp_multipath: Literal["enable", "disable"]  # Enable/disable IBGP multi-path. | Default: disable
    enforce_first_as: Literal["enable", "disable"]  # Enable/disable enforce first AS for EBGP routes. | Default: enable
    fast_external_failover: Literal["enable", "disable"]  # Enable/disable reset peer BGP session if link goes | Default: enable
    log_neighbour_changes: Literal["enable", "disable"]  # Log BGP neighbor changes. | Default: enable
    network_import_check: Literal["enable", "disable"]  # Enable/disable ensure BGP network route exists in | Default: enable
    ignore_optional_capability: Literal["enable", "disable"]  # Do not send unknown optional capability notificati | Default: enable
    additional_path: Literal["enable", "disable"]  # Enable/disable selection of BGP IPv4 additional pa | Default: disable
    additional_path6: Literal["enable", "disable"]  # Enable/disable selection of BGP IPv6 additional pa | Default: disable
    additional_path_vpnv4: Literal["enable", "disable"]  # Enable/disable selection of BGP VPNv4 additional p | Default: disable
    additional_path_vpnv6: Literal["enable", "disable"]  # Enable/disable selection of BGP VPNv6 additional p | Default: disable
    multipath_recursive_distance: Literal["enable", "disable"]  # Enable/disable use of recursive distance to select | Default: disable
    recursive_next_hop: Literal["enable", "disable"]  # Enable/disable recursive resolution of next-hop us | Default: disable
    recursive_inherit_priority: Literal["enable", "disable"]  # Enable/disable priority inheritance for recursive | Default: disable
    tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"]  # Configure tag-match mode. Resolves BGP routes with | Default: disable
    cluster_id: str  # Route reflector cluster ID. | Default: 0.0.0.0
    confederation_identifier: int  # Confederation identifier. | Default: 0 | Min: 1 | Max: 4294967295
    confederation_peers: list[BgpConfederationpeersItem]  # Confederation peers.
    dampening_route_map: str  # Criteria for dampening. | MaxLen: 35
    dampening_reachability_half_life: int  # Reachability half-life time for penalty (min). | Default: 15 | Min: 1 | Max: 45
    dampening_reuse: int  # Threshold to reuse routes. | Default: 750 | Min: 1 | Max: 20000
    dampening_suppress: int  # Threshold to suppress routes. | Default: 2000 | Min: 1 | Max: 20000
    dampening_max_suppress_time: int  # Maximum minutes a route can be suppressed. | Default: 60 | Min: 1 | Max: 255
    dampening_unreachability_half_life: int  # Unreachability half-life time for penalty (min). | Default: 15 | Min: 1 | Max: 45
    default_local_preference: int  # Default local preference. | Default: 100 | Min: 0 | Max: 4294967295
    scan_time: int  # Background scanner interval (sec), 0 to disable it | Default: 60 | Min: 5 | Max: 60
    distance_external: int  # Distance for routes external to the AS. | Default: 20 | Min: 1 | Max: 255
    distance_internal: int  # Distance for routes internal to the AS. | Default: 200 | Min: 1 | Max: 255
    distance_local: int  # Distance for routes local to the AS. | Default: 200 | Min: 1 | Max: 255
    synchronization: Literal["enable", "disable"]  # Enable/disable only advertise routes from iBGP if | Default: disable
    graceful_restart: Literal["enable", "disable"]  # Enable/disable BGP graceful restart capabilities. | Default: disable
    graceful_restart_time: int  # Time needed for neighbors to restart (sec). | Default: 120 | Min: 1 | Max: 3600
    graceful_stalepath_time: int  # Time to hold stale paths of restarting neighbor | Default: 360 | Min: 1 | Max: 3600
    graceful_update_delay: int  # Route advertisement/selection delay after restart | Default: 120 | Min: 1 | Max: 3600
    graceful_end_on_timer: Literal["enable", "disable"]  # Enable/disable to exit graceful restart on timer o | Default: disable
    additional_path_select: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    additional_path_select6: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    additional_path_select_vpnv4: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    additional_path_select_vpnv6: int  # Number of additional paths to be selected for each | Default: 2 | Min: 2 | Max: 255
    cross_family_conditional_adv: Literal["enable", "disable"]  # Enable/disable cross address family conditional ad | Default: disable
    aggregate_address: list[BgpAggregateaddressItem]  # BGP aggregate address table.
    aggregate_address6: list[BgpAggregateaddress6Item]  # BGP IPv6 aggregate address table.
    neighbor: list[BgpNeighborItem]  # BGP neighbor table.
    neighbor_group: list[BgpNeighborgroupItem]  # BGP neighbor group table.
    neighbor_range: list[BgpNeighborrangeItem]  # BGP neighbor range table.
    neighbor_range6: list[BgpNeighborrange6Item]  # BGP IPv6 neighbor range table.
    network: list[BgpNetworkItem]  # BGP network table.
    network6: list[BgpNetwork6Item]  # BGP IPv6 network table.
    redistribute: list[BgpRedistributeItem]  # BGP IPv4 redistribute table.
    redistribute6: list[BgpRedistribute6Item]  # BGP IPv6 redistribute table.
    admin_distance: list[BgpAdmindistanceItem]  # Administrative distance modifications.
    vrf: list[BgpVrfItem]  # BGP VRF leaking table.
    vrf6: list[BgpVrf6Item]  # BGP IPv6 VRF leaking table.


@final
class BgpObject:
    """Typed FortiObject for router/bgp with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Router AS number, asplain/asdot/asdot+ format, 0 to disable
    asn: str
    # Router ID.
    router_id: str
    # Frequency to send keep alive requests. | Default: 60 | Min: 0 | Max: 65535
    keepalive_timer: int
    # Number of seconds to mark peer as dead. | Default: 180 | Min: 3 | Max: 65535
    holdtime_timer: int
    # Enable/disable always compare MED. | Default: disable
    always_compare_med: Literal["enable", "disable"]
    # Enable/disable ignore AS path. | Default: disable
    bestpath_as_path_ignore: Literal["enable", "disable"]
    # Enable/disable compare federation AS path length. | Default: disable
    bestpath_cmp_confed_aspath: Literal["enable", "disable"]
    # Enable/disable compare router ID for identical EBGP paths. | Default: disable
    bestpath_cmp_routerid: Literal["enable", "disable"]
    # Enable/disable compare MED among confederation paths. | Default: disable
    bestpath_med_confed: Literal["enable", "disable"]
    # Enable/disable treat missing MED as least preferred. | Default: disable
    bestpath_med_missing_as_worst: Literal["enable", "disable"]
    # Enable/disable client-to-client route reflection. | Default: enable
    client_to_client_reflection: Literal["enable", "disable"]
    # Enable/disable route-flap dampening. | Default: disable
    dampening: Literal["enable", "disable"]
    # Enable/disable enforce deterministic comparison of MED. | Default: disable
    deterministic_med: Literal["enable", "disable"]
    # Enable/disable EBGP multi-path. | Default: disable
    ebgp_multipath: Literal["enable", "disable"]
    # Enable/disable IBGP multi-path. | Default: disable
    ibgp_multipath: Literal["enable", "disable"]
    # Enable/disable enforce first AS for EBGP routes. | Default: enable
    enforce_first_as: Literal["enable", "disable"]
    # Enable/disable reset peer BGP session if link goes down. | Default: enable
    fast_external_failover: Literal["enable", "disable"]
    # Log BGP neighbor changes. | Default: enable
    log_neighbour_changes: Literal["enable", "disable"]
    # Enable/disable ensure BGP network route exists in IGP. | Default: enable
    network_import_check: Literal["enable", "disable"]
    # Do not send unknown optional capability notification message | Default: enable
    ignore_optional_capability: Literal["enable", "disable"]
    # Enable/disable selection of BGP IPv4 additional paths. | Default: disable
    additional_path: Literal["enable", "disable"]
    # Enable/disable selection of BGP IPv6 additional paths. | Default: disable
    additional_path6: Literal["enable", "disable"]
    # Enable/disable selection of BGP VPNv4 additional paths. | Default: disable
    additional_path_vpnv4: Literal["enable", "disable"]
    # Enable/disable selection of BGP VPNv6 additional paths. | Default: disable
    additional_path_vpnv6: Literal["enable", "disable"]
    # Enable/disable use of recursive distance to select multipath | Default: disable
    multipath_recursive_distance: Literal["enable", "disable"]
    # Enable/disable recursive resolution of next-hop using BGP ro | Default: disable
    recursive_next_hop: Literal["enable", "disable"]
    # Enable/disable priority inheritance for recursive resolution | Default: disable
    recursive_inherit_priority: Literal["enable", "disable"]
    # Configure tag-match mode. Resolves BGP routes with other rou | Default: disable
    tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"]
    # Route reflector cluster ID. | Default: 0.0.0.0
    cluster_id: str
    # Confederation identifier. | Default: 0 | Min: 1 | Max: 4294967295
    confederation_identifier: int
    # Confederation peers.
    confederation_peers: list[BgpConfederationpeersObject]
    # Criteria for dampening. | MaxLen: 35
    dampening_route_map: str
    # Reachability half-life time for penalty (min). | Default: 15 | Min: 1 | Max: 45
    dampening_reachability_half_life: int
    # Threshold to reuse routes. | Default: 750 | Min: 1 | Max: 20000
    dampening_reuse: int
    # Threshold to suppress routes. | Default: 2000 | Min: 1 | Max: 20000
    dampening_suppress: int
    # Maximum minutes a route can be suppressed. | Default: 60 | Min: 1 | Max: 255
    dampening_max_suppress_time: int
    # Unreachability half-life time for penalty (min). | Default: 15 | Min: 1 | Max: 45
    dampening_unreachability_half_life: int
    # Default local preference. | Default: 100 | Min: 0 | Max: 4294967295
    default_local_preference: int
    # Background scanner interval (sec), 0 to disable it. | Default: 60 | Min: 5 | Max: 60
    scan_time: int
    # Distance for routes external to the AS. | Default: 20 | Min: 1 | Max: 255
    distance_external: int
    # Distance for routes internal to the AS. | Default: 200 | Min: 1 | Max: 255
    distance_internal: int
    # Distance for routes local to the AS. | Default: 200 | Min: 1 | Max: 255
    distance_local: int
    # Enable/disable only advertise routes from iBGP if routes pre | Default: disable
    synchronization: Literal["enable", "disable"]
    # Enable/disable BGP graceful restart capabilities. | Default: disable
    graceful_restart: Literal["enable", "disable"]
    # Time needed for neighbors to restart (sec). | Default: 120 | Min: 1 | Max: 3600
    graceful_restart_time: int
    # Time to hold stale paths of restarting neighbor (sec). | Default: 360 | Min: 1 | Max: 3600
    graceful_stalepath_time: int
    # Route advertisement/selection delay after restart (sec). | Default: 120 | Min: 1 | Max: 3600
    graceful_update_delay: int
    # Enable/disable to exit graceful restart on timer only. | Default: disable
    graceful_end_on_timer: Literal["enable", "disable"]
    # Number of additional paths to be selected for each IPv4 NLRI | Default: 2 | Min: 2 | Max: 255
    additional_path_select: int
    # Number of additional paths to be selected for each IPv6 NLRI | Default: 2 | Min: 2 | Max: 255
    additional_path_select6: int
    # Number of additional paths to be selected for each VPNv4 NLR | Default: 2 | Min: 2 | Max: 255
    additional_path_select_vpnv4: int
    # Number of additional paths to be selected for each VPNv6 NLR | Default: 2 | Min: 2 | Max: 255
    additional_path_select_vpnv6: int
    # Enable/disable cross address family conditional advertisemen | Default: disable
    cross_family_conditional_adv: Literal["enable", "disable"]
    # BGP aggregate address table.
    aggregate_address: list[BgpAggregateaddressObject]
    # BGP IPv6 aggregate address table.
    aggregate_address6: list[BgpAggregateaddress6Object]
    # BGP neighbor table.
    neighbor: list[BgpNeighborObject]
    # BGP neighbor group table.
    neighbor_group: list[BgpNeighborgroupObject]
    # BGP neighbor range table.
    neighbor_range: list[BgpNeighborrangeObject]
    # BGP IPv6 neighbor range table.
    neighbor_range6: list[BgpNeighborrange6Object]
    # BGP network table.
    network: list[BgpNetworkObject]
    # BGP IPv6 network table.
    network6: list[BgpNetwork6Object]
    # BGP IPv4 redistribute table.
    redistribute: list[BgpRedistributeObject]
    # BGP IPv6 redistribute table.
    redistribute6: list[BgpRedistribute6Object]
    # Administrative distance modifications.
    admin_distance: list[BgpAdmindistanceObject]
    # BGP VRF leaking table.
    vrf: list[BgpVrfObject]
    # BGP IPv6 VRF leaking table.
    vrf6: list[BgpVrf6Object]
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> BgpPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Bgp:
    """
    Configure BGP.
    
    Path: router/bgp
    Category: cmdb
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> BgpObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> BgpObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> BgpObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> dict[str, Any] | FortiObject: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> BgpObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> BgpObject: ...
    
    @overload
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: BgpPayload | None = ...,
        asn: str | None = ...,
        router_id: str | None = ...,
        keepalive_timer: int | None = ...,
        holdtime_timer: int | None = ...,
        always_compare_med: Literal["enable", "disable"] | None = ...,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = ...,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = ...,
        bestpath_med_confed: Literal["enable", "disable"] | None = ...,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = ...,
        client_to_client_reflection: Literal["enable", "disable"] | None = ...,
        dampening: Literal["enable", "disable"] | None = ...,
        deterministic_med: Literal["enable", "disable"] | None = ...,
        ebgp_multipath: Literal["enable", "disable"] | None = ...,
        ibgp_multipath: Literal["enable", "disable"] | None = ...,
        enforce_first_as: Literal["enable", "disable"] | None = ...,
        fast_external_failover: Literal["enable", "disable"] | None = ...,
        log_neighbour_changes: Literal["enable", "disable"] | None = ...,
        network_import_check: Literal["enable", "disable"] | None = ...,
        ignore_optional_capability: Literal["enable", "disable"] | None = ...,
        additional_path: Literal["enable", "disable"] | None = ...,
        additional_path6: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv4: Literal["enable", "disable"] | None = ...,
        additional_path_vpnv6: Literal["enable", "disable"] | None = ...,
        multipath_recursive_distance: Literal["enable", "disable"] | None = ...,
        recursive_next_hop: Literal["enable", "disable"] | None = ...,
        recursive_inherit_priority: Literal["enable", "disable"] | None = ...,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = ...,
        cluster_id: str | None = ...,
        confederation_identifier: int | None = ...,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = ...,
        dampening_route_map: str | None = ...,
        dampening_reachability_half_life: int | None = ...,
        dampening_reuse: int | None = ...,
        dampening_suppress: int | None = ...,
        dampening_max_suppress_time: int | None = ...,
        dampening_unreachability_half_life: int | None = ...,
        default_local_preference: int | None = ...,
        scan_time: int | None = ...,
        distance_external: int | None = ...,
        distance_internal: int | None = ...,
        distance_local: int | None = ...,
        synchronization: Literal["enable", "disable"] | None = ...,
        graceful_restart: Literal["enable", "disable"] | None = ...,
        graceful_restart_time: int | None = ...,
        graceful_stalepath_time: int | None = ...,
        graceful_update_delay: int | None = ...,
        graceful_end_on_timer: Literal["enable", "disable"] | None = ...,
        additional_path_select: int | None = ...,
        additional_path_select6: int | None = ...,
        additional_path_select_vpnv4: int | None = ...,
        additional_path_select_vpnv6: int | None = ...,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = ...,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = ...,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = ...,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = ...,
        network: str | list[str] | list[dict[str, Any]] | None = ...,
        network6: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute: str | list[str] | list[dict[str, Any]] | None = ...,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = ...,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf: str | list[str] | list[dict[str, Any]] | None = ...,
        vrf6: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Bgp",
    "BgpPayload",
    "BgpResponse",
    "BgpObject",
]
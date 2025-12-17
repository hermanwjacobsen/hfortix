"""FortiOS CMDB - Router BGP - BGP configuration"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Bgp:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client
    def get(self, datasource: Optional[bool] = None, with_meta: Optional[bool] = None, skip: Optional[bool] = None, format: Optional[str] = None, action: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        params = {}
        if datasource is not None:
            params["datasource"] = datasource
        if with_meta is not None:
            params["with_meta"] = with_meta
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if action is not None:
            params["action"] = action
        params.update(kwargs)
        return self._client.get("cmdb", "router/bgp", params=params if params else None, vdom=vdom)
    def put(self, data_dict: Optional[dict[str, Any]] = None, as_number: Optional[int] = None, router_id: Optional[str] = None, keepalive_timer: Optional[int] = None, holdtime_timer: Optional[int] = None, always_compare_med: Optional[str] = None, bestpath_as_path_ignore: Optional[str] = None, bestpath_cmp_confed_aspath: Optional[str] = None, bestpath_cmp_routerid: Optional[str] = None, bestpath_med_confed: Optional[str] = None, bestpath_med_missing_as_worst: Optional[str] = None, client_to_client_reflection: Optional[str] = None, dampening: Optional[str] = None, deterministic_med: Optional[str] = None, ebgp_multipath: Optional[str] = None, ibgp_multipath: Optional[str] = None, enforce_first_as: Optional[str] = None, fast_external_failover: Optional[str] = None, log_neighbour_changes: Optional[str] = None, network_import_check: Optional[str] = None, ignore_optional_capability: Optional[str] = None, additional_path: Optional[str] = None, additional_path6: Optional[str] = None, multipath_recursive_distance: Optional[str] = None, recursive_next_hop: Optional[str] = None, cluster_id: Optional[str] = None, confederation_identifier: Optional[int] = None, confederation_peers: Optional[list] = None, dampening_route_map: Optional[str] = None, dampening_reachability_half_life: Optional[int] = None, dampening_reuse: Optional[int] = None, dampening_suppress: Optional[int] = None, dampening_max_suppress_time: Optional[int] = None, dampening_unreachability_half_life: Optional[int] = None, default_local_preference: Optional[int] = None, scan_time: Optional[int] = None, distance_external: Optional[int] = None, distance_internal: Optional[int] = None, distance_local: Optional[int] = None, synchronization: Optional[str] = None, graceful_restart: Optional[str] = None, graceful_restart_time: Optional[int] = None, graceful_stalepath_time: Optional[int] = None, graceful_update_delay: Optional[int] = None, graceful_end_on_timer: Optional[str] = None, additional_path_select: Optional[int] = None, additional_path_select6: Optional[int] = None, aggregate_address: Optional[list] = None, aggregate_address6: Optional[list] = None, neighbor: Optional[list] = None, neighbor_group: Optional[list] = None, neighbor_range: Optional[list] = None, neighbor_range6: Optional[list] = None, network: Optional[list] = None, network6: Optional[list] = None, redistribute: Optional[list] = None, redistribute6: Optional[list] = None, admin_distance: Optional[list] = None, vrf: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"as_number": "as", "router_id": "router-id", "keepalive_timer": "keepalive-timer", "holdtime_timer": "holdtime-timer", "always_compare_med": "always-compare-med", "bestpath_as_path_ignore": "bestpath-as-path-ignore", "bestpath_cmp_confed_aspath": "bestpath-cmp-confed-aspath", "bestpath_cmp_routerid": "bestpath-cmp-routerid", "bestpath_med_confed": "bestpath-med-confed", "bestpath_med_missing_as_worst": "bestpath-med-missing-as-worst", "client_to_client_reflection": "client-to-client-reflection", "deterministic_med": "deterministic-med", "ebgp_multipath": "ebgp-multipath", "ibgp_multipath": "ibgp-multipath", "enforce_first_as": "enforce-first-as", "fast_external_failover": "fast-external-failover", "log_neighbour_changes": "log-neighbour-changes", "network_import_check": "network-import-check", "ignore_optional_capability": "ignore-optional-capability", "additional_path": "additional-path", "additional_path6": "additional-path6", "multipath_recursive_distance": "multipath-recursive-distance", "recursive_next_hop": "recursive-next-hop", "cluster_id": "cluster-id", "confederation_identifier": "confederation-identifier", "confederation_peers": "confederation-peers", "dampening_route_map": "dampening-route-map", "dampening_reachability_half_life": "dampening-reachability-half-life", "dampening_reuse": "dampening-reuse", "dampening_suppress": "dampening-suppress", "dampening_max_suppress_time": "dampening-max-suppress-time", "dampening_unreachability_half_life": "dampening-unreachability-half-life", "default_local_preference": "default-local-preference", "scan_time": "scan-time", "distance_external": "distance-external", "distance_internal": "distance-internal", "distance_local": "distance-local", "graceful_restart": "graceful-restart", "graceful_restart_time": "graceful-restart-time", "graceful_stalepath_time": "graceful-stalepath-time", "graceful_update_delay": "graceful-update-delay", "graceful_end_on_timer": "graceful-end-on-timer", "additional_path_select": "additional-path-select", "additional_path_select6": "additional-path-select6", "aggregate_address": "aggregate-address", "aggregate_address6": "aggregate-address6", "neighbor_group": "neighbor-group", "neighbor_range": "neighbor-range", "neighbor_range6": "neighbor-range6", "admin_distance": "admin-distance"}
        if as_number is not None:
            data[param_map["as_number"]] = as_number
        if router_id is not None:
            data[param_map["router_id"]] = router_id
        if keepalive_timer is not None:
            data[param_map["keepalive_timer"]] = keepalive_timer
        if holdtime_timer is not None:
            data[param_map["holdtime_timer"]] = holdtime_timer
        if always_compare_med is not None:
            data[param_map["always_compare_med"]] = always_compare_med
        if bestpath_as_path_ignore is not None:
            data[param_map["bestpath_as_path_ignore"]] = bestpath_as_path_ignore
        if bestpath_cmp_confed_aspath is not None:
            data[param_map["bestpath_cmp_confed_aspath"]] = bestpath_cmp_confed_aspath
        if bestpath_cmp_routerid is not None:
            data[param_map["bestpath_cmp_routerid"]] = bestpath_cmp_routerid
        if bestpath_med_confed is not None:
            data[param_map["bestpath_med_confed"]] = bestpath_med_confed
        if bestpath_med_missing_as_worst is not None:
            data[param_map["bestpath_med_missing_as_worst"]] = bestpath_med_missing_as_worst
        if client_to_client_reflection is not None:
            data[param_map["client_to_client_reflection"]] = client_to_client_reflection
        if dampening is not None:
            data["dampening"] = dampening
        if deterministic_med is not None:
            data[param_map["deterministic_med"]] = deterministic_med
        if ebgp_multipath is not None:
            data[param_map["ebgp_multipath"]] = ebgp_multipath
        if ibgp_multipath is not None:
            data[param_map["ibgp_multipath"]] = ibgp_multipath
        if enforce_first_as is not None:
            data[param_map["enforce_first_as"]] = enforce_first_as
        if fast_external_failover is not None:
            data[param_map["fast_external_failover"]] = fast_external_failover
        if log_neighbour_changes is not None:
            data[param_map["log_neighbour_changes"]] = log_neighbour_changes
        if network_import_check is not None:
            data[param_map["network_import_check"]] = network_import_check
        if ignore_optional_capability is not None:
            data[param_map["ignore_optional_capability"]] = ignore_optional_capability
        if additional_path is not None:
            data[param_map["additional_path"]] = additional_path
        if additional_path6 is not None:
            data[param_map["additional_path6"]] = additional_path6
        if multipath_recursive_distance is not None:
            data[param_map["multipath_recursive_distance"]] = multipath_recursive_distance
        if recursive_next_hop is not None:
            data[param_map["recursive_next_hop"]] = recursive_next_hop
        if cluster_id is not None:
            data[param_map["cluster_id"]] = cluster_id
        if confederation_identifier is not None:
            data[param_map["confederation_identifier"]] = confederation_identifier
        if confederation_peers is not None:
            data[param_map["confederation_peers"]] = confederation_peers
        if dampening_route_map is not None:
            data[param_map["dampening_route_map"]] = dampening_route_map
        if dampening_reachability_half_life is not None:
            data[param_map["dampening_reachability_half_life"]] = dampening_reachability_half_life
        if dampening_reuse is not None:
            data[param_map["dampening_reuse"]] = dampening_reuse
        if dampening_suppress is not None:
            data[param_map["dampening_suppress"]] = dampening_suppress
        if dampening_max_suppress_time is not None:
            data[param_map["dampening_max_suppress_time"]] = dampening_max_suppress_time
        if dampening_unreachability_half_life is not None:
            data[param_map["dampening_unreachability_half_life"]] = dampening_unreachability_half_life
        if default_local_preference is not None:
            data[param_map["default_local_preference"]] = default_local_preference
        if scan_time is not None:
            data[param_map["scan_time"]] = scan_time
        if distance_external is not None:
            data[param_map["distance_external"]] = distance_external
        if distance_internal is not None:
            data[param_map["distance_internal"]] = distance_internal
        if distance_local is not None:
            data[param_map["distance_local"]] = distance_local
        if synchronization is not None:
            data["synchronization"] = synchronization
        if graceful_restart is not None:
            data[param_map["graceful_restart"]] = graceful_restart
        if graceful_restart_time is not None:
            data[param_map["graceful_restart_time"]] = graceful_restart_time
        if graceful_stalepath_time is not None:
            data[param_map["graceful_stalepath_time"]] = graceful_stalepath_time
        if graceful_update_delay is not None:
            data[param_map["graceful_update_delay"]] = graceful_update_delay
        if graceful_end_on_timer is not None:
            data[param_map["graceful_end_on_timer"]] = graceful_end_on_timer
        if additional_path_select is not None:
            data[param_map["additional_path_select"]] = additional_path_select
        if additional_path_select6 is not None:
            data[param_map["additional_path_select6"]] = additional_path_select6
        if aggregate_address is not None:
            data[param_map["aggregate_address"]] = aggregate_address
        if aggregate_address6 is not None:
            data[param_map["aggregate_address6"]] = aggregate_address6
        if neighbor is not None:
            data["neighbor"] = neighbor
        if neighbor_group is not None:
            data[param_map["neighbor_group"]] = neighbor_group
        if neighbor_range is not None:
            data[param_map["neighbor_range"]] = neighbor_range
        if neighbor_range6 is not None:
            data[param_map["neighbor_range6"]] = neighbor_range6
        if network is not None:
            data["network"] = network
        if network6 is not None:
            data["network6"] = network6
        if redistribute is not None:
            data["redistribute"] = redistribute
        if redistribute6 is not None:
            data["redistribute6"] = redistribute6
        if admin_distance is not None:
            data[param_map["admin_distance"]] = admin_distance
        if vrf is not None:
            data["vrf"] = vrf
        data.update(kwargs)
        return self._client.put("cmdb", "router/bgp", data=data, vdom=vdom)

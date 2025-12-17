"""FortiOS CMDB - Router OSPF - OSPF configuration"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Ospf:
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
        return self._client.get("cmdb", "router/ospf", params=params if params else None, vdom=vdom)
    def put(self, data_dict: Optional[dict[str, Any]] = None, abr_type: Optional[str] = None, auto_cost_ref_bandwidth: Optional[int] = None, distance_external: Optional[int] = None, distance_inter_area: Optional[int] = None, distance_intra_area: Optional[int] = None, database_overflow: Optional[str] = None, database_overflow_max_lsas: Optional[int] = None, database_overflow_time_to_recover: Optional[int] = None, default_information_originate: Optional[str] = None, default_information_metric: Optional[int] = None, default_information_metric_type: Optional[str] = None, default_information_route_map: Optional[str] = None, default_metric: Optional[int] = None, distance: Optional[int] = None, rfc1583_compatible: Optional[str] = None, router_id: Optional[str] = None, spf_timers: Optional[str] = None, bfd: Optional[str] = None, log_neighbour_changes: Optional[str] = None, distribute_list_in: Optional[str] = None, distribute_route_map_in: Optional[str] = None, restart_mode: Optional[str] = None, restart_period: Optional[int] = None, restart_on_topology_change: Optional[str] = None, area: Optional[list] = None, ospf_interface: Optional[list] = None, network: Optional[list] = None, neighbor: Optional[list] = None, passive_interface: Optional[list] = None, summary_address: Optional[list] = None, distribute_list: Optional[list] = None, redistribute: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"abr_type": "abr-type", "auto_cost_ref_bandwidth": "auto-cost-ref-bandwidth", "distance_external": "distance-external", "distance_inter_area": "distance-inter-area", "distance_intra_area": "distance-intra-area", "database_overflow": "database-overflow", "database_overflow_max_lsas": "database-overflow-max-lsas", "database_overflow_time_to_recover": "database-overflow-time-to-recover", "default_information_originate": "default-information-originate", "default_information_metric": "default-information-metric", "default_information_metric_type": "default-information-metric-type", "default_information_route_map": "default-information-route-map", "default_metric": "default-metric", "rfc1583_compatible": "rfc1583-compatible", "router_id": "router-id", "spf_timers": "spf-timers", "log_neighbour_changes": "log-neighbour-changes", "distribute_list_in": "distribute-list-in", "distribute_route_map_in": "distribute-route-map-in", "restart_mode": "restart-mode", "restart_period": "restart-period", "restart_on_topology_change": "restart-on-topology-change", "ospf_interface": "ospf-interface", "passive_interface": "passive-interface", "summary_address": "summary-address", "distribute_list": "distribute-list"}
        if abr_type is not None:
            data[param_map["abr_type"]] = abr_type
        if auto_cost_ref_bandwidth is not None:
            data[param_map["auto_cost_ref_bandwidth"]] = auto_cost_ref_bandwidth
        if distance_external is not None:
            data[param_map["distance_external"]] = distance_external
        if distance_inter_area is not None:
            data[param_map["distance_inter_area"]] = distance_inter_area
        if distance_intra_area is not None:
            data[param_map["distance_intra_area"]] = distance_intra_area
        if database_overflow is not None:
            data[param_map["database_overflow"]] = database_overflow
        if database_overflow_max_lsas is not None:
            data[param_map["database_overflow_max_lsas"]] = database_overflow_max_lsas
        if database_overflow_time_to_recover is not None:
            data[param_map["database_overflow_time_to_recover"]] = database_overflow_time_to_recover
        if default_information_originate is not None:
            data[param_map["default_information_originate"]] = default_information_originate
        if default_information_metric is not None:
            data[param_map["default_information_metric"]] = default_information_metric
        if default_information_metric_type is not None:
            data[param_map["default_information_metric_type"]] = default_information_metric_type
        if default_information_route_map is not None:
            data[param_map["default_information_route_map"]] = default_information_route_map
        if default_metric is not None:
            data[param_map["default_metric"]] = default_metric
        if distance is not None:
            data["distance"] = distance
        if rfc1583_compatible is not None:
            data[param_map["rfc1583_compatible"]] = rfc1583_compatible
        if router_id is not None:
            data[param_map["router_id"]] = router_id
        if spf_timers is not None:
            data[param_map["spf_timers"]] = spf_timers
        if bfd is not None:
            data["bfd"] = bfd
        if log_neighbour_changes is not None:
            data[param_map["log_neighbour_changes"]] = log_neighbour_changes
        if distribute_list_in is not None:
            data[param_map["distribute_list_in"]] = distribute_list_in
        if distribute_route_map_in is not None:
            data[param_map["distribute_route_map_in"]] = distribute_route_map_in
        if restart_mode is not None:
            data[param_map["restart_mode"]] = restart_mode
        if restart_period is not None:
            data[param_map["restart_period"]] = restart_period
        if restart_on_topology_change is not None:
            data[param_map["restart_on_topology_change"]] = restart_on_topology_change
        if area is not None:
            data["area"] = area
        if ospf_interface is not None:
            data[param_map["ospf_interface"]] = ospf_interface
        if network is not None:
            data["network"] = network
        if neighbor is not None:
            data["neighbor"] = neighbor
        if passive_interface is not None:
            data[param_map["passive_interface"]] = passive_interface
        if summary_address is not None:
            data[param_map["summary_address"]] = summary_address
        if distribute_list is not None:
            data[param_map["distribute_list"]] = distribute_list
        if redistribute is not None:
            data["redistribute"] = redistribute
        data.update(kwargs)
        return self._client.put("cmdb", "router/ospf", data=data, vdom=vdom)

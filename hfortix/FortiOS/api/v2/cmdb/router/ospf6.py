"""FortiOS CMDB - Router OSPF6 - OSPFv3 configuration"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Ospf6:
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
        return self._client.get("cmdb", "router/ospf6", params=params if params else None, vdom=vdom)
    def put(self, data_dict: Optional[dict[str, Any]] = None, abr_type: Optional[str] = None, auto_cost_ref_bandwidth: Optional[int] = None, default_information_originate: Optional[str] = None, default_information_metric: Optional[int] = None, default_information_metric_type: Optional[str] = None, default_information_route_map: Optional[str] = None, default_metric: Optional[int] = None, router_id: Optional[str] = None, spf_timers: Optional[str] = None, bfd: Optional[str] = None, log_neighbour_changes: Optional[str] = None, restart_mode: Optional[str] = None, restart_period: Optional[int] = None, restart_on_topology_change: Optional[str] = None, area: Optional[list] = None, ospf6_interface: Optional[list] = None, summary_address: Optional[list] = None, redistribute: Optional[list] = None, passive_interface: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"abr_type": "abr-type", "auto_cost_ref_bandwidth": "auto-cost-ref-bandwidth", "default_information_originate": "default-information-originate", "default_information_metric": "default-information-metric", "default_information_metric_type": "default-information-metric-type", "default_information_route_map": "default-information-route-map", "default_metric": "default-metric", "router_id": "router-id", "spf_timers": "spf-timers", "log_neighbour_changes": "log-neighbour-changes", "restart_mode": "restart-mode", "restart_period": "restart-period", "restart_on_topology_change": "restart-on-topology-change", "ospf6_interface": "ospf6-interface", "summary_address": "summary-address", "passive_interface": "passive-interface"}
        if abr_type is not None:
            data[param_map["abr_type"]] = abr_type
        if auto_cost_ref_bandwidth is not None:
            data[param_map["auto_cost_ref_bandwidth"]] = auto_cost_ref_bandwidth
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
        if router_id is not None:
            data[param_map["router_id"]] = router_id
        if spf_timers is not None:
            data[param_map["spf_timers"]] = spf_timers
        if bfd is not None:
            data["bfd"] = bfd
        if log_neighbour_changes is not None:
            data[param_map["log_neighbour_changes"]] = log_neighbour_changes
        if restart_mode is not None:
            data[param_map["restart_mode"]] = restart_mode
        if restart_period is not None:
            data[param_map["restart_period"]] = restart_period
        if restart_on_topology_change is not None:
            data[param_map["restart_on_topology_change"]] = restart_on_topology_change
        if area is not None:
            data["area"] = area
        if ospf6_interface is not None:
            data[param_map["ospf6_interface"]] = ospf6_interface
        if summary_address is not None:
            data[param_map["summary_address"]] = summary_address
        if redistribute is not None:
            data["redistribute"] = redistribute
        if passive_interface is not None:
            data[param_map["passive_interface"]] = passive_interface
        data.update(kwargs)
        return self._client.put("cmdb", "router/ospf6", data=data, vdom=vdom)

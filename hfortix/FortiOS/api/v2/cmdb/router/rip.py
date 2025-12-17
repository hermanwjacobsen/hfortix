"""FortiOS CMDB - Router RIP - RIP configuration"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Rip:
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
        return self._client.get("cmdb", "router/rip", params=params if params else None, vdom=vdom)
    def put(self, data_dict: Optional[dict[str, Any]] = None, default_information_originate: Optional[str] = None, default_metric: Optional[int] = None, max_out_metric: Optional[int] = None, recv_buffer_size: Optional[int] = None, distance: Optional[list] = None, distribute_list: Optional[list] = None, neighbor: Optional[list] = None, network: Optional[list] = None, offset_list: Optional[list] = None, passive_interface: Optional[list] = None, redistribute: Optional[list] = None, update_timer: Optional[int] = None, timeout_timer: Optional[int] = None, garbage_timer: Optional[int] = None, version: Optional[str] = None, interface: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"default_information_originate": "default-information-originate", "default_metric": "default-metric", "max_out_metric": "max-out-metric", "recv_buffer_size": "recv-buffer-size", "distribute_list": "distribute-list", "offset_list": "offset-list", "passive_interface": "passive-interface", "update_timer": "update-timer", "timeout_timer": "timeout-timer", "garbage_timer": "garbage-timer"}
        if default_information_originate is not None:
            data[param_map["default_information_originate"]] = default_information_originate
        if default_metric is not None:
            data[param_map["default_metric"]] = default_metric
        if max_out_metric is not None:
            data[param_map["max_out_metric"]] = max_out_metric
        if recv_buffer_size is not None:
            data[param_map["recv_buffer_size"]] = recv_buffer_size
        if distance is not None:
            data["distance"] = distance
        if distribute_list is not None:
            data[param_map["distribute_list"]] = distribute_list
        if neighbor is not None:
            data["neighbor"] = neighbor
        if network is not None:
            data["network"] = network
        if offset_list is not None:
            data[param_map["offset_list"]] = offset_list
        if passive_interface is not None:
            data[param_map["passive_interface"]] = passive_interface
        if redistribute is not None:
            data["redistribute"] = redistribute
        if update_timer is not None:
            data[param_map["update_timer"]] = update_timer
        if timeout_timer is not None:
            data[param_map["timeout_timer"]] = timeout_timer
        if garbage_timer is not None:
            data[param_map["garbage_timer"]] = garbage_timer
        if version is not None:
            data["version"] = version
        if interface is not None:
            data["interface"] = interface
        data.update(kwargs)
        return self._client.put("cmdb", "router/rip", data=data, vdom=vdom)

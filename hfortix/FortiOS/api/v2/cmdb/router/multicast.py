"""FortiOS CMDB - Router Multicast - IPv4 multicast routing configuration"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Multicast:
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
        return self._client.get("cmdb", "router/multicast", params=params if params else None, vdom=vdom)
    def put(self, data_dict: Optional[dict[str, Any]] = None, route_threshold: Optional[int] = None, route_limit: Optional[int] = None, multicast_routing: Optional[str] = None, pim_sm_global: Optional[dict] = None, interface: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"route_threshold": "route-threshold", "route_limit": "route-limit", "multicast_routing": "multicast-routing", "pim_sm_global": "pim-sm-global"}
        if route_threshold is not None:
            data[param_map["route_threshold"]] = route_threshold
        if route_limit is not None:
            data[param_map["route_limit"]] = route_limit
        if multicast_routing is not None:
            data[param_map["multicast_routing"]] = multicast_routing
        if pim_sm_global is not None:
            data[param_map["pim_sm_global"]] = pim_sm_global
        if interface is not None:
            data["interface"] = interface
        data.update(kwargs)
        return self._client.put("cmdb", "router/multicast", data=data, vdom=vdom)

"""FortiOS CMDB - Router Static6 - IPv6 static routes"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
from hfortix.FortiOS.http_client import encode_path_component
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Static6:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client
    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        return self.get(vdom=vdom, **kwargs)
    def get(self, seq_num: Optional[int] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        path = "router/static6"
        if seq_num is not None:
            path = f"{path}/{encode_path_component(str(seq_num))}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)
    def post(self, data_dict: Optional[dict[str, Any]] = None, seq_num: Optional[int] = None, dst: Optional[str] = None, gateway: Optional[str] = None, device: Optional[str] = None, devindex: Optional[int] = None, distance: Optional[int] = None, weight: Optional[int] = None, priority: Optional[int] = None, comment: Optional[str] = None, blackhole: Optional[str] = None, sdwan_zone: Optional[list] = None, virtual_wan_link: Optional[str] = None, link_monitor_exempt: Optional[str] = None, vrf: Optional[int] = None, bfd: Optional[str] = None, status: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"seq_num": "seq-num", "sdwan_zone": "sdwan-zone", "virtual_wan_link": "virtual-wan-link", "link_monitor_exempt": "link-monitor-exempt"}
        if seq_num is not None:
            data[param_map["seq_num"]] = seq_num
        if dst is not None:
            data["dst"] = dst
        if gateway is not None:
            data["gateway"] = gateway
        if device is not None:
            data["device"] = device
        if devindex is not None:
            data["devindex"] = devindex
        if distance is not None:
            data["distance"] = distance
        if weight is not None:
            data["weight"] = weight
        if priority is not None:
            data["priority"] = priority
        if comment is not None:
            data["comment"] = comment
        if blackhole is not None:
            data["blackhole"] = blackhole
        if sdwan_zone is not None:
            data[param_map["sdwan_zone"]] = sdwan_zone
        if virtual_wan_link is not None:
            data[param_map["virtual_wan_link"]] = virtual_wan_link
        if link_monitor_exempt is not None:
            data[param_map["link_monitor_exempt"]] = link_monitor_exempt
        if vrf is not None:
            data["vrf"] = vrf
        if bfd is not None:
            data["bfd"] = bfd
        if status is not None:
            data["status"] = status
        data.update(kwargs)
        return self._client.post("cmdb", "router/static6", data=data, vdom=vdom)
    def put(self, seq_num: int, data_dict: Optional[dict[str, Any]] = None, dst: Optional[str] = None, gateway: Optional[str] = None, device: Optional[str] = None, devindex: Optional[int] = None, distance: Optional[int] = None, weight: Optional[int] = None, priority: Optional[int] = None, comment: Optional[str] = None, blackhole: Optional[str] = None, sdwan_zone: Optional[list] = None, virtual_wan_link: Optional[str] = None, link_monitor_exempt: Optional[str] = None, vrf: Optional[int] = None, bfd: Optional[str] = None, status: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"sdwan_zone": "sdwan-zone", "virtual_wan_link": "virtual-wan-link", "link_monitor_exempt": "link-monitor-exempt"}
        if dst is not None:
            data["dst"] = dst
        if gateway is not None:
            data["gateway"] = gateway
        if device is not None:
            data["device"] = device
        if devindex is not None:
            data["devindex"] = devindex
        if distance is not None:
            data["distance"] = distance
        if weight is not None:
            data["weight"] = weight
        if priority is not None:
            data["priority"] = priority
        if comment is not None:
            data["comment"] = comment
        if blackhole is not None:
            data["blackhole"] = blackhole
        if sdwan_zone is not None:
            data[param_map["sdwan_zone"]] = sdwan_zone
        if virtual_wan_link is not None:
            data[param_map["virtual_wan_link"]] = virtual_wan_link
        if link_monitor_exempt is not None:
            data[param_map["link_monitor_exempt"]] = link_monitor_exempt
        if vrf is not None:
            data["vrf"] = vrf
        if bfd is not None:
            data["bfd"] = bfd
        if status is not None:
            data["status"] = status
        data.update(kwargs)
        path = f"router/static6/{encode_path_component(str(seq_num))}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
    def delete(self, seq_num: int, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        path = f"router/static6/{encode_path_component(str(seq_num))}"
        return self._client.delete("cmdb", path, vdom=vdom)
    def exists(self, seq_num: int, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(seq_num=seq_num, vdom=vdom)
            return True
        except Exception:
            return False

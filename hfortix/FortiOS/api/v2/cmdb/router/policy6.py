"""FortiOS CMDB - Router Policy6 - IPv6 routing policies"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
from hfortix.FortiOS.http_client import encode_path_component
if TYPE_CHECKING:
    from ....http_client import HTTPClient

class Policy6:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client
    def get(self, seq_num: Optional[int] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        path = "router/policy6"
        if seq_num is not None:
            path = f"{path}/{encode_path_component(str(seq_num))}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)
    def post(self, data_dict: Optional[dict[str, Any]] = None, seq_num: Optional[int] = None, input_device: Optional[list] = None, input_device_negate: Optional[str] = None, src: Optional[str] = None, srcaddr: Optional[list] = None, dst: Optional[str] = None, dstaddr: Optional[list] = None, action: Optional[str] = None, protocol: Optional[int] = None, start_port: Optional[int] = None, end_port: Optional[int] = None, start_source_port: Optional[int] = None, end_source_port: Optional[int] = None, gateway: Optional[str] = None, output_device: Optional[str] = None, tos: Optional[str] = None, tos_mask: Optional[str] = None, status: Optional[str] = None, comments: Optional[str] = None, internet_service_id: Optional[list] = None, internet_service_custom: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        param_map = {"seq_num": "seq-num", "input_device": "input-device", "input_device_negate": "input-device-negate", "start_port": "start-port", "end_port": "end-port", "start_source_port": "start-source-port", "end_source_port": "end-source-port", "output_device": "output-device", "tos_mask": "tos-mask", "internet_service_id": "internet-service-id", "internet_service_custom": "internet-service-custom"}
        if seq_num is not None:
            data[param_map["seq_num"]] = seq_num
        if input_device is not None:
            data[param_map["input_device"]] = input_device
        if input_device_negate is not None:
            data[param_map["input_device_negate"]] = input_device_negate
        if src is not None:
            data["src"] = src
        if srcaddr is not None:
            data["srcaddr"] = srcaddr
        if dst is not None:
            data["dst"] = dst
        if dstaddr is not None:
            data["dstaddr"] = dstaddr
        if action is not None:
            data["action"] = action
        if protocol is not None:
            data["protocol"] = protocol
        if start_port is not None:
            data[param_map["start_port"]] = start_port
        if end_port is not None:
            data[param_map["end_port"]] = end_port
        if start_source_port is not None:
            data[param_map["start_source_port"]] = start_source_port
        if end_source_port is not None:
            data[param_map["end_source_port"]] = end_source_port
        if gateway is not None:
            data["gateway"] = gateway
        if output_device is not None:
            data[param_map["output_device"]] = output_device
        if tos is not None:
            data["tos"] = tos
        if tos_mask is not None:
            data[param_map["tos_mask"]] = tos_mask
        if status is not None:
            data["status"] = status
        if comments is not None:
            data["comments"] = comments
        if internet_service_id is not None:
            data[param_map["internet_service_id"]] = internet_service_id
        if internet_service_custom is not None:
            data[param_map["internet_service_custom"]] = internet_service_custom
        data.update(kwargs)
        return self._client.post("cmdb", "router/policy6", data=data, vdom=vdom)
    def put(self, seq_num: int, data_dict: Optional[dict[str, Any]] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        path = f"router/policy6/{encode_path_component(str(seq_num))}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
    def delete(self, seq_num: int, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        path = f"router/policy6/{encode_path_component(str(seq_num))}"
        return self._client.delete("cmdb", path, vdom=vdom)
    def exists(self, seq_num: int, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(seq_num=seq_num, vdom=vdom)
            return True
        except Exception:
            return False

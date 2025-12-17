"""
FortiOS CMDB - Router Auth Path

Configure authentication based routing.

API Endpoints:
    GET    /api/v2/cmdb/router/auth-path           - List all / Get specific
    POST   /api/v2/cmdb/router/auth-path           - Create
    PUT    /api/v2/cmdb/router/auth-path/{name}   - Update
    DELETE /api/v2/cmdb/router/auth-path/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AuthPath:
    """Router auth path endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        path = "router/auth-path"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        device: Optional[str] = None,
        gateway: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        if name is not None:
            data["name"] = name
        if device is not None:
            data["device"] = device
        if gateway is not None:
            data["gateway"] = gateway
        data.update(kwargs)
        return self._client.post("cmdb", "router/auth-path", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        device: Optional[str] = None,
        gateway: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        if device is not None:
            data["device"] = device
        if gateway is not None:
            data["gateway"] = gateway
        data.update(kwargs)
        path = f"router/auth-path/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        path = f"router/auth-path/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(name=name, vdom=vdom)
            return True
        except Exception:
            return False

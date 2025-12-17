"""
FortiOS CMDB - Router Community List

Configure community lists.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union
from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient

class CommunityList:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        path = "router/community-list"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def post(self, data_dict: Optional[dict[str, Any]] = None, name: Optional[str] = None, type: Optional[str] = None, rule: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        if name is not None:
            data["name"] = name
        if type is not None:
            data["type"] = type
        if rule is not None:
            data["rule"] = rule
        data.update(kwargs)
        return self._client.post("cmdb", "router/community-list", data=data, vdom=vdom)

    def put(self, name: str, data_dict: Optional[dict[str, Any]] = None, type: Optional[str] = None, rule: Optional[list] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        if type is not None:
            data["type"] = type
        if rule is not None:
            data["rule"] = rule
        data.update(kwargs)
        path = f"router/community-list/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        path = f"router/community-list/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(name=name, vdom=vdom)
            return True
        except Exception:
            return False

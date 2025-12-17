"""FortiOS CMDB - IPS Rule Settings"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class RuleSettings:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self, id: Optional[int] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get IPS rule settings - List all or get specific."""
        path = "ips/rule-settings"
        if id is not None:
            path = f"{path}/{encode_path_component(str(id))}"
        return self._client.get(
            "cmdb",
            path,
            params=kwargs if kwargs else None,
            vdom=vdom,
        )

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        id: Optional[int] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        if id is not None:
            data["id"] = id
        data.update(kwargs)
        return self._client.post("cmdb", "ips/rule-settings", data=data, vdom=vdom)

    def put(
        self,
        id: int,
        data_dict: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        data = data_dict.copy() if data_dict else {}
        data.update(kwargs)
        return self._client.put(
            "cmdb", f"ips/rule-settings/{encode_path_component(str(id))}", data=data, vdom=vdom
        )

    def delete(self, id: int, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        return self._client.delete(
            "cmdb", f"ips/rule-settings/{encode_path_component(str(id))}", vdom=vdom
        )

    def exists(self, id: int, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(id, vdom=vdom)
            return True
        except Exception:
            return False

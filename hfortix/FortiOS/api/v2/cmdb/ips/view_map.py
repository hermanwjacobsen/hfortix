"""FortiOS CMDB - IPS View Map"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class ViewMap:
    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        return self._client.get(
            "cmdb", "ips/view-map", params=kwargs if kwargs else None, vdom=vdom
        )

    def get(
        self, id: int, vdom: Optional[Union[str, bool]] = None, **kwargs: Any
    ) -> dict[str, Any]:
        return self._client.get(
            "cmdb",
            f"ips/view-map/{encode_path_component(str(id))}",
            params=kwargs if kwargs else None,
            vdom=vdom,
        )

    def create(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        id: Optional[int] = None,
        vdom_id: Optional[int] = None,
        policy_id: Optional[int] = None,
        id_policy_id: Optional[int] = None,
        which: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create IPS view map.

        Args:
            id: Map ID
            vdom_id: VDOM ID
            policy_id: Policy ID
            id_policy_id: ID policy ID
            which: Which (before|after)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "id": id,
            "vdom-id": vdom_id,
            "policy-id": policy_id,
            "id-policy-id": id_policy_id,
            "which": which,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)
        return self._client.post("cmdb", "ips/view-map", data=data, vdom=vdom)

    def update(
        self,
        id: int,
        data_dict: Optional[dict[str, Any]] = None,
        vdom_id: Optional[int] = None,
        policy_id: Optional[int] = None,
        id_policy_id: Optional[int] = None,
        which: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update IPS view map.

        Args:
            id: Map ID to update
            vdom_id: VDOM ID
            policy_id: Policy ID
            id_policy_id: ID policy ID
            which: Which (before|after)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "vdom-id": vdom_id,
            "policy-id": policy_id,
            "id-policy-id": id_policy_id,
            "which": which,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)
        return self._client.put(
            "cmdb", f"ips/view-map/{encode_path_component(str(id))}", data=data, vdom=vdom
        )

    def delete(self, id: int, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        return self._client.delete(
            "cmdb", f"ips/view-map/{encode_path_component(str(id))}", vdom=vdom
        )

    def exists(self, id: int, vdom: Optional[Union[str, bool]] = None) -> bool:
        try:
            self.get(id, vdom=vdom)
            return True
        except Exception:
            return False

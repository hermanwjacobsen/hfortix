"""
FortiOS CMDB - Extension Controller FortiGate

Configure FortiGate controller settings for managing connected FortiGates.

API Endpoints:
    GET    /api/v2/cmdb/extension-controller/fortigate           - List all / Get specific
    POST   /api/v2/cmdb/extension-controller/fortigate           - Create
    PUT    /api/v2/cmdb/extension-controller/fortigate/{name}   - Update
    DELETE /api/v2/cmdb/extension-controller/fortigate/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Fortigate:
    """FortiGate controller endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get FortiGate controller(s) - List all or get specific."""
        params = {k: v for k, v in kwargs.items() if v is not None}
        path = "extension-controller/fortigate"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        raw_json: bool = False,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create FortiGate controller."""
        data = {"name": name}
        for key, value in kwargs.items():
            data[key.replace("_", "-")] = value
        return self._client.post(
            "cmdb", "extension-controller/fortigate", data=data, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        raw_json: bool = False,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update a FortiGate controller."""
        data = {}
        for key, value in kwargs.items():
            data[key.replace("_", "-")] = value
        return self._client.put(
            "cmdb",
            f"extension-controller/fortigate/{name}",
            data=data,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        name: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """Delete a FortiGate controller."""
        params = {}
        if scope is not None:
            params["scope"] = scope
        return self._client.delete(
            "cmdb",
            f"extension-controller/fortigate/{name}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

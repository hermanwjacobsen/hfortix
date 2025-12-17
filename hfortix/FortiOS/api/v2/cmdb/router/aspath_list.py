"""
FortiOS CMDB - Router AS Path List

Configure Autonomous System (AS) path lists.

API Endpoints:
    GET    /api/v2/cmdb/router/aspath-list           - List all / Get specific
    POST   /api/v2/cmdb/router/aspath-list           - Create
    PUT    /api/v2/cmdb/router/aspath-list/{name}   - Update
    DELETE /api/v2/cmdb/router/aspath-list/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AspathList:
    """Router AS path list endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get AS path list(s) - List all or get specific."""
        path = "router/aspath-list"
        if name:
            path = f"{path}/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        rule: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create AS path list."""
        data = data_dict.copy() if data_dict else {}
        if name is not None:
            data["name"] = name
        if rule is not None:
            data["rule"] = rule
        data.update(kwargs)
        return self._client.post("cmdb", "router/aspath-list", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        rule: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update AS path list."""
        data = data_dict.copy() if data_dict else {}
        if rule is not None:
            data["rule"] = rule
        data.update(kwargs)
        path = f"router/aspath-list/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """Delete AS path list."""
        path = f"router/aspath-list/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """Check if AS path list exists."""
        try:
            self.get(name=name, vdom=vdom)
            return True
        except Exception:
            return False

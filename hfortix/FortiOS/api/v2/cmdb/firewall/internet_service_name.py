"""FortiOS CMDB - Firewall Internet Service Name

Configure Internet Service name.

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/internet-service-name
    - /api/v2/cmdb/firewall/internet-service-name/{name}

Notes:
    - This is a CLI table endpoint keyed by ``name``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class InternetServiceName:
    """Firewall `internet-service-name` table endpoint."""

    name = "internet-service-name"
    path = "firewall/internet-service-name"

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    # -----------------------------
    # Collection operations
    # -----------------------------
    def post(
        self,
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        nkey: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create one or more Internet Service Name objects."""
        params: dict[str, Any] = {}
        for key, value in {
            "action": action,
            "nkey": nkey,
            "scope": scope,
        }.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)
        return self._client.post(
            "cmdb",
            self.path,
            data=data,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    # -----------------------------
    # Member operations
    # -----------------------------
    def get(
        self,
        name: Optional[Union[str, int]] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get an Internet Service Name entry by name."""
        params: dict[str, Any] = {}
        for key, value in {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        # Determine path based on whether name is provided
        if name is not None:
            name_str = self._client.validate_mkey(name, "name")
            path = f"{self.path}/{encode_path_component(str(name))}"
        else:
            path = self.path

        return self._client.get(
            "cmdb",
            path,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def put(
        self,
        name: Union[str, int],
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update an Internet Service Name entry by name."""
        params: dict[str, Any] = {}
        for key, value in {
            "action": action,
            "before": before,
            "after": after,
            "scope": scope,
        }.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.put(
            "cmdb",
            f"{self.path}/{name_str}",
            data=data,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        name: Union[str, int],
        vdom: Optional[Union[str, bool]] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete an Internet Service Name entry by name."""
        name_str = self._client.validate_mkey(name, "name")
        params: dict[str, Any] = {}
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.delete(
            "cmdb",
            f"{self.path}/{name_str}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

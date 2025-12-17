"""FortiOS CMDB - Firewall Internet Service Extension

Configure Internet Services Extension.

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/internet-service-extension
    - /api/v2/cmdb/firewall/internet-service-extension/{id}

Notes:
    - This is a CLI table endpoint keyed by ``id``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class InternetServiceExtension:
    """Firewall `internet-service-extension` table endpoint."""

    name = "internet-service-extension"
    path = "firewall/internet-service-extension"

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
        """Create one or more Internet Service Extension objects."""
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
        id: Optional[Union[int, str]] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get an Internet Service Extension entry by id."""
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

        # Determine path based on whether id is provided
        if id is not None:
            id_str = self._client.validate_mkey(id, "id")
            path = f"{self.path}/{encode_path_component(str(id))}"
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
        id: Union[int, str],
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update an Internet Service Extension entry by id."""
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
            f"{self.path}/{id_str}",
            data=data,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        id: Union[int, str],
        vdom: Optional[Union[str, bool]] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete an Internet Service Extension entry by id."""
        id_str = self._client.validate_mkey(id, "id")
        params: dict[str, Any] = {}
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.delete(
            "cmdb",
            f"{self.path}/{id_str}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

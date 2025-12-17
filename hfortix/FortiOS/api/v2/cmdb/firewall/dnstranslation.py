"""FortiOS CMDB - Firewall DNS Translation

Configure firewall DNS translation rules.

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/dnstranslation
    - /api/v2/cmdb/firewall/dnstranslation/{id}

Notes:
    - This is a CLI table endpoint keyed by ``id``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Dnstranslation:
    """Firewall `dnstranslation` table endpoint."""

    name = "dnstranslation"
    path = "firewall/dnstranslation"

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    # -----------------------------
    # Collection operations
    # -----------------------------
    def list(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        filter: Optional[list] = None,
        sort: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """List DNS translation objects."""
        params: dict[str, Any] = {}
        for key, value in {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "filter": filter,
            "sort": sort,
            "action": action,
        }.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)
        return self._client.get(
            "cmdb", self.path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        nkey: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create one or more DNS translation objects."""
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
        id: Union[int, str],
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get a DNS translation entry by id."""
        id_str = self._client.validate_mkey(id, "id")

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

        return self._client.get(
            "cmdb",
            f"{self.path}/{id_str}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def update(
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
        """Update a DNS translation entry by id."""
        id_str = self._client.validate_mkey(id, "id")

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
        """Delete a DNS translation entry by id."""
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

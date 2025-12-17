"""FortiOS CMDB - Firewall Internet Service FortiGuard

Configure FortiGuard Internet Services (read-only).

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/internet-service-fortiguard
    - /api/v2/cmdb/firewall/internet-service-fortiguard/{id}

Notes:
    - This is a CLI table endpoint keyed by ``id``.
    - Read-only endpoint (no write operations).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class InternetServiceFortiguard:
    """Firewall `internet-service-fortiguard` table endpoint."""

    name = "internet-service-fortiguard"
    path = "firewall/internet-service-fortiguard"

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    # -----------------------------
    # Collection operations
    # -----------------------------
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
        """Get a FortiGuard Internet Service entry by id."""
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

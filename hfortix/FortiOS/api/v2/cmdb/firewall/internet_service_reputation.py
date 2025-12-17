"""FortiOS CMDB - Firewall Internet Service Reputation

Configure Internet Service reputation (read-only).

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/internet-service-reputation
    - /api/v2/cmdb/firewall/internet-service-reputation/{id}

Notes:
    - This is a CLI table endpoint keyed by ``id``.
    - Read-only endpoint (no write operations).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class InternetServiceReputation:
    """Firewall `internet-service-reputation` table endpoint."""

    name = "internet-service-reputation"
    path = "firewall/internet-service-reputation"

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
        id: Optional[Union[int, str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get an Internet Service Reputation entry by id."""
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
            f"{self.path}/{encode_path_component(id)}" if id else self.path,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

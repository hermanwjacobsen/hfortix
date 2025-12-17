"""FortiOS CMDB - Firewall Central SNAT Map

Configure IPv4 and IPv6 central SNAT policies.

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/central-snat-map
    - /api/v2/cmdb/firewall/central-snat-map/{policyid}

Notes:
    - This is a CLI table endpoint keyed by ``policyid``.
    - The FortiOS API uses hyphenated field names; this wrapper keeps payloads
      largely "as-is" and only provides minimal helpers.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class CentralSnatMap:
    """Firewall `central-snat-map` table endpoint."""

    # Fortinet-documented endpoint identifiers
    name = "central-snat-map"
    path = "firewall/central-snat-map"

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    # -----------------------------
    # Collection operations
    # -----------------------------
    def post(
        self,
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create one or more central SNAT policies.

        Args:
            data: FortiOS payload dict (hyphenated keys supported)
            vdom: Virtual domain
            **kwargs: Extra query params (rare; forwarded)
        """
        params = kwargs or None
        return self._client.post(
            "cmdb", self.path, data=data, params=params, vdom=vdom, raw_json=raw_json
        )

    # -----------------------------
    # Member operations
    # -----------------------------
    def get(
        self,
        policyid: Optional[Union[int, str]] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get policyid(s) - list all or get specific by policyid.

        Args:
            policyid: Optional policyid to get specific entry. If None, lists all.
        """
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

        # If policyid provided, get specific; otherwise list all
        if policyid is not None:
            policyid_str = self._client.validate_mkey(policyid, "policyid")
            path = f"{self.path}/{policyid_str}"
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
        policyid: Union[int, str],
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update central SNAT policy."""
        policyid_str = self._client.validate_mkey(policyid, "policyid")

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
            f"{self.path}/{policyid_str}",
            data=data,
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        policyid: Union[int, str],
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete an existing central SNAT policy."""
        policyid_str = self._client.validate_mkey(policyid, "policyid")
        params = kwargs or None
        return self._client.delete(
            "cmdb", f"{self.path}/{policyid_str}", params=params, vdom=vdom, raw_json=raw_json
        )

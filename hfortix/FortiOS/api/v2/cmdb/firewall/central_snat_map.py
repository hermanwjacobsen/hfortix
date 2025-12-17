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
        """List central SNAT policies.

        Args mirror common FortiOS CMDB query parameters.

        Examples:
            >>> fgt.api.cmdb.firewall.central_snat_map.list()
            >>> fgt.api.cmdb.firewall.central_snat_map.list(action='schema')
        """
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
        policyid: Union[int, str],
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get a specific central SNAT policy by policyid."""
        policyid_str = self._client.validate_mkey(policyid, "policyid")

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
            f"{self.path}/{policyid_str}",
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

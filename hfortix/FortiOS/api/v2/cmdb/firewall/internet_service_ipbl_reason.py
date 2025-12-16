"""FortiOS CMDB - Firewall Internet Service IPBL Reason

Configure Internet Service IP Block List reason (read-only).

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/internet-service-ipbl-reason
    - /api/v2/cmdb/firewall/internet-service-ipbl-reason/{id}

Notes:
    - This is a CLI table endpoint keyed by ``id``.
    - Read-only endpoint (no write operations).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class InternetServiceIpblReason:
    """Firewall `internet-service-ipbl-reason` table endpoint."""

    name = 'internet-service-ipbl-reason'
    path = 'firewall/internet-service-ipbl-reason'

    def __init__(self, client: 'HTTPClient') -> None:
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
        **kwargs: Any,
    ) -> dict[str, Any]:
        """List Internet Service IPBL Reason objects."""
        params: dict[str, Any] = {}
        for key, value in {
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'format': format,
            'filter': filter,
            'sort': sort,
            'action': action,
        }.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)
        return self._client.get('cmdb', self.path, params=params if params else None, vdom=vdom)

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
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get an Internet Service IPBL Reason entry by id."""
        id_str = self._client.validate_mkey(id, 'id')

        params: dict[str, Any] = {}
        for key, value in {
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'format': format,
            'action': action,
        }.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        return self._client.get('cmdb', f'{self.path}/{id_str}', params=params if params else None, vdom=vdom)

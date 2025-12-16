"""FortiOS CMDB - Firewall Internet Service Append

Configure additional port mappings for Internet Services.

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/internet-service-append

Notes:
    - This is a singleton-style endpoint (no mkey in the URL).
"""

from __future__ import annotations

from typing import Dict, TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class InternetServiceAppend:
    """Firewall `internet-service-append` singleton endpoint."""

    name = 'internet-service-append'
    path = 'firewall/internet-service-append'

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Internet Service Append settings."""
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
        return self._client.get('cmdb', self.path, params=params if params else None, vdom=vdom)

    def update(
        self,
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update Internet Service Append settings."""
        params: dict[str, Any] = {}
        for key, value in {
            'action': action,
            'before': before,
            'after': after,
            'scope': scope,
        }.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)
        return self._client.put('cmdb', self.path, data=data, params=params if params else None, vdom=vdom)

"""
FortiOS CMDB - Extension Controller Extender VAP

Configure FortiExtender WiFi VAP settings.

API Endpoints:
    GET    /api/v2/cmdb/extension-controller/extender-vap        - List all VAPs
    GET    /api/v2/cmdb/extension-controller/extender-vap/{name} - Get specific VAP
    POST   /api/v2/cmdb/extension-controller/extender-vap        - Create VAP
    PUT    /api/v2/cmdb/extension-controller/extender-vap/{name} - Update VAP
    DELETE /api/v2/cmdb/extension-controller/extender-vap/{name} - Delete VAP
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ExtenderVap:
    """FortiExtender WiFi VAP endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    def get(self, name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get FortiExtender VAP(s)."""
        params = {k: v for k, v in kwargs.items() if v is not None}
        path = 'extension-controller/extender-vap'
        if name:
            path = f'{path}/{name}'
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get all FortiExtender VAPs."""
        return self.get(name=None, vdom=vdom, **kwargs)

    def create(self, name: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Create a new FortiExtender VAP."""
        data = {'name': name}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.post('cmdb', 'extension-controller/extender-vap', data=data, vdom=vdom)

    def update(self, name: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Update a FortiExtender VAP."""
        data = {}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.put('cmdb', f'extension-controller/extender-vap/{name}', data=data, vdom=vdom)

    def delete(self, name: str, scope: Optional[str] = None, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """Delete a FortiExtender VAP."""
        params = {}
        if scope is not None:
            params['scope'] = scope
        return self._client.delete('cmdb', f'extension-controller/extender-vap/{name}', 
                                   params=params if params else None, vdom=vdom)

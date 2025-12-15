"""
FortiOS CMDB - Extension Controller FortiGate Profile

Configure FortiGate connector profile settings and templates.

API Endpoints:
    GET    /api/v2/cmdb/extension-controller/fortigate-profile        - List all FortiGate profiles
    GET    /api/v2/cmdb/extension-controller/fortigate-profile/{name} - Get specific FortiGate profile
    POST   /api/v2/cmdb/extension-controller/fortigate-profile        - Create FortiGate profile
    PUT    /api/v2/cmdb/extension-controller/fortigate-profile/{name} - Update FortiGate profile
    DELETE /api/v2/cmdb/extension-controller/fortigate-profile/{name} - Delete FortiGate profile
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class FortigateProfile:
    """FortiGate connector profile endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    def get(self, name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get FortiGate profile(s)."""
        params = {k: v for k, v in kwargs.items() if v is not None}
        path = 'extension-controller/fortigate-profile'
        if name:
            path = f'{path}/{name}'
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get all FortiGate profiles."""
        return self.get(name=None, vdom=vdom, **kwargs)

    def create(self, name: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Create a new FortiGate profile."""
        data = {'name': name}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.post('cmdb', 'extension-controller/fortigate-profile', data=data, vdom=vdom)

    def update(self, name: str, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Update a FortiGate profile."""
        data = {}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.put('cmdb', f'extension-controller/fortigate-profile/{name}', data=data, vdom=vdom)

    def delete(self, name: str, scope: Optional[str] = None, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """Delete a FortiGate profile."""
        params = {}
        if scope is not None:
            params['scope'] = scope
        return self._client.delete('cmdb', f'extension-controller/fortigate-profile/{name}', 
                                   params=params if params else None, vdom=vdom)

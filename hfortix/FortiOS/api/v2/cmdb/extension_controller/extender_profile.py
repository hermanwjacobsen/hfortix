"""
FortiOS CMDB - Extension Controller Extender Profile

Configure FortiExtender extender profiles.

API Endpoints:
    GET    /api/v2/cmdb/extension-controller/extender-profile        - List all profiles
    GET    /api/v2/cmdb/extension-controller/extender-profile/{name} - Get specific profile
    POST   /api/v2/cmdb/extension-controller/extender-profile        - Create profile
    PUT    /api/v2/cmdb/extension-controller/extender-profile/{name} - Update profile
    DELETE /api/v2/cmdb/extension-controller/extender-profile/{name} - Delete profile
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ExtenderProfile:
    """FortiExtender profile endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    def get(self, name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get FortiExtender profile(s)."""
        params = {k: v for k, v in kwargs.items() if v is not None}
        path = 'extension-controller/extender-profile'
        if name:
            path = f'{path}/{name}'
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get all FortiExtender profiles."""
        return self.get(name=None, vdom=vdom, **kwargs)

    def create(self, data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Create a new FortiExtender profile."""
        data = {'name': name}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.post('cmdb', 'extension-controller/extender-profile', data=data, vdom=vdom)

    def update(self, data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Update a FortiExtender profile."""
        data = {}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.put('cmdb', f'extension-controller/extender-profile/{name}', data=data, vdom=vdom)

    def delete(self, name: str, scope: Optional[str] = None, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """Delete a FortiExtender profile."""
        params = {}
        if scope is not None:
            params['scope'] = scope
        return self._client.delete('cmdb', f'extension-controller/extender-profile/{name}', 
                                   params=params if params else None, vdom=vdom)

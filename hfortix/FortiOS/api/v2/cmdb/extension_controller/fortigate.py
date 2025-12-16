"""
FortiOS CMDB - Extension Controller FortiGate

Configure FortiGate controller settings for managing connected FortiGates.

API Endpoints:
    GET    /api/v2/cmdb/extension-controller/fortigate        - List all FortiGate controllers
    GET    /api/v2/cmdb/extension-controller/fortigate/{name} - Get specific FortiGate controller
    POST   /api/v2/cmdb/extension-controller/fortigate        - Create FortiGate controller
    PUT    /api/v2/cmdb/extension-controller/fortigate/{name} - Update FortiGate controller
    DELETE /api/v2/cmdb/extension-controller/fortigate/{name} - Delete FortiGate controller
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Fortigate:
    """FortiGate controller endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    def get(self, name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get FortiGate controller(s)."""
        params = {k: v for k, v in kwargs.items() if v is not None}
        path = 'extension-controller/fortigate'
        if name:
            path = f'{path}/{name}'
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Get all FortiGate controllers."""
        return self.get(name=None, vdom=vdom, **kwargs)

    def create(self, data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Create a new FortiGate controller."""
        data = {'name': name}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.post('cmdb', 'extension-controller/fortigate', data=data, vdom=vdom)

    def update(self, data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """Update a FortiGate controller."""
        data = {}
        for key, value in kwargs.items():
            data[key.replace('_', '-')] = value
        return self._client.put('cmdb', f'extension-controller/fortigate/{name}', data=data, vdom=vdom)

    def delete(self, name: str, scope: Optional[str] = None, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """Delete a FortiGate controller."""
        params = {}
        if scope is not None:
            params['scope'] = scope
        return self._client.delete('cmdb', f'extension-controller/fortigate/{name}', 
                                   params=params if params else None, vdom=vdom)

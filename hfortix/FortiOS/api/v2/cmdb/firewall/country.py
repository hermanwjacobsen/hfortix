"""FortiOS CMDB - Firewall Country

Define country table.

Swagger paths (FortiOS 7.6.5):
    - /api/v2/cmdb/firewall/country
    - /api/v2/cmdb/firewall/country/{id}

Notes:
    - This is a CLI table endpoint keyed by ``id``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Country:
    """Firewall `country` table endpoint."""

    name = 'country'
    path = 'firewall/country'

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
        """List country objects."""
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

    def create(
        self,
        data: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        # Body parameters
        id: Optional[int] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create one or more country objects.
        
        Supports two usage patterns:
        1. Pass data dict: create(data={"id": 10001, "name": "Custom"}, vdom="root")
        2. Pass kwargs: create(id=10001, name="Custom", vdom="root")
        """
        # Build data from kwargs if not provided
        if data is None:
            data = {}
            if id is not None:
                data['id'] = id
            if name is not None:
                data['name'] = name
            if comment is not None:
                data['comment'] = comment
        
        params = kwargs or None
        return self._client.post('cmdb', self.path, data=data, params=params, vdom=vdom)

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
        """Get a country by id."""
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

    def update(
        self,
        id: Union[int, str],
        data: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        # Body parameters
        name: Optional[str] = None,
        comment: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update a country by id.
        
        Supports two usage patterns:
        1. Pass data dict: update(id=10001, data={"comment": "Updated"}, vdom="root")
        2. Pass kwargs: update(id=10001, comment="Updated", vdom="root")
        """
        id_str = self._client.validate_mkey(id, 'id')

        # Build data from kwargs if not provided
        if data is None:
            data = {}
            if name is not None:
                data['name'] = name
            if comment is not None:
                data['comment'] = comment

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

        return self._client.put('cmdb', f'{self.path}/{id_str}', data=data, params=params if params else None, vdom=vdom)

    def delete(
        self,
        id: Union[int, str],
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete a country by id."""
        id_str = self._client.validate_mkey(id, 'id')
        params = kwargs or None
        return self._client.delete('cmdb', f'{self.path}/{id_str}', params=params, vdom=vdom)

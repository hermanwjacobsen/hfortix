"""
FortiOS CMDB - Application Signatures

Query Fortinet-provided application signatures (application names).

This endpoint is READ-ONLY. It contains application signatures provided by Fortinet
and cannot be modified. For custom user-defined applications, use the
application/custom endpoint instead.

API Endpoints:
    GET    /api/v2/cmdb/application/name       - Get all application signatures
    GET    /api/v2/cmdb/application/name/{name} - Get specific application signature

Note: POST, PUT, and DELETE operations are not supported on this endpoint.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Name:
    """Application signature endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        attr: Optional[str] = None,
        datasource: Optional[bool] = False,
        with_meta: Optional[bool] = False,
        skip: Optional[bool] = False,
        count: Optional[int] = None,
        skip_to_datasource: Optional[str] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get application signature(s)

        Retrieve application signatures with filtering and query options.

        Args:
            name (str, optional): Application name. If provided, get specific signature.
            attr (str, optional): Attribute name that references other table
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable skip operator
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (str, optional): Skip to datasource entry
            acs (bool, optional): If true, return in ascending order
            search (str, optional): Filter by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            format (str, optional): Return specific fields (e.g., 'name|comment')
            action (str, optional): Action type - 'default', 'schema', or 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response with signature data

        Examples:
            >>> # Get all application signatures
            >>> signatures = fgt.cmdb.application.name.list()

            >>> # Get specific signature by name
            >>> app_sig = fgt.cmdb.application.name.get('custom-app')

            >>> # Get with filtering
            >>> filtered = fgt.cmdb.application.name.get(
            ...     format='name|category|sub-category',
            ...     count=20
            ... )
        """
        params = {}
        param_map = {
            'attr': attr,
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'count': count,
            'skip_to_datasource': skip_to_datasource,
            'acs': acs,
            'search': search,
            'scope': scope,
            'format': format,
            'action': action
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        # Build path
        path = 'application/name'
        if name:
            path = f'{path}/{name}'

        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(self, **kwargs: Any) -> dict[str, Any]:
        """
        Get all application signatures (convenience method)

        Args:
            **kwargs: All parameters from get() method

        Returns:
            dict: API response with all signatures

        Examples:
            >>> # Get all signatures
            >>> all_sigs = fgt.cmdb.application.name.list()
        """
        return self.get(**kwargs)

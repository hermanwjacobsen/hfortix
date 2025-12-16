"""
FortiOS CMDB - Application Groups

Configure firewall application groups.

API Endpoints:
    GET    /api/v2/cmdb/application/group       - List all application groups
    GET    /api/v2/cmdb/application/group/{name} - Get a specific application group
    POST   /api/v2/cmdb/application/group       - Create a new application group
    PUT    /api/v2/cmdb/application/group/{name} - Update an application group
    DELETE /api/v2/cmdb/application/group/{name} - Delete an application group
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Group:
    """Application groups endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Group endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        # Query parameters
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get application group(s).

        Retrieves either a specific application group by name, or lists
        all application groups with optional filtering.

        Args:
            name (str, optional): Group name to retrieve. If None, retrieves all groups
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (dict, optional): Skip to provided table's Nth entry
            acs (int, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information for each linked object
            with_meta (bool, optional): Include meta information about each object
            skip (bool, optional): Enable CLI skip operator to hide skipped properties
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing application group data

        Examples:
            >>> # List all application groups
            >>> groups = fgt.cmdb.application.group.list()
            >>> for grp in groups['results']:
            ...     print(grp['name'], grp.get('comment', ''))

            >>> # Get a specific group
            >>> grp = fgt.cmdb.application.group.get('WebApps')
            >>> print(grp['results']['type'])

            >>> # Get with filtering
            >>> groups = fgt.cmdb.application.group.get(
            ...     format='name|comment|type',
            ...     count=10
            ... )
        """
        # Build query parameters
        params = {}
        param_map = {
            'attr': attr,
            'count': count,
            'skip_to_datasource': skip_to_datasource,
            'acs': acs,
            'search': search,
            'scope': scope,
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'format': format,
            'action': action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        # Build path
        path = 'application/group'
        if name:
            path = f'{path}/{name}'

        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(
        self,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        List all application groups.

        Convenience method that calls get() without a specific name.

        Args:
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (dict, optional): Skip to provided table's Nth entry
            acs (int, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information for each linked object
            with_meta (bool, optional): Include meta information about each object
            skip (bool, optional): Enable CLI skip operator to hide skipped properties
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing list of application groups

        Examples:
            >>> # List all groups
            >>> groups = fgt.cmdb.application.group.list()
            >>> print(f"Total groups: {len(groups['results'])}")

            >>> # List with count limit
            >>> groups = fgt.cmdb.application.group.list(count=5)
        """
        return self.get(
            name=None,
            attr=attr,
            count=count,
            skip_to_datasource=skip_to_datasource,
            acs=acs,
            search=search,
            scope=scope,
            datasource=datasource,
            with_meta=with_meta,
            skip=skip,
            format=format,
            action=action,
            vdom=vdom,
            **kwargs
        )

    def create(
        self,
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Group parameters
        comment: Optional[str] = None,
        type: Optional[str] = None,
        application: Optional[list[Union[int, dict[str, Any]]]] = None,
        category: Optional[list[Union[int, dict[str, Any]]]] = None,
        risk: Optional[list[Union[int, dict[str, Any]]]] = None,
        protocols: Optional[str] = None,
        vendor: Optional[list[Union[int, dict[str, Any]]]] = None,
        technology: Optional[list[Union[int, dict[str, Any]]]] = None,
        behavior: Optional[str] = None,
        popularity: Optional[list[Union[int, dict[str, Any]]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new application group.

        Args:
            name (str, required): Application group name (max 63 chars)
            comment (str, optional): Comments (max 255 chars)
            type (str, optional): Application group type - 'application' or 'filter'
            application (list, optional): Application ID list. List of dicts with 'id' key
            category (list, optional): Application category ID list. List of dicts with 'id' key
            risk (list, optional): Risk levels (1-5). List of dicts with 'level' key
            protocols (str, optional): Application protocol filter
            vendor (str, optional): Application vendor filter
            technology (str, optional): Application technology filter
            behavior (str, optional): Application behavior filter
            popularity (str, optional): Popularity filter - '1', '2', '3', '4', or '5'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing creation status

        Examples:
            >>> # Create a group with specific applications
            >>> result = fgt.cmdb.application.group.create(
            ...     name='WebApps',
            ...     comment='Web application group',
            ...     type='application',
            ...     application=[
            ...         {'id': 16072},  # HTTP
            ...         {'id': 16073}   # HTTPS
            ...     ]
            ... )

            >>> # Create a filter-based group
            >>> result = fgt.cmdb.application.group.create(
            ...     name='HighRiskApps',
            ...     comment='High risk applications',
            ...     type='filter',
            ...     risk=[{'level': 4}, {'level': 5}],
            ...     popularity='5'
            ... )

            >>> # Create with category filter
            >>> result = fgt.cmdb.application.group.create(
            ...     name='SocialMedia',
            ...     type='filter',
            ...     category=[{'id': 2}],  # Social.Media category
            ...     comment='Social media applications'
            ... )
        """
        # Build data dictionary
        data = {}
        param_map = {
            'name': name,
            'comment': comment,
            'type': type,
            'application': application,
            'category': category,
            'risk': risk,
            'protocols': protocols,
            'vendor': vendor,
            'technology': technology,
            'behavior': behavior,
            'popularity': popularity,
        }

        # No special field mapping needed - all fields use same name
        for param_name, value in param_map.items():
            if value is not None:
                data[param_name] = value

        data.update(kwargs)

        return self._client.post('cmdb', 'application/group', data, vdom=vdom)

    def update(
        self,
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # Group parameters
        comment: Optional[str] = None,
        type: Optional[str] = None,
        application: Optional[list[Union[int, dict[str, Any]]]] = None,
        category: Optional[list[Union[int, dict[str, Any]]]] = None,
        risk: Optional[list[Union[int, dict[str, Any]]]] = None,
        protocols: Optional[str] = None,
        vendor: Optional[list[Union[int, dict[str, Any]]]] = None,
        technology: Optional[list[Union[int, dict[str, Any]]]] = None,
        behavior: Optional[str] = None,
        popularity: Optional[list[Union[int, dict[str, Any]]]] = None,
        # Action parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an existing application group.

        Args:
            name (str, required): Application group name to update
            comment (str, optional): Comments (max 255 chars)
            type (str, optional): Application group type - 'application' or 'filter'
            application (list, optional): Application ID list. List of dicts with 'id' key
            category (list, optional): Application category ID list. List of dicts with 'id' key
            risk (list, optional): Risk levels (1-5). List of dicts with 'level' key
            protocols (str, optional): Application protocol filter
            vendor (str, optional): Application vendor filter
            technology (str, optional): Application technology filter
            behavior (str, optional): Application behavior filter
            popularity (str, optional): Popularity filter - '1', '2', '3', '4', or '5'
            action (str, optional): Action to perform - 'move'
            before (str, optional): Move before this group (requires action='move')
            after (str, optional): Move after this group (requires action='move')
            scope (str, optional): Scope level - 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing update status

        Examples:
            >>> # Update comment and add applications
            >>> result = fgt.cmdb.application.group.update(
            ...     name='WebApps',
            ...     comment='Updated web applications',
            ...     application=[
            ...         {'id': 16072},
            ...         {'id': 16073},
            ...         {'id': 16074}
            ...     ]
            ... )

            >>> # Update filter criteria
            >>> result = fgt.cmdb.application.group.update(
            ...     name='HighRiskApps',
            ...     risk=[{'level': 5}],  # Only critical
            ...     popularity='4'
            ... )

            >>> # Move group in list
            >>> result = fgt.cmdb.application.group.update(
            ...     name='WebApps',
            ...     action='move',
            ...     after='SocialMedia'
            ... )
        """
        # Build data dictionary
        data = {}
        param_map = {
            'name': name,
            'comment': comment,
            'type': type,
            'application': application,
            'category': category,
            'risk': risk,
            'protocols': protocols,
            'vendor': vendor,
            'technology': technology,
            'behavior': behavior,
            'popularity': popularity,
        }

        # No special field mapping needed
        for param_name, value in param_map.items():
            if value is not None:
                data[param_name] = value

        data.update(kwargs)

        # Build query parameters for action/move
        params = {}
        query_param_map = {
            'action': action,
            'before': before,
            'after': after,
            'scope': scope,
        }

        for key, value in query_param_map.items():
            if value is not None:
                params[key] = value

        return self._client.put(
            'cmdb',
            f'application/group/{name}',
            data,
            params=params if params else None,
            vdom=vdom
        )

    def delete(
        self,
        name: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete an application group.

        Args:
            name (str, required): Application group name to delete
            scope (str, optional): Scope level - 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response containing deletion status

        Examples:
            >>> # Delete a group
            >>> result = fgt.cmdb.application.group.delete('WebApps')
            >>> print(result['status'])

            >>> # Delete with specific scope
            >>> result = fgt.cmdb.application.group.delete(
            ...     name='HighRiskApps',
            ...     scope='vdom'
            ... )
        """
        params = {}
        if scope is not None:
            params['scope'] = scope

        return self._client.delete(
            'cmdb',
            f'application/group/{name}',
            params=params if params else None,
            vdom=vdom
        )

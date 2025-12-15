"""
FortiOS CMDB - Ethernet OAM CFM

Configure Connectivity Fault Management (CFM) domains for Ethernet OAM.

API Endpoints:
    GET    /api/v2/cmdb/ethernet-oam/cfm              - List all CFM domains
    GET    /api/v2/cmdb/ethernet-oam/cfm/{domain-id}  - Get specific CFM domain
    POST   /api/v2/cmdb/ethernet-oam/cfm              - Create CFM domain
    PUT    /api/v2/cmdb/ethernet-oam/cfm/{domain-id}  - Update CFM domain
    DELETE /api/v2/cmdb/ethernet-oam/cfm/{domain-id}  - Delete CFM domain
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Cfm:
    """Connectivity Fault Management (CFM) domain endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Cfm endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        domain_id: Optional[str] = None,
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
        Get CFM domain(s).

        Args:
            domain_id (str, optional): Domain ID to retrieve. If None, retrieves all domains
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (int, optional): Skip to provided table's Nth entry
            acs (bool, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing CFM domain data

        Examples:
            >>> # List all CFM domains
            >>> domains = fgt.cmdb.ethernet_oam.cfm.list()

            >>> # Get a specific CFM domain
            >>> domain = fgt.cmdb.ethernet_oam.cfm.get('domain1')

            >>> # Get with filtering
            >>> domains = fgt.cmdb.ethernet_oam.cfm.get(
            ...     format='domain-id|name|level',
            ...     count=10
            ... )
        """
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

        path = 'ethernet-oam/cfm'
        if domain_id:
            path = f'{path}/{domain_id}'

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
        Get all CFM domains (convenience method).

        Args:
            Same as get() method, excluding domain_id

        Returns:
            dict: API response containing all CFM domains

        Examples:
            >>> domains = fgt.cmdb.ethernet_oam.cfm.list()
        """
        return self.get(
            domain_id=None,
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
        domain_id: str,
        # CFM domain configuration
        name: Optional[str] = None,
        level: Optional[int] = None,
        ma_group: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new CFM domain.

        Args:
            domain_id (str): Domain ID (primary identifier)
            name (str, optional): Domain name
            level (int, optional): Domain level (0-7)
            ma_group (list, optional): List of Maintenance Association (MA) groups
                Each MA group dict can contain:
                - name (str): MA group name
                - maid (str): Maintenance Association Identifier
                - mepid (int): Maintenance Association End Point ID
                - ccm_interval (str): CCM interval - 'disabled'/'3.3ms'/'10ms'/'100ms'/'1s'/'10s'/'1min'/'10min'
                - vlan (int): VLAN ID
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create CFM domain
            >>> result = fgt.cmdb.ethernet_oam.cfm.create(
            ...     domain_id='domain1',
            ...     name='MyDomain',
            ...     level=5
            ... )

            >>> # Create with MA groups
            >>> result = fgt.cmdb.ethernet_oam.cfm.create(
            ...     domain_id='domain2',
            ...     name='Domain2',
            ...     level=3,
            ...     ma_group=[
            ...         {
            ...             'name': 'MA1',
            ...             'maid': 'MA-ID-1',
            ...             'ccm_interval': '1s',
            ...             'vlan': 100
            ...         }
            ...     ]
            ... )
        """
        data = {'domain-id': domain_id}
        
        param_map = {
            'name': name,
            'level': level,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace('_', '-')] = value

        if ma_group is not None:
            # Convert snake_case keys to hyphen-case in MA group dicts
            converted_ma_group = []
            for ma in ma_group:
                converted_ma = {}
                for k, v in ma.items():
                    converted_ma[k.replace('_', '-')] = v
                converted_ma_group.append(converted_ma)
            data['ma-group'] = converted_ma_group

        data.update(kwargs)

        return self._client.post('cmdb', 'ethernet-oam/cfm', data=data, vdom=vdom)

    def update(
        self,
        domain_id: str,
        # CFM domain configuration
        name: Optional[str] = None,
        level: Optional[int] = None,
        ma_group: Optional[list[dict[str, Any]]] = None,
        # Update parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update a CFM domain.

        Args:
            domain_id (str): Domain ID to update
            name (str, optional): Domain name
            level (int, optional): Domain level (0-7)
            ma_group (list, optional): List of Maintenance Association (MA) groups
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            before (str, optional): Place new object before given object
            after (str, optional): Place new object after given object
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update CFM domain
            >>> result = fgt.cmdb.ethernet_oam.cfm.update(
            ...     domain_id='domain1',
            ...     level=6,
            ...     name='UpdatedDomain'
            ... )
        """
        data = {}
        
        param_map = {
            'name': name,
            'level': level,
            'action': action,
            'before': before,
            'after': after,
            'scope': scope,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key.replace('_', '-')] = value

        if ma_group is not None:
            # Convert snake_case keys to hyphen-case in MA group dicts
            converted_ma_group = []
            for ma in ma_group:
                converted_ma = {}
                for k, v in ma.items():
                    converted_ma[k.replace('_', '-')] = v
                converted_ma_group.append(converted_ma)
            data['ma-group'] = converted_ma_group

        data.update(kwargs)

        return self._client.put('cmdb', f'ethernet-oam/cfm/{domain_id}', data=data, vdom=vdom)

    def delete(
        self,
        domain_id: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete a CFM domain.

        Args:
            domain_id (str): Domain ID to delete
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.ethernet_oam.cfm.delete('domain1')
        """
        params = {}
        if scope is not None:
            params['scope'] = scope

        return self._client.delete('cmdb', f'ethernet-oam/cfm/{domain_id}', 
                                   params=params if params else None, vdom=vdom)

"""
FortiOS CMDB - Email Filter DNSBL

Configure AntiSpam DNSBL/ORBL (DNS-based Blacklist/Open Relay Blacklist).

API Endpoints:
    GET    /api/v2/cmdb/emailfilter/dnsbl       - List all DNSBL entries
    GET    /api/v2/cmdb/emailfilter/dnsbl/{id}  - Get specific DNSBL entry
    POST   /api/v2/cmdb/emailfilter/dnsbl       - Create DNSBL entry
    PUT    /api/v2/cmdb/emailfilter/dnsbl/{id}  - Update DNSBL entry
    DELETE /api/v2/cmdb/emailfilter/dnsbl/{id}  - Delete DNSBL entry
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Dnsbl:
    """Email filter DNSBL endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Dnsbl endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        entry_id: Optional[int] = None,
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
        Get email filter DNSBL entry(ies).

        Args:
            entry_id (int, optional): Entry ID to retrieve. If None, retrieves all entries
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
            dict: API response containing DNSBL entry data

        Examples:
            >>> # List all DNSBL entries
            >>> entries = fgt.cmdb.emailfilter.dnsbl.list()

            >>> # Get a specific entry by ID
            >>> entry = fgt.cmdb.emailfilter.dnsbl.get(1)

            >>> # Get with filtering
            >>> entries = fgt.cmdb.emailfilter.dnsbl.get(
            ...     format='id|name|comment',
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

        path = 'emailfilter/dnsbl'
        if entry_id is not None:
            path = f'{path}/{entry_id}'

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
        Get all email filter DNSBL entries (convenience method).

        Args:
            Same as get() method, excluding entry_id

        Returns:
            dict: API response containing all DNSBL entries

        Examples:
            >>> entries = fgt.cmdb.emailfilter.dnsbl.list()
        """
        return self.get(
            entry_id=None,
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
        data_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # DNSBL configuration
        comment: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new email filter DNSBL entry.

        Args:
            name (str): DNSBL entry name
            comment (str, optional): Optional comment
            entries (list, optional): DNSBL server entries with server (domain/IP),
                                     status (enable/disable), action (reject/spam)
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create DNSBL entry
            >>> result = fgt.cmdb.emailfilter.dnsbl.create(
            ...     name='spamhaus',
            ...     comment='Spamhaus DNSBL service',
            ...     entries=[
            ...         {'server': 'zen.spamhaus.org', 'action': 'reject'},
            ...         {'server': 'dbl.spamhaus.org', 'action': 'spam'}
            ...     ]
            ... )
        """
        data = {'name': name}
        
        if comment is not None:
            data['comment'] = comment
        if entries is not None:
            converted_entries = []
            for entry in entries:
                converted = {}
                for key, value in entry.items():
                    converted[key.replace('_', '-')] = value
                converted_entries.append(converted)
            data['entries'] = converted_entries

        data.update(kwargs)

        return self._client.post('cmdb', 'emailfilter/dnsbl', data=data, vdom=vdom)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        entry_id: Optional[int] = None,
        # DNSBL configuration
        name: Optional[str] = None,
        comment: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        # Update parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an email filter DNSBL entry.

        Args:
            entry_id (int): Entry ID to update
            name (str, optional): DNSBL entry name
            comment (str, optional): Optional comment
            entries (list, optional): DNSBL server entries with server, action, status
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            before (str, optional): Place new object before given object ID
            after (str, optional): Place new object after given object ID
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update DNSBL entry
            >>> result = fgt.cmdb.emailfilter.dnsbl.update(
            ...     entry_id=1,
            ...     entries=[
            ...         {'server': 'new.dnsbl.org', 'action': 'reject'}
            ...     ]
            ... )
        """
        data = {}
        
        if name is not None:
            data['name'] = name
        if comment is not None:
            data['comment'] = comment
        if entries is not None:
            converted_entries = []
            for entry in entries:
                converted = {}
                for key, value in entry.items():
                    converted[key.replace('_', '-')] = value
                converted_entries.append(converted)
            data['entries'] = converted_entries
        if action is not None:
            data['action'] = action
        if before is not None:
            data['before'] = before
        if after is not None:
            data['after'] = after
        if scope is not None:
            data['scope'] = scope

        data.update(kwargs)

        return self._client.put('cmdb', f'emailfilter/dnsbl/{entry_id}', data=data, vdom=vdom)

    def delete(
        self,
        entry_id: int,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete an email filter DNSBL entry.

        Args:
            entry_id (int): Entry ID to delete
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.emailfilter.dnsbl.delete(1)
        """
        params = {}
        if scope is not None:
            params['scope'] = scope

        return self._client.delete('cmdb', f'emailfilter/dnsbl/{entry_id}', 
                                   params=params if params else None, vdom=vdom)

"""
FortiOS CMDB - Firewall Address6 Group

Configure IPv6 address groups.

API Endpoints:
    GET    /api/v2/cmdb/firewall/addrgrp6        - List all IPv6 address groups
    GET    /api/v2/cmdb/firewall/addrgrp6/{name} - Get specific IPv6 address group
    POST   /api/v2/cmdb/firewall/addrgrp6        - Create IPv6 address group
    PUT    /api/v2/cmdb/firewall/addrgrp6/{name} - Update IPv6 address group
    DELETE /api/v2/cmdb/firewall/addrgrp6/{name} - Delete IPv6 address group
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Addrgrp6:
    """Firewall IPv6 address group endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Addrgrp6 endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all IPv6 address group objects.

        Args:
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters (filter, format, count, etc.)

        Returns:
            API response dict with list of address group objects

        Examples:
            >>> # List all IPv6 address groups
            >>> result = fgt.cmdb.firewall.addrgrp6.list()
            >>> for grp in result['results']:
            ...     print(f"{grp['name']}: {len(grp.get('member', []))} members")
            
            >>> # List with filters
            >>> result = fgt.cmdb.firewall.addrgrp6.list(
            ...     format=['name', 'member', 'comment']
            ... )
        """
        return self.get(vdom=vdom, **kwargs)

    def get(
        self,
        name: Optional[str] = None,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[dict] = None,
        acs: Optional[int] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get IPv6 address group object(s).

        Args:
            name: Object name (if specified, gets single object)
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned result are in ascending order
            search: Filter objects by search value
            scope: Scope level (global, vdom, or both)
            datasource: Enable to include datasource information
            with_meta: Enable to include meta information
            skip: Enable to call CLI skip operator
            format: List of property names to include in results
            action: Special action (datasource, stats, schema, etc.)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # List all IPv6 address groups
            >>> result = fgt.cmdb.firewall.addrgrp6.get()
            
            >>> # Get specific IPv6 address group
            >>> result = fgt.cmdb.firewall.addrgrp6.get('ipv6-internal-networks')
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.addrgrp6.get('ipv6-internal-networks', with_meta=True)
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
        
        path = 'firewall/addrgrp6'
        if name:
            path = f'{path}/{name}'
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def create(
        self,
        name: str,
        member: list[str] | list[dict[str, str]],
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        exclude: Optional[str] = None,
        exclude_member: Optional[list[dict[str, str]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create IPv6 address group object.

        Args:
            name: Address group name (required)
            member: List of address names (strings) or dicts [{'name': 'addr1'}] (required)
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            exclude: Enable/disable exclude members ('enable'|'disable')
            exclude_member: List of address dicts to exclude [{'name': 'addr1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Create IPv6 address group with string list (simplified API)
            >>> result = fgt.cmdb.firewall.addrgrp6.create(
            ...     name='ipv6-internal-networks',
            ...     member=['ipv6-subnet1', 'ipv6-subnet2'],
            ...     comment='All internal IPv6 networks'
            ... )
            
            >>> # Create IPv6 address group with dict list (explicit format)
            >>> result = fgt.cmdb.firewall.addrgrp6.create(
            ...     name='ipv6-web-servers',
            ...     member=[{'name': 'ipv6-web1'}, {'name': 'ipv6-web2'}],
            ...     comment='IPv6 web server group'
            ... )
            
            >>> # Create group with excluded members
            >>> result = fgt.cmdb.firewall.addrgrp6.create(
            ...     name='ipv6-trusted-nets',
            ...     member=['ipv6-all-internal'],
            ...     exclude='enable',
            ...     exclude_member=[{'name': 'ipv6-quarantine'}]
            ... )
        """
        # Convert member list if needed (simplified API)
        if member and isinstance(member, list) and len(member) > 0:
            if isinstance(member[0], str):
                member = [{'name': m} for m in member]
        
        data = {'name': name, 'member': member}
        
        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            'comment': 'comment',
            'visibility': 'visibility',
            'color': 'color',
            'tags': 'tags',
            'exclude': 'exclude',
            'exclude_member': 'exclude-member',
        }
        
        param_map = {
            'comment': comment,
            'visibility': visibility,
            'color': color,
            'tags': tags,
            'exclude': exclude,
            'exclude_member': exclude_member,
        }
        
        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                data[api_key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = 'firewall/addrgrp6'
        return self._client.post('cmdb', path, data=data, vdom=vdom)

    def update(
        self,
        name: str,
        member: Optional[list[str] | list[dict[str, str]]] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        exclude: Optional[str] = None,
        exclude_member: Optional[list[dict[str, str]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update IPv6 address group object.

        Args:
            name: Address group name (required)
            member: List of address names (strings) or dicts [{'name': 'addr1'}]
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            exclude: Enable/disable exclude members ('enable'|'disable')
            exclude_member: List of address dicts to exclude [{'name': 'addr1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Update members with simplified API
            >>> result = fgt.cmdb.firewall.addrgrp6.update(
            ...     name='ipv6-internal-networks',
            ...     member=['ipv6-subnet1', 'ipv6-subnet2', 'ipv6-subnet3'],
            ...     comment='Updated IPv6 internal networks'
            ... )
        """
        data = {}
        
        # Convert member list if needed (simplified API)
        if member is not None:
            if isinstance(member, list) and len(member) > 0:
                if isinstance(member[0], str):
                    member = [{'name': m} for m in member]
            data['member'] = member
        
        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            'comment': 'comment',
            'visibility': 'visibility',
            'color': 'color',
            'tags': 'tags',
            'exclude': 'exclude',
            'exclude_member': 'exclude-member',
        }
        
        param_map = {
            'comment': comment,
            'visibility': visibility,
            'color': color,
            'tags': tags,
            'exclude': exclude,
            'exclude_member': exclude_member,
        }
        
        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                data[api_key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = f'firewall/addrgrp6/{name}'
        return self._client.put('cmdb', path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete IPv6 address group object.

        Args:
            name: Address group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete IPv6 address group
            >>> result = fgt.cmdb.firewall.addrgrp6.delete('test-group6')
        """
        path = f'firewall/addrgrp6/{name}'
        return self._client.delete('cmdb', path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if IPv6 address group object exists.

        Args:
            name: Address group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if IPv6 address group exists
            >>> if fgt.cmdb.firewall.addrgrp6.exists('ipv6-internal-networks'):
            ...     print("IPv6 address group exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False

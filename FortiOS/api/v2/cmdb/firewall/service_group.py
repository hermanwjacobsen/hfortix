"""
FortiOS CMDB - Firewall Service Group

Configure service groups.

API Endpoints:
    GET    /api/v2/cmdb/firewall.service/group        - List all service groups
    GET    /api/v2/cmdb/firewall.service/group/{name} - Get specific service group
    POST   /api/v2/cmdb/firewall.service/group        - Create new service group
    PUT    /api/v2/cmdb/firewall.service/group/{name} - Update service group
    DELETE /api/v2/cmdb/firewall.service/group/{name} - Delete service group
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ServiceGroup:
    """Firewall service group endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize ServiceGroup endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(
        self,
        filter: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
        with_meta: Optional[bool] = None,
        datasource: Optional[bool] = None,
        format: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        List all service groups.

        Args:
            filter: Filter results
            start: Starting entry index
            count: Maximum number of entries to return
            with_meta: Include metadata
            datasource: Include datasource information
            format: List of fields to return
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # List all service groups
            >>> result = fgt.cmdb.firewall.service.group.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.service.group.list(
            ...     format=['name', 'member']
            ... )
        """
        return self.get(
            name=None,
            filter=filter,
            start=start,
            count=count,
            with_meta=with_meta,
            datasource=datasource,
            format=format,
            vdom=vdom,
            **kwargs
        )

    def get(
        self,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
        with_meta: Optional[bool] = None,
        datasource: Optional[bool] = None,
        format: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get service group configuration.

        Args:
            name: Group name (if None, returns all)
            filter: Filter results
            start: Starting entry index
            count: Maximum number of entries to return
            with_meta: Include metadata
            datasource: Include datasource information
            format: List of fields to return
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Get all service groups
            >>> result = fgt.cmdb.firewall.service.group.get()
            
            >>> # Get specific group
            >>> result = fgt.cmdb.firewall.service.group.get('Web-Services')
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.service.group.get(
            ...     'Web-Services',
            ...     with_meta=True
            ... )
        """
        params = {}
        param_map = {
            'filter': filter,
            'start': start,
            'count': count,
            'with_meta': with_meta,
            'datasource': datasource,
            'format': format,
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        params.update(kwargs)
        
        path = 'firewall.service/group'
        if name:
            path = f'{path}/{name}'
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def create(
        self,
        name: str,
        member: Optional[list] = None,
        comment: Optional[str] = None,
        color: Optional[int] = None,
        proxy: Optional[str] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new service group.

        Args:
            name: Group name (required)
            member: List of member services (list of dicts with 'name' key)
            comment: Comment text (max 255 chars)
            color: Color value (0-32)
            proxy: Enable/disable web proxy service group - 'enable' or 'disable'
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Create service group with members
            >>> result = fgt.cmdb.firewall.service.group.create(
            ...     name='Web-Services',
            ...     member=[
            ...         {'name': 'HTTP'},
            ...         {'name': 'HTTPS'}
            ...     ],
            ...     comment='Standard web services'
            ... )
            
            >>> # Create with color
            >>> result = fgt.cmdb.firewall.service.group.create(
            ...     name='Custom-Services',
            ...     member=[
            ...         {'name': 'HTTPS-8443'},
            ...         {'name': 'Custom-DNS'}
            ...     ],
            ...     color=10
            ... )
        """
        data = {}
        param_map = {
            'name': name,
            'member': member,
            'comment': comment,
            'color': color,
            'proxy': proxy,
            'fabric_object': fabric_object,
        }
        
        api_field_map = {
            'name': 'name',
            'member': 'member',
            'comment': 'comment',
            'color': 'color',
            'proxy': 'proxy',
            'fabric_object': 'fabric-object',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.service/group', data, vdom=vdom)

    def update(
        self,
        name: str,
        member: Optional[list] = None,
        comment: Optional[str] = None,
        color: Optional[int] = None,
        proxy: Optional[str] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an existing service group.

        Args:
            name: Group name (required)
            member: List of member services (list of dicts with 'name' key)
            comment: Comment text (max 255 chars)
            color: Color value (0-32)
            proxy: Enable/disable web proxy service group - 'enable' or 'disable'
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Update members
            >>> result = fgt.cmdb.firewall.service.group.update(
            ...     name='Web-Services',
            ...     member=[
            ...         {'name': 'HTTP'},
            ...         {'name': 'HTTPS'},
            ...         {'name': 'HTTPS-8443'}
            ...     ]
            ... )
            
            >>> # Update color
            >>> result = fgt.cmdb.firewall.service.group.update(
            ...     name='Web-Services',
            ...     color=15
            ... )
        """
        data = {}
        param_map = {
            'member': member,
            'comment': comment,
            'color': color,
            'proxy': proxy,
            'fabric_object': fabric_object,
        }
        
        api_field_map = {
            'member': 'member',
            'comment': 'comment',
            'color': 'color',
            'proxy': 'proxy',
            'fabric_object': 'fabric-object',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.put('cmdb', f'firewall.service/group/{name}', data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete a service group.

        Args:
            name: Group name
            vdom: Virtual domain

        Returns:
            API response dictionary

        Examples:
            >>> # Delete service group
            >>> result = fgt.cmdb.firewall.service.group.delete('Web-Services')
        """
        return self._client.delete('cmdb', f'firewall.service/group/{name}', vdom=vdom)

    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if a service group exists.

        Args:
            name: Group name
            vdom: Virtual domain

        Returns:
            True if group exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.service.group.exists('Web-Services'):
            ...     print("Service group exists")
        """
        try:
            result = self.get(name, vdom=vdom)
            return (
                result.get('status') == 'success' and
                result.get('http_status') == 200 and
                len(result.get('results', [])) > 0
            )
        except Exception:
            return False

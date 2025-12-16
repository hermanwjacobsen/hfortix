"""
FortiOS CMDB - Firewall Schedule Group

Schedule group configuration.

API Endpoints:
    GET    /api/v2/cmdb/firewall.schedule/group        - List all schedule groups
    GET    /api/v2/cmdb/firewall.schedule/group/{name} - Get specific schedule group
    POST   /api/v2/cmdb/firewall.schedule/group        - Create new schedule group
    PUT    /api/v2/cmdb/firewall.schedule/group/{name} - Update schedule group
    DELETE /api/v2/cmdb/firewall.schedule/group/{name} - Delete schedule group
"""

from __future__ import annotations

from typing import Dict, TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ScheduleGroup:
    """Firewall schedule group endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize ScheduleGroup endpoint

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
        List all schedule groups.

        Args:
            filter: Filter results
            start: Starting entry index
            count: Maximum number of entries to return
            with_meta: Include metadata
            datasource: Include datasource information
            format: List of property names to include
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # List all schedule groups
            >>> result = fgt.cmdb.firewall.schedule.group.list()
            >>> for group in result['results']:
            ...     print(f"{group['name']}: {len(group.get('member', []))} members")
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.schedule.group.list(format=['name', 'member'])
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
        
        path = 'firewall.schedule/group'
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def get(
        self,
        name: str,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get a specific schedule group by name.

        Args:
            name: Schedule group name
            datasource: Include datasource information
            with_meta: Include metadata
            action: Special actions (default, schema)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # Get schedule group
            >>> result = fgt.cmdb.firewall.schedule.group.get('workweek')
            >>> print(f"Members: {result['results']['member']}")
        """
        params = {}
        param_map = {
            'datasource': datasource,
            'with_meta': with_meta,
            'action': action,
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        params.update(kwargs)
        
        path = f'firewall.schedule/group/{name}'
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    def create(
        self,
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        member: Optional[list[dict[str, str]]] = None,
        color: Optional[int] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new schedule group.

        
        Supports two usage patterns:
        1. Pass data dict: create(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Schedule group name
            member: List of schedule objects, each dict with 'name' key
            color: Color (0-32, default=0)
            fabric_object: Security Fabric global object setting ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Create schedule group with members
            >>> result = fgt.cmdb.firewall.schedule.group.create(
            ...     name='business-hours',
            ...     member=[
            ...         {'name': 'weekday-daytime'},
            ...         {'name': 'weekend-morning'}
            ...     ]
            ... )
            
            >>> # Create with color
            >>> result = fgt.cmdb.firewall.schedule.group.create(
            ...     name='maintenance-windows',
            ...     member=[{'name': 'saturday-night'}],
            ...     color=5
            ... )
        """
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if name is not None:
                data['name'] = name
            if member is not None:
                # Convert string list to dict list if needed
                if isinstance(member, list) and len(member) > 0:
                    if isinstance(member[0], str):
                        member = [{'name': m} for m in member]
                data['member'] = member
            if color is not None:
                data['color'] = color
            if fabric_object is not None:
                data['fabric-object'] = fabric_object

        data = {'name': name}
        
        param_map = {
            'member': member,
            'color': color,
            'fabric-object': fabric_object,
        }
        
        for key, value in param_map.items():
            if value is not None:
                data[key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = 'firewall.schedule/group'
        return self._client.post('cmdb', path, data=data, vdom=vdom)
    def update(
        self,
        name: str,
        data: Optional[Dict[str, Any]] = None,
        member: Optional[list[dict[str, str]]] = None,
        color: Optional[int] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an existing schedule group.

        
        Supports two usage patterns:
        1. Pass data dict: update(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Schedule group name
            member: List of schedule objects, each dict with 'name' key
            color: Color (0-32, default=0)
            fabric_object: Security Fabric global object setting ('enable' or 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Update members
            >>> result = fgt.cmdb.firewall.schedule.group.update(
            ...     name='business-hours',
            ...     member=[
            ...         {'name': 'weekday-daytime'},
            ...         {'name': 'saturday-morning'}
            ...     ]
            ... )
            
            >>> # Change color
            >>> result = fgt.cmdb.firewall.schedule.group.update(
            ...     name='maintenance-windows',
            ...     color=10
            ... )
        """
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if member is not None:
                # Convert string list to dict list if needed
                if isinstance(member, list) and len(member) > 0:
                    if isinstance(member[0], str):
                        member = [{'name': m} for m in member]
                data['member'] = member
            if color is not None:
                data['color'] = color
            if fabric_object is not None:
                data['fabric-object'] = fabric_object

        data = {}
        
        param_map = {
            'member': member,
            'color': color,
            'fabric-object': fabric_object,
        }
        
        for key, value in param_map.items():
            if value is not None:
                data[key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = f'firewall.schedule/group/{name}'
        return self._client.put('cmdb', path, data=data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete a schedule group.

        Args:
            name: Schedule group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete schedule group
            >>> result = fgt.cmdb.firewall.schedule.group.delete('old-schedule')
        """
        path = f'firewall.schedule/group/{name}'
        return self._client.delete('cmdb', path, vdom=vdom)

    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if a schedule group exists.

        Args:
            name: Schedule group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if group exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.schedule.group.exists('workweek'):
            ...     print("Schedule group exists")
        """
        try:
            result = self.get(name, vdom=vdom)
            return result.get('status') == 'success'
        except Exception:
            return False

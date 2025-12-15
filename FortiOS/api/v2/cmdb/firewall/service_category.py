"""
FortiOS CMDB - Firewall Service Category

Configure service categories.

API Endpoints:
    GET    /api/v2/cmdb/firewall.service/category        - List all service categories
    GET    /api/v2/cmdb/firewall.service/category/{name} - Get specific service category
    POST   /api/v2/cmdb/firewall.service/category        - Create new service category
    PUT    /api/v2/cmdb/firewall.service/category/{name} - Update service category
    DELETE /api/v2/cmdb/firewall.service/category/{name} - Delete service category
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ServiceCategory:
    """Firewall service category endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize ServiceCategory endpoint

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
        List all service categories.

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
            >>> # List all service categories
            >>> result = fgt.cmdb.firewall.service.category.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.service.category.list(
            ...     format=['name', 'comment']
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
        Get service category configuration.

        Args:
            name: Category name (if None, returns all)
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
            >>> # Get all categories
            >>> result = fgt.cmdb.firewall.service.category.get()
            
            >>> # Get specific category
            >>> result = fgt.cmdb.firewall.service.category.get('General')
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.service.category.get(
            ...     'Web Access',
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
        
        path = 'firewall.service/category'
        if name:
            path = f'{path}/{name}'
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def create(
        self,
        name: str,
        comment: Optional[str] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new service category.

        Args:
            name: Category name (required)
            comment: Comment text (max 255 chars)
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Create basic category
            >>> result = fgt.cmdb.firewall.service.category.create(
            ...     name='Custom-Apps',
            ...     comment='Custom application services'
            ... )
            
            >>> # Create with fabric object
            >>> result = fgt.cmdb.firewall.service.category.create(
            ...     name='Enterprise-Apps',
            ...     comment='Enterprise applications',
            ...     fabric_object='enable'
            ... )
        """
        data = {}
        param_map = {
            'name': name,
            'comment': comment,
            'fabric_object': fabric_object,
        }
        
        api_field_map = {
            'name': 'name',
            'comment': 'comment',
            'fabric_object': 'fabric-object',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.service/category', data, vdom=vdom)

    def update(
        self,
        name: str,
        comment: Optional[str] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an existing service category.

        Args:
            name: Category name (required)
            comment: Comment text (max 255 chars)
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Update comment
            >>> result = fgt.cmdb.firewall.service.category.update(
            ...     name='Custom-Apps',
            ...     comment='Updated description'
            ... )
            
            >>> # Enable fabric object
            >>> result = fgt.cmdb.firewall.service.category.update(
            ...     name='Custom-Apps',
            ...     fabric_object='enable'
            ... )
        """
        data = {}
        param_map = {
            'comment': comment,
            'fabric_object': fabric_object,
        }
        
        api_field_map = {
            'comment': 'comment',
            'fabric_object': 'fabric-object',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.put('cmdb', f'firewall.service/category/{name}', data, vdom=vdom)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete a service category.

        Args:
            name: Category name
            vdom: Virtual domain

        Returns:
            API response dictionary

        Examples:
            >>> # Delete category
            >>> result = fgt.cmdb.firewall.service.category.delete('Custom-Apps')
        """
        return self._client.delete('cmdb', f'firewall.service/category/{name}', vdom=vdom)

    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if a service category exists.

        Args:
            name: Category name
            vdom: Virtual domain

        Returns:
            True if category exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.service.category.exists('General'):
            ...     print("Category exists")
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

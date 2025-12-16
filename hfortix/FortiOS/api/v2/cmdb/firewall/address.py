"""
FortiOS CMDB - Firewall Address

Configure IPv4 addresses.

API Endpoints:
    GET    /api/v2/cmdb/firewall/address        - List all IPv4 addresses
    GET    /api/v2/cmdb/firewall/address/{name} - Get specific IPv4 address
    POST   /api/v2/cmdb/firewall/address        - Create IPv4 address
    PUT    /api/v2/cmdb/firewall/address/{name} - Update IPv4 address
    DELETE /api/v2/cmdb/firewall/address/{name} - Delete IPv4 address
"""

from __future__ import annotations

from typing import Dict, TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Address:
    """Firewall IPv4 address endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Address endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all IPv4 address objects.

        Args:
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters (filter, format, count, etc.)

        Returns:
            API response dict with list of address objects

        Examples:
            >>> # List all addresses
            >>> result = fgt.cmdb.firewall.address.list()
            >>> for addr in result['results']:
            ...     print(f"{addr['name']}: {addr.get('subnet', 'N/A')}")
            
            >>> # List with filters
            >>> result = fgt.cmdb.firewall.address.list(
            ...     filter='type==ipmask',
            ...     format=['name', 'subnet', 'comment']
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
        Get IPv4 address object(s).

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
            >>> # List all addresses
            >>> result = fgt.cmdb.firewall.address.get()
            
            >>> # Get specific address
            >>> result = fgt.cmdb.firewall.address.get('web-server')
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.address.get('web-server', with_meta=True)
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
        
        path = 'firewall/address'
        if name:
            path = f'{path}/{name}'
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    def create(
        self,
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        subnet: Optional[str] = None,
        start_ip: Optional[str] = None,
        end_ip: Optional[str] = None,
        fqdn: Optional[str] = None,
        country: Optional[str] = None,
        comment: Optional[str] = None,
        associated_interface: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        allow_routing: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create IPv4 address object.

        
        Supports two usage patterns:
        1. Pass data dict: create(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Address name (required)
            type: Address type: 'ipmask', 'iprange', 'fqdn', 'geography', 'wildcard', 'dynamic', etc. (default: 'ipmask')
            subnet: IP address and subnet mask (for type=ipmask, e.g., '10.0.0.0/8')
            start_ip: Start IP address (for type=iprange)
            end_ip: End IP address (for type=iprange)
            fqdn: Fully qualified domain name (for type=fqdn)
            country: Country code (for type=geography)
            comment: Description/comment
            associated_interface: Interface name to bind to
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            allow_routing: Enable/disable routing ('enable'|'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Create subnet address
            >>> result = fgt.cmdb.firewall.address.create(
            ...     name='internal-net',
            ...     type='ipmask',
            ...     subnet='192.168.1.0/24',
            ...     comment='Internal network'
            ... )
            
            >>> # Create IP range
            >>> result = fgt.cmdb.firewall.address.create(
            ...     name='dhcp-range',
            ...     type='iprange',
            ...     start_ip='192.168.1.100',
            ...     end_ip='192.168.1.200'
            ... )
            
            >>> # Create FQDN
            >>> result = fgt.cmdb.firewall.address.create(
            ...     name='google-dns',
            ...     type='fqdn',
            ...     fqdn='dns.google.com'
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
            if type is not None:
                data['type'] = type
            if subnet is not None:
                data['subnet'] = subnet
            if start_ip is not None:
                data['start-ip'] = start_ip
            if end_ip is not None:
                data['end-ip'] = end_ip
            if fqdn is not None:
                data['fqdn'] = fqdn
            if country is not None:
                data['country'] = country
            if comment is not None:
                data['comment'] = comment
            if associated_interface is not None:
                data['associated-interface'] = associated_interface
            if visibility is not None:
                data['visibility'] = visibility
            if color is not None:
                data['color'] = color
            if tags is not None:
                data['tags'] = tags
            if allow_routing is not None:
                data['allow-routing'] = allow_routing

        data = {'name': name, 'type': type}
        
        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            'subnet': 'subnet',
            'start_ip': 'start-ip',
            'end_ip': 'end-ip',
            'fqdn': 'fqdn',
            'country': 'country',
            'comment': 'comment',
            'associated_interface': 'associated-interface',
            'visibility': 'visibility',
            'color': 'color',
            'tags': 'tags',
            'allow_routing': 'allow-routing',
        }
        
        param_map = {
            'subnet': subnet,
            'start_ip': start_ip,
            'end_ip': end_ip,
            'fqdn': fqdn,
            'country': country,
            'comment': comment,
            'associated_interface': associated_interface,
            'visibility': visibility,
            'color': color,
            'tags': tags,
            'allow_routing': allow_routing,
        }
        
        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                data[api_key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = 'firewall/address'
        return self._client.post('cmdb', path, data=data, vdom=vdom)
    def update(
        self,
        name: str,
        data: Optional[Dict[str, Any]] = None,
        subnet: Optional[str] = None,
        start_ip: Optional[str] = None,
        end_ip: Optional[str] = None,
        fqdn: Optional[str] = None,
        country: Optional[str] = None,
        comment: Optional[str] = None,
        associated_interface: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        allow_routing: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update IPv4 address object.

        
        Supports two usage patterns:
        1. Pass data dict: update(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Address name (required)
            subnet: IP address and subnet mask (for type=ipmask)
            start_ip: Start IP address (for type=iprange)
            end_ip: End IP address (for type=iprange)
            fqdn: Fully qualified domain name (for type=fqdn)
            country: Country code (for type=geography)
            comment: Description/comment
            associated_interface: Interface name to bind to
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            allow_routing: Enable/disable routing ('enable'|'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Update subnet
            >>> result = fgt.cmdb.firewall.address.update(
            ...     name='internal-net',
            ...     subnet='192.168.2.0/24',
            ...     comment='Updated internal network'
            ... )
        """
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if subnet is not None:
                data['subnet'] = subnet
            if start_ip is not None:
                data['start-ip'] = start_ip
            if end_ip is not None:
                data['end-ip'] = end_ip
            if fqdn is not None:
                data['fqdn'] = fqdn
            if country is not None:
                data['country'] = country
            if comment is not None:
                data['comment'] = comment
            if associated_interface is not None:
                data['associated-interface'] = associated_interface
            if visibility is not None:
                data['visibility'] = visibility
            if color is not None:
                data['color'] = color
            if tags is not None:
                data['tags'] = tags
            if allow_routing is not None:
                data['allow-routing'] = allow_routing

        data = {}
        
        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            'subnet': 'subnet',
            'start_ip': 'start-ip',
            'end_ip': 'end-ip',
            'fqdn': 'fqdn',
            'country': 'country',
            'comment': 'comment',
            'associated_interface': 'associated-interface',
            'visibility': 'visibility',
            'color': 'color',
            'tags': 'tags',
            'allow_routing': 'allow-routing',
        }
        
        param_map = {
            'subnet': subnet,
            'start_ip': start_ip,
            'end_ip': end_ip,
            'fqdn': fqdn,
            'country': country,
            'comment': comment,
            'associated_interface': associated_interface,
            'visibility': visibility,
            'color': color,
            'tags': tags,
            'allow_routing': allow_routing,
        }
        
        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                data[api_key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = f'firewall/address/{name}'
        return self._client.put('cmdb', path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete IPv4 address object.

        Args:
            name: Address name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete address
            >>> result = fgt.cmdb.firewall.address.delete('test-address')
        """
        path = f'firewall/address/{name}'
        return self._client.delete('cmdb', path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if IPv4 address object exists.

        Args:
            name: Address name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if address exists
            >>> if fgt.cmdb.firewall.address.exists('internal-net'):
            ...     print("Address exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False

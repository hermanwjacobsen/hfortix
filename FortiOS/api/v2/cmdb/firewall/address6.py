"""
FortiOS CMDB - Firewall Address6

Configure IPv6 firewall addresses.

API Endpoints:
    GET    /api/v2/cmdb/firewall/address6        - List all IPv6 addresses
    GET    /api/v2/cmdb/firewall/address6/{name} - Get specific IPv6 address
    POST   /api/v2/cmdb/firewall/address6        - Create IPv6 address
    PUT    /api/v2/cmdb/firewall/address6/{name} - Update IPv6 address
    DELETE /api/v2/cmdb/firewall/address6/{name} - Delete IPv6 address
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Address6:
    """Firewall IPv6 address endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Address6 endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all IPv6 address objects.

        Args:
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters (filter, format, count, etc.)

        Returns:
            API response dict with list of address objects

        Examples:
            >>> # List all IPv6 addresses
            >>> result = fgt.cmdb.firewall.address6.list()
            >>> for addr in result['results']:
            ...     print(f"{addr['name']}: {addr.get('ip6', 'N/A')}")
            
            >>> # List with filters
            >>> result = fgt.cmdb.firewall.address6.list(
            ...     filter='type==ipprefix',
            ...     format=['name', 'ip6', 'comment']
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
        Get IPv6 address object(s).

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
            >>> result = fgt.cmdb.firewall.address6.get()
            
            >>> # Get specific address
            >>> result = fgt.cmdb.firewall.address6.get('ipv6-server')
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.address6.get('ipv6-server', with_meta=True)
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
        
        path = 'firewall/address6'
        if name:
            path = f'{path}/{name}'
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def create(
        self,
        name: str,
        type: str = 'ipprefix',
        ip6: Optional[str] = None,
        start_ip: Optional[str] = None,
        end_ip: Optional[str] = None,
        fqdn: Optional[str] = None,
        country: Optional[str] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create IPv6 address object.

        Args:
            name: Address name (required)
            type: Address type: 'ipprefix', 'iprange', 'fqdn', 'geography', 'dynamic', etc. (default: 'ipprefix')
            ip6: IPv6 address and prefix (for type=ipprefix, e.g., '2001:db8::/32')
            start_ip: Start IPv6 address (for type=iprange)
            end_ip: End IPv6 address (for type=iprange)
            fqdn: Fully qualified domain name (for type=fqdn)
            country: Country code (for type=geography)
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Create IPv6 prefix
            >>> result = fgt.cmdb.firewall.address6.create(
            ...     name='ipv6-internal',
            ...     type='ipprefix',
            ...     ip6='2001:db8::/32',
            ...     comment='Internal IPv6 network'
            ... )
            
            >>> # Create IPv6 range
            >>> result = fgt.cmdb.firewall.address6.create(
            ...     name='ipv6-dhcp-range',
            ...     type='iprange',
            ...     start_ip='2001:db8::100',
            ...     end_ip='2001:db8::200'
            ... )
            
            >>> # Create IPv6 FQDN
            >>> result = fgt.cmdb.firewall.address6.create(
            ...     name='google-dns6',
            ...     type='fqdn',
            ...     fqdn='dns.google.com'
            ... )
        """
        data = {'name': name, 'type': type}
        
        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            'ip6': 'ip6',
            'start_ip': 'start-ip',
            'end_ip': 'end-ip',
            'fqdn': 'fqdn',
            'country': 'country',
            'comment': 'comment',
            'visibility': 'visibility',
            'color': 'color',
            'tags': 'tags',
        }
        
        param_map = {
            'ip6': ip6,
            'start_ip': start_ip,
            'end_ip': end_ip,
            'fqdn': fqdn,
            'country': country,
            'comment': comment,
            'visibility': visibility,
            'color': color,
            'tags': tags,
        }
        
        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                data[api_key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = 'firewall/address6'
        return self._client.post('cmdb', path, data=data, vdom=vdom)

    def update(
        self,
        name: str,
        ip6: Optional[str] = None,
        start_ip: Optional[str] = None,
        end_ip: Optional[str] = None,
        fqdn: Optional[str] = None,
        country: Optional[str] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update IPv6 address object.

        Args:
            name: Address name (required)
            ip6: IPv6 address and prefix (for type=ipprefix)
            start_ip: Start IPv6 address (for type=iprange)
            end_ip: End IPv6 address (for type=iprange)
            fqdn: Fully qualified domain name (for type=fqdn)
            country: Country code (for type=geography)
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # Update IPv6 prefix
            >>> result = fgt.cmdb.firewall.address6.update(
            ...     name='ipv6-internal',
            ...     ip6='2001:db8:1::/48',
            ...     comment='Updated IPv6 network'
            ... )
        """
        data = {}
        
        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            'ip6': 'ip6',
            'start_ip': 'start-ip',
            'end_ip': 'end-ip',
            'fqdn': 'fqdn',
            'country': 'country',
            'comment': 'comment',
            'visibility': 'visibility',
            'color': 'color',
            'tags': 'tags',
        }
        
        param_map = {
            'ip6': ip6,
            'start_ip': start_ip,
            'end_ip': end_ip,
            'fqdn': fqdn,
            'country': country,
            'comment': comment,
            'visibility': visibility,
            'color': color,
            'tags': tags,
        }
        
        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                data[api_key] = value
        
        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                data[key] = value
        
        path = f'firewall/address6/{name}'
        return self._client.put('cmdb', path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete IPv6 address object.

        Args:
            name: Address name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete address
            >>> result = fgt.cmdb.firewall.address6.delete('test-address6')
        """
        path = f'firewall/address6/{name}'
        return self._client.delete('cmdb', path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if IPv6 address object exists.

        Args:
            name: Address name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if address exists
            >>> if fgt.cmdb.firewall.address6.exists('ipv6-internal'):
            ...     print("Address exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False

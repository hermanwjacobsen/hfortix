"""
FortiOS CMDB - Firewall SSH Local CA
SSH proxy local CA.

API Endpoints:
    GET    /api/v2/cmdb/firewall.ssh/local-ca       - List all local CAs
    GET    /api/v2/cmdb/firewall.ssh/local-ca/{id}  - Get specific local CA
    POST   /api/v2/cmdb/firewall.ssh/local-ca       - Create local CA
    PUT    /api/v2/cmdb/firewall.ssh/local-ca/{id}  - Update local CA
    DELETE /api/v2/cmdb/firewall.ssh/local-ca/{id}  - Delete local CA
"""

from typing import Dict, Optional, Union, List, Any

from .....http_client import HTTPResponse


class LocalCa:
    """SSH proxy local CA endpoint"""
    
    def __init__(self, client):
        self._client = client
    
    def list(
        self,
        filter: Optional[str] = None,
        range: Optional[str] = None,
        sort: Optional[str] = None,
        format: Optional[List[str]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        List all SSH local CAs.
        
        Args:
            filter: Filter results
            range: Range of results (e.g., '0-50')
            sort: Sort results
            format: List of fields to include in response
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # List all local CAs
            >>> result = fgt.cmdb.firewall.ssh.local_ca.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.ssh.local_ca.list(
            ...     format=['name', 'source']
            ... )
        """
        return self.get(
            filter=filter,
            range=range,
            sort=sort,
            format=format,
            vdom=vdom,
            **kwargs
        )
    
    def get(
        self,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        range: Optional[str] = None,
        sort: Optional[str] = None,
        format: Optional[List[str]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Get SSH local CA(s).
        
        Args:
            name: Local CA name (if retrieving specific CA)
            filter: Filter results
            range: Range of results
            sort: Sort results
            format: List of fields to include
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Get specific local CA
            >>> result = fgt.cmdb.firewall.ssh.local_ca.get('company-ca')
            
            >>> # Get all local CAs
            >>> result = fgt.cmdb.firewall.ssh.local_ca.get()
        """
        path = 'firewall.ssh/local-ca'
        if name:
            path = f'{path}/{name}'
        
        params = {}
        param_map = {
            'filter': filter,
            'range': range,
            'sort': sort,
            'format': format,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    def create(
        self,
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        source: Optional[str] = None,
        source_ip: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Create an SSH local CA.
        
        
        Supports two usage patterns:
        1. Pass data dict: create(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Local CA name (max 35 chars)
            source: CA source - 'built-in' or 'user'
            source_ip: CA source IP address
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create local CA
            >>> result = fgt.cmdb.firewall.ssh.local_ca.create(
            ...     'company-ca',
            ...     source='user'
            ... )
            
            >>> # Create with source IP
            >>> result = fgt.cmdb.firewall.ssh.local_ca.create(
            ...     'internal-ca',
            ...     source='user',
            ...     source_ip='192.168.1.50'
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
            if source is not None:
                data['source'] = source
            if source_ip is not None:
                data['source-ip'] = source_ip
        
        return self._client.post('cmdb', 'firewall.ssh/local-ca', data, vdom=vdom)
    def update(
        self,
        name: str,
        data: Optional[Dict[str, Any]] = None,
        source: Optional[str] = None,
        source_ip: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Update an SSH local CA.
        
        
        Supports two usage patterns:
        1. Pass data dict: update(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Local CA name
            source: CA source - 'built-in' or 'user'
            source_ip: CA source IP address
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update source IP
            >>> result = fgt.cmdb.firewall.ssh.local_ca.update(
            ...     'company-ca',
            ...     source_ip='192.168.1.51'
            ... )
        """
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if source is not None:
                data['source'] = source
            if source_ip is not None:
                data['source-ip'] = source_ip
        
        return self._client.put('cmdb', f'firewall.ssh/local-ca/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> HTTPResponse:
        """
        Delete an SSH local CA.
        
        Args:
            name: Local CA name
            vdom: Virtual domain
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete local CA
            >>> result = fgt.cmdb.firewall.ssh.local_ca.delete('company-ca')
        """
        return self._client.delete('cmdb', f'firewall.ssh/local-ca/{name}', vdom=vdom)
    
    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if SSH local CA exists.
        
        Args:
            name: Local CA name
            vdom: Virtual domain
        
        Returns:
            True if local CA exists, False otherwise
        
        Examples:
            >>> if fgt.cmdb.firewall.ssh.local_ca.exists('company-ca'):
            ...     print("Local CA exists")
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

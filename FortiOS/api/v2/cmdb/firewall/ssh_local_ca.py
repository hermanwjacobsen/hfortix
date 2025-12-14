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

from typing import Optional, Union, List


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
    ):
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
    ):
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
        name: str,
        source: Optional[str] = None,
        source_ip: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        Create an SSH local CA.
        
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
        data = {'name': name}
        
        param_map = {
            'source': source,
            'source_ip': source_ip,
        }
        
        api_field_map = {
            'source': 'source',
            'source_ip': 'source-ip',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.ssh/local-ca', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        source: Optional[str] = None,
        source_ip: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        Update an SSH local CA.
        
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
        data = {}
        
        param_map = {
            'source': source,
            'source_ip': source_ip,
        }
        
        api_field_map = {
            'source': 'source',
            'source_ip': 'source-ip',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.put('cmdb', f'firewall.ssh/local-ca/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ):
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

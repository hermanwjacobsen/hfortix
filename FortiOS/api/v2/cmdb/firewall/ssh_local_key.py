"""
FortiOS CMDB - Firewall SSH Local Key
SSH proxy local keys.

API Endpoints:
    GET    /api/v2/cmdb/firewall.ssh/local-key       - List all local keys
    GET    /api/v2/cmdb/firewall.ssh/local-key/{id}  - Get specific local key
    POST   /api/v2/cmdb/firewall.ssh/local-key       - Create local key
    PUT    /api/v2/cmdb/firewall.ssh/local-key/{id}  - Update local key
    DELETE /api/v2/cmdb/firewall.ssh/local-key/{id}  - Delete local key
"""

from typing import Optional, Union, List


class LocalKey:
    """SSH proxy local key endpoint"""
    
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
        List all SSH local keys.
        
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
            >>> # List all local keys
            >>> result = fgt.cmdb.firewall.ssh.local_key.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.ssh.local_key.list(
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
        Get SSH local key(s).
        
        Args:
            name: Local key name (if retrieving specific key)
            filter: Filter results
            range: Range of results
            sort: Sort results
            format: List of fields to include
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Get specific local key
            >>> result = fgt.cmdb.firewall.ssh.local_key.get('server-key')
            
            >>> # Get all local keys
            >>> result = fgt.cmdb.firewall.ssh.local_key.get()
        """
        path = 'firewall.ssh/local-key'
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
        password: Optional[str] = None,
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        Create an SSH local key.
        
        Args:
            name: Local key name (max 35 chars)
            source: Key source - 'built-in' or 'user'
            password: Password for encrypted private key
            private_key: SSH private key (Base64 encoded, PEM format)
            public_key: SSH public key (Base64 encoded)
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create local key
            >>> result = fgt.cmdb.firewall.ssh.local_key.create(
            ...     'server-key',
            ...     source='user'
            ... )
            
            >>> # Create with keys
            >>> result = fgt.cmdb.firewall.ssh.local_key.create(
            ...     'admin-key',
            ...     source='user',
            ...     private_key='LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0t...',
            ...     public_key='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ...'
            ... )
        """
        data = {'name': name}
        
        param_map = {
            'source': source,
            'password': password,
            'private_key': private_key,
            'public_key': public_key,
        }
        
        api_field_map = {
            'source': 'source',
            'password': 'password',
            'private_key': 'private-key',
            'public_key': 'public-key',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.ssh/local-key', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        source: Optional[str] = None,
        password: Optional[str] = None,
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ):
        """
        Update an SSH local key.
        
        Args:
            name: Local key name
            source: Key source - 'built-in' or 'user'
            password: Password for encrypted private key
            private_key: SSH private key (Base64 encoded, PEM format)
            public_key: SSH public key (Base64 encoded)
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update password
            >>> result = fgt.cmdb.firewall.ssh.local_key.update(
            ...     'server-key',
            ...     password='newpassword123'
            ... )
        """
        data = {}
        
        param_map = {
            'source': source,
            'password': password,
            'private_key': private_key,
            'public_key': public_key,
        }
        
        api_field_map = {
            'source': 'source',
            'password': 'password',
            'private_key': 'private-key',
            'public_key': 'public-key',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.put('cmdb', f'firewall.ssh/local-key/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ):
        """
        Delete an SSH local key.
        
        Args:
            name: Local key name
            vdom: Virtual domain
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete local key
            >>> result = fgt.cmdb.firewall.ssh.local_key.delete('server-key')
        """
        return self._client.delete('cmdb', f'firewall.ssh/local-key/{name}', vdom=vdom)
    
    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if SSH local key exists.
        
        Args:
            name: Local key name
            vdom: Virtual domain
        
        Returns:
            True if local key exists, False otherwise
        
        Examples:
            >>> if fgt.cmdb.firewall.ssh.local_key.exists('server-key'):
            ...     print("Local key exists")
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

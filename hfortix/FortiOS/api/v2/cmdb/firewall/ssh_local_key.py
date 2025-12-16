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

from typing import Dict, Optional, Union, List, Any

from .....http_client import HTTPResponse


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
    ) -> HTTPResponse:
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
    ) -> HTTPResponse:
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
        data: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        source: Optional[str] = None,
        password: Optional[str] = None,
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Create an SSH local key.
        
        
        Supports two usage patterns:
        1. Pass data dict: create(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
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
            if password is not None:
                data['password'] = password
            if private_key is not None:
                data['private-key'] = private_key
            if public_key is not None:
                data['public-key'] = public_key
        
        return self._client.post('cmdb', 'firewall.ssh/local-key', data, vdom=vdom)
    def update(
        self,
        name: str,
        data: Optional[Dict[str, Any]] = None,
        source: Optional[str] = None,
        password: Optional[str] = None,
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Update an SSH local key.
        
        
        Supports two usage patterns:
        1. Pass data dict: update(data={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
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
        # Pattern 1: data dict provided
        if data is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            data = {}
            if source is not None:
                data['source'] = source
            if password is not None:
                data['password'] = password
            if private_key is not None:
                data['private-key'] = private_key
            if public_key is not None:
                data['public-key'] = public_key
        
        return self._client.put('cmdb', f'firewall.ssh/local-key/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> HTTPResponse:
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

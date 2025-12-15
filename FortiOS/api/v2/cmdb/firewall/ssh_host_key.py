"""
FortiOS CMDB - Firewall SSH Host Key
SSH proxy host public keys.

API Endpoints:
    GET    /api/v2/cmdb/firewall.ssh/host-key       - List all host keys
    GET    /api/v2/cmdb/firewall.ssh/host-key/{id}  - Get specific host key
    POST   /api/v2/cmdb/firewall.ssh/host-key       - Create host key
    PUT    /api/v2/cmdb/firewall.ssh/host-key/{id}  - Update host key
    DELETE /api/v2/cmdb/firewall.ssh/host-key/{id}  - Delete host key
"""

from typing import Optional, Union, List


class HostKey:
    """SSH proxy host key endpoint"""
    
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
        List all SSH host keys.
        
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
            >>> # List all host keys
            >>> result = fgt.cmdb.firewall.ssh.host_key.list()
            
            >>> # List with specific fields
            >>> result = fgt.cmdb.firewall.ssh.host_key.list(
            ...     format=['name', 'hostname', 'status']
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
        Get SSH host key(s).
        
        Args:
            name: Host key name (if retrieving specific key)
            filter: Filter results
            range: Range of results
            sort: Sort results
            format: List of fields to include
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Get specific host key
            >>> result = fgt.cmdb.firewall.ssh.host_key.get('server1-key')
            
            >>> # Get all host keys
            >>> result = fgt.cmdb.firewall.ssh.host_key.get()
        """
        path = 'firewall.ssh/host-key'
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
        status: Optional[str] = None,
        type: Optional[str] = None,
        hostname: Optional[str] = None,
        nid: Optional[str] = None,
        ip: Optional[str] = None,
        port: Optional[int] = None,
        public_key: Optional[str] = None,
        usage: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Create an SSH host key.
        
        Args:
            name: Host key name (max 35 chars)
            status: Enable/disable host key - 'enable' or 'disable'
            type: Key type - 'RSA' or 'DSA' or 'ECDSA' or 'ED25519'
            hostname: Hostname of the SSH server
            nid: Set the NID for the SSH host
            ip: IP address of the SSH server
            port: Port of the SSH server (1-65535)
            public_key: SSH public key (Base64 encoded)
            usage: Usage - 'transparent-proxy', 'access-proxy'
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create SSH host key
            >>> result = fgt.cmdb.firewall.ssh.host_key.create(
            ...     'server1-key',
            ...     hostname='ssh.example.com',
            ...     ip='192.168.1.100',
            ...     port=22,
            ...     type='RSA',
            ...     status='enable'
            ... )
            
            >>> # Create with public key
            >>> result = fgt.cmdb.firewall.ssh.host_key.create(
            ...     'server2-key',
            ...     hostname='ssh2.example.com',
            ...     public_key='AAAAB3NzaC1yc2EAAAADAQABAAABAQDTest...',
            ...     type='RSA'
            ... )
        """
        data = {'name': name}
        
        param_map = {
            'status': status,
            'type': type,
            'hostname': hostname,
            'nid': nid,
            'ip': ip,
            'port': port,
            'public_key': public_key,
            'usage': usage,
        }
        
        api_field_map = {
            'status': 'status',
            'type': 'type',
            'hostname': 'hostname',
            'nid': 'nid',
            'ip': 'ip',
            'port': 'port',
            'public_key': 'public-key',
            'usage': 'usage',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.post('cmdb', 'firewall.ssh/host-key', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        status: Optional[str] = None,
        type: Optional[str] = None,
        hostname: Optional[str] = None,
        nid: Optional[str] = None,
        ip: Optional[str] = None,
        port: Optional[int] = None,
        public_key: Optional[str] = None,
        usage: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Update an SSH host key.
        
        Args:
            name: Host key name
            status: Enable/disable host key - 'enable' or 'disable'
            type: Key type - 'RSA' or 'DSA' or 'ECDSA' or 'ED25519'
            hostname: Hostname of the SSH server
            nid: Set the NID for the SSH host
            ip: IP address of the SSH server
            port: Port of the SSH server (1-65535)
            public_key: SSH public key (Base64 encoded)
            usage: Usage - 'transparent-proxy', 'access-proxy'
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update hostname and port
            >>> result = fgt.cmdb.firewall.ssh.host_key.update(
            ...     'server1-key',
            ...     hostname='newssh.example.com',
            ...     port=2222
            ... )
            
            >>> # Update status
            >>> result = fgt.cmdb.firewall.ssh.host_key.update(
            ...     'server2-key',
            ...     status='disable'
            ... )
        """
        data = {}
        
        param_map = {
            'status': status,
            'type': type,
            'hostname': hostname,
            'nid': nid,
            'ip': ip,
            'port': port,
            'public_key': public_key,
            'usage': usage,
        }
        
        api_field_map = {
            'status': 'status',
            'type': 'type',
            'hostname': 'hostname',
            'nid': 'nid',
            'ip': 'ip',
            'port': 'port',
            'public_key': 'public-key',
            'usage': 'usage',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.put('cmdb', f'firewall.ssh/host-key/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> HTTPResponse:
        """
        Delete an SSH host key.
        
        Args:
            name: Host key name
            vdom: Virtual domain
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete host key
            >>> result = fgt.cmdb.firewall.ssh.host_key.delete('server1-key')
        """
        return self._client.delete('cmdb', f'firewall.ssh/host-key/{name}', vdom=vdom)
    
    def exists(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None
    ) -> bool:
        """
        Check if SSH host key exists.
        
        Args:
            name: Host key name
            vdom: Virtual domain
        
        Returns:
            True if host key exists, False otherwise
        
        Examples:
            >>> if fgt.cmdb.firewall.ssh.host_key.exists('server1-key'):
            ...     print("Host key exists")
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

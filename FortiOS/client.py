import requests


class FortiOS:
    def __init__(self, host=None, token=None, verify=True, vdom=None, port=None):
        """
        Initialize FortiOS API client
        
        With token authentication, everything is stateless - just provide credentials
        and start making API calls. No login/logout needed.
        
        Args:
            host: FortiGate IP/hostname (e.g., "192.168.1.99")
            token: API token for authentication
            verify: Verify SSL certificates (default: True, use False for self-signed)
            vdom: Virtual domain (default: None = FortiGate's default VDOM)
            port: HTTPS port (default: None = use 443, or specify custom port like 8443)
        
        Examples:
            # Simple - default port 443
            fgt = FortiOS("192.168.1.99", token="abc123", verify=False)
            
            # Custom port
            fgt = FortiOS("192.168.1.99", token="abc123", verify=False, port=8443)
            
            # Port in hostname (alternative)
            fgt = FortiOS("192.168.1.99:8443", token="abc123", verify=False)
        """
        self.host = host
        self.vdom = vdom
        self.port = port
        
        # Build URL with port handling
        if host:
            # If port is already in host string, use as-is
            if ':' in host:
                self.url = f"https://{host}"
            # If explicit port provided, append it
            elif port:
                self.url = f"https://{host}:{port}"
            # Otherwise use default (443)
            else:
                self.url = f"https://{host}"
        else:
            self.url = None
        
        self.verify = verify
        self.session = requests.Session()
        self.session.verify = verify
        
        if not verify:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Set token if provided
        if token:
            self.session.headers['Authorization'] = f'Bearer {token}'
        
        # Initialize API helpers
        from .api.v2.cmdb import CMDB
        from .api.v2.service import Service
        from .api.v2.log import Log
        from .api.v2.monitor import Monitor
        self.cmdb = CMDB(self)
        self.service = Service(self)
        self.log = Log(self)
        self.monitor = Monitor(self)
    
    def request(self, method, api_type, path, data=None, params=None, vdom=None):
        """
        Generic request method for all API calls
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            api_type: API type (cmdb, monitor, log, service)
            path: API endpoint path (e.g., 'firewall/address', 'system/status')
            data: Request body data (for POST/PUT)
            params: Query parameters dict
            vdom: Virtual domain (None=use default, or specify vdom name)
        
        Returns:
            JSON response
        """
        url = f"{self.url}/api/v2/{api_type}/{path}"
        params = params or {}
        
        # Only add vdom parameter if explicitly specified (either from login or this call)
        # Following Fortinet documentation: vdom parameter is optional
        if vdom is not None:
            # Use specific vdom for this request
            params['vdom'] = vdom
        elif self.vdom is not None and 'vdom' not in params:
            # Use default vdom from login
            params['vdom'] = self.vdom
        # else: No vdom parameter (FortiGate uses its default)
        
        # Make request
        res = self.session.request(
            method=method,
            url=url,
            json=data if data else None,
            params=params if params else None
        )
        
        # If error, try to get detailed error message from response
        if not res.ok:
            try:
                error_detail = res.json()
                from .exceptions import APIError
                raise APIError(
                    f"HTTP {res.status_code}: {error_detail}"
                )
            except ValueError:
                # If response is not JSON, just raise the standard error
                res.raise_for_status()
        
        return res.json()
    
    def get(self, api_type, path, params=None, vdom=None):
        """
        GET request
        
        Args:
            api_type: cmdb, monitor, log, service
            path: Endpoint path (e.g., 'firewall/address', 'firewall/address/myaddr')
            params: Query parameters (format, filter, mkey, etc.)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
        
        Examples:
            # Get all firewall addresses
            get('cmdb', 'firewall/address')
            
            # Get specific address
            get('cmdb', 'firewall/address/myaddr')
            
            # With filters
            get('cmdb', 'firewall/address', params={'format': 'name|comment'})
            
            # Skip vdom
            get('cmdb', 'system/alertemail', vdom=False)
            
            # Monitor endpoint
            get('monitor', 'system/status', vdom=False)
        """
        return self.request('GET', api_type, path, params=params, vdom=vdom)
    
    def get_binary(self, api_type, path, params=None, vdom=None):
        """
        GET request returning binary data (for file downloads)
        
        Args:
            api_type: cmdb, monitor, log, service
            path: Endpoint path
            params: Query parameters
            vdom: Virtual domain
        
        Returns:
            bytes: Raw binary response data
        
        Examples:
            # Download packet capture
            pcap_data = get_binary('service', 'sniffer/download', params={'mkey': 'any_root'})
            
            # Download archived file
            archive = get_binary('log', 'disk/ips/archive-download', params={'mkey': 123})
        """
        # Build URL
        url = f"{self.url}/api/v2/{api_type}/{path}"
        params = params or {}
        
        # Add vdom if applicable
        if vdom is not None:
            params['vdom'] = vdom
        elif self.vdom is not None and 'vdom' not in params:
            params['vdom'] = self.vdom
        
        # Make request
        res = self.session.get(url, params=params if params else None)
        
        # Check for errors
        if not res.ok:
            try:
                error_detail = res.json()
                from .exceptions import APIError
                raise APIError(
                    f"HTTP {res.status_code}: {error_detail}"
                )
            except ValueError:
                res.raise_for_status()
        
        # Return raw binary content
        return res.content
    
    def post(self, api_type, path, data, params=None, vdom=None):
        """
        POST request - Create new object
        
        Args:
            api_type: cmdb, monitor, log, service
            path: Endpoint path
            data: Object data to create
            params: Query parameters (action=clone, nkey, etc.)
            vdom: Virtual domain
        
        Examples:
            # Create firewall address
            post('cmdb', 'firewall/address', {'name': 'test', 'subnet': '10.0.0.0/24'})
            
            # Clone existing object
            post('cmdb', 'firewall/address', data, params={'action': 'clone', 'nkey': 'new_name'})
        """
        return self.request('POST', api_type, path, data=data, params=params, vdom=vdom)
    
    def put(self, api_type, path, data, params=None, vdom=None):
        """
        PUT request - Update existing object
        
        Args:
            api_type: cmdb, monitor, log, service
            path: Endpoint path (include object identifier)
            data: Updated object data
            params: Query parameters (action=move, before, after, etc.)
            vdom: Virtual domain
        
        Examples:
            # Update firewall address
            put('cmdb', 'firewall/address/myaddr', {'subnet': '10.0.1.0/24'})
            
            # Move object
            put('cmdb', 'firewall/policy/1', data, params={'action': 'move', 'after': '5'})
        """
        return self.request('PUT', api_type, path, data=data, params=params, vdom=vdom)
    
    def delete(self, api_type, path, params=None, vdom=None):
        """
        DELETE request - Delete object
        
        Args:
            api_type: cmdb, monitor, log, service
            path: Endpoint path (include object identifier)
            params: Query parameters
            vdom: Virtual domain
        
        Examples:
            # Delete firewall address
            delete('cmdb', 'firewall/address/myaddr')
        """
        return self.request('DELETE', api_type, path, params=params, vdom=vdom)
    
    def close(self):
        """
        Close the HTTP session and release resources
        
        Optional: Python automatically cleans up when object is destroyed.
        Use this for explicit resource management or in long-running apps.
        """
        if self.session:
            self.session.close()
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - automatically closes session"""
        self.close()
        return False
    

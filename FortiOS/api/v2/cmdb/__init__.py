"""
FortiOS CMDB API
Configuration Management Database endpoints
"""


class CMDB:
    """
    CMDB API helper class
    Provides access to FortiOS configuration endpoints
    """
    
    def __init__(self, client):
        """
        Initialize CMDB helper
        
        Args:
            client: FortiOS client instance
        """
        self._client = client
        
        # Initialize endpoint classes
        from .alertemail import AlertEmail
        from .antivirus import Antivirus
        from .application import Application
        from .authentication import Authentication
        from .automation import Automation
        from .casb import Casb
        
        self.alertemail = AlertEmail(client)
        self.antivirus = Antivirus(client)
        self.application = Application(client)
        self.authentication = Authentication(client)
        self.automation = Automation(client)
        self.casb = Casb(client)
    
    def get(self, path, params=None, vdom=None):
        """
        GET request to CMDB API
        
        Args:
            path: Endpoint path (e.g., 'firewall/address', 'alertemail/setting')
            params: Query parameters dict
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
        
        Returns:
            JSON response
        
        Examples:
            # Get all firewall addresses
            cmdb.get('firewall/address')
            
            # Get specific address
            cmdb.get('firewall/address/myaddr')
            
            # With filters
            cmdb.get('firewall/address', params={'format': 'name|comment'})
            
            # Skip vdom
            cmdb.get('alertemail/setting', vdom=False)
        """
        return self._client.request('GET', 'cmdb', path, params=params, vdom=vdom)
    
    def post(self, path, data, params=None, vdom=None):
        """
        POST request to CMDB API - Create new object
        
        Args:
            path: Endpoint path
            data: Object data to create
            params: Query parameters (action=clone, nkey, etc.)
            vdom: Virtual domain
        
        Returns:
            JSON response
        
        Examples:
            # Create firewall address
            cmdb.post('firewall/address', {'name': 'test', 'subnet': '10.0.0.0/24'})
            
            # Clone existing
            cmdb.post('firewall/address', data, params={'action': 'clone', 'nkey': 'new_name'})
        """
        return self._client.request('POST', 'cmdb', path, data=data, params=params, vdom=vdom)
    
    def put(self, path, data, params=None, vdom=None):
        """
        PUT request to CMDB API - Update existing object
        
        Args:
            path: Endpoint path (include object identifier)
            data: Updated object data
            params: Query parameters (action=move, before, after, etc.)
            vdom: Virtual domain
        
        Returns:
            JSON response
        
        Examples:
            # Update firewall address
            cmdb.put('firewall/address/myaddr', {'subnet': '10.0.1.0/24'})
            
            # Move object
            cmdb.put('firewall/policy/1', data, params={'action': 'move', 'after': '5'})
        """
        return self._client.request('PUT', 'cmdb', path, data=data, params=params, vdom=vdom)
    
    def delete(self, path, params=None, vdom=None):
        """
        DELETE request to CMDB API - Delete object
        
        Args:
            path: Endpoint path (include object identifier)
            params: Query parameters
            vdom: Virtual domain
        
        Returns:
            JSON response
        
        Examples:
            # Delete firewall address
            cmdb.delete('firewall/address/myaddr')
        """
        return self._client.request('DELETE', 'cmdb', path, params=params, vdom=vdom)

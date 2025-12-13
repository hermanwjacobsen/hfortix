"""
FortiOS CMDB - Certificate Remote

View remote certificates.

API Endpoints:
    GET    /certificate/remote       - List all remote certificates
    GET    /certificate/remote/{name} - Get specific remote certificate

Note: This is a READ-ONLY endpoint. Remote certificates are typically:
    - Certificates from remote servers
    - SSL/TLS certificates from external services
    - Certificates retrieved during SSL inspection
"""


class Remote:
    """Certificate Remote endpoint (read-only)"""
    
    def __init__(self, client):
        """
        Initialize Remote endpoint
        
        Args:
            client: FortiOS client instance
        """
        self._client = client
    
    def list(self, vdom=None, **kwargs):
        """
        List all remote certificates
        
        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)
            
        Returns:
            dict: API response with list of remote certificates
            
        Examples:
            >>> # List all remote certificates
            >>> result = fgt.cmdb.certificate.remote.list()
            
            >>> # List with search
            >>> result = fgt.cmdb.certificate.remote.list(search='vpn')
        """
        return self.get(vdom=vdom, **kwargs)
    
    def get(self, name=None, attr=None, count=None, skip_to_datasource=None, acs=None, 
            search=None, scope=None, datasource=None, with_meta=None, skip=None, 
            format=None, action=None, vdom=None, **kwargs):
        """
        Get remote certificate(s)
        
        Args:
            name (str, optional): Remote certificate name (for specific certificate)
            filter (str): Filter results
            format (str): Response format (name|brief|full)
            count (int): Limit number of results
            with_meta (bool): Include meta information
            skip (int): Skip N results
            search (str): Search string
            vdom (str/bool, optional): Virtual domain, False to skip
            
        Returns:
            dict: API response
            
        Examples:
            >>> # Get specific remote certificate
            >>> result = fgt.cmdb.certificate.remote.get('RemoteCert1')
            
            >>> # Get all remote certificates
            >>> result = fgt.cmdb.certificate.remote.get()
            
            >>> # Get with details
            >>> result = fgt.cmdb.certificate.remote.get('RemoteCert1', with_meta=True)
        """
        # Build path
        path = f'certificate/remote/{name}' if name else 'certificate/remote'
        
        # Build query parameters
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
            'action': action
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        # Add any additional parameters
        params.update(kwargs)
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    
    def exists(self, name, vdom=None):
        """
        Check if remote certificate exists
        
        Args:
            name (str): Remote certificate name
            vdom (str/bool, optional): Virtual domain, False to skip
        
        Returns:
            bool: True if exists, False otherwise
        
        Example:
            >>> if fgt.cmdb.certificate.remote.exists('RemoteCert1'):
            ...     print('Remote certificate exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except:
            return False

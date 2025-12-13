"""
FortiOS CMDB - Certificate CA

View CA (Certificate Authority) certificates.

API Endpoints:
    GET    /certificate/ca       - List all CA certificates
    GET    /certificate/ca/{name} - Get specific CA certificate

Note: This is a READ-ONLY endpoint. CA certificates are typically:
    - Bundle certificates (pre-installed by Fortinet)
    - User-uploaded certificates via GUI/CLI
    - Factory certificates
"""


class Ca:
    """Certificate CA endpoint (read-only)"""
    
    def __init__(self, client):
        """
        Initialize Ca endpoint
        
        Args:
            client: FortiOS client instance
        """
        self._client = client
    
    def list(self, vdom=None, **kwargs):
        """
        List all CA certificates
        
        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)
            
        Returns:
            dict: API response with list of CA certificates
            
        Examples:
            >>> # List all CA certificates
            >>> result = fgt.cmdb.certificate.ca.list()
            
            >>> # List only user-uploaded certificates
            >>> result = fgt.cmdb.certificate.ca.list(filter='source==user')
            
            >>> # List trusted certificates
            >>> result = fgt.cmdb.certificate.ca.list(filter='ssl-inspection-trusted==enable')
        """
        return self.get(vdom=vdom, **kwargs)
    
    def get(self, name=None, attr=None, count=None, skip_to_datasource=None, acs=None, 
            search=None, scope=None, datasource=None, with_meta=None, skip=None, 
            format=None, action=None, vdom=None, **kwargs):
        """
        Get CA certificate(s)
        
        Args:
            name (str, optional): CA certificate name (for specific certificate)
            filter (str): Filter results (e.g., 'source==bundle')
            format (str): Response format (name|brief|full)
            count (int): Limit number of results
            with_meta (bool): Include meta information
            skip (int): Skip N results
            search (str): Search string
            vdom (str/bool, optional): Virtual domain, False to skip
            
        Returns:
            dict: API response
            
        Examples:
            >>> # Get specific CA certificate
            >>> result = fgt.cmdb.certificate.ca.get('Fortinet_CA_SSL')
            
            >>> # Get all CA certificates
            >>> result = fgt.cmdb.certificate.ca.get()
            
            >>> # Get with details
            >>> result = fgt.cmdb.certificate.ca.get('Fortinet_CA_SSL', with_meta=True)
        """
        # Build path
        path = f'certificate/ca/{name}' if name else 'certificate/ca'
        
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
        Check if CA certificate exists
        
        Args:
            name (str): CA certificate name
            vdom (str/bool, optional): Virtual domain, False to skip
        
        Returns:
            bool: True if exists, False otherwise
        
        Example:
            >>> if fgt.cmdb.certificate.ca.exists('Fortinet_CA_SSL'):
            ...     print('CA certificate exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except:
            return False
    
    def get_bundle_certificates(self, vdom=None):
        """
        Get all bundle (pre-installed) CA certificates
        
        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
        
        Returns:
            dict: API response with bundle certificates
        
        Example:
            >>> result = fgt.cmdb.certificate.ca.get_bundle_certificates()
            >>> print(f"Bundle CAs: {len(result['results'])}")
        """
        return self.get(filter='source==bundle', vdom=vdom)
    
    def get_user_certificates(self, vdom=None):
        """
        Get all user-uploaded CA certificates
        
        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
        
        Returns:
            dict: API response with user certificates
        
        Example:
            >>> result = fgt.cmdb.certificate.ca.get_user_certificates()
            >>> print(f"User CAs: {len(result['results'])}")
        """
        return self.get(filter='source==user', vdom=vdom)
    
    def get_trusted_certificates(self, vdom=None):
        """
        Get all trusted CA certificates (for SSL inspection)
        
        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
        
        Returns:
            dict: API response with trusted certificates
        
        Example:
            >>> result = fgt.cmdb.certificate.ca.get_trusted_certificates()
            >>> print(f"Trusted CAs: {len(result['results'])}")
        """
        return self.get(filter='ssl-inspection-trusted==enable', vdom=vdom)

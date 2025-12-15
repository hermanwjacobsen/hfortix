"""
FortiOS API endpoint: firewall.ssl/setting

SSL proxy settings (singleton).
"""


class Setting:
    """
    Manage SSL proxy settings.
    
    This is a singleton endpoint - there is only one SSL proxy settings object.
    Only GET and UPDATE operations are supported.
    
    API Path: firewall.ssl/setting
    """
    
    def __init__(self, client):
        """
        Initialize the Setting endpoint.
        
        Args:
            client: FortiOS API client instance
        """
        self._client = client
    
    def get(self, vdom=None, **params) -> HTTPResponse:
        """
        Get SSL proxy settings.
        
        Args:
            vdom (str, optional): Virtual domain name
            **params: Additional query parameters (filter, format, etc.)
            
        Returns:
            dict: API response containing SSL proxy settings
            
        Example:
            # Get all settings
            result = fgt.cmdb.firewall.ssl.setting.get()
            
            # Get with metadata
            result = fgt.cmdb.firewall.ssl.setting.get(meta=True)
        """
        return self._client.get('cmdb', 'firewall.ssl/setting', vdom=vdom, params=params)
    
    def update(
        self,
        proxy_connect_timeout: int = None,
        ssl_dh_bits: str = None,
        ssl_send_empty_frags: str = None,
        no_matching_cipher_action: str = None,
        cert_cache_capacity: int = None,
        cert_cache_timeout: int = None,
        session_cache_capacity: int = None,
        session_cache_timeout: int = None,
        kxp_queue_threshold: int = None,
        ssl_queue_threshold: int = None,
        abbreviate_handshake: str = None,
        vdom=None
    ) -> HTTPResponse:
        """
        Update SSL proxy settings.
        
        Args:
            proxy_connect_timeout (int): Time limit to detect proxy connection timeout (1-3600 sec)
            ssl_dh_bits (str): Bit-size of Diffie-Hellman prime: 768, 1024, 1536, 2048, 3072, 4096
            ssl_send_empty_frags (str): Enable/disable sending empty fragments: enable, disable
            no_matching_cipher_action (str): Bypass or drop the connection on no matching cipher: bypass, drop
            cert_cache_capacity (int): Maximum capacity of certificate cache (0 for unlimited)
            cert_cache_timeout (int): Time limit to cache certificate (1-120 min)
            session_cache_capacity (int): Capacity of SSL session cache (1-1000)
            session_cache_timeout (int): Time limit for SSL session cache (1-60 min)
            kxp_queue_threshold (int): Maximum queue depth for key exchange protocol
            ssl_queue_threshold (int): Maximum queue depth for SSL
            abbreviate_handshake (str): Enable/disable abbreviated handshake: enable, disable
            vdom (str, optional): Virtual domain name
            
        Returns:
            dict: API response
            
        Example:
            # Update timeout settings
            result = fgt.cmdb.firewall.ssl.setting.update(
                proxy_connect_timeout=30,
                cert_cache_timeout=60
            )
            
            # Update SSL settings
            result = fgt.cmdb.firewall.ssl.setting.update(
                ssl_dh_bits='2048',
                ssl_send_empty_frags='enable',
                abbreviate_handshake='enable'
            )
        """
        data = {}
        
        if proxy_connect_timeout is not None:
            data['proxy-connect-timeout'] = proxy_connect_timeout
        if ssl_dh_bits is not None:
            data['ssl-dh-bits'] = ssl_dh_bits
        if ssl_send_empty_frags is not None:
            data['ssl-send-empty-frags'] = ssl_send_empty_frags
        if no_matching_cipher_action is not None:
            data['no-matching-cipher-action'] = no_matching_cipher_action
        if cert_cache_capacity is not None:
            data['cert-cache-capacity'] = cert_cache_capacity
        if cert_cache_timeout is not None:
            data['cert-cache-timeout'] = cert_cache_timeout
        if session_cache_capacity is not None:
            data['session-cache-capacity'] = session_cache_capacity
        if session_cache_timeout is not None:
            data['session-cache-timeout'] = session_cache_timeout
        if kxp_queue_threshold is not None:
            data['kxp-queue-threshold'] = kxp_queue_threshold
        if ssl_queue_threshold is not None:
            data['ssl-queue-threshold'] = ssl_queue_threshold
        if abbreviate_handshake is not None:
            data['abbreviate-handshake'] = abbreviate_handshake
        
        return self._client.put('cmdb', 'firewall.ssl/setting', data, vdom=vdom)

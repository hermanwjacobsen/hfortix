"""
FortiOS firewall.ssl sub-category.

Provides access to SSL proxy configuration endpoints.
"""


class Ssl:
    """
    SSL proxy configuration sub-category.
    
    This class provides access to SSL proxy settings through property methods
    that lazy-load the corresponding endpoint modules.
    
    Usage:
        fgt.cmdb.firewall.ssl.setting.get()
    """
    
    def __init__(self, client):
        self._client = client
        self._setting = None
    
    @property
    def setting(self):
        """
        Access the SSL proxy settings endpoint (singleton).
        
        Returns:
            Setting: SSL proxy settings endpoint instance
            
        Example:
            result = fgt.cmdb.firewall.ssl.setting.get()
        """
        if self._setting is None:
            from .ssl_setting import Setting
            self._setting = Setting(self._client)
        return self._setting

"""
FortiOS Log API
Log retrieval endpoints for various log sources
"""


class Log:
    """
    Log API helper class
    Provides access to log endpoints
    """
    
    def __init__(self, client):
        """
        Initialize Log helper
        
        Args:
            client: FortiOS client instance
        """
        self._client = client
        
        # Initialize endpoint classes
        from .disk.disk import Disk
        from .fortianalyzer.fortianalyzer import FortiAnalyzer
        from .memory.memory import Memory
        
        self.disk = Disk(client)
        self.fortianalyzer = FortiAnalyzer(client)
        self.memory = Memory(client)
    
    def get(self, endpoint, params=None):
        """
        GET request to log API endpoint
        
        Args:
            endpoint: API endpoint path (without /api/v2/log/)
            params: Query parameters
        
        Returns:
            dict: API response
        """
        return self._client.get('log', endpoint, params=params)
    
    def get_binary(self, endpoint, params=None):
        """
        GET request to log API endpoint returning binary data
        
        Args:
            endpoint: API endpoint path (without /api/v2/log/)
            params: Query parameters
        
        Returns:
            bytes: Binary response data
        """
        return self._client.get_binary('log', endpoint, params=params)

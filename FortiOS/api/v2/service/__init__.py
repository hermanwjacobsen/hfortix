"""
FortiOS Service API
Service endpoints for operations and diagnostics
"""


class Service:
    """
    Service API helper class
    Provides access to service endpoints
    """
    
    def __init__(self, client):
        """
        Initialize Service helper
        
        Args:
            client: FortiOS client instance
        """
        self._client = client
        
        # Initialize endpoint classes
        from .sniffer.sniffer import Sniffer
        
        self.sniffer = Sniffer(client)

"""
FortiOS Monitor API
Real-time monitoring and status endpoints

Note: Monitor API endpoints are not yet implemented.
This is a placeholder for future development.
"""


class Monitor:
    """
    Monitor API helper class
    Provides access to FortiOS monitoring endpoints (Coming Soon)
    
    The Monitor API provides real-time status information and monitoring
    capabilities for FortiGate devices. This module is under development.
    
    Planned categories (0/29 implemented):
    - system/ - System status and performance
    - firewall/ - Firewall statistics and sessions
    - router/ - Routing table and statistics
    - vpn/ - VPN status and tunnels
    - user/ - User authentication status
    - wifi/ - WiFi status and clients
    - switch-controller/ - Switch management
    - log/ - Log statistics
    - webfilter/ - Web filtering statistics
    - antivirus/ - Antivirus status
    - ips/ - IPS status
    - application/ - Application control statistics
    - endpoint-control/ - Endpoint status
    - network/ - Network statistics
    - fortiguard/ - FortiGuard status
    - license/ - License information
    - system-config/ - Configuration status
    - utm/ - UTM statistics
    - And 11 more...
    """
    
    def __init__(self, client):
        """
        Initialize Monitor helper
        
        Args:
            client: FortiOS client instance
        """
        self._client = client
    
    def get(self, path, params=None, vdom=None):
        """
        GET request to Monitor API
        
        Args:
            path: Endpoint path (e.g., 'system/status', 'firewall/session')
            params: Query parameters dict
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
        
        Returns:
            JSON response
        
        Examples:
            >>> # Get system status
            >>> monitor.get('system/status')
            
            >>> # Get firewall sessions
            >>> monitor.get('firewall/session')
            
            >>> # Get interface statistics
            >>> monitor.get('system/interface', params={'interface_name': 'port1'})
        
        Note:
            Most monitor endpoints are read-only (GET only) and provide
            real-time status information. Some endpoints may support POST
            for triggering actions (e.g., clearing sessions).
        """
        return self._client.get('monitor', path, params=params, vdom=vdom)

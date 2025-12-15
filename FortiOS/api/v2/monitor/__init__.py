"""
FortiOS Monitor API
Real-time monitoring and status endpoints

Note: Monitor API endpoints are not yet implemented.
This is a placeholder for future development.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient

__all__ = ['Monitor']


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

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Monitor helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return []  # No public attributes yet, monitor endpoints not implemented


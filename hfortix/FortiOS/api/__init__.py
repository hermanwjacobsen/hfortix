"""
FortiOS API
Main API namespace containing cmdb, monitor, log, and service
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..http_client import HTTPClient
    from .v2.cmdb import CMDB
    from .v2.log import Log
    from .v2.monitor import Monitor
    from .v2.service import Service

__all__ = ['API']


class API:
    """
    FortiOS API namespace
    
    Attributes:
        cmdb: Configuration Management Database
        monitor: Real-time monitoring
        log: Log retrieval
        service: System services
    """
    
    # Type hints for attributes (helps IDE autocomplete)
    cmdb: 'CMDB'
    log: 'Log'
    monitor: 'Monitor'
    service: 'Service'
    
    def __init__(self, client: 'HTTPClient') -> None:
        """Initialize API namespace"""
        # Keep a reference to the internal HTTP client for advanced usage and
        # for the repository's script-style harnesses under X/tests.
        self._client = client

        from .v2.cmdb import CMDB
        from .v2.log import Log
        from .v2.monitor import Monitor
        from .v2.service import Service
        
        self.cmdb = CMDB(client)
        self.log = Log(client)
        self.monitor = Monitor(client)
        self.service = Service(client)
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return ['cmdb', 'log', 'monitor', 'service']

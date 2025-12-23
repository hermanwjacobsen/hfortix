"""
FortiOS REST API v2 Interface

Provides access to all FortiOS REST API endpoints organized by category:
- CMDB (Configuration Management Database): Create/read/update/delete
configuration
- Monitor: Real-time status and monitoring data
- Log: Historical log retrieval and search
- Service: System services and operations

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # CMDB: Configuration operations (POST/PUT/GET/DELETE)
    >>> fgt.api.cmdb.firewall.address.post(name="Server", subnet="10.1.1.5/32")
    >>> fgt.api.cmdb.firewall.address.put(name="Server", subnet="10.1.1.6/32")
    >>> fgt.api.cmdb.system.interface.get(name="port1")
    >>>
    >>> # Monitor: Real-time data (GET only, read-only)
    >>> fgt.api.monitor.system.resource.get()
    >>> fgt.api.monitor.firewall.session.get()
    >>> fgt.api.monitor.router.ipv4.get()
    >>>
    >>> # Log: Historical logs (GET only, read-only)
    >>> fgt.api.log.disk.traffic.get()
    >>> fgt.api.log.memory.event.get()

See Also:
    - CMDB documentation: help(fgt.api.cmdb)
    - Monitor documentation: help(fgt.api.monitor)
    - FortiOS REST API: https://docs.fortinet.com/
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional

    from ..http_client_interface import IHTTPClient
    from .utils import Utils
    from .v2.cmdb import CMDB
    from .v2.log import Log
    from .v2.monitor import Monitor
    from .v2.service import Service

__all__ = ["API"]


class API:
    """
    FortiOS REST API v2 Interface.

    Organizes all FortiOS API endpoints into logical categories for easy
    access.

    Attributes:
        cmdb: Configuration Management Database (CRUD operations on config)
            - Create objects with POST
            - Update objects with PUT
            - Read objects with GET
            - Delete objects with DELETE
            - Example: fgt.api.cmdb.firewall.address.post(...)

        monitor: Real-time monitoring and status (read-only, GET operations)
            - System resources, interfaces, sessions
            - Firewall statistics and connections
            - Routing tables, VPN status
            - Example: fgt.api.monitor.system.resource.get()

        log: Historical log retrieval (read-only, GET operations)
            - Traffic logs, event logs, security logs
            - Disk, memory, FortiAnalyzer logs
            - Example: fgt.api.log.disk.traffic.get()

        service: System services and operations
            - Special service endpoints
            - Example: fgt.api.service.system.get()

        utils: Utility functions for testing and diagnostics
            - Performance testing and benchmarking
            - Connection pool validation
            - Device profiling and recommendations
            - Example: fgt.api.utils.performance_test()

    HTTP Method Guidelines:
        - **POST**: Create new configuration objects (returns 404 if already
        exists)
        - **PUT**: Update existing configuration objects (returns 404 if not
        found)
        - **GET**: Retrieve data (config, monitoring, logs) - read-only
        - **DELETE**: Remove configuration objects (returns 404 if not found)

    Example:
        >>> from hfortix.FortiOS import FortiOS
        >>> fgt = FortiOS(host="192.168.1.99", token="your-token")
        >>>
        >>> # CMDB: Manage configuration
        >>> fgt.api.cmdb.firewall.address.post(name="WebServer",
        subnet="10.0.0.5/32")
        >>> fgt.api.cmdb.firewall.policy.get(policyid=1)
        >>>
        >>> # Monitor: Real-time data
        >>> fgt.api.monitor.system.interface.get()
        >>> fgt.api.monitor.firewall.session.get()
        >>>
        >>> # Log: Historical data
        >>> fgt.api.log.disk.traffic.get(count=100)
    """

    # Type hints for attributes (helps IDE autocomplete)
    cmdb: "CMDB"
    log: "Log"
    monitor: "Monitor"
    service: "Service"
    utils: (
        "Optional[Utils]"  # None when using custom IHTTPClient implementations
    )

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize API namespace with HTTP client implementing IHTTPClient
        protocol.

        Note:
            Utils requires concrete HTTPClient for internal access. When a
            protocol-only
            client is provided, Utils will be unavailable (set to None).
        """
        # Keep a reference to the internal HTTP client for advanced usage and
        # for the repository's script-style harnesses under X/tests.
        self._client = client

        from .utils import Utils
        from .v2.cmdb import CMDB
        from .v2.log import Log
        from .v2.monitor import Monitor
        from .v2.service import Service

        self.cmdb = CMDB(client)
        self.log = Log(client)
        self.monitor = Monitor(client)
        self.service = Service(client)

        # Utils requires concrete HTTPClient for access to internal attributes
        # Check if client is the concrete HTTPClient type
        from ..http_client import HTTPClient

        if isinstance(client, HTTPClient):
            self.utils = Utils(client)
        else:
            # Custom protocol implementations won't have utils
            self.utils = None

    def __dir__(self) -> list[str]:
        """Control autocomplete to show only public attributes"""
        return ["cmdb", "log", "monitor", "service", "utils"]

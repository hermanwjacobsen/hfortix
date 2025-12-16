from __future__ import annotations

from typing import Any, Optional, Union

from .http_client import HTTPClient
from .api import API

__all__ = ['FortiOS']


class FortiOS:
    """
    FortiOS REST API Client
    
    Python client for interacting with Fortinet FortiGate firewalls via REST API.
    Supports configuration management (CMDB), monitoring, logging, and services.
    
    This client uses token-based authentication and provides a stateless interface
    to FortiOS devices. No login/logout required - just initialize with your token
    and start making API calls.
    
    Main API categories:
        - api.cmdb: Configuration Management Database (firewall policies, objects, etc.)
        - api.monitor: Real-time monitoring and status
        - api.log: Log queries and analysis
        - api.service: System services (sniffer, security rating, etc.)
    
    Attributes:
        api (API): API namespace containing cmdb, monitor, log, service
    
    Example:
    >>> from hfortix import FortiOS
        >>> fgt = FortiOS("fortigate.example.com", token="your_token_here")
        >>> 
        >>> # List firewall addresses
        >>> addresses = fgt.api.cmdb.firewall.address.list()
        >>> 
        >>> # Create a firewall address
        >>> fgt.api.cmdb.firewall.address.create(
        ...     name='test-host',
        ...     subnet='192.0.2.100/32',
        ...     comment='Example host'
        ... )
        >>> 
        >>> # Get system status
        >>> status = fgt.api.monitor.system.status.get()
    
    Note:
        - Requires FortiOS 6.0+ with REST API enabled
        - API token must be created in FortiOS: System > Admin > API Users
        - Use verify=False only in development with self-signed certificates
    
    See Also:
        - API Reference: https://docs.fortinet.com/
        - Token Setup: QUICKSTART.md
        - Examples: EXAMPLES.md
    """
    
    # Type hint for IDE autocomplete (note: Python will also create __annotations__)
    api: API
    
    def __init__(
        self,
        host: Optional[str] = None,
        token: Optional[str] = None,
        verify: bool = True,
        vdom: Optional[str] = None,
        port: Optional[int] = None
    ) -> None:
        """
        Initialize FortiOS API client

        With token authentication, everything is stateless - just provide credentials
        and start making API calls. No login/logout needed.

        Args:
            host: FortiGate IP/hostname (e.g., "192.0.2.10" or "fortigate.example.com")
            token: API token for authentication
            verify: Verify SSL certificates (default: True, recommended for production)
            vdom: Virtual domain (default: None = FortiGate's default VDOM)
            port: HTTPS port (default: None = use 443, or specify custom port like 8443)

        Examples:
            # Production - with valid SSL certificate
            fgt = FortiOS("fortigate.example.com", token="your_token_here", verify=True)

            # Development/Testing - with self-signed certificate (example IP from RFC 5737)
            fgt = FortiOS("192.0.2.10", token="your_token_here", verify=False)

            # Custom port
            fgt = FortiOS("192.0.2.10", token="your_token_here", verify=False, port=8443)

            # Port in hostname (alternative)
            fgt = FortiOS("192.0.2.10:8443", token="your_token_here", verify=False)
        """
        self._host = host
        self._vdom = vdom
        self._port = port

        # Build URL with port handling
        if host:
            # If port is already in host string, use as-is
            if ':' in host:
                url = f"https://{host}"
            # If explicit port provided, append it
            elif port:
                url = f"https://{host}:{port}"
            # Otherwise use default (443)
            else:
                url = f"https://{host}"
        else:
            url = None

        # Initialize HTTP client
        self._client = HTTPClient(
            url=url,
            verify=verify,
            token=token,
            vdom=vdom
        )

        # Initialize API namespace.
        # Store it privately and expose a property so IDEs treat it as a concrete
        # instance attribute (often improves autocomplete ranking vs dunder attrs).
        self._api = API(self._client)

    @property
    def api(self) -> API:
        """Primary entry point to FortiOS endpoints (cmdb/monitor/log/service)."""
        return self._api

    def __dir__(self) -> list[str]:
        """Prefer showing `api` early in interactive completion."""
        # Start with the default dir() list, then move "api" to the front.
        names = sorted(set(super().__dir__()))
        if 'api' in names:
            names.remove('api')
            names.insert(0, 'api')
        return names

    @property
    def host(self) -> Optional[str]:
        """FortiGate hostname or IP address"""
        return self._host

    @property
    def port(self) -> Optional[int]:
        """HTTPS port number"""
        return self._port

    @property
    def vdom(self) -> Optional[str]:
        """Active virtual domain"""
        return self._vdom

    def close(self) -> None:
        """
        Close the HTTP session and release resources

        Optional: Python automatically cleans up when object is destroyed.
        Use this for explicit resource management or in long-running apps.
        """
        self._client.close()

    def __enter__(self) -> 'FortiOS':
        """Context manager entry"""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        """Context manager exit - automatically closes session"""
        self.close()
        return False


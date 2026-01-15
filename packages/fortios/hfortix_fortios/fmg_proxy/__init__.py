"""
FortiManager Proxy Module

Enables FortiOS API calls to be routed through FortiManager to managed devices.

Example:
    >>> from hfortix_fortios import FortiManagerProxy
    >>>
    >>> # Connect to FortiManager
    >>> fmg = FortiManagerProxy(
    ...     host="fortimanager.example.com",
    ...     username="admin",
    ...     password="password",
    ... )
    >>>
    >>> # Get a proxied FortiOS client for a specific device
    >>> fgt = fmg.proxy(adom="production", device="firewall-01")
    >>>
    >>> # Use the exact same FortiOS API!
    >>> addresses = fgt.api.cmdb.firewall.address.get()
    >>> for addr in addresses:
    ...     print(f"{addr.name}: {addr.subnet}")
"""

from .client import FortiManagerProxy, ProxiedFortiOS, ProxyHTTPClient, FMGSession
from .models import ProxyResponse, DeviceResult

# Alias for backward compatibility
FMGProxyClient = ProxyHTTPClient

__all__ = [
    "FortiManagerProxy",
    "ProxiedFortiOS",
    "ProxyHTTPClient",
    "FMGProxyClient",  # Alias
    "FMGSession",
    "ProxyResponse",
    "DeviceResult",
]

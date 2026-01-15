"""Type stubs for FortiManager Proxy module."""

from .client import FortiManagerProxy as FortiManagerProxy
from .client import ProxiedFortiOS as ProxiedFortiOS
from .client import ProxyHTTPClient as ProxyHTTPClient
from .client import FMGSession as FMGSession
from .models import ProxyResponse as ProxyResponse
from .models import DeviceResult as DeviceResult

# Alias
FMGProxyClient = ProxyHTTPClient

__all__ = [
    "FortiManagerProxy",
    "ProxiedFortiOS",
    "ProxyHTTPClient",
    "FMGProxyClient",
    "FMGSession",
    "ProxyResponse",
    "DeviceResult",
]

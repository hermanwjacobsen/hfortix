"""Type stubs for FMG proxy client."""

from typing import Any, Literal

from hfortix_core.http import HTTPClientFMG
from hfortix_fortios.api import API
from .models import ProxyResponse, DeviceResult

# FMGSession is now an alias to HTTPClientFMG
FMGSession = HTTPClientFMG


class ProxyHTTPClient:
    """HTTP client that routes FortiOS API calls through FortiManager."""
    
    def __init__(
        self,
        session: FMGSession,
        target: str,
        vdom: str | None = None,
    ) -> None: ...
    
    def get(
        self,
        api_type: str,
        path: str,
        params: dict[str, Any] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]: ...
    
    def post(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]: ...
    
    def put(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]: ...
    
    def delete(
        self,
        api_type: str,
        path: str,
        params: dict[str, Any] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]: ...


class FortiManagerProxy:
    """
    FortiManager Proxy Client.
    
    Allows making FortiOS API calls to managed devices through FortiManager.
    
    Example:
        >>> from hfortix_fortios import FortiManagerProxy
        >>>
        >>> fmg = FortiManagerProxy(
        ...     host="fortimanager.example.com",
        ...     username="admin",
        ...     password="password",
        ... )
        >>>
        >>> fgt = fmg.proxy(adom="production", device="firewall-01")
        >>> addresses = fgt.api.cmdb.firewall.address.get()
    """
    
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        port: int = 443,
        verify: bool = True,
        timeout: float = 60.0,
        adom: str | None = None,
    ) -> None: ...
    
    @property
    def host(self) -> str: ...
    @property
    def adom(self) -> str | None: ...
    @property
    def verify(self) -> bool: ...
    @property
    def is_authenticated(self) -> bool: ...
    
    def login(self) -> None: ...
    def logout(self) -> None: ...
    
    def proxy(
        self,
        device: str,
        adom: str | None = None,
        vdom: str | None = None,
        timeout: int = 60,
    ) -> "ProxiedFortiOS": ...
    
    def __enter__(self) -> "FortiManagerProxy": ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...


class ProxiedFortiOS:
    """
    FortiOS client that routes API calls through FortiManager.
    
    Provides the same API as the direct FortiOS client but sends
    requests through FortiManager's proxy endpoint.
    """
    
    _proxy_client: ProxyHTTPClient
    
    def __init__(
        self,
        session: FMGSession,
        target: str,
        vdom: str | None = None,
    ) -> None: ...
    
    @property
    def api(self) -> API: ...
    @property
    def target(self) -> str: ...
    @property
    def vdom(self) -> str | None: ...

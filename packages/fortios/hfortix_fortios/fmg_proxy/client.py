"""
FortiManager Proxy Client

Main client class for proxying FortiOS API calls through FortiManager.
"""

from __future__ import annotations

import time
from typing import Any, Literal, cast

from hfortix_core.http import HTTPClientFMG

from .models import ProxyResponse, DeviceResult


# Re-export HTTPClientFMG as FMGSession for backward compatibility
FMGSession = HTTPClientFMG


class ProxyHTTPClient:
    """
    HTTP client adapter that converts FortiOS REST API calls to FMG proxy format.
    
    This implements the same interface as hfortix_core HTTPClient, but routes
    all requests through FortiManager's /sys/proxy/json endpoint.
    """
    
    def __init__(
        self,
        fmg_session: FMGSession,
        target: str,
        vdom: str | None = None,
        timeout: int = 60,
    ):
        """
        Initialize the proxy HTTP client.
        
        Args:
            fmg_session: FMG session for making requests
            target: Target device/group path (e.g., "adom/root/device/fw-01")
            vdom: Default VDOM for requests
            timeout: Default timeout for proxy requests
        """
        self._fmg = fmg_session
        self._target = target
        self._vdom = vdom
        self._timeout = timeout
        self._last_response_time: float | None = None
    
    def _build_resource(
        self,
        api_type: str,
        path: str,
        params: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
    ) -> str:
        """
        Build the FortiOS resource URL for the proxy request.
        
        Args:
            api_type: API type (cmdb, monitor, etc.)
            path: API path (e.g., "/firewall/address")
            params: Query parameters
            vdom: VDOM override
            
        Returns:
            Full resource URL (e.g., "/api/v2/cmdb/firewall/address?vdom=root")
        """
        # Normalize path
        path = path.lstrip("/")
        resource = f"/api/v2/{api_type}/{path}"
        
        # Build query string
        query_parts = []
        
        # Handle VDOM
        effective_vdom = vdom if vdom is not None else self._vdom
        if effective_vdom is True:
            query_parts.append("global=1")
        elif effective_vdom:
            query_parts.append(f"vdom={effective_vdom}")
        
        # Add other params
        if params:
            for key, value in params.items():
                if value is not None:
                    if isinstance(value, list):
                        for v in value:
                            query_parts.append(f"{key}={v}")
                    else:
                        query_parts.append(f"{key}={value}")
        
        if query_parts:
            resource += "?" + "&".join(query_parts)
        
        return resource
    
    def _make_request(
        self,
        action: Literal["get", "post", "put", "delete"],
        api_type: str,
        path: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Make a proxied request through FortiManager.
        
        Returns the FortiOS response dict (from the first/only target device).
        """
        resource = self._build_resource(api_type, path, params, vdom)
        
        start_time = time.perf_counter()
        
        # HTTPClientFMG returns raw dict, we wrap it in ProxyResponse
        raw_response = self._fmg.proxy_request(
            action=action,
            resource=resource,
            targets=[self._target],
            payload=data,
            timeout=self._timeout,
        )
        
        self._last_response_time = time.perf_counter() - start_time
        
        # Parse the FMG response
        proxy_response = ProxyResponse.from_fmg_response(raw_response)
        
        # For single-device proxy, return the FortiOS response directly
        if proxy_response.first:
            return proxy_response.first.response
        
        # No response - return empty success
        return {"status": "error", "http_status": 500, "results": []}
    
    def get(
        self,
        api_type: str,
        path: str,
        params: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """GET request through FMG proxy."""
        return self._make_request("get", api_type, path, params, None, vdom, raw_json)
    
    def post(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """POST request through FMG proxy."""
        return self._make_request("post", api_type, path, params, data, vdom, raw_json)
    
    def put(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """PUT request through FMG proxy."""
        return self._make_request("put", api_type, path, params, data, vdom, raw_json)
    
    def delete(
        self,
        api_type: str,
        path: str,
        params: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """DELETE request through FMG proxy."""
        return self._make_request("delete", api_type, path, params, None, vdom, raw_json)


class FortiManagerProxy:
    """
    FortiManager Proxy Client.
    
    Allows making FortiOS API calls to managed devices through FortiManager.
    
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
    
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        port: int = 443,
        verify: bool = True,
        timeout: float = 60.0,
        adom: str | None = None,
        max_retries: int = 3,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
    ):
        """
        Initialize FortiManager proxy client.
        
        Args:
            host: FortiManager hostname or IP
            username: Admin username
            password: Admin password
            port: HTTPS port (default: 443)
            verify: Verify SSL certificate (default: True)
            timeout: Request timeout in seconds (default: 60)
            adom: Default ADOM for proxy requests
            max_retries: Maximum retry attempts on transient failures
            circuit_breaker_threshold: Failures before opening circuit breaker
            circuit_breaker_timeout: Seconds before retrying after circuit opens
        """
        # Build URL from host and port
        url = f"https://{host}:{port}" if port != 443 else f"https://{host}"
        
        self._host = host
        self._port = port
        self._verify = verify
        
        self._session = HTTPClientFMG(
            url=url,
            username=username,
            password=password,
            verify=verify,
            adom=adom,
            connect_timeout=10.0,
            read_timeout=timeout,
            max_retries=max_retries,
            circuit_breaker_threshold=circuit_breaker_threshold,
            circuit_breaker_timeout=circuit_breaker_timeout,
        )
        self._default_adom = adom
    
    @property
    def host(self) -> str:
        """FortiManager hostname."""
        return self._host
    
    @property
    def adom(self) -> str | None:
        """Default ADOM for proxy requests."""
        return self._default_adom
    
    @property
    def verify(self) -> bool:
        """SSL verification setting."""
        return self._verify
    
    @property
    def is_authenticated(self) -> bool:
        """Check if connected to FortiManager."""
        return self._session.is_authenticated
    
    def login(self) -> None:
        """
        Authenticate with FortiManager.
        
        Called automatically on first proxy request if not already authenticated.
        """
        self._session.login()
    
    def logout(self) -> None:
        """End FortiManager session."""
        self._session.logout()
    
    def proxy(
        self,
        device: str,
        adom: str | None = None,
        vdom: str | None = None,
        timeout: int = 60,
    ) -> "ProxiedFortiOS":
        """
        Get a FortiOS client that proxies through this FortiManager.
        
        Args:
            device: Device name in FortiManager
            adom: ADOM name (uses default if not specified)
            vdom: Default VDOM for requests
            timeout: Request timeout in seconds
            
        Returns:
            ProxiedFortiOS client with same API as FortiOS
            
        Example:
            >>> fgt = fmg.proxy(device="firewall-01", adom="production")
            >>> policies = fgt.api.cmdb.firewall.policy.get()
        """
        effective_adom = adom or self._default_adom
        if not effective_adom:
            raise ValueError("ADOM must be specified (either in proxy() or as default)")
        
        target = f"adom/{effective_adom}/device/{device}"
        
        return ProxiedFortiOS(
            fmg_session=self._session,
            target=target,
            vdom=vdom,
            timeout=timeout,
        )
    
    def proxy_group(
        self,
        group: str,
        adom: str | None = None,
        vdom: str | None = None,
        timeout: int = 60,
    ) -> "ProxiedFortiOS":
        """
        Get a FortiOS client that proxies to a device group.
        
        Args:
            group: Device group name in FortiManager
            adom: ADOM name (uses default if not specified)
            vdom: Default VDOM for requests
            timeout: Request timeout in seconds
            
        Returns:
            ProxiedFortiOS client - responses will contain results from all devices
            
        Example:
            >>> fgt = fmg.proxy_group(group="All_FortiGate", adom="production")
            >>> # This will get routes from ALL devices in the group!
            >>> routes = fgt.api.monitor.router.ipv4.get()
        """
        effective_adom = adom or self._default_adom
        if not effective_adom:
            raise ValueError("ADOM must be specified (either in proxy_group() or as default)")
        
        target = f"adom/{effective_adom}/group/{group}"
        
        return ProxiedFortiOS(
            fmg_session=self._session,
            target=target,
            vdom=vdom,
            timeout=timeout,
        )
    
    def close(self) -> None:
        """Close connection to FortiManager."""
        self._session.close()
    
    def __enter__(self) -> "FortiManagerProxy":
        """Context manager entry."""
        self.login()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.close()


class ProxiedFortiOS:
    """
    A FortiOS client that routes all API calls through FortiManager.
    
    This class provides the same `api` interface as the standard FortiOS client,
    but all requests are proxied through FortiManager to the target device(s).
    """
    
    def __init__(
        self,
        fmg_session: FMGSession,
        target: str,
        vdom: str | None = None,
        timeout: int = 60,
    ):
        """
        Initialize proxied FortiOS client.
        
        Args:
            fmg_session: FMG session for making requests
            target: Target path (e.g., "adom/root/device/fw-01")
            vdom: Default VDOM
            timeout: Request timeout
        """
        self._fmg_session = fmg_session
        self._target = target
        self._vdom = vdom
        self._timeout = timeout
        
        # Create the proxy HTTP client
        self._proxy_client = ProxyHTTPClient(
            fmg_session=fmg_session,
            target=target,
            vdom=vdom,
            timeout=timeout,
        )
        
        # Lazy-load the API namespace
        self._api: Any = None
    
    @property
    def api(self):
        """
        FortiOS API namespace.
        
        Provides access to all FortiOS API endpoints, proxied through FortiManager.
        
        Example:
            >>> fgt.api.cmdb.firewall.address.get()
            >>> fgt.api.monitor.router.ipv4.get()
        """
        if self._api is None:
            # Import here to avoid circular imports
            from hfortix_fortios.api import API
            from hfortix_fortios.models import process_response
            import time as _time
            
            # Create a response-processing wrapper (like FortiOS client does)
            proxy_client = self._proxy_client
            
            class ResponseProcessingClient:
                """Wrapper that automatically processes responses with FortiObject."""
                
                def __init__(self, client):
                    self._wrapped_client = client
                
                def get(self, api_type, path, params=None, vdom=None, unwrap_single=False):
                    start_time = _time.perf_counter()
                    result = self._wrapped_client.get(api_type, path, params, vdom, raw_json=True)
                    response_time = _time.perf_counter() - start_time
                    return process_response(result, unwrap_single=unwrap_single, raw_envelope=result, response_time=response_time)
                
                def post(self, api_type, path, data=None, params=None, vdom=None):
                    start_time = _time.perf_counter()
                    result = self._wrapped_client.post(api_type, path, data, params, vdom, raw_json=True)
                    response_time = _time.perf_counter() - start_time
                    return process_response(result, raw_envelope=result, response_time=response_time)
                
                def put(self, api_type, path, data=None, params=None, vdom=None):
                    start_time = _time.perf_counter()
                    result = self._wrapped_client.put(api_type, path, data, params, vdom, raw_json=True)
                    response_time = _time.perf_counter() - start_time
                    return process_response(result, raw_envelope=result, response_time=response_time)
                
                def delete(self, api_type, path, params=None, vdom=None):
                    start_time = _time.perf_counter()
                    result = self._wrapped_client.delete(api_type, path, params, vdom, raw_json=True)
                    response_time = _time.perf_counter() - start_time
                    return process_response(result, raw_envelope=result, response_time=response_time)
                
                def __getattr__(self, name):
                    return getattr(self._wrapped_client, name)
            
            from typing import cast
            from hfortix_core.http.interface import IHTTPClient
            
            wrapped_client = cast(IHTTPClient, ResponseProcessingClient(proxy_client))
            self._api = API(wrapped_client)
        
        return self._api
    
    @property
    def target(self) -> str:
        """Target device/group path."""
        return self._target
    
    @property
    def vdom(self) -> str | None:
        """Default VDOM."""
        return self._vdom

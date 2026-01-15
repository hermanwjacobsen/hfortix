"""Type stubs for FortiManager HTTP Client."""

from typing import Any, Literal, Optional

from .base import BaseHTTPClient


class HTTPClientFMG(BaseHTTPClient):
    """
    HTTP client for FortiManager JSON-RPC API.
    
    Provides session-based authentication and JSON-RPC request handling
    while reusing the retry logic, circuit breaker, connection pooling,
    and statistics from BaseHTTPClient.
    """
    
    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        verify: bool = True,
        adom: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 60.0,
        max_connections: int = 100,
        max_keepalive_connections: int = 20,
        adaptive_retry: bool = False,
        retry_strategy: str = "exponential",
        retry_jitter: bool = False,
    ) -> None: ...
    
    @property
    def jsonrpc_url(self) -> str: ...
    
    @property
    def is_authenticated(self) -> bool: ...
    
    @property
    def adom(self) -> str | None: ...
    
    def login(self) -> None: ...
    
    def logout(self) -> None: ...
    
    def execute(
        self,
        method: Literal["exec", "get", "set", "add", "update", "delete"],
        params: list[dict[str, Any]],
        verbose: int = 1,
    ) -> dict[str, Any]: ...
    
    def proxy_request(
        self,
        action: Literal["get", "post", "put", "delete"],
        resource: str,
        targets: list[str],
        payload: dict[str, Any] | None = None,
        timeout: int = 60,
    ) -> dict[str, Any]: ...
    
    def close(self) -> None: ...
    
    def get_health_metrics(self) -> dict[str, Any]: ...
    
    def get_connection_stats(self) -> dict[str, Any]: ...
    
    def __enter__(self) -> "HTTPClientFMG": ...
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

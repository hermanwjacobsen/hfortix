"""Type stubs for hfortix_fortios.client module."""

from __future__ import annotations

from typing import Any, Literal, Optional

from hfortix_core.http.interface import IHTTPClient
from hfortix_fortios.api import API

class FortiOS:
    """FortiOS REST API Client.

    All endpoint methods return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"] 
    - Convert to dict: response.dict or response.json
    - Get raw response: response.raw
    """

    def __init__(
        self,
        host: str,
        token: str | None = None,
        *,
        username: str | None = None,
        password: str | None = None,
        port: int = 443,
        verify: bool = True,
        timeout: float = 30.0,
        vdom: str | None = None,
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
        http_client: IHTTPClient | None = None,
    ) -> None:
        """
        Initialize FortiOS client.

        Args:
            host: FortiGate hostname or IP address
            token: API token for authentication
            username: Username for username/password auth (alternative to token)
            password: Password for username/password auth
            port: HTTPS port (default: 443)
            verify: Verify SSL certificate (default: True)
            timeout: Request timeout in seconds (default: 30.0)
            vdom: Default VDOM for all requests
            error_mode: How to handle errors - "raise", "return", or "print"
            error_format: Error message format - "detailed", "simple", or "code_only"
            http_client: Custom HTTP client instance (optional)
        """
        ...

    @staticmethod
    def _validate_credentials(
        token: str | None,
        username: str | None,
        password: str | None,
    ) -> None: ...

    @property
    def api(self) -> API: ...
    @property
    def host(self) -> Optional[str]: ...
    @property
    def port(self) -> Optional[int]: ...
    @property
    def vdom(self) -> Optional[str]: ...
    @property
    def error_mode(self) -> Literal["raise", "return", "print"]: ...
    @property
    def error_format(self) -> Literal["detailed", "simple", "code_only"]: ...
    @property
    def connection_stats(self) -> dict[str, Any]: ...
    @property
    def last_request(self) -> dict[str, Any] | None: ...
    def get_connection_stats(self) -> dict[str, Any]: ...
    def get_write_operations(self) -> list[dict[str, Any]]: ...
    def get_operations(self) -> list[dict[str, Any]]: ...
    def get_retry_stats(self) -> dict[str, Any]: ...
    def get_circuit_breaker_state(self) -> dict[str, Any]: ...
    def get_health_metrics(self) -> dict[str, Any]: ...
    def export_audit_logs(
        self,
        filepath: Optional[str] = None,
        format: str = "json",
        filter_method: Optional[str] = None,
        filter_api_type: Optional[str] = None,
        since: Optional[str] = None,
    ) -> Optional[str]: ...
    def request(
        self,
        config: dict[str, Any],
    ) -> Any: ...
    def close(self) -> None: ...
    async def aclose(self) -> None: ...
    def __enter__(self) -> FortiOS: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    async def __aenter__(self) -> FortiOS: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

"""Type stubs for hfortix_fortios.client module."""

from __future__ import annotations

from typing import Any, Literal, Optional, Union, overload

from hfortix_core.http.interface import IHTTPClient
from hfortix_core.audit import AuditHandler
from hfortix_fortios.api import API

class FortiOS:
    """FortiOS REST API Client.

    All endpoint methods return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"] 
    - Convert to dict: response.dict or response.json
    - Get raw response: response.raw
    """

    @overload
    def __init__(
        self,
        host: str | None = None,
        token: str | None = None,
        *,
        username: str | None = None,
        password: str | None = None,
        client: IHTTPClient | None = None,
        mode: Literal["sync"] = "sync",
        verify: bool = True,
        vdom: str | None = None,
        port: int | None = None,
        debug: str | bool | None = None,
        debug_options: dict[str, Any] | None = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        user_agent: str | None = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 10,
        max_keepalive_connections: int = 5,
        session_idle_timeout: int | float | None = 300,
        read_only: bool = False,
        track_operations: bool = False,
        adaptive_retry: bool = False,
        retry_strategy: Literal["exponential", "linear"] = "exponential",
        retry_jitter: bool = False,
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
        audit_handler: AuditHandler | None = None,
        audit_callback: Any | None = None,
        user_context: dict[str, Any] | None = None,
        trace_id: str | None = None,
    ) -> None:
        """Initialize sync FortiOS client."""
        ...

    @overload
    def __init__(
        self,
        host: str | None = None,
        token: str | None = None,
        *,
        username: str | None = None,
        password: str | None = None,
        client: IHTTPClient | None = None,
        mode: Literal["async"],
        verify: bool = True,
        vdom: str | None = None,
        port: int | None = None,
        debug: str | bool | None = None,
        debug_options: dict[str, Any] | None = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        user_agent: str | None = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 10,
        max_keepalive_connections: int = 5,
        session_idle_timeout: int | float | None = 300,
        read_only: bool = False,
        track_operations: bool = False,
        adaptive_retry: bool = False,
        retry_strategy: Literal["exponential", "linear"] = "exponential",
        retry_jitter: bool = False,
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
        audit_handler: AuditHandler | None = None,
        audit_callback: Any | None = None,
        user_context: dict[str, Any] | None = None,
        trace_id: str | None = None,
    ) -> None:
        """Initialize async FortiOS client."""
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

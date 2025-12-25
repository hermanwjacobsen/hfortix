from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, Any, Literal, Optional, Union, cast, overload

from .api import API
from .http_client import HTTPClient
from .http_client_interface import IHTTPClient

if TYPE_CHECKING:
    pass

__all__ = ["FortiOS"]


class FirewallNamespace:
    """Namespace for firewall convenience wrappers."""

    def __init__(self, fortios_instance: "FortiOS"):
        """Initialize with reference to FortiOS instance."""
        from .firewall import (
            FirewallPolicy,
            IPMACBindingSetting,
            IPMACBindingTable,
            ScheduleGroup,
            ScheduleOnetime,
            ScheduleRecurring,
        )

        self.policy = FirewallPolicy(fortios_instance)
        self.ipmac_binding_setting = IPMACBindingSetting(fortios_instance)
        self.ipmac_binding_table = IPMACBindingTable(fortios_instance)
        self.schedule_recurring = ScheduleRecurring(fortios_instance)
        self.schedule_onetime = ScheduleOnetime(fortios_instance)
        self.schedule_group = ScheduleGroup(fortios_instance)


class FortiOS:
    """
    FortiOS REST API Client

    Python client for interacting with Fortinet FortiGate firewalls via REST
    API.
    Supports configuration management (CMDB), monitoring, logging, and
    services.

    This client uses token-based authentication and provides a stateless
    interface
    to FortiOS devices. No login/logout required - just initialize with your
    token
    and start making API calls.

    Main API categories:
        - api.cmdb: Configuration Management Database (firewall policies,
        objects, etc.)
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

    # Type overloads for better IDE support
    @overload
    def __init__(
        self,
        host: Optional[str] = None,
        token: Optional[str] = None,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client: Optional[IHTTPClient] = None,
        mode: Literal["sync"] = "sync",
        verify: bool = True,
        vdom: Optional[str] = None,
        port: Optional[int] = None,
        debug: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 10,
        max_keepalive_connections: int = 5,
        session_idle_timeout: Union[int, float, None] = 300,
        read_only: bool = False,
        track_operations: bool = False,
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
    ) -> None:
        """Synchronous FortiOS client (default)"""
        ...

    @overload
    def __init__(
        self,
        host: Optional[str] = None,
        token: Optional[str] = None,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client: Optional[IHTTPClient] = None,
        mode: Literal["async"],
        verify: bool = True,
        vdom: Optional[str] = None,
        port: Optional[int] = None,
        debug: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 10,
        max_keepalive_connections: int = 5,
        session_idle_timeout: Union[int, float, None] = 300,
        read_only: bool = False,
        track_operations: bool = False,
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
    ) -> None:
        """Asynchronous FortiOS client"""
        ...

    def __init__(
        self,
        host: Optional[str] = None,
        token: Optional[str] = None,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None,
        client: Optional[IHTTPClient] = None,
        mode: Literal["sync", "async"] = "sync",
        verify: bool = True,
        vdom: Optional[str] = None,
        port: Optional[int] = None,
        debug: Optional[str] = None,
        max_retries: int = 3,
        connect_timeout: float = 10.0,
        read_timeout: float = 300.0,
        user_agent: Optional[str] = None,
        circuit_breaker_threshold: int = 10,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_auto_retry: bool = False,
        circuit_breaker_max_retries: int = 3,
        circuit_breaker_retry_delay: float = 5.0,
        max_connections: int = 10,
        max_keepalive_connections: int = 5,
        session_idle_timeout: Union[int, float, None] = 300,
        read_only: bool = False,
        track_operations: bool = False,
        adaptive_retry: bool = False,
        error_mode: Literal["raise", "return", "print"] = "raise",
        error_format: Literal["detailed", "simple", "code_only"] = "detailed",
    ) -> None:
        """
        Initialize FortiOS API client (sync or async mode)

        Supports two authentication methods:
        1. API Token authentication (stateless, recommended for production)
        2. Username/Password authentication (session-based, requires
        login/logout)

        Args:
            host: FortiGate IP/hostname (e.g., "192.0.2.10" or
            "fortigate.example.com")
                  Not required if providing a custom client
            token: API token for authentication (mutually exclusive with
            username/password)
                   Not required if providing a custom client or using
                   username/password
            username: Username for password authentication (must be used with
            password)
                      Mutually exclusive with token
            password: Password for username authentication (must be used with
            username)
                      Mutually exclusive with token
            client: Optional custom HTTP client implementing IHTTPClient
            protocol
                   If provided, host/token/verify/etc. are ignored and the
                   custom client is used
                   Allows for custom authentication, proxying, caching, etc.
            mode: Client mode - 'sync' (default) or 'async'
                 - 'sync': Traditional synchronous API calls
                 - 'async': Asynchronous API calls with async/await
                 Ignored if custom client is provided
            verify: Verify SSL certificates (default: True, recommended for
            production)
            vdom: Virtual domain (default: None = FortiGate's default VDOM)
            port: HTTPS port (default: None = use 443, or specify custom port
            like 8443)
            debug: Logging level for this instance ('debug', 'info', 'warning',
            'error', 'off')
                   If not specified, uses the global log level set via
                   hfortix.set_log_level()
            max_retries: Maximum number of retry attempts on transient failures
            (default: 3)
            connect_timeout: Timeout for establishing connection in seconds
            (default: 10.0)
            read_timeout: Timeout for reading response in seconds (default:
            300.0)
            user_agent: Custom User-Agent header (default: 'hfortix/{version}')
                       Useful for identifying different applications/teams in
                       FortiGate logs
            circuit_breaker_threshold: Number of consecutive failures before
            opening circuit (default: 10)
            circuit_breaker_timeout: Seconds to wait before transitioning to
            half-open (default: 30.0)
            circuit_breaker_auto_retry: When True, automatically wait and retry
            when circuit breaker
                                       opens instead of raising error
                                       immediately (default: False).
                                       WARNING: Not recommended for test
                                       environments - may cause long delays.
            circuit_breaker_max_retries: Maximum number of auto-retry attempts
            when circuit breaker
                                        opens (default: 3). Only used when
                                        circuit_breaker_auto_retry=True.
            circuit_breaker_retry_delay: Delay in seconds between retry
            attempts when auto-retry enabled (default: 5.0).
                                        This is separate from
                                        circuit_breaker_timeout, which controls
                                        when the circuit transitions from open
                                        to half-open.
            max_connections: Maximum number of connections in the pool
            (default: 10)
                           Conservative default (50% below lowest-performing
                           device tested).
                           Should work for most FortiGate models and network
                           conditions. Most devices
                           serialize API requests internally, so high
                           concurrency doesn't improve
                           throughput. Increase based on performance testing:
                           20 for remote-wan,
                           30 for fast-lan, 60+ for high-performance local
                           deployments.
            max_keepalive_connections: Maximum number of keepalive connections
            (default: 5)
                           Conservative default for connection reuse. If
                           max_keepalive_connections
                           exceeds max_connections, it will be automatically
                           adjusted with a warning.
                           Increase proportionally with max_connections based
                           on your device profile.
            session_idle_timeout: For username/password auth only. Idle timeout
            in seconds before
                       proactively re-authenticating (default: 300 = 5
                       minutes). This should match
                       your FortiGate's 'config system global' ->
                       'remoteauthtimeout' setting.
                       Set to None or False to disable proactive
                       re-authentication.
                       Note: The idle timer resets on each API request.
                       Proactive re-auth triggers
                       when time since *last request* exceeds threshold (not
                       time since login).
                       API token authentication is stateless and doesn't use
                       sessions.
                       **Important**: Proactive re-auth only works when using
                       context manager (with statement).
            read_only: Enable read-only mode - simulate all write operations
            without executing them
                      (default: False). When enabled, POST/PUT/DELETE requests
                      are logged but not
                      sent to FortiGate. Useful for testing, dry-run, CI/CD
                      pipelines, and training.
                      GET requests are executed normally.
            track_operations: Enable operation tracking - maintain audit log of
            all API calls
                            (default: False). When enabled, all requests
                            (GET/POST/PUT/DELETE) are
                            recorded with timestamp, method, URL, and data.
                            Access via get_operations()
                            or get_write_operations(). Useful for debugging,
                            auditing, and documentation.
            adaptive_retry: Enable adaptive retry with backpressure detection
            (default: False).
                          When enabled, monitors response times and adjusts
                          retry delays based on
                          FortiGate health signals (slow responses, 503
                          errors). Increases retry
                          delays when FortiGate is overloaded to prevent
                          cascading failures.
                          Access health metrics via get_health_metrics().
            error_mode: How convenience wrappers handle errors (default:
            "raise").
                       - "raise": Raise exceptions (stops program unless
                       caught with try/except)
                       - "return": Return error dict instead of raising
                       (program always continues)
                       - "log": Log error and return None (program always
                       continues)
                       Can be overridden per method call. This only affects
                       convenience wrappers
                       (e.g., fgt.firewall.policy.create), not direct API
                       calls (e.g., fgt.api.cmdb...).
            error_format: Error message detail level (default: "detailed").
                         - "detailed": Full context with endpoint, parameters,
                         and helpful hints
                         - "simple": Just error message and code
                         - "code_only": Just the error code number
                         Can be overridden per method call. Affects both raised
                         exceptions and
                         returned error dicts depending on error_mode.
                          delays when FortiGate is overloaded to prevent
                          cascading failures.
                          Access health metrics via get_health_metrics().

        Important:
            Username/password authentication still works in FortiOS 7.4.x but
            is removed in
            FortiOS 7.6.x and later. Use API token authentication for
            production deployments.

        Performance Note:
            Most FortiGate devices serialize API requests internally, meaning
            concurrent requests
            don't improve throughput and actually increase response times
            (10-15x slower).
            **Sequential requests are recommended** for most deployments. Use
            async mode only when
            integrating with async frameworks or managing multiple devices in
            parallel.
            Performance testing shows ~5 req/s for most devices, ~30 req/s for
            high-performance
            local deployments. See COMPARATIVE_ANALYSIS.md for detailed
            performance profiles.

        Examples:
            # Token authentication (recommended)
            fgt = FortiOS("fortigate.example.com", token="your_token_here",
            verify=True)
            addresses = fgt.api.cmdb.firewall.address.get("test-host")

            # Username/Password authentication with context manager (sync)
            with FortiOS("192.0.2.10", username="admin", password="password",
            verify=False) as fgt:
                addresses = fgt.api.cmdb.firewall.address.get("test-host")
                # Auto-logout on exit

            # Username/Password authentication with context manager (async)
            async with FortiOS("192.0.2.10", username="admin",
            password="password",
                              mode="async", verify=False) as fgt:
                status = await fgt.api.monitor.system.status.get()
                # Auto-logout on exit

            # Asynchronous mode with token
            fgt = FortiOS("fortigate.example.com", token="your_token_here",
            mode="async")
            addresses = await fgt.api.cmdb.firewall.address.get("test-host")

            # Custom HTTP client
            class MyHTTPClient:
                def get(self, api_type, path, **kwargs):
                    # Custom implementation with company auth, logging, etc.
                    ...
                def post(self, api_type, path, data, **kwargs):
                    ...
                # ... put, delete

            fgt = FortiOS(client=MyHTTPClient())
            addresses = fgt.api.cmdb.firewall.address.get("test-host")

            # Production - with valid SSL certificate
            fgt = FortiOS("fortigate.example.com", token="your_token_here",
            verify=True)

            # Development/Testing - with self-signed certificate (example IP from RFC 5737)  # noqa: E501
            fgt = FortiOS("192.0.2.10", token="your_token_here", verify=False)

            # Environment variables (credentials from environment)
            # Set: export FORTIOS_HOST="192.0.2.10"
            #      export FORTIOS_TOKEN="your_token_here"
            fgt = FortiOS()  # Reads from FORTIOS_HOST, FORTIOS_TOKEN

            # Environment variables with username/password
            # Set: export FORTIOS_HOST="192.0.2.10"
            #      export FORTIOS_USERNAME="admin"
            #      export FORTIOS_PASSWORD="your_password"
            fgt = FortiOS()  # Reads from FORTIOS_HOST, FORTIOS_USERNAME,
            FORTIOS_PASSWORD

            # Custom port
            fgt = FortiOS("192.0.2.10", token="your_token_here", verify=False,
            port=8443)

            # Port in hostname (alternative)
            fgt = FortiOS("192.0.2.10:8443", token="your_token_here",
            verify=False)

            # Enable debug logging for this instance only
            fgt = FortiOS("192.0.2.10", token="your_token_here", verify=False,
            debug='info')

            # Custom timeouts (e.g., slower network)
            fgt = FortiOS("192.0.2.10", token="your_token_here",
            connect_timeout=30.0, read_timeout=600.0)

            # Custom User-Agent for multi-team environments
            fgt = FortiOS("192.0.2.10", token="your_token_here",
            user_agent="BackupScript/2.1.0")

            # Read-only mode for testing (simulates writes without executing)
            fgt = FortiOS("192.0.2.10", token="your_token_here",
            read_only=True)
            fgt.api.cmdb.firewall.address.create(name="test")  # Logged but not
            executed

            # Operation tracking for debugging/auditing
            fgt = FortiOS("192.0.2.10", token="your_token_here",
            track_operations=True)
            fgt.api.cmdb.firewall.address.create(name="test",
            subnet="10.0.0.1/32")
            operations = fgt.get_operations()  # Get all operations
            write_ops = fgt.get_write_operations()  # Only POST/PUT/DELETE
        """
        # Support environment variables for credentials (convenience for end
        # users)
        # Priority: explicit parameters > environment variables
        host = host or os.getenv("FORTIOS_HOST")
        token = token or os.getenv("FORTIOS_TOKEN")
        username = username or os.getenv("FORTIOS_USERNAME")
        password = password or os.getenv("FORTIOS_PASSWORD")

        self._host = host
        self._vdom = vdom
        self._port = port
        self._mode = mode
        self._error_mode: Literal["raise", "return", "print"] = error_mode
        self._error_format: Literal["detailed", "simple", "code_only"] = (
            error_format
        )

        # Validate credentials if not using custom client
        if client is None:
            self._validate_credentials(token, username, password)

        # Set up instance-specific logging if requested
        if debug:
            self._setup_logging(debug)

        # Initialize HTTP client
        self._client: Union[HTTPClient, AsyncHTTPClient, IHTTPClient]

        # If custom client provided, use it directly
        if client is not None:
            self._client = client
        else:
            # Build URL with port handling
            if host:
                # If port is already in host string, use as-is
                if ":" in host:
                    url = f"https://{host}"
                # If explicit port provided, append it
                elif port:
                    url = f"https://{host}:{port}"
                # Otherwise use default (443)
                else:
                    url = f"https://{host}"
            else:
                raise ValueError(
                    "host parameter is required when not providing a custom client"  # noqa: E501
                )

            # Create default client based on mode
            if mode == "async":
                from .http_client_async import AsyncHTTPClient

                self._client = AsyncHTTPClient(
                    url=url,
                    verify=verify,
                    token=token,
                    username=username,
                    password=password,
                    vdom=vdom,
                    max_retries=max_retries,
                    connect_timeout=connect_timeout,
                    read_timeout=read_timeout,
                    user_agent=user_agent,
                    circuit_breaker_threshold=circuit_breaker_threshold,
                    circuit_breaker_timeout=circuit_breaker_timeout,
                    circuit_breaker_auto_retry=circuit_breaker_auto_retry,
                    circuit_breaker_max_retries=circuit_breaker_max_retries,
                    circuit_breaker_retry_delay=circuit_breaker_retry_delay,
                    max_connections=max_connections,
                    max_keepalive_connections=max_keepalive_connections,
                    session_idle_timeout=session_idle_timeout,
                    read_only=read_only,
                    track_operations=track_operations,
                    adaptive_retry=adaptive_retry,
                )
            else:
                self._client = HTTPClient(
                    url=url,
                    verify=verify,
                    token=token,
                    username=username,
                    password=password,
                    vdom=vdom,
                    max_retries=max_retries,
                    connect_timeout=connect_timeout,
                    read_timeout=read_timeout,
                    user_agent=user_agent,
                    circuit_breaker_threshold=circuit_breaker_threshold,
                    circuit_breaker_timeout=circuit_breaker_timeout,
                    circuit_breaker_auto_retry=circuit_breaker_auto_retry,
                    circuit_breaker_max_retries=circuit_breaker_max_retries,
                    circuit_breaker_retry_delay=circuit_breaker_retry_delay,
                    max_connections=max_connections,
                    max_keepalive_connections=max_keepalive_connections,
                    session_idle_timeout=session_idle_timeout,
                    read_only=read_only,
                    track_operations=track_operations,
                    adaptive_retry=adaptive_retry,
                )

        # Initialize API namespace.
        # Store it privately and expose a property so IDEs treat it as a
        # concrete
        # instance attribute (often improves autocomplete ranking vs dunder
        # attrs).
        self._api = API(self._client)

        # Log initialization
        logger = logging.getLogger("hfortix.client")
        logger.info(
            "Initialized FortiOS client for %s (mode=%s)",
            host or "unknown",
            mode,
        )
        if not verify:
            logger.warning(
                "SSL verification disabled - not recommended for production"
            )
        if vdom:
            logger.debug("Using VDOM: %s", vdom)

    def _setup_logging(self, level: str) -> None:
        """Set up logging for this instance"""
        level_map = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "OFF": logging.CRITICAL + 10,
        }

        log_level = level_map.get(level.upper(), logging.WARNING)
        logger = logging.getLogger("hfortix")
        logger.setLevel(log_level)

        # Configure basic logging if not already configured
        if not logging.getLogger().handlers:
            logging.basicConfig(
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

    @staticmethod
    def _validate_credentials(
        token: Optional[str], username: Optional[str], password: Optional[str]
    ) -> None:
        """
        Validate authentication credentials.

        Args:
            token: API token
            username: Username for password auth
            password: Password for username auth

        Raises:
            ValueError: If credentials are invalid or missing
        """
        # Check if any authentication method is provided
        has_token = token is not None and token.strip() != ""
        has_userpass = (
            username is not None
            and username.strip() != ""
            and password is not None
            and password.strip() != ""
        )

        if not has_token and not has_userpass:
            raise ValueError(
                "Authentication required: provide either 'token' or both 'username' and 'password'. "  # noqa: E501
                "Example: FortiOS(host='...', token='your-api-token') or "
                "FortiOS(host='...', username='admin', password='password')"
            )

        # Check for invalid token format (common mistakes)
        if has_token and token is not None:
            # Token should not contain spaces (common copy-paste error)
            if " " in token:
                raise ValueError(
                    "Invalid token format: API tokens should not contain spaces. "  # noqa: E501
                    "Check for copy-paste errors or extra whitespace."
                )

            # Token should meet minimum length (FortiOS tokens are typically
            # 31+ characters)
            # Note: Token length varies by FortiOS version (31-32 chars in
            # older versions, 40+ in newer)
            # We use 25 as a reasonable minimum to catch obviously invalid
            # tokens
            if len(token) < 25:
                raise ValueError(
                    f"Invalid token format: token is too short "
                    f"({len(token)} characters). "
                    "FortiOS API tokens are typically 31+ characters "
                    "(older versions) or 40+ characters (newer versions). "
                    "Ensure you're using a valid API token, not a "
                    "password or placeholder."
                )

            # Token should only contain alphanumeric characters (FortiOS
            # tokens are alphanumeric)
            if not token.replace("-", "").replace("_", "").isalnum():
                raise ValueError(
                    "Invalid token format: API tokens should contain only letters, numbers, "  # noqa: E501
                    "hyphens, and underscores. Check for copy-paste errors."
                )

            # Warn about common placeholder strings
            if token.lower() in [
                "token",
                "api_token",
                "your_token_here",
                "your-api-token",
                "xxx",
                "xxxx",
                "xxxxx",
                "paste_token_here",
            ]:
                raise ValueError(
                    f"Invalid token: '{token}' appears to be a placeholder. "
                    "Please provide a valid API token from your FortiGate device. "  # noqa: E501
                    "Generate one via: System > Administrators > Create New > REST API Admin"  # noqa: E501
                )

        # Check for username without password or vice versa
        if (username and not password) or (password and not username):
            raise ValueError(
                "Username/password authentication requires both 'username' AND 'password'. "  # noqa: E501
                "Provide both parameters or use token authentication instead."
            )

    @property
    def api(self) -> API:
        """
        Primary entry point to FortiOS endpoints (cmdb/monitor/log/service).
        """
        return self._api

    @property
    def firewall(self) -> FirewallNamespace:
        """
        Convenience wrappers for firewall operations.

        Provides simplified syntax for common firewall tasks.

        Example:
            >>> fgt = FortiOS("192.0.2.10", token="...")
            >>> # Create a policy using the convenience wrapper
            >>> fgt.firewall.policy.create(
            ...     name='Allow-Web',
            ...     srcintf='port1',
            ...     dstintf='port2',
            ...     srcaddr='all',
            ...     dstaddr='all',
            ...     service=['HTTP', 'HTTPS'],
            ...     action='accept'
            ... )
        """
        if not hasattr(self, "_firewall"):
            self._firewall = FirewallNamespace(self)
        return self._firewall

    def __dir__(self) -> list[str]:
        """
        Prefer showing `api` and `firewall` early in interactive completion.
        """
        # Start with the default dir() list, then move important attrs to the
        # front.
        names = sorted(set(super().__dir__()))
        priority_attrs = ["api", "firewall"]
        for attr in reversed(priority_attrs):
            if attr in names:
                names.remove(attr)
                names.insert(0, attr)
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

    @property
    def error_mode(self) -> Literal["raise", "return", "print"]:
        """Default error handling mode for convenience wrappers"""
        return self._error_mode

    @property
    def error_format(self) -> Literal["detailed", "simple", "code_only"]:
        """Default error message format for convenience wrappers"""
        return self._error_format

    def get_connection_stats(self) -> dict[str, Any]:
        """
        Get HTTP connection pool statistics and metrics

        Provides insights into connection health, retry behavior, and circuit
        breaker state.
        Useful for monitoring, debugging, and capacity planning.

        Returns:
            Dictionary containing connection statistics:
                - total_requests: Total number of API requests made
                - successful_requests: Number of successful requests
                - failed_requests: Number of failed requests
                - total_retries: Total number of retry attempts
                - success_rate: Percentage of successful requests
                - retry_by_reason: Breakdown of retries by failure reason
                - retry_by_endpoint: Breakdown of retries by endpoint
                - circuit_breaker_state: Current circuit breaker state
                (closed/open/half_open)
                - circuit_breaker_failures: Consecutive failure count
                - last_retry_time: Timestamp of last retry (if any)

        Example:
            >>> fgt = FortiOS("192.0.2.10", token="...")
            >>> stats = fgt.get_connection_stats()
            >>> print(f"Success rate: {stats['success_rate']:.1f}%")
            >>> print(f"Total retries: {stats['total_retries']}")
            >>> print(f"Circuit breaker: {stats['circuit_breaker_state']}")
            >>> if stats['retry_by_reason']:
            ...     print("Retry reasons:")
            ...     for reason, count in stats['retry_by_reason'].items():
            ...         print(f"  {reason}: {count}")

        Note:
            Statistics are collected from the time the FortiOS instance was
            created.
            Use this method to monitor connection health and identify issues.
        """
        return self._client.get_connection_stats()

    def get_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of all API operations (requires track_operations=True)

        Returns list of all operations (GET/POST/PUT/DELETE) with details about
        each request.
        Only available when track_operations=True was passed to FortiOS
        constructor.

        Returns:
            List of operation dictionaries containing:
                - timestamp: ISO 8601 timestamp when operation was executed
                - method: HTTP method (GET/POST/PUT/DELETE)
                - api_type: API type (cmdb/monitor/log/service)
                - path: API endpoint path
                - data: Request payload (for POST/PUT), None for GET/DELETE
                - status_code: HTTP response status code
                - vdom: Virtual domain (if specified)

        Raises:
            RuntimeError: If track_operations was not enabled

        Example:
            >>> fgt = FortiOS("192.0.2.10", token="...", track_operations=True)
            >>> fgt.api.cmdb.firewall.address.create(name="test",
            subnet="10.0.0.1/32")
            >>> fgt.api.cmdb.firewall.policy.update("10", action="deny")
            >>>
            >>> operations = fgt.get_operations()
            >>> for op in operations:
            ...     print(f"{op['timestamp']} {op['method']} {op['path']}")
            2024-12-20T10:30:15Z POST /api/v2/cmdb/firewall/address
            2024-12-20T10:30:16Z PUT /api/v2/cmdb/firewall/policy/10

        Note:
            Use get_write_operations() to filter only write operations
            (POST/PUT/DELETE).
        """
        if not hasattr(self._client, "get_operations"):
            raise RuntimeError(
                "Operation tracking is not enabled. "
                "Initialize FortiOS with track_operations=True to use this feature."  # noqa: E501
            )
        return self._client.get_operations()

    def get_write_operations(self) -> list[dict[str, Any]]:
        """
        Get audit log of write operations only (requires track_operations=True)

        Returns list of only write operations (POST/PUT/DELETE), excluding GET
        requests.
        Only available when track_operations=True was passed to FortiOS
        constructor.

        Returns:
            List of write operation dictionaries (same format as
            get_operations())

        Raises:
            RuntimeError: If track_operations was not enabled

        Example:
            >>> fgt = FortiOS("192.0.2.10", token="...", track_operations=True)
            >>> fgt.api.cmdb.firewall.address.get("test")  # GET - not included
            >>> fgt.api.cmdb.firewall.address.create(name="test2",
            subnet="10.0.0.2/32")  # POST
            >>> fgt.api.cmdb.firewall.address.delete("test")  # DELETE
            >>>
            >>> write_ops = fgt.get_write_operations()
            >>> # Only POST and DELETE are returned, GET is excluded
            >>> for op in write_ops:
            ...     print(f"{op['method']} {op['path']} - {op['data']}")
            POST /api/v2/cmdb/firewall/address - {'name': 'test2', 'subnet':
            '10.0.0.2/32'}
            DELETE /api/v2/cmdb/firewall/address/test - None

        Note:
            Useful for generating change logs, rollback scripts, and audit
            reports.
        """
        if not hasattr(self._client, "get_write_operations"):
            raise RuntimeError(
                "Operation tracking is not enabled. "
                "Initialize FortiOS with track_operations=True to use this feature."  # noqa: E501
            )
        return self._client.get_write_operations()

    def get_health_metrics(self) -> dict[str, Any]:
        """
        Get comprehensive health metrics for HTTP client

        Returns health metrics including:
        - Circuit breaker state and failures
        - Retry statistics by endpoint and reason
        - Response time metrics (if adaptive_retry=True)
        - Endpoint health status (slow vs normal)

        Returns:
            Dictionary containing:
            - circuit_breaker: Circuit breaker state, consecutive failures,
            threshold
            - retry_stats: Total retries, requests, success/failure counts
            - adaptive_retry_enabled: Whether adaptive retry is active
            - response_times: Per-endpoint metrics (avg, min, max, p50, p95) if
            adaptive_retry=True

        Example:
            >>> fgt = FortiOS("192.0.2.10", token="...", adaptive_retry=True)
            >>> # Make some requests
            >>> fgt.api.cmdb.firewall.address.list()
            >>>
            >>> # Check health
            >>> metrics = fgt.get_health_metrics()
            >>> print(f"Circuit state: {metrics['circuit_breaker']['state']}")
            >>> print(f"Total retries:
            {metrics['retry_stats']['total_retries']}")
            >>>
            >>> # Check response times (if adaptive_retry=True)
            >>> if metrics['response_times']:
            ...     for endpoint, stats in metrics['response_times'].items():
            ...         print(f"{endpoint}: avg={stats['avg_ms']}ms,
            slow={stats['is_slow']}")
            Circuit state: closed
            Total retries: 2
            cmdb/firewall/address: avg=245.5ms, slow=False

        Note:
            Response time metrics only available when adaptive_retry=True
        """
        if not hasattr(self._client, "get_health_metrics"):
            # Fallback for custom clients without health metrics
            return {
                "error": "Health metrics not available for this client",
                "circuit_breaker": {},
                "retry_stats": {},
                "adaptive_retry_enabled": False,
            }
        return self._client.get_health_metrics()

    def close(self) -> None:
        """
        Close the HTTP session and release resources

        Optional: Python automatically cleans up when object is destroyed.
        Use this for explicit resource management or in long-running apps.

        Note:
            For async mode, use `await fgt.aclose()` instead.
        """
        if self._mode == "async":
            raise RuntimeError(
                "Cannot use .close() in async mode. Use 'await fgt.aclose()' or 'async with' instead."  # noqa: E501
            )
        # In sync mode, close() returns None, not a coroutine
        # Cast to satisfy mypy since we've already verified we're in sync mode
        cast(None, self._client.close())

    async def aclose(self) -> None:
        """
        Close the async HTTP session and release resources (async mode only)

        This method should be called to properly clean up resources when using
        FortiOS in async mode.
        It ensures that all network connections and sessions are closed.

        Usage:
            - Call `await fgt.aclose()` when you are done with the client in
            async mode.
            - Prefer using the async context manager (`async with`) for
            automatic cleanup.

        Example:
            >>> fgt = FortiOS("192.0.2.10", token="...", mode="async")
            >>> try:
            ...     addresses = await fgt.api.cmdb.firewall.address.list()
            ... finally:
            ...     await fgt.aclose()

        Note:
            Prefer using 'async with' statement for automatic cleanup:
            >>> async with FortiOS("192.0.2.10", token="...", mode="async") as
            fgt:
            ...     addresses = await fgt.api.cmdb.firewall.address.list()
        """
        if self._mode != "async":
            raise RuntimeError("aclose() is only available in async mode")
        if hasattr(self._client, "close") and callable(
            getattr(self._client, "close")
        ):
            result = self._client.close()
            if result is not None:
                await result

    def __enter__(self) -> "FortiOS":
        """Context manager entry (sync mode only)"""
        if self._mode == "async":
            raise RuntimeError(
                "Cannot use 'with' statement in async mode. Use 'async with' instead."  # noqa: E501
            )
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """
        Context manager exit - automatically closes session (sync mode only)
        """
        if self._mode == "async":
            raise RuntimeError(
                "Cannot use 'with' statement in async mode. Use 'async with' instead."  # noqa: E501
            )
        self.close()

    async def __aenter__(self) -> "FortiOS":
        """
        Async context manager entry (async mode only)

        Enters the async context for FortiOS. Use with `async with` to ensure
        proper resource management.

        Returns:
            FortiOS: The async client instance.

        Example:
            >>> async with FortiOS("192.0.2.10", token="...", mode="async") as
            fgt:
            ...     addresses = await fgt.api.cmdb.firewall.address.list()
        """
        if self._mode != "async":
            raise RuntimeError(
                "Cannot use 'async with' statement in sync mode. Use regular 'with' instead."  # noqa: E501
            )
        return self

    async def __aexit__(
        self, exc_type: Any, exc_val: Any, exc_tb: Any
    ) -> bool:
        """
        Async context manager exit - automatically closes session (async mode
        only)

        Ensures that all resources are cleaned up when exiting the async
        context.

        Returns:
            bool: False (exceptions are not suppressed)
        """
        if self._mode != "async":
            raise RuntimeError(
                "Cannot use 'async with' statement in sync mode. Use regular 'with' instead."  # noqa: E501
            )
        await self.aclose()
        return False

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Username/Password Authentication**: Alternative authentication method for FortiOS devices
  - Session-based authentication using username and password (alternative to API tokens)
  - Automatic login on initialization, automatic logout on context manager exit
  - Context manager support for automatic session cleanup: `with FortiOS(username="admin", password="***") as fgt:`
  - Proactive session refresh to prevent idle timeout expiration
  - Configurable session idle timeout (default: 5 minutes, matching FortiGate defaults)
  - Automatic re-authentication on 401 errors if session expires
  - Session tracking with last activity timestamps
  - **⚠️ Deprecation Notice**: Username/password authentication **still works in FortiOS 7.4.x** but is **removed in FortiOS 7.6.x and later**. Fortinet recommends using API token authentication for all new deployments. See [FortiOS 7.4 Release Notes](https://docs.fortinet.com/document/fortigate/7.4.0/fortios-release-notes).
  - **Important**: Proactive re-authentication only works with context manager (`with` statement). Without context manager, you must manually manage login/logout.
  - **Note**: The idle timer resets on each API request. Proactive re-auth triggers when time since *last request* exceeds the threshold (not time since login).
  - Examples:
    ```python
    # Recommended: Context manager (automatic login/logout + proactive re-auth)
    with FortiOS(host="fw", username="admin", password="***") as fgt:
        addresses = fgt.api.cmdb.firewall.address.get()
        # Session automatically refreshed if approaching timeout
        # Auto-logout on exit
    
    # Custom timeout (match your FortiGate's remoteauthtimeout setting)
    with FortiOS(host="fw", username="admin", password="***", 
                 session_idle_timeout=120) as fgt:  # 2 minutes
        # Proactive re-auth at 96 seconds (80% of 120s)
        status = fgt.api.monitor.system.status.get()
    
    # Disable proactive re-authentication
    with FortiOS(host="fw", username="admin", password="***",
                 session_idle_timeout=None) as fgt:
        # Will only re-auth on 401 errors
        addresses = fgt.api.cmdb.firewall.address.get()
    ```
  - Implementation details:
    - Login via POST to `/logincheck` with `secretkey` parameter (FortiOS convention)
    - CSRF token extracted from `ccsrftoken` cookie
    - Session cookies managed automatically by httpx client
    - Logout via POST to `/logout` (clears session, sets cookies to expire in 1976)
    - Proactive re-auth triggered at 80% of idle timeout (before expiration)
    - Fallback re-auth on 401 Unauthorized responses
    - Session timestamps: `_session_created_at`, `_session_last_activity`

## [0.3.15] - 2025-12-20

### Added

- **Async/Await Support**: Full dual-mode support for asynchronous operations
  - Single `FortiOS` class now supports both sync and async modes via `mode` parameter
  - All 750+ API methods work transparently in async mode with `await`
  - All 288 `.exists()` helper methods are async-aware
  - Async context manager support with `async with`
  - Zero breaking changes - existing sync code continues to work
  - Implementation:
    - New `AsyncHTTPClient` class mirroring sync `HTTPClient` with async/await
    - `mode="async"` parameter on `FortiOS.__init__()`
    - Automatic coroutine detection using `inspect.iscoroutine()`
    - Type hints with `@overload` decorators for IDE support
  - Performance: Enables concurrent operations with `asyncio.gather()` for 3x+ speedup
  - See [ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ASYNC_GUIDE.md) for complete documentation

- **Helper Methods**: Added `.exists()` helper method to 288 CMDB endpoints
  - Provides safe existence checking without raising exceptions
  - Returns `True` if object exists, `False` if not found
  - Works transparently in both sync and async modes
  - Available on all endpoints that support full CRUD operations
  - Example (sync): `if fgt.api.cmdb.firewall.address.exists("test-host"): ...`
  - Example (async): `if await fgt.api.cmdb.firewall.address.exists("test-host"): ...`
  - See [HELPER_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/HELPER_METHODS.md) for complete documentation and usage examples

### Changed

- **Code Refactoring**: Eliminated code duplication in HTTP client implementation
  - Created `BaseHTTPClient` base class with shared logic for sync and async clients
  - `HTTPClient` and `AsyncHTTPClient` now inherit from `BaseHTTPClient`
  - Removed 744 lines of duplicated code (35% reduction in HTTP client code)
  - Zero duplication between sync and async implementations
  - Improved maintainability: bug fixes now apply to both sync and async modes automatically
  - Better consistency: retry logic, circuit breaker, and validation identical across modes
  - Enhanced testability: shared logic tested once in base class
  - Implementation:
    - `BaseHTTPClient`: Parameter validation, URL building, retry logic, circuit breaker, statistics
    - `HTTPClient`: Sync-specific HTTP operations (httpx.Client)
    - `AsyncHTTPClient`: Async-specific HTTP operations (httpx.AsyncClient)
  - Created `IHTTPClient` Protocol interface for extensibility
  - Updated 863 endpoint files to use Protocol-based type hints
  - Enables users to provide custom HTTP client implementations

### Fixed

- **Test Fixes**: Fixed certificate/local test helper methods to properly filter by source
  - Updated `test_get_factory_helper()` and `test_get_user_helper()` to use correct filters
  - Added `filter='source==factory'` and `filter='source==user'` parameters
  - All 9 certificate/local tests now pass correctly

### Documentation

- **Async Guide**: Created comprehensive [ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ASYNC_GUIDE.md) documentation
  - Complete async/await usage guide with examples
  - Common patterns: concurrent requests, bulk operations, error handling
  - Migration guide from sync to async
  - Performance comparisons and best practices
  - Advanced usage: rate limiting, timeouts, multiple FortiGates
  - Troubleshooting common async errors
- **API Reference**: Created comprehensive [ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ENDPOINT_METHODS.md) documentation
  - Complete listing of all 857 FortiOS API endpoints
  - Shows available methods (`.get()`, `.post()`, `.put()`, `.delete()`, `.exists()`) for each endpoint
  - Organized by API category (CMDB, LOG, MONITOR, SERVICE)
  - Quick navigation with anchor links to all subcategories
  - Coverage: 561 CMDB endpoints, 19 LOG endpoints, 274 MONITOR endpoints, 3 SERVICE endpoints
- **Helper Methods Guide**: Created detailed [HELPER_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/HELPER_METHODS.md) documentation
  - In-depth guide to the `.exists()` helper method
  - Practical usage examples for common scenarios (idempotent operations, safe deletion, batch processing)
  - Reference table of identifier types for all 288 endpoints with `.exists()`
  - Organized by category with example code snippets
- **README Updates**: Added GitHub links to all documentation references
  - Updated documentation links to point to GitHub repository
  - Added ASYNC_GUIDE.md, ENDPOINT_METHODS.md and HELPER_METHODS.md to main documentation section
  - Updated roadmap to mark async support as completed (v0.3.15)
  - Added async/await to features list
  - Improved discoverability for PyPI users
- **QUICKSTART Updates**: Added async/await section
  - Quick example of async mode usage
  - Link to comprehensive ASYNC_GUIDE.md
  - Updated tips section to mention async for concurrent operations
- **Project Cleanup**: Cleaned up root folder and updated documentation
  - Moved `REFACTORING_PROGRESS.md` and `REFACTORING_RECOMMENDATIONS.md` to `X/docs/project/`
  - Removed `update_endpoints.py` (one-time migration script)
  - Updated `CHANGELOG.md` with comprehensive refactoring details
  - Updated `README.md` to highlight refactored architecture

## [0.3.14] - 2025-12-19

### Fixed

- **Critical**: Fixed httpx dependency in requirements.txt (was incorrectly listing requests/urllib3)
  - Package now correctly declares httpx[http2]>=0.27.0 as dependency
  - Resolves installation issues where wrong HTTP library was installed
- **Build**: Updated MANIFEST.in to reflect moved development docs
  - Commented out CONTRIBUTING.md and DEVELOPMENT.md (moved to development workspace)
  - Prevents build warnings about missing files
- **Type Checking**: Fixed mypy configuration for Python 3.10+ syntax
  - Updated pyproject.toml: python_version = "3.10" (was "3.8")
  - Added httpx module ignore for missing type stubs
  - Fixes compatibility with modern union syntax (str | None)

### Added

- **PEP 561 Compliance**: Full type checker support for hfortix package
  - ✅ `py.typed` marker file included in package
  - ✅ All public APIs have complete type hints
  - ✅ mypy/pyright can now validate user code using hfortix
  - ✅ IDE autocomplete with full type information
  - Benefits: Catch type errors at development time, better developer experience
  - Example: Type checkers now understand `fgt.api.cmdb.firewall.address.get()` returns `dict[str, Any]`
- **Public API**: Added `get_connection_stats()` method to FortiOS class
  - Monitor HTTP connection pool health and performance
  - Track retry statistics by reason and endpoint
  - Access circuit breaker state and failure counts
  - Example: `stats = fgt.get_connection_stats()`
- **Exception Exports**: Exported all 16 exception classes from main hfortix package
  - Complete exception hierarchy now available: `from hfortix import CircuitBreakerOpenError, ...`
  - Added 10 new exception exports: ServiceUnavailableError, CircuitBreakerOpenError, TimeoutError, DuplicateEntryError, EntryInUseError, InvalidValueError, PermissionDeniedError
  - Exported helper functions: get_error_description(), raise_for_status()
  - Exported data structures: FORTIOS_ERROR_CODES, HTTP_STATUS_CODES

### Changed

- **Python Version Requirement**: Updated minimum Python version from 3.8 to 3.10
  - Code uses Python 3.10+ syntax (str | None union types)
  - Updated pyproject.toml: requires-python = ">=3.10"
  - Removed Python 3.8, 3.9 from classifiers
  - Added "Typing :: Typed" classifier for PEP 561 compliance
- **Development Status**: Updated from Alpha (3) to Beta (4)
  - Package metadata now consistently declares Beta status
  - Updated in setup.py, pyproject.toml classifiers
  - Reflects maturity of codebase and API stability
- **Documentation**: Updated API_COVERAGE.md to reflect 100% coverage achievement
  - Changed from "38/77 (49%)" to "77/77 (100%)"
  - Added celebration section for milestone achievement
  - Updated test coverage statistics (226 test files)
- **Documentation**: Removed broken internal development references from README.md
  - Cleaned up references to development workspace content

### Notes

- Version synchronized across setup.py (0.3.14), pyproject.toml (0.3.14), and hfortix/FortiOS/__init__.py (0.3.14)
- All changes are backward compatible
- PEP 561 compliance makes hfortix a first-class typed Python package
- This release prepares the package for broader beta testing

## [Unreleased]

### Added

- **🎉 100% API COVERAGE ACHIEVED** (December 2025) - **Complete FortiOS 7.6.5 implementation!**
  - **CMDB API**: All 37 documented categories (100% coverage)
    - **Refactored**: alertemail, antivirus, application, authentication, automation, casb, certificate, dlp, dnsfilter, emailfilter, firewall, icap, ips, log, monitoring, report, router, rule, system (19 categories)
    - Complete categories: diameter-filter, endpoint-control, ethernet-oam, extension-controller, file-filter, ftp-proxy, sctp-filter, switch-controller, user, videofilter, virtual-patch, voip, vpn, waf, web-proxy, webfilter, wireless-controller, ztna (18 categories)
    - Note: ssh-filter, telemetry-controller, wanopt, extender-controller not yet documented on FNDN
  - **Monitor API**: All 32 documented categories (100% coverage)
    - **Previously implemented**: azure, casb, endpoint-control, extender-controller, extension-controller, firewall (6 categories)
    - **Added in this session**: firmware, fortiguard, fortiview, geoip, ips, license, log, network, registration, router, sdwan, service, switch-controller, system, user, utm, videofilter, virtual-wan, vpn, vpn-certificate, wanopt, web-ui, webcache, webfilter, webproxy, wifi (26 categories)
  - **Log API**: 5 categories (100% coverage) - disk, fortianalyzer, memory, forticloud, search
  - **Service API**: 3 categories (100% coverage) - sniffer, security-rating, system
  - **Total**: 77 of 77 documented categories with 750+ API methods
  - **Generated via unified module generator** with automatic edge case handling
  - **Status**: All endpoints generated, ~50% tested with live FortiGate
  - **Quality**: All follow standardized dual-pattern interface with full type hints

- **Router CMDB Category** - Complete routing protocol configuration support (BETA)
  - Implemented all 26 router endpoints with full CRUD operations
  - Collection endpoints: static, static6, access-list, access-list6, prefix-list, prefix-list6, route-map, policy, policy6, aspath-list, community-list, extcommunity-list, key-chain, auth-path, multicast, multicast6, multicast-flow
  - Singleton endpoints: bgp, ospf, ospf6, rip, ripng, isis, bfd, bfd6, setting
  - Comprehensive test coverage: 22/26 endpoints tested (85%), 100% pass rate
  - **Note:** Singleton endpoints (BGP, OSPF, RIP, etc.) require GET→Modify→PUT pattern for nested objects

### Changed

- **🔄 MAJOR API REFACTORING** (December 2025) - **All 500+ endpoints refactored**
  - **Breaking Change**: Standardized method names across all endpoints
  - **Old API**: `create()`, `update()`, `delete()` - required manual `mkey` parameter handling
  - **New API**: `list()`, `get()`, `create()`, `update()`, `delete()` - RESTful and intuitive
  - **Dual-Pattern Interface**: All `create()` and `update()` methods now support:
    - Dictionary pattern: `create(data_dict={'name': 'x', 'subnet': '10.0.0.0/24'})`
    - Keyword pattern: `create(name='x', subnet='10.0.0.0/24')`
    - Mixed pattern: `create(data_dict=base_config, name='override')`
  - **Benefits**: Cleaner code, better IDE autocomplete, template-friendly, more Pythonic
  - **Migration**: Old code will break - update `create(data)` → `create(data_dict=data)`
  - **Scope**: All 37 CMDB categories + 32 Monitor categories refactored with unified generator
  - **Scope**: 200+ endpoints across 24 CMDB categories refactored
  - **Status**: ~85% complete, router endpoints verified with comprehensive tests

- **Repository Organization** (December 19, 2025)
  - Moved development tools (CONTRIBUTING.md, DEVELOPMENT.md) to development workspace
  - Cleaned up public documentation to focus on user-facing content
  - Simplified README.md contributing section
  - Updated all documentation cross-references

- **Module Naming Improvements** (December 19, 2025)
  - Fixed invalid Python identifiers: renamed `3g_modem` → `modem_3g`, `5g_modem` → `modem_5g`
  - Module classes: `Modem3g`, `Modem5g` with proper attribute access
  - Test files updated to match new naming convention
  - All modem tests now passing

- **Development Workflow** (December 19, 2025)
  - Created unified module generator handling all edge cases automatically
  - Auto-detects digit-prefixed names and sanitizes to valid Python identifiers
  - Auto-adds certificate helper methods for certificate endpoints
  - Generates nested resource classes for complex endpoints
  - Detects read-only endpoints and generates appropriate methods
  - Consolidated all generation tools into single location
  - All new modules follow standardized dual-pattern interface

- **Singleton Endpoint Pattern** - Important behavioral note for routing protocols
  - Routing protocol endpoints (BGP, OSPF, RIP, ISIS, etc.) work differently than other endpoints
  - Unlike firewall addresses or policies, you cannot add/remove individual neighbors or networks
  - Instead, you must retrieve the entire configuration, make changes, and send it back
  - This requires more code than typical CRUD operations (see README examples)
  - **Why?** FortiOS API design - routing configs are single objects with nested lists
  - **Future:** Helper methods like `add_neighbor()`, `remove_neighbor()` are planned to simplify this

## [0.3.13] - 2025-12-17

### Added

- **Custom User-Agent Header** - Identify applications in FortiGate logs
  - Configure via `user_agent` parameter in `FortiOS()` constructor
  - Default: `hfortix/{version}` if not specified
  - Useful for multi-team environments and troubleshooting
  - Shows up in FortiGate admin logs for better visibility
  - Example: `FortiOS(host='...', token='...', user_agent='BackupScript/2.1.0')`

- **New Exception Classes** - Better error handling and type safety
  - `ServiceUnavailableError` - HTTP 503 service unavailable
  - `CircuitBreakerOpenError` - Circuit breaker is open (replaces generic RuntimeError)
  - `TimeoutError` - Request timeout errors
  - More specific exceptions for better error handling

- **Configurable Circuit Breaker** - Customize circuit breaker behavior
  - `circuit_breaker_threshold` - Number of failures before opening (default: 5)
  - `circuit_breaker_timeout` - Seconds before transitioning to half-open (default: 60.0)
  - Configure per FortiGate size/environment
  - Example: `FortiOS(host='...', circuit_breaker_threshold=10, circuit_breaker_timeout=120.0)`

- **Configurable Connection Pool** - Tune connection limits
  - `max_connections` - Maximum connections in pool (default: 100)
  - `max_keepalive_connections` - Maximum keepalive connections (default: 20)
  - Adjust for small embedded FortiGates or large enterprise models
  - Example: `FortiOS(host='...', max_connections=50, max_keepalive_connections=10)`

- **Enhanced Retry Statistics** - More detailed metrics
  - `total_requests` - Total number of requests made
  - `successful_requests` - Number of successful requests
  - `failed_requests` - Number of failed requests
  - `last_retry_time` - Timestamp of last retry
  - `success_rate` - Percentage of successful requests (0-100)
  - Better visibility into client performance

- **Advanced Wildcard Matching** - fnmatch support for endpoint timeouts
  - Supports shell-style patterns: `monitor/*`, `*/status`, `monitor/*/interface`
  - More flexible than simple prefix matching
  - Exact match still takes priority over patterns

### Changed

- **Enhanced Parameter Sanitization** - Security improvement
  - Now sanitizes query parameters in addition to request data
  - Prevents leaking API keys, tokens, passwords in logs
  - Added more sensitive key patterns: `api_key`, `api-key`, `apikey`, `auth`, `authorization`
  - Improves security for production logging

- **Parameter Validation** - Fail fast with clear errors
  - Validates `max_retries` (must be >= 0, warns if > 100)
  - Validates `connect_timeout` and `read_timeout` (must be > 0)
  - Validates `circuit_breaker_threshold` (must be > 0)
  - Validates `max_connections` and `max_keepalive_connections` (must be > 0)
  - Validates `host` parameter is required (no longer accepts None)
  - Better error messages for invalid configurations

- **Code Quality Improvements**
  - Reduced code duplication with `_normalize_path()` helper method
  - Improved type hints for `__exit__()` method
  - Enhanced docstrings with examples
  - Better logging consistency

### Fixed

- **Integer ID Path Encoding** - Fixed URL encoding for numeric IDs
  - `dos_policy.get()`, `dos_policy.update()`, `dos_policy.delete()` - Convert policyid to string before encoding
  - `dos_policy6.get()`, `dos_policy6.update()`, `dos_policy6.delete()` - Convert policyid to string before encoding
  - `ipmacbinding.table.get()`, `ipmacbinding.table.update()`, `ipmacbinding.table.delete()` - Convert seq_num to string before encoding
  - Resolves `TypeError: quote_from_bytes() expected bytes` when using numeric IDs
  - All numeric identifiers are now properly converted to strings for URL path encoding

- **Type Safety** - Fixed type checking errors
  - `host` parameter properly validated (no longer Optional in practice)
  - Better type hints for exception handling
  - Cleaner type checking for HTTPClient initialization

### Technical Details

- **100% backwards compatible** - all existing code works unchanged
- Test coverage: 28 tests (all passing)
- Zero breaking changes - all improvements are additive or internal

## [0.3.13] - 2025-12-17 (if releasing the v0.3.13 from earlier)

### Added

- **Request ID / Correlation Tracking** - Track requests across logs for better debugging
  - Auto-generates short 8-character UUID if not provided
  - Support for custom correlation IDs via `request_id` parameter
  - Request ID appears in all log entries for full traceability
  - Enables distributed tracing across multiple systems

- **Connection Pool Metrics** - Monitor HTTP client health and performance
  - `get_connection_stats()` method returns pool health metrics
  - Track: HTTP/2 status, max connections, circuit breaker state, failures
  - Enable proactive monitoring and alerting
  - Zero performance overhead

- **Circuit Breaker Pattern** - Prevent cascading failures with automatic fail-fast
  - Opens after 5 consecutive failures (configurable)
  - Automatically enters half-open state after 60s timeout
  - Manual reset via `reset_circuit_breaker()` method
  - Clear error messages with time-until-retry
  - Protects downstream services from overload

- **Per-Endpoint Timeout Configuration** - Fine-grained timeout control
  - `configure_endpoint_timeout(pattern, timeout)` for custom timeouts
  - Supports wildcard patterns: `monitor/*`, `log/*/report`
  - Exact match takes priority over wildcard
  - Ideal for slow endpoints (reports, large policy lists)
  - Zero overhead if not configured

- **Structured Logging** - Machine-readable logs with extra fields
  - All log entries include: request_id, method, endpoint, status_code, duration, vdom
  - Compatible with JSON log formatters (Elasticsearch, Splunk, CloudWatch)
  - Enables log aggregation and analysis
  - Better troubleshooting with correlation
  - Same performance as string logging

### Technical Details

- All features are **100% backwards compatible** - no breaking changes
- Comprehensive test coverage: 13 new tests in `test_advanced_features.py`
- Total test suite: 24 tests (4 retry + 7 improvements + 13 advanced)
- Documentation: See `docs/ADVANCED_HTTP_FEATURES.md` for complete usage guide
- Performance: Minimal overhead (~0.001ms per request for circuit breaker)

## [0.3.12] - 2025-12-17

### Changed

- **BREAKING: Migrated from requests to httpx** - Complete HTTP client library migration
  - Replaced `requests` library with modern `httpx` library
  - **HTTP/2 Support Enabled** - Improved performance with connection multiplexing
  - More explicit timeout configuration using `httpx.Timeout` object
  - Connection pooling: 100 max connections, 20 keepalive connections
  - Updated exception handling:
    * `ConnectionError` → `httpx.ConnectError, httpx.NetworkError`
    * `Timeout` → `httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout, httpx.ConnectTimeout`
    * `requests.HTTPError` → `httpx.HTTPStatusError`
  - Response API changes: `response.ok` → `response.is_success`
  - Requires: `httpx[http2]>=0.27.0` (previously `requests>=2.31.0`)
  - **No API Changes**: All 644 endpoint methods work unchanged
  - Better foundation for future async support

### Added

- **Automatic Retry Logic** - HTTPClient now automatically retries failed requests with exponential backoff
  - Retries on transient failures: connection errors, timeouts, rate limits (429), server errors (500, 502, 503, 504)
  - Configurable via `max_retries` parameter (default: 3 attempts)
  - Exponential backoff: 1s, 2s, 4s, 8s (capped at 30s)
  - Respects `Retry-After` header for rate limit responses
  - Detailed retry logging at INFO level
  - Improves reliability in unstable network conditions

- **Context Manager Support** - HTTPClient can now be used with `with` statement
  - Automatically closes client on exit: `with HTTPClient(...) as client:`
  - Ensures proper resource cleanup
  - Implements `__enter__` and `__exit__` methods

- **Enhanced Documentation**
  - Query parameter encoding behavior documented in class docstring
  - Timeout configuration explained with detailed examples
  - Path encoding strategy documented (safe='/%' prevents double-encoding)
  - Binary error response handling documented

### Fixed

- **URL Normalization** - Base URL now has trailing slashes stripped during initialization
  - Prevents potential double-slash issues like `https://host//api/v2/...`
  - Ensures consistent URL construction across all requests
  
- **HTTP Client Path Normalization** - Fixed 404 errors when endpoint methods pass paths with leading slashes
  - HTTPClient now strips leading slashes from paths before URL construction
  - Prevents double-slash URLs (e.g., `/api/v2/monitor//firewall/acl`)
  - Backwards compatible: works with both `"firewall/acl"` and `"/firewall/acl"` path formats
  - Affects `request()` and `get_binary()` methods
  - Resolves `ResourceNotFoundError` for monitor endpoints like `firewall.acl.list()`

- **Path Encoding Implementation** - Paths are now properly URL-encoded
  - Special characters in paths are encoded (e.g., spaces → `%20`, `@` → `%40`)
  - Safe characters: `/` (path separator) and `%` (already-encoded marker)
  - Prevents double-encoding of pre-encoded components
  - Example: `"user@domain"` → `"user%40domain"`

- **Binary Response Error Handling** - Improved error handling for non-JSON responses
  - Added try/except around JSON parsing in `_handle_response_errors()`
  - Falls back to standard HTTP error for binary/HTML error pages
  - Logs response size for debugging
  - Handles proxy/firewall error pages gracefully

- **Rate Limit Handling** - HTTP 429 responses now properly handled with retry logic
  - Respects `Retry-After` header from server
  - Falls back to exponential backoff if header not present
  - Prevents overwhelming servers during rate limiting

## [0.3.11] - 2025-12-17

### Added - December 17, 2025

- **FTP Proxy Category** - FTP proxy configuration (1 endpoint):
  - **explicit** - FTP proxy explicit configuration (GET, PUT)
  - Parameters: status, incoming_port, incoming_ip, outgoing_ip, sec_default_action, server_data_mode
  - SSL/TLS support: ssl, ssl_cert, ssl_dh_bits, ssl_algorithm
  - Singleton endpoint pattern (no POST/DELETE operations)
  - Test coverage: 5 test sections with comprehensive parameter validation

- **Monitor API Categories** - 6 categories implemented (18% coverage):
  - **azure/** - Azure application list monitoring (1 endpoint)
  - **casb/** - SaaS application statistics (1 endpoint)
  - **endpoint-control/** - FortiClient EMS monitoring (7 endpoints):
    - ems-status, ems-status-summary, installer, profile-xml
    - record-list, registration-password, summary
  - **extender-controller/** - FortiExtender status monitoring (1 endpoint)
  - **extension-controller/** - Extension controller status (2 endpoints):
    - extender, fortigate
  - **firewall/** - Firewall monitoring (39 endpoints):
    - Policy statistics (policy, policy6, proxy-policy, security-policy, etc.)
    - Session monitoring with 20+ filter parameters
    - ACL counters (acl, acl6) with clear operations
    - Address objects (address, address6, address-dynamic, address-fqdn)
    - Traffic shapers (per-ip-shaper, shaper, multi-class-shaper)
    - Special endpoints (policy-lookup callable, clearpass-address actions)
    - GTP statistics, health monitoring, load balancing
    - Internet service matching and reputation
    - VIP overlap detection, UUID objects
  - Test coverage: 39 firewall tests with 100% pass rate
  - All endpoints support explicit parameters (no **kwargs)

- **Log Configuration Category** - Complete logging configuration (56 endpoints):
  - Nested object pattern: `fgt.api.cmdb.log.disk.filter.get()`
  - **disk/** - Disk logging (filter, setting)
  - **memory/** - Memory logging (filter, global-setting, setting)
  - **fortianalyzer-cloud/** - FortiAnalyzer Cloud (4 endpoints)
  - **fortianalyzer/** - FortiAnalyzer 1/2/3 servers (12 endpoints total)
  - **fortiguard/** - FortiGuard logging (4 endpoints)
  - **null-device/** - Null device logging (filter, setting)
  - **syslogd/** - Syslog servers 1/2/3/4 (16 endpoints total)
  - **tacacs+accounting/** - TACACS+ accounting 1/2/3 (6 endpoints total)
  - **webtrends/** - WebTrends logging (filter, setting)
  - **Singleton endpoints** - custom-field (CRUD), eventfilter, gui-display, setting, threat-weight
  - Test coverage: 12 test files, 47 test cases (100% pass rate)

- **ICAP Category** - Internet Content Adaptation Protocol (3 endpoints):
  - **profile** - ICAP profiles (30+ parameters)
  - **server** - ICAP server configuration with SSL/TLS support
  - **server-group** - ICAP server groups for load balancing

- **IPS Category** - Intrusion Prevention System (8 endpoints):
  - **custom** - Custom IPS signatures (CRUD)
  - **decoder** - Protocol decoders (CRUD)
  - **global** - Global IPS settings (singleton)
  - **rule** - IPS rules (CRUD)
  - **rule-settings** - IPS rule settings (CRUD)
  - **sensor** - IPS sensors/profiles (CRUD)
  - **settings** - VDOM IPS settings (singleton)
  - **view-map** - IPS view-map configuration (CRUD)

- **Monitoring Category** - System monitoring configuration (1 endpoint):
  - **npu-hpe** - NPU-HPE performance monitoring (3 parameters)

- **Report Category** - Report configuration (2 endpoints):
  - **layout** - Report layouts with CRUD (17 parameters)
  - **setting** - Report settings (5 parameters)

### Changed
- **Module Creation Prompt** - Added nested object pattern documentation
  - Complete examples of intermediate classes
  - Property decorators with lazy loading
  - Usage patterns for nested vs flat endpoints

### Improved
- **API Coverage** - Now at 48% overall (37 of 77 categories):
  - CMDB: 23 of 40 categories (57.5% - all beta)
  - Monitor: 6 of 33 categories (18% - all beta)
  - Log: 5 of 5 categories (100% - all beta)
  - Service: 3 of 3 categories (100% - all beta)
  - Total: 200+ endpoints, 250+ API methods
  - **Note:** All implementations remain in beta until v1.0.0

### Status
- **Beta Release** - All implementations are in beta status:
  - Functional and tested with real FortiGate devices
  - May have incomplete parameter coverage or undiscovered edge cases
  - Production-ready status (v1.0.0) requires comprehensive unit test coverage

### Planned
- Complete CMDB endpoint coverage (23 of 40 categories implemented)
- Monitor endpoints implementation (6 of 33 categories)
- Remaining Monitor categories: system, user, router, vpn, network, etc.
- FortiManager module
- FortiAnalyzer module
- Async support
- CLI tool
- Version 1.0.0: Comprehensive unit tests and production-ready status

## [0.3.10] - 2025-12-16

### Added
- **Configurable Timeouts** - HTTP timeout values are now customizable:
  - `connect_timeout`: Time to wait for connection establishment (default: 10.0 seconds)
  - `read_timeout`: Time to wait for response data (default: 300.0 seconds)
  - Configurable via `FortiOS()` constructor parameters
  - Useful for slow networks, international connections, or large operations
  - `max_retries`: Parameter added for future retry mechanism (default: 3)
- **URL Encoding Helper** - Centralized URL encoding for special characters:
  - New `encode_path_component()` function in `http_client.py`
  - Automatically encodes special characters in object names: `/`, `@`, `:`, spaces, etc.
  - Applied to all 145 CMDB endpoint files (84 path variables encoded)
  - Prevents URL parsing errors when object names contain special characters

### Fixed
- **URL Encoding for Special Characters** - Object names with special characters now work correctly:
  - Fixed issue where objects with `/` in names (e.g., `Test_NET_192.0.2.0/24`) caused 404 errors
  - Special characters are now properly encoded: `/` → `%2F`, `@` → `%40`, `:` → `%3A`, space → `%20`
  - Applies to all API operations: get, create, update, delete
  - Implemented as reusable helper function to avoid code duplication
  - Covers all path variables: `name`, `mkey`, `policyid`, `seq_num`, `member`

## [0.3.9] - 2025-12-16

### Added
- **raw_json Parameter** (100% Coverage) - All API methods now support raw_json parameter:
  - Default behavior: Returns just the results data
  - With `raw_json=True`: Returns complete API response with status codes, metadata
  - Coverage: 45+ methods across all CMDB, Log, and Service endpoints
  - Enables access to `http_status`, `status`, `serial`, `version`, `build` fields

- **Logging System** (Complete) - Comprehensive logging framework:
  - Global control: `hfortix.set_log_level('DEBUG'|'INFO'|'WARNING'|'ERROR'|'OFF')`
  - Per-instance control: `FortiOS(debug='info')`
  - 5 log levels with automatic sensitive data sanitization
  - Hierarchical loggers (`hfortix.http`, `hfortix.client`)
  - Request/response logging with timing information
  - Replaced all print() statements with proper logging

### Changed
- **Code Quality** - Applied comprehensive formatting and linting:
  - Black formatter applied to all 195 files (100% PEP 8 compliance)
  - isort applied to organize imports (86 files updated)
  - flake8 checks passed with max-complexity=10
  - All type hints verified
  - Removed all print() statements in production code (replaced with logging)

### Fixed
- **Bug Fixes** - Fixed multiple undefined variable errors:
  - `antivirus/profile.py`: Fixed 2 instances of undefined 'data' variable (lines 265, 451)
  - `certificate` helpers: Added raw_json parameter to import_p12() and other helper methods
  - `DoS Policy`: Fixed interface_data variable bugs in dos_policy.py and dos_policy6.py
  - `firewall` access-proxy: Fixed raw_json parameter placement in 6 files
  - Multiple service/shaper/ssh files: Fixed data→payload_dict variable name consistency
  
- **Test Fixes** - Updated test files to use raw_json=True where needed:
  - Fixed 159 test files to properly check API responses
  - Updated payload structures in multiple test files
  - Fixed syntax errors in certificate and firewall tests

## [0.3.8] - 2025-12-16

### Added
- **Dual-Pattern Interface** (100% Complete) - All 43 create/update methods now support:
  - Dictionary pattern: `create(data_dict={'name': 'x', 'param': 'y'})`
  - Keyword pattern: `create(name='x', param='y')`
  - Mixed pattern: `create(data_dict=base, name='override')`
  - Coverage: 38 CMDB endpoints + 5 Service methods

### Changed
- **Documentation**: Updated all docs with dual-pattern examples
  - README.md, QUICKSTART.md with usage examples

### Fixed
- `extension_controller`: Fixed fortigate_profile registration
- `firewall.ssl_setting`: Added missing typing imports
- `firewall.vendor_mac_summary`: Added get() method for singleton endpoint
- Test fixes for alertemail and proxy_addrgrp

## [0.3.7] - 2025-12-16

### Improved
- Packaging/layout cleanup to align with the canonical `hfortix/` package structure
- Additional FortiOS v2 endpoint modules (log/service/cmdb expansions)

## [0.3.6] - 2025-12-15

### Improved - IDE Autocomplete Experience 🎯

**Note:** This is an alpha release with internal refactoring for better developer experience.

#### Hidden Internal Methods for Cleaner Autocomplete
- **Generic CRUD methods renamed** - Methods moved to underscore prefix:
  - `cmdb.get()` → `cmdb._get()` (escape hatch for unmapped endpoints)
  - `cmdb.post()` → `cmdb._post()`
  - `cmdb.put()` → `cmdb._put()`
  - `cmdb.delete()` → `cmdb._delete()`
  - Similar changes for log, monitor, service modules
- **Benefit:** IDE now shows only endpoint-specific methods (create, update, list, etc.)
- **Migration:** If you use generic methods directly, add underscore prefix

#### Hidden Internal Client Attributes
- **Client internals renamed** - FortiOS client implementation details:
  - `fgt.session` → `fgt._session`
  - `fgt.url` → `fgt._url`
  - `fgt.verify` → `fgt._verify`
- **Public attributes unchanged:** `host`, `port`, `vdom`, `cmdb`, `monitor`, `log`, `service`
- **Benefit:** Cleaner autocomplete showing only user-facing API

#### Hidden Lazy-Loaded Property Cache
- **Firewall lazy loading internals** - Changed cache naming to double underscore
- **Affects:** 11 firewall endpoints (dos_policy, address, addrgrp, access_proxy, etc.)
- **Benefit:** IDE no longer shows internal cached attributes

### Added
- **`__all__` exports** - Explicit control over public API in all modules
- Better documentation and import suggestions

### Technical Details
- 79+ endpoint files updated to use underscore methods internally
- Follows Python naming conventions (single _ = internal, double __ = private)
- All endpoint-specific methods work as before (no breaking changes)
- All tests passing (8/8 for address, access_proxy)

## [0.3.5] - 2025-12-15

### Improved - IDE Autocomplete & Type Hints ✨

#### Developer Experience Enhancements
- **Added PEP 561 support** - Created `FortiOS/py.typed` marker file for better IDE type checking
- **Enhanced type hints** - Added explicit type annotations to all API helper classes
  - `self.cmdb: CMDB` - Full autocomplete for CMDB endpoints
  - `self.firewall: Firewall` - Full autocomplete for firewall endpoints
  - All 16 CMDB categories now have proper type hints
- **Improved `__all__` exports** - Better module discovery and import suggestions
- **Updated setup.py** - Added `package_data` for py.typed and "Typing :: Typed" classifier
- **Fixed duplicate assignments** - Removed redundant initialization in CMDB `__init__.py`

#### Documentation Improvements
- Added comprehensive docstrings explaining API helper class attributes
- Clarified purpose of generic methods (advanced/fallback usage)
- Better examples in class docstrings

### Technical Details
- Type hints now work correctly in VS Code, PyCharm, and other PEP 561-compliant IDEs
- Autocomplete shows all available endpoints when typing `fgt.api.cmdb.firewall.`
- Method signatures display parameter types and return types
- No breaking changes - fully backward compatible

## [0.3.4] - 2025-12-15

### Documentation - Unified Import Syntax 📚

#### Updated All Documentation
- **README.md** - Changed all examples to use `from hfortix import FortiOS`
- **QUICKSTART.md** - Updated import patterns and all code examples
- **Added PyPI badges** - Version, Python 3.8+, MIT license
- **Status updates** - FortiOS "✅ Active", FortiManager/FortiAnalyzer "⏸️ Planned"

### Technical Details
- All documentation now reflects the unified package import structure
- Installation instructions prioritize PyPI method
- 190 insertions, 78 deletions across documentation files

## [0.3.3] - 2025-12-15

### Added - Unified Package Import Structure 📦

#### Package Restructuring
- **Created `hfortix.py`** - Main module for unified imports
- **Enable `from hfortix import FortiOS`** - Clean import syntax
- **Backward compatible** - Old imports still work
- **Updated `__init__.py`** - Changed from relative to absolute imports

### Technical Details
- Added `py_modules=['hfortix', 'exceptions', 'exceptions_forti']` to setup.py
- Package now supports both import styles:
  - Recommended: `from hfortix import FortiOS`
  - Also works: `from FortiOS import FortiOS`

## [0.3.2] - 2025-12-15

### Fixed - Package Distribution 🔧

#### Resolved Import Errors
- **Fixed ModuleNotFoundError** - Added root-level modules to package
- **Updated setup.py** - Added `py_modules` configuration
- **Included exceptions modules** - Both `exceptions.py` and `exceptions_forti.py` now in package

### Technical Details
- Root-level Python modules now properly included in wheel and sdist
- No code changes needed - pure packaging fix

## [0.3.1] - 2025-12-15

### Fixed - Import Error Handling 🛠️

#### Exception Module Imports
- **Added fallback imports** - Better handling for missing exception modules
- **Enhanced FortiOS/exceptions.py** - Try/except blocks for imports
- **Fallback exceptions defined** - Basic exception classes if imports fail

### Technical Details
- Partial fix for import issues (fully resolved in 0.3.2)

## [0.3.0] - 2025-12-14

### Added - Firewall Flat Endpoints + Sub-categories! 🎉

#### New Flat Firewall Endpoints (6 endpoints)
Implemented DoS protection and access proxy endpoints with simplified API:

- **firewall/DoS-policy** - IPv4 DoS protection policies
  - Full CRUD operations with automatic type conversion
  - Comprehensive anomaly detection (18 types with default thresholds)
  - Simplified API: `interface='port3'` → `{'q_origin_key': 'port3'}`
  - Test coverage: 8/8 tests passing (100%)

- **firewall/DoS-policy6** - IPv6 DoS protection policies
  - Same features as DoS-policy for IPv6
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy** - IPv4 reverse proxy/WAF
  - Full CRUD with 16+ configuration parameters
  - VIP integration (requires type="access-proxy")
  - Server pool multiplexing support
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy6** - IPv6 reverse proxy/WAF
  - Same features as access-proxy for IPv6
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy-ssh-client-cert** - SSH client certificates
  - Certificate-based SSH authentication
  - Permit controls (agent forwarding, port forwarding, PTY, X11, user RC)
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy-virtual-host** - Virtual host configuration
  - Domain/wildcard/regex host matching
  - SSL certificate management with automatic list conversion
  - Test coverage: 8/8 tests passing (100%)

**Total Test Coverage:** 48/48 tests (100% pass rate)

**Key Features:**
- **Simplified API** - Automatic type conversion for better UX
  - String → dict: `'port3'` → `{'q_origin_key': 'port3'}`
  - String list → dict list: `['HTTP']` → `[{'name': 'HTTP'}]`
  - Certificate string → list: `'cert'` → `[{'name': 'cert'}]`
- **Comprehensive Documentation** - Anomaly detection types with thresholds
- **Prerequisites Documented** - VIP types, certificates, CAs
- **Lazy Loading** - @property pattern for optimal performance

#### CMDB Category: Firewall Sub-categories (17 endpoints, 7 sub-categories)
Implemented nested/hierarchical structure for firewall endpoints with lazy-loading pattern:

- **firewall.ipmacbinding** (2 endpoints)
  - `setting` - IP/MAC binding global settings
  - `table` - IP/MAC binding table entries

- **firewall.schedule** (3 endpoints)
  - `group` - Schedule groups
  - `onetime` - One-time schedules
  - `recurring` - Recurring schedules

- **firewall.service** (3 endpoints)
  - `category` - Service categories
  - `custom` - Custom service definitions
  - `group` - Service groups

- **firewall.shaper** (2 endpoints)
  - `per-ip-shaper` - Per-IP traffic shaping
  - `traffic-shaper` - Shared traffic shaping

- **firewall.ssh** (4 endpoints)
  - `host-key` - SSH proxy host public keys
  - `local-ca` - SSH proxy local CA
  - `local-key` - SSH proxy local keys (with PEM format support)
  - `setting` - SSH proxy settings

- **firewall.ssl** (1 endpoint)
  - `setting` - SSL proxy settings (timeout, DH bits, caching)

- **firewall.wildcard-fqdn** (2 endpoints)
  - `custom` - Wildcard FQDN addresses (e.g., *.example.com)
  - `group` - Wildcard FQDN groups

### Technical Improvements
- ✅ Nested API structure: `fgt.api.cmdb.firewall.[subcategory].[endpoint]`
- ✅ Lazy-loading with @property methods
- ✅ Singleton pattern for settings endpoints (results as dict)
- ✅ Collection pattern for list endpoints (results as list)
- ✅ exists() methods with try/except for 404 handling
- ✅ Real SSH key generation for testing (PEM format)
- ✅ Member management for group endpoints
- ✅ 138 comprehensive tests (100% pass rate)

### Documentation
- ✅ Complete module creation guide (1,900+ lines)
- ✅ Documentation generation prompt
- ✅ Comprehensive docstrings with examples for all methods
- ✅ Type hints on all parameters

## [0.2.0] - 2025-12-14

### Added - Major Expansion! 🎉

#### New CMDB Categories (7 categories, 30 endpoints)
- **DLP (Data Loss Prevention)** - 8 endpoints
  - `data-type` - Predefined data type patterns
  - `dictionary` - Custom DLP dictionaries
  - `exact-data-match` - Fingerprinting for exact data matching
  - `filepattern` - File type and pattern matching
  - `label` - Classification labels
  - `profile` - DLP policy profiles
  - `sensor` - DLP sensor configuration
  - `settings` - Global DLP settings

- **DNS Filter** - 2 endpoints
  - `domain-filter` - Custom domain filtering lists
  - `profile` - DNS filtering profiles

- **Email Filter** - 8 endpoints
  - `block-allow-list` - Email sender block/allow lists
  - `bword` - Banned word filtering
  - `dnsbl` - DNS-based blacklist checking
  - `fortishield` - FortiShield spam filtering
  - `iptrust` - Trusted IP addresses
  - `mheader` - Email header filtering rules
  - `options` - Global email filter options
  - `profile` - Email filtering profiles

- **Endpoint Control** - 3 endpoints
  - `fctems` - FortiClient EMS integration
  - `fctems-override` - EMS override configurations
  - `settings` - Endpoint control settings

- **Ethernet OAM** - 1 endpoint
  - `cfm` - Connectivity Fault Management (requires physical hardware)

- **Extension Controller** - 6 endpoints
  - `dataplan` - FortiExtender data plan configuration
  - `extender` - FortiExtender controller settings
  - `extender-profile` - FortiExtender profiles
  - `extender-vap` - FortiExtender WiFi VAP
  - `fortigate` - FortiGate controller configuration
  - `fortigate-profile` - FortiGate connector profiles

- **File Filter** - 1 endpoint
  - `profile` - File content filtering profiles

### Changed
- **License**: Changed from MIT to Proprietary License with free use
  - Free for personal, educational, and business use
  - Companies can use for internal operations and client services
  - Tech support and MSPs can use in their service offerings
  - **Cannot sell the software itself as a standalone product**
  - Simple rule: Use it freely for your work, just don't sell the software

### Improved
- **CMDB Coverage**: 21 → 51 endpoints (+143% growth!)
- **CMDB Categories**: 7 → 14 categories (+100% growth!)
- All modules follow consistent patterns:
  - `from __future__ import annotations` for modern type hints
  - Comprehensive docstrings with examples
  - Snake_case to hyphen-case parameter conversion
  - Full CRUD operations where applicable
  - **kwargs for flexibility

### Fixed
- Directory naming issues (hyphens → underscores for Python imports)
- Graceful error handling for hardware-dependent features
- Improved test patterns for pre-allocated resource slots
- Better handling of list/dict API responses

### Documentation
- Updated PROJECT_STATUS.md with all new modules
- Updated README with current statistics
- Updated CHANGELOG with detailed release notes
- All modules include comprehensive test files

## [0.1.0] - 2025-12-13

### Added
- Initial release of Fortinet Python SDK
- Modular package architecture supporting FortiOS, FortiManager, FortiAnalyzer
- FortiOS client with token-based authentication
- Comprehensive exception handling system (387 FortiOS error codes)
- CMDB endpoints (Beta - partial coverage):
  - `alertemail` - Email alert settings
  - `antivirus` - Antivirus profiles and settings
  - `application` - Application control (custom, list, group, name)
  - `authentication` - Authentication rules, schemes, and settings
  - `automation` - Automation settings
  - `casb` - CASB (Cloud Access Security Broker) profiles
  - `certificate` - Certificate management (CA, CRL, local, remote, HSM)
  - `diameter_filter` - Diameter filter profiles
- Service endpoints (Beta):
  - `sniffer` - Packet capture and analysis
  - `security_rating` - Security Fabric rating
  - `system` - System information and operations
- Log endpoints (Beta):
  - `disk` - Disk-based logging
  - `fortianalyzer` - FortiAnalyzer logging
  - `forticloud` - FortiCloud logging
  - `memory` - Memory-based logging
  - `search` - Log search functionality
- Base exception classes for all Fortinet products
- FortiOS-specific exception classes with detailed error code mapping
- Support for both full package and standalone module installation
- Module availability detection (`get_available_modules()`)
- Version information (`get_version()`)

### Documentation
- Comprehensive README with installation and usage examples
- QUICKSTART guide for rapid onboarding
- Exception hierarchy documentation
- API structure overview
- Common usage patterns and examples

### Infrastructure
- Package distribution setup (setup.py, MANIFEST.in)
- Requirements management (requirements.txt)
- Git ignore configuration
- MIT License

## [0.0.1] - 2025-11-XX

### Added
- Initial project structure
- Basic FortiOS client implementation
- Core exception handling

---

## Version Numbering

- **Major version (X.0.0)**: Incompatible API changes
- **Minor version (0.X.0)**: New features, backward compatible
- **Patch version (0.0.X)**: Bug fixes, backward compatible

## Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes

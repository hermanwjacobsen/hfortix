# HFortix - Fortinet Python SDK

Python client library for Fortinet products including FortiOS, FortiManager, and FortiAnalyzer.

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

## 🎯 Current Status

> **⚠️ BETA STATUS - Version 0.5.76**
>
> - **Current Version**: 0.5.76 (Released - January 15, 2026)
> - **Schema Version**: v1.7.0 (1,348 endpoints with enhanced metadata)
> - **Package Size**: ~30 MB (optimized with MetadataMixin refactoring)
> - **Implementation**: Advanced Features (100% complete) - Production ready!
> - **Install**: `pip install hfortix[fortios]` or `pip install hfortix-fortios`
>
> **📊 Implementation Status:** **All major features complete!** See details below.

**FortiOS 7.6.5 Coverage (Schema v1.7.0 - January 2026):**

- **CMDB API**: 561 endpoints (100% coverage) - Full configuration management ✅ Complete
- **Monitor API**: 490 endpoints (100% coverage) - Complete monitoring capabilities ✅ Complete
- **Log API**: 286 endpoints (100% coverage) - Log query support ✅ Complete  
- **Service API**: 11 endpoints (100% coverage) - Service operations ✅ Complete
- **Overall**: **1,348 total endpoints** - All features implemented 🎉

**Code Generation Status:**

✅ **Completed (100%):**
- ✅ **Schema v1.7.0**: 1,348 endpoints with capabilities, complexity, relationships
- ✅ **Basic API Classes**: 2,129 endpoint files with full CRUD methods
- ✅ **Type Stubs**: 2,129 .pyi files with complete type annotations
- ✅ **Pydantic Models**: Runtime validation models for all endpoints
- ✅ **Capabilities Metadata**: All endpoints expose SUPPORTS_* constants
- ✅ **Action Methods**: move(), clone(), exists() for all endpoints
- ✅ **Type Hints**: Full type annotations with Literal types for enums
- ✅ **Validators**: Validation helper modules with field constraints
- ✅ **Query Parameters**: Enhanced filter, count, start on all CMDB endpoints
- ✅ **Schema Introspection**: Runtime get_schema() method
- ✅ **Docstrings**: Comprehensive documentation with examples
- ✅ **Tests**: Auto-generated test files - all passing ✅

**Overall Progress: 100% Complete** (Production Ready!)
- Schema & Infrastructure: ✅ 100%
- Basic API Generation: ✅ 100%
- Advanced Features (Pydantic, validation, capabilities): ✅ 100%
- IDE Improvements (query params, schema introspection): ✅ 100%
- Documentation: ✅ 100%
- Release: ✅ 100%

**Latest Release:** v0.5.76 - FortiManager Proxy Support, Enhanced Response Properties

**Test Coverage:** **All endpoints tested and passing!** ✅
**Status:** Ready for production use - comprehensive feature set complete!

**🔥 Latest Improvements (January 2026):**

**v0.5.76 - FortiManager Proxy Support & Response Enhancements:**
- 🎯 **FortiManagerProxy**: Route FortiOS API calls through FortiManager!
  - Proxy API requests to managed FortiGate devices
  - Full ADOM and device targeting support
  - Session-based authentication with FortiManager
  - JSON-RPC protocol support for FMG API
- 🔧 **HTTPClientFMG**: New HTTP client for FortiManager in `hfortix_core`
  - Extends BaseHTTPClient with retry/circuit-breaker support
  - Session-based login/logout with token caching
  - Proxy request method for FMG's `/sys/proxy/json` endpoint
- 📦 **ProxiedFortiOS**: FortiOS-like interface through FMG
  - Same API patterns: `proxied_fgt.api.cmdb.firewall.address.get()`
  - Automatic request translation to FMG JSON-RPC format
  - Full response wrapping with timing and metadata
- ⚡ **http_stats property**: Simplified timing access
  - `obj.http_stats` returns `{"http_response_time": 123.5}` (in milliseconds)
- ⏱️ **Response timing properties**: Track API performance
  - `obj.response_time` - Response time in seconds (float)
  - `obj.response_time_ms` - Response time in milliseconds (int)
- 📊 **Explicit envelope properties**: Clear access to API metadata
  - `obj.revision`, `obj.serial`, `obj.build`, `obj.version`
- 🔕 **Silent 404 handling**: `exists()` returns `False` without printing errors

**v0.5.45 - Formatting & Type Improvements:**
- ✨ **fmt module in core**: `from hfortix_core import fmt` - 13 formatting utilities
- 🎯 **Improved to_dict() types**: Better Pylance compatibility with `.get()` method
- 🔄 **Automatic key normalization**: API response keys converted from hyphens to underscores
  - `tcp-portrange` → `tcp_portrange` automatically
- 📦 **Optimized helper files**: 50-80 lines reduced per file using functools.partial

**v0.5.44 - Core Formatting Module:**
- � Moved formatting utilities to `hfortix_core.fmt` for easier access
- 🎯 All 13 functions: `to_list()`, `to_json()`, `to_csv()`, `to_dict()`, `to_table()`, etc.
- 📋 Auto-split for space-delimited strings: `"80 443"` → `['80', '443']`

**v0.5.43 - Enhanced Formatting:**
- ✨ `to_dictlist()` / `to_listdict()` for columnar↔row format conversion
- 📊 `to_table()`, `to_yaml()`, `to_xml()` for various output formats
- 🔧 `to_markdown_table()` for documentation generation

**🔥 Previous Highlights (v0.5.32-v0.5.42):**

- � **Key Normalization**: Automatic hyphen-to-underscore conversion for API responses
- 🎯 **Single Object Returns**: Querying by mkey returns single object, not list
- � **Nested Table Field Wrapping**: Full attribute access on nested objects
- 🛠️ **Enhanced Type Stubs**: Improved overloads for better Pylance type inference
- 📊 **MutationResponse TypedDict**: Type-safe POST/PUT/DELETE responses
- 🔍 **Validation Hints**: Field constraints shown in IDE tooltips
- 🔗 **ENDPOINT RELATIONSHIP DOCUMENTATION**: Enhanced IDE experience with cross-references! (v0.5.11)
- ⚡ See what resources each endpoint depends on (forward dependencies)
- 🔍 Field-level mappings: Know which fields reference which endpoints
- 🎯 RST cross-references: Ctrl+Click to navigate between related endpoints
- 📚 Smart truncation: Top 10 dependencies shown, then "... and X more"
- ✅ All 562 CMDB endpoints include relationship documentation
- 🎨 **LITERAL TYPES FOR IDE AUTOCOMPLETE**: 15,000+ parameters with enum autocomplete! (v0.5.18)
- ⚡ Instant IDE suggestions for all enum fields (action, status, protocol, etc.)
- 🛡️ Type safety: Invalid values caught at type-check time
- 📚 Self-documenting: See all valid options in IDE tooltips
- ✅ 100% backward compatible - no breaking changes
- 🎉 **METADATAMIXIN REFACTORING**: 53% total package size reduction (64 MB → 30 MB)! (v0.5.4)
- ♻️ **CODE DEDUPLICATION**: Eliminated ~160K lines of duplicate metadata methods
- 📦 **OPTIMIZED PACKAGE**: Two-phase optimization (stub separation + mixin refactoring)

**📖 Documentation:**

- **Quick Start Guide**: [QUICKSTART.md](https://github.com/hermanwjacobsen/hfortix/blob/main/QUICKSTART.md) - Getting started guide
- **Full Changelog**: [CHANGELOG.md](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) - Complete version history

**Latest Features (v0.4.3 - January 2, 2026):**

> **✅ PUBLISHED TO PYPI - January 2, 2026**
>
> Version 0.4.3 completes the required field validation integration across all 374 helpers
> and adds comprehensive type safety improvements.
>
> **All packages remain in BETA** until v1.0 with comprehensive unit test coverage.

- ✅ **Required Fields Validation** (v0.4.3):
  - **374 helpers with required field validation** (216 newly integrated)
  - Two-stage validation: required fields → field values (enums, ranges, formats)
  - Schema-based validators automatically derived from FortiOS API schemas
  - Clear error messages identifying missing required fields
  - Automatic null payload handling for all validators
  - See [VALIDATION_GUIDE.md](docs/fortios/VALIDATION_GUIDE.md) for examples

- 🔒 **Type Safety Improvements** (v0.4.3):
  - Fixed all mypy type errors in validator functions
  - Proper type annotations for all `FIELDS_WITH_DEFAULTS` dictionaries
  - All 585 helper files now pass strict type checking
  - Enhanced code quality with PEP8 compliance

- 📚 **Schema Discovery Documentation** (v0.4.3):
  - New [SCHEMA_DISCOVERY.md](docs/fortios/SCHEMA_DISCOVERY.md) guide
  - Documents current capabilities and future runtime schema fetching
  - Complete roadmap for implementing dynamic schema discovery
  - Tested runtime schema fetching with rich field metadata

- 🎯 **Generic request() Method** (v0.4.2):
  - **Zero-Translation API Workflow**: Copy JSON directly from FortiGate GUI API preview
  - Accepts exact JSON format shown in FortiGate GUI when viewing/editing objects
  - Supports all CRUD operations: GET, POST, PUT, DELETE
  - Perfect for rapid API testing and prototyping
  - Example:
    ```python
    # Copy this directly from FortiGate GUI API preview
    config = {
        "method": "POST",
        "url": "/api/v2/cmdb/firewall/address",
        "params": {"vdom": "test"},
        "data": {"name": "host1", "subnet": "10.0.0.1/32"}
    }
    result = fgt.request(config)
    ```
  - See [REQUEST_METHOD_GUIDE.md](REQUEST_METHOD_GUIDE.md) for complete guide

- 📦 **Modular Package Structure**: Major architectural improvement with split packages (v0.4.0)
  - **hfortix-core**: Core exceptions and HTTP client framework (sync/async)
  - **hfortix-fortios**: FortiOS/FortiGate client, API endpoints, and firewall helpers
  - **hfortix** (meta-package): Minimal core install, optional extras for products
  - New import options: `from hfortix_fortios import FortiOS`
  - Install options:
    - `pip install hfortix` - Core only (minimal)
    - `pip install hfortix[fortios]` - Core + FortiOS
    - `pip install hfortix[all]` - Everything
    - `pip install hfortix-fortios` - Just FortiOS (includes core)

- 🔧 **Code Quality Improvements** (v0.4.0-v0.4.1):
  - Fixed all E501 line length errors
  - Fixed mypy type errors with namespace package imports
  - Enhanced pre-commit configuration for auto-generated code
  - All linters, type checkers, and pre-commit hooks passing
  - Updated pre-release checks to work with split package architecture

- ⚡ **Smart Retry & Circuit Breaker Enhancements** (v0.4.1):
  - **Retry Strategy Selection**: Choose between exponential or linear backoff
    - `retry_strategy="exponential"` (default) - 1s, 2s, 4s, 8s, 16s, 30s (best for transient failures)
    - `retry_strategy="linear"` - 1s, 2s, 3s, 4s, 5s (best for rate limiting scenarios)
  - **Jitter Support**: Add random variation to prevent thundering herd
    - `retry_jitter=True` - Adds 0-25% random variation to retry delays
    - Prevents multiple clients from retrying simultaneously
  - **Public Telemetry APIs**: Monitor retry patterns and circuit health
    - `fgt.get_retry_stats()` - Track retries by endpoint and reason
    - `fgt.get_circuit_breaker_state()` - Monitor circuit breaker health
    - `fgt.get_health_metrics()` - Comprehensive health view
  - **Audit Log Export**: Batch export for compliance reporting
    - `fgt.export_audit_logs()` - Export to JSON/CSV/text format
    - Filter by method, API type, or timestamp
    - Essential for SOC 2, HIPAA, PCI-DSS compliance
  - See `examples/retry_strategy_demo.py` for comprehensive examples

- � **Enhanced Debugging & Observability** (v0.4.1):
  - **Connection Pool Monitoring**: Fixed hardcoded values bug
    - `fgt.connection_stats` - Real-time pool metrics (max_connections, active_requests, pool_exhaustion_count)
    - Track connection exhaustion with timestamps
    - Essential for capacity planning and performance tuning
  - **Request Inspection**: Debug slow or failed requests
    - `fgt.last_request` - Detailed info about last API call (method, endpoint, response_time_ms, status_code)
    - `inspect_last_request()` method on HTTP clients
    - Identify performance bottlenecks quickly
  - **Enhanced Debug Mode**: Simplified debugging
    - `debug=True` - Quick debug mode (enables DEBUG logging)
    - `debug="INFO"` - Explicit log level control
    - `debug_options` parameter for advanced configuration
  - **DebugSession Context Manager**: Comprehensive session monitoring
    - Capture all requests, timing, and connection stats
    - Auto-calculate aggregate metrics (avg/min/max response times)
    - Print detailed summary on exit
    - Example: `with DebugSession(fgt) as session: ...`
  - **Debug Utilities**: Helper functions for debugging
    - `debug_timer()` - Time operations with context manager
    - `format_request_info()` - Pretty-print request details
    - `format_connection_stats()` - Pretty-print connection stats
    - `print_debug_info()` - Comprehensive debug output
  - **Enhanced Type Hints**: Better IDE support
    - New type stubs (.pyi files) for all clients
    - TypedDict definitions for API responses
    - Improved autocomplete in VS Code, PyCharm
  - **Comprehensive Documentation**:
    - `docs/fortios/DEBUGGING.md` - Complete debugging guide
    - `docs/fortios/RATE_LIMITING.md` - Rate limit handling guide
    - Integration examples for ELK, Splunk, CloudWatch

- 📊 **Enhanced Structured Logging with Multi-Tenant Support** (v0.4.1):
  - **VDOM/ADOM Fields**: Automatic inclusion in all structured logs
    - `vdom` field automatically added for FortiOS Virtual Domain environments
    - `adom` field support ready for future FortiManager/FortiAnalyzer clients
    - Essential for multi-tenant environments and per-customer observability
  - **Consistent Log Context**: All log events include standard fields
    - request_id, method, endpoint, status_code, duration_seconds
    - vdom/adom (when configured)
    - error_type, attempt, max_attempts (for errors/retries)
  - **Multi-Tenant Benefits**:
    - Easy log filtering: `jq '.vdom == "customer_a"' logs.json`
    - Per-tenant metrics and dashboards in ELK/Splunk/Datadog
    - Audit trail isolation by virtual domain
    - Compliance reporting per customer/tenant
  - See `docs/fortios/OBSERVABILITY.md` for complete documentation

**Features from v0.3.39 (December 29, 2025):**

- 🎨 **Complete Service Management Wrappers**: Production-ready wrappers for firewall services
  - **Service Category** (`fgt.firewall.service_category`) - Organize services into categories
  - **Custom Services** (`fgt.firewall.service_custom`) - TCP/UDP/ICMP/IP services with 30+ parameters
  - **Service Groups** (`fgt.firewall.service_group`) - Group services with member management
  - Full parameter support with comprehensive validation
  - Consistent interface: `.create()`, `.get()`, `.update()`, `.delete()`, `.exists()`, `.get_by_name()`, `.rename()`
  - Advanced features: `.add_member()`, `.remove_member()` for groups
  - See `docs/fortios/wrappers/CONVENIENCE_WRAPPERS.md` for complete guide and examples

- 📅 **Enhanced Schedule Wrappers**: Production-ready schedule management
  - **Schedule Onetime** (`fgt.firewall.schedule_onetime`) - One-time schedules with expiration
  - **Schedule Recurring** (`fgt.firewall.schedule_recurring`) - Daily/weekly recurring schedules
  - **Schedule Groups** (`fgt.firewall.schedule_group`) - Group schedules with member management
  - Full CRUD operations with validation
  - Convenience methods: `.clone()`, `.rename()`, `.add_member()`, `.remove_member()`
  - See `docs/fortios/wrappers/SCHEDULE_WRAPPERS.md` for complete guide

- 🔗 **IP/MAC Binding Wrappers**: Complete IP/MAC binding management
  - **Binding Table** (`fgt.firewall.ipmacbinding_table`) - Manage IP/MAC binding entries
  - **Binding Settings** (`fgt.firewall.ipmacbinding_setting`) - Configure binding behavior
  - Full validation: IP addresses, MAC addresses, sequence numbers
  - Convenience methods: `.enable()`, `.disable()`, `.exists()`

- 🚀 **Automated Release Workflow**: New `make release` target for streamlined releases
  - Automated version bumping and CHANGELOG updates
  - Runs all pre-release checks (formatting, linting, type-checking, security)
  - Creates git commit and tag with automatic GitHub push prompt

**Features from v0.3.38 (December 29, 2025):**

- 🚦 **Traffic Shaper Convenience Wrappers**: Production-ready wrappers for traffic shaping
  - **Per-IP Shaper** (`fgt.firewall.shaper_per_ip`) - Bandwidth and session limits per source IP
  - **Traffic Shaper** (`fgt.firewall.traffic_shaper`) - Shared traffic shaper with guaranteed/maximum bandwidth
  - Full parameter support with comprehensive validation
  - ⚠️ **Important:** Rename operations not supported (FortiOS API limitation - name is immutable primary key)
  - See `docs/fortios/wrappers/SHAPER_WRAPPERS.md` for complete guide and examples

**Features from v0.3.34 (December 25, 2025):**

- 📋 **Schedule Convenience Methods**: All schedule types now have consistent convenience methods
  - `get_by_name()` - Get schedule data directly (not full API response)
  - `rename()` - Rename a schedule in one call
  - `clone()` - Clone schedule with optional modifications
  - Response helpers: `get_mkey()`, `is_success()`, `get_results()`
  - Available for: `schedule_onetime`, `schedule_recurring`, `schedule_group`
  - See `SCHEDULE_CONVENIENCE_METHODS.md` and `examples/schedule_convenience_demo.py`

- 🔗 **IP/MAC Binding Convenience Wrapper**: New helper class for firewall IP/MAC binding
  - CRUD operations: `create()`, `update()`, `delete()`, `get()`, `get_all()`
  - Convenience methods: `exists()`, `enable()`, `disable()`
  - Full validation: IP addresses, MAC addresses, status values, name length
  - Comprehensive test suite: `examples/ipmacbinding_test_suite.py` (19 pytest tests)

- � **Circuit Breaker Auto-Retry**: Optional automatic retry when circuit opens
  - New parameters: `circuit_breaker_auto_retry`, `circuit_breaker_max_retries`, `circuit_breaker_retry_delay`
  - Useful for production scripts requiring resilience
  - Fail-fast behavior preserved by default
  - See `examples/circuit_breaker_test.py` for demonstrations

**Features from v0.3.24 (December 24, 2025):**

- 🎯 **Exception Hierarchy & Retry Logic**: Intelligent error handling support
- 🆕 **New Exception Types**: Better error classification
- 📊 **Enhanced Exception Metadata**: Better debugging with request_id and timestamps
- 💡 **Recovery Suggestions**: Built-in error recovery guidance

**Features from v0.3.23 (December 23, 2025):**

- 🐛 **Bug Fixes**: Missing API endpoints and code quality improvements
  - Added `check_addrgrp_exclude_mac_member` monitor endpoint
  - Added `check_port_availability` system endpoint
  - Fixed .gitignore pattern blocking legitimate API files
  - All pre-commit hooks now pass consistently

**Features from v0.3.22 (December 23, 2025):**

- 🎯 **CI/CD Pipeline**: Complete GitHub Actions automation
  - Automated code quality checks (lint, format, type-check, security)
  - PyPI publishing with trusted publishing (no API tokens needed)
  - CodeQL security scanning and dependency review
  - Multi-Python version testing (3.10, 3.11, 3.12)
- 🧹 **Code Quality**: Comprehensive PEP 8 compliance
  - Reformatted 796 files with Black (79-char line limit)
  - Fixed 1000+ flake8 lint errors
  - Proper handling of long lines, imports, and f-strings

**Features from v0.3.19:**

- 🔧 **Type Checking Improvements**: Enhanced type safety and IDE support
  - Cleaned up mypy configuration (removed unnecessary overrides for httpx and requests)
  - Better IDE autocomplete and type checking
  - Zero breaking changes - purely internal improvements

**Features from v0.3.18:**

- ✨ **Extensibility: Custom HTTP Clients**: Support for custom HTTP client implementations
  - `IHTTPClient` Protocol interface for audit logging, caching, testing, custom auth
  - See [examples/custom_http_client_example.py](https://github.com/hermanwjacobsen/hfortix/blob/main/examples/custom_http_client_example.py)
- ✨ **Environment Variables Support**: Load credentials from environment variables
  - Support for `FORTIOS_HOST`, `FORTIOS_TOKEN`, `FORTIOS_USERNAME`, `FORTIOS_PASSWORD`
  - Perfect for CI/CD pipelines and security best practices
- ✨ **Credential Validation**: Comprehensive validation for authentication credentials
  - Validates token format and catches common copy-paste errors
- 🐛 **Test File Naming Fix**: Fixed critical circular import issues
  - Renamed all 354 test files to use `test_` prefix

**Features from v0.3.17:**

- ✨ **Performance Testing API**: Built-in performance testing and optimization
  - New `fgt.api.utils.performance_test()` method for testing your device
  - Validates connection pool settings automatically
  - Tests real-world API endpoints and identifies device performance profile
  - Provides device-specific recommendations for optimal settings
  - See [docs/fortios/PERFORMANCE_TESTING.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/PERFORMANCE_TESTING.md) for complete guide
- 🔧 **Optimized Connection Pool Defaults**: Conservative defaults based on real-world testing
  - `max_connections`: 10 (down from 100)
  - `max_keepalive_connections`: 5 (down from 20)
  - Run `fgt.api.utils.performance_test()` to get device-specific recommendations
- ✨ **Read-Only Mode**: Block all write operations for safe testing and CI/CD
  - Enable with `read_only=True` parameter
  - Perfect for testing automation scripts without making changes
- ✨ **Operation Tracking**: Complete audit logging of all API calls
  - Enable with `track_operations=True` parameter
  - Get detailed logs via `fgt.get_operations()`
- ✨ **Comprehensive Filter Documentation**: Complete guide to FortiOS filtering
  - New [docs/fortios/FILTERING_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/FILTERING_GUIDE.md) with 50+ examples
  - All FortiOS filter operators documented: `==`, `!=`, `=@`, `!@`, `<`, `<=`, `>`, `>=`
- ✨ **Username/Password Authentication**: Alternative to API tokens
  - Session-based authentication for temporary access
- ✨ **Firewall Policy Wrapper**: Intuitive interface with 150+ parameters
  - Access via `fgt.firewall.policy` namespace
  - See [docs/FIREWALL_POLICY_WRAPPER.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/FIREWALL_POLICY_WRAPPER.md) for complete guide

**Also in v0.3.17:**

- ✨ **Async/Await Support**: Full dual-mode support for async operations
  - Single `FortiOS` class works in both sync and async modes
  - All 750+ API methods support async with `mode="async"` parameter
  - All helper methods (`.exists()`) work transparently in both modes
  - See [docs/fortios/ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ASYNC_GUIDE.md) for complete guide
- ✨ **288 Helper Methods**: `.exists()` methods on CMDB endpoints
  - Check object existence without exceptions
  - Returns `True`/`False` instead of raising exceptions

**Previous Features:**

- Policy statistics, session monitoring, ACL counters
- Address objects, traffic shapers, GTP stats
- Special endpoints: policy-lookup (callable), clearpass-address (actions)
- **endpoint-control/**: 7 endpoints for FortiClient EMS monitoring
- **azure/, casb/, extender-controller/, extension-controller/**: Additional monitoring
- Test coverage: 39 firewall tests with 100% pass rate
- All endpoints support explicit parameters (no **kwargs)
- ✨ **Log Configuration Category**: 56 endpoints for comprehensive logging setup
  - Nested object pattern: `fgt.api.cmdb.log.disk.filter.get()`
  - Multiple FortiAnalyzer, syslog, TACACS+ server support
  - Custom fields, event filters, threat weights
- ✨ **ICAP Category**: Complete ICAP integration (3 endpoints, 30+ parameters)
- ✨ **IPS Category**: Full IPS management (8 endpoints)
  - Custom signatures, sensors, decoders, rules
- ✨ **Monitoring & Report Categories**: NPU-HPE monitoring, report layouts
- ✨ **Firewall Category Expansion**: 29 endpoints with nested objects
  - DoS policies, access-proxy (reverse proxy/WAF)
  - Schedule, service, shaper, SSH/SSL configurations

**Previous Release (v0.3.10):**

- ✨ **Configurable Timeouts**: Customize connection and read timeouts
  - `connect_timeout`: Connection establishment timeout (default: 10.0s)
  - `read_timeout`: Response read timeout (default: 300.0s)
  - Example: `FortiOS(host='...', token='...', connect_timeout=30.0, read_timeout=600.0)`
- ✨ **URL Encoding for Special Characters**: Automatic encoding of special characters in object names
  - Handles `/`, `@`, `:`, spaces, and other special characters
  - Works with objects like `Test_NET_192.0.2.0/24` (IP addresses with CIDR notation)
  - Applied to all 145 CMDB endpoint files automatically
- ✅ **Bug Fix**: Fixed 404 errors when object names contain special characters

**Previous Release (v0.3.9):**

- ✨ **raw_json Parameter**: All 200+ API methods now support `raw_json=True` for full response access
- ✨ **Logging System**: Global and per-instance logging control
- ✅ **Code Quality**: 100% PEP 8 compliance (black + isort + flake8)
- ✅ **Comprehensive Tests**: 200+ test files covering all endpoints

**Previous Releases:**

- v0.3.8: Dual-pattern interface for all create/update methods
- v0.3.7: Packaging and layout improvements
- v0.3.6: Hidden internal CRUD methods for cleaner autocomplete
- v0.3.5: Enhanced IDE autocomplete with PEP 561 type hints
- v0.3.4: Unified import syntax documentation
- v0.3.0: Firewall endpoints expansion

## 🎯 Features

### Core Features

- **Unified Package**: Import all Fortinet products from a single package
- **Type-Safe & Type-Checked**: Full PEP 561 compliance with mypy/pyright support for IDE autocomplete
- **Async/Await Support**: Full dual-mode operation - works with both sync and async code
- **Modular Architecture**: Each product module can be used independently
- **PyPI Installation**: `pip install hfortix` - simple and straightforward
- **Comprehensive Exception Handling**: 387+ FortiOS error codes with detailed descriptions
- **Well-Documented**: Extensive API documentation and examples
- **Modern Python**: Type hints, PEP 585 compliance, Python 3.10+

### 🆕 Advanced Features (v0.5.5)

#### **Pydantic Models - Runtime Validation** ✨
- **1,065 Pydantic models** automatically generated from FortiOS schemas
- **Field validation** with constraints (max_length, min/max values, regex patterns)
- **Type safety** with proper type hints and Literal types for enums
- **Helper methods**: `to_fortios_dict()`, `from_fortios_response()`
- **Location**: `hfortix_fortios.api.models.cmdb.*`

```python
from hfortix_fortios.api.models.cmdb.firewall.address import AddressModel

# Create and validate configuration
address = AddressModel(
    name="MyAddress",
    type="ipmask",
    subnet="192.168.1.0/24",
    comment="Example address"
)

# Convert to FortiOS payload
payload = address.to_fortios_dict()
fgt.api.cmdb.firewall.address.post(payload_dict=payload)
```

#### **Capabilities Metadata - Feature Detection** ✨
- **SUPPORTS_* constants** on all 1,065 endpoints
- Runtime capability checks before API calls
- No more guessing which operations are supported

```python
endpoint = fgt.api.cmdb.firewall.policy

# Check capabilities before calling
if endpoint.SUPPORTS_CREATE:
    endpoint.post(payload_dict=data)
    
if endpoint.SUPPORTS_MOVE:
    endpoint.move(policyid=5, action="before", reference_policyid=1)
    
# Available constants:
# SUPPORTS_CREATE, SUPPORTS_READ, SUPPORTS_UPDATE, SUPPORTS_DELETE
# SUPPORTS_MOVE, SUPPORTS_CLONE
# SUPPORTS_FILTERING, SUPPORTS_PAGINATION, SUPPORTS_SEARCH, SUPPORTS_SORTING
```

#### **Action Methods - Enhanced Operations** ✨
- **move()** - Reorder objects with position-based ordering
- **clone()** - Duplicate objects with automatic payload generation
- **exists()** - Check object existence without exceptions

```python
# Check if object exists
if fgt.api.cmdb.firewall.address.exists(name="MyAddress"):
    print("Address exists!")

# Move firewall policy before another
fgt.api.cmdb.firewall.policy.move(
    policyid=10, 
    action="before", 
    reference_policyid=5
)

# Clone an object
fgt.api.cmdb.firewall.address.clone(
    name="OriginalAddress",
    new_name="ClonedAddress"
)
```

#### **Object Response Mode - Clean Attribute Access** ✨
- **FortiObject wrapper** for cleaner, more Pythonic code
- **Attribute access** instead of dict keys: `obj.name` vs `obj["name"]`
- **Nested table field wrapping** - Full attribute access on nested objects
- **Single object returns** - Querying by mkey returns single object, not list
- **Dictionary-style access** - Both `obj.field` and `obj['field']` work
- **Multiple output formats** - Access as `.dict`, `.json`, or `.raw`
- **Full IDE autocomplete** with type stubs for all FortiObject methods
- **Zero maintenance** - works with any FortiOS version, no schemas required

```python
# All API calls now return FortiObject instances! ✨

fgt = FortiOS(host="...", token="...")

# Query all addresses - returns list of FortiObjects
addresses = fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    # Attribute access with full autocomplete ✅
    print(addr.name)
    print(addr.subnet)
    
    # Dictionary-style access also works ✅
    print(addr["name"])
    
    # Convert to dict when needed ✅
    addr_dict = addr.dict    # or addr.json or addr.raw
    print(addr_dict)         # {'name': 'MyAddress', 'subnet': '10.0.0.1/32', ...}

# Query by name - returns SINGLE FortiObject (not list) ✨
addr = fgt.api.cmdb.firewall.address.get(name="MyAddress")
print(addr.name)      # Direct access - no need for addr[0].name
print(addr.subnet)    # Clean and intuitive!
print(addr.dict)      # Convert to dict: {'name': 'MyAddress', ...}

# Nested table field support ✨
group = fgt.api.cmdb.firewall.service.group.get(name="MyGroup")
# Access nested members with full attribute support
for member in group.member:
    print(member.name)  # ✅ Works! FortiObjects all the way down
    
# Multiple ways to access the same data:
print(addr.name)      # ✅ Attribute access (recommended)
print(addr['name'])   # ✅ Dictionary-style access
print(addr.dict)      # ✅ Full dictionary: {'name': 'x', 'subnet': 'y', ...}
print(addr.json)      # ✅ Alias for .dict
print(addr.raw)       # ✅ Raw API response
    
# Convert back to dict for JSON serialization or dict operations
addr_dict = addr.to_dict()  # Full method
addr_dict = addr.dict        # Shortcut property  
addr_dict = addr.json        # Another alias

# Keyword argument support
addr = fgt.api.cmdb.firewall.address.get(name="MyAddress")  # ✅ Works
addr = fgt.api.cmdb.firewall.address.get("MyAddress")        # ✅ Also works
```

**Benefits:**
- ✨ **Full IDE autocomplete** for all FortiObject methods (get_full(), to_dict(), keys(), etc.)
- 🛡️ **Type safety** - IDE knows exact return types based on response_mode parameter
- 📝 **Cleaner code** - `addr.name` is more readable than `addr["name"]`
- 🎯 **Consistent behavior** - Both dict and object modes return single item when querying by mkey
- 🔗 **Nested access** - Full attribute access on table field members
- 🎯 **Zero maintenance** - No code generation, works with all endpoints

See [examples/fortiobject_autocomplete_demo.py](examples/fortiobject_autocomplete_demo.py) for complete examples.

### Additional Features

- **Convenience Wrappers**: High-level wrappers for common operations (policies, schedules, services, shapers, SSH/SSL proxy, wildcard FQDN)
  - ⚠️ **Note**: Some FortiOS API endpoints have limitations:
    - **SSH/SSL Proxy**: See [SSH/SSL Proxy Limitations](docs/fortios/wrappers/SSH_SSL_PROXY_WRAPPERS.md#fortios-api-limitations)
    - **Wildcard FQDN**: Create/Update/Delete operations not supported via API (use CLI). Read operations work normally.
  - SSH/SSL proxy wrappers document all known API restrictions
  - Test coverage: 67 comprehensive tests across SSH/SSL proxy features + 38 tests for wildcard FQDN (12 passing read tests)
- **Automatic Retry Logic**: Built-in retry mechanism with exponential backoff for transient failures
- **HTTP/2 Support**: Modern HTTP client with connection multiplexing for improved performance
- **Circuit Breaker**: Prevents cascade failures with automatic recovery
- **Simplified APIs**: Auto-conversion for common patterns (e.g., address group members)
- **Performance Testing**: Built-in utility to test and optimize your FortiGate performance

## 📁 Project Structure

```text
hfortix/
├── packages/           # Modular package architecture (v0.4.0+)
│   ├── core/          # Core exceptions and HTTP client
│   ├── fortios/       # FortiOS/FortiGate implementation
│   ├── fortimanager/  # FortiManager (planned)
│   ├── fortianalyzer/ # FortiAnalyzer (planned)
│   └── meta/          # Meta-package for unified installation
├── docs/              # User documentation (included in releases)
│   ├── fortios/       # FortiOS-specific guides
│   └── source/        # Sphinx documentation source
├── examples/          # Example scripts and usage patterns
├── examples/          # Example scripts
├── docs/              # User documentation
├── packages/          # Modular packages
│   ├── core/          # hfortix-core package
│   ├── fortios/       # hfortix-fortios package
│   └── meta/          # hfortix meta-package
├── README.md          # This file
├── QUICKSTART.md      # Quick reference guide
├── CHANGELOG.md       # Version history
└── pyproject.toml     # Package configuration
```

## 📚 Documentation

### Getting Started

- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference guide with examples
- **[docs/SECURITY.md](docs/SECURITY.md)** - Security best practices and audit results

### Feature Guides

#### Convenience Wrappers (Start Here!)
- **[docs/fortios/wrappers/CONVENIENCE_WRAPPERS.md](docs/fortios/wrappers/CONVENIENCE_WRAPPERS.md)** - **Overview of all convenience wrappers** (policies, shapers, schedules, services, SSH/SSL proxy) with common patterns and examples
- **[docs/fortios/wrappers/FIREWALL_POLICY_WRAPPER.md](docs/fortios/wrappers/FIREWALL_POLICY_WRAPPER.md)** - Detailed firewall policy API reference (150+ parameters)
- **[docs/fortios/wrappers/SHAPER_WRAPPERS.md](docs/fortios/wrappers/SHAPER_WRAPPERS.md)** - Detailed traffic shaper API reference (per-IP and traffic shapers)
- **[docs/fortios/wrappers/SCHEDULE_WRAPPERS.md](docs/fortios/wrappers/SCHEDULE_WRAPPERS.md)** - Schedule management reference (onetime, recurring, groups)
- **[docs/fortios/wrappers/SSH_SSL_PROXY_WRAPPERS.md](docs/fortios/wrappers/SSH_SSL_PROXY_WRAPPERS.md)** - SSH/SSL proxy configuration with **FortiOS API limitations** documented
- **[docs/fortios/ERROR_HANDLING_CONFIG.md](docs/fortios/ERROR_HANDLING_CONFIG.md)** - Configurable error handling for wrappers

#### Framework & Advanced Features
- **[docs/fortios/VALIDATION_GUIDE.md](docs/fortios/VALIDATION_GUIDE.md)** - Using the validation framework (832 validators)
- **[docs/archive/BUILDER_PATTERN_GUIDE.md](docs/archive/BUILDER_PATTERN_GUIDE.md)** - Builder pattern implementation details
- **[docs/fortios/ASYNC_GUIDE.md](docs/fortios/ASYNC_GUIDE.md)** - Async/await patterns and best practices
- **[docs/fortios/FILTERING_GUIDE.md](docs/fortios/FILTERING_GUIDE.md)** - FortiOS filtering with 50+ examples
- **[docs/fortios/PERFORMANCE_TESTING.md](docs/fortios/PERFORMANCE_TESTING.md)** - Performance testing and optimization

> **⚡ Performance Note**: When using convenience wrappers like `fgt.firewall.policy.exists()`:
>
> - **By ID** (`policy_id=123`) - Direct API call, fastest method
> - **By Name** (`name="MyPolicy"`) - Requires recursive lookup through all policies, slower but more convenient
> - Recommendation: Use `policy_id` for performance-critical code, `name` for readability and convenience

### API Reference

- **[docs/fortios/ENDPOINT_METHODS.md](docs/fortios/ENDPOINT_METHODS.md)** - Complete API method reference
- **[API_COVERAGE.md](API_COVERAGE.md)** - Detailed API implementation status
- **[CHANGELOG.md](CHANGELOG.md)** - Complete version history

## 🧪 Performance Testing

Test your FortiGate's performance and get optimal configuration recommendations:

```python
from hfortix import FortiOS

# Initialize your FortiGate client
fgt = FortiOS("192.168.1.99", token="your_token", verify=False)

# Run performance test via API (recommended - new in v0.3.17!)
results = fgt.api.utils.performance_test()

# Automatically provides:
# ✅ Connection pool validation
# ✅ API endpoint performance metrics
# ✅ Device performance profile (high-performance/fast-lan/remote-wan)
# ✅ Recommended settings for YOUR specific device
# ✅ Expected throughput estimates

# Example output:
# Device profile: high-performance
# Throughput: 70.54 req/s
# Recommended settings: {
#     'max_connections': 60,
#     'max_keepalive_connections': 30,
#     'recommended_concurrency': '20-30',
#     'expected_throughput': '~30 req/s'
# }
```

**Real-World Test Results (December 2025):**

- **FGT 70F** (10.37.95.1): 70.54 req/s - high-performance profile ⚡
- **FGT 200F** (212.55.57.170): 11.11 req/s - fast-lan profile
- **Remote VM** (fw.wjacobsen.fo): 4.75 req/s - remote-wan profile

### Alternative: Standalone function

```python
from hfortix.FortiOS.performance_test import quick_test

results = quick_test("192.168.1.99", "your_token", verify=False)
```

**Features:**

- ✅ Validates connection pool configuration
- ✅ Tests real-world API endpoints (status, policies, addresses, etc.)
- ✅ Identifies device profile (high-performance, fast-lan, or remote-wan)
- ✅ Provides specific recommendations for your device
- ✅ Determines optimal concurrency settings
- ✅ Command-line interface available: `python -m hfortix.FortiOS.performance_test`

**Key Finding:** Most FortiGate devices serialize API requests internally, meaning concurrent requests don't improve throughput and can actually make things 10-15x slower! The performance test helps you identify if your device benefits from concurrency or should use sequential requests.

**New Default Settings (v0.3.17):**

- `max_connections`: **10** (conservative - should work for most devices)
- `max_keepalive_connections`: **5** (50% below slowest device tested)
- Run performance test to get device-specific optimal settings!

## 📦 Available Modules

| Module | Status | Description |
| ------ | ------ | ----------- |
| **FortiOS** | ✅ Active | FortiGate firewall management API |
| **FortiManager** | ⏸️ Planned | Centralized management for FortiGate devices |
| **FortiAnalyzer** | ⏸️ Planned | Log analysis and reporting platform |

## 🚀 Installation

### From PyPI (Recommended)

```bash
# Install everything (meta-package)
pip install hfortix

# Or install only what you need (modular packages)
pip install hfortix-fortios  # FortiOS/FortiGate client only
pip install hfortix-core     # Core exceptions and HTTP framework only
```

**Note:** Version 0.4.0 introduces modular packages (`hfortix-core`, `hfortix-fortios`, `hfortix`) for flexible installation. The `hfortix` meta-package installs everything and provides full backward compatibility with earlier versions.

## 📖 Quick Start

### Basic Usage

```python
from hfortix import FortiOS

# Initialize with API token (recommended)
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False  # Use True in production with valid SSL cert
)
# Uses conservative defaults: max_connections=10, max_keepalive=5
# Run fgt.api.utils.performance_test() to get device-specific optimal settings!

# List firewall addresses
addresses = fgt.api.cmdb.firewall.address.list()
print(f"Found {len(addresses['results'])} addresses")

# Create a new address
result = fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='192.168.10.50/32',
    comment='Production web server'
)
```

### 🎯 IDE Autocomplete with Literal Types ✨ NEW in v0.5.4

**15,000+ parameters now have intelligent autocomplete!** Every enum parameter across all 1,065 endpoints now provides IDE suggestions for valid values.

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token')

# ✨ IDE autocomplete for ALL enum fields!
fgt.api.cmdb.firewall.policy.create(
    name='allow-web',
    action='accept',      # 💡 IDE suggests: 'accept', 'deny', 'ipsec'
    status='enable',      # 💡 IDE suggests: 'enable', 'disable'
    schedule='always',    # 💡 IDE suggests: 'always', 'none', or custom schedule
    logtraffic='all',     # 💡 IDE suggests: 'all', 'utm', 'disable'
    nat='enable',         # 💡 IDE suggests: 'enable', 'disable'
    # ... and 85 more autocompleted parameters!
)

# 🛡️ Type safety - catches errors before runtime
fgt.api.cmdb.system.interface.create(
    name='port1',
    mode='static',        # 💡 IDE suggests: 'static', 'dhcp', 'pppoe'
    type='physical',      # 💡 IDE suggests: 'physical', 'vlan', 'tunnel', 'loopback', ...
    role='lan',           # 💡 IDE suggests: 'lan', 'wan', 'dmz', 'undefined'
)

# 📚 Self-documenting - hover to see all valid options
fgt.api.cmdb.firewall.address.create(
    name='server1',
    type='ipmask',        # 💡 Hover shows: 'ipmask', 'iprange', 'fqdn', 'geography', ...
    subnet='10.0.1.5/32'
)
```

**Benefits:**

- ⚡ **Instant autocomplete** - No more guessing enum values
- 🛡️ **Type safety** - Invalid values caught by IDE and mypy
- 📚 **Self-documenting** - Hover tooltips show all valid options
- 🚀 **Zero learning curve** - Works immediately in VSCode, PyCharm, etc.
- ✅ **100% backward compatible** - No breaking changes

**Coverage:**

- **1,476 endpoints** with Literal-typed parameters
- **15,000+ parameters** with IDE autocomplete
- **firewall.policy**: 85 Literal parameters out of 189 total
- **Works with all major IDEs**: VSCode, PyCharm, Sublime Text, etc.

See [.dev/LITERAL_TYPES_QUICKSTART.md](.dev/LITERAL_TYPES_QUICKSTART.md) for more examples and tips!

### Raw JSON Response ✨

All API methods support `raw_json` parameter for full response access:

```python
# Default behavior - returns just the results
addresses = fgt.api.cmdb.firewall.address.list()
print(addresses)  # ['obj1', 'obj2', 'obj3']

# With raw_json=True - returns complete API response
response = fgt.api.cmdb.firewall.address.list(raw_json=True)
print(response['http_status'])  # 200
print(response['status'])       # 'success'
print(response['results'])      # ['obj1', 'obj2', 'obj3']
print(response['serial'])       # 'FGT60FTK19000001'
print(response['version'])      # 'v7.6.5'

# Useful for error checking
result = fgt.api.cmdb.firewall.address.get('web-server', raw_json=True)
if result['http_status'] == 200:
    print(f"Object found: {result['results']}")
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

**Available on:** All 45+ API methods (100% coverage)

### Environment Variables ✨ NEW in v0.3.18

Load credentials from environment variables for better security and CI/CD integration:

```python
from hfortix import FortiOS

# Set environment variables in your shell
# export FORTIOS_HOST="192.168.1.99"
# export FORTIOS_TOKEN="your-api-token"

# Create client without hardcoding credentials
fgt = FortiOS()  # Automatically loads from environment

# Also supports username/password
# export FORTIOS_HOST="192.168.1.99"
# export FORTIOS_USERNAME="admin"
# export FORTIOS_PASSWORD="your-password"

fgt = FortiOS()  # Loads credentials from environment

# Explicit parameters override environment variables
fgt = FortiOS(host='override.com', token='override-token')

# Mix both: host from parameter, token from environment
fgt = FortiOS(host='192.168.1.99')  # Token from FORTIOS_TOKEN env var
```

**Supported Environment Variables:**

- `FORTIOS_HOST` - FortiGate hostname or IP
- `FORTIOS_TOKEN` - API token
- `FORTIOS_USERNAME` - Username for password authentication
- `FORTIOS_PASSWORD` - Password for username authentication

**Use Cases:**

- **CI/CD Pipelines**: Store credentials as secrets, not in code
- **Docker Containers**: Pass credentials via environment
- **Security**: No credentials committed to version control
- **Multiple Environments**: Easy dev/staging/prod configuration
- **12-Factor Apps**: Configuration via environment (industry best practice)

### Logging Control ✨

Control logging output globally or per-instance:

```python
import hfortix
from hfortix import FortiOS

# Enable detailed logging globally for all instances
hfortix.set_log_level('DEBUG')  # Very verbose - all requests/responses
hfortix.set_log_level('INFO')   # Normal - request summaries
hfortix.set_log_level('WARNING') # Quiet - only warnings (default)
hfortix.set_log_level('ERROR')   # Silent - only errors
hfortix.set_log_level('OFF')     # No logging output

# Or enable logging for a specific instance
fgt = FortiOS('192.168.1.99', token='your-token', debug='info')

# Automatic sensitive data sanitization
# Tokens, passwords, and API keys are automatically masked in logs
```

**Features:**

- 5 log levels (DEBUG, INFO, WARNING, ERROR, OFF)
- Automatic sensitive data sanitization
- Request/response logging with timing
- Hierarchical loggers for fine-grained control

### Enterprise Audit Logging & Observability ✨ NEW in v0.4.0

Production-ready audit logging and observability for compliance and distributed systems:

```python
from hfortix_fortios import FortiOS, configure_logging
from hfortix_core.audit import FileHandler, SyslogHandler

# 1. Configure structured logging (one-time setup)
configure_logging(level="INFO", format="json")  # JSON logs for ELK/Splunk/CloudWatch

# 2. Create client with audit logging and observability
audit_handler = SyslogHandler("siem.company.com:514")  # Send to SIEM

fgt = FortiOS(
    "192.168.1.99",
    token="your-token",
    audit_handler=audit_handler,           # Audit logs to SIEM
    trace_id="req-abc-123",                # Distributed tracing ID
    user_context={                          # Change management metadata
        "username": "john.doe",
        "ticket": "CHG-12345",
        "environment": "production"
    }
)

# All API calls are automatically logged with full context
fgt.api.cmdb.firewall.address.create(name="web-server", subnet="10.0.0.1/32")
```

**Audit Log Output (JSONL format)**:
```json
{"timestamp":"2026-01-02T10:30:15Z","request_id":"a1b2c3d4","method":"POST","endpoint":"/api/v2/cmdb/firewall/address","action":"create","object_type":"firewall.address","object_name":"web-server","data":{"name":"web-server","subnet":"10.0.0.1/32"},"status_code":200,"success":true,"duration_ms":145,"host":"192.168.1.99","vdom":"root","trace_id":"req-abc-123","user_context":{"username":"john.doe","ticket":"CHG-12345","environment":"production"}}
```

**Key Features:**

- **Compliance Ready**: SOC 2, HIPAA, PCI-DSS audit trails
- **Multiple Handlers**: File, Syslog (RFC 5424), Stream, Composite
- **Multiple Formatters**: JSON, Syslog, CEF (Common Event Format)
- **Distributed Tracing**: `trace_id` for request correlation across microservices
- **User Context**: Track who, what, when, why for change management
- **SIEM Integration**: Compatible with Splunk, ELK, QRadar, ArcSight
- **Structured Logging**: JSON format for log aggregation (ELK, Splunk, CloudWatch)
- **Data Sanitization**: Automatic masking of passwords, tokens, keys
- **Non-Blocking**: Audit failures never break API operations

**Available Handlers:**

```python
from hfortix_core.audit import (
    FileHandler,        # Log to local file (JSONL format)
    SyslogHandler,      # Send to syslog server (RFC 5424)
    StreamHandler,      # Log to stdout/stderr
    CompositeHandler,   # Send to multiple destinations
    NullHandler         # Disable audit logging
)

# File logging
file_handler = FileHandler("/var/log/fortinet-audit.jsonl")

# Syslog to SIEM
syslog_handler = SyslogHandler("siem.company.com:514")

# Multiple destinations
composite = CompositeHandler([
    FileHandler("/var/log/audit.jsonl"),
    SyslogHandler("siem.company.com:514")
])
```

**Production Example:**

```python
from hfortix_fortios import FortiOS, configure_logging
from hfortix_core.audit import CompositeHandler, FileHandler, SyslogHandler
import uuid

# Configure JSON logging for production
configure_logging(level="INFO", format="json")

# Setup audit logging to multiple destinations
audit = CompositeHandler([
    FileHandler("/var/log/fortinet/audit.jsonl"),    # Local backup
    SyslogHandler("siem.company.com:514")            # SIEM
])

# Generate trace_id for distributed tracing
trace_id = f"req-{uuid.uuid4().hex[:16]}"

# Create client with full observability
fgt = FortiOS(
    "192.168.1.99",
    token="your-token",
    verify=True,  # Always verify SSL in production
    audit_handler=audit,
    trace_id=trace_id,
    user_context={
        "username": "automation",
        "service": "firewall-manager",
        "environment": "production",
        "ticket": "CHG-67890"
    }
)

# All operations automatically logged with full context
fgt.api.cmdb.firewall.policy.create(
    policyid=100,
    srcintf=["port1"],
    dstintf=["port2"],
    srcaddr=["all"],
    dstaddr=["all"],
    service=["ALL"],
    action="accept",
    schedule="always"
)
```

**Documentation:**

- **Full Guide**: [docs/fortios/AUDIT_LOGGING.md](docs/fortios/AUDIT_LOGGING.md)
- **Handler Protocol System**: [docs/fortios/HANDLER_PROTOCOL_SYSTEM.md](docs/fortios/HANDLER_PROTOCOL_SYSTEM.md)
- **Observability**: [docs/fortios/OBSERVABILITY.md](docs/fortios/OBSERVABILITY.md)
- **Examples**: `examples/audit_logging_demo.py`, `examples/observability_demo.py`

**Benefits:**

- ✅ **Compliance**: Automatic audit trails for SOC 2, HIPAA, PCI-DSS
- ✅ **Troubleshooting**: Complete operation history with timing
- ✅ **Change Management**: Link changes to tickets and users
- ✅ **Security**: Track who made what changes and when
- ✅ **Distributed Systems**: Correlate requests across microservices
- ✅ **Observability**: Integration with ELK, Splunk, CloudWatch, Datadog

**Unique to hfortix**: No other Python FortiGate library has built-in enterprise audit logging and observability!

### Handler Protocol System (Plugin Architecture) ✨ NEW in v0.4.1

**Extensible audit logging without modifying HFortix code**. Write custom handlers to integrate with any system.

#### Protocol-Based Architecture

Any class implementing `log_operation(operation: dict)` can be used as an audit handler:

```python
from typing import Any
from hfortix import FortiOS

class SlackNotifier:
    """Send notifications to Slack when firewall rules change"""

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def log_operation(self, operation: dict[str, Any]) -> None:
        """Called after every API operation"""
        if 'firewall.policy' in operation.get('object_type', ''):
            action = operation['action']
            user = operation.get('user_context', {}).get('username', 'Unknown')
            object_name = operation.get('object_name', 'N/A')

            message = f"🔥 Firewall changed by {user}: {action} {object_name}"
            self._send_to_slack(message)

    def _send_to_slack(self, message: str):
        import requests
        requests.post(self.webhook_url, json={"text": message})

# Use it
handler = SlackNotifier("https://hooks.slack.com/services/YOUR/WEBHOOK")
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

# Now all firewall policy changes trigger Slack notifications
fgt.api.cmdb.firewall.policy.create(name="Block-Malware", ...)
# → Slack: "🔥 Firewall changed by admin: create Block-Malware"
```

#### Enhanced CompositeHandler

Route operations to different handlers based on priority and filters:

```python
from hfortix_core.audit import CompositeHandler, FileHandler, SyslogHandler

# Define filters
def is_critical(op):
    return op['action'] == 'delete' or not op['success']

def is_policy_change(op):
    return 'policy' in op.get('object_type', '')

# Priority-based routing with filters
handler = CompositeHandler([
    # Critical operations to dedicated file (highest priority)
    (FileHandler('/var/log/critical.jsonl'), 100, is_critical),

    # Policy changes to SIEM (medium priority)
    (SyslogHandler('siem.company.com:514'), 50, is_policy_change),

    # Everything to general log (lowest priority)
    (FileHandler('/var/log/all.jsonl'), 1, None),
])

fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)

# Error tracking
summary = handler.error_summary
print(f"Total handler errors: {summary['total_errors']}")
```

#### Built-in Custom Handler Examples

**Kafka Handler** - Stream events to Kafka for distributed systems:
```python
from examples.custom_handlers.kafka_handler import KafkaHandler

handler = KafkaHandler(
    bootstrap_servers=["kafka1:9092", "kafka2:9092"],
    topic="fortinet-audit"
)
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
```

**Database Handler** - Store audit logs in SQL databases:
```python
from examples.custom_handlers.database_handler import DatabaseHandler

# SQLite for development
handler = DatabaseHandler("sqlite:///audit.db")

# PostgreSQL for production
handler = DatabaseHandler("postgresql://user:pass@localhost/audit_db")

fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
```

**Webhook Handler** - Send notifications to Slack, Teams, Discord:
```python
from examples.custom_handlers.webhook_handler import SlackNotifier, TeamsNotifier

# Slack notifications (only for policy changes)
slack = SlackNotifier(
    "https://hooks.slack.com/services/YOUR/WEBHOOK",
    filter_fn=lambda op: 'policy' in op.get('object_type', '')
)

# Teams alerts (only for failures)
teams = TeamsNotifier(
    "https://outlook.office.com/webhook/...",
    filter_fn=lambda op: not op['success']
)

# Use both
handler = CompositeHandler([slack, teams])
fgt = FortiOS("192.168.1.99", token="token", audit_handler=handler)
```

**Features:**

- ✅ **No Inheritance Required**: Protocol-based (duck typing)
- ✅ **Priority Ordering**: Execute handlers in priority order
- ✅ **Conditional Routing**: Filter which operations go where
- ✅ **Error Aggregation**: Track handler reliability
- ✅ **Dynamic Management**: Add/remove handlers at runtime
- ✅ **Production Ready**: Kafka, Database, Webhook examples included

**Documentation:**

- **Complete Guide**: [docs/fortios/HANDLER_PROTOCOL_SYSTEM.md](docs/fortios/HANDLER_PROTOCOL_SYSTEM.md) (800+ lines)
- **Examples**: `examples/custom_handlers/` (Kafka, Database, Webhook handlers)
- **Demo**: `examples/composite_handler_demo.py`

### Read-Only Mode & Operation Tracking ✨ NEW in v0.3.17

Safe testing and comprehensive audit logging:

```python
from hfortix import FortiOS
from hfortix.FortiOS.exceptions_forti import ReadOnlyModeError

# 1. Read-Only Mode - Block all write operations
fgt = FortiOS('192.168.1.99', token='your-token', read_only=True)

# GET requests work normally
status = fgt.api.monitor.system.status.get()  # ✅ Works

try:
    # POST/PUT/DELETE requests are blocked
    fgt.api.cmdb.firewall.address.post(data={"name": "test", "subnet": "10.0.0.1/32"})
except ReadOnlyModeError as e:
    print(f"Blocked: {e}")  # ❌ Raises ReadOnlyModeError

# Perfect for: testing, CI/CD pipelines, dry-run, training environments

# 2. Operation Tracking - Audit logging of all API calls
fgt = FortiOS('192.168.1.99', token='your-token', track_operations=True)

# Make some API calls
fgt.api.monitor.system.status.get()
fgt.api.cmdb.firewall.address.get(filter="name=@web")

# Get complete audit log
operations = fgt.get_operations()
for op in operations:
    print(f"{op['timestamp']} {op['method']} {op['path']} - Status: {op['status_code']}")

# Get only write operations (POST/PUT/DELETE)
write_ops = fgt.get_write_operations()
for op in write_ops:
    print(f"{op['method']} {op['path']}")
    if op['data']:
        print(f"  Data: {op['data']}")

# 3. Combine both features
fgt = FortiOS('192.168.1.99', token='your-token',
              read_only=True, track_operations=True)

# Test your automation script safely while logging everything
try:
    # Your automation code here
    fgt.api.cmdb.firewall.policy.post(data={...})  # Blocked
except ReadOnlyModeError:
    pass

# Review what would have been executed
blocked_ops = [op for op in fgt.get_operations() if op.get('blocked_by_read_only')]
print(f"Would have executed {len(blocked_ops)} write operations")
```

**Use Cases:**

- **Testing**: Test automation scripts without affecting production
- **CI/CD**: Validate configuration changes in pipelines
- **Auditing**: Track all API operations for compliance
- **Documentation**: Auto-generate change logs from operations
- **Debugging**: See exact API call sequence
- **Training**: Safe environment for learning

### Advanced Filtering ✨ Enhanced in v0.3.17

Complete guide to FortiOS native filter operators:

```python
from hfortix import FortiOS

fgt = FortiOS('192.168.1.99', token='your-token')

# All 8 FortiOS filter operators:
addresses = fgt.api.cmdb.firewall.address.get(filter="name==web-server")      # Equals
addresses = fgt.api.cmdb.firewall.address.get(filter="name!=test")            # Not equals
addresses = fgt.api.cmdb.firewall.address.get(filter="subnet=@10.0")          # Contains
addresses = fgt.api.cmdb.firewall.address.get(filter="subnet!@192.168")       # Not contains
policies = fgt.api.cmdb.firewall.policy.get(filter="policyid<100")            # Less than
policies = fgt.api.cmdb.firewall.policy.get(filter="policyid<=100")           # Less than or equal
policies = fgt.api.cmdb.firewall.policy.get(filter="policyid>100")            # Greater than
policies = fgt.api.cmdb.firewall.policy.get(filter="policyid>=100")           # Greater than or equal

# Combine multiple filters (AND logic)
policies = fgt.api.cmdb.firewall.policy.get(
    filter="status==enable&action==accept&policyid>=100&policyid<=200"
)

# Range queries
addresses = fgt.api.cmdb.firewall.address.get(
    filter="subnet=@10.&comment=@production"
)

# Supports 8 filtering operators
```

### Authentication Methods ✨ Enhanced in v0.3.17

#### API Token Authentication (Recommended)

FortiOS API tokens are the recommended authentication method:

```python
from hfortix import FortiOS

# API token authentication
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',  # 25+ alphanumeric characters
    verify=False
)

# Token validation catches common errors:
# ❌ Token too short (< 25 chars)
# ❌ Token with spaces (copy-paste errors)
# ❌ Invalid characters (only letters, numbers, hyphens, underscores allowed)
# ❌ Common placeholders ("your_token_here", "xxx", "api_token", etc.)
```

**Token Requirements:**

- **Length**: Minimum 25 characters (FortiOS tokens are typically 31+ chars)
  - Older FortiOS versions: ~31-32 characters
  - Newer FortiOS versions: 40+ characters
  - Length varies by version - no fixed standard
- **Format**: Alphanumeric characters (letters, numbers, hyphens, underscores)
- **Generate**: System > Administrators > Create New > REST API Admin

**Why 25-character minimum?**

- Catches obviously invalid tokens (passwords, test strings, placeholders)
- Flexible enough for all FortiOS versions (31-32 char old, 40+ char new)
- Prevents common user errors without being too restrictive

#### Username/Password Authentication

Session-based authentication with automatic session management:

```python
from hfortix import FortiOS

# Context manager - recommended (auto-logout)
with FortiOS('192.168.1.99', username='admin', password='password',
             verify=False) as fgt:
    # Session automatically created
    addresses = fgt.api.cmdb.firewall.address.get()
    # Session automatically cleaned up on exit

# Manual session management
fgt = FortiOS('192.168.1.99', username='admin', password='password')
# Login happens automatically
addresses = fgt.api.cmdb.firewall.address.get()
fgt.close()  # Manual logout

# Configure session timeout (default: 5 minutes)
with FortiOS('192.168.1.99', username='admin', password='password',
             session_idle_timeout=600) as fgt:  # 10 minutes
    # Proactive re-auth at 80% of timeout (8 minutes)
    # Timer resets on each request (idle timer)
    addresses = fgt.api.cmdb.firewall.address.get()

# Disable proactive re-auth
fgt = FortiOS('192.168.1.99', username='admin', password='password',
              session_idle_timeout=None)

# Credential validation enforces:
# ✅ Both username AND password must be provided together
# ❌ Cannot provide username without password (or vice versa)
```

**Important Notes:**

- ⚠️ Username/password works in FortiOS ≤7.4.x but **removed in 7.6.x+**
- 🔒 Use API token authentication for production deployments
- ⏱️ Idle timer resets on each API request
- 🔄 Proactive re-auth at 80% of idle timeout
- 📌 Context manager required for proactive re-auth

### Extensibility: Custom HTTP Clients ✨ v0.3.18

HFortix uses the `IHTTPClient` Protocol interface (PEP 544), making it extensible for custom requirements. Create custom HTTP clients to add:

- **Audit logging** to external systems (SIEM, syslog, databases)
- **Response caching** to reduce API load
- **Custom authentication schemes** (OAuth, mutual TLS, corporate SSO)
- **Request proxying** through corporate infrastructure
- **Rate limiting** for custom policies
- **Metrics collection** to monitoring systems
- **Testing with fake data** without a real FortiGate

**Basic Example:**

```python
from hfortix import FortiOS
from hfortix.FortiOS.http_client import HTTPClient

# Create a custom client wrapper
class AuditLoggingHTTPClient:
    """Wraps real client to log all API calls to external audit system."""

    def __init__(self, real_client, audit_logger):
        self._client = real_client
        self._logger = audit_logger

    def get(self, api_type, path, **kwargs):
        self._logger.info(f"API Call: GET {api_type}/{path}")
        return self._client.get(api_type, path, **kwargs)

    def post(self, api_type, path, data, **kwargs):
        self._logger.info(f"API Call: POST {api_type}/{path}", extra={'data': data})
        return self._client.post(api_type, path, data, **kwargs)

    def put(self, api_type, path, data, **kwargs):
        self._logger.info(f"API Call: PUT {api_type}/{path}", extra={'data': data})
        return self._client.put(api_type, path, data, **kwargs)

    def delete(self, api_type, path, **kwargs):
        self._logger.info(f"API Call: DELETE {api_type}/{path}")
        return self._client.delete(api_type, path, **kwargs)

    def close(self):
        return self._client.close()

# Use custom client with FortiOS
real_client = HTTPClient(url="https://192.0.2.10", token="your-token", verify=False)
audit_client = AuditLoggingHTTPClient(real_client, my_audit_logger)

# FortiOS uses your custom client
fgt = FortiOS(client=audit_client)

# All API calls are now logged to your audit system
fgt.api.cmdb.firewall.address.create(name="web-server", subnet="10.0.0.1/32")
```

**Protocol Interface:**

```python
from typing import Protocol, Any, Optional, Union

class IHTTPClient(Protocol):
    """Protocol defining HTTP client interface for extensibility."""

    def get(
        self,
        api_type: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]: ...

    def post(
        self,
        api_type: str,
        path: str,
        data: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]: ...

    def put(self, api_type: str, path: str, data: dict[str, Any], ...) -> dict[str, Any]: ...

    def delete(self, api_type: str, path: str, ...) -> dict[str, Any]: ...
```

**Complete Examples:**

See `examples/custom_http_client_example.py` for production-ready implementations:

- `AuditLoggingHTTPClient` - Log all API calls to syslog/SIEM for compliance
- `CachingHTTPClient` - Cache GET responses to reduce API load
- `FakeHTTPClient` - Return fake data for testing without a real FortiGate

**Use Cases:**

- **Enterprise Compliance**: Log all FortiGate changes to SIEM for SOC 2/HIPAA/PCI-DSS
- **Development/Testing**: Use fake client in CI/CD pipelines without FortiGate hardware
- **Performance Optimization**: Cache frequently-read data (address objects, service definitions)
- **Custom Authentication**: Integrate with corporate SSO or vault systems
- **Request Debugging**: Log detailed request/response data for troubleshooting

### Advanced HTTP Features ✨ v0.3.15

Enterprise-grade reliability and observability features:

```python
from hfortix import FortiOS

fgt = FortiOS('192.168.1.99', token='your-token', verify=False)

# 1. Request correlation tracking (auto-generated or custom)
result = fgt._client.request(
    "GET", "monitor", "system/status",
    request_id="batch-update-2025-12-17"
)

# 2. Monitor connection pool health
stats = fgt.get_connection_stats()
print(f"Circuit breaker: {stats['circuit_breaker_state']}")  # closed/open/half_open
print(f"HTTP/2 enabled: {stats['http2_enabled']}")           # True
print(f"Total requests: {stats['total_requests']}")
print(f"Success rate: {stats['success_rate']:.1f}%")
print(f"Total retries: {stats['total_retries']}")

# View retry breakdown
for reason, count in stats['retry_by_reason'].items():
    print(f"  {reason}: {count} retries")

# 3. Circuit breaker pattern (automatic fail-fast)
# Prevents cascading failures - opens after 5 consecutive failures
# Auto-recovers to half-open after 60s, then closed if successful
try:
    result = fgt.api.monitor.system.status.get()
except RuntimeError as e:
    if "Circuit breaker is OPEN" in str(e):
        print("⚠️  Service is down - failing fast to prevent cascade")
        print("Circuit will auto-recover in 60s or use manual reset:")
        fgt._client.reset_circuit_breaker()  # Manual reset if needed

# 4. Per-endpoint custom timeouts (wildcard pattern matching)
# Useful for slow operations like log queries or config exports
fgt._client.configure_endpoint_timeout(
    endpoint_pattern='monitor/log/*',      # Longer timeout for log queries
    connect_timeout=10.0,
    read_timeout=600.0                     # 10 minutes for large logs
)

fgt._client.configure_endpoint_timeout(
    endpoint_pattern='cmdb/system/config/backup',  # Config backup
    read_timeout=300.0                             # 5 minutes
)

# Default timeouts still apply to other endpoints
# Fast operations remain fast (10s connect, 300s read)

# 5. Structured logging (machine-readable logs with extra fields)
# All logs include: request_id, endpoint, method, status_code, duration, vdom/adom
# Compatible with Elasticsearch, Splunk, CloudWatch
import hfortix

hfortix.set_log_level('INFO')  # See request/response timing
# Logs include: timestamp, level, module, request_id, endpoint, duration, status

# 6. Multi-tenant logging with VDOM/ADOM
# When vdom is configured, it's automatically added to all structured logs
fgt = FortiOS(
    host="192.168.1.99",
    token="token",
    vdom="customer_a"  # Virtual Domain for multi-tenant environments
)

# All logs automatically include vdom field:
# {"timestamp":"...","level":"INFO","vdom":"customer_a","endpoint":"/api/v2/cmdb/firewall/policy",...}

# Benefits for multi-tenant environments:
# - Filter logs by customer: jq '.vdom == "customer_a"' logs.json
# - Per-tenant metrics in ELK/Splunk/Datadog
# - Audit trail isolation by virtual domain
# - Compliance reporting per customer/tenant
```

**Benefits:**

- **Request Tracking**: Trace requests across distributed systems with correlation IDs
- **Circuit Breaker**: Automatic fail-fast prevents wasting time on dead connections
- **Connection Metrics**: Monitor health, detect issues before they cause problems
- **Per-Endpoint Timeouts**: Different timeouts for fast/slow operations (no more one-size-fits-all)
- **Structured Logs**: Machine-readable JSON logs for aggregation tools

**Circuit Breaker States:**

- `closed` (normal): All requests pass through
- `open` (failing): Requests fail immediately without attempting connection (fail-fast)
- `half_open` (testing): One request allowed to test if service recovered

**When Circuit Opens:**

- After 10 consecutive failures (configurable via `circuit_breaker_threshold`, default changed from 5 to 10)
- Automatically transitions to `half_open` after 30s (configurable via `circuit_breaker_timeout`, default changed from 60s to 30s)
- If test request succeeds → back to `closed`
- If test request fails → back to `open` for another 30s

**Circuit Breaker Behavior Options:**

1. **Fail-fast (default)**: Immediately raises `CircuitBreakerOpenError` when circuit opens
   - Best for test environments and catching issues early
   - No waiting - fails immediately

2. **Auto-retry (optional)**: Automatically waits and retries when circuit opens
   - Enable with `circuit_breaker_auto_retry=True`
   - Configure max retries with `circuit_breaker_max_retries` (default: 3)
   - Configure retry delay with `circuit_breaker_retry_delay` (default: 5.0 seconds)
   - Best for production scripts that need resilience
   - ⚠️ WARNING: Not recommended for tests - may cause long delays

**Important**: `circuit_breaker_retry_delay` and `circuit_breaker_timeout` serve different purposes:

- `circuit_breaker_retry_delay` (5s): How long to wait **between retry attempts**
- `circuit_breaker_timeout` (30s): How long circuit stays **open before testing recovery**

```python
# Fail-fast (default)
fgt = FortiOS(host="192.0.2.10", token="token")

# Auto-retry with custom delay for production resilience
fgt = FortiOS(
    host="192.0.2.10",
    token="token",
    circuit_breaker_auto_retry=True,
    circuit_breaker_max_retries=3,
    circuit_breaker_retry_delay=5.0  # Wait 5s between retries
)
```

### Dual-Pattern Interface ✨

HFortix supports **flexible dual-pattern syntax** - use dictionaries, keywords, or mix both:

```python
# Pattern 1: Dictionary-based (great for templates)
config = {
    'name': 'web-server',
    'subnet': '192.168.10.50/32',
    'comment': 'Production web server'
}
fgt.api.cmdb.firewall.address.create(data_dict=config)

# Pattern 2: Keyword-based (great for readability)
fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='192.168.10.50/32',
    comment='Production web server'
)

# Pattern 3: Mixed (template + overrides)
base_config = load_template('address_template.json')
fgt.api.cmdb.firewall.address.create(
    data_dict=base_config,
    name=f'server-{site_id}',  # Override name
    comment=f'Site: {site_name}'
)
```

**Available on:** 43 methods across 13 categories (100% coverage)

- All CMDB create/update operations (38 endpoints)
- Service operations (5 methods)

### Exception Handling

```python
from hfortix import (
    FortiOS,
    APIError,
    ResourceNotFoundError,
    DuplicateEntryError
)

try:
    result = fgt.api.cmdb.firewall.address.create(
        name='test-address',
        subnet='10.0.0.0/24'
    )
except DuplicateEntryError as e:
    print(f"Address already exists: {e}")
except ResourceNotFoundError as e:
    print(f"Resource not found: {e}")
except APIError as e:
    print(f"API Error: {e.message}")
    print(f"HTTP Status: {e.http_status}")
    print(f"Error Code: {e.error_code}")
```

## 🏗️ Project Structure

```text
fortinet/
├── hfortix/                  # Main package
│   ├── __init__.py           # Public API exports
│   ├── exceptions.py         # Base exceptions
│   ├── exceptions_forti.py   # FortiOS-specific error codes/helpers
│   ├── py.typed              # PEP 561 marker
│   └── FortiOS/
│       ├── __init__.py
│       ├── fortios.py        # FortiOS client
│       ├── http_client.py    # Internal HTTP client
│       ├── exceptions.py     # FortiOS re-exports
│       └── api/
│           └── v2/
│               ├── cmdb/     # Configuration endpoints
│               ├── log/      # Log reading endpoints
│               ├── service/  # Service operations
│               └── monitor/  # Monitoring endpoints
├── setup.py                  # Package configuration
├── pyproject.toml            # Build system config
├── README.md                 # This file
├── QUICKSTART.md             # Quick reference guide
├── API_COVERAGE.md           # API implementation status
└── CHANGELOG.md              # Version history
```

## 🔍 Module Discovery

Check which modules are available:

```python
from hfortix import get_available_modules

modules = get_available_modules()
print(modules)
# {'FortiOS': True, 'FortiManager': False, 'FortiAnalyzer': False}
```

## 🎓 Examples

## Async/Await Usage ✨

HFortix provides full async/await support for all FortiOS API operations. To use async mode, simply pass `mode="async"` to the `FortiOS` constructor. All API methods and helpers support async/await, enabling high-performance concurrent automation.

**Quick Example:**

```python
import asyncio
from hfortix import FortiOS

async def main():
    # Enable async mode
    async with FortiOS(host='192.168.1.99', token='your-token', mode="async") as fgt:
        addresses = await fgt.api.cmdb.firewall.address.list()
        print(f"Found {len(addresses)} addresses")

asyncio.run(main())
```

**Key Points:**

- Use `mode="async"` to enable async mode
- Use `async with` for automatic cleanup, or call `await fgt.aclose()` manually
- All API methods and helpers (like `.exists()`) must be awaited
- Use `asyncio.gather()` for concurrent requests

**Best Practices:**

- Use async mode for bulk operations or high concurrency
- Always use context managers for resource cleanup
- Limit concurrency with semaphores if needed
- See [docs/fortios/ASYNC_GUIDE.md](docs/fortios/ASYNC_GUIDE.md) for advanced patterns, migration tips, and troubleshooting

---

### FortiOS - Firewall Address Management

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token', verify=False)

# List addresses
addresses = fgt.api.cmdb.firewall.address.list()

# Create address
result = fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='10.0.1.100/32',
    comment='Production web server'
)

# Update address
result = fgt.api.cmdb.firewall.address.update(
    name='web-server',
    comment='Updated comment'
)

```python

# Delete address
result = fgt.api.cmdb.firewall.address.delete(name='web-server')
```

### FortiOS - DoS Protection (NEW!)

```python
# Create IPv4 DoS policy with simplified API
result = fgt.api.cmdb.firewall.dos_policy.create(
    policyid=1,
    name='protect-web-servers',
    interface='port3',              # Simple string format
    srcaddr=['all'],                # Simple list format
    dstaddr=['web-servers'],
    service=['HTTP', 'HTTPS'],
    status='enable',
    comments='Protect web farm from DoS attacks'
)

# API automatically converts to FortiGate format:
# interface='port3' → {'q_origin_key': 'port3'}
# service=['HTTP'] → [{'name': 'HTTP'}]

# Custom anomaly detection thresholds
result = fgt.api.cmdb.firewall.dos_policy.create(
    policyid=2,
    name='strict-dos-policy',
    interface='wan1',
    srcaddr=['all'],
    dstaddr=['all'],
    service=['ALL'],
    anomaly=[
        {'name': 'tcp_syn_flood', 'threshold': 500, 'action': 'block'},
        {'name': 'udp_flood', 'threshold': 1000, 'action': 'block'}
    ]
)
```

### FortiOS - Reverse Proxy/WAF (NEW!)

```python
# Create access proxy (requires VIP with type='access-proxy')
result = fgt.api.cmdb.firewall.access_proxy.create(
    name='web-proxy',
    vip='web-vip',                    # VIP must be type='access-proxy'
    auth_portal='enable',
    log_blocked_traffic='enable',
    http_supported_max_version='2.0',
    svr_pool_multiplex='enable'
)

# Create virtual host with simplified API
result = fgt.api.cmdb.firewall.access_proxy_virtual_host.create(
    name='api-vhost',
    host='*.api.example.com',
    host_type='wildcard',
    ssl_certificate='Fortinet_Factory'  # String auto-converts to list
)

# API automatically converts:
# ssl_certificate='cert' → [{'name': 'cert'}]
```

### FortiOS - Address & Address Group Management (NEW!)

```python
# Create IPv4 address (subnet)
result = fgt.api.cmdb.firewall.address.create(
    name='internal-net',
    type='ipmask',
    subnet='192.168.1.0/24',
    comment='Internal network'
)

# Create IPv4 address (IP range)
result = fgt.api.cmdb.firewall.address.create(
    name='dhcp-range',
    type='iprange',
    start_ip='192.168.1.100',
    end_ip='192.168.1.200'
)

# Create IPv4 address (FQDN)
result = fgt.api.cmdb.firewall.address.create(
    name='google-dns',
    type='fqdn',
    fqdn='dns.google.com'
)

# Create IPv6 address
result = fgt.api.cmdb.firewall.address6.create(
    name='ipv6-internal',
    type='ipprefix',
    ip6='2001:db8::/32',
    comment='IPv6 internal network'
)

# Create address group with simplified API
result = fgt.api.cmdb.firewall.addrgrp.create(
    name='internal-networks',
    member=['subnet1', 'subnet2', 'subnet3'],  # Simple string list!
    comment='All internal networks'
)

# API automatically converts:
# member=['addr1', 'addr2'] → [{'name': 'addr1'}, {'name': 'addr2'}]

# Create IPv6 address group
result = fgt.api.cmdb.firewall.addrgrp6.create(
    name='ipv6-internal-networks',
    member=['ipv6-subnet1', 'ipv6-subnet2'],
    comment='All internal IPv6 networks'
)

# Create IPv6 address template
result = fgt.api.cmdb.firewall.address6_template.create(
    name='ipv6-subnet-template',
    ip6='2001:db8::/32',
    subnet_segment_count=2,
    comment='IPv6 subnet template'
)
```

### FortiOS - Schedule Management

```python
# Create recurring schedule
result = fgt.api.cmdb.firewall.schedule.recurring.create(
    name='business-hours',
    day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
    start='08:00',
    end='18:00'
)

# Create one-time schedule
from datetime import datetime, timedelta
tomorrow = datetime.now() + timedelta(days=1)
start = f"09:00 {tomorrow.strftime('%Y/%m/%d')}"
end = f"17:00 {tomorrow.strftime('%Y/%m/%d')}"

result = fgt.api.cmdb.firewall.schedule.onetime.create(
    name='maintenance-window',
    start=start,
    end=end,
    color=5
)
```

### FortiOS - Routing Protocols (Singleton Endpoints) ⚠️

**Important:** Routing protocol configurations use a different pattern than collection endpoints.

**Collection Endpoints** (addresses, policies, etc.) support standard CRUD:

```python
# Standard CRUD - simple and intuitive
fgt.api.cmdb.firewall.address.create(name='test', subnet='192.168.1.0/24')
fgt.api.cmdb.firewall.address.update(name='test', comment='updated')
fgt.api.cmdb.firewall.address.delete('test')
```

**Singleton Endpoints** (BGP, OSPF, RIP, ISIS, etc.) require GET→Modify→PUT pattern:

```python
# BGP Neighbor Management - requires full config update
# Step 1: Get current BGP configuration
result = fgt.api.cmdb.router.bgp.get()

# Step 2: Extract config (handles different response formats)
if isinstance(result, list):
    config = result[0] if result else {}
elif isinstance(result, dict) and 'results' in result:
    config = result['results']
    if isinstance(config, list):
        config = config[0] if config else {}
else:
    config = result

# Step 3: Modify nested objects (neighbors, networks, etc.)
neighbors = config.get('neighbor', [])
neighbors.append({
    'ip': '10.0.0.1',
    'remote-as': 65001,
    'description': 'New BGP neighbor',
    'shutdown': 'enable'  # Disabled for safety
})
config['neighbor'] = neighbors

# Step 4: Send entire config back
result = fgt.api.cmdb.router.bgp.update(data_dict=config)

# Verify
config = fgt.api.cmdb.router.bgp.get()
# Extract config again (same as step 2)
neighbors = config.get('neighbor', []) if isinstance(config, dict) else []
print(f"BGP now has {len(neighbors)} neighbors")
```

OSPF Network Management (same pattern)

```python
# OSPF Network Management - same pattern
config = fgt.api.cmdb.router.ospf.get()
# Extract config (same pattern as BGP)
if isinstance(config, list):
    config = config[0] if config else {}

networks = config.get('network', [])
networks.append({
    'id': 9999,
    'prefix': '192.168.1.0 255.255.255.0'
})
config['network'] = networks
fgt.api.cmdb.router.ospf.update(data_dict=config)
```

RIP Network Management

```python
# RIP Network Management
config = fgt.api.cmdb.router.rip.get()
if isinstance(config, list):
    config = config[0]

networks = config.get('network', [])
networks.append({'id': 1, 'prefix': '10.0.0.0 255.0.0.0'})
config['network'] = networks
fgt.api.cmdb.router.rip.update(data_dict=config)
```

**Why This Pattern?**

- FortiOS API design: Routing protocols are singleton objects (only one BGP/OSPF/RIP config per VDOM)
- Nested objects (neighbors, networks, areas) are managed as lists within the main config
- The API requires sending the entire configuration on updates to maintain consistency

**Future Enhancement:**
Helper methods are planned to simplify this pattern:

```python
# Planned for future release (not yet available)
fgt.api.cmdb.router.bgp.add_neighbor(ip='10.0.0.1', remote_as=65001)
fgt.api.cmdb.router.bgp.remove_neighbor('10.0.0.1')
fgt.api.cmdb.router.bgp.list_neighbors()
```

**Affected Endpoints:**

- `router/bgp` - BGP neighbors, networks, aggregate addresses, VRFs
- `router/ospf` - OSPF areas, interfaces, networks, neighbors
- `router/ospf6` - OSPFv3 areas, interfaces
- `router/rip` - RIP networks, neighbors, interfaces
- `router/ripng` - RIPng networks, neighbors
- `router/isis` - IS-IS NETs, interfaces
- `router/bfd` - BFD neighbors (IPv4)
- `router/bfd6` - BFD neighbors (IPv6)

See the test files in the development workspace for complete working examples.

### Helper Methods - Safe Existence Checking ✨

The `.exists()` helper method provides safe existence checking on 288 CMDB endpoints without raising exceptions:

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token', verify=False)

# Check if object exists before operations
if fgt.api.cmdb.firewall.address.exists('web-server'):
    print("Address already exists")
    fgt.api.cmdb.firewall.address.update('web-server', comment='Updated')
else:
    print("Creating new address")
    fgt.api.cmdb.firewall.address.create(
        name='web-server',
        subnet='10.0.1.100/32'
    )

# Safe deletion pattern
if fgt.api.cmdb.user.local.exists('testuser'):
    fgt.api.cmdb.user.local.delete('testuser')

# Conditional processing
users = ['alice', 'bob', 'charlie']
for user in users:
    if not fgt.api.cmdb.user.local.exists(user):
        fgt.api.cmdb.user.local.create(
            name=user,
            type='password',
            passwd='SecureP@ss123'
        )
```

**Available on:** 288 endpoints with full CRUD operations (firewall addresses, policies, users, VPN configs, etc.)

**📚 Complete Documentation:**

- See [docs/fortios/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ENDPOINT_METHODS.md) for complete API method reference
- See [docs/fortios/ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ASYNC_GUIDE.md) for async/await usage patterns

## Exception Hierarchy

```text
Exception
└── FortinetError (base)
    ├── AuthenticationError
    ├── AuthorizationError
    └── APIError
        ├── ResourceNotFoundError (404)
        ├── BadRequestError (400)
        ├── MethodNotAllowedError (405)
        ├── RateLimitError (429)
        ├── ServerError (500)
        ├── DuplicateEntryError (-5, -15, -100)
        ├── EntryInUseError (-23, -94, -95)
        ├── InvalidValueError (-651, -1, -50)
        └── PermissionDeniedError (-14, -37)
```

## 🧪 Testing

**Note:** This SDK is currently in beta (v0.3.x). All endpoints are functional but will remain in beta status until version 1.0.0 with comprehensive unit test coverage.

**Current Status:**

- All implemented endpoints are tested against live FortiGate devices
- Integration testing performed during development
- Unit test framework planned for v1.0.0 release

## 📝 Version

Current version: **0.3.16** (See [CHANGELOG.md](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) for release notes)

```python
from hfortix import get_version
print(get_version())
```

## 🤝 Contributing

Contributions are welcome! Please feel free to:

- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests

For code contributions:

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper tests
4. Submit a pull request with clear description

### For Maintainers: Automated Release Process

HFortix includes an automated release workflow via `make release`:

```bash
# Auto-increment patch version (e.g., 0.3.38 → 0.3.39)
make release

# Specify exact version
make release VERSION=0.3.40

# Bump minor version (e.g., 0.3.38 → 0.4.0)
make release TYPE=minor

# Bump major version (e.g., 0.3.38 → 1.0.0)
make release TYPE=major
```

**What it does:**
1. Auto-fixes code issues (formatting, imports)
2. Runs all pre-release checks (lint, type-check, security)
3. Executes test suite
4. Updates version in all files (pyproject.toml, setup.py, `__init__.py`)
5. Updates CHANGELOG.md
6. Creates git commit and tag
7. Prompts to push to GitHub (triggers CI/CD for PyPI publishing)

**Prerequisites:**
- Clean git working directory
- All tests passing
- CHANGELOG.md has [Unreleased] section

## 📄 License

Proprietary License - Free for personal, educational, and business use.

**You may:**

- Use for personal projects and learning
- Use in your business operations
- Deploy in client environments
- Use in managed services and technical support

**You may not:**

- Sell the software itself as a standalone product
- Redistribute as your own product

See [CHANGELOG.md](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) v0.2.0 for details.

## 🔗 Links

- [FortiOS API Documentation](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [FortiManager API Documentation](https://docs.fortinet.com/document/fortimanager)
- [FortiAnalyzer API Documentation](https://docs.fortinet.com/document/fortianalyzer)

## 💡 Tips

- **Use API Tokens**: Only token-based authentication is supported for FortiOS REST API
- **Error Handling**: Always catch specific exceptions for better error handling
- **Verify SSL**: Set `verify=True` in production (requires valid certificates)
- **Automatic Retries**: Built-in retry logic handles transient failures (429, 500, 502, 503, 504)
- **Connection Pooling**: HTTP/2 support with connection multiplexing for better performance
- **Timeout Configuration**: Customize `connect_timeout` and `read_timeout` for your environment
- **Logging**: Use `hfortix.set_log_level('INFO')` for request/response debugging

## ⚙️ Configuration

### Environment Variables

```bash
export FGT_HOST="192.168.1.99"
export FGT_TOKEN="your-api-token"
export FGT_VERIFY_SSL="false"
```

### Using .env File

```python
from dotenv import load_dotenv
import os

load_dotenv()

fgt = FortiOS(
    host=os.getenv('FGT_HOST'),
    token=os.getenv('FGT_TOKEN'),
    verify=os.getenv('FGT_VERIFY_SSL', 'false').lower() == 'true'
)
```

## 🎯 Roadmap

- [🚧] FortiOS API implementation (In Development)
  - [x] Exception handling system (387 error codes)
  - [x] Base client architecture with HTTP/2, retry logic, circuit breaker
  - [🔷] CMDB endpoints (Beta - 57.5% coverage, 23/40 categories)
    - [🔷] Firewall (address, policy, service, DoS, ICAP, IPS, etc.) - Beta
    - [🔷] System (interface, admin, global, etc.) - Beta
    - [🔷] Router (static, bgp, ospf, rip, isis, etc.) - **NEW** Beta ⚠️ See note below
    - [🔷] VPN (IPsec, SSL, etc.) - Beta
    - [🔷] Log (disk, syslog, fortianalyzer, etc.) - Beta
    - [🔷] Wireless Controller, User, Web Filter, Application - Beta
    - [ ] Remaining 17 categories (Switch Controller, WAD, etc.)
  - [🔷] Monitor endpoints (Beta - 18% coverage, 6/33 categories)
    - [🔷] Firewall, Endpoint Control, Azure, CASB, Extender - Beta
    - [ ] Remaining 27 categories
  - [🔷] Service endpoints (Beta - 100% coverage, 3/3 categories)
    - Sniffer, Security Rating, etc.
  - [🔷] Log endpoints (Beta - 100% coverage, 5/5 categories)
    - Traffic, Event, Virus, etc.
- [x] Modular package architecture
- [x] PyPI package publication (hfortix on PyPI)
- [ ] FortiManager module (Not Started)
- [ ] FortiAnalyzer module (Not Started)
- [ ] Helper methods for singleton routing endpoints (Planned)
- [x] Async/await support (Implemented in v0.3.15)
- [ ] CLI tool (Planned)

### ⚠️ Important Note: Singleton Routing Endpoints (Beta)

**Routing protocol configurations (BGP, OSPF, RIP, ISIS, etc.) use a different pattern than collection endpoints:**

- **Collection Endpoints** (addresses, policies, etc.): Use standard CRUD operations

  ```python
  # Simple add/remove pattern
  fgt.api.cmdb.firewall.address.create(name='test', subnet='192.168.1.0/24')
  fgt.api.cmdb.firewall.address.delete('test')
  ```

- **Singleton Endpoints** (bgp, ospf, rip, isis, etc.): Require GET→Modify→PUT pattern

  ```python
  # Must get entire config, modify, and send back
  config = fgt.api.cmdb.router.bgp.get()
  config['neighbor'].append({'ip': '10.0.0.1', 'remote-as': 65001})
  fgt.api.cmdb.router.bgp.update(data_dict=config)
  ```

**Why?** This is a FortiOS API design - routing protocols are singleton objects with nested lists (neighbors, networks, areas). The API requires sending the entire configuration on updates.

**Future Enhancement:** Helper methods like `add_neighbor()`, `remove_neighbor()`, `list_neighbors()` are planned to simplify this pattern.

**Affected Endpoints:**

- `router/bgp` - BGP neighbors, networks, VRFs
- `router/ospf` - OSPF areas, interfaces, networks
- `router/ospf6` - OSPFv3 configuration
- `router/rip` - RIP networks, neighbors
- `router/ripng` - RIPng configuration
- `router/isis` - IS-IS NETs, interfaces
- `router/bfd` - BFD neighbors (IPv4)
- `router/bfd6` - BFD neighbors (IPv6)

**All implementations remain in BETA until version 1.0.0 with comprehensive unit test coverage.**

---

## 👤 Author

### Herman W. Jacobsen

- Email: herman@wjacobsen.fo
- LinkedIn: [linkedin.com/in/hermanwjacobsen](https://www.linkedin.com/in/hermanwjacobsen/)
- GitHub: [@hermanwjacobsen](https://github.com/hermanwjacobsen)

---

## Built with ❤️ for the Fortinet community

# HFortix - Fortinet Python SDK

Python client library for Fortinet products including FortiOS, FortiManager, and FortiAnalyzer.

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

## 🎯 Current Status

**⚠️ BETA STATUS**: All implementations are functional but in beta. APIs work correctly but may have incomplete parameter coverage or undiscovered edge cases.

**FortiOS 7.6.5 Coverage (December 23, 2025):**

- **CMDB API**: 37 of 37 categories (100% coverage) - 500+ endpoints 🔷 Beta
- **Monitor API**: 32 of 32 categories (100% coverage) - 200+ endpoints 🔷 Beta
- **Log API**: 5 of 5 categories (100% coverage) - Log reading functionality 🔷 Beta
- **Service API**: 3 of 3 categories (100% coverage) - 21 methods 🔷 Beta
- **Overall**: 77 of 77 categories (100% coverage) - 750+ API methods 🎉

**Validation Coverage (v0.3.21):**

- 832 validation helper modules auto-generated for all API types (CMDB, Monitor, Log, Service)
- Enum, length, range, pattern, and type validation implemented
- **Required field validation is NOT yet implemented**

**Test Coverage:** 226 test files (145 CMDB, 81 Monitor) with 75%+ pass rate (~50% of generated endpoints tested)
**Note:** All implementations remain in beta until version 1.0.0 with comprehensive unit test coverage.

**Note:** Documentation in the `X/` folder is for internal development only, is not referenced outside `X`, and is not included in git or releases.

**🔥 Recent Highlights (December 2025):**

- 🎉 **100% API COVERAGE**: Complete implementation of ALL documented FortiOS 7.6.5 API categories!
- 🚀 **MASSIVE EXPANSION**: Generated 500+ new endpoints across 37 CMDB + 32 Monitor categories
- 🔄 **API Refactoring**: All endpoints refactored with RESTful methods (.list(), .get(), .create(), .update(), .delete())
- ⚡ **Dual-Pattern Interface**: Flexible syntax supporting both dictionary and keyword arguments
- 🏗️ **Repository Organization**: Clean structure with all dev tools
- ⚡ **Unified Module Generator**: Single tool handles all edge cases (digit-prefixed names, certificates, nested resources)
- ✨ **Monitor API** (v0.3.11): 6 categories with 50+ monitoring endpoints (firewall stats, sessions, EMS, etc.)
- ✨ **Log Configuration** (v0.3.11): 56 endpoints for comprehensive logging setup
- ✨ **Firewall Expansion** (v0.3.11): FTP proxy, ICAP, IPS, DoS policies, access-proxy (WAF)

**📖 Documentation:**

- **Quick Start Guide**: [QUICKSTART.md](https://github.com/hermanwjacobsen/hfortix/blob/main/QUICKSTART.md) - Getting started guide
- **Full Changelog**: [CHANGELOG.md](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) - Complete version history

**Latest Features (v0.3.38 - December 29, 2025):**

- 🚦 **Traffic Shaper Convenience Wrappers**: Production-ready wrappers for traffic shaping
  - **Per-IP Shaper** (`fgt.firewall.shaper_per_ip`) - Bandwidth and session limits per source IP
  - **Traffic Shaper** (`fgt.firewall.traffic_shaper`) - Shared traffic shaper with guaranteed/maximum bandwidth
  - Full parameter support with comprehensive validation
  - ⚠️ **Important:** Rename operations not supported (FortiOS API limitation - name is immutable primary key)
  - See `docs/SHAPER_WRAPPERS.md` for complete guide and examples
  - Comprehensive test suite: `X/pytests/firewall/shaper.py` (20 tests passing)

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
  - See [docs/PERFORMANCE_TESTING.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/PERFORMANCE_TESTING.md) for complete guide
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
  - New [docs/FILTERING_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/FILTERING_GUIDE.md) with 50+ examples
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
  - See [docs/ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ASYNC_GUIDE.md) for complete guide
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

- **Unified Package**: Import all Fortinet products from a single package
- **Type-Safe & Type-Checked**: Full PEP 561 compliance with mypy/pyright support for IDE autocomplete
- **Async/Await Support**: Full dual-mode operation - works with both sync and async code
- **Modular Architecture**: Each product module can be used independently
- **PyPI Installation**: `pip install hfortix` - simple and straightforward
- **Comprehensive Exception Handling**: 387+ FortiOS error codes with detailed descriptions
- **Automatic Retry Logic**: Built-in retry mechanism with exponential backoff for transient failures
- **HTTP/2 Support**: Modern HTTP client with connection multiplexing for improved performance
- **Circuit Breaker**: Prevents cascade failures with automatic recovery
- **Simplified APIs**: Auto-conversion for common patterns (e.g., address group members)
- **Performance Testing**: Built-in utility to test and optimize your FortiGate performance
- **Well-Documented**: Extensive API documentation and examples
- **Modern Python**: Type hints, PEP 585 compliance, Python 3.10+

## 📚 Documentation

### Getting Started

- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference guide with examples
- **[docs/SECURITY.md](docs/SECURITY.md)** - Security best practices and audit results

### Feature Guides

#### Convenience Wrappers (Start Here!)
- **[docs/wrappers/CONVENIENCE_WRAPPERS.md](docs/wrappers/CONVENIENCE_WRAPPERS.md)** - **Overview of all convenience wrappers** (policies, shapers, schedules, services) with common patterns and examples
- **[docs/wrappers/FIREWALL_POLICY_WRAPPER.md](docs/wrappers/FIREWALL_POLICY_WRAPPER.md)** - Detailed firewall policy API reference (150+ parameters)
- **[docs/wrappers/SHAPER_WRAPPERS.md](docs/wrappers/SHAPER_WRAPPERS.md)** - Detailed traffic shaper API reference (per-IP and traffic shapers)
- **[docs/wrappers/SCHEDULE_WRAPPERS.md](docs/wrappers/SCHEDULE_WRAPPERS.md)** - Schedule management reference (onetime, recurring, groups)
- **[docs/ERROR_HANDLING_CONFIG.md](docs/ERROR_HANDLING_CONFIG.md)** - Configurable error handling for wrappers

#### Framework & Advanced Features
- **[docs/VALIDATION_GUIDE.md](docs/VALIDATION_GUIDE.md)** - Using the validation framework (832 validators)
- **[docs/BUILDER_PATTERN_GUIDE.md](docs/BUILDER_PATTERN_GUIDE.md)** - Builder pattern implementation details
- **[docs/ASYNC_GUIDE.md](docs/ASYNC_GUIDE.md)** - Async/await patterns and best practices
- **[docs/FILTERING_GUIDE.md](docs/FILTERING_GUIDE.md)** - FortiOS filtering with 50+ examples
- **[docs/PERFORMANCE_TESTING.md](docs/PERFORMANCE_TESTING.md)** - Performance testing and optimization

> **⚡ Performance Note**: When using convenience wrappers like `fgt.firewall.policy.exists()`:
>
> - **By ID** (`policy_id=123`) - Direct API call, fastest method
> - **By Name** (`name="MyPolicy"`) - Requires recursive lookup through all policies, slower but more convenient
> - Recommendation: Use `policy_id` for performance-critical code, `name` for readability and convenience

### API Reference

- **[docs/ENDPOINT_METHODS.md](docs/ENDPOINT_METHODS.md)** - Complete API method reference
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
pip install hfortix
```

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

- **Enterprise Compliance**: Log all FortiGate changes to SIEM for SOX/HIPAA/PCI-DSS
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
# All logs include: request_id, endpoint, method, status_code, duration
# Compatible with Elasticsearch, Splunk, CloudWatch
import hfortix

hfortix.set_log_level('INFO')  # See request/response timing
# Logs include: timestamp, level, module, request_id, endpoint, duration, status
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
- See [docs/ASYNC_GUIDE.md](docs/ASYNC_GUIDE.md) for advanced patterns, migration tips, and troubleshooting

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

- See [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md) for complete API method reference
- See [docs/ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ASYNC_GUIDE.md) for async/await usage patterns

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

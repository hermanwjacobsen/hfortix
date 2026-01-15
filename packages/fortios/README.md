
# HFortix FortiOS

Python SDK for FortiGate/FortiOS API - Complete, type-safe, production-ready.

[![PyPI version](https://badge.fury.io/py/hfortix-fortios.svg)](https://pypi.org/project/hfortix-fortios/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)


> **⚠️ BETA STATUS - Version 0.5.57 (January 14, 2026)**
>
> **Breaking Changes:** See v0.5.33 and v0.5.32 for important return type changes in dict/object mode.
> **Status:** Production-ready but in beta until v1.0 with comprehensive unit tests.
> **What's New:** Major bug fixes, expanded test suite, improved type stubs!

**Version:** 0.5.57
**Status:** Beta (100% auto-generated, production-ready, optimized for performance)


## 🚀 What's New in v0.5.57 (January 2026)

### Latest Bug Fixes (v0.5.57)

- **Bug #21**: `CompositeHandler.error_summary` now correctly tracks handler errors
- **Bug #22**: `process_response()` no longer crashes on lists of non-dict items
- **Bug #23**: `exists()` method returns `False` for API error responses
- **Bug #24**: `Utils.performance_test()` now works correctly
- **Bug #26**: Fixed `log_operation` stub signature mismatch
- **Generator fixes**: NotRequired import for Python <3.11, class name mappings, kebab-case test keys

### Recent Improvements (v0.5.50-v0.5.56)

- **Expanded test suite**: 8 new test files (~78 new tests)
- **Type stub fixes**: FortiObject, print_debug_info exports, results type improved
- **Python 3.10+ compatibility**: `NotRequired` imported from `typing_extensions`

### Core Features (v0.5.43-v0.5.45)

- **Core `fmt` module**: 13 formatting utilities now in `hfortix_core.fmt`
  - `to_list()`, `to_json()`, `to_csv()`, `to_dict()`, `to_table()`, `to_yaml()`, etc.
  - Auto-split for space-delimited strings: `"80 443"` → `['80', '443']`
  - `to_dictlist()` / `to_listdict()` for columnar↔row format conversion
- **Automatic key normalization**: API response keys converted from hyphens to underscores
  - `tcp-portrange` → `tcp_portrange` automatically in responses
- **Improved type annotations**: Better `to_dict()` return type for Pylance compatibility
- **Optimized helper files**: 50-80 lines reduced per file using functools.partial

### Breaking Changes (v0.5.32-v0.5.34)

- **Single object returns**: Querying by mkey returns single dict/object, not list
  - `fgt.api.cmdb.firewall.address.get(name="test")` → returns `dict` (not `list[dict]`)
- **Nested typed classes**: Table fields have their own typed classes for full autocomplete
- **Enhanced type stubs**: Better overload ordering for Pylance type inference

See the [complete changelog](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) for all details.

## Overview

Complete Python client for FortiOS 7.6.5 REST API with 100% endpoint coverage (1,348 endpoints), full type safety, and enterprise features. All code is auto-generated from FortiOS API schemas.

## Installation

```bash
pip install hfortix-fortios
```

This automatically installs:
- `hfortix-core` - Core utilities and HTTP client
- `hfortix-fortios-stubs` - Type stubs for optimal IDE/type checker performance

**For minimal installation (without stubs, smaller size):**
```bash
pip install --no-deps hfortix-fortios
pip install hfortix-core  # Then install only runtime dependencies
```

**For everything (includes future products):**
```bash
pip install hfortix[all]
```

## Quick Start

```python
from hfortix_fortios import FortiOS

# Connect to FortiGate
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    verify=False
)

# Get system status
status = fgt.monitor.system.status()
print(f"Hostname: {status['hostname']}")
print(f"Version: {status['version']}")

# Manage firewall addresses
fgt.api.cmdb.firewall.address.create(
    name="web-server",
    subnet="192.168.1.100 255.255.255.255"
)

# 🎯 NEW! IDE autocomplete with Literal types (v0.5.4+)
fgt.api.cmdb.firewall.policy.create(
    name="allow-web",
    action="accept",      # 💡 IDE suggests: 'accept', 'deny', 'ipsec'
    status="enable",      # 💡 IDE suggests: 'enable', 'disable'
    logtraffic="all"      # 💡 IDE suggests: 'all', 'utm', 'disable'
)
```

## API Coverage

**FortiOS 7.6.5 - 100% Coverage (Schema v1.7.0):**

- **CMDB API**: 561 endpoints - Full configuration management (firewall, system, VPN, routing, etc.)
- **Monitor API**: 490 endpoints - Real-time monitoring (sessions, stats, resources, etc.)
- **Log API**: 286 endpoints - Log queries (disk, memory, FortiAnalyzer, FortiCloud, search)
- **Service API**: 11 endpoints - Service operations (sniffer, security rating, system)
- **Total**: 1,348 endpoints with 2,129 implementation files

All endpoints are **100% auto-generated** with:
- Complete `.pyi` type stub files (2,129 files)
- Schema-based parameter validation
- Auto-generated basic tests
- Comprehensive error handling
- Automatic key normalization (hyphens → underscores)

## Key Features

### 🎯 IDE Autocomplete with Literal Types (NEW in v0.5.4!)

**15,000+ parameters with intelligent IDE autocomplete!** Every enum parameter provides instant suggestions:

```python
# ✨ Autocomplete for ALL enum fields
fgt.api.cmdb.firewall.policy.create(
    action='accept',      # 💡 IDE: 'accept', 'deny', 'ipsec'
    status='enable',      # 💡 IDE: 'enable', 'disable'
    nat='enable',         # 💡 IDE: 'enable', 'disable'
    logtraffic='all'      # 💡 IDE: 'all', 'utm', 'disable'
)

# 🛡️ Type safety catches errors at development time
fgt.api.cmdb.system.interface.create(
    mode='static',        # 💡 IDE: 'static', 'dhcp', 'pppoe'
    type='physical',      # 💡 IDE: 'physical', 'vlan', 'tunnel', ...
    role='lan'            # 💡 IDE: 'lan', 'wan', 'dmz', 'undefined'
)
```

**Benefits:** ⚡ Instant autocomplete • 🛡️ Type safety • 📚 Self-documenting • ✅ 100% backward compatible

### 🎯 Complete API Coverage

Access every FortiOS endpoint with clean, Pythonic syntax:

```python
# CMDB (Configuration)
fgt.api.cmdb.firewall.policy.get()
fgt.api.cmdb.system.interface.get(name="port1")
fgt.api.cmdb.router.static.create(...)

# Monitor (Real-time data)
sessions = fgt.api.monitor.firewall.session.get()
resources = fgt.api.monitor.system.resource.usage.get()

# Log (Query logs)
vpn_logs = fgt.api.log.disk.event.vpn.get(rows=50)
traffic = fgt.api.log.memory.traffic.forward.get(rows=100)
```

### 🎨 Pretty Printing with FortiObject

**Clean, readable output for FortiOS data** - all methods return FortiObject by default:

```python
fgt = FortiOS(
    host="192.168.1.99",
    token="your-token",
)

# Get policies and print cleanly
policies = fgt.api.cmdb.firewall.policy.get()

for policy in policies:
    print(f"\nPolicy {policy.policyid}: {policy.name}")
    print(f"  {policy.join('srcintf')} → {policy.join('dstintf')}")
    print(f"  {policy.join('srcaddr')} → {policy.join('dstaddr')}")
    print(f"  Service: {policy.join('service')} [{policy.action.upper()}]")

# Output:
# Policy 11: allow-web
#   port3 → port4
#   login.windows.net → gmail.com
#   Service: SAMBA [DENY]
```

**FortiObject Methods:**
- `obj.join('field')` - Join list values into comma-separated string
- `obj.join('field', ' | ')` - Custom separator
- `obj.pretty('field')` - Alias for join() with default separator
- Auto-flattens member_table fields: `['port1']` instead of `[{'name': 'port1'}]`

**Benefits:**
- 📊 Clean console output
- 🎯 No manual list comprehension needed
- ✨ Works with all FortiOS list fields
- 🔄 Original data always accessible via `.to_dict()`

### 🎨 Direct API Access

All 1,219 endpoints are accessed directly - no wrappers needed:

```python
# Service Management
fgt.firewall.service_custom.create(
    name="custom-app",
    tcp_portrange="8080-8090",
    comment="My application"
)

# Schedules
fgt.firewall.schedule_recurring.create(
    name="business-hours",
    day=["monday", "tuesday", "wednesday", "thursday", "friday"],
    start="08:00",
    end="17:00"
)

# Traffic Shaping
fgt.firewall.traffic_shaper.create(
    name="critical-apps",
    guaranteed_bandwidth=50000,
    maximum_bandwidth=100000,
    bandwidth_unit="kbps"
)

# IP/MAC Binding
fgt.firewall.ipmacbinding_table.create(
    ip="10.0.1.100",
    mac="00:11:22:33:44:55",
    name="Server-01"
)
```

**Available Wrappers:**
- **Service Management**: `service_custom`, `service_category`, `service_group`
- **Schedules**: `schedule_onetime`, `schedule_recurring`, `schedule_group`
- **Traffic Shaping**: `traffic_shaper`, `shaper_per_ip`
- **IP/MAC Binding**: `ipmacbinding_table`, `ipmacbinding_setting`
- **SSH/SSL Proxy**: `ssh_host_key`, `ssh_local_ca`, `ssh_local_key`, `ssh_setting`, `ssl_setting` (⚠️ with API limitations)
- **Firewall Policies**: `policy` with 150+ parameters

**Note:** Some wrappers have FortiOS API limitations (e.g., SSH CA deletion requires CLI/GUI). See documentation for details.

### ⚡ Advanced Features

**Async/Await Support:**
```python
import asyncio

async def main():
    async with FortiOS(host="...", token="...", mode="async") as fgt:
        # All methods support await
        addresses = await fgt.api.cmdb.firewall.address.list()

        # Concurrent operations
        addr, pol, svc = await asyncio.gather(
            fgt.api.cmdb.firewall.address.list(),
            fgt.api.cmdb.firewall.policy.list(),
            fgt.api.cmdb.firewall.service.custom.list()
        )

asyncio.run(main())
```

**Error Handling:**
```python
from hfortix_core import (
    APIError,
    ResourceNotFoundError,
    DuplicateEntryError
)

try:
    fgt.api.cmdb.firewall.address.create(name="test", subnet="10.0.0.1/32")
except DuplicateEntryError:
    print("Address already exists")
except ResourceNotFoundError:
    print("Resource not found")
except APIError as e:
    print(f"API Error: {e.message} (code: {e.error_code})")
```

**Read-Only Mode & Operation Tracking:**
```python
# Safe testing - block all write operations
fgt = FortiOS(host="...", token="...", read_only=True)

# Audit logging - track all API calls
fgt = FortiOS(host="...", token="...", track_operations=True)
operations = fgt.get_operations()
```

**Performance Testing:**
```python
# Test your device and get optimal settings
results = fgt.api.utils.performance_test()
print(f"Recommended settings: {results['recommendations']}")
```

### 🔧 Enterprise Features

- **Audit Logging**: Built-in compliance logging with SIEM integration (SOC 2, HIPAA, PCI-DSS)
- **Observability**: Structured logging, distributed tracing with `trace_id`, user context tracking
- **HTTP/2 Support**: Connection multiplexing for better performance
- **Automatic Retry**: Handles transient failures (429, 500, 502, 503, 504) with exponential/linear/fibonacci backoff
- **Circuit Breaker**: Prevents cascade failures with automatic recovery
- **Request Tracking**: Correlation IDs for distributed tracing
- **Validation Framework**: 832 auto-generated validators

### 🔍 Debugging & Monitoring (v0.4.0)

**Quick Debug Mode:**
```python
# Enable debug logging with simple boolean
fgt = FortiOS(host="...", token="...", debug=True)
```

**Connection Pool Monitoring:**
```python
# Real-time connection statistics
stats = fgt.connection_stats
print(f"Active: {stats['active_requests']}/{stats['max_connections']}")
print(f"Total requests: {stats['total_requests']}")
print(f"Pool exhaustion: {stats['pool_exhaustion_count']}")
```

**Request Inspection:**
```python
# Debug slow or failed requests
result = fgt.api.cmdb.firewall.address.list()
info = fgt.last_request
print(f"Endpoint: {info['endpoint']}")
print(f"Response time: {info['response_time_ms']}ms")
print(f"Status: {info['status_code']}")
```

**Debug Session:**
```python
from hfortix_fortios import DebugSession

# Comprehensive session monitoring
with DebugSession(fgt) as session:
    # Make API calls
    fgt.api.cmdb.firewall.address.list()
    fgt.api.cmdb.firewall.policy.list()

    # Auto-prints summary on exit:
    # - Duration, total requests, success/failure counts
    # - Avg/min/max response times
    # - Connection pool deltas
```

**Performance Profiling:**
```python
from hfortix_fortios import debug_timer

# Time individual operations
with debug_timer("Fetch all addresses") as timing:
    result = fgt.api.cmdb.firewall.address.list()

print(f"Took {timing['duration_ms']:.1f}ms")
```

**Enhanced Logging:**
```python
from hfortix_fortios import configure_logging

# JSON logging for ELK/Splunk
configure_logging(
    level="INFO",
    format="json",
    include_trace=True,  # Add request_id to all logs
    output_file="/var/log/fortios.log"  # Log to file
)

# Text logging with colors for development
configure_logging(
    level="DEBUG",
    format="text",
    use_color=True
)
```

**Type Hints & IDE Support:**
```python
# Full type hints for better autocomplete
from hfortix_fortios import FortiOS
from hfortix_core import APIResponse, ListResponse

fgt: FortiOS = FortiOS(host="...", token="...")
response: APIResponse = fgt.api.cmdb.firewall.address.get(name="test")
```

See `docs/fortios/DEBUGGING.md` for complete debugging guide.
- **Type Safety**: Full type hints with IDE autocomplete
- **Structured Logging**: Machine-readable JSON logs for ELK/Splunk/CloudWatch

## Import Patterns

### Recommended (New)
```python
from hfortix_fortios import FortiOS
```

### Legacy (Still Supported)
```python
from hfortix import FortiOS
from hfortix.FortiOS import FortiOS
```

## API Structure

```python
# Configuration Management (CMDB)
fgt.api.cmdb.firewall.policy.*
fgt.api.cmdb.firewall.address.*
fgt.api.cmdb.system.interface.*
fgt.api.cmdb.router.static.*
fgt.api.cmdb.vpn.ipsec.*

# Monitoring
fgt.api.monitor.system.status()
fgt.api.monitor.firewall.session.*
fgt.api.monitor.system.resource.*

# Logging
fgt.api.log.disk.traffic.*
fgt.api.log.disk.event.*
fgt.api.log.disk.virus.*

# Convenience Wrappers
fgt.firewall.policy.*
fgt.firewall.service_custom.*
fgt.firewall.schedule_recurring.*
fgt.firewall.traffic_shaper.*
```

## Documentation

**Main Guides:**
- [Quick Start](https://github.com/hermanwjacobsen/hfortix/blob/main/QUICKSTART.md) - Getting started guide
- [Async Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ASYNC_GUIDE.md) - Async/await patterns
- [API Reference](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ENDPOINT_METHODS.md) - Complete method reference

**Convenience Wrappers:**
- [Overview Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/CONVENIENCE_WRAPPERS.md) - All wrappers
- [Service Wrappers](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/CONVENIENCE_WRAPPERS.md#service-management) - Service management
- [Schedule Wrappers](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/SCHEDULE_WRAPPERS.md) - Schedule management
- [Shaper Wrappers](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/SHAPER_WRAPPERS.md) - Traffic shaping

**Advanced Features:**
- [Validation Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/VALIDATION_GUIDE.md) - Using validators
- [Filtering Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/FILTERING_GUIDE.md) - FortiOS filtering
- [Performance Testing](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/PERFORMANCE_TESTING.md) - Optimization

**Full Documentation:**
- [Complete Changelog](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) - Version history
- [Main Repository](https://github.com/hermanwjacobsen/hfortix) - Complete docs

## Requirements

- Python 3.10+
- FortiOS 7.0+ (tested with 7.6.5)
- hfortix-core >= 0.4.0-dev1

## Development Status

**Beta** - All APIs are functional and tested against live FortiGate devices. The package remains in beta status until version 1.0.0 with comprehensive unit test coverage.

**Current Test Coverage:**
- 226 test files (145 CMDB, 81 Monitor)
- 75%+ pass rate
- ~50% of endpoints have dedicated tests
- All implementations validated against FortiOS 7.6.5

## Examples

### Firewall Policies

```python
# Create policy
fgt.firewall.policy.create(
    name="Allow-Web",
    srcintf=["port1"],
    dstintf=["port2"],
    srcaddr=["all"],
    dstaddr=["web-servers"],
    action="accept",
    schedule="always",
    service=["HTTP", "HTTPS"],
    logtraffic="all"
)

# Check if exists
if fgt.firewall.policy.exists(policy_id=10):
    fgt.firewall.policy.update(policy_id=10, status="disable")
```

### Address Management

```python
# Create address
fgt.api.cmdb.firewall.address.create(
    name="web-server",
    subnet="192.168.1.100 255.255.255.255",
    comment="Production web server"
)

# Create address group
fgt.api.cmdb.firewall.addrgrp.create(
    name="internal-networks",
    member=["subnet1", "subnet2", "subnet3"],
    comment="All internal networks"
)
```

### VPN Configuration

```python
# Create IPsec Phase 1
fgt.api.cmdb.vpn.ipsec.phase1_interface.create(
    name="site-to-site",
    type="static",
    interface="wan1",
    ike_version=2,
    peertype="any",
    proposal="aes256-sha256",
    remote_gw="203.0.113.10"
)
```

## License

Proprietary - See LICENSE file

## Support

- 📖 [Documentation](https://github.com/hermanwjacobsen/hfortix)
- 🐛 [Report Issues](https://github.com/hermanwjacobsen/hfortix/issues)
- 💬 [Discussions](https://github.com/hermanwjacobsen/hfortix/discussions)

## Author

**Herman W. Jacobsen**
- Email: herman@wjacobsen.fo
- LinkedIn: [linkedin.com/in/hermanwjacobsen](https://www.linkedin.com/in/hermanwjacobsen/)
- GitHub: [@hermanwjacobsen](https://github.com/hermanwjacobsen)

# HFortix FortiOS

Python SDK for FortiGate/FortiOS API - Complete, type-safe, production-ready.

[![PyPI version](https://badge.fury.io/py/hfortix-fortios.svg)](https://pypi.org/project/hfortix-fortios/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> **⚠️ BETA STATUS - Version 0.4.0**
>
> Production-ready FortiOS client, but in beta until v1.0 with comprehensive unit tests.
> **Major release** with modular architecture. See migration guide if upgrading from 0.3.x.

**Version:** 0.4.0
**Status:** Beta (Functional, production-ready, pending comprehensive unit tests for v1.0)

## Overview

Complete Python client for FortiOS 7.6.5 REST API with 100% endpoint coverage, convenience wrappers, and enterprise features.

## Installation

```bash
pip install hfortix-fortios
```

This automatically installs `hfortix-core` as a dependency.

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

# Use convenience wrappers (v0.3.39+)
fgt.firewall.service_custom.create(
    name="HTTPS-8443",
    tcp_portrange="8443",
    protocol="TCP/UDP/SCTP"
)
```

## API Coverage

**FortiOS 7.6.5 - 100% Coverage:**

- **CMDB API**: 500+ endpoints across 37 categories (addresses, policies, VPN, routing, etc.)
- **Monitor API**: 200+ endpoints across 32 categories (sessions, stats, resources, etc.)
- **Log API**: Complete log reading functionality (traffic, events, threats, etc.)
- **Service API**: All service categories

## Key Features

### 🎯 Complete API Coverage

Access every FortiOS endpoint with clean, Pythonic syntax:

```python
# CMDB (Configuration)
fgt.api.cmdb.firewall.policy.list()
fgt.api.cmdb.system.interface.get(name="port1")
fgt.api.cmdb.router.static.create(...)

# Monitor (Real-time data)
sessions = fgt.api.monitor.firewall.session.list()
resources = fgt.api.monitor.system.resource.get()

# Log (Historical data)
logs = fgt.api.log.disk.traffic.list(filter="dstport==443")
```

### 🎨 Convenience Wrappers

Production-ready wrappers with comprehensive validation:

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
- **Firewall Policies**: `policy` with 150+ parameters

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

- **HTTP/2 Support**: Connection multiplexing for better performance
- **Automatic Retry**: Handles transient failures (429, 500, 502, 503, 504)
- **Circuit Breaker**: Prevents cascade failures with automatic recovery
- **Request Tracking**: Correlation IDs for distributed tracing
- **Validation Framework**: 832 auto-generated validators
- **Type Safety**: Full type hints with IDE autocomplete
- **Structured Logging**: Machine-readable logs for aggregation tools

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

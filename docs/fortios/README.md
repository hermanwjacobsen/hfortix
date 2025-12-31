# HFortix FortiOS Documentation

Complete Python SDK for FortiOS/FortiGate with 100% API coverage (750+ endpoints).

> **⚠️ Version 0.4.0 - BETA STATUS**: Production-ready FortiOS client, but in beta until v1.0 with comprehensive unit tests. **MAJOR release** with modular architecture.

## 📦 Package Overview

`hfortix-fortios` provides comprehensive FortiOS 7.6.5 REST API support:

- **100% API Coverage**: All 77 categories, 750+ endpoints (CMDB, Monitor, Log, Service)
- **Convenience Wrappers**: High-level interfaces for common operations (policies, shapers, schedules, services)
- **Type-Safe**: Full type hints and IDE autocomplete support
- **Async Support**: All endpoints work in both sync and async modes
- **Production-Ready**: Retry logic, circuit breaker, validation, error handling

## 🚀 Quick Start

```python
from hfortix_fortios import FortiOS

# Connect to FortiGate
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    verify=False
)

# Use convenience wrappers (recommended)
fgt.firewall.policy.create(
    name="Allow-Web-Traffic",
    srcintf="internal",
    dstintf="wan1",
    srcaddr="all",
    dstaddr="all",
    service="HTTP",
    action="accept"
)

# Or use direct API access
fgt.api.cmdb.firewall.address.create(
    name="web-server",
    subnet="192.168.1.100/32"
)

# Monitor and logging
status = fgt.api.monitor.system.status.get()
logs = fgt.api.log.disk.traffic.list()
```

## 📚 Documentation Topics

### Getting Started

- **[../SECURITY.md](../SECURITY.md)** - Security best practices and API token setup
- **[ASYNC_GUIDE.md](ASYNC_GUIDE.md)** - Async/await support for concurrent operations
- **[FILTERING_GUIDE.md](FILTERING_GUIDE.md)** - Complete guide to filtering API queries (50+ examples)
- **[PERFORMANCE_TESTING.md](PERFORMANCE_TESTING.md)** - Test your FortiGate and optimize connection settings

### Convenience Wrappers (Recommended)

High-level interfaces that simplify common operations:

- **[wrappers/CONVENIENCE_WRAPPERS.md](wrappers/CONVENIENCE_WRAPPERS.md)** - **START HERE:** Overview of all wrappers with patterns and examples
- **[wrappers/FIREWALL_POLICY_WRAPPER.md](wrappers/FIREWALL_POLICY_WRAPPER.md)** - Firewall policy management (150+ parameters)
- **[wrappers/SHAPER_WRAPPERS.md](wrappers/SHAPER_WRAPPERS.md)** - Traffic shaping (per-IP and traffic shapers)
- **[wrappers/SCHEDULE_WRAPPERS.md](wrappers/SCHEDULE_WRAPPERS.md)** - Schedule management (onetime, recurring, groups)
- **[ERROR_HANDLING_CONFIG.md](ERROR_HANDLING_CONFIG.md)** - Configurable error handling for wrappers

### API Reference

- **[ENDPOINT_METHODS.md](ENDPOINT_METHODS.md)** - Complete method reference for all 750+ endpoints
- **[API_COVERAGE.md](API_COVERAGE.md)** - Detailed API implementation status
- **[VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)** - Using the validation framework (832 validators)

## 🎯 API Coverage

**FortiOS 7.6.5 (December 2025):**

- **CMDB API**: 37/37 categories (100%) - 500+ endpoints ✅
- **Monitor API**: 32/32 categories (100%) - 200+ endpoints ✅
- **Log API**: 5/5 categories (100%) - Log reading ✅
- **Service API**: 3/3 categories (100%) - 21 methods ✅
- **Overall**: 77/77 categories - 750+ endpoints ✅

**Status:** All APIs functional and tested, beta until v1.0 with comprehensive unit tests.

## 📖 Common Use Cases

### Firewall Management

```python
# Create firewall address
fgt.api.cmdb.firewall.address.create(
    name="web-server",
    subnet="192.168.1.100/32",
    comment="Production web server"
)

# Create firewall policy (convenience wrapper)
fgt.firewall.policy.create(
    name="Allow-HTTP",
    srcintf="internal",
    dstintf="wan1",
    srcaddr=["web-server"],  # Automatically normalized to list
    dstaddr="all",
    service="HTTP",
    action="accept",
    status="enable"
)

# Check if policy exists (by ID or name)
if fgt.firewall.policy.exists(policyid="1"):
    print("Policy exists!")
```

### Traffic Shaping

```python
# Create per-IP shaper
fgt.firewall.shaper_per_ip.create(
    name="user-bandwidth-limit",
    max_bandwidth=10000,      # 10 Mbps
    max_concurrent_session=100
)

# Create traffic shaper
fgt.firewall.traffic_shaper.create(
    name="shared-pool",
    guaranteed_bandwidth=50000,  # 50 Mbps
    maximum_bandwidth=100000     # 100 Mbps
)
```

### Schedule Management

```python
# Create recurring schedule
fgt.firewall.schedule_recurring.create(
    name="business-hours",
    day=["monday", "tuesday", "wednesday", "thursday", "friday"],
    start="08:00",
    end="18:00"
)

# Clone schedule with modifications
fgt.firewall.schedule_recurring.clone(
    name="business-hours",
    new_name="extended-hours",
    end="20:00"  # Override end time
)
```

### Monitoring & Logging

```python
# Get system status
status = fgt.api.monitor.system.status.get()
print(f"Hostname: {status['hostname']}")
print(f"Version: {status['version']}")

# Monitor firewall sessions
sessions = fgt.api.monitor.firewall.session.list()

# Read traffic logs
logs = fgt.api.log.disk.traffic.list(
    filter="srcip==192.168.1.100"
)
```

### Async Operations

```python
import asyncio
from hfortix_fortios import FortiOS

async def main():
    async with FortiOS(
        host="192.168.1.99",
        token="your-token",
        mode="async"
    ) as fgt:
        # All operations support await
        addresses = await fgt.api.cmdb.firewall.address.list()
        
        # Concurrent operations
        results = await asyncio.gather(
            fgt.api.monitor.system.status.get(),
            fgt.api.cmdb.firewall.policy.list(),
            fgt.api.cmdb.firewall.address.list()
        )

asyncio.run(main())
```

## 🔗 Related Documentation

- **[Main Documentation](../README.md)** - HFortix documentation index
- **[Core Documentation](../core/README.md)** - Core package documentation
- **[Package README](../../packages/fortios/README.md)** - FortiOS package README
- **[Quick Start Guide](../../QUICKSTART.md)** - Get started in 5 minutes
- **[Examples](../../examples/)** - Working code samples

## 📋 Installation

```bash
# Install FortiOS package (includes core)
pip install hfortix-fortios

# Or install via meta-package
pip install hfortix[fortios]  # FortiOS only
pip install hfortix[all]       # All products

# Legacy install (v0.3.39 and earlier)
pip install hfortix  # Monolithic package
```

## 📝 Status

**Version:** 0.4.0  
**Status:** Beta - All APIs functional and tested, pending comprehensive unit tests for v1.0

**Note:** All implementations remain in beta status until version 1.0.0 with comprehensive unit test coverage.

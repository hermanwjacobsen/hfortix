# HFortix

Complete Python SDK for Fortinet Products - Modular, type-safe, production-ready.

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> **⚠️ BETA STATUS - Version 0.4.0 MAJOR RELEASE**
>
> **Breaking Changes**: Modular architecture introduced. Existing users upgrade with `pip install hfortix[fortios]`
> **Status**: Production-ready but in beta until v1.0 with comprehensive unit tests.

**Version:** 0.4.0
**Status:** Beta (Functional, production-ready, pending comprehensive unit tests for v1.0)

## Overview

HFortix is a modular Python SDK that provides comprehensive, production-ready clients for Fortinet products. Starting with FortiOS/FortiGate, with future support planned for FortiManager, FortiAnalyzer, and more.

This is a **meta-package** that provides convenient installation patterns for the HFortix ecosystem.

## Installation

### Minimal Installation (Core Only)
```bash
pip install hfortix
```
Installs only `hfortix-core` - the shared foundation (exceptions, HTTP client, type definitions).

### FortiOS/FortiGate Support
```bash
pip install hfortix[fortios]
```
Installs `hfortix-core` + `hfortix-fortios` - Everything needed for FortiGate/FortiOS.

### Complete Installation
```bash
pip install hfortix[all]
```
Installs all current and future Fortinet product packages.

### Individual Packages

You can also install product packages directly:

```bash
# Just FortiOS (includes core automatically)
pip install hfortix-fortios

# Just the core framework
pip install hfortix-core
```

## Quick Start

### FortiOS/FortiGate

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

# Manage firewall addresses
fgt.api.cmdb.firewall.address.create(
    name="web-server",
    subnet="192.168.1.100 255.255.255.255"
)

# Use convenience wrappers
fgt.firewall.service_custom.create(
    name="HTTPS-8443",
    tcp_portrange="8443",
    protocol="TCP/UDP/SCTP"
)
```

## Package Structure

HFortix uses a modular architecture:

```text
hfortix (meta-package)
├── hfortix-core          # Shared foundation
│   ├── Exception system (387+ error codes)
│   ├── HTTP client framework
│   ├── Type definitions
│   └── Common utilities
│
└── hfortix-fortios       # FortiOS/FortiGate client
    ├── Complete API coverage (750+ endpoints)
    ├── Convenience wrappers
    ├── Auto-generated validators
    └── Product-specific features
```

**Future Packages:**
- `hfortix-fortimanager` - FortiManager API client
- `hfortix-fortianalyzer` - FortiAnalyzer API client
- `hfortix-fortiswitch` - FortiSwitch API client
- And more...

## Key Features

### 🎯 Modular Design

Install only what you need:
- Minimal footprint with `hfortix-core`
- Product-specific packages when needed
- Shared infrastructure across all products

### ⚡ Complete FortiOS Support

**API Coverage (FortiOS 7.6.5):**
- 500+ CMDB endpoints (configuration)
- 200+ Monitor endpoints (real-time data)
- Complete Log API (historical data)
- All Service categories

**Convenience Wrappers:**
- Service management (`service_custom`, `service_category`, `service_group`)
- Schedules (`schedule_onetime`, `schedule_recurring`, `schedule_group`)
- Traffic shaping (`traffic_shaper`, `shaper_per_ip`)
- IP/MAC binding (`ipmacbinding_table`, `ipmacbinding_setting`)
- Firewall policies (150+ parameters)

### �� Enterprise Features

- **Async/Await Support**: Full async implementation with context managers
- **Error Handling**: 387+ specific error codes with comprehensive exception hierarchy
- **HTTP/2 Support**: Connection multiplexing for better performance
- **Automatic Retry**: Handles transient failures intelligently
- **Circuit Breaker**: Prevents cascade failures with automatic recovery
- **Type Safety**: Full type hints with IDE autocomplete
- **Read-Only Mode**: Safe testing without accidental changes
- **Operation Tracking**: Audit logging for all API calls
- **Performance Testing**: Built-in tools to optimize device communication

## Import Patterns

### Recommended (New in v0.4.0-dev1)
```python
# Product packages
from hfortix_fortios import FortiOS

# Core exceptions
from hfortix_core import (
    APIError,
    ResourceNotFoundError,
    DuplicateEntryError
)
```

### Legacy (Still Supported)
```python
from hfortix import FortiOS
from hfortix.FortiOS import FortiOS
```

## Migration from v0.3.x

**From monolithic package:**
```bash
# Old installation
pip uninstall hfortix

# New installation
pip install hfortix[fortios]  # or hfortix-fortios
```

**Code changes:**
- Update imports to `from hfortix_fortios import FortiOS`
- Legacy imports (`from hfortix import FortiOS`) still work
- No other code changes required

## Documentation

**Getting Started:**
- [Quick Start Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/QUICKSTART.md) - Installation and basic usage
- [Async Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ASYNC_GUIDE.md) - Async/await patterns
- [API Reference](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ENDPOINT_METHODS.md) - Complete method reference

**Convenience Wrappers:**
- [Overview](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/CONVENIENCE_WRAPPERS.md) - All wrappers
- [Service Management](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/CONVENIENCE_WRAPPERS.md#service-management)
- [Schedules](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/SCHEDULE_WRAPPERS.md)
- [Traffic Shaping](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/wrappers/SHAPER_WRAPPERS.md)

**Advanced Topics:**
- [Validation Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/VALIDATION_GUIDE.md) - Using validators
- [Error Handling](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ERROR_HANDLING_CONFIG.md) - Exception system
- [Performance Testing](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/PERFORMANCE_TESTING.md) - Optimization

**Project Info:**
- [Changelog](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) - Version history
- [GitHub Repository](https://github.com/hermanwjacobsen/hfortix) - Complete docs

## Requirements

- Python 3.10+
- FortiOS 7.0+ (tested with 7.6.5)

## Development Status

**Beta** - All APIs are functional and tested against live Fortinet devices. The package remains in beta status until version 1.0.0 with comprehensive unit test coverage.

**Current Test Coverage:**
- 226 test files for FortiOS
- 75%+ pass rate
- ~50% of endpoints have dedicated tests
- All implementations validated against FortiOS 7.6.5

## Why Modular?

**Benefits of the split package architecture:**

1. **Smaller Dependencies**: Install only what you need
2. **Faster Updates**: Product packages can be updated independently
3. **Better Organization**: Clear separation of concerns
4. **Easier Maintenance**: Focused development per product
5. **Future Flexibility**: Easy to add new Fortinet products

## Version History

- **v0.4.0-dev1** (Current): Package split - modular architecture
- **v0.3.39**: Convenience wrappers (services, schedules, shaping, IP/MAC binding)
- **v0.3.38**: Firewall policy wrapper with 150+ parameters
- **v0.3.x**: Async support, error handling, performance tools
- **v0.1.x-v0.2.x**: Initial FortiOS API implementation

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

# HFortix

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Documentation Status](https://readthedocs.org/projects/hfortix/badge/?version=latest)](https://hfortix.readthedocs.io/en/latest/)
[![License](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

**HFortix** is the meta-package that installs all HFortix components for Fortinet automation. Install this package to get the complete suite of tools for FortiOS/FortiGate automation.

## 🚀 Quick Start

```bash
pip install hfortix
```

This single command installs:
- `hfortix-core` - Core infrastructure and utilities
- `hfortix-fortios` - FortiOS/FortiGate API client

```python
from hfortix_fortios import FortiOS

# Connect to your FortiGate
with FortiOS(host="192.168.1.99", token="your-api-token") as fgt:
    # Get system status
    status = fgt.api.monitor.system.status.get()
    print(f"Hostname: {status['hostname']}, Model: {status['model']}")
    
    # Create firewall address
    fgt.api.cmdb.firewall.address.post(
        name="web-server",
        subnet="10.0.1.100/32",
        comment="Production web server"
    )
```

## 📦 What's Included

When you install `hfortix`, you automatically get:

### hfortix-fortios
Complete FortiOS/FortiGate API client with:
- 1,348 FortiOS 7.6.5 endpoints
- Full type hints and IDE autocomplete
- Async/await support
- Batch transactions and atomic operations
- Comprehensive error handling
- Rate limiting and retry logic

### hfortix-core
Foundational infrastructure including:
- Observable HTTP client
- Event-driven monitoring
- Base abstractions and protocols
- Shared utilities

## ✨ Key Features

- **🎯 Complete API Coverage** - All CMDB, Monitor, Log, and Service endpoints
- **💪 Fully Typed** - Complete type hints with .pyi stubs
- **⚡ Modern & Fast** - Async/await support, HTTP/2, connection pooling
- **🛡️ Production Ready** - Comprehensive error handling and validation
- **🔄 Simplified Syntax** - Simple list format auto-converts to FortiOS dict format
- **📦 Batch Transactions** - Atomic configuration changes with automatic commit/rollback
- **🔍 API Inspection** - Debug and audit API interactions

## 📚 Documentation

- **[HFortix Documentation](https://hfortix.readthedocs.io/)** - Getting started and guides
- **[FortiOS Client Docs](https://hfortix-fortios.readthedocs.io/)** - Complete API reference
- **[Core Library Docs](https://hfortix-core.readthedocs.io/)** - Infrastructure details

## 🔗 Individual Packages

If you only need specific components, you can install them separately:

```bash
# Just the FortiOS client (includes hfortix-core as dependency)
pip install hfortix-fortios

# Just the core infrastructure (for custom implementations)
pip install hfortix-core
```

## 🆚 Package Comparison

| Package | Purpose | Dependencies | Use When |
|---------|---------|--------------|----------|
| `hfortix` | Meta-package | All packages | You want everything |
| `hfortix-fortios` | FortiOS API client | hfortix-core | FortiGate automation |
| `hfortix-core` | Core infrastructure | httpx, typing-extensions | Building custom clients |

## 📖 Quick Examples

### Firewall Management
```python
from hfortix_fortios import FortiOS

with FortiOS(host="192.168.1.99", token="token") as fgt:
    # Create firewall policy
    fgt.api.cmdb.firewall.policy.post(
        name="Allow-Web",
        srcintf=["internal"],
        dstintf=["wan1"],
        srcaddr=["all"],
        dstaddr=["web-server"],
        service=["HTTP", "HTTPS"],
        action="accept"
    )
```

### Batch Transactions
```python
from hfortix_fortios import FortiOS

with FortiOS(host="192.168.1.99", token="token") as fgt:
    # Atomic batch operation
    with fgt.transaction() as txn:
        txn.add(fgt.api.cmdb.firewall.address.post, name="server1", subnet="10.0.1.1/32")
        txn.add(fgt.api.cmdb.firewall.address.post, name="server2", subnet="10.0.1.2/32")
        # Both addresses created or both rolled back on error
```

### Async Support
```python
from hfortix_fortios import AsyncFortiOS

async with AsyncFortiOS(host="192.168.1.99", token="token") as fgt:
    status = await fgt.api.monitor.system.status.get()
    addresses = await fgt.api.cmdb.firewall.address.get()
```

## 🤝 Contributing

This is a proprietary library. For support or feature requests, please contact the maintainer.

## 📄 License

Proprietary License - See individual package LICENSE files for details.

---

**HFortix** - Modern Python SDKs for Fortinet automation

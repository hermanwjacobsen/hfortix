# HFortix Core

Core foundation for HFortix - Python SDK for Fortinet products.

[![PyPI version](https://badge.fury.io/py/hfortix-core.svg)](https://pypi.org/project/hfortix-core/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> **⚠️ BETA STATUS - Version 0.4.0**
>
> Production-ready but in beta. All packages remain in beta until v1.0 with comprehensive unit tests.

## Overview

`hfortix-core` provides the shared foundation for all HFortix Fortinet SDKs. It includes exception handling, HTTP client framework, and common utilities used across FortiOS, FortiManager, and FortiAnalyzer clients.

**This package is typically used as a dependency.** For most users, install a product-specific package like `hfortix-fortios` or the meta-package `hfortix[all]`.

## Installation

```bash
pip install hfortix-core
```

## What's Included

### Exception System

Comprehensive exception hierarchy with 387+ FortiOS error codes:

```python
from hfortix_core import (
    FortinetError,      # Base exception
    APIError,           # API-specific errors
    AuthenticationError,
    ResourceNotFoundError,
    DuplicateEntryError,
    # ... and 380+ more
)

try:
    # Your Fortinet API code
    pass
except DuplicateEntryError as e:
    print(f"Object already exists: {e}")
except ResourceNotFoundError as e:
    print(f"Not found: {e}")
except APIError as e:
    print(f"API Error: {e.message} (code: {e.error_code})")
```

**Features:**
- 387+ specific error codes with detailed descriptions
- Intelligent error classification
- Built-in recovery suggestions
- Request correlation tracking

### HTTP Client Framework

Enterprise-grade HTTP client with advanced features:

```python
from hfortix_core import HTTPClient

# Create client
client = HTTPClient(
    url="https://192.168.1.99",
    token="your-api-token",
    verify=False
)

# Features included:
# ✅ HTTP/2 support with connection multiplexing
# ✅ Automatic retry with exponential backoff
# ✅ Circuit breaker pattern (fail-fast protection)
# ✅ Request correlation tracking
# ✅ Configurable timeouts
# ✅ Full async/await support
```

**Enterprise Features:**
- **Automatic Retry**: Handles transient failures (429, 500, 502, 503, 504)
- **Circuit Breaker**: Prevents cascade failures with automatic recovery
- **Connection Pooling**: HTTP/2 multiplexing for better performance
- **Async Support**: Full async/await for high-performance concurrent operations
- **Timeout Control**: Separate connect and read timeouts
- **Request Tracking**: Correlation IDs for distributed tracing

### Type Definitions

Shared type aliases and protocols for type safety:

```python
from hfortix_core import IHTTPClient

# Protocol interface for extensibility
class MyCustomClient:
    def get(self, api_type: str, path: str, **kwargs) -> dict: ...
    def post(self, api_type: str, path: str, data: dict, **kwargs) -> dict: ...
    # ... implement IHTTPClient protocol
```

## When to Use This Package

**Use `hfortix-core` directly if:**
- Building custom Fortinet integrations
- Creating specialized HTTP clients
- Extending exception handling
- Implementing custom protocols

**For most users:**
```bash
# Install FortiOS client (includes core automatically)
pip install hfortix-fortios

# Or install everything
pip install hfortix[all]
```

## Product Packages

This core is used by:
- **hfortix-fortios** - FortiOS/FortiGate API client (750+ endpoints)
- **hfortix-fortimanager** - FortiManager client (planned)
- **hfortix-fortianalyzer** - FortiAnalyzer client (planned)

## Key Features

- 🔒 **Type-Safe**: Full PEP 561 compliance with type hints
- ⚡ **High Performance**: HTTP/2 support with connection pooling
- 🔄 **Resilient**: Automatic retry logic and circuit breaker
- 🎯 **Async Ready**: Full async/await support
- 📊 **Observable**: Request tracking and structured logging
- 🛡️ **Enterprise Grade**: Production-ready reliability features

## Requirements

- Python 3.10+
- httpx[http2] >= 0.27.0

## Documentation

For complete documentation, see the [main repository](https://github.com/hermanwjacobsen/hfortix):

- [Quick Start Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/QUICKSTART.md)
- [API Reference](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ENDPOINT_METHODS.md)
- [Async Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/fortios/ASYNC_GUIDE.md)

## License

Proprietary - See LICENSE file

## Support

- 📖 [Documentation](https://github.com/hermanwjacobsen/hfortix)
- 🐛 [Report Issues](https://github.com/hermanwjacobsen/hfortix/issues)
- 💬 [Discussions](https://github.com/hermanwjacobsen/hfortix/discussions)

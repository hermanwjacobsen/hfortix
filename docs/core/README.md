# HFortix Core Documentation

Core foundation for all HFortix packages - exceptions, HTTP client framework, and shared utilities.

> **⚠️ Version 0.4.0 - BETA STATUS**: Production-ready but in beta until v1.0 with comprehensive unit tests.

## 📦 Package Overview

`hfortix-core` provides the shared foundation used across all HFortix Fortinet SDKs:

- **Exception System**: 387+ FortiOS error codes with intelligent classification
- **HTTP Client Framework**: Sync/async HTTP client with retry logic, circuit breaker, connection pooling
- **Type Definitions**: Shared type hints and protocols for all packages
- **Utilities**: Common helper functions and utilities

## 🎯 Who Should Use This?

**Typical Users:** This package is automatically installed as a dependency of product packages like `hfortix-fortios`. Most users should install a product package instead.

**Advanced Users:** Install this package directly if you're:
- Building custom Fortinet integrations
- Extending HFortix with new product support
- Using only the exception system for error handling

## 📚 Documentation Topics

### Exception System

The core exception hierarchy provides comprehensive error handling:

```python
from hfortix_core import (
    FortinetError,           # Base exception
    APIError,                # API-specific errors
    AuthenticationError,     # Auth failures
    ResourceNotFoundError,   # 404 errors
    DuplicateEntryError,     # Duplicate resource errors
    RetryableError,          # Transient errors that can be retried
    NonRetryableError,       # Permanent errors
)
```

**Features:**
- 387+ specific FortiOS error codes mapped to Python exceptions
- Intelligent retry classification (retryable vs. non-retryable)
- Built-in recovery suggestions for common errors
- Request correlation IDs for distributed tracing
- Rich metadata (http_status, error_code, timestamp, etc.)

**Documentation:**
- Coming soon: `EXCEPTIONS.md` - Complete exception hierarchy and error handling guide

### HTTP Client Framework

Production-grade HTTP client with enterprise features:

**Sync Client:**
```python
from hfortix_core import HTTPClient

client = HTTPClient(
    url="https://192.168.1.99",
    token="your-api-token",
    verify=False
)
```

**Async Client:**
```python
from hfortix_core import HTTPClientAsync

async with HTTPClientAsync(
    url="https://192.168.1.99",
    token="your-api-token",
    verify=False
) as client:
    response = await client.get("monitor", "system/status")
```

**Features:**
- HTTP/2 support with connection multiplexing
- Automatic retry with exponential backoff
- Circuit breaker pattern for fail-fast behavior
- Connection pool health monitoring
- Request correlation tracking
- Per-endpoint custom timeouts
- Structured logging for observability

**Documentation:**
- Coming soon: `HTTP_CLIENT.md` - HTTP client configuration and usage
- Coming soon: `RETRY_LOGIC.md` - Retry mechanisms and circuit breaker patterns

## 🔗 Related Documentation

- **[Main Documentation](../README.md)** - HFortix documentation index
- **[FortiOS Documentation](../fortios/README.md)** - FortiOS package documentation
- **[Package README](../../packages/core/README.md)** - Core package README with installation instructions

## 📋 Installation

```bash
# Install core only (minimal)
pip install hfortix-core

# Or install with a product package (recommended)
pip install hfortix-fortios  # Includes core automatically
pip install hfortix[all]      # Includes all packages
```

## 🤝 Contributing

This is core infrastructure used by all HFortix packages. Changes here affect all products.

**Before modifying:**
- Ensure backward compatibility with all product packages
- Run full test suite across all packages
- Update documentation for breaking changes

## 📝 Status

**Version:** 0.4.0  
**Status:** Beta - Functional and production-ready, pending comprehensive unit tests for v1.0

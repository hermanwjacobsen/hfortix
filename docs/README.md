# HFortix Documentation

Complete reference documentation for the HFortix Python SDK for Fortinet products.

> **⚠️ Version 0.4.0 - BETA STATUS**: All packages functional and production-ready, but remain in beta until v1.0 with comprehensive unit tests.

## 📚 Documentation by Package

### 🔷 Core Framework (`hfortix-core`)
Foundation for all HFortix packages - exceptions, HTTP client, retry logic.

- **[Core Documentation](core/README.md)** - Core package overview and guides

### 🔥 FortiOS/FortiGate (`hfortix-fortios`)
Complete FortiOS 7.6.5 API client with 750+ endpoints and convenience wrappers.

- **[FortiOS Documentation](fortios/README.md)** - FortiOS package overview and guides

## 🚀 Quick Start

- **[Quick Start Guide](../QUICKSTART.md)** - Get started in 5 minutes
- **[Main README](../README.md)** - Project overview and installation

## 🔒 Security & Best Practices

- **[SECURITY.md](SECURITY.md)** - Security best practices, audit results, and compliance guidance

## 📖 Additional Resources

- **[Changelog](../CHANGELOG.md)** - Complete version history
- **[Examples](../examples/)** - Working code samples
- **[Archive](archive/)** - Historical/deprecated documentation

## 📦 Package Status

| Package | Version | Status | PyPI Published |
|---------|---------|--------|----------------|
| `hfortix-core` | 0.4.0 | Beta | ✅ Yes |
| `hfortix-fortios` | 0.4.0 | Beta | ✅ Yes |
| `hfortix` (meta) | 0.4.0 | Beta | ✅ Yes |

**Note**: All packages are in BETA status until version 1.0.0 with comprehensive unit test coverage.
  - Custom services, service categories, service groups
  - Full CRUD operations with rename and clone support
- **Consolidated Documentation**: New comprehensive convenience wrappers guide

## What's New in v0.3.34

- **Schedule Convenience Methods**: Added `get_by_name()`, `rename()`, and `clone()` to all schedule types
- **IP/MAC Binding Modules**: New modules for managing IP/MAC binding settings and table entries
- **Firewall Policy Helpers**: Extracted validation utilities into reusable `_helpers.py` module

## What's New in v0.3.24

- **Error Handling Configuration**: Configurable error handling for convenience wrappers
  - Three error modes: "raise" (default), "return", "print"
  - Three error formats: "detailed" (default), "simple", "code_only"
  - Configure at instance level or override per method call

## What's New in v0.3.21

- **Validation Framework**: 832 auto-generated validators for all API types
- **Builder Pattern**: Centralized payload construction (Phase 1: Firewall Policy)
- **Security Audit**: Comprehensive security review and best practices guide
- **Code Quality**: 100% PEP 8 compliance, type hints, and docstrings

---

**Documentation Status:** ✅ Complete and up-to-date (December 29, 2025)
